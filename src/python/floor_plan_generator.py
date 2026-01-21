#!/usr/bin/env python3
"""
Floor Plan Generator for House
Generates floor plan images for Main Floor and Basement levels using matplotlib.

Output files are saved to the 'output/' directory.

Features:
- YAML configuration file for easy editing
- Data-driven room definitions for easy modification
- Data-driven special elements (theater, pool, furniture)
- Scale factor for resizing
- Rotation helper functions
- Improved door swing logic
- Window support
- Multi-page PDF output option
- Reusable drawing functions to eliminate duplication
- Debug grid mode for development
- Auto-dimensioning for rooms
- Config validation for early error detection
"""

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Arc, Circle, Ellipse, Rectangle

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Try to import yaml, with fallback
try:
    import yaml

    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    print("Warning: PyYAML not installed. Using built-in configuration.")

# Global scale factor for easy resizing
SCALE = 1.0

# Output directory
OUTPUT_DIR = Path(__file__).parent / "output"

# Global debug mode
DEBUG_MODE = False
GRID_SPACING = 10

# Global auto-dimensions mode
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
    # Basement colors
    "theater": "#1a1a2e",
    "gaming": "#4a5568",
    "pool": "#63b3ed",
    "pool_area": "#e0f7fa",
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
}


# =============================================================================
# DATA CLASSES
# =============================================================================


@dataclass
class FloorPlanSettings:
    """Global settings for floor plan generation."""

    scale: float = 1.0
    debug_mode: bool = False
    grid_spacing: int = 10
    auto_dimensions: bool = True
    output_dpi: int = 300
    output_format: str = "png"
    show_north_arrow: bool = True

    def validate(self) -> list[str]:
        """Validate settings and return list of warnings."""
        warnings = []
        if self.scale <= 0:
            warnings.append(f"Invalid scale {self.scale}, using 1.0")
            self.scale = 1.0
        if self.grid_spacing <= 0:
            warnings.append(f"Invalid grid_spacing {self.grid_spacing}, using 10")
            self.grid_spacing = 10
        if self.output_dpi < 72:
            warnings.append(f"Low DPI {self.output_dpi} may result in poor quality")
        return warnings


@dataclass
class Room:
    """Data class for room definition."""

    x: float
    y: float
    width: float
    height: float
    label: str
    color: str = "white"
    label_fontsize: int = 8
    label_color: str = "black"
    linewidth: int = 2
    fontweight: str = "normal"
    auto_dimension: bool = False
    dimension_text: str = ""
    notes: str = ""

    def validate(self) -> list[str]:
        """Validate room dimensions and return list of warnings."""
        warnings = []
        if self.width <= 0:
            warnings.append(f"Room '{self.label}' has invalid width: {self.width}")
        if self.height <= 0:
            warnings.append(f"Room '{self.label}' has invalid height: {self.height}")
        return warnings

    @property
    def center(self) -> tuple[float, float]:
        """Return the center point of the room."""
        return (self.x + self.width / 2, self.y + self.height / 2)

    @property
    def bounds(self) -> tuple[float, float, float, float]:
        """Return (x_min, y_min, x_max, y_max) bounds."""
        return (self.x, self.y, self.x + self.width, self.y + self.height)


@dataclass
class Door:
    """Data class for door definition."""

    x: float
    y: float
    width: float
    direction: Literal["right", "left", "up", "down"] = "right"
    swing: Literal["up", "down", "left", "right"] = "up"

    def validate(self) -> list[str]:
        """Validate door dimensions."""
        warnings = []
        if self.width <= 0:
            warnings.append(
                f"Door at ({self.x}, {self.y}) has invalid width: {self.width}"
            )
        if self.width > 8:
            warnings.append(
                f"Door at ({self.x}, {self.y}) seems unusually wide: {self.width}'"
            )
        return warnings


@dataclass
class Window:
    """Data class for window definition."""

    x: float
    y: float
    width: float
    orientation: Literal["horizontal", "vertical"] = "horizontal"

    def validate(self) -> list[str]:
        """Validate window dimensions."""
        warnings = []
        if self.width <= 0:
            warnings.append(
                f"Window at ({self.x}, {self.y}) has invalid width: {self.width}"
            )
        return warnings


@dataclass
class Stairs:
    """Data class for stairs definition."""

    x: float
    y: float
    width: float
    height: float
    num_steps: int = 8
    orientation: Literal["horizontal", "vertical"] = "horizontal"
    label: str = ""


@dataclass
class Fireplace:
    """Data class for fireplace definition."""

    x: float
    y: float
    width: float
    height: float
    label: str = ""


@dataclass
class Furniture:
    """Data class for furniture/special elements."""

    furniture_type: Literal["rectangle", "circle", "ellipse"]
    x: float
    y: float
    width: float
    height: float = 0  # For circles, this is ignored; for ellipse, it's the second axis
    color: str = "#8b4513"
    edge_color: str = "black"
    label: str = ""
    label_fontsize: int = 7
    label_color: str = "black"
    rotation: float = 0
    linewidth: float = 1


@dataclass
class TextAnnotation:
    """Data class for text annotations."""

    x: float
    y: float
    text: str
    fontsize: int = 8
    color: str = "black"
    ha: str = "center"
    va: str = "center"
    rotation: float = 0
    fontweight: str = "normal"
    style: str = "normal"


@dataclass
class LineAnnotation:
    """Data class for line annotations."""

    x1: float
    y1: float
    x2: float
    y2: float
    color: str = "black"
    linewidth: float = 2
    linestyle: str = "-"
    zorder: int = 5


@dataclass
class TheaterSeating:
    """Data class for theater seating configuration."""

    start_x: float
    start_y: float
    rows: int = 4
    seats_per_row: int = 5
    chair_width: float = 4
    chair_height: float = 3
    row_spacing: float = 6
    seat_spacing: float = 5
    chair_color: str = "#4a4a4a"
    edge_color: str = "gray"


@dataclass
class PoolConfig:
    """Data class for pool configuration."""

    # Pool area (outer bounds) - required fields first
    area_x: float
    area_y: float
    area_width: float
    area_height: float
    # Pool itself - required fields
    pool_x: float
    pool_y: float
    pool_width: float
    pool_height: float
    # Hot tub position - required fields
    hot_tub_x: float
    hot_tub_y: float
    # Optional fields with defaults
    area_color: str = "#e0f7fa"
    area_label: str = "Pool Area"
    pool_color: str = "#63b3ed"
    pool_edge_color: str = "#0288d1"
    pool_label: str = "Salt Water\nPool"
    hot_tub_radius: float = 4
    hot_tub_color: str = "#81e6d9"
    hot_tub_label: str = "Hot\nTub"
    spa_label_x: float = 0
    spa_label_y: float = 0


# =============================================================================
# CONFIG VALIDATION
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
# HELPER FUNCTIONS
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
        '14\'-6"'
        >>> format_dimension(14.0)
        '14\'-0"'
        >>> format_dimension(14.25)
        '14\'-3"'
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
        not in ["black", "white", "gray", "red", "blue", "green", "brown"]
    ):
        logger.debug(f"Color '{color_name}' not in palette, using as-is")
    return resolved


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
# DRAWING FUNCTIONS
# =============================================================================


def draw_debug_grid(ax, x_min, x_max, y_min, y_max, spacing=10):
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


def add_room(ax, room: Room):
    """Add a room rectangle with label to the plot."""
    x, y, w, h = scale(room.x), scale(room.y), scale(room.width), scale(room.height)
    color = resolve_color(room.color)

    rect = Rectangle(
        (x, y), w, h, linewidth=room.linewidth, edgecolor="black", facecolor=color
    )
    ax.add_patch(rect)

    # Build label text
    label_parts = [room.label]
    if AUTO_DIMENSIONS and room.auto_dimension and room.dimension_text:
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
    ax,
    x,
    y,
    width,
    height,
    label,
    color="white",
    label_fontsize=8,
    label_color="black",
    fontweight="normal",
    auto_dimension=False,
    dimension_text="",
    notes="",
):
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


def add_door(ax, door: Door):
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
    if direction in ("right", "left"):
        ax.plot([x, x + width], [y, y], color="white", linewidth=4, zorder=5)
    else:  # up or down
        ax.plot([x, x], [y, y + width], color="white", linewidth=4, zorder=5)

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
            linewidth=1.5,
            zorder=6,
        )
        ax.add_patch(arc)
        ax.plot(line_coords[0], line_coords[1], color="black", linewidth=1.5, zorder=6)
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
            linewidth=1.5,
            zorder=6,
        )
        ax.add_patch(arc)


def add_door_simple(
    ax,
    x,
    y,
    width,
    direction: Literal["right", "left", "up", "down"] = "right",
    swing: Literal["up", "down", "left", "right"] = "up",
):
    """Add a door symbol (simple function interface)."""
    door = Door(x, y, width, direction, swing)
    add_door(ax, door)


def add_window(ax, window: Window):
    """
    Add a window symbol to the plot.

    Windows are represented as thin rectangles with a line through the middle.
    """
    x, y, width = scale(window.x), scale(window.y), scale(window.width)
    window_color = resolve_color("window")

    if window.orientation == "horizontal":
        # Horizontal window (on top/bottom walls)
        thickness = scale(0.8)
        rect = Rectangle(
            (x, y - thickness / 2),
            width,
            thickness,
            linewidth=1.5,
            edgecolor="black",
            facecolor=window_color,
            zorder=7,
        )
        ax.add_patch(rect)
        # Center line
        ax.plot([x, x + width], [y, y], color="black", linewidth=0.5, zorder=8)
    else:
        # Vertical window (on left/right walls)
        thickness = scale(0.8)
        rect = Rectangle(
            (x - thickness / 2, y),
            thickness,
            width,
            linewidth=1.5,
            edgecolor="black",
            facecolor=window_color,
            zorder=7,
        )
        ax.add_patch(rect)
        # Center line
        ax.plot([x, x], [y, y + width], color="black", linewidth=0.5, zorder=8)


def add_window_simple(
    ax, x, y, width, orientation: Literal["horizontal", "vertical"] = "horizontal"
):
    """Add a window symbol (simple function interface)."""
    window = Window(x, y, width, orientation)
    add_window(ax, window)


def add_stairs(ax, stairs: Stairs):
    """Add stairs symbol with step lines."""
    x, y = scale(stairs.x), scale(stairs.y)
    width, height = scale(stairs.width), scale(stairs.height)

    rect = Rectangle(
        (x, y), width, height, linewidth=1, edgecolor="black", facecolor="lightgray"
    )
    ax.add_patch(rect)

    if stairs.orientation == "horizontal":
        step_width = width / stairs.num_steps
        for i in range(stairs.num_steps):
            ax.plot(
                [x + i * step_width, x + i * step_width],
                [y, y + height],
                color="black",
                linewidth=0.5,
            )
    else:
        step_height = height / stairs.num_steps
        for i in range(stairs.num_steps):
            ax.plot(
                [x, x + width],
                [y + i * step_height, y + i * step_height],
                color="black",
                linewidth=0.5,
            )

    if stairs.label:
        ax.text(
            x + width / 2,
            y + height / 2,
            stairs.label,
            fontsize=7,
            ha="center",
            va="center",
        )


def add_stairs_simple(
    ax,
    x,
    y,
    width,
    height,
    num_steps=8,
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    label="",
):
    """Add stairs symbol (simple function interface)."""
    stairs = Stairs(x, y, width, height, num_steps, orientation, label)
    add_stairs(ax, stairs)


def add_fireplace(ax, fireplace: Fireplace):
    """Add fireplace symbol."""
    x, y = scale(fireplace.x), scale(fireplace.y)
    width, height = scale(fireplace.width), scale(fireplace.height)

    rect = Rectangle(
        (x, y), width, height, linewidth=1, edgecolor="black", facecolor="darkgray"
    )
    ax.add_patch(rect)

    # Inner fireplace opening
    inner = Rectangle(
        (x + width * 0.2, y),
        width * 0.6,
        height * 0.7,
        linewidth=1,
        edgecolor="black",
        facecolor="black",
    )
    ax.add_patch(inner)

    if fireplace.label:
        ax.text(
            x + width / 2,
            y + height + scale(1),
            fireplace.label,
            fontsize=6,
            ha="center",
        )


def add_fireplace_simple(ax, x, y, width, height, label=""):
    """Add fireplace symbol (simple function interface)."""
    fp = Fireplace(x, y, width, height, label)
    add_fireplace(ax, fp)


def add_furniture(ax, furniture: Furniture):
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
    ax,
    furniture_type,
    x,
    y,
    width,
    height=0,
    color="#8b4513",
    edge_color="black",
    label="",
    label_fontsize=7,
    label_color="black",
    rotation=0,
    linewidth=1,
):
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


def add_text_annotation(ax, annotation: TextAnnotation):
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


def add_line_annotation(ax, line: LineAnnotation):
    """Add a line annotation to the plot."""
    ax.plot(
        [scale(line.x1), scale(line.x2)],
        [scale(line.y1), scale(line.y2)],
        color=line.color,
        linewidth=line.linewidth,
        linestyle=line.linestyle,
        zorder=line.zorder,
    )


def add_dimension_arrow(ax, start, end, label, offset: float = 0, rotation: float = 0):
    """Add a dimension arrow with label."""
    ax.annotate(
        "",
        xy=start,
        xytext=end,
        arrowprops=dict(arrowstyle="<->", color="gray"),
    )
    mid_x = (start[0] + end[0]) / 2 + offset
    mid_y = (start[1] + end[1]) / 2 + offset
    ax.text(
        mid_x, mid_y, label, ha="center", fontsize=10, color="gray", rotation=rotation
    )


def add_north_arrow(ax, x: float, y: float, size: float = 5):
    """Add a north arrow indicator to the plot."""
    cx, cy = scale(x), scale(y)
    arrow_size = scale(size)

    # Draw the arrow pointing up (north)
    ax.annotate(
        "",
        xy=(cx, cy + arrow_size),
        xytext=(cx, cy),
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            lw=2,
        ),
    )

    # Draw "N" label above the arrow
    ax.text(
        cx,
        cy + arrow_size + scale(1.5),
        "N",
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="bottom",
        color="black",
    )

    # Draw a small circle at the base
    base_circle = Circle(
        (cx, cy),
        scale(0.8),
        facecolor="white",
        edgecolor="black",
        linewidth=1.5,
        zorder=10,
    )
    ax.add_patch(base_circle)


def add_theater_seating(ax, seating: TheaterSeating):
    """Add theater seating rows."""
    chair_color = resolve_color(seating.chair_color)
    edge_color = resolve_color(seating.edge_color)

    for row in range(seating.rows):
        x_pos = scale(seating.start_x + row * seating.row_spacing)
        for seat in range(seating.seats_per_row):
            y_pos = scale(seating.start_y + seat * seating.seat_spacing)
            chair = Rectangle(
                (x_pos, y_pos),
                scale(seating.chair_width),
                scale(seating.chair_height),
                linewidth=1,
                edgecolor=edge_color,
                facecolor=chair_color,
            )
            ax.add_patch(chair)


def add_pool_area(ax, pool_config: PoolConfig):
    """Add pool area with pool and hot tub."""
    area_color = resolve_color(pool_config.area_color)
    pool_color = resolve_color(pool_config.pool_color)
    hot_tub_color = resolve_color(pool_config.hot_tub_color)

    # Pool area background
    pool_area = Rectangle(
        (scale(pool_config.area_x), scale(pool_config.area_y)),
        scale(pool_config.area_width),
        scale(pool_config.area_height),
        linewidth=3,
        edgecolor="black",
        facecolor=area_color,
    )
    ax.add_patch(pool_area)
    ax.text(
        scale(pool_config.area_x + pool_config.area_width / 2),
        scale(pool_config.area_y + pool_config.area_height - 3),
        pool_config.area_label,
        fontsize=12,
        ha="center",
        fontweight="bold",
    )

    # Pool itself
    pool = Rectangle(
        (scale(pool_config.pool_x), scale(pool_config.pool_y)),
        scale(pool_config.pool_width),
        scale(pool_config.pool_height),
        linewidth=2,
        edgecolor=pool_config.pool_edge_color,
        facecolor=pool_color,
    )
    ax.add_patch(pool)
    ax.text(
        scale(pool_config.pool_x + pool_config.pool_width / 2),
        scale(pool_config.pool_y + pool_config.pool_height / 2),
        pool_config.pool_label,
        fontsize=10,
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
            linewidth=2,
        )
        ax.add_patch(hot_tub)
        ax.text(
            scale(pool_config.hot_tub_x),
            scale(pool_config.hot_tub_y),
            pool_config.hot_tub_label,
            fontsize=7,
            ha="center",
        )
        # Spa label
        if pool_config.spa_label_x and pool_config.spa_label_y:
            ax.text(
                scale(pool_config.spa_label_x),
                scale(pool_config.spa_label_y),
                "Spa",
                fontsize=8,
                ha="center",
            )


# =============================================================================
# BATCH DRAWING FUNCTIONS
# =============================================================================


def draw_rooms_from_data(ax, rooms_data: list[dict[str, Any]]) -> int:
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
            if "color" in room_data:
                room_data = room_data.copy()
                room_data["color"] = resolve_color(room_data["color"])

            # Filter out any unexpected keys
            valid_keys = {f.name for f in Room.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in room_data.items() if k in valid_keys}

            room = Room(**filtered_data)
            add_room(ax, room)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping room {i} due to error: {e}")
    return drawn


def draw_doors_from_data(ax, doors_data: list[dict[str, Any]]) -> int:
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


def draw_windows_from_data(ax, windows_data: list[dict[str, Any]]) -> int:
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


def draw_furniture_from_data(ax, furniture_data: list[dict[str, Any]]) -> int:
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
            item_data = item_data.copy()
            # Map 'type' to 'furniture_type' if needed (YAML uses 'type' for cleaner syntax)
            if "type" in item_data and "furniture_type" not in item_data:
                item_data["furniture_type"] = item_data.pop("type")

            valid_keys = {f.name for f in Furniture.__dataclass_fields__.values()}
            filtered_data = {k: v for k, v in item_data.items() if k in valid_keys}

            furniture = Furniture(**filtered_data)
            add_furniture(ax, furniture)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping furniture {i} due to error: {e}")
    return drawn


def draw_stairs_from_data(ax, stairs_data: list[dict[str, Any]]) -> int:
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


def draw_fireplaces_from_data(ax, fireplaces_data: list[dict[str, Any]]) -> int:
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


def draw_text_annotations_from_data(ax, annotations_data: list[dict[str, Any]]) -> int:
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
            filtered_data = {
                k: v for k, v in annotation_data.items() if k in valid_keys
            }
            annotation = TextAnnotation(**filtered_data)
            add_text_annotation(ax, annotation)
            drawn += 1
        except (TypeError, ValueError) as e:
            logger.warning(f"Skipping text annotation {i} due to error: {e}")
    return drawn


def draw_lines_from_data(ax, lines_data: list[dict[str, Any]]) -> int:
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
        config_path = Path(__file__).parent / "floor_plan_config.yaml"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        logger.warning(f"Config file not found: {config_path}")
        logger.info("Using built-in default configuration.")
        return get_default_config()

    if not YAML_AVAILABLE:
        logger.warning("PyYAML not available. Using built-in default configuration.")
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
    global SCALE, DEBUG_MODE, GRID_SPACING, AUTO_DIMENSIONS, COLORS

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
    SCALE = floor_settings.scale
    DEBUG_MODE = floor_settings.debug_mode
    GRID_SPACING = floor_settings.grid_spacing
    AUTO_DIMENSIONS = floor_settings.auto_dimensions

    # Update colors from config
    if "colors" in config:
        COLORS.update(config["colors"])

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
# DEFAULT DATA (used when YAML is not available)
# =============================================================================

MAIN_FLOOR_ROOMS_DEFAULT = [
    # Garage area
    {
        "x": 45,
        "y": 81,
        "width": 25,
        "height": 29,
        "label": "2 Car Garage",
        "color": "garage",
        "label_fontsize": 10,
        "auto_dimension": True,
        "dimension_text": "29'-2\" x 31'-9\"",
    },
    {
        "x": 55,
        "y": 70,
        "width": 8,
        "height": 11,
        "label": "Mud Room",
        "color": "utility",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "11' x 7.5'",
    },
    # Bedrooms
    {
        "x": 58,
        "y": 56,
        "width": 12,
        "height": 14,
        "label": "Bedroom 3",
        "color": "bedroom",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "13' x 13'",
    },
    {
        "x": 63,
        "y": 48,
        "width": 7,
        "height": 8,
        "label": "Bath 3",
        "color": "bathroom",
        "label_fontsize": 8,
    },
    {
        "x": 58,
        "y": 48,
        "width": 5,
        "height": 8,
        "label": "WIC",
        "color": "closet",
        "label_fontsize": 7,
    },
    {
        "x": 58,
        "y": 33,
        "width": 12,
        "height": 15,
        "label": "Bedroom 2",
        "color": "bedroom",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "14' x 14.5'",
    },
    {
        "x": 58,
        "y": 23,
        "width": 12,
        "height": 10,
        "label": "Bath 2",
        "color": "bathroom",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "11'4\" x 11'",
    },
    {
        "x": 53,
        "y": 40,
        "width": 5,
        "height": 8,
        "label": "WIC",
        "color": "closet",
        "label_fontsize": 7,
    },
    {
        "x": 50,
        "y": 60,
        "width": 8,
        "height": 10,
        "label": "Laundry",
        "color": "utility",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "12'",
    },
    # Kitchen area
    {
        "x": 45,
        "y": 19,
        "width": 13,
        "height": 14,
        "label": "Breakfast\nNook",
        "color": "kitchen",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "14' x 14'",
    },
    {
        "x": 40,
        "y": 68,
        "width": 15,
        "height": 13,
        "label": "Bedroom 4",
        "color": "bedroom",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "13' x 13'",
    },
    {
        "x": 45,
        "y": 60,
        "width": 10,
        "height": 8,
        "label": "Bath 4\nWIC",
        "color": "bathroom",
        "label_fontsize": 8,
    },
    {
        "x": 45,
        "y": 52,
        "width": 10,
        "height": 8,
        "label": "Pantry",
        "color": "utility",
        "label_fontsize": 7,
    },
    # Middle section
    {
        "x": 38,
        "y": 37,
        "width": 15,
        "height": 15,
        "label": "Kitchen",
        "color": "kitchen",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "13' x 12'",
    },
    {
        "x": 32,
        "y": 52,
        "width": 13,
        "height": 16,
        "label": "Butler's\nPantry",
        "color": "kitchen",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "15' x 8'",
    },
    {
        "x": 38,
        "y": 5,
        "width": 15,
        "height": 14,
        "label": "Breakfast\nPorch",
        "color": "porch",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "13'4\" x 12'",
    },
    {
        "x": 20,
        "y": 19,
        "width": 18,
        "height": 18,
        "label": "Family Room",
        "color": "living",
        "label_fontsize": 10,
        "auto_dimension": True,
        "dimension_text": "16'6\" x 15'-2\"",
        "notes": "Vaulted Clg.",
    },
    {
        "x": 22,
        "y": 63,
        "width": 18,
        "height": 18,
        "label": "Dining\nRoom",
        "color": "dining",
        "label_fontsize": 10,
        "auto_dimension": True,
        "dimension_text": "18' x 14'6\"",
    },
    {
        "x": 22,
        "y": 51,
        "width": 10,
        "height": 12,
        "label": "Front\nHall",
        "color": "hall",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "10'-2\" x 12'",
    },
    {
        "x": 8,
        "y": 70,
        "width": 14,
        "height": 11,
        "label": "Foyer",
        "color": "hall",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "11' x 13'",
    },
    {
        "x": 20,
        "y": 5,
        "width": 18,
        "height": 14,
        "label": "Outdoor\nLiving",
        "color": "porch",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "35'-2\" x 13'",
    },
    # Master suite area
    {
        "x": -4,
        "y": 67,
        "width": 12,
        "height": 14,
        "label": "Lounge",
        "color": "living",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "14'-2\" x 12'-2\"",
    },
    {
        "x": 8,
        "y": 53,
        "width": 14,
        "height": 14,
        "label": "Bar",
        "color": "living",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "14'6\" x 9'4\"",
    },
    {
        "x": 8,
        "y": 45,
        "width": 7,
        "height": 8,
        "label": "WIC",
        "color": "closet",
        "label_fontsize": 7,
        "auto_dimension": True,
        "dimension_text": "12'",
    },
    {
        "x": 8,
        "y": 32,
        "width": 12,
        "height": 13,
        "label": "Office",
        "color": "office",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "12'6\" x 12'",
    },
    {
        "x": 8,
        "y": 5,
        "width": 12,
        "height": 14,
        "label": "Office\nPorch",
        "color": "porch",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "11'4\" x 10'",
    },
    {
        "x": -2,
        "y": 45,
        "width": 10,
        "height": 8,
        "label": "WIC",
        "color": "closet",
        "label_fontsize": 7,
        "auto_dimension": True,
        "dimension_text": "12'",
    },
    {
        "x": -12,
        "y": 25,
        "width": 20,
        "height": 20,
        "label": "Master\nSuite",
        "color": "bedroom",
        "label_fontsize": 10,
        "auto_dimension": True,
        "dimension_text": "17'-4\" x 22'-8\"",
        "notes": "Vaulted Clg.",
    },
    {
        "x": -12,
        "y": 53,
        "width": 12,
        "height": 14,
        "label": "Master\nBath",
        "color": "bathroom",
        "label_fontsize": 9,
        "notes": "12' Clg.",
    },
    {
        "x": -4,
        "y": 53,
        "width": 12,
        "height": 14,
        "label": "WIC",
        "color": "closet",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "12'",
    },
    {
        "x": -12,
        "y": 10,
        "width": 15,
        "height": 15,
        "label": "Master\nPorch",
        "color": "porch",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "19'-2\" x 12'-6\"",
    },
    {
        "x": -27,
        "y": 10,
        "width": 15,
        "height": 15,
        "label": "Side\nPorch",
        "color": "porch",
        "label_fontsize": 8,
        "auto_dimension": True,
        "dimension_text": "10' x 22'",
    },
    {
        "x": 0,
        "y": 81,
        "width": 20,
        "height": 29,
        "label": "Front Porch",
        "color": "porch",
        "label_fontsize": 10,
        "auto_dimension": True,
        "dimension_text": "50'-5\" x 12'-4\"",
    },
]

MAIN_FLOOR_DOORS_DEFAULT = [
    {"x": 58, "y": 70, "width": 3, "direction": "down", "swing": "right"},
    {"x": 58, "y": 61, "width": 3, "direction": "down", "swing": "left"},
    {"x": 65, "y": 48, "width": 2.5, "direction": "down", "swing": "left"},
    {"x": 60, "y": 48, "width": 2.5, "direction": "down", "swing": "left"},
    {"x": 58, "y": 40, "width": 3, "direction": "down", "swing": "left"},
    {"x": 62, "y": 23, "width": 2.5, "direction": "down", "swing": "left"},
    {"x": 53, "y": 43, "width": 2.5, "direction": "down", "swing": "right"},
    {"x": 50, "y": 65, "width": 3, "direction": "down", "swing": "right"},
    {"x": 40, "y": 73, "width": 3, "direction": "down", "swing": "right"},
    {"x": 48, "y": 60, "width": 2.5, "direction": "down", "swing": "right"},
    {"x": 45, "y": 55, "width": 2.5, "direction": "down", "swing": "right"},
    {"x": 32, "y": 60, "width": 3, "direction": "down", "swing": "right"},
    {"x": 45, "y": 5, "width": 4, "direction": "down", "swing": "left"},
    {"x": 28, "y": 5, "width": 4, "direction": "down", "swing": "left"},
    {"x": 8, "y": 73, "width": 4, "direction": "down", "swing": "right"},
    {"x": 10, "y": 45, "width": 2.5, "direction": "down", "swing": "left"},
    {"x": 12, "y": 32, "width": 3, "direction": "down", "swing": "left"},
    {"x": 12, "y": 5, "width": 3, "direction": "down", "swing": "left"},
    {"x": -2, "y": 48, "width": 2.5, "direction": "down", "swing": "right"},
    {"x": 2, "y": 25, "width": 3, "direction": "down", "swing": "left"},
    {"x": -6, "y": 53, "width": 3, "direction": "down", "swing": "left"},
    {"x": -2, "y": 53, "width": 3, "direction": "down", "swing": "left"},
    {"x": -2, "y": 10, "width": 4, "direction": "down", "swing": "left"},
    {"x": 20, "y": 90, "width": 4, "direction": "left", "swing": "down"},
]

MAIN_FLOOR_WINDOWS_DEFAULT = [
    {"x": 5, "y": 81, "width": 8, "orientation": "horizontal"},
    {"x": 12, "y": 81, "width": 6, "orientation": "horizontal"},
    {"x": -12, "y": 35, "width": 8, "orientation": "vertical"},
    {"x": -2, "y": 25, "width": 6, "orientation": "horizontal"},
    {"x": 70, "y": 60, "width": 6, "orientation": "vertical"},
    {"x": 70, "y": 38, "width": 6, "orientation": "vertical"},
    {"x": 25, "y": 5, "width": 8, "orientation": "horizontal"},
    {"x": 48, "y": 19, "width": 6, "orientation": "horizontal"},
    {"x": 53, "y": 19, "width": 5, "orientation": "horizontal"},
    {"x": -12, "y": 60, "width": 6, "orientation": "vertical"},
    {"x": 20, "y": 81, "width": 6, "orientation": "horizontal"},
]

MAIN_FLOOR_FIREPLACES_DEFAULT = [
    {"x": 35, "y": 63, "width": 4, "height": 3, "label": ""},
    {"x": -4, "y": 73, "width": 3, "height": 3, "label": "Gas\nFireplace"},
]

MAIN_FLOOR_STAIRS_DEFAULT = [
    {
        "x": 20,
        "y": 45,
        "width": 12,
        "height": 6,
        "num_steps": 10,
        "orientation": "horizontal",
        "label": "DN",
    },
]

BASEMENT_ROOMS_DEFAULT = [
    {
        "x": 0,
        "y": 0,
        "width": 10,
        "height": 30,
        "label": "Bath",
        "color": "bath",
        "label_fontsize": 9,
        "auto_dimension": True,
        "dimension_text": "30'",
    },
    {
        "x": 10,
        "y": 0,
        "width": 15,
        "height": 15,
        "label": "Utilities",
        "color": "utility",
        "label_fontsize": 7,
        "notes": "Power, Internet,\nGas, Furnace,\nWater Treatment",
    },
    {
        "x": 0,
        "y": 30,
        "width": 5,
        "height": 30,
        "label": "Books",
        "color": "books",
        "label_fontsize": 8,
    },
    {
        "x": 5,
        "y": 60,
        "width": 20,
        "height": 40,
        "label": "Gaming / Studio",
        "color": "gaming",
        "label_fontsize": 11,
        "label_color": "white",
        "auto_dimension": True,
        "dimension_text": "40' x 20'",
    },
    {
        "x": 5,
        "y": 88,
        "width": 20,
        "height": 12,
        "label": "Books",
        "color": "books",
        "label_fontsize": 8,
    },
    {
        "x": 10,
        "y": 30,
        "width": 10,
        "height": 10,
        "label": "Storage\nUnder\nStairs",
        "color": "storage",
        "label_fontsize": 7,
    },
    {
        "x": 20,
        "y": 15,
        "width": 15,
        "height": 8,
        "label": "Books",
        "color": "books",
        "label_fontsize": 8,
    },
    {
        "x": 20,
        "y": 23,
        "width": 20,
        "height": 37,
        "label": "",
        "color": "bar",
        "label_fontsize": 10,
    },
    {
        "x": 35,
        "y": 15,
        "width": 25,
        "height": 8,
        "label": "Books",
        "color": "books",
        "label_fontsize": 8,
    },
    {
        "x": 40,
        "y": 30,
        "width": 20,
        "height": 30,
        "label": "Pool\nUtilities",
        "color": "utility",
        "label_fontsize": 9,
    },
    {
        "x": 40,
        "y": 88,
        "width": 20,
        "height": 12,
        "label": "Books",
        "color": "books",
        "label_fontsize": 8,
    },
]

BASEMENT_THEATER_DEFAULT = {
    "room": {
        "x": 25,
        "y": 0,
        "width": 35,
        "height": 15,
        "label": "Home Theater",
        "color": "theater",
        "label_fontsize": 11,
        "label_color": "white",
        "fontweight": "bold",
        "auto_dimension": True,
        "dimension_text": "30' x 40'",
    },
    "seating": {
        "start_x": 28,
        "start_y": 2,
        "rows": 4,
        "seats_per_row": 3,
        "chair_width": 3,
        "chair_height": 2.5,
        "row_spacing": 5,
        "seat_spacing": 4,
        "chair_color": "chair",
        "edge_color": "gray",
    },
    "false_wall": {
        "x1": 25,
        "y1": 0,
        "x2": 60,
        "y2": 0,
        "color": "red",
        "linewidth": 4,
        "linestyle": "--",
        "label": "False Wall",
        "label_x": 42,
        "label_y": -2,
    },
}

BASEMENT_POOL_DEFAULT = {
    "area": {
        "x": 25,
        "y": 60,
        "width": 35,
        "height": 40,
        "color": "pool_area",
        "label": "Pool Area",
    },
    "pool": {
        "x": 28,
        "y": 63,
        "width": 18,
        "height": 32,
        "color": "pool",
        "edge_color": "#0288d1",
        "label": "Salt Water\nPool",
    },
    "hot_tub": {
        "x": 52,
        "y": 73,
        "radius": 4,
        "color": "spa",
        "edge_color": "#0288d1",
        "label": "Hot\nTub",
    },
    "spa_label": {
        "x": 52,
        "y": 88,
        "text": "Spa",
    },
}

BASEMENT_DOORS_DEFAULT = [
    {"x": 0, "y": 20, "width": 3, "direction": "up", "swing": "right"},
    {"x": 20, "y": 8, "width": 3, "direction": "up", "swing": "left"},
    {"x": 40, "y": 15, "width": 4, "direction": "up", "swing": "left"},
    {"x": 20, "y": 60, "width": 4, "direction": "up", "swing": "left"},
    {"x": 20, "y": 35, "width": 4, "direction": "up", "swing": "right"},
    {"x": 40, "y": 45, "width": 3, "direction": "up", "swing": "left"},
    {"x": 40, "y": 60, "width": 4, "direction": "up", "swing": "left"},
    {"x": 40, "y": 15, "width": 4, "direction": "up", "swing": "left"},
]

BASEMENT_STAIRS_DEFAULT = [
    {
        "x": 0,
        "y": 60,
        "width": 5,
        "height": 10,
        "num_steps": 8,
        "orientation": "vertical",
        "label": "Exit\nStairs\n60'",
    },
    {
        "x": 0,
        "y": 70,
        "width": 5,
        "height": 12,
        "num_steps": 8,
        "orientation": "vertical",
        "label": "Stairs\nto Main",
    },
]

BASEMENT_FURNITURE_DEFAULT = [
    {
        "furniture_type": "ellipse",
        "x": 15,
        "y": 78,
        "width": 4,
        "height": 12,
        "color": "hammock",
        "edge_color": "#8b4513",
        "label": "Hammock",
        "label_fontsize": 7,
        "rotation": 90,
        "linewidth": 2,
    },
    {
        "furniture_type": "rectangle",
        "x": 23,
        "y": 35,
        "width": 4,
        "height": 12,
        "color": "wood",
        "edge_color": "brown",
        "label": "Bar",
        "label_fontsize": 7,
        "label_color": "white",
        "rotation": 90,
        "linewidth": 2,
    },
    {
        "furniture_type": "rectangle",
        "x": 30,
        "y": 35,
        "width": 3,
        "height": 12,
        "color": "leather",
        "edge_color": "black",
        "label": "Couch",
        "label_fontsize": 6,
        "label_color": "white",
        "rotation": 90,
        "linewidth": 1,
    },
    {
        "furniture_type": "circle",
        "x": 28,
        "y": 41,
        "width": 1.5,
        "color": "wood",
        "edge_color": "black",
        "label": "",
        "linewidth": 1,
    },
    {
        "furniture_type": "rectangle",
        "x": 26,
        "y": 1,
        "width": 8,
        "height": 1.5,
        "color": "#333333",
        "edge_color": "black",
        "label": "",
        "linewidth": 1,
    },
]

BASEMENT_TEXT_ANNOTATIONS_DEFAULT = [
    {"x": 22, "y": 32, "text": "Sink\nDW", "fontsize": 6, "ha": "center"},
    {"x": 22, "y": 50, "text": "Coffee", "fontsize": 6, "ha": "center"},
    {
        "x": 30,
        "y": 56,
        "text": "Bar Area",
        "fontsize": 10,
        "ha": "center",
        "fontweight": "bold",
    },
    {
        "x": 55,
        "y": 7,
        "text": "Rows of\nChairs",
        "fontsize": 8,
        "ha": "center",
        "color": "white",
    },
]


# =============================================================================
# FLOOR PLAN DRAWING FUNCTIONS
# =============================================================================


def draw_main_floor(ax, config: dict[str, Any]):
    """Draw the main floor plan on the given axes."""
    main_config = config.get("main_floor", {})
    fig_config = main_config.get("figure", {})
    settings = config.get("settings", {})

    # Draw debug grid if enabled
    if DEBUG_MODE:
        draw_debug_grid(
            ax,
            fig_config.get("x_min", -32),
            fig_config.get("x_max", 85),
            fig_config.get("y_min", -5),
            fig_config.get("y_max", 120),
            GRID_SPACING,
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


def draw_basement(ax, config: dict[str, Any]):
    """Draw the basement floor plan on the given axes."""
    basement_config = config.get("basement", {})
    fig_config = basement_config.get("figure", {})

    # Draw debug grid if enabled
    if DEBUG_MODE:
        draw_debug_grid(
            ax,
            fig_config.get("x_min", -5),
            fig_config.get("x_max", 65),
            fig_config.get("y_min", -5),
            fig_config.get("y_max", 105),
            GRID_SPACING,
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


def generate_main_floor(config: dict[str, Any] | None = None):
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
    if not DEBUG_MODE:
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


def generate_basement(config: dict[str, Any] | None = None):
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
    if not DEBUG_MODE:
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

    if not DEBUG_MODE:
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
    filename="floor_plans.pdf", config: dict[str, Any] | None = None
):
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
        if not DEBUG_MODE:
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
        if not DEBUG_MODE:
            ax.axis("off")

        plt.tight_layout()
        pdf.savefig(fig, bbox_inches="tight", facecolor="white")
        plt.close()

    print(f"Combined floor plans saved to '{output_path}'")


def main(args: list[str] | None = None):
    """
    Generate all floor plans in multiple formats.

    Supports command-line arguments:
        --png-only    Only generate PNG files
        --svg-only    Only generate SVG files
        --pdf-only    Only generate PDF file
        --debug       Enable debug mode (grid overlay)
        --help        Show help message

    Args:
        args: Command-line arguments (uses sys.argv if None)
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate house floor plans in multiple formats",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python floor_plan_generator.py              # Generate all formats
  python floor_plan_generator.py --svg-only   # Generate only SVG files
  python floor_plan_generator.py --debug      # Generate with grid overlay
        """,
    )
    parser.add_argument(
        "--png-only", action="store_true", help="Only generate PNG files"
    )
    parser.add_argument(
        "--svg-only", action="store_true", help="Only generate SVG files"
    )
    parser.add_argument(
        "--pdf-only", action="store_true", help="Only generate combined PDF"
    )
    parser.add_argument(
        "--debug", action="store_true", help="Enable debug mode with grid overlay"
    )
    parser.add_argument("--config", type=str, help="Path to custom config file")

    parsed_args = parser.parse_args(args)

    print("=" * 60)
    print("House Floor Plan Generator")
    print("=" * 60)
    print()

    # Load configuration
    print("Loading configuration...")
    config_path = parsed_args.config if parsed_args.config else None
    config = load_config(config_path)
    apply_config_settings(config)

    # Override debug mode if specified on command line
    global DEBUG_MODE
    if parsed_args.debug:
        DEBUG_MODE = True

    # Show current settings
    print(f"  Scale: {SCALE}")
    print(f"  Debug Mode: {DEBUG_MODE}")
    print(f"  Grid Spacing: {GRID_SPACING}")
    print(f"  Auto Dimensions: {AUTO_DIMENSIONS}")
    print()

    # Determine which formats to generate
    generate_png = not (parsed_args.svg_only or parsed_args.pdf_only)
    generate_svg_files = not (parsed_args.png_only or parsed_args.pdf_only)
    generate_pdf = not (parsed_args.png_only or parsed_args.svg_only)

    output_files = []

    if generate_png:
        print("Generating PNG files...")
        print("  Main Floor Plan...")
        generate_main_floor(config)
        output_files.append(OUTPUT_DIR / "main_floor_plan.png")

        print("  Basement Floor Plan...")
        generate_basement(config)
        output_files.append(OUTPUT_DIR / "basement_floor_plan.png")
        print()

    if generate_svg_files:
        print("Generating SVG files...")
        svg_paths = generate_all_svg(config)
        output_files.extend(svg_paths)
        print()

    if generate_pdf:
        print("Generating Combined PDF...")
        generate_combined_pdf(config=config)
        output_files.append(OUTPUT_DIR / "floor_plans.pdf")
        print()

    print("=" * 60)
    print("Floor plan generation complete!")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    print("Output files:")
    for f in output_files:
        print(f"  - {f}")
    print()
    print("To modify the floor plans, edit 'floor_plan_config.yaml'")
    print("Set 'debug_mode: true' in the config to show grid overlay")
    print()
    print("SVG files can be opened in:")
    print("  - Web browsers (for viewing)")
    print("  - Inkscape, Adobe Illustrator (for editing)")
    print("  - CAD software (for import)")
    print("=" * 60)


if __name__ == "__main__":
    import sys

    sys.exit(main() or 0)
