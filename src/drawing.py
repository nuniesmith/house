"""
Drawing functions for floor plan generation.

This module contains all functions for drawing floor plan elements
like rooms, doors, windows, stairs, furniture, annotations, etc.
"""

import logging
from typing import Any, Literal

from matplotlib.axes import Axes
from matplotlib.patches import Arc, Circle, Ellipse, Rectangle

from models import (
    Door,
    Fireplace,
    Furniture,
    LineAnnotation,
    PoolConfig,
    Room,
    Stairs,
    TextAnnotation,
    TheaterSeating,
    Window,
)
from utilities import (
    get_auto_dimensions,
    get_drawing_style,
    get_wall_thick,
    resolve_color,
    scale,
)

logger = logging.getLogger(__name__)


# =============================================================================
# DEBUG FUNCTIONS
# =============================================================================


def draw_debug_grid(
    ax: Axes, x_min: float, x_max: float, y_min: float, y_max: float, spacing: int = 10
) -> None:
    """Draw a debug grid overlay on the axes."""
    # Draw vertical lines
    for x in range(int(x_min), int(x_max) + 1, spacing):
        ax.axvline(x=scale(x), color="#cccccc", linewidth=0.5, linestyle="--", zorder=0)
        ax.text(
            scale(x),
            scale(y_min - 2),
            str(x),
            fontsize=6,
            ha="center",
            color="#999999",
        )

    # Draw horizontal lines
    for y in range(int(y_min), int(y_max) + 1, spacing):
        ax.axhline(y=scale(y), color="#cccccc", linewidth=0.5, linestyle="--", zorder=0)
        ax.text(
            scale(x_min - 2),
            scale(y),
            str(y),
            fontsize=6,
            ha="right",
            va="center",
            color="#999999",
        )


# =============================================================================
# ROOM DRAWING FUNCTIONS
# =============================================================================


def add_room(ax: Axes, room: Room) -> None:
    """Add a room rectangle with label to the plot."""
    x, y, w, h = scale(room.x), scale(room.y), scale(room.width), scale(room.height)
    color = resolve_color(room.color)

    rect = Rectangle((x, y), w, h, linewidth=room.linewidth, edgecolor="black", facecolor=color)
    ax.add_patch(rect)

    # Build label text
    label_parts = [room.label]
    if get_auto_dimensions() and room.auto_dimension and room.dimension_text:
        label_parts.append(room.dimension_text)
    if room.notes:
        label_parts.append(room.notes)

    full_label = "\n".join(filter(None, label_parts))

    ax.text(
        x + w / 2,
        y + h / 2,
        full_label,
        fontsize=room.label_fontsize,
        ha="center",
        va="center",
        color=room.label_color,
        fontweight=room.fontweight,
        wrap=True,
    )


def add_room_simple(
    ax: Axes,
    x: float,
    y: float,
    width: float,
    height: float,
    label: str,
    color: str = "white",
    label_fontsize: int = 8,
    label_color: str = "black",
    fontweight: str = "normal",
    auto_dimension: bool = False,
    dimension_text: str = "",
    notes: str = "",
) -> None:
    """Add a room rectangle with label to the plot (simple function interface)."""
    room = Room(
        x,
        y,
        width,
        height,
        label,
        color,
        label_fontsize,
        label_color,
        fontweight=fontweight,
        auto_dimension=auto_dimension,
        dimension_text=dimension_text,
        notes=notes,
    )
    add_room(ax, room)


# =============================================================================
# DOOR DRAWING FUNCTIONS
# =============================================================================


def add_door(ax: Axes, door: Door) -> None:
    """
    Add a door symbol (arc indicating swing direction).

    The door consists of:
    1. A white gap in the wall (the door opening)
    2. A line representing the door panel
    3. An arc showing the swing direction
    """
    x, y, width = scale(door.x), scale(door.y), scale(door.width)
    direction, swing = door.direction, door.swing

    # Draw the door opening (white gap in wall)
    # Use wall_thick + 1 to ensure the gap fully covers the wall
    door_gap_linewidth = get_wall_thick() + 1
    if direction in ("right", "left"):
        ax.plot(
            [x, x + width],
            [y, y],
            color="white",
            linewidth=door_gap_linewidth,
            zorder=5,
        )
    else:  # up or down
        ax.plot(
            [x, x],
            [y, y + width],
            color="white",
            linewidth=door_gap_linewidth,
            zorder=5,
        )

    # Door swing arc configurations
    # Each config: (arc_center, theta1, theta2, door_line_coords)
    arc_configs = {
        ("right", "up"): ((x, y), 0, 90, ([x, x + width], [y, y])),
        ("right", "down"): ((x, y), 270, 360, ([x, x + width], [y, y])),
        ("left", "up"): ((x + width, y), 90, 180, ([x, x + width], [y, y])),
        ("left", "down"): ((x + width, y), 180, 270, ([x, x + width], [y, y])),
        ("up", "right"): ((x, y), 0, 90, ([x, x], [y, y + width])),
        ("up", "left"): ((x, y + width), 270, 360, ([x, x], [y, y + width])),
        ("down", "right"): ((x, y + width), 270, 360, ([x, x], [y, y + width])),
        ("down", "left"): ((x, y), 90, 180, ([x, x], [y, y + width])),
    }

    config = arc_configs.get((direction, swing))
    arc_linewidth = get_drawing_style("door_arc_linewidth", 1.5)
    panel_linewidth = get_drawing_style("door_panel_linewidth", 1.5)
    if config:
        arc_center, theta1, theta2, line_coords = config
        arc = Arc(
            arc_center,
            width * 2,
            width * 2,
            angle=0,
            theta1=theta1,
            theta2=theta2,
            color="black",
            linewidth=arc_linewidth,
            zorder=6,
        )
        ax.add_patch(arc)
        ax.plot(
            line_coords[0],
            line_coords[1],
            color="black",
            linewidth=panel_linewidth,
            zorder=6,
        )
    else:
        # Fallback: simple arc
        arc = Arc(
            (x, y),
            width * 2,
            width * 2,
            angle=0,
            theta1=0,
            theta2=90,
            color="black",
            linewidth=arc_linewidth,
            zorder=6,
        )
        ax.add_patch(arc)


def add_door_simple(
    ax: Axes,
    x: float,
    y: float,
    width: float,
    direction: Literal["right", "left", "up", "down"] = "right",
    swing: Literal["up", "down", "left", "right"] = "up",
) -> None:
    """Add a door symbol (simple function interface)."""
    door = Door(x, y, width, direction, swing)
    add_door(ax, door)


# =============================================================================
# WINDOW DRAWING FUNCTIONS
# =============================================================================


def add_window(ax: Axes, window: Window) -> None:
    """
    Add a window symbol to the plot.

    Windows are represented as thin rectangles with a line through the middle.
    """
    x, y, width = scale(window.x), scale(window.y), scale(window.width)
    window_color = resolve_color("window")

    # Get configurable style parameters
    window_thickness = get_drawing_style("window_thickness", 0.8)
    window_linewidth = get_drawing_style("window_linewidth", 1.5)
    center_linewidth = get_drawing_style("window_center_linewidth", 0.5)

    if window.orientation == "horizontal":
        # Horizontal window (on top/bottom walls)
        thickness = scale(window_thickness)
        rect = Rectangle(
            (x, y - thickness / 2),
            width,
            thickness,
            linewidth=window_linewidth,
            edgecolor="black",
            facecolor=window_color,
            zorder=7,
        )
        ax.add_patch(rect)
        # Center line
        ax.plot([x, x + width], [y, y], color="black", linewidth=center_linewidth, zorder=8)
    else:
        # Vertical window (on left/right walls)
        thickness = scale(window_thickness)
        rect = Rectangle(
            (x - thickness / 2, y),
            thickness,
            width,
            linewidth=window_linewidth,
            edgecolor="black",
            facecolor=window_color,
            zorder=7,
        )
        ax.add_patch(rect)
        # Center line
        ax.plot([x, x], [y, y + width], color="black", linewidth=center_linewidth, zorder=8)


def add_window_simple(
    ax: Axes,
    x: float,
    y: float,
    width: float,
    orientation: Literal["horizontal", "vertical"] = "horizontal",
) -> None:
    """Add a window symbol (simple function interface)."""
    window = Window(x, y, width, orientation)
    add_window(ax, window)


# =============================================================================
# STAIRS DRAWING FUNCTIONS
# =============================================================================


def add_stairs(ax: Axes, stairs: Stairs) -> None:
    """Add stairs symbol with step lines."""
    x, y = scale(stairs.x), scale(stairs.y)
    width, height = scale(stairs.width), scale(stairs.height)

    # Get configurable style parameters
    stairs_linewidth = get_drawing_style("stairs_linewidth", 1)
    step_linewidth = get_drawing_style("stairs_step_linewidth", 0.5)
    stairs_facecolor = get_drawing_style("stairs_facecolor", "lightgray")
    label_fontsize = get_drawing_style("stairs_label_fontsize", 7)

    rect = Rectangle(
        (x, y),
        width,
        height,
        linewidth=stairs_linewidth,
        edgecolor="black",
        facecolor=stairs_facecolor,
    )
    ax.add_patch(rect)

    if stairs.orientation == "horizontal":
        step_width = width / stairs.num_steps
        for i in range(stairs.num_steps):
            ax.plot(
                [x + i * step_width, x + i * step_width],
                [y, y + height],
                color="black",
                linewidth=step_linewidth,
            )
    else:
        step_height = height / stairs.num_steps
        for i in range(stairs.num_steps):
            ax.plot(
                [x, x + width],
                [y + i * step_height, y + i * step_height],
                color="black",
                linewidth=step_linewidth,
            )

    if stairs.label:
        ax.text(
            x + width / 2,
            y + height / 2,
            stairs.label,
            fontsize=label_fontsize,
            ha="center",
            va="center",
        )


def add_stairs_simple(
    ax: Axes,
    x: float,
    y: float,
    width: float,
    height: float,
    num_steps: int = 8,
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    label: str = "",
) -> None:
    """Add stairs symbol (simple function interface)."""
    stairs = Stairs(x, y, width, height, num_steps, orientation, label)
    add_stairs(ax, stairs)


# =============================================================================
# FIREPLACE DRAWING FUNCTIONS
# =============================================================================


def add_fireplace(ax: Axes, fireplace: Fireplace) -> None:
    """Add fireplace symbol."""
    x, y = scale(fireplace.x), scale(fireplace.y)
    width, height = scale(fireplace.width), scale(fireplace.height)

    # Get configurable style parameters
    fp_linewidth = get_drawing_style("fireplace_linewidth", 1)
    fp_facecolor = get_drawing_style("fireplace_facecolor", "darkgray")
    fp_inner_color = get_drawing_style("fireplace_inner_color", "black")
    label_fontsize = get_drawing_style("fireplace_label_fontsize", 6)

    rect = Rectangle(
        (x, y),
        width,
        height,
        linewidth=fp_linewidth,
        edgecolor="black",
        facecolor=fp_facecolor,
    )
    ax.add_patch(rect)

    # Inner fireplace opening
    inner = Rectangle(
        (x + width * 0.2, y),
        width * 0.6,
        height * 0.7,
        linewidth=fp_linewidth,
        edgecolor="black",
        facecolor=fp_inner_color,
    )
    ax.add_patch(inner)

    if fireplace.label:
        ax.text(
            x + width / 2,
            y + height + scale(1),
            fireplace.label,
            fontsize=label_fontsize,
            ha="center",
        )


def add_fireplace_simple(
    ax: Axes, x: float, y: float, width: float, height: float, label: str = ""
) -> None:
    """Add fireplace symbol (simple function interface)."""
    fp = Fireplace(x, y, width, height, label)
    add_fireplace(ax, fp)


# =============================================================================
# FURNITURE DRAWING FUNCTIONS
# =============================================================================


def add_furniture(ax: Axes, furniture: Furniture) -> None:
    """Add furniture or special element to the plot."""
    x, y = scale(furniture.x), scale(furniture.y)
    width = scale(furniture.width)
    height = scale(furniture.height) if furniture.height else width
    color = resolve_color(furniture.color)
    edge_color = resolve_color(furniture.edge_color)

    if furniture.furniture_type == "rectangle":
        patch = Rectangle(
            (x, y),
            width,
            height,
            linewidth=furniture.linewidth,
            edgecolor=edge_color,
            facecolor=color,
        )
    elif furniture.furniture_type == "circle":
        patch = Circle(
            (x, y),
            width,
            color=color,
            ec=edge_color,
            linewidth=furniture.linewidth,
        )
    elif furniture.furniture_type == "ellipse":
        patch = Ellipse(
            (x, y),
            width,
            height,
            linewidth=furniture.linewidth,
            edgecolor=edge_color,
            facecolor=color,
        )
    else:
        return

    ax.add_patch(patch)

    if furniture.label:
        label_x = x + width / 2 if furniture.furniture_type == "rectangle" else x
        label_y = y + height / 2 if furniture.furniture_type == "rectangle" else y
        ax.text(
            label_x,
            label_y,
            furniture.label,
            fontsize=furniture.label_fontsize,
            ha="center",
            va="center",
            color=furniture.label_color,
            rotation=furniture.rotation,
        )


def add_furniture_simple(
    ax: Axes,
    furniture_type: Literal["rectangle", "circle", "ellipse"],
    x: float,
    y: float,
    width: float,
    height: float = 0,
    color: str = "#8b4513",
    edge_color: str = "black",
    label: str = "",
    label_fontsize: int = 7,
    label_color: str = "black",
    rotation: float = 0,
    linewidth: float = 1,
) -> None:
    """Add furniture (simple function interface)."""
    furniture = Furniture(
        furniture_type,
        x,
        y,
        width,
        height,
        color,
        edge_color,
        label,
        label_fontsize,
        label_color,
        rotation,
        linewidth,
    )
    add_furniture(ax, furniture)


# =============================================================================
# ANNOTATION DRAWING FUNCTIONS
# =============================================================================


def add_text_annotation(ax: Axes, annotation: TextAnnotation) -> None:
    """Add a text annotation to the plot."""
    ax.text(
        scale(annotation.x),
        scale(annotation.y),
        annotation.text,
        fontsize=annotation.fontsize,
        color=annotation.color,
        ha=annotation.ha,
        va=annotation.va,
        rotation=annotation.rotation,
        fontweight=annotation.fontweight,
        style=annotation.style,
    )


def add_line_annotation(ax: Axes, line: LineAnnotation) -> None:
    """Add a line annotation to the plot."""
    ax.plot(
        [scale(line.x1), scale(line.x2)],
        [scale(line.y1), scale(line.y2)],
        color=line.color,
        linewidth=line.linewidth,
        linestyle=line.linestyle,
        zorder=line.zorder,
    )


def add_dimension_arrow(
    ax: Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    label: str,
    offset: float = 0,
    rotation: float = 0,
) -> None:
    """Add a dimension arrow with label."""
    # Get configurable style parameters
    dim_fontsize = get_drawing_style("dimension_fontsize", 10)
    dim_color = get_drawing_style("dimension_color", "gray")

    ax.annotate(
        "",
        xy=start,
        xytext=end,
        arrowprops={"arrowstyle": "<->", "color": dim_color},
    )
    mid_x = (start[0] + end[0]) / 2 + offset
    mid_y = (start[1] + end[1]) / 2 + offset
    ax.text(
        mid_x,
        mid_y,
        label,
        ha="center",
        fontsize=dim_fontsize,
        color=dim_color,
        rotation=rotation,
    )


def add_north_arrow(ax: Axes, x: float, y: float, size: float = 5) -> None:
    """Add a north arrow indicator to the plot."""
    cx, cy = scale(x), scale(y)
    arrow_size = scale(size)

    # Get configurable style parameters
    arrow_linewidth = get_drawing_style("north_arrow_linewidth", 2)
    arrow_fontsize = get_drawing_style("north_arrow_fontsize", 12)
    circle_radius = get_drawing_style("north_arrow_circle_radius", 0.8)

    # Draw the arrow pointing up (north)
    ax.annotate(
        "",
        xy=(cx, cy + arrow_size),
        xytext=(cx, cy),
        arrowprops={
            "arrowstyle": "->",
            "color": "black",
            "lw": arrow_linewidth,
        },
    )

    # Draw "N" label above the arrow
    ax.text(
        cx,
        cy + arrow_size + scale(1.5),
        "N",
        fontsize=arrow_fontsize,
        fontweight="bold",
        ha="center",
        va="bottom",
        color="black",
    )

    # Draw a small circle at the base
    base_circle = Circle(
        (cx, cy),
        scale(circle_radius),
        facecolor="white",
        edgecolor="black",
        linewidth=1.5,
        zorder=10,
    )
    ax.add_patch(base_circle)


# =============================================================================
# SPECIAL ELEMENT DRAWING FUNCTIONS
# =============================================================================


def add_theater_seating(ax: Axes, seating: TheaterSeating) -> None:
    """Add theater seating rows."""
    chair_color = resolve_color(seating.chair_color)
    edge_color = resolve_color(seating.edge_color)

    # Get configurable style parameters
    chair_linewidth = get_drawing_style("theater_chair_linewidth", 1)

    for row in range(seating.rows):
        x_pos = scale(seating.start_x + row * seating.row_spacing)
        for seat in range(seating.seats_per_row):
            y_pos = scale(seating.start_y + seat * seating.seat_spacing)
            chair = Rectangle(
                (x_pos, y_pos),
                scale(seating.chair_width),
                scale(seating.chair_height),
                linewidth=chair_linewidth,
                edgecolor=edge_color,
                facecolor=chair_color,
            )
            ax.add_patch(chair)


def add_pool_area(ax: Axes, pool_config: PoolConfig) -> None:
    """Add pool area with pool and hot tub."""
    area_color = resolve_color(pool_config.area_color)
    pool_color = resolve_color(pool_config.pool_color)
    hot_tub_color = resolve_color(pool_config.hot_tub_color)

    # Get configurable style parameters
    pool_area_linewidth = get_drawing_style("pool_area_linewidth", 3)
    pool_linewidth = get_drawing_style("pool_linewidth", 2)
    pool_label_fontsize = get_drawing_style("pool_label_fontsize", 10)
    pool_area_label_fontsize = get_drawing_style("pool_area_label_fontsize", 12)
    hot_tub_label_fontsize = get_drawing_style("hot_tub_label_fontsize", 7)
    spa_label_fontsize = get_drawing_style("spa_label_fontsize", 8)

    # Pool area background
    pool_area = Rectangle(
        (scale(pool_config.area_x), scale(pool_config.area_y)),
        scale(pool_config.area_width),
        scale(pool_config.area_height),
        linewidth=pool_area_linewidth,
        edgecolor="black",
        facecolor=area_color,
    )
    ax.add_patch(pool_area)
    ax.text(
        scale(pool_config.area_x + pool_config.area_width / 2),
        scale(pool_config.area_y + pool_config.area_height - 3),
        pool_config.area_label,
        fontsize=pool_area_label_fontsize,
        ha="center",
        fontweight="bold",
    )

    # Pool itself
    pool = Rectangle(
        (scale(pool_config.pool_x), scale(pool_config.pool_y)),
        scale(pool_config.pool_width),
        scale(pool_config.pool_height),
        linewidth=pool_linewidth,
        edgecolor=pool_config.pool_edge_color,
        facecolor=pool_color,
    )
    ax.add_patch(pool)
    ax.text(
        scale(pool_config.pool_x + pool_config.pool_width / 2),
        scale(pool_config.pool_y + pool_config.pool_height / 2),
        pool_config.pool_label,
        fontsize=pool_label_fontsize,
        ha="center",
        color="white",
        fontweight="bold",
    )

    # Hot tub
    if pool_config.hot_tub_radius > 0:
        hot_tub = Circle(
            (scale(pool_config.hot_tub_x), scale(pool_config.hot_tub_y)),
            scale(pool_config.hot_tub_radius),
            color=hot_tub_color,
            ec=pool_config.pool_edge_color,
            linewidth=pool_linewidth,
        )
        ax.add_patch(hot_tub)
        ax.text(
            scale(pool_config.hot_tub_x),
            scale(pool_config.hot_tub_y),
            pool_config.hot_tub_label,
            fontsize=hot_tub_label_fontsize,
            ha="center",
        )
        # Spa label
        if pool_config.spa_label_x and pool_config.spa_label_y:
            ax.text(
                scale(pool_config.spa_label_x),
                scale(pool_config.spa_label_y),
                "Spa",
                fontsize=spa_label_fontsize,
                ha="center",
            )


# =============================================================================
# BATCH DRAWING FUNCTIONS
# =============================================================================


def draw_rooms_from_data(ax: Axes, rooms_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple rooms from a list of room data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        rooms_data: List of room configuration dictionaries

    Returns:
        Number of rooms successfully drawn
    """
    drawn = 0
    for i, room_data in enumerate(rooms_data):
        try:
            # Resolve color name to hex
            room_dict = room_data.copy()
            if "color" in room_dict:
                room_dict["color"] = resolve_color(room_dict["color"])

            # Filter out any unexpected keys
            valid_keys = {f.name for f in Room.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in room_dict.items() if k in valid_keys}

            room = Room(**filtered_data)
            add_room(ax, room)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping room {i} due to error: {e}")
    return drawn


def draw_doors_from_data(ax: Axes, doors_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple doors from a list of door data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        doors_data: List of door configuration dictionaries

    Returns:
        Number of doors successfully drawn
    """
    drawn = 0
    for i, door_data in enumerate(doors_data):
        try:
            valid_keys = {f.name for f in Door.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in door_data.items() if k in valid_keys}
            door = Door(**filtered_data)
            add_door(ax, door)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping door {i} due to error: {e}")
    return drawn


def draw_windows_from_data(ax: Axes, windows_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple windows from a list of window data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        windows_data: List of window configuration dictionaries

    Returns:
        Number of windows successfully drawn
    """
    drawn = 0
    for i, window_data in enumerate(windows_data):
        try:
            valid_keys = {f.name for f in Window.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in window_data.items() if k in valid_keys}
            window = Window(**filtered_data)
            add_window(ax, window)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping window {i} due to error: {e}")
    return drawn


def draw_furniture_from_data(ax: Axes, furniture_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple furniture items from a list of furniture data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        furniture_data: List of furniture configuration dictionaries

    Returns:
        Number of furniture items successfully drawn
    """
    drawn = 0
    for i, item_data in enumerate(furniture_data):
        try:
            item_dict = item_data.copy()
            # Map 'type' to 'furniture_type' if needed (YAML uses 'type' for cleaner syntax)
            if "type" in item_dict and "furniture_type" not in item_dict:
                item_dict["furniture_type"] = item_dict.pop("type")

            valid_keys = {f.name for f in Furniture.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in item_dict.items() if k in valid_keys}

            furniture = Furniture(**filtered_data)
            add_furniture(ax, furniture)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping furniture {i} due to error: {e}")
    return drawn


def draw_stairs_from_data(ax: Axes, stairs_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple stairs from a list of stairs data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        stairs_data: List of stairs configuration dictionaries

    Returns:
        Number of stairs successfully drawn
    """
    drawn = 0
    for i, stair_data in enumerate(stairs_data):
        try:
            valid_keys = {f.name for f in Stairs.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in stair_data.items() if k in valid_keys}
            stairs = Stairs(**filtered_data)
            add_stairs(ax, stairs)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping stairs {i} due to error: {e}")
    return drawn


def draw_fireplaces_from_data(ax: Axes, fireplaces_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple fireplaces from a list of fireplace data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        fireplaces_data: List of fireplace configuration dictionaries

    Returns:
        Number of fireplaces successfully drawn
    """
    drawn = 0
    for i, fp_data in enumerate(fireplaces_data):
        try:
            valid_keys = {f.name for f in Fireplace.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in fp_data.items() if k in valid_keys}
            fireplace = Fireplace(**filtered_data)
            add_fireplace(ax, fireplace)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping fireplace {i} due to error: {e}")
    return drawn


def draw_text_annotations_from_data(ax: Axes, annotations_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple text annotations from a list of annotation data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        annotations_data: List of annotation configuration dictionaries

    Returns:
        Number of annotations successfully drawn
    """
    drawn = 0
    for i, annotation_data in enumerate(annotations_data):
        try:
            valid_keys = {f.name for f in TextAnnotation.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in annotation_data.items() if k in valid_keys}
            annotation = TextAnnotation(**filtered_data)
            add_text_annotation(ax, annotation)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping text annotation {i} due to error: {e}")
    return drawn


def draw_lines_from_data(ax: Axes, lines_data: list[dict[str, Any]]) -> int:
    """
    Draw multiple lines from a list of line data dictionaries.

    Args:
        ax: Matplotlib axes to draw on
        lines_data: List of line configuration dictionaries

    Returns:
        Number of lines successfully drawn
    """
    drawn = 0
    for i, line_data in enumerate(lines_data):
        try:
            valid_keys = {f.name for f in LineAnnotation.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in line_data.items() if k in valid_keys}
            line = LineAnnotation(**filtered_data)
            add_line_annotation(ax, line)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping line annotation {i} due to error: {e}")
    return drawn


# Export all drawing functions (sorted alphabetically)
__all__ = [
    "add_dimension_arrow",
    "add_door",
    "add_door_simple",
    "add_fireplace",
    "add_fireplace_simple",
    "add_furniture",
    "add_furniture_simple",
    "add_line_annotation",
    "add_north_arrow",
    "add_pool_area",
    "add_room",
    "add_room_simple",
    "add_stairs",
    "add_stairs_simple",
    "add_text_annotation",
    "add_theater_seating",
    "add_window",
    "add_window_simple",
    "draw_debug_grid",
    "draw_doors_from_data",
    "draw_fireplaces_from_data",
    "draw_furniture_from_data",
    "draw_lines_from_data",
    "draw_rooms_from_data",
    "draw_stairs_from_data",
    "draw_text_annotations_from_data",
    "draw_windows_from_data",
]
