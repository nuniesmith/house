"""
Data models for floor plan generation.

This module contains all dataclass definitions used to represent
floor plan elements like rooms, doors, windows, furniture, etc.
"""

from dataclasses import dataclass
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


# Export all models
__all__ = [
    "FloorPlanSettings",
    "Room",
    "Door",
    "Window",
    "Stairs",
    "Fireplace",
    "Furniture",
    "TextAnnotation",
    "LineAnnotation",
    "TheaterSeating",
    "PoolConfig",
]
