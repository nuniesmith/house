"""
Floor plan generation functions.

This module contains functions for loading configuration,
generating floor plans, and exporting to various formats.
"""

import logging
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import yaml
from defaults import (
    BASEMENT_DOORS_DEFAULT,
    BASEMENT_FURNITURE_DEFAULT,
    BASEMENT_POOL_DEFAULT,
    BASEMENT_ROOMS_DEFAULT,
    BASEMENT_STAIRS_DEFAULT,
    BASEMENT_TEXT_ANNOTATIONS_DEFAULT,
    BASEMENT_THEATER_DEFAULT,
    MAIN_FLOOR_DOORS_DEFAULT,
    MAIN_FLOOR_FIREPLACES_DEFAULT,
    MAIN_FLOOR_ROOMS_DEFAULT,
    MAIN_FLOOR_STAIRS_DEFAULT,
    MAIN_FLOOR_WINDOWS_DEFAULT,
)
from drawing import (
    add_dimension_arrow,
    add_line_annotation,
    add_north_arrow,
    add_pool_area,
    add_room_simple,
    add_theater_seating,
    draw_debug_grid,
    draw_doors_from_data,
    draw_fireplaces_from_data,
    draw_furniture_from_data,
    draw_rooms_from_data,
    draw_stairs_from_data,
    draw_text_annotations_from_data,
    draw_windows_from_data,
)
from matplotlib.backends.backend_pdf import PdfPages
from models import FloorPlanSettings, LineAnnotation, PoolConfig, TheaterSeating
from utilities import (
    COLORS,
    get_debug_mode,
    get_grid_spacing,
    scale,
    set_auto_dimensions,
    set_debug_mode,
    set_grid_spacing,
    set_scale,
    update_colors,
    validate_config,
)

logger = logging.getLogger(__name__)

# Output directory (navigate from src/generators/ -> src/ -> python/ -> python/output)
OUTPUT_DIR = Path(__file__).parent.parent.parent / "output"


# =============================================================================
# YAML CONFIGURATION LOADING
# =============================================================================


def load_config(
    config_path: str | Path | None = None, validate: bool = True
) -> dict[str, Any]:
    """
    Load configuration from YAML file.

    Args:
        config_path: Path to YAML config file. If None, uses default location.
        validate: If True, validates config and logs warnings.

    Returns:
        Configuration dictionary

    Raises:
        FileNotFoundError: If config file doesn't exist and no fallback available
        yaml.YAMLError: If YAML parsing fails
    """
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config" / "floor_plan_config.yaml"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        logger.warning(f"Config file not found: {config_path}")
        logger.info("Using built-in default configuration.")
        return get_default_config()

    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML config: {e}")
        logger.info("Using built-in default configuration.")
        return get_default_config()

    if config is None:
        logger.warning("Empty config file, using defaults")
        return get_default_config()

    # Validate configuration
    if validate:
        warnings = validate_config(config)
        for warning in warnings:
            logger.warning(warning)
        if warnings:
            logger.info(f"Config validation complete: {len(warnings)} warning(s)")

    return config


def apply_config_settings(config: dict[str, Any]) -> FloorPlanSettings:
    """
    Apply global settings from configuration.

    Args:
        config: Configuration dictionary

    Returns:
        FloorPlanSettings object with applied settings
    """
    settings = config.get("settings", {})

    # Create settings object for validation
    floor_settings = FloorPlanSettings(
        scale=settings.get("scale", 1.0),
        debug_mode=settings.get("debug_mode", False),
        grid_spacing=settings.get("grid_spacing", 10),
        auto_dimensions=settings.get("auto_dimensions", True),
        output_dpi=settings.get("output_dpi", 300),
        output_format=settings.get("output_format", "png"),
        show_north_arrow=settings.get("show_north_arrow", True),
    )

    # Apply to globals
    set_scale(floor_settings.scale)
    set_debug_mode(floor_settings.debug_mode)
    set_grid_spacing(floor_settings.grid_spacing)
    set_auto_dimensions(floor_settings.auto_dimensions)

    # Update colors from config
    if "colors" in config:
        update_colors(config["colors"])

    return floor_settings


def get_default_config() -> dict[str, Any]:
    """Return default configuration when YAML is not available."""
    return {
        "settings": {
            "scale": 1.0,
            "debug_mode": False,
            "grid_spacing": 10,
            "auto_dimensions": True,
            "output_dpi": 300,
        },
        "colors": COLORS,
        "main_floor": {
            "figure": {
                "width": 16,
                "height": 20,
                "title": "Main Floor Plan",
                "x_min": -32,
                "x_max": 85,
                "y_min": -5,
                "y_max": 120,
            },
            "dimensions": {
                "width_label": "~70'",
                "height_label": "~110'",
            },
            "rooms": MAIN_FLOOR_ROOMS_DEFAULT,
            "doors": MAIN_FLOOR_DOORS_DEFAULT,
            "windows": MAIN_FLOOR_WINDOWS_DEFAULT,
            "fireplaces": MAIN_FLOOR_FIREPLACES_DEFAULT,
            "stairs": MAIN_FLOOR_STAIRS_DEFAULT,
        },
        "basement": {
            "figure": {
                "width": 12,
                "height": 18,
                "title": "Basement Floor Plan (12' Ceilings)",
                "x_min": -5,
                "x_max": 65,
                "y_min": -5,
                "y_max": 105,
            },
            "dimensions": {
                "width_label": "~60'",
                "height_label": "~100'",
            },
            "ceiling_note": {
                "text": "12' Ceilings Throughout",
                "x": 30,
                "y": 102,
            },
            "rooms": BASEMENT_ROOMS_DEFAULT,
            "theater": BASEMENT_THEATER_DEFAULT,
            "pool": BASEMENT_POOL_DEFAULT,
            "doors": BASEMENT_DOORS_DEFAULT,
            "stairs": BASEMENT_STAIRS_DEFAULT,
            "furniture": BASEMENT_FURNITURE_DEFAULT,
            "text_annotations": BASEMENT_TEXT_ANNOTATIONS_DEFAULT,
        },
    }


# =============================================================================
# FLOOR PLAN DRAWING FUNCTIONS
# =============================================================================


def draw_main_floor(ax, config: dict[str, Any]) -> None:
    """Draw the main floor plan on the given axes."""
    main_config = config.get("main_floor", {})
    fig_config = main_config.get("figure", {})
    settings = config.get("settings", {})

    # Draw debug grid if enabled
    if get_debug_mode():
        draw_debug_grid(
            ax,
            fig_config.get("x_min", -32),
            fig_config.get("x_max", 85),
            fig_config.get("y_min", -5),
            fig_config.get("y_max", 120),
            get_grid_spacing(),
        )

    # Draw all rooms from data
    rooms = main_config.get("rooms", MAIN_FLOOR_ROOMS_DEFAULT)
    draw_rooms_from_data(ax, rooms)

    # Draw all doors from data
    doors = main_config.get("doors", MAIN_FLOOR_DOORS_DEFAULT)
    draw_doors_from_data(ax, doors)

    # Draw all windows from data
    windows = main_config.get("windows", MAIN_FLOOR_WINDOWS_DEFAULT)
    draw_windows_from_data(ax, windows)

    # Add fireplaces
    fireplaces = main_config.get("fireplaces", MAIN_FLOOR_FIREPLACES_DEFAULT)
    draw_fireplaces_from_data(ax, fireplaces)

    # Add stairs
    stairs = main_config.get("stairs", MAIN_FLOOR_STAIRS_DEFAULT)
    draw_stairs_from_data(ax, stairs)

    # Add dimension annotations
    dims = main_config.get("dimensions", {})
    add_dimension_arrow(
        ax,
        (scale(-3), scale(0)),
        (scale(-3), scale(110)),
        dims.get("height_label", "~110'"),
        offset=scale(-1),
        rotation=90,
    )
    add_dimension_arrow(
        ax,
        (scale(-27), scale(-3)),
        (scale(70), scale(-3)),
        dims.get("width_label", "~70'"),
        offset=scale(-1),
    )

    # Add north arrow if enabled
    if settings.get("show_north_arrow", False):
        north_config = main_config.get("north_arrow", {})
        add_north_arrow(
            ax,
            north_config.get("x", 75),
            north_config.get("y", 110),
            north_config.get("size", 8),
        )


def draw_basement(ax, config: dict[str, Any]) -> None:
    """Draw the basement floor plan on the given axes."""
    basement_config = config.get("basement", {})
    fig_config = basement_config.get("figure", {})

    # Draw debug grid if enabled
    if get_debug_mode():
        draw_debug_grid(
            ax,
            fig_config.get("x_min", -5),
            fig_config.get("x_max", 65),
            fig_config.get("y_min", -5),
            fig_config.get("y_max", 105),
            get_grid_spacing(),
        )

    # Draw rooms from data
    rooms = basement_config.get("rooms", BASEMENT_ROOMS_DEFAULT)
    draw_rooms_from_data(ax, rooms)

    # ===== Home Theater =====
    theater_config = basement_config.get("theater", BASEMENT_THEATER_DEFAULT)
    theater_room = theater_config.get("room", {})

    # Draw theater room
    add_room_simple(
        ax,
        theater_room.get("x", 25),
        theater_room.get("y", 0),
        theater_room.get("width", 35),
        theater_room.get("height", 15),
        theater_room.get("label", "Home Theater"),
        theater_room.get("color", "theater"),
        theater_room.get("label_fontsize", 11),
        theater_room.get("label_color", "white"),
        theater_room.get("fontweight", "bold"),
        theater_room.get("auto_dimension", True),
        theater_room.get("dimension_text", "30' x 40'"),
    )

    # Theater seating
    seating_config = theater_config.get("seating", {})
    seating = TheaterSeating(
        start_x=seating_config.get("start_x", 28),
        start_y=seating_config.get("start_y", 2),
        rows=seating_config.get("rows", 4),
        seats_per_row=seating_config.get("seats_per_row", 3),
        chair_width=seating_config.get("chair_width", 3),
        chair_height=seating_config.get("chair_height", 2.5),
        row_spacing=seating_config.get("row_spacing", 5),
        seat_spacing=seating_config.get("seat_spacing", 4),
        chair_color=seating_config.get("chair_color", "chair"),
        edge_color=seating_config.get("edge_color", "gray"),
    )
    add_theater_seating(ax, seating)

    # False wall
    false_wall = theater_config.get("false_wall", {})
    line = LineAnnotation(
        x1=false_wall.get("x1", 25),
        y1=false_wall.get("y1", 0),
        x2=false_wall.get("x2", 60),
        y2=false_wall.get("y2", 0),
        color=false_wall.get("color", "red"),
        linewidth=false_wall.get("linewidth", 4),
        linestyle=false_wall.get("linestyle", "--"),
    )
    add_line_annotation(ax, line)
    ax.text(
        scale(false_wall.get("label_x", 42)),
        scale(false_wall.get("label_y", -2)),
        false_wall.get("label", "False Wall"),
        fontsize=8,
        ha="center",
        color="red",
    )

    # ===== Pool Area =====
    pool_config = basement_config.get("pool", BASEMENT_POOL_DEFAULT)
    area = pool_config.get("area", {})
    pool = pool_config.get("pool", {})
    hot_tub = pool_config.get("hot_tub", {})
    spa_label = pool_config.get("spa_label", {})

    pool_data = PoolConfig(
        area_x=area.get("x", 25),
        area_y=area.get("y", 60),
        area_width=area.get("width", 35),
        area_height=area.get("height", 40),
        pool_x=pool.get("x", 28),
        pool_y=pool.get("y", 63),
        pool_width=pool.get("width", 18),
        pool_height=pool.get("height", 32),
        hot_tub_x=hot_tub.get("x", 52),
        hot_tub_y=hot_tub.get("y", 73),
        area_color=area.get("color", "pool_area"),
        area_label=area.get("label", "Pool Area"),
        pool_color=pool.get("color", "pool"),
        pool_edge_color=pool.get("edge_color", "#0288d1"),
        pool_label=pool.get("label", "Salt Water\nPool"),
        hot_tub_radius=hot_tub.get("radius", 4),
        hot_tub_color=hot_tub.get("color", "spa"),
        hot_tub_label=hot_tub.get("label", "Hot\nTub"),
        spa_label_x=spa_label.get("x", 52),
        spa_label_y=spa_label.get("y", 88),
    )
    add_pool_area(ax, pool_data)

    # Draw doors from data
    doors = basement_config.get("doors", BASEMENT_DOORS_DEFAULT)
    draw_doors_from_data(ax, doors)

    # ===== Stairs =====
    stairs = basement_config.get("stairs", BASEMENT_STAIRS_DEFAULT)
    draw_stairs_from_data(ax, stairs)

    # ===== Furniture =====
    furniture = basement_config.get("furniture", BASEMENT_FURNITURE_DEFAULT)
    draw_furniture_from_data(ax, furniture)

    # ===== Text Annotations =====
    annotations = basement_config.get(
        "text_annotations", BASEMENT_TEXT_ANNOTATIONS_DEFAULT
    )
    draw_text_annotations_from_data(ax, annotations)

    # Add dimension annotations
    dims = basement_config.get("dimensions", {})
    fig_x_max = fig_config.get("x_max", 105)
    fig_y_max = fig_config.get("y_max", 65)
    add_dimension_arrow(
        ax,
        (scale(-3), scale(0)),
        (scale(-3), scale(fig_y_max - 5)),
        dims.get("height_label", "~60'"),
        offset=scale(-1),
        rotation=90,
    )
    add_dimension_arrow(
        ax,
        (scale(0), scale(-3)),
        (scale(fig_x_max - 5), scale(-3)),
        dims.get("width_label", "~100'"),
        offset=scale(-1),
    )

    # Ceiling height note
    ceiling_note = basement_config.get("ceiling_note", {})
    ax.text(
        scale(ceiling_note.get("x", 50)),
        scale(ceiling_note.get("y", 62)),
        ceiling_note.get("text", "12' Ceilings Throughout"),
        fontsize=ceiling_note.get("fontsize", 10),
        ha="center",
        style=ceiling_note.get("style", "italic"),
        color=ceiling_note.get("color", "gray"),
    )

    # Add north arrow if enabled
    settings = config.get("settings", {})
    if settings.get("show_north_arrow", False):
        north_config = basement_config.get("north_arrow", {})
        add_north_arrow(
            ax,
            north_config.get("x", 95),
            north_config.get("y", 58),
            north_config.get("size", 6),
        )


# =============================================================================
# GENERATION FUNCTIONS
# =============================================================================


def generate_main_floor(config: dict[str, Any] | None = None) -> Path:
    """Generate the main floor plan."""
    if config is None:
        config = load_config()
        apply_config_settings(config)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    main_config = config.get("main_floor", {})
    fig_config = main_config.get("figure", {})

    fig, ax = plt.subplots(
        figsize=(fig_config.get("width", 16), fig_config.get("height", 20))
    )

    ax.set_xlim(scale(fig_config.get("x_min", -32)), scale(fig_config.get("x_max", 85)))
    ax.set_ylim(scale(fig_config.get("y_min", -5)), scale(fig_config.get("y_max", 120)))
    ax.set_aspect("equal")
    ax.set_title(
        fig_config.get("title", "Main Floor Plan"), fontsize=16, fontweight="bold"
    )

    # Draw the floor plan
    draw_main_floor(ax, config)

    # Remove axes for cleaner look (unless debug mode)
    if not get_debug_mode():
        ax.axis("off")

    output_path = OUTPUT_DIR / "main_floor_plan.png"
    plt.tight_layout()
    plt.savefig(
        output_path,
        dpi=config.get("settings", {}).get("output_dpi", 300),
        bbox_inches="tight",
        facecolor="white",
    )
    print(f"Main floor plan saved to '{output_path}'")
    plt.close()

    return output_path


def generate_basement(config: dict[str, Any] | None = None) -> Path:
    """Generate the basement floor plan."""
    if config is None:
        config = load_config()
        apply_config_settings(config)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    basement_config = config.get("basement", {})
    fig_config = basement_config.get("figure", {})

    fig, ax = plt.subplots(
        figsize=(fig_config.get("width", 12), fig_config.get("height", 18))
    )

    ax.set_xlim(scale(fig_config.get("x_min", -5)), scale(fig_config.get("x_max", 65)))
    ax.set_ylim(scale(fig_config.get("y_min", -5)), scale(fig_config.get("y_max", 105)))
    ax.set_aspect("equal")
    ax.set_title(
        fig_config.get("title", "Basement Floor Plan (12' Ceilings)"),
        fontsize=16,
        fontweight="bold",
    )

    # Draw the floor plan
    draw_basement(ax, config)

    # Remove axes for cleaner look (unless debug mode)
    if not get_debug_mode():
        ax.axis("off")

    output_path = OUTPUT_DIR / "basement_floor_plan.png"
    plt.tight_layout()
    plt.savefig(
        output_path,
        dpi=config.get("settings", {}).get("output_dpi", 300),
        bbox_inches="tight",
        facecolor="white",
    )
    print(f"Basement floor plan saved to '{output_path}'")
    plt.close()

    return output_path


def generate_svg(floor: str = "main", config: dict[str, Any] | None = None) -> Path:
    """
    Generate an SVG file for a floor plan.

    SVG format is ideal for:
    - Scalable vector graphics that don't lose quality when zoomed
    - Editing in tools like Inkscape, Adobe Illustrator
    - Web embedding
    - CAD software import

    Args:
        floor: "main" or "basement"
        config: Configuration dictionary (loaded if None)

    Returns:
        Path to the generated SVG file
    """
    if config is None:
        config = load_config()
        apply_config_settings(config)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if floor == "main":
        floor_config = config.get("main_floor", {})
        fig_config = floor_config.get("figure", {})
        output_path = OUTPUT_DIR / "main_floor_plan.svg"
        draw_func = draw_main_floor
        default_title = "Main Floor Plan"
    else:
        floor_config = config.get("basement", {})
        fig_config = floor_config.get("figure", {})
        output_path = OUTPUT_DIR / "basement_floor_plan.svg"
        draw_func = draw_basement
        default_title = "Basement Floor Plan (12' Ceilings)"

    fig, ax = plt.subplots(
        figsize=(fig_config.get("width", 16), fig_config.get("height", 20))
    )

    ax.set_xlim(scale(fig_config.get("x_min", -32)), scale(fig_config.get("x_max", 85)))
    ax.set_ylim(scale(fig_config.get("y_min", -5)), scale(fig_config.get("y_max", 120)))
    ax.set_aspect("equal")
    ax.set_title(fig_config.get("title", default_title), fontsize=16, fontweight="bold")

    draw_func(ax, config)

    if not get_debug_mode():
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(
        output_path,
        format="svg",
        bbox_inches="tight",
        facecolor="white",
    )
    print(f"{floor.capitalize()} floor plan SVG saved to '{output_path}'")
    plt.close()

    return output_path


def generate_all_svg(config: dict[str, Any] | None = None) -> list[Path]:
    """
    Generate SVG files for all floor plans.

    Args:
        config: Configuration dictionary (loaded if None)

    Returns:
        List of paths to generated SVG files
    """
    if config is None:
        config = load_config()
        apply_config_settings(config)

    paths = []
    paths.append(generate_svg("main", config))
    paths.append(generate_svg("basement", config))
    return paths


def generate_combined_pdf(
    filename: str = "floor_plans.pdf", config: dict[str, Any] | None = None
) -> Path:
    """Generate a multi-page PDF with both floor plans."""
    if config is None:
        config = load_config()
        apply_config_settings(config)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / filename

    with PdfPages(output_path) as pdf:
        # Main floor
        main_config = config.get("main_floor", {})
        fig_config = main_config.get("figure", {})

        fig, ax = plt.subplots(
            figsize=(fig_config.get("width", 16), fig_config.get("height", 20))
        )
        ax.set_xlim(
            scale(fig_config.get("x_min", -32)), scale(fig_config.get("x_max", 85))
        )
        ax.set_ylim(
            scale(fig_config.get("y_min", -5)), scale(fig_config.get("y_max", 120))
        )
        ax.set_aspect("equal")
        ax.set_title(
            fig_config.get("title", "Main Floor Plan"), fontsize=16, fontweight="bold"
        )

        draw_main_floor(ax, config)
        if not get_debug_mode():
            ax.axis("off")

        plt.tight_layout()
        pdf.savefig(fig, bbox_inches="tight", facecolor="white")
        plt.close()

        # Basement floor
        basement_config = config.get("basement", {})
        fig_config = basement_config.get("figure", {})

        fig, ax = plt.subplots(
            figsize=(fig_config.get("width", 12), fig_config.get("height", 18))
        )
        ax.set_xlim(
            scale(fig_config.get("x_min", -5)), scale(fig_config.get("x_max", 65))
        )
        ax.set_ylim(
            scale(fig_config.get("y_min", -5)), scale(fig_config.get("y_max", 105))
        )
        ax.set_aspect("equal")
        ax.set_title(
            fig_config.get("title", "Basement Floor Plan (12' Ceilings)"),
            fontsize=16,
            fontweight="bold",
        )

        draw_basement(ax, config)
        if not get_debug_mode():
            ax.axis("off")

        plt.tight_layout()
        pdf.savefig(fig, bbox_inches="tight", facecolor="white")
        plt.close()

    print(f"Combined floor plans saved to '{output_path}'")
    return output_path


# Export all public functions
__all__ = [
    # Config loading
    "load_config",
    "apply_config_settings",
    "get_default_config",
    # Drawing functions
    "draw_main_floor",
    "draw_basement",
    # Generation functions
    "generate_main_floor",
    "generate_basement",
    "generate_svg",
    "generate_all_svg",
    "generate_combined_pdf",
    # Constants
    "OUTPUT_DIR",
]
