"""
Data models for floor plan generation.

This module contains all dataclass definitions used to represent
floor plan elements like rooms, doors, windows, furniture, etc.

All models include:
- Type hints for all fields
- Default values where appropriate
- Validation via __post_init__ hooks
- Utility methods for common operations
"""

from dataclasses import dataclass, field
from typing import Literal


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
    wall_thick: int = 2

    def __post_init__(self) -> None:
        """Validate and normalize settings after initialization."""
        if self.scale <= 0:
            self.scale = 1.0
        if self.grid_spacing <= 0:
            self.grid_spacing = 10
        self.output_dpi = max(self.output_dpi, 72)
        if self.output_format not in ("png", "svg", "pdf"):
            self.output_format = "png"

    def validate(self) -> list[str]:
        """Validate settings and return list of warnings."""
        warnings = []
        if self.scale <= 0:
            warnings.append(f"Invalid scale {self.scale}, using 1.0")
        if self.grid_spacing <= 0:
            warnings.append(f"Invalid grid_spacing {self.grid_spacing}, using 10")
        if self.output_dpi < 72:
            warnings.append(f"Low DPI {self.output_dpi} may result in poor quality")
        return warnings

    def to_dict(self) -> dict:
        """Convert settings to dictionary for serialization."""
        return {
            "scale": self.scale,
            "debug_mode": self.debug_mode,
            "grid_spacing": self.grid_spacing,
            "auto_dimensions": self.auto_dimensions,
            "output_dpi": self.output_dpi,
            "output_format": self.output_format,
            "show_north_arrow": self.show_north_arrow,
            "wall_thick": self.wall_thick,
        }


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

    def __post_init__(self) -> None:
        """Validate room dimensions after initialization."""
        if self.width < 0:
            self.width = abs(self.width)
        if self.height < 0:
            self.height = abs(self.height)
        if self.label_fontsize < 1:
            self.label_fontsize = 8

    def validate(self) -> list[str]:
        """Validate room dimensions and return list of warnings."""
        warnings = []
        if self.width <= 0:
            warnings.append(f"Room '{self.label}' has invalid width: {self.width}")
        if self.height <= 0:
            warnings.append(f"Room '{self.label}' has invalid height: {self.height}")
        if self.width > 100:
            warnings.append(f"Room '{self.label}' has unusually large width: {self.width}'")
        if self.height > 100:
            warnings.append(f"Room '{self.label}' has unusually large height: {self.height}'")
        return warnings

    @property
    def center(self) -> tuple[float, float]:
        """Return the center point of the room."""
        return (self.x + self.width / 2, self.y + self.height / 2)

    @property
    def bounds(self) -> tuple[float, float, float, float]:
        """Return (x_min, y_min, x_max, y_max) bounds."""
        return (self.x, self.y, self.x + self.width, self.y + self.height)

    @property
    def area(self) -> float:
        """Return the area of the room in square feet."""
        return self.width * self.height

    @property
    def corners(self) -> list[tuple[float, float]]:
        """Return list of corner coordinates [(x, y), ...] clockwise from bottom-left."""
        return [
            (self.x, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height),
            (self.x + self.width, self.y),
        ]

    def contains_point(self, px: float, py: float) -> bool:
        """Check if a point is inside the room."""
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height

    def overlaps(self, other: "Room", tolerance: float = 0.0) -> bool:
        """Check if this room overlaps with another room."""
        return not (
            self.x + self.width <= other.x - tolerance
            or other.x + other.width <= self.x - tolerance
            or self.y + self.height <= other.y - tolerance
            or other.y + other.height <= self.y - tolerance
        )

    def get_display_label(self, include_dimensions: bool = True) -> str:
        """Get the full display label including dimensions and notes."""
        parts = [self.label]
        if include_dimensions and self.auto_dimension and self.dimension_text:
            parts.append(self.dimension_text)
        if self.notes:
            parts.append(self.notes)
        return "\n".join(filter(None, parts))


@dataclass
class Door:
    """Data class for door definition."""

    x: float
    y: float
    width: float
    direction: Literal["right", "left", "up", "down"] = "right"
    swing: Literal["up", "down", "left", "right"] = "up"

    def __post_init__(self) -> None:
        """Validate door dimensions after initialization."""
        if self.width < 0:
            self.width = abs(self.width)

    def validate(self) -> list[str]:
        """Validate door dimensions."""
        warnings = []
        if self.width <= 0:
            warnings.append(f"Door at ({self.x}, {self.y}) has invalid width: {self.width}")
        if self.width > 8:
            warnings.append(f"Door at ({self.x}, {self.y}) seems unusually wide: {self.width}'")
        if self.width < 2:
            warnings.append(f"Door at ({self.x}, {self.y}) seems unusually narrow: {self.width}'")
        return warnings

    @property
    def is_horizontal(self) -> bool:
        """Check if door opens horizontally."""
        return self.direction in ("right", "left")

    @property
    def is_vertical(self) -> bool:
        """Check if door opens vertically."""
        return self.direction in ("up", "down")

    def get_arc_config(self) -> tuple[tuple[float, float], int, int] | None:
        """
        Get arc drawing configuration for the door swing.

        Returns:
            Tuple of (arc_center_offset, theta1, theta2) or None if invalid config.
        """
        configs = {
            ("right", "up"): ((0, 0), 0, 90),
            ("right", "down"): ((0, 0), 270, 360),
            ("left", "up"): ((1, 0), 90, 180),
            ("left", "down"): ((1, 0), 180, 270),
            ("up", "right"): ((0, 0), 0, 90),
            ("up", "left"): ((0, 1), 270, 360),
            ("down", "right"): ((0, 1), 270, 360),
            ("down", "left"): ((0, 0), 90, 180),
        }
        return configs.get((self.direction, self.swing))


@dataclass
class Window:
    """Data class for window definition."""

    x: float
    y: float
    width: float
    orientation: Literal["horizontal", "vertical"] = "horizontal"

    def __post_init__(self) -> None:
        """Validate window dimensions after initialization."""
        if self.width < 0:
            self.width = abs(self.width)

    def validate(self) -> list[str]:
        """Validate window dimensions."""
        warnings = []
        if self.width <= 0:
            warnings.append(f"Window at ({self.x}, {self.y}) has invalid width: {self.width}")
        if self.width > 20:
            warnings.append(f"Window at ({self.x}, {self.y}) seems unusually wide: {self.width}'")
        return warnings

    @property
    def is_horizontal(self) -> bool:
        """Check if window is horizontal (on top/bottom walls)."""
        return self.orientation == "horizontal"

    @property
    def is_vertical(self) -> bool:
        """Check if window is vertical (on left/right walls)."""
        return self.orientation == "vertical"


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
    label_offset_x: float = 0
    label_offset_y: float = 0

    def __post_init__(self) -> None:
        """Validate stairs dimensions after initialization."""
        if self.width < 0:
            self.width = abs(self.width)
        if self.height < 0:
            self.height = abs(self.height)
        self.num_steps = max(self.num_steps, 1)

    @property
    def step_size(self) -> float:
        """Get the size of each step based on orientation."""
        if self.orientation == "horizontal":
            return self.width / self.num_steps
        return self.height / self.num_steps

    @property
    def center(self) -> tuple[float, float]:
        """Return the center point of the stairs."""
        return (self.x + self.width / 2, self.y + self.height / 2)


@dataclass
class Fireplace:
    """Data class for fireplace definition."""

    x: float
    y: float
    width: float
    height: float
    label: str = ""

    def __post_init__(self) -> None:
        """Validate fireplace dimensions after initialization."""
        if self.width < 0:
            self.width = abs(self.width)
        if self.height < 0:
            self.height = abs(self.height)

    @property
    def center(self) -> tuple[float, float]:
        """Return the center point of the fireplace."""
        return (self.x + self.width / 2, self.y + self.height / 2)

    @property
    def inner_bounds(self) -> tuple[float, float, float, float]:
        """Return bounds for the inner fireplace opening (x, y, width, height)."""
        return (
            self.x + self.width * 0.2,
            self.y,
            self.width * 0.6,
            self.height * 0.7,
        )


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

    def __post_init__(self) -> None:
        """Validate furniture dimensions after initialization."""
        if self.width < 0:
            self.width = abs(self.width)
        if self.height < 0:
            self.height = abs(self.height)
        # For circles, height is not used, default to width
        if self.furniture_type == "circle" and self.height == 0:
            self.height = self.width

    @property
    def is_circle(self) -> bool:
        """Check if furniture is circular."""
        return self.furniture_type == "circle"

    @property
    def is_rectangle(self) -> bool:
        """Check if furniture is rectangular."""
        return self.furniture_type == "rectangle"

    @property
    def is_ellipse(self) -> bool:
        """Check if furniture is elliptical."""
        return self.furniture_type == "ellipse"

    @property
    def center(self) -> tuple[float, float]:
        """Return the center point for label placement."""
        if self.furniture_type == "rectangle":
            return (self.x + self.width / 2, self.y + self.height / 2)
        # For circle and ellipse, x, y is already the center
        return (self.x, self.y)


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

    def __post_init__(self) -> None:
        """Validate annotation after initialization."""
        if self.fontsize < 1:
            self.fontsize = 8
        # Normalize alignment values
        if self.ha not in ("left", "center", "right"):
            self.ha = "center"
        if self.va not in ("top", "center", "bottom", "baseline"):
            self.va = "center"


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
    label: str = ""
    label_x: float | None = None
    label_y: float | None = None

    @property
    def length(self) -> float:
        """Calculate the length of the line."""
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    @property
    def midpoint(self) -> tuple[float, float]:
        """Return the midpoint of the line."""
        return ((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)

    @property
    def is_horizontal(self) -> bool:
        """Check if line is horizontal."""
        return abs(self.y1 - self.y2) < 0.001

    @property
    def is_vertical(self) -> bool:
        """Check if line is vertical."""
        return abs(self.x1 - self.x2) < 0.001


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

    def __post_init__(self) -> None:
        """Validate seating configuration after initialization."""
        self.rows = max(self.rows, 1)
        self.seats_per_row = max(self.seats_per_row, 1)
        if self.chair_width < 0:
            self.chair_width = abs(self.chair_width)
        if self.chair_height < 0:
            self.chair_height = abs(self.chair_height)

    @property
    def total_seats(self) -> int:
        """Return total number of seats."""
        return self.rows * self.seats_per_row

    @property
    def total_width(self) -> float:
        """Return total width of seating area."""
        return self.rows * self.row_spacing

    @property
    def total_height(self) -> float:
        """Return total height of seating area."""
        return self.seats_per_row * self.seat_spacing

    def get_seat_position(self, row: int, seat: int) -> tuple[float, float]:
        """Get the position of a specific seat (0-indexed)."""
        x = self.start_x + row * self.row_spacing
        y = self.start_y + seat * self.seat_spacing
        return (x, y)


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

    def __post_init__(self) -> None:
        """Validate pool configuration after initialization."""
        if self.area_width < 0:
            self.area_width = abs(self.area_width)
        if self.area_height < 0:
            self.area_height = abs(self.area_height)
        if self.pool_width < 0:
            self.pool_width = abs(self.pool_width)
        if self.pool_height < 0:
            self.pool_height = abs(self.pool_height)
        if self.hot_tub_radius < 0:
            self.hot_tub_radius = abs(self.hot_tub_radius)

    @property
    def pool_area(self) -> float:
        """Return the area of the pool in square feet."""
        return self.pool_width * self.pool_height

    @property
    def total_area(self) -> float:
        """Return the total pool area footprint in square feet."""
        return self.area_width * self.area_height

    @property
    def pool_center(self) -> tuple[float, float]:
        """Return the center point of the pool."""
        return (
            self.pool_x + self.pool_width / 2,
            self.pool_y + self.pool_height / 2,
        )

    @property
    def has_hot_tub(self) -> bool:
        """Check if pool configuration includes a hot tub."""
        return self.hot_tub_radius > 0


@dataclass
class FloorPlan:
    """Container for a complete floor plan."""

    name: str
    rooms: list[Room] = field(default_factory=list)
    doors: list[Door] = field(default_factory=list)
    windows: list[Window] = field(default_factory=list)
    stairs: list[Stairs] = field(default_factory=list)
    fireplaces: list[Fireplace] = field(default_factory=list)
    furniture: list[Furniture] = field(default_factory=list)
    text_annotations: list[TextAnnotation] = field(default_factory=list)
    line_annotations: list[LineAnnotation] = field(default_factory=list)

    @property
    def total_area(self) -> float:
        """Calculate total floor area from all rooms."""
        return sum(room.area for room in self.rooms)

    @property
    def room_count(self) -> int:
        """Return number of rooms."""
        return len(self.rooms)

    def get_rooms_by_color(self, color: str) -> list[Room]:
        """Get all rooms with a specific color/type."""
        return [room for room in self.rooms if room.color == color]

    def get_room_by_label(self, label: str) -> Room | None:
        """Find a room by its label."""
        for room in self.rooms:
            if room.label.lower() == label.lower():
                return room
        return None

    def validate(self) -> list[str]:
        """Validate all elements and return list of warnings."""
        warnings = []
        for room in self.rooms:
            warnings.extend(room.validate())
        for door in self.doors:
            warnings.extend(door.validate())
        for window in self.windows:
            warnings.extend(window.validate())
        # Check for overlapping rooms
        for i, room1 in enumerate(self.rooms):
            for room2 in self.rooms[i + 1 :]:
                if room1.overlaps(room2, tolerance=-0.5):  # Allow small overlaps
                    warnings.append(
                        f"Significant overlap between '{room1.label}' and '{room2.label}'"
                    )
        return warnings

    def get_bounds(self) -> tuple[float, float, float, float]:
        """
        Get the bounding box of all rooms.

        Returns:
            Tuple of (min_x, min_y, max_x, max_y)
        """
        if not self.rooms:
            return (0, 0, 0, 0)

        min_x = min(room.x for room in self.rooms)
        min_y = min(room.y for room in self.rooms)
        max_x = max(room.x + room.width for room in self.rooms)
        max_y = max(room.y + room.height for room in self.rooms)

        return (min_x, min_y, max_x, max_y)

    def get_dimensions(self) -> tuple[float, float]:
        """
        Get the overall width and height of the floor plan.

        Returns:
            Tuple of (width, height)
        """
        min_x, min_y, max_x, max_y = self.get_bounds()
        return (max_x - min_x, max_y - min_y)

    def find_room_at(self, x: float, y: float) -> Room | None:
        """Find a room that contains the given point."""
        for room in self.rooms:
            if room.contains_point(x, y):
                return room
        return None

    def get_adjacent_rooms(self, room: Room, tolerance: float = 0.5) -> list[Room]:
        """Get all rooms adjacent to the given room."""
        adjacent = []
        room_dict = {"x": room.x, "y": room.y, "width": room.width, "height": room.height}
        for other in self.rooms:
            if other is room:
                continue
            other_dict = {"x": other.x, "y": other.y, "width": other.width, "height": other.height}
            # Check if rooms share a wall
            r1_right = room_dict["x"] + room_dict["width"]
            r1_top = room_dict["y"] + room_dict["height"]
            r2_right = other_dict["x"] + other_dict["width"]
            r2_top = other_dict["y"] + other_dict["height"]

            shares_wall = False
            # Check horizontal adjacency
            horizontal_adjacent = (
                abs(r1_right - other_dict["x"]) <= tolerance
                or abs(room_dict["x"] - r2_right) <= tolerance
            )
            if horizontal_adjacent and room_dict["y"] < r2_top and r1_top > other_dict["y"]:
                shares_wall = True
            # Check vertical adjacency
            vertical_adjacent = (
                abs(r1_top - other_dict["y"]) <= tolerance
                or abs(room_dict["y"] - r2_top) <= tolerance
            )
            if vertical_adjacent and room_dict["x"] < r2_right and r1_right > other_dict["x"]:
                shares_wall = True

            if shares_wall:
                adjacent.append(other)
        return adjacent

    def to_dict(self) -> dict:
        """Convert floor plan to dictionary for serialization."""
        return {
            "name": self.name,
            "rooms": [
                {
                    "x": r.x,
                    "y": r.y,
                    "width": r.width,
                    "height": r.height,
                    "label": r.label,
                    "color": r.color,
                    "auto_dimension": r.auto_dimension,
                    "dimension_text": r.dimension_text,
                    "notes": r.notes,
                }
                for r in self.rooms
            ],
            "doors": [
                {"x": d.x, "y": d.y, "width": d.width, "direction": d.direction, "swing": d.swing}
                for d in self.doors
            ],
            "windows": [
                {"x": w.x, "y": w.y, "width": w.width, "orientation": w.orientation}
                for w in self.windows
            ],
        }


class FloorPlanBuilder:
    """
    Fluent builder for creating floor plans.

    Example usage:
        >>> plan = (FloorPlanBuilder("Main Floor")
        ...     .add_room(x=0, y=0, width=20, height=15, label="Living Room", color="living")
        ...     .add_room(x=20, y=0, width=15, height=15, label="Kitchen", color="kitchen")
        ...     .add_door(x=20, y=5, width=3, direction="right", swing="up")
        ...     .add_window(x=5, y=0, width=4, orientation="horizontal")
        ...     .build())
    """

    def __init__(self, name: str):
        """Initialize a new floor plan builder."""
        self._plan = FloorPlan(name)

    def add_room(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        label: str,
        color: str = "white",
        label_fontsize: int = 8,
        label_color: str = "black",
        linewidth: int = 2,
        fontweight: str = "normal",
        auto_dimension: bool = False,
        dimension_text: str = "",
        notes: str = "",
    ) -> "FloorPlanBuilder":
        """Add a room to the floor plan."""
        room = Room(
            x=x,
            y=y,
            width=width,
            height=height,
            label=label,
            color=color,
            label_fontsize=label_fontsize,
            label_color=label_color,
            linewidth=linewidth,
            fontweight=fontweight,
            auto_dimension=auto_dimension,
            dimension_text=dimension_text,
            notes=notes,
        )
        self._plan.rooms.append(room)
        return self

    def add_door(
        self,
        x: float,
        y: float,
        width: float,
        direction: Literal["right", "left", "up", "down"] = "right",
        swing: Literal["up", "down", "left", "right"] = "up",
    ) -> "FloorPlanBuilder":
        """Add a door to the floor plan."""
        door = Door(x=x, y=y, width=width, direction=direction, swing=swing)
        self._plan.doors.append(door)
        return self

    def add_window(
        self,
        x: float,
        y: float,
        width: float,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
    ) -> "FloorPlanBuilder":
        """Add a window to the floor plan."""
        window = Window(x=x, y=y, width=width, orientation=orientation)
        self._plan.windows.append(window)
        return self

    def add_stairs(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        num_steps: int = 8,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        label: str = "",
    ) -> "FloorPlanBuilder":
        """Add stairs to the floor plan."""
        stairs = Stairs(
            x=x,
            y=y,
            width=width,
            height=height,
            num_steps=num_steps,
            orientation=orientation,
            label=label,
        )
        self._plan.stairs.append(stairs)
        return self

    def add_fireplace(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        label: str = "",
    ) -> "FloorPlanBuilder":
        """Add a fireplace to the floor plan."""
        fireplace = Fireplace(x=x, y=y, width=width, height=height, label=label)
        self._plan.fireplaces.append(fireplace)
        return self

    def add_furniture(
        self,
        furniture_type: Literal["rectangle", "circle", "ellipse"],
        x: float,
        y: float,
        width: float,
        height: float = 0,
        color: str = "#8b4513",
        edge_color: str = "black",
        label: str = "",
        label_fontsize: int = 7,
        rotation: float = 0,
    ) -> "FloorPlanBuilder":
        """Add furniture to the floor plan."""
        furniture = Furniture(
            furniture_type=furniture_type,
            x=x,
            y=y,
            width=width,
            height=height,
            color=color,
            edge_color=edge_color,
            label=label,
            label_fontsize=label_fontsize,
            rotation=rotation,
        )
        self._plan.furniture.append(furniture)
        return self

    def add_text(
        self,
        x: float,
        y: float,
        text: str,
        fontsize: int = 8,
        color: str = "black",
        ha: str = "center",
        va: str = "center",
        rotation: float = 0,
    ) -> "FloorPlanBuilder":
        """Add a text annotation to the floor plan."""
        annotation = TextAnnotation(
            x=x,
            y=y,
            text=text,
            fontsize=fontsize,
            color=color,
            ha=ha,
            va=va,
            rotation=rotation,
        )
        self._plan.text_annotations.append(annotation)
        return self

    def add_line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: str = "black",
        linewidth: float = 2,
        linestyle: str = "-",
    ) -> "FloorPlanBuilder":
        """Add a line annotation to the floor plan."""
        line = LineAnnotation(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            color=color,
            linewidth=linewidth,
            linestyle=linestyle,
        )
        self._plan.line_annotations.append(line)
        return self

    def build(self) -> FloorPlan:
        """Build and return the floor plan."""
        return self._plan

    def validate(self) -> list[str]:
        """Validate the floor plan being built and return warnings."""
        return self._plan.validate()


# =============================================================================
# ROOM TEMPLATES
# =============================================================================


class RoomTemplates:
    """
    Pre-defined room layout templates for common room configurations.

    Example usage:
        >>> builder = FloorPlanBuilder("My House")
        >>> RoomTemplates.add_bedroom_suite(builder, x=0, y=0, width=15, height=20)
        >>> plan = builder.build()
    """

    @staticmethod
    def add_bedroom_suite(
        builder: FloorPlanBuilder,
        x: float,
        y: float,
        width: float,
        height: float,
        name: str = "Bedroom",
        bathroom_width: float = 8,
        closet_width: float = 5,
    ) -> FloorPlanBuilder:
        """
        Add a bedroom suite with attached bathroom and walk-in closet.

        Layout: Bedroom takes main space, bathroom and closet on one side.
        """
        # Main bedroom
        bedroom_width = width - max(bathroom_width, closet_width)
        builder.add_room(
            x=x,
            y=y,
            width=bedroom_width,
            height=height,
            label=name,
            color="bedroom",
            auto_dimension=True,
        )

        # Bathroom (top portion of side area)
        bath_height = height * 0.6
        builder.add_room(
            x=x + bedroom_width,
            y=y + height - bath_height,
            width=bathroom_width,
            height=bath_height,
            label=f"{name}\nBath",
            color="bathroom",
        )

        # Walk-in closet (bottom portion of side area)
        closet_height = height - bath_height
        builder.add_room(
            x=x + bedroom_width,
            y=y,
            width=closet_width,
            height=closet_height,
            label="WIC",
            color="closet",
        )

        # Door from bedroom to bathroom
        builder.add_door(
            x=x + bedroom_width,
            y=y + height - bath_height + 2,
            width=3,
            direction="right",
            swing="up",
        )

        # Door from bedroom to closet
        builder.add_door(
            x=x + bedroom_width,
            y=y + 2,
            width=3,
            direction="right",
            swing="down",
        )

        return builder

    @staticmethod
    def add_kitchen_layout(
        builder: FloorPlanBuilder,
        x: float,
        y: float,
        width: float,
        height: float,
        with_pantry: bool = True,
        pantry_width: float = 6,
    ) -> FloorPlanBuilder:
        """
        Add a kitchen layout optionally with pantry.
        """
        if with_pantry:
            kitchen_width = width - pantry_width
            builder.add_room(
                x=x,
                y=y,
                width=kitchen_width,
                height=height,
                label="Kitchen",
                color="kitchen",
                auto_dimension=True,
            )
            builder.add_room(
                x=x + kitchen_width,
                y=y,
                width=pantry_width,
                height=height,
                label="Pantry",
                color="utility",
            )
            builder.add_door(
                x=x + kitchen_width,
                y=y + height / 2 - 1.5,
                width=3,
                direction="right",
                swing="up",
            )
        else:
            builder.add_room(
                x=x,
                y=y,
                width=width,
                height=height,
                label="Kitchen",
                color="kitchen",
                auto_dimension=True,
            )

        return builder

    @staticmethod
    def add_garage(
        builder: FloorPlanBuilder,
        x: float,
        y: float,
        width: float,
        height: float,
        cars: int = 2,
    ) -> FloorPlanBuilder:
        """Add a garage with proper labeling."""
        label = f"{cars} Car Garage" if cars > 1 else "Garage"
        builder.add_room(
            x=x,
            y=y,
            width=width,
            height=height,
            label=label,
            color="garage",
            auto_dimension=True,
        )
        return builder

    @staticmethod
    def add_theater_room(
        builder: FloorPlanBuilder,
        x: float,
        y: float,
        width: float,
        height: float,
        rows: int = 3,
        seats_per_row: int = 4,
    ) -> FloorPlanBuilder:
        """Add a home theater room with seating annotation."""
        builder.add_room(
            x=x,
            y=y,
            width=width,
            height=height,
            label="Home Theater",
            color="theater",
            label_color="white",
            fontweight="bold",
            auto_dimension=True,
        )
        # Add text annotation for seating capacity
        builder.add_text(
            x=x + width / 2,
            y=y + 3,
            text=f"{rows} rows x {seats_per_row} seats",
            fontsize=7,
            color="white",
        )
        return builder

    @staticmethod
    def add_pool_area(
        builder: FloorPlanBuilder,
        x: float,
        y: float,
        width: float,
        height: float,
        pool_width: float | None = None,  # noqa: ARG004
        pool_height: float | None = None,  # noqa: ARG004
        with_hot_tub: bool = True,
    ) -> FloorPlanBuilder:
        """Add a pool area room (pool drawing handled separately).

        Note: pool_width and pool_height are accepted for API compatibility
        but pool drawing is handled separately by the drawing module.
        """
        builder.add_room(
            x=x,
            y=y,
            width=width,
            height=height,
            label="Pool Area",
            color="pool_area",
            auto_dimension=True,
        )
        if with_hot_tub:
            builder.add_text(
                x=x + width - 5,
                y=y + 5,
                text="Hot Tub",
                fontsize=7,
            )
        return builder


# Export all models (sorted alphabetically)
__all__ = [
    "Door",
    "Fireplace",
    "FloorPlan",
    "FloorPlanBuilder",
    "FloorPlanSettings",
    "Furniture",
    "LineAnnotation",
    "PoolConfig",
    "Room",
    "RoomTemplates",
    "Stairs",
    "TextAnnotation",
    "TheaterSeating",
    "Window",
]
