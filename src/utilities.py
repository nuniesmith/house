"""
Utility functions for floor plan generation.

This module contains helper functions for scaling, formatting,
validation, color resolution, and coordinate transformations.

Uses a configuration class instead of global state for better
testability and thread safety.
"""

import logging
from dataclasses import dataclass, field
from typing import Any

from models import FloorPlanSettings, Room

logger = logging.getLogger(__name__)


# =============================================================================
# CONFIGURATION CLASS
# =============================================================================


@dataclass
class DrawingConfig:
    """
    Configuration container for all drawing settings.

    This replaces global state variables with a proper configuration object
    that can be passed around, making the code more testable and thread-safe.
    """

    scale: float = 1.0
    debug_mode: bool = False
    grid_spacing: int = 10
    auto_dimensions: bool = True
    wall_thick: int = 2

    # Drawing styles with defaults
    drawing_styles: dict[str, Any] = field(
        default_factory=lambda: {
            # Door drawing parameters
            "door_arc_linewidth": 1.5,
            "door_panel_linewidth": 1.5,
            # Window drawing parameters
            "window_thickness": 0.8,
            "window_linewidth": 1.5,
            "window_center_linewidth": 0.5,
            # Stairs drawing parameters
            "stairs_linewidth": 1,
            "stairs_step_linewidth": 0.5,
            "stairs_facecolor": "lightgray",
            "stairs_label_fontsize": 7,
            # Fireplace drawing parameters
            "fireplace_linewidth": 1,
            "fireplace_facecolor": "darkgray",
            "fireplace_inner_color": "black",
            "fireplace_label_fontsize": 6,
            # North arrow parameters
            "north_arrow_linewidth": 2,
            "north_arrow_fontsize": 12,
            "north_arrow_circle_radius": 0.8,
            # Dimension arrow parameters
            "dimension_fontsize": 10,
            "dimension_color": "gray",
            # Pool area parameters
            "pool_area_linewidth": 3,
            "pool_linewidth": 2,
            "pool_label_fontsize": 10,
            "pool_area_label_fontsize": 12,
            "hot_tub_label_fontsize": 7,
            "spa_label_fontsize": 8,
            # Theater seating parameters
            "theater_chair_linewidth": 1,
        }
    )

    # Color palette
    colors: dict[str, str] = field(
        default_factory=lambda: {
            # Main floor colors
            "garage": "#e0e0e0",
            "bedroom": "#fffacd",
            "bathroom": "#e6f3ff",
            "kitchen": "#e8f5e9",
            "living": "#fff3e0",
            "dining": "#fce4ec",
            "office": "#f3e5f5",
            "utility": "#f5f5f5",
            "porch": "#c8e6c9",
            "closet": "#fafafa",
            "hall": "#ffffff",
            "powder": "#f0f8ff",
            # Basement colors
            "theater": "#1a1a2e",
            "gaming": "#4a5568",
            "pool": "#63b3ed",
            "pool_area": "#e0f7fa",
            "pool_utilities": "#b0bec5",
            "spa": "#81e6d9",
            "bar": "#c4b5fd",
            "storage": "#d1d5db",
            "bath": "#e6f3ff",
            "books": "#fef3c7",
            # Furniture colors
            "wood": "#8b4513",
            "leather": "#6b5b4f",
            "chair": "#4a4a4a",
            "hammock": "#deb887",
            # Window color
            "window": "#87CEEB",
            # Fixture colors
            "fixture": "#ffffff",
            "tub": "#e6f3ff",
            "toilet": "#ffffff",
            "sink": "#ffffff",
        }
    )

    def apply_scale(self, value: float) -> float:
        """Apply scale factor to a value."""
        return value * self.scale

    def get_style(self, key: str, default: Any = None) -> Any:
        """Get a drawing style value by key."""
        return self.drawing_styles.get(key, default)

    def set_style(self, key: str, value: Any) -> None:
        """Set a drawing style value."""
        self.drawing_styles[key] = value

    def get_color(self, name: str) -> str:
        """Resolve a color name to its hex value."""
        if not name:
            return "#ffffff"
        if name.startswith("#"):
            return name
        return self.colors.get(name, name)

    def update_colors(self, new_colors: dict[str, str]) -> None:
        """Update the color palette with new colors."""
        self.colors.update(new_colors)

    def update_styles(self, new_styles: dict[str, Any]) -> None:
        """Update drawing styles with new values."""
        self.drawing_styles.update(new_styles)

    @classmethod
    def from_settings(cls, settings: FloorPlanSettings) -> "DrawingConfig":
        """Create a DrawingConfig from FloorPlanSettings."""
        return cls(
            scale=settings.scale,
            debug_mode=settings.debug_mode,
            grid_spacing=settings.grid_spacing,
            auto_dimensions=settings.auto_dimensions,
            wall_thick=getattr(settings, "wall_thick", 2),
        )

    def copy(self) -> "DrawingConfig":
        """Create a copy of this configuration."""
        return DrawingConfig(
            scale=self.scale,
            debug_mode=self.debug_mode,
            grid_spacing=self.grid_spacing,
            auto_dimensions=self.auto_dimensions,
            wall_thick=self.wall_thick,
            drawing_styles=self.drawing_styles.copy(),
            colors=self.colors.copy(),
        )


# =============================================================================
# GLOBAL DEFAULT CONFIGURATION
# =============================================================================

_default_config = DrawingConfig()


def get_default_config() -> DrawingConfig:
    """Get the global default configuration."""
    return _default_config


def set_default_config(config: DrawingConfig) -> None:
    """Set the global default configuration."""
    global _default_config
    _default_config = config


# Color palette reference for convenient access
COLORS = _default_config.colors


# =============================================================================
# SCALING AND FORMATTING FUNCTIONS
# =============================================================================


def scale(value: float, config: DrawingConfig | None = None) -> float:
    """
    Apply scale factor to a value.

    Args:
        value: The value to scale
        config: Optional configuration (uses default if not provided)

    Returns:
        Scaled value
    """
    if config is None:
        config = _default_config
    return config.apply_scale(value)


def format_dimension(feet: float, include_inches: bool = True) -> str:
    """
    Format a dimension in feet to a standard display string.

    Args:
        feet: Dimension in feet (can be decimal, e.g., 14.5 = 14'-6")
        include_inches: If True, shows inches; if False, rounds to nearest foot

    Returns:
        Formatted string like "14'-6\"" or "14'"

    Examples:
        >>> format_dimension(14.5)
        '14\\'-6"'
        >>> format_dimension(14.0)
        '14\\'-0"'
        >>> format_dimension(14.25)
        '14\\'-3"'
    """
    whole_feet = int(feet)
    inches = round((feet - whole_feet) * 12)

    if inches == 12:
        whole_feet += 1
        inches = 0

    if include_inches:
        return f"{whole_feet}'-{inches}\""
    else:
        if inches >= 6:
            whole_feet += 1
        return f"{whole_feet}'"


def format_room_dimensions(width: float, height: float) -> str:
    """
    Format room dimensions as "W x H" string.

    Args:
        width: Room width in feet
        height: Room height in feet

    Returns:
        Formatted string like "14'-6\" x 12'-0\""
    """
    return f"{format_dimension(width)} x {format_dimension(height)}"


def calculate_area(width: float, height: float) -> float:
    """
    Calculate room area in square feet.

    Args:
        width: Room width in feet
        height: Room height in feet

    Returns:
        Area in square feet
    """
    return width * height


def format_area(area: float, precision: int = 0) -> str:
    """
    Format an area value with units.

    Args:
        area: Area in square feet
        precision: Decimal places to show

    Returns:
        Formatted string like "150 sq ft" or "150.5 sq ft"
    """
    if precision == 0:
        return f"{int(round(area))} sq ft"
    return f"{area:.{precision}f} sq ft"


# =============================================================================
# COLOR FUNCTIONS
# =============================================================================


def resolve_color(color_name: str, config: DrawingConfig | None = None) -> str:
    """
    Resolve a color name to its hex value, or return as-is if it's already a color.

    Args:
        color_name: Either a hex color string (e.g., "#ff0000") or a named color
                   from the colors dictionary (e.g., "bedroom")
        config: Optional configuration (uses default if not provided)

    Returns:
        Hex color string
    """
    if config is None:
        config = _default_config
    return config.get_color(color_name)


def update_colors(new_colors: dict[str, str], config: DrawingConfig | None = None) -> None:
    """Update the colors dictionary with new colors."""
    if config is None:
        config = _default_config
    config.update_colors(new_colors)


def is_valid_hex_color(color: str) -> bool:
    """
    Check if a string is a valid hex color.

    Args:
        color: String to check

    Returns:
        True if valid hex color (#RGB or #RRGGBB format)
    """
    if not color or not color.startswith("#"):
        return False
    hex_part = color[1:]
    if len(hex_part) not in (3, 6):
        return False
    try:
        int(hex_part, 16)
        return True
    except ValueError:
        return False


def lighten_color(hex_color: str, factor: float = 0.3) -> str:
    """
    Lighten a hex color by a given factor.

    Args:
        hex_color: Hex color string (e.g., "#ff0000")
        factor: Lightening factor (0-1, where 1 is white)

    Returns:
        Lightened hex color
    """
    if not hex_color.startswith("#"):
        return hex_color

    hex_part = hex_color[1:]
    if len(hex_part) == 3:
        hex_part = "".join(c * 2 for c in hex_part)

    try:
        r = int(hex_part[0:2], 16)
        g = int(hex_part[2:4], 16)
        b = int(hex_part[4:6], 16)

        r = int(r + (255 - r) * factor)
        g = int(g + (255 - g) * factor)
        b = int(b + (255 - b) * factor)

        return f"#{r:02x}{g:02x}{b:02x}"
    except ValueError:
        return hex_color


def darken_color(hex_color: str, factor: float = 0.3) -> str:
    """
    Darken a hex color by a given factor.

    Args:
        hex_color: Hex color string (e.g., "#ff0000")
        factor: Darkening factor (0-1, where 1 is black)

    Returns:
        Darkened hex color
    """
    if not hex_color.startswith("#"):
        return hex_color

    hex_part = hex_color[1:]
    if len(hex_part) == 3:
        hex_part = "".join(c * 2 for c in hex_part)

    try:
        r = int(hex_part[0:2], 16)
        g = int(hex_part[2:4], 16)
        b = int(hex_part[4:6], 16)

        r = int(r * (1 - factor))
        g = int(g * (1 - factor))
        b = int(b * (1 - factor))

        return f"#{r:02x}{g:02x}{b:02x}"
    except ValueError:
        return hex_color


# =============================================================================
# COORDINATE TRANSFORMATION FUNCTIONS
# =============================================================================


def rotate_90_cw(
    x: float, y: float, w: float, h: float, max_y: float
) -> tuple[float, float, float, float]:
    """
    Rotate coordinates 90° clockwise.
    Transforms (x, y, w, h) -> (max_y - y - h, x, h, w)

    Args:
        x, y: Origin coordinates
        w, h: Width and height
        max_y: Maximum Y value (canvas height)

    Returns:
        Tuple of (new_x, new_y, new_w, new_h)
    """
    new_x = max_y - y - h
    new_y = x
    new_w = h
    new_h = w
    return (new_x, new_y, new_w, new_h)


def rotate_90_ccw(
    x: float, y: float, w: float, h: float, max_x: float
) -> tuple[float, float, float, float]:
    """
    Rotate coordinates 90° counter-clockwise.
    Transforms (x, y, w, h) -> (y, max_x - x - w, h, w)

    Args:
        x, y: Origin coordinates
        w, h: Width and height
        max_x: Maximum X value (canvas width)

    Returns:
        Tuple of (new_x, new_y, new_w, new_h)
    """
    new_x = y
    new_y = max_x - x - w
    new_w = h
    new_h = w
    return (new_x, new_y, new_w, new_h)


def mirror_horizontal(
    x: float, y: float, w: float, h: float, max_x: float
) -> tuple[float, float, float, float]:
    """
    Mirror coordinates horizontally.

    Args:
        x, y: Origin coordinates
        w, h: Width and height
        max_x: Maximum X value (canvas width)

    Returns:
        Tuple of (new_x, new_y, new_w, new_h)
    """
    return (max_x - x - w, y, w, h)


def mirror_vertical(
    x: float, y: float, w: float, h: float, max_y: float
) -> tuple[float, float, float, float]:
    """
    Mirror coordinates vertically.

    Args:
        x, y: Origin coordinates
        w, h: Width and height
        max_y: Maximum Y value (canvas height)

    Returns:
        Tuple of (new_x, new_y, new_w, new_h)
    """
    return (x, max_y - y - h, w, h)


def translate(x: float, y: float, dx: float, dy: float) -> tuple[float, float]:
    """
    Translate coordinates by a delta.

    Args:
        x, y: Original coordinates
        dx, dy: Translation delta

    Returns:
        Tuple of (new_x, new_y)
    """
    return (x + dx, y + dy)


# =============================================================================
# ROOM UTILITY FUNCTIONS
# =============================================================================


def rooms_adjacent(
    room1: dict[str, float], room2: dict[str, float], tolerance: float = 0.5
) -> bool:
    """
    Check if two rooms share a wall (are adjacent).

    Args:
        room1: Dict with x, y, width, height keys
        room2: Dict with x, y, width, height keys
        tolerance: How close walls need to be to count as shared

    Returns:
        True if rooms share a wall
    """
    r1_right = room1["x"] + room1["width"]
    r1_top = room1["y"] + room1["height"]
    r2_right = room2["x"] + room2["width"]
    r2_top = room2["y"] + room2["height"]

    # Check if room1's right edge touches room2's left edge
    if abs(r1_right - room2["x"]) <= tolerance:
        # Check vertical overlap
        if room1["y"] < r2_top and r1_top > room2["y"]:
            return True

    # Check if room1's left edge touches room2's right edge
    if abs(room1["x"] - r2_right) <= tolerance:
        if room1["y"] < r2_top and r1_top > room2["y"]:
            return True

    # Check if room1's top edge touches room2's bottom edge
    if abs(r1_top - room2["y"]) <= tolerance:
        # Check horizontal overlap
        if room1["x"] < r2_right and r1_right > room2["x"]:
            return True

    # Check if room1's bottom edge touches room2's top edge
    if abs(room1["y"] - r2_top) <= tolerance:
        if room1["x"] < r2_right and r1_right > room2["x"]:
            return True

    return False


def get_shared_wall(
    room1: dict[str, float], room2: dict[str, float], tolerance: float = 0.5
) -> str | None:
    """
    Get the direction of the shared wall between two rooms.

    Args:
        room1: Dict with x, y, width, height keys
        room2: Dict with x, y, width, height keys
        tolerance: How close walls need to be to count as shared

    Returns:
        "right", "left", "top", "bottom" from room1's perspective, or None
    """
    r1_right = room1["x"] + room1["width"]
    r1_top = room1["y"] + room1["height"]
    r2_right = room2["x"] + room2["width"]
    r2_top = room2["y"] + room2["height"]

    if abs(r1_right - room2["x"]) <= tolerance:
        if room1["y"] < r2_top and r1_top > room2["y"]:
            return "right"

    if abs(room1["x"] - r2_right) <= tolerance:
        if room1["y"] < r2_top and r1_top > room2["y"]:
            return "left"

    if abs(r1_top - room2["y"]) <= tolerance:
        if room1["x"] < r2_right and r1_right > room2["x"]:
            return "top"

    if abs(room1["y"] - r2_top) <= tolerance:
        if room1["x"] < r2_right and r1_right > room2["x"]:
            return "bottom"

    return None


def get_total_floor_area(rooms: list[dict]) -> float:
    """
    Calculate total floor area from a list of rooms.

    Note: This is a simple sum and doesn't account for overlapping rooms.

    Args:
        rooms: List of room dictionaries with width and height

    Returns:
        Total area in square feet
    """
    total = 0.0
    for room in rooms:
        if "width" in room and "height" in room:
            total += room["width"] * room["height"]
    return total


def get_bounding_box(rooms: list[dict]) -> tuple[float, float, float, float]:
    """
    Calculate the bounding box of all rooms.

    Args:
        rooms: List of room dictionaries with x, y, width, height

    Returns:
        Tuple of (min_x, min_y, max_x, max_y)
    """
    if not rooms:
        return (0, 0, 0, 0)

    min_x = min(r.get("x", 0) for r in rooms)
    min_y = min(r.get("y", 0) for r in rooms)
    max_x = max(r.get("x", 0) + r.get("width", 0) for r in rooms)
    max_y = max(r.get("y", 0) + r.get("height", 0) for r in rooms)

    return (min_x, min_y, max_x, max_y)


def normalize_room_positions(rooms: list[dict]) -> list[dict]:
    """
    Normalize room positions so the minimum x and y are at origin.

    Args:
        rooms: List of room dictionaries

    Returns:
        New list with normalized positions
    """
    if not rooms:
        return []

    min_x, min_y, _, _ = get_bounding_box(rooms)

    return [
        {**room, "x": room.get("x", 0) - min_x, "y": room.get("y", 0) - min_y} for room in rooms
    ]


# =============================================================================
# CONFIG VALIDATION FUNCTIONS
# =============================================================================


def validate_config(config: dict[str, Any]) -> list[str]:
    """
    Validate the entire configuration and return a list of warnings/errors.

    This helps catch common issues like:
    - Overlapping rooms
    - Invalid dimensions
    - Missing required fields
    - Doors/windows outside room boundaries

    Args:
        config: Configuration dictionary

    Returns:
        List of warning/error messages
    """
    warnings = []

    # Validate settings (check raw values before FloorPlanSettings normalizes them)
    settings = config.get("settings", {})

    # Check for invalid scale before normalization
    raw_scale = settings.get("scale")
    if raw_scale is not None and raw_scale <= 0:
        warnings.append(f"Invalid scale value {raw_scale}, will be normalized to 1.0")

    # Check for invalid grid_spacing before normalization
    raw_grid_spacing = settings.get("grid_spacing")
    if raw_grid_spacing is not None and raw_grid_spacing <= 0:
        warnings.append(f"Invalid grid_spacing value {raw_grid_spacing}, will be normalized to 10")

    floor_settings = FloorPlanSettings(
        **{k: v for k, v in settings.items() if k in FloorPlanSettings.__dataclass_fields__}
    )
    warnings.extend(floor_settings.validate())

    # Validate main floor rooms
    main_floor = config.get("main_floor", {})
    main_rooms = main_floor.get("rooms", [])
    warnings.extend(_validate_rooms(main_rooms, "Main Floor"))

    # Validate basement rooms
    basement = config.get("basement", {})
    basement_rooms = basement.get("rooms", [])
    warnings.extend(_validate_rooms(basement_rooms, "Basement"))

    # Check for potential room overlaps (warning only)
    warnings.extend(_check_room_overlaps(main_rooms, "Main Floor"))
    warnings.extend(_check_room_overlaps(basement_rooms, "Basement"))

    return warnings


def _validate_rooms(rooms_data: list[dict], floor_name: str) -> list[str]:
    """Validate a list of room data dictionaries."""
    warnings = []
    for i, room_data in enumerate(rooms_data):
        try:
            # Check required fields
            required = ["x", "y", "width", "height"]
            missing = [f for f in required if f not in room_data]
            if missing:
                label = room_data.get("label", f"Room {i}")
                warnings.append(f"{floor_name}: '{label}' missing required fields: {missing}")
                continue

            # Check for invalid dimensions before Room normalization
            raw_width = room_data.get("width", 0)
            raw_height = room_data.get("height", 0)
            label = room_data.get("label", f"Room {i}")

            if raw_width <= 0:
                warnings.append(f"{floor_name}: '{label}' has invalid width {raw_width}")
            if raw_height <= 0:
                warnings.append(f"{floor_name}: '{label}' has invalid height {raw_height}")

            room = Room(
                x=room_data.get("x", 0),
                y=room_data.get("y", 0),
                width=raw_width,
                height=raw_height,
                label=label,
            )
            warnings.extend([f"{floor_name}: {w}" for w in room.validate()])
        except (TypeError, ValueError) as e:
            warnings.append(f"{floor_name}: Error validating room {i}: {e}")
    return warnings


def _check_room_overlaps(rooms_data: list[dict], floor_name: str) -> list[str]:
    """Check for significantly overlapping rooms (may be intentional for layering)."""
    warnings = []
    rooms = []
    for room_data in rooms_data:
        if all(k in room_data for k in ["x", "y", "width", "height"]):
            rooms.append(room_data)

    for i, r1 in enumerate(rooms):
        for j, r2 in enumerate(rooms[i + 1 :], i + 1):
            # Check if rooms overlap significantly (more than 50% of smaller room)
            x_overlap = max(
                0,
                min(r1["x"] + r1["width"], r2["x"] + r2["width"]) - max(r1["x"], r2["x"]),
            )
            y_overlap = max(
                0,
                min(r1["y"] + r1["height"], r2["y"] + r2["height"]) - max(r1["y"], r2["y"]),
            )
            overlap_area = x_overlap * y_overlap

            min_area = min(r1["width"] * r1["height"], r2["width"] * r2["height"])
            if min_area > 0 and overlap_area / min_area > 0.5:
                label1 = r1.get("label", f"Room {i}")
                label2 = r2.get("label", f"Room {j}")
                warnings.append(
                    f"{floor_name}: Significant overlap between '{label1}' and '{label2}'"
                )

    return warnings


# =============================================================================
# GLOBAL STATE MANAGEMENT
# =============================================================================


def set_scale(value: float) -> None:
    """Set the global scale factor."""
    _default_config.scale = value


def get_scale() -> float:
    """Get the current global scale factor."""
    return _default_config.scale


def set_debug_mode(value: bool) -> None:
    """Set the global debug mode."""
    _default_config.debug_mode = value


def get_debug_mode() -> bool:
    """Get the current debug mode."""
    return _default_config.debug_mode


def set_grid_spacing(value: int) -> None:
    """Set the global grid spacing."""
    _default_config.grid_spacing = value


def get_grid_spacing() -> int:
    """Get the current grid spacing."""
    return _default_config.grid_spacing


def set_auto_dimensions(value: bool) -> None:
    """Set the global auto dimensions mode."""
    _default_config.auto_dimensions = value


def get_auto_dimensions() -> bool:
    """Get the current auto dimensions mode."""
    return _default_config.auto_dimensions


def set_wall_thick(value: int) -> None:
    """Set the global wall thickness."""
    _default_config.wall_thick = value


def get_wall_thick() -> int:
    """Get the current wall thickness."""
    return _default_config.wall_thick


def update_drawing_styles(styles: dict[str, Any]) -> None:
    """Update the global drawing styles with new values."""
    _default_config.update_styles(styles)


def get_drawing_style(key: str, default: Any = None) -> Any:
    """Get a drawing style value by key."""
    return _default_config.get_style(key, default)


def get_all_drawing_styles() -> dict[str, Any]:
    """Get all drawing styles."""
    return _default_config.drawing_styles.copy()


# Export all public functions and classes (sorted alphabetically)
__all__ = [
    "calculate_area",
    "COLORS",
    "darken_color",
    "DrawingConfig",
    "format_area",
    "format_dimension",
    "format_room_dimensions",
    "get_all_drawing_styles",
    "get_auto_dimensions",
    "get_bounding_box",
    "get_debug_mode",
    "get_default_config",
    "get_drawing_style",
    "get_grid_spacing",
    "get_scale",
    "get_shared_wall",
    "get_total_floor_area",
    "get_wall_thick",
    "is_valid_hex_color",
    "lighten_color",
    "mirror_horizontal",
    "mirror_vertical",
    "normalize_room_positions",
    "resolve_color",
    "rooms_adjacent",
    "rotate_90_ccw",
    "rotate_90_cw",
    "scale",
    "set_auto_dimensions",
    "set_debug_mode",
    "set_default_config",
    "set_grid_spacing",
    "set_scale",
    "set_wall_thick",
    "translate",
    "update_colors",
    "update_drawing_styles",
    "validate_config",
]
