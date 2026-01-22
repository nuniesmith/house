"""
Utility functions for floor plan generation.

This module contains helper functions for scaling, formatting,
validation, color resolution, and coordinate transformations.
"""

import logging
from typing import Any

from models import FloorPlanSettings, Room

logger = logging.getLogger(__name__)

# Global state variables (set by config)
SCALE = 1.0
DEBUG_MODE = False
GRID_SPACING = 10
AUTO_DIMENSIONS = True

# Global color scheme for all floor plans
COLORS = {
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


# =============================================================================
# SCALING AND FORMATTING FUNCTIONS
# =============================================================================


def scale(value: float) -> float:
    """Apply global scale factor to a value."""
    return value * SCALE


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


# =============================================================================
# COLOR FUNCTIONS
# =============================================================================


def resolve_color(color_name: str) -> str:
    """
    Resolve a color name to its hex value, or return as-is if it's already a color.

    Args:
        color_name: Either a hex color string (e.g., "#ff0000") or a named color
                   from the COLORS dictionary (e.g., "bedroom")

    Returns:
        Hex color string
    """
    if not color_name:
        return "#ffffff"
    if color_name.startswith("#"):
        return color_name
    resolved = COLORS.get(color_name, color_name)
    # Log warning if color not found and doesn't look like a valid color
    if (
        resolved == color_name
        and not color_name.startswith("#")
        and color_name
        not in ["black", "white", "gray", "red", "blue", "green", "brown", "orange"]
    ):
        logger.debug(f"Color '{color_name}' not in palette, using as-is")
    return resolved


def update_colors(new_colors: dict[str, str]) -> None:
    """Update the global COLORS dictionary with new colors."""
    global COLORS
    COLORS.update(new_colors)


# =============================================================================
# COORDINATE TRANSFORMATION FUNCTIONS
# =============================================================================


def rotate_90_cw(
    x: float, y: float, w: float, h: float, max_y: float
) -> tuple[float, float, float, float]:
    """
    Rotate coordinates 90° clockwise.
    Transforms (x, y, w, h) -> (max_y - y - h, x, h, w)
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
    """
    new_x = y
    new_y = max_x - x - w
    new_w = h
    new_h = w
    return (new_x, new_y, new_w, new_h)


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
    """
    warnings = []

    # Validate settings
    settings = config.get("settings", {})
    floor_settings = FloorPlanSettings(
        **{
            k: v
            for k, v in settings.items()
            if k in FloorPlanSettings.__dataclass_fields__
        }
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
                warnings.append(
                    f"{floor_name}: '{label}' missing required fields: {missing}"
                )
                continue

            room = Room(
                x=room_data.get("x", 0),
                y=room_data.get("y", 0),
                width=room_data.get("width", 0),
                height=room_data.get("height", 0),
                label=room_data.get("label", f"Room {i}"),
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
                min(r1["x"] + r1["width"], r2["x"] + r2["width"])
                - max(r1["x"], r2["x"]),
            )
            y_overlap = max(
                0,
                min(r1["y"] + r1["height"], r2["y"] + r2["height"])
                - max(r1["y"], r2["y"]),
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
    global SCALE
    SCALE = value


def get_scale() -> float:
    """Get the current global scale factor."""
    return SCALE


def set_debug_mode(value: bool) -> None:
    """Set the global debug mode."""
    global DEBUG_MODE
    DEBUG_MODE = value


def get_debug_mode() -> bool:
    """Get the current debug mode."""
    return DEBUG_MODE


def set_grid_spacing(value: int) -> None:
    """Set the global grid spacing."""
    global GRID_SPACING
    GRID_SPACING = value


def get_grid_spacing() -> int:
    """Get the current grid spacing."""
    return GRID_SPACING


def set_auto_dimensions(value: bool) -> None:
    """Set the global auto dimensions mode."""
    global AUTO_DIMENSIONS
    AUTO_DIMENSIONS = value


def get_auto_dimensions() -> bool:
    """Get the current auto dimensions mode."""
    return AUTO_DIMENSIONS


# Export all public functions
__all__ = [
    # Constants
    "COLORS",
    # Scaling and formatting
    "scale",
    "format_dimension",
    "format_room_dimensions",
    "calculate_area",
    # Color functions
    "resolve_color",
    "update_colors",
    # Coordinate transformations
    "rotate_90_cw",
    "rotate_90_ccw",
    # Room utilities
    "rooms_adjacent",
    "get_total_floor_area",
    # Validation
    "validate_config",
    # Global state management
    "set_scale",
    "get_scale",
    "set_debug_mode",
    "get_debug_mode",
    "set_grid_spacing",
    "get_grid_spacing",
    "set_auto_dimensions",
    "get_auto_dimensions",
]
