"""
Comprehensive tests for floor plan models.

This module contains unit tests, edge case tests, and property-based tests
for all data classes in the models module.
"""

import sys
from pathlib import Path

import pytest

# Add the src directory to the path for imports
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from models import (
    Door,
    Fireplace,
    FloorPlan,
    FloorPlanBuilder,
    FloorPlanSettings,
    Furniture,
    LineAnnotation,
    PoolConfig,
    Room,
    RoomTemplates,
    Stairs,
    TextAnnotation,
    TheaterSeating,
    Window,
)

# =============================================================================
# FLOOR PLAN SETTINGS TESTS
# =============================================================================


class TestFloorPlanSettings:
    """Tests for FloorPlanSettings dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        settings = FloorPlanSettings()
        assert settings.scale == 1.0
        assert settings.debug_mode is False
        assert settings.grid_spacing == 10
        assert settings.auto_dimensions is True
        assert settings.output_dpi == 300
        assert settings.output_format == "png"
        assert settings.show_north_arrow is True
        assert settings.wall_thick == 2

    def test_custom_values(self):
        """Test that custom values are accepted."""
        settings = FloorPlanSettings(
            scale=2.0,
            debug_mode=True,
            grid_spacing=5,
            auto_dimensions=False,
            output_dpi=600,
            output_format="svg",
            show_north_arrow=False,
            wall_thick=3,
        )
        assert settings.scale == 2.0
        assert settings.debug_mode is True
        assert settings.grid_spacing == 5
        assert settings.auto_dimensions is False
        assert settings.output_dpi == 600
        assert settings.output_format == "svg"
        assert settings.show_north_arrow is False
        assert settings.wall_thick == 3

    def test_post_init_normalizes_invalid_scale(self):
        """Test that __post_init__ normalizes invalid scale."""
        settings = FloorPlanSettings(scale=-1.0)
        assert settings.scale == 1.0

    def test_post_init_normalizes_zero_scale(self):
        """Test that __post_init__ normalizes zero scale."""
        settings = FloorPlanSettings(scale=0)
        assert settings.scale == 1.0

    def test_post_init_normalizes_invalid_grid_spacing(self):
        """Test that __post_init__ normalizes invalid grid spacing."""
        settings = FloorPlanSettings(grid_spacing=-5)
        assert settings.grid_spacing == 10

    def test_post_init_normalizes_low_dpi(self):
        """Test that __post_init__ normalizes very low DPI."""
        settings = FloorPlanSettings(output_dpi=50)
        assert settings.output_dpi == 72

    def test_post_init_normalizes_invalid_format(self):
        """Test that __post_init__ normalizes invalid output format."""
        settings = FloorPlanSettings(output_format="invalid")
        assert settings.output_format == "png"

    def test_validate_valid_settings(self):
        """Test validation returns no warnings for valid settings."""
        settings = FloorPlanSettings()
        warnings = settings.validate()
        assert len(warnings) == 0

    def test_validate_invalid_scale(self):
        """Test validation catches invalid scale (before normalization)."""
        settings = FloorPlanSettings(scale=1.0)
        settings.scale = -1.0  # Set after init to bypass normalization
        warnings = settings.validate()
        assert any("scale" in w.lower() for w in warnings)

    def test_validate_low_dpi_warning(self):
        """Test validation warns about low DPI."""
        settings = FloorPlanSettings(output_dpi=72)
        settings.output_dpi = 50  # Set after init
        warnings = settings.validate()
        assert any("dpi" in w.lower() for w in warnings)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        settings = FloorPlanSettings(scale=1.5, debug_mode=True)
        result = settings.to_dict()
        assert isinstance(result, dict)
        assert result["scale"] == 1.5
        assert result["debug_mode"] is True


# =============================================================================
# ROOM TESTS
# =============================================================================


class TestRoom:
    """Tests for Room dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        room = Room(x=0, y=0, width=10, height=10, label="Test")
        assert room.color == "white"
        assert room.label_fontsize == 8
        assert room.label_color == "black"
        assert room.linewidth == 2
        assert room.fontweight == "normal"
        assert room.auto_dimension is False
        assert room.dimension_text == ""
        assert room.notes == ""

    def test_custom_values(self):
        """Test that custom values are accepted."""
        room = Room(
            x=10,
            y=20,
            width=15,
            height=12,
            label="Bedroom",
            color="bedroom",
            label_fontsize=10,
            label_color="white",
            linewidth=3,
            fontweight="bold",
            auto_dimension=True,
            dimension_text="15' x 12'",
            notes="Master",
        )
        assert room.x == 10
        assert room.y == 20
        assert room.width == 15
        assert room.height == 12
        assert room.label == "Bedroom"
        assert room.color == "bedroom"
        assert room.notes == "Master"

    def test_post_init_normalizes_negative_width(self):
        """Test that negative width is normalized."""
        room = Room(x=0, y=0, width=-10, height=10, label="Test")
        assert room.width == 10

    def test_post_init_normalizes_negative_height(self):
        """Test that negative height is normalized."""
        room = Room(x=0, y=0, width=10, height=-10, label="Test")
        assert room.height == 10

    def test_post_init_normalizes_invalid_fontsize(self):
        """Test that invalid fontsize is normalized."""
        room = Room(x=0, y=0, width=10, height=10, label="Test", label_fontsize=0)
        assert room.label_fontsize == 8

    def test_validate_valid_room(self):
        """Test validation for valid room."""
        room = Room(x=0, y=0, width=10, height=10, label="Test")
        warnings = room.validate()
        assert len(warnings) == 0

    def test_validate_zero_width(self):
        """Test validation catches zero width."""
        room = Room(x=0, y=0, width=10, height=10, label="Test")
        room.width = 0
        warnings = room.validate()
        assert any("width" in w.lower() for w in warnings)

    def test_validate_zero_height(self):
        """Test validation catches zero height."""
        room = Room(x=0, y=0, width=10, height=10, label="Test")
        room.height = 0
        warnings = room.validate()
        assert any("height" in w.lower() for w in warnings)

    def test_validate_unusually_large_dimensions(self):
        """Test validation warns about unusually large dimensions."""
        room = Room(x=0, y=0, width=150, height=150, label="Test")
        warnings = room.validate()
        assert len(warnings) >= 2  # Both width and height warnings

    def test_center_property(self):
        """Test center property calculation."""
        room = Room(x=10, y=20, width=20, height=10, label="Test")
        center = room.center
        assert center == (20, 25)

    def test_bounds_property(self):
        """Test bounds property calculation."""
        room = Room(x=10, y=20, width=20, height=10, label="Test")
        bounds = room.bounds
        assert bounds == (10, 20, 30, 30)

    def test_area_property(self):
        """Test area property calculation."""
        room = Room(x=0, y=0, width=10, height=15, label="Test")
        assert room.area == 150

    def test_corners_property(self):
        """Test corners property calculation."""
        room = Room(x=10, y=20, width=20, height=10, label="Test")
        corners = room.corners
        assert len(corners) == 4
        assert (10, 20) in corners  # Bottom-left
        assert (30, 30) in corners  # Top-right

    def test_contains_point_inside(self):
        """Test contains_point for point inside room."""
        room = Room(x=0, y=0, width=10, height=10, label="Test")
        assert room.contains_point(5, 5) is True

    def test_contains_point_outside(self):
        """Test contains_point for point outside room."""
        room = Room(x=0, y=0, width=10, height=10, label="Test")
        assert room.contains_point(15, 15) is False

    def test_contains_point_on_edge(self):
        """Test contains_point for point on edge."""
        room = Room(x=0, y=0, width=10, height=10, label="Test")
        assert room.contains_point(10, 5) is True

    def test_overlaps_true(self):
        """Test overlaps for overlapping rooms."""
        room1 = Room(x=0, y=0, width=10, height=10, label="Room1")
        room2 = Room(x=5, y=5, width=10, height=10, label="Room2")
        assert room1.overlaps(room2) is True

    def test_overlaps_false(self):
        """Test overlaps for non-overlapping rooms."""
        room1 = Room(x=0, y=0, width=10, height=10, label="Room1")
        room2 = Room(x=20, y=20, width=10, height=10, label="Room2")
        assert room1.overlaps(room2) is False

    def test_overlaps_adjacent(self):
        """Test overlaps for adjacent rooms (should be False)."""
        room1 = Room(x=0, y=0, width=10, height=10, label="Room1")
        room2 = Room(x=10, y=0, width=10, height=10, label="Room2")
        assert room1.overlaps(room2) is False

    def test_get_display_label_simple(self):
        """Test get_display_label with just label."""
        room = Room(x=0, y=0, width=10, height=10, label="Bedroom")
        assert room.get_display_label() == "Bedroom"

    def test_get_display_label_with_dimensions(self):
        """Test get_display_label with dimensions."""
        room = Room(
            x=0,
            y=0,
            width=10,
            height=10,
            label="Bedroom",
            auto_dimension=True,
            dimension_text="10' x 10'",
        )
        label = room.get_display_label()
        assert "Bedroom" in label
        assert "10' x 10'" in label

    def test_get_display_label_with_notes(self):
        """Test get_display_label with notes."""
        room = Room(x=0, y=0, width=10, height=10, label="Bedroom", notes="Master Suite")
        label = room.get_display_label()
        assert "Bedroom" in label
        assert "Master Suite" in label

    def test_get_display_label_exclude_dimensions(self):
        """Test get_display_label with dimensions excluded."""
        room = Room(
            x=0,
            y=0,
            width=10,
            height=10,
            label="Bedroom",
            auto_dimension=True,
            dimension_text="10' x 10'",
        )
        label = room.get_display_label(include_dimensions=False)
        assert "Bedroom" in label
        assert "10' x 10'" not in label


# =============================================================================
# DOOR TESTS
# =============================================================================


class TestDoor:
    """Tests for Door dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        door = Door(x=10, y=20, width=3)
        assert door.direction == "right"
        assert door.swing == "up"

    def test_custom_values(self):
        """Test that custom values are accepted."""
        door = Door(x=10, y=20, width=3, direction="left", swing="down")
        assert door.x == 10
        assert door.y == 20
        assert door.width == 3
        assert door.direction == "left"
        assert door.swing == "down"

    def test_post_init_normalizes_negative_width(self):
        """Test that negative width is normalized."""
        door = Door(x=10, y=20, width=-3)
        assert door.width == 3

    def test_validate_valid_door(self):
        """Test validation for valid door."""
        door = Door(x=10, y=20, width=3)
        warnings = door.validate()
        assert len(warnings) == 0

    def test_validate_zero_width(self):
        """Test validation catches zero width."""
        door = Door(x=10, y=20, width=3)
        door.width = 0
        warnings = door.validate()
        assert any("width" in w.lower() for w in warnings)

    def test_validate_unusually_wide(self):
        """Test validation warns about unusually wide door."""
        door = Door(x=10, y=20, width=10)
        warnings = door.validate()
        assert any("wide" in w.lower() for w in warnings)

    def test_validate_unusually_narrow(self):
        """Test validation warns about unusually narrow door."""
        door = Door(x=10, y=20, width=1.5)
        warnings = door.validate()
        assert any("narrow" in w.lower() for w in warnings)

    def test_is_horizontal(self):
        """Test is_horizontal property."""
        door_h = Door(x=10, y=20, width=3, direction="right")
        door_v = Door(x=10, y=20, width=3, direction="up")
        assert door_h.is_horizontal is True
        assert door_v.is_horizontal is False

    def test_is_vertical(self):
        """Test is_vertical property."""
        door_h = Door(x=10, y=20, width=3, direction="right")
        door_v = Door(x=10, y=20, width=3, direction="up")
        assert door_h.is_vertical is False
        assert door_v.is_vertical is True

    def test_get_arc_config_valid(self):
        """Test get_arc_config for valid direction/swing combo."""
        door = Door(x=10, y=20, width=3, direction="right", swing="up")
        config = door.get_arc_config()
        assert config is not None
        assert len(config) == 3  # (offset, theta1, theta2)

    def test_get_arc_config_all_combinations(self):
        """Test get_arc_config for all valid combinations."""
        valid_combos: list[tuple[str, str]] = [
            ("right", "up"),
            ("right", "down"),
            ("left", "up"),
            ("left", "down"),
            ("up", "right"),
            ("up", "left"),
            ("down", "right"),
            ("down", "left"),
        ]
        for direction, swing in valid_combos:
            door = Door(
                x=10,
                y=20,
                width=3,
                direction=direction,  # type: ignore[arg-type]
                swing=swing,  # type: ignore[arg-type]
            )
            config = door.get_arc_config()
            assert config is not None


# =============================================================================
# WINDOW TESTS
# =============================================================================


class TestWindow:
    """Tests for Window dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        window = Window(x=5, y=10, width=4)
        assert window.orientation == "horizontal"

    def test_custom_values(self):
        """Test that custom values are accepted."""
        window = Window(x=5, y=10, width=4, orientation="vertical")
        assert window.x == 5
        assert window.y == 10
        assert window.width == 4
        assert window.orientation == "vertical"

    def test_post_init_normalizes_negative_width(self):
        """Test that negative width is normalized."""
        window = Window(x=5, y=10, width=-4)
        assert window.width == 4

    def test_validate_valid_window(self):
        """Test validation for valid window."""
        window = Window(x=5, y=10, width=4)
        warnings = window.validate()
        assert len(warnings) == 0

    def test_validate_zero_width(self):
        """Test validation catches zero width."""
        window = Window(x=5, y=10, width=4)
        window.width = 0
        warnings = window.validate()
        assert any("width" in w.lower() for w in warnings)

    def test_validate_unusually_wide(self):
        """Test validation warns about unusually wide window."""
        window = Window(x=5, y=10, width=25)
        warnings = window.validate()
        assert any("wide" in w.lower() for w in warnings)

    def test_is_horizontal(self):
        """Test is_horizontal property."""
        window_h = Window(x=5, y=10, width=4, orientation="horizontal")
        window_v = Window(x=5, y=10, width=4, orientation="vertical")
        assert window_h.is_horizontal is True
        assert window_v.is_horizontal is False

    def test_is_vertical(self):
        """Test is_vertical property."""
        window_h = Window(x=5, y=10, width=4, orientation="horizontal")
        window_v = Window(x=5, y=10, width=4, orientation="vertical")
        assert window_h.is_vertical is False
        assert window_v.is_vertical is True


# =============================================================================
# STAIRS TESTS
# =============================================================================


class TestStairs:
    """Tests for Stairs dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        stairs = Stairs(x=0, y=0, width=4, height=10)
        assert stairs.num_steps == 8
        assert stairs.orientation == "horizontal"
        assert stairs.label == ""

    def test_custom_values(self):
        """Test that custom values are accepted."""
        stairs = Stairs(
            x=10,
            y=20,
            width=5,
            height=12,
            num_steps=10,
            orientation="vertical",
            label="DN",
        )
        assert stairs.x == 10
        assert stairs.y == 20
        assert stairs.width == 5
        assert stairs.height == 12
        assert stairs.num_steps == 10
        assert stairs.orientation == "vertical"
        assert stairs.label == "DN"

    def test_post_init_normalizes_negative_dimensions(self):
        """Test that negative dimensions are normalized."""
        stairs = Stairs(x=0, y=0, width=-4, height=-10)
        assert stairs.width == 4
        assert stairs.height == 10

    def test_post_init_normalizes_zero_steps(self):
        """Test that zero steps is normalized."""
        stairs = Stairs(x=0, y=0, width=4, height=10, num_steps=0)
        assert stairs.num_steps == 1

    def test_step_size_horizontal(self):
        """Test step_size property for horizontal stairs."""
        stairs = Stairs(x=0, y=0, width=10, height=4, num_steps=5, orientation="horizontal")
        assert stairs.step_size == 2.0

    def test_step_size_vertical(self):
        """Test step_size property for vertical stairs."""
        stairs = Stairs(x=0, y=0, width=4, height=10, num_steps=5, orientation="vertical")
        assert stairs.step_size == 2.0

    def test_center_property(self):
        """Test center property calculation."""
        stairs = Stairs(x=10, y=20, width=4, height=10)
        center = stairs.center
        assert center == (12, 25)


# =============================================================================
# FIREPLACE TESTS
# =============================================================================


class TestFireplace:
    """Tests for Fireplace dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        fireplace = Fireplace(x=10, y=20, width=4, height=3)
        assert fireplace.label == ""

    def test_custom_values(self):
        """Test that custom values are accepted."""
        fireplace = Fireplace(x=10, y=20, width=4, height=3, label="Gas FP")
        assert fireplace.x == 10
        assert fireplace.y == 20
        assert fireplace.width == 4
        assert fireplace.height == 3
        assert fireplace.label == "Gas FP"

    def test_post_init_normalizes_negative_dimensions(self):
        """Test that negative dimensions are normalized."""
        fireplace = Fireplace(x=10, y=20, width=-4, height=-3)
        assert fireplace.width == 4
        assert fireplace.height == 3

    def test_center_property(self):
        """Test center property calculation."""
        fireplace = Fireplace(x=10, y=20, width=4, height=3)
        center = fireplace.center
        assert center == (12, 21.5)

    def test_inner_bounds_property(self):
        """Test inner_bounds property calculation."""
        fireplace = Fireplace(x=10, y=20, width=10, height=5)
        inner = fireplace.inner_bounds
        assert inner[0] == 12  # x + width * 0.2
        assert inner[1] == 20  # y
        assert inner[2] == 6  # width * 0.6
        assert inner[3] == 3.5  # height * 0.7


# =============================================================================
# FURNITURE TESTS
# =============================================================================


class TestFurniture:
    """Tests for Furniture dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        furniture = Furniture(furniture_type="rectangle", x=10, y=20, width=5)
        assert furniture.height == 0
        assert furniture.color == "#8b4513"
        assert furniture.edge_color == "black"
        assert furniture.label == ""

    def test_rectangle_furniture(self):
        """Test rectangle furniture type."""
        furniture = Furniture(
            furniture_type="rectangle", x=10, y=20, width=5, height=3, label="Table"
        )
        assert furniture.is_rectangle is True
        assert furniture.is_circle is False
        assert furniture.is_ellipse is False

    def test_circle_furniture(self):
        """Test circle furniture type."""
        furniture = Furniture(furniture_type="circle", x=10, y=20, width=5, label="Ottoman")
        assert furniture.is_rectangle is False
        assert furniture.is_circle is True
        assert furniture.is_ellipse is False

    def test_ellipse_furniture(self):
        """Test ellipse furniture type."""
        furniture = Furniture(furniture_type="ellipse", x=10, y=20, width=6, height=4, label="Rug")
        assert furniture.is_rectangle is False
        assert furniture.is_circle is False
        assert furniture.is_ellipse is True

    def test_post_init_normalizes_negative_dimensions(self):
        """Test that negative dimensions are normalized."""
        furniture = Furniture(furniture_type="rectangle", x=10, y=20, width=-5, height=-3)
        assert furniture.width == 5
        assert furniture.height == 3

    def test_post_init_circle_height_defaults_to_width(self):
        """Test that circle height defaults to width."""
        furniture = Furniture(furniture_type="circle", x=10, y=20, width=5, height=0)
        assert furniture.height == 5

    def test_center_rectangle(self):
        """Test center property for rectangle."""
        furniture = Furniture(furniture_type="rectangle", x=10, y=20, width=10, height=6)
        center = furniture.center
        assert center == (15, 23)

    def test_center_circle(self):
        """Test center property for circle (x, y is already center)."""
        furniture = Furniture(furniture_type="circle", x=10, y=20, width=5)
        center = furniture.center
        assert center == (10, 20)


# =============================================================================
# TEXT ANNOTATION TESTS
# =============================================================================


class TestTextAnnotation:
    """Tests for TextAnnotation dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        annotation = TextAnnotation(x=50, y=50, text="Test")
        assert annotation.fontsize == 8
        assert annotation.color == "black"
        assert annotation.ha == "center"
        assert annotation.va == "center"
        assert annotation.rotation == 0
        assert annotation.fontweight == "normal"
        assert annotation.style == "normal"

    def test_custom_values(self):
        """Test that custom values are accepted."""
        annotation = TextAnnotation(
            x=50,
            y=50,
            text="Test",
            fontsize=12,
            color="red",
            ha="left",
            va="top",
            rotation=45,
            fontweight="bold",
            style="italic",
        )
        assert annotation.fontsize == 12
        assert annotation.color == "red"
        assert annotation.ha == "left"
        assert annotation.va == "top"
        assert annotation.rotation == 45

    def test_post_init_normalizes_fontsize(self):
        """Test that invalid fontsize is normalized."""
        annotation = TextAnnotation(x=50, y=50, text="Test", fontsize=0)
        assert annotation.fontsize == 8

    def test_post_init_normalizes_alignment(self):
        """Test that invalid alignment is normalized."""
        annotation = TextAnnotation(x=50, y=50, text="Test", ha="invalid", va="invalid")
        assert annotation.ha == "center"
        assert annotation.va == "center"


# =============================================================================
# LINE ANNOTATION TESTS
# =============================================================================


class TestLineAnnotation:
    """Tests for LineAnnotation dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        line = LineAnnotation(x1=0, y1=0, x2=10, y2=10)
        assert line.color == "black"
        assert line.linewidth == 2
        assert line.linestyle == "-"
        assert line.zorder == 5

    def test_custom_values(self):
        """Test that custom values are accepted."""
        line = LineAnnotation(
            x1=0, y1=0, x2=10, y2=10, color="red", linewidth=3, linestyle="--", zorder=10
        )
        assert line.color == "red"
        assert line.linewidth == 3
        assert line.linestyle == "--"
        assert line.zorder == 10

    def test_length_property(self):
        """Test length property calculation."""
        line = LineAnnotation(x1=0, y1=0, x2=3, y2=4)
        assert line.length == 5.0  # 3-4-5 triangle

    def test_midpoint_property(self):
        """Test midpoint property calculation."""
        line = LineAnnotation(x1=0, y1=0, x2=10, y2=20)
        midpoint = line.midpoint
        assert midpoint == (5, 10)

    def test_is_horizontal(self):
        """Test is_horizontal property."""
        line_h = LineAnnotation(x1=0, y1=5, x2=10, y2=5)
        line_v = LineAnnotation(x1=5, y1=0, x2=5, y2=10)
        line_d = LineAnnotation(x1=0, y1=0, x2=10, y2=10)
        assert line_h.is_horizontal is True
        assert line_v.is_horizontal is False
        assert line_d.is_horizontal is False

    def test_is_vertical(self):
        """Test is_vertical property."""
        line_h = LineAnnotation(x1=0, y1=5, x2=10, y2=5)
        line_v = LineAnnotation(x1=5, y1=0, x2=5, y2=10)
        line_d = LineAnnotation(x1=0, y1=0, x2=10, y2=10)
        assert line_h.is_vertical is False
        assert line_v.is_vertical is True
        assert line_d.is_vertical is False


# =============================================================================
# THEATER SEATING TESTS
# =============================================================================


class TestTheaterSeating:
    """Tests for TheaterSeating dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        seating = TheaterSeating(start_x=10, start_y=20)
        assert seating.rows == 4
        assert seating.seats_per_row == 5
        assert seating.chair_width == 4
        assert seating.chair_height == 3
        assert seating.row_spacing == 6
        assert seating.seat_spacing == 5

    def test_custom_values(self):
        """Test that custom values are accepted."""
        seating = TheaterSeating(
            start_x=10,
            start_y=20,
            rows=3,
            seats_per_row=6,
            chair_width=3,
            chair_height=2.5,
            row_spacing=5,
            seat_spacing=4,
        )
        assert seating.rows == 3
        assert seating.seats_per_row == 6

    def test_post_init_normalizes_invalid_rows(self):
        """Test that invalid rows is normalized."""
        seating = TheaterSeating(start_x=10, start_y=20, rows=0)
        assert seating.rows == 1

    def test_post_init_normalizes_invalid_seats(self):
        """Test that invalid seats_per_row is normalized."""
        seating = TheaterSeating(start_x=10, start_y=20, seats_per_row=-1)
        assert seating.seats_per_row == 1

    def test_total_seats(self):
        """Test total_seats property calculation."""
        seating = TheaterSeating(start_x=10, start_y=20, rows=3, seats_per_row=5)
        assert seating.total_seats == 15

    def test_total_width(self):
        """Test total_width property calculation."""
        seating = TheaterSeating(start_x=10, start_y=20, rows=3, row_spacing=6)
        assert seating.total_width == 18

    def test_total_height(self):
        """Test total_height property calculation."""
        seating = TheaterSeating(start_x=10, start_y=20, seats_per_row=5, seat_spacing=5)
        assert seating.total_height == 25

    def test_get_seat_position(self):
        """Test get_seat_position method."""
        seating = TheaterSeating(start_x=10, start_y=20, row_spacing=6, seat_spacing=5)
        pos = seating.get_seat_position(1, 2)
        assert pos == (16, 30)  # (10 + 1*6, 20 + 2*5)


# =============================================================================
# POOL CONFIG TESTS
# =============================================================================


class TestPoolConfig:
    """Tests for PoolConfig dataclass."""

    def test_required_fields(self):
        """Test that required fields work correctly."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=5,
            pool_y=5,
            pool_width=25,
            pool_height=20,
            hot_tub_x=35,
            hot_tub_y=10,
        )
        assert pool.area_x == 0
        assert pool.pool_width == 25
        assert pool.hot_tub_x == 35

    def test_default_values(self):
        """Test that default values are set correctly."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=5,
            pool_y=5,
            pool_width=25,
            pool_height=20,
            hot_tub_x=35,
            hot_tub_y=10,
        )
        assert pool.area_color == "#e0f7fa"
        assert pool.hot_tub_radius == 4
        assert pool.hot_tub_label == "Hot\nTub"

    def test_post_init_normalizes_negative_dimensions(self):
        """Test that negative dimensions are normalized."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=-40,
            area_height=-30,
            pool_x=5,
            pool_y=5,
            pool_width=-25,
            pool_height=-20,
            hot_tub_x=35,
            hot_tub_y=10,
            hot_tub_radius=-4,
        )
        assert pool.area_width == 40
        assert pool.pool_height == 20
        assert pool.hot_tub_radius == 4

    def test_pool_area_property(self):
        """Test pool_area property calculation."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=5,
            pool_y=5,
            pool_width=25,
            pool_height=20,
            hot_tub_x=35,
            hot_tub_y=10,
        )
        assert pool.pool_area == 500  # 25 * 20

    def test_total_area_property(self):
        """Test total_area property calculation."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=5,
            pool_y=5,
            pool_width=25,
            pool_height=20,
            hot_tub_x=35,
            hot_tub_y=10,
        )
        assert pool.total_area == 1200  # 40 * 30

    def test_pool_center_property(self):
        """Test pool_center property calculation."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=0,
            pool_y=0,
            pool_width=20,
            pool_height=10,
            hot_tub_x=35,
            hot_tub_y=10,
        )
        center = pool.pool_center
        assert center == (10, 5)

    def test_has_hot_tub_true(self):
        """Test has_hot_tub property when hot tub exists."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=5,
            pool_y=5,
            pool_width=25,
            pool_height=20,
            hot_tub_x=35,
            hot_tub_y=10,
            hot_tub_radius=4,
        )
        assert pool.has_hot_tub is True

    def test_has_hot_tub_false(self):
        """Test has_hot_tub property when no hot tub."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=5,
            pool_y=5,
            pool_width=25,
            pool_height=20,
            hot_tub_x=35,
            hot_tub_y=10,
            hot_tub_radius=0,
        )
        assert pool.has_hot_tub is False


# =============================================================================
# FLOOR PLAN TESTS
# =============================================================================


class TestFloorPlan:
    """Tests for FloorPlan dataclass."""

    def test_empty_floor_plan(self):
        """Test creating an empty floor plan."""
        plan = FloorPlan(name="Test")
        assert plan.name == "Test"
        assert len(plan.rooms) == 0
        assert len(plan.doors) == 0
        assert plan.total_area == 0

    def test_floor_plan_with_rooms(self):
        """Test floor plan with rooms."""
        plan = FloorPlan(
            name="Test",
            rooms=[
                Room(x=0, y=0, width=10, height=10, label="Room1"),
                Room(x=10, y=0, width=15, height=10, label="Room2"),
            ],
        )
        assert len(plan.rooms) == 2
        assert plan.total_area == 250  # 100 + 150

    def test_room_count(self):
        """Test room_count property."""
        plan = FloorPlan(
            name="Test",
            rooms=[
                Room(x=0, y=0, width=10, height=10, label="Room1"),
                Room(x=10, y=0, width=10, height=10, label="Room2"),
                Room(x=20, y=0, width=10, height=10, label="Room3"),
            ],
        )
        assert plan.room_count == 3

    def test_get_rooms_by_color(self):
        """Test get_rooms_by_color method."""
        plan = FloorPlan(
            name="Test",
            rooms=[
                Room(x=0, y=0, width=10, height=10, label="Bedroom1", color="bedroom"),
                Room(x=10, y=0, width=10, height=10, label="Kitchen", color="kitchen"),
                Room(x=20, y=0, width=10, height=10, label="Bedroom2", color="bedroom"),
            ],
        )
        bedrooms = plan.get_rooms_by_color("bedroom")
        assert len(bedrooms) == 2
        kitchens = plan.get_rooms_by_color("kitchen")
        assert len(kitchens) == 1

    def test_get_room_by_label(self):
        """Test get_room_by_label method."""
        plan = FloorPlan(
            name="Test",
            rooms=[
                Room(x=0, y=0, width=10, height=10, label="Bedroom"),
                Room(x=10, y=0, width=10, height=10, label="Kitchen"),
            ],
        )
        room = plan.get_room_by_label("Kitchen")
        assert room is not None
        assert room.label == "Kitchen"

    def test_get_room_by_label_case_insensitive(self):
        """Test get_room_by_label is case insensitive."""
        plan = FloorPlan(
            name="Test",
            rooms=[Room(x=0, y=0, width=10, height=10, label="Kitchen")],
        )
        room = plan.get_room_by_label("kitchen")
        assert room is not None

    def test_get_room_by_label_not_found(self):
        """Test get_room_by_label returns None when not found."""
        plan = FloorPlan(
            name="Test",
            rooms=[Room(x=0, y=0, width=10, height=10, label="Kitchen")],
        )
        room = plan.get_room_by_label("Bedroom")
        assert room is None

    def test_validate_empty_plan(self):
        """Test validation of empty plan."""
        plan = FloorPlan(name="Test")
        warnings = plan.validate()
        assert len(warnings) == 0

    def test_validate_with_invalid_room(self):
        """Test validation catches invalid rooms."""
        plan = FloorPlan(
            name="Test",
            rooms=[Room(x=0, y=0, width=10, height=10, label="Room")],
        )
        plan.rooms[0].width = 0
        warnings = plan.validate()
        assert len(warnings) > 0

    def test_get_bounds_empty(self):
        """Test get_bounds for empty plan."""
        plan = FloorPlan(name="Test")
        bounds = plan.get_bounds()
        assert bounds == (0, 0, 0, 0)

    def test_get_bounds_with_rooms(self):
        """Test get_bounds with rooms."""
        plan = FloorPlan(
            name="Test",
            rooms=[
                Room(x=10, y=20, width=30, height=40, label="Room1"),
                Room(x=50, y=10, width=20, height=50, label="Room2"),
            ],
        )
        bounds = plan.get_bounds()
        assert bounds == (10, 10, 70, 60)  # min_x, min_y, max_x, max_y

    def test_get_dimensions(self):
        """Test get_dimensions method."""
        plan = FloorPlan(
            name="Test",
            rooms=[
                Room(x=0, y=0, width=50, height=30, label="Room"),
            ],
        )
        dims = plan.get_dimensions()
        assert dims == (50, 30)

    def test_find_room_at(self):
        """Test find_room_at method."""
        room = Room(x=10, y=10, width=20, height=20, label="Target")
        plan = FloorPlan(name="Test", rooms=[room])
        found = plan.find_room_at(15, 15)
        assert found is room

    def test_find_room_at_not_found(self):
        """Test find_room_at returns None when no room at point."""
        plan = FloorPlan(
            name="Test",
            rooms=[Room(x=10, y=10, width=10, height=10, label="Room")],
        )
        found = plan.find_room_at(0, 0)
        assert found is None

    def test_to_dict(self):
        """Test to_dict method."""
        plan = FloorPlan(
            name="Test",
            rooms=[Room(x=0, y=0, width=10, height=10, label="Room")],
            doors=[Door(x=5, y=0, width=3)],
        )
        result = plan.to_dict()
        assert result["name"] == "Test"
        assert len(result["rooms"]) == 1
        assert len(result["doors"]) == 1


# =============================================================================
# FLOOR PLAN BUILDER TESTS
# =============================================================================


class TestFloorPlanBuilder:
    """Tests for FloorPlanBuilder class."""

    def test_basic_builder(self):
        """Test basic builder usage."""
        plan = FloorPlanBuilder("Test Plan").build()
        assert plan.name == "Test Plan"
        assert len(plan.rooms) == 0

    def test_add_room(self):
        """Test adding a room via builder."""
        plan = (
            FloorPlanBuilder("Test")
            .add_room(x=0, y=0, width=10, height=10, label="Living Room", color="living")
            .build()
        )
        assert len(plan.rooms) == 1
        assert plan.rooms[0].label == "Living Room"

    def test_add_door(self):
        """Test adding a door via builder."""
        plan = (
            FloorPlanBuilder("Test")
            .add_door(x=5, y=0, width=3, direction="up", swing="right")
            .build()
        )
        assert len(plan.doors) == 1
        assert plan.doors[0].direction == "up"

    def test_add_window(self):
        """Test adding a window via builder."""
        plan = (
            FloorPlanBuilder("Test").add_window(x=2, y=0, width=4, orientation="horizontal").build()
        )
        assert len(plan.windows) == 1

    def test_add_stairs(self):
        """Test adding stairs via builder."""
        plan = (
            FloorPlanBuilder("Test")
            .add_stairs(x=0, y=0, width=4, height=10, num_steps=8, label="DN")
            .build()
        )
        assert len(plan.stairs) == 1
        assert plan.stairs[0].label == "DN"

    def test_add_fireplace(self):
        """Test adding fireplace via builder."""
        plan = (
            FloorPlanBuilder("Test")
            .add_fireplace(x=10, y=20, width=4, height=3, label="Gas FP")
            .build()
        )
        assert len(plan.fireplaces) == 1

    def test_add_furniture(self):
        """Test adding furniture via builder."""
        plan = (
            FloorPlanBuilder("Test")
            .add_furniture(furniture_type="rectangle", x=5, y=5, width=6, height=3, label="Table")
            .build()
        )
        assert len(plan.furniture) == 1

    def test_add_text(self):
        """Test adding text annotation via builder."""
        plan = (
            FloorPlanBuilder("Test").add_text(x=50, y=50, text="Hello World", fontsize=12).build()
        )
        assert len(plan.text_annotations) == 1
        assert plan.text_annotations[0].text == "Hello World"

    def test_add_line(self):
        """Test adding line annotation via builder."""
        plan = (
            FloorPlanBuilder("Test")
            .add_line(x1=0, y1=0, x2=10, y2=10, color="red", linestyle="--")
            .build()
        )
        assert len(plan.line_annotations) == 1
        assert plan.line_annotations[0].color == "red"

    def test_fluent_chaining(self):
        """Test that builder methods return self for chaining."""
        plan = (
            FloorPlanBuilder("My House")
            .add_room(x=0, y=0, width=20, height=15, label="Living Room", color="living")
            .add_room(x=20, y=0, width=15, height=15, label="Kitchen", color="kitchen")
            .add_door(x=20, y=5, width=3, direction="right", swing="up")
            .add_window(x=5, y=0, width=6, orientation="horizontal")
            .add_fireplace(x=10, y=13, width=4, height=2)
            .build()
        )
        assert len(plan.rooms) == 2
        assert len(plan.doors) == 1
        assert len(plan.windows) == 1
        assert len(plan.fireplaces) == 1

    def test_validate(self):
        """Test builder validation method."""
        builder = FloorPlanBuilder("Test")
        builder.add_room(x=0, y=0, width=10, height=10, label="Room")
        warnings = builder.validate()
        assert isinstance(warnings, list)


# =============================================================================
# ROOM TEMPLATES TESTS
# =============================================================================


class TestRoomTemplates:
    """Tests for RoomTemplates class."""

    def test_add_bedroom_suite(self):
        """Test adding a bedroom suite template."""
        builder = FloorPlanBuilder("Test")
        RoomTemplates.add_bedroom_suite(builder, x=0, y=0, width=20, height=15, name="Master")
        plan = builder.build()
        # Should have bedroom, bathroom, and closet
        assert len(plan.rooms) >= 3
        # Should have doors between rooms
        assert len(plan.doors) >= 2

    def test_add_kitchen_layout_with_pantry(self):
        """Test adding kitchen with pantry."""
        builder = FloorPlanBuilder("Test")
        RoomTemplates.add_kitchen_layout(builder, x=0, y=0, width=20, height=12, with_pantry=True)
        plan = builder.build()
        assert len(plan.rooms) == 2  # Kitchen and pantry
        assert len(plan.doors) == 1  # Door to pantry

    def test_add_kitchen_layout_without_pantry(self):
        """Test adding kitchen without pantry."""
        builder = FloorPlanBuilder("Test")
        RoomTemplates.add_kitchen_layout(builder, x=0, y=0, width=15, height=12, with_pantry=False)
        plan = builder.build()
        assert len(plan.rooms) == 1  # Just kitchen

    def test_add_garage(self):
        """Test adding garage template."""
        builder = FloorPlanBuilder("Test")
        RoomTemplates.add_garage(builder, x=0, y=0, width=24, height=24, cars=2)
        plan = builder.build()
        assert len(plan.rooms) == 1
        assert "2 Car" in plan.rooms[0].label

    def test_add_garage_single_car(self):
        """Test adding single car garage."""
        builder = FloorPlanBuilder("Test")
        RoomTemplates.add_garage(builder, x=0, y=0, width=12, height=20, cars=1)
        plan = builder.build()
        assert "Garage" in plan.rooms[0].label
        assert "2 Car" not in plan.rooms[0].label

    def test_add_theater_room(self):
        """Test adding theater room template."""
        builder = FloorPlanBuilder("Test")
        RoomTemplates.add_theater_room(
            builder, x=0, y=0, width=30, height=20, rows=4, seats_per_row=5
        )
        plan = builder.build()
        assert len(plan.rooms) == 1
        assert plan.rooms[0].color == "theater"
        # Should have seating annotation
        assert len(plan.text_annotations) == 1

    def test_add_pool_area(self):
        """Test adding pool area template."""
        builder = FloorPlanBuilder("Test")
        RoomTemplates.add_pool_area(builder, x=0, y=0, width=50, height=40, with_hot_tub=True)
        plan = builder.build()
        assert len(plan.rooms) == 1
        assert plan.rooms[0].color == "pool_area"


# =============================================================================
# EDGE CASES AND REGRESSION TESTS
# =============================================================================


class TestEdgeCases:
    """Tests for edge cases and potential bugs."""

    def test_room_with_zero_position(self):
        """Test room at origin."""
        room = Room(x=0, y=0, width=10, height=10, label="Origin")
        assert room.center == (5, 5)
        assert room.contains_point(0, 0) is True

    def test_room_with_negative_position(self):
        """Test room with negative coordinates."""
        room = Room(x=-10, y=-20, width=15, height=25, label="Negative")
        assert room.center == (-2.5, -7.5)
        assert room.bounds == (-10, -20, 5, 5)

    def test_room_with_very_small_dimensions(self):
        """Test room with very small dimensions."""
        room = Room(x=0, y=0, width=0.5, height=0.5, label="Tiny")
        assert room.area == 0.25
        assert room.contains_point(0.25, 0.25) is True

    def test_room_with_large_dimensions(self):
        """Test room with large dimensions."""
        room = Room(x=0, y=0, width=1000, height=1000, label="Huge")
        warnings = room.validate()
        # Should warn about large dimensions
        assert len(warnings) >= 2

    def test_door_direction_swing_combinations(self):
        """Test all valid door direction/swing combinations."""
        valid_combos: list[tuple[str, str]] = [
            ("right", "up"),
            ("right", "down"),
            ("left", "up"),
            ("left", "down"),
            ("up", "right"),
            ("up", "left"),
            ("down", "right"),
            ("down", "left"),
        ]
        for direction, swing in valid_combos:
            door = Door(x=0, y=0, width=3, direction=direction, swing=swing)  # type: ignore[arg-type]
            assert door.get_arc_config() is not None, f"Failed for {direction}, {swing}"

    def test_stairs_single_step(self):
        """Test stairs with single step."""
        # For horizontal stairs, step_size = width / num_steps = 4 / 1 = 4.0
        stairs = Stairs(x=0, y=0, width=4, height=1, num_steps=1)
        assert stairs.step_size == 4.0

    def test_empty_floor_plan_methods(self):
        """Test FloorPlan methods on empty plan."""
        plan = FloorPlan(name="Empty")
        assert plan.total_area == 0
        assert plan.room_count == 0
        assert plan.get_bounds() == (0, 0, 0, 0)
        assert plan.get_dimensions() == (0, 0)
        assert plan.find_room_at(5, 5) is None
        assert plan.get_rooms_by_color("bedroom") == []
        assert plan.get_room_by_label("Test") is None

    def test_overlapping_rooms_detection(self):
        """Test that overlapping rooms are detected in validation."""
        plan = FloorPlan(
            name="Overlap Test",
            rooms=[
                Room(x=0, y=0, width=20, height=20, label="Room1"),
                Room(x=10, y=10, width=20, height=20, label="Room2"),  # Overlaps!
            ],
        )
        warnings = plan.validate()
        assert any("overlap" in w.lower() for w in warnings)

    def test_line_annotation_zero_length(self):
        """Test line with zero length."""
        line = LineAnnotation(x1=5, y1=5, x2=5, y2=5)
        assert line.length == 0

    def test_furniture_rotation(self):
        """Test furniture with rotation."""
        furniture = Furniture(
            furniture_type="rectangle",
            x=10,
            y=20,
            width=6,
            height=3,
            rotation=45,
        )
        assert furniture.rotation == 45
        # Center should still be calculated correctly
        assert furniture.center == (13, 21.5)


# =============================================================================
# PROPERTY-BASED STYLE TESTS
# =============================================================================


class TestPropertyBased:
    """Property-based style tests for models."""

    @pytest.mark.parametrize(
        "width,height",
        [
            (1, 1),
            (10, 10),
            (100, 50),
            (0.5, 0.5),
            (50, 100),
        ],
    )
    def test_room_area_matches_dimensions(self, width, height):
        """Test that room area equals width * height."""
        room = Room(x=0, y=0, width=width, height=height, label="Test")
        assert room.area == width * height

    @pytest.mark.parametrize(
        "x,y,width,height",
        [
            (0, 0, 10, 10),
            (10, 20, 30, 40),
            (-5, -5, 15, 15),
            (0, 0, 100, 100),
        ],
    )
    def test_room_bounds_consistency(self, x, y, width, height):
        """Test that bounds are consistent with position and dimensions."""
        room = Room(x=x, y=y, width=width, height=height, label="Test")
        x_min, y_min, x_max, y_max = room.bounds
        assert x_max - x_min == width
        assert y_max - y_min == height

    @pytest.mark.parametrize(
        "x,y,width,height",
        [
            (0, 0, 10, 10),
            (5, 5, 20, 20),
            (10, 20, 30, 40),
        ],
    )
    def test_room_center_is_inside(self, x, y, width, height):
        """Test that room center is always inside the room."""
        room = Room(x=x, y=y, width=width, height=height, label="Test")
        cx, cy = room.center
        assert room.contains_point(cx, cy) is True

    @pytest.mark.parametrize("num_steps", [1, 2, 5, 10, 20])
    def test_stairs_step_size_times_steps_equals_dimension(self, num_steps):
        """Test that step_size * num_steps equals the relevant dimension."""
        stairs_h = Stairs(
            x=0, y=0, width=20, height=4, num_steps=num_steps, orientation="horizontal"
        )
        assert abs(stairs_h.step_size * num_steps - 20) < 0.001

        stairs_v = Stairs(x=0, y=0, width=4, height=20, num_steps=num_steps, orientation="vertical")
        assert abs(stairs_v.step_size * num_steps - 20) < 0.001

    @pytest.mark.parametrize("rows,seats", [(1, 1), (2, 3), (4, 5), (3, 6)])
    def test_theater_total_seats(self, rows, seats):
        """Test that total_seats equals rows * seats_per_row."""
        seating = TheaterSeating(start_x=0, start_y=0, rows=rows, seats_per_row=seats)
        assert seating.total_seats == rows * seats

    @pytest.mark.parametrize(
        "x1,y1,x2,y2",
        [
            (0, 0, 3, 4),  # 3-4-5 triangle
            (0, 0, 6, 8),  # 6-8-10 triangle
            (0, 0, 5, 12),  # 5-12-13 triangle
            (1, 1, 4, 5),  # 3-4-5 triangle shifted
        ],
    )
    def test_line_length_pythagorean(self, x1, y1, x2, y2):
        """Test line length follows Pythagorean theorem."""
        line = LineAnnotation(x1=x1, y1=y1, x2=x2, y2=y2)
        dx = x2 - x1
        dy = y2 - y1
        expected = (dx**2 + dy**2) ** 0.5
        assert abs(line.length - expected) < 0.001
