"""
Tests for the drawing package.

This module tests all drawing functions including:
- Debug grid drawing
- Room drawing functions
- Door drawing functions
- Window drawing functions
- Stairs drawing functions
- Fireplace drawing functions
- Furniture drawing functions
- Annotation drawing functions
- Special elements (theater seating, pool area)
- Batch drawing functions
"""

import matplotlib.pyplot as plt
import pytest
from drawing import (
    add_dimension_arrow,
    add_door,
    add_door_simple,
    add_fireplace,
    add_fireplace_simple,
    add_furniture,
    add_furniture_simple,
    add_line_annotation,
    add_north_arrow,
    add_pool_area,
    add_room,
    add_room_simple,
    add_stairs,
    add_stairs_simple,
    add_text_annotation,
    add_theater_seating,
    add_window,
    add_window_simple,
    draw_debug_grid,
    draw_doors_from_data,
    draw_fireplaces_from_data,
    draw_furniture_from_data,
    draw_lines_from_data,
    draw_rooms_from_data,
    draw_stairs_from_data,
    draw_text_annotations_from_data,
    draw_windows_from_data,
)
from matplotlib.patches import Circle, Rectangle
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
from utilities import set_auto_dimensions, set_scale


@pytest.fixture
def fig_ax():
    """Create a matplotlib figure and axes for testing."""
    fig, ax = plt.subplots(figsize=(10, 10))
    yield fig, ax
    plt.close(fig)


@pytest.fixture
def clean_axes():
    """Create clean axes for each test."""
    fig, ax = plt.subplots()
    yield ax
    plt.close(fig)


class TestDrawDebugGrid:
    """Tests for the draw_debug_grid() function."""

    def test_grid_creates_lines(self, clean_axes):
        """Test that debug grid creates lines on axes."""
        initial_children = len(clean_axes.get_children())
        draw_debug_grid(clean_axes, x_min=0, x_max=100, y_min=0, y_max=100, spacing=10)
        # Should have added lines
        assert len(clean_axes.get_children()) > initial_children

    def test_grid_with_different_spacing(self, clean_axes):
        """Test grid with different spacing values."""
        draw_debug_grid(clean_axes, x_min=0, x_max=100, y_min=0, y_max=100, spacing=20)
        # Should complete without error
        assert True

    def test_grid_small_area(self, clean_axes):
        """Test grid on a small area."""
        draw_debug_grid(clean_axes, 0, 20, 0, 20, spacing=5)
        assert True


class TestAddRoom:
    """Tests for the add_room() function."""

    def test_add_room_creates_rectangle(self, clean_axes):
        """Test that add_room creates a rectangle patch."""
        room = Room(x=10, y=20, width=15, height=12, label="Test Room")
        add_room(clean_axes, room)

        # Check that patches were added
        patches = [p for p in clean_axes.patches if isinstance(p, Rectangle)]
        assert len(patches) >= 1

    def test_add_room_with_color(self, clean_axes):
        """Test add_room with a specific color."""
        room = Room(
            x=0, y=0, width=10, height=10, label="Colored Room", color="#ff0000"
        )
        add_room(clean_axes, room)
        patches = [p for p in clean_axes.patches if isinstance(p, Rectangle)]
        assert len(patches) >= 1

    def test_add_room_with_dimension_text(self, clean_axes):
        """Test add_room with auto dimension enabled."""
        set_auto_dimensions(True)
        room = Room(
            x=0,
            y=0,
            width=15,
            height=12,
            label="Dimensioned Room",
            auto_dimension=True,
            dimension_text="15' x 12'",
        )
        add_room(clean_axes, room)
        # Should add text annotation for dimensions
        texts = clean_axes.texts
        assert len(texts) >= 1


class TestAddRoomSimple:
    """Tests for the add_room_simple() function."""

    def test_add_room_simple_with_params(self, clean_axes):
        """Test add_room_simple with individual parameters."""
        add_room_simple(
            clean_axes,
            x=0,
            y=0,
            width=10,
            height=8,
            label="Simple Room",
            color="bedroom",
        )
        patches = [p for p in clean_axes.patches if isinstance(p, Rectangle)]
        assert len(patches) >= 1

    def test_add_room_simple_minimal_params(self, clean_axes):
        """Test add_room_simple with minimal parameters."""
        add_room_simple(clean_axes, x=5, y=5, width=10, height=10, label="Min")
        assert len(clean_axes.patches) >= 1


class TestAddDoor:
    """Tests for the add_door() function."""

    def test_add_door_creates_elements(self, clean_axes):
        """Test that add_door creates visual elements."""
        door = Door(x=10, y=20, width=3, direction="right", swing="up")
        initial_children = len(clean_axes.get_children())
        add_door(clean_axes, door)
        # Should add arc for door swing and line for door
        assert len(clean_axes.get_children()) > initial_children

    def test_add_door_different_directions(self, clean_axes):
        """Test add_door with different directions."""
        from typing import Literal

        directions: list[Literal["right", "left", "up", "down"]] = [
            "right",
            "left",
            "up",
            "down",
        ]
        for direction in directions:
            door = Door(x=10, y=10, width=3, direction=direction, swing="up")
            add_door(clean_axes, door)
        # Should complete without error
        assert True

    def test_add_door_different_swings(self, clean_axes):
        """Test add_door with different swing directions."""
        from typing import Literal

        swings: list[Literal["up", "down", "left", "right"]] = [
            "up",
            "down",
            "left",
            "right",
        ]
        for swing in swings:
            door = Door(x=10, y=10, width=3, direction="right", swing=swing)
            add_door(clean_axes, door)
        assert True


class TestAddDoorSimple:
    """Tests for the add_door_simple() function."""

    def test_add_door_simple_with_params(self, clean_axes):
        """Test add_door_simple with individual parameters."""
        add_door_simple(clean_axes, x=15, y=25, width=3, direction="left", swing="down")
        # Should complete without error
        assert True


class TestAddWindow:
    """Tests for the add_window() function."""

    def test_add_window_creates_rectangle(self, clean_axes):
        """Test that add_window creates a rectangle patch."""
        window = Window(x=10, y=0, width=4, orientation="horizontal")
        add_window(clean_axes, window)
        patches = [p for p in clean_axes.patches if isinstance(p, Rectangle)]
        assert len(patches) >= 1

    def test_add_window_horizontal(self, clean_axes):
        """Test add_window with horizontal orientation."""
        window = Window(x=10, y=0, width=4, orientation="horizontal")
        add_window(clean_axes, window)
        assert True

    def test_add_window_vertical(self, clean_axes):
        """Test add_window with vertical orientation."""
        window = Window(x=0, y=10, width=4, orientation="vertical")
        add_window(clean_axes, window)
        assert True


class TestAddWindowSimple:
    """Tests for the add_window_simple() function."""

    def test_add_window_simple_with_params(self, clean_axes):
        """Test add_window_simple with individual parameters."""
        add_window_simple(clean_axes, x=5, y=0, width=3, orientation="horizontal")
        assert len(clean_axes.patches) >= 1


class TestAddStairs:
    """Tests for the add_stairs() function."""

    def test_add_stairs_creates_elements(self, clean_axes):
        """Test that add_stairs creates visual elements."""
        stairs = Stairs(x=30, y=40, width=4, height=10, num_steps=8)
        initial_patches = len(clean_axes.patches)
        add_stairs(clean_axes, stairs)
        # Should add multiple rectangles for steps
        assert len(clean_axes.patches) > initial_patches

    def test_add_stairs_horizontal(self, clean_axes):
        """Test add_stairs with horizontal orientation."""
        stairs = Stairs(
            x=0, y=0, width=4, height=10, num_steps=8, orientation="horizontal"
        )
        add_stairs(clean_axes, stairs)
        assert True

    def test_add_stairs_vertical(self, clean_axes):
        """Test add_stairs with vertical orientation."""
        stairs = Stairs(
            x=0, y=0, width=10, height=4, num_steps=8, orientation="vertical"
        )
        add_stairs(clean_axes, stairs)
        assert True

    def test_add_stairs_with_label(self, clean_axes):
        """Test add_stairs with a label."""
        stairs = Stairs(x=0, y=0, width=4, height=10, num_steps=8, label="Main Stairs")
        add_stairs(clean_axes, stairs)
        assert True


class TestAddStairsSimple:
    """Tests for the add_stairs_simple() function."""

    def test_add_stairs_simple_with_params(self, clean_axes):
        """Test add_stairs_simple with individual parameters."""
        add_stairs_simple(
            clean_axes,
            x=10,
            y=20,
            width=4,
            height=12,
            num_steps=10,
            orientation="vertical",
        )
        assert len(clean_axes.patches) >= 1


class TestAddFireplace:
    """Tests for the add_fireplace() function."""

    def test_add_fireplace_creates_elements(self, clean_axes):
        """Test that add_fireplace creates visual elements."""
        fireplace = Fireplace(x=20, y=30, width=5, height=2)
        add_fireplace(clean_axes, fireplace)
        # Should add patches for fireplace outline and interior
        assert len(clean_axes.patches) >= 1

    def test_add_fireplace_with_label(self, clean_axes):
        """Test add_fireplace with a label."""
        fireplace = Fireplace(x=20, y=30, width=6, height=3, label="Stone Fireplace")
        add_fireplace(clean_axes, fireplace)
        assert True


class TestAddFireplaceSimple:
    """Tests for the add_fireplace_simple() function."""

    def test_add_fireplace_simple_with_params(self, clean_axes):
        """Test add_fireplace_simple with individual parameters."""
        add_fireplace_simple(clean_axes, x=15, y=25, width=5, height=2)
        assert len(clean_axes.patches) >= 1


class TestAddFurniture:
    """Tests for the add_furniture() function."""

    def test_add_furniture_rectangle(self, clean_axes):
        """Test add_furniture with rectangle type."""
        furniture = Furniture(
            furniture_type="rectangle",
            x=10,
            y=20,
            width=6,
            height=4,
            color="#8b4513",
            label="Table",
        )
        add_furniture(clean_axes, furniture)
        patches = [p for p in clean_axes.patches if isinstance(p, Rectangle)]
        assert len(patches) >= 1

    def test_add_furniture_circle(self, clean_axes):
        """Test add_furniture with circle type."""
        furniture = Furniture(
            furniture_type="circle",
            x=15,
            y=25,
            width=3,  # width is radius for circle
            color="#654321",
            label="Round Table",
        )
        add_furniture(clean_axes, furniture)
        patches = [p for p in clean_axes.patches if isinstance(p, Circle)]
        assert len(patches) >= 1

    def test_add_furniture_ellipse(self, clean_axes):
        """Test add_furniture with ellipse type."""
        furniture = Furniture(
            furniture_type="ellipse",
            x=20,
            y=30,
            width=8,
            height=5,
            color="#a0522d",
            label="Oval Rug",
        )
        add_furniture(clean_axes, furniture)
        # Ellipse adds a patch
        assert len(clean_axes.patches) >= 1

    def test_add_furniture_with_rotation(self, clean_axes):
        """Test add_furniture with rotation."""
        furniture = Furniture(
            furniture_type="rectangle",
            x=10,
            y=10,
            width=8,
            height=4,
            rotation=45,
            label="Rotated",
        )
        add_furniture(clean_axes, furniture)
        assert True


class TestAddFurnitureSimple:
    """Tests for the add_furniture_simple() function."""

    def test_add_furniture_simple_with_params(self, clean_axes):
        """Test add_furniture_simple with individual parameters."""
        add_furniture_simple(
            clean_axes,
            furniture_type="rectangle",
            x=5,
            y=5,
            width=4,
            height=3,
            color="#8b4513",
            label="Desk",
        )
        assert len(clean_axes.patches) >= 1


class TestAddTextAnnotation:
    """Tests for the add_text_annotation() function."""

    def test_add_text_annotation(self, clean_axes):
        """Test that add_text_annotation adds text."""
        annotation = TextAnnotation(
            x=50, y=50, text="Test Annotation", fontsize=10, color="black"
        )
        add_text_annotation(clean_axes, annotation)
        assert len(clean_axes.texts) >= 1

    def test_add_text_annotation_styled(self, clean_axes):
        """Test add_text_annotation with styling."""
        annotation = TextAnnotation(
            x=50,
            y=50,
            text="Styled Text",
            fontsize=14,
            color="red",
            fontweight="bold",
            style="italic",
            rotation=45,
        )
        add_text_annotation(clean_axes, annotation)
        assert len(clean_axes.texts) >= 1


class TestAddLineAnnotation:
    """Tests for the add_line_annotation() function."""

    def test_add_line_annotation(self, clean_axes):
        """Test that add_line_annotation adds a line."""
        line = LineAnnotation(x1=10, y1=20, x2=50, y2=60, color="blue", linewidth=2)
        add_line_annotation(clean_axes, line)
        # Should add a line to the axes
        assert len(clean_axes.lines) >= 1

    def test_add_line_annotation_dashed(self, clean_axes):
        """Test add_line_annotation with dashed style."""
        line = LineAnnotation(
            x1=0, y1=0, x2=100, y2=100, color="gray", linewidth=1, linestyle="--"
        )
        add_line_annotation(clean_axes, line)
        assert len(clean_axes.lines) >= 1


class TestAddDimensionArrow:
    """Tests for the add_dimension_arrow() function."""

    def test_add_dimension_arrow(self, clean_axes):
        """Test that add_dimension_arrow adds annotation."""
        add_dimension_arrow(clean_axes, start=(0, 0), end=(20, 0), label="20'-0\"")
        # Should add text annotation
        assert True  # Function should complete without error

    def test_add_dimension_arrow_vertical(self, clean_axes):
        """Test add_dimension_arrow for vertical measurement."""
        add_dimension_arrow(clean_axes, start=(0, 0), end=(0, 15), label="15'-0\"")
        assert True


class TestAddNorthArrow:
    """Tests for the add_north_arrow() function."""

    def test_add_north_arrow(self, clean_axes):
        """Test that add_north_arrow adds visual elements."""
        initial_children = len(clean_axes.get_children())
        add_north_arrow(clean_axes, x=90, y=90)
        # Should add arrow and text
        assert len(clean_axes.get_children()) > initial_children

    def test_add_north_arrow_custom_size(self, clean_axes):
        """Test add_north_arrow with custom size."""
        add_north_arrow(clean_axes, x=50, y=50, size=10)
        assert True


class TestAddTheaterSeating:
    """Tests for the add_theater_seating() function."""

    def test_add_theater_seating(self, clean_axes):
        """Test that add_theater_seating creates chair elements."""
        theater = TheaterSeating(start_x=10, start_y=20, rows=3, seats_per_row=4)
        initial_patches = len(clean_axes.patches)
        add_theater_seating(clean_axes, theater)
        # Should add multiple rectangles for chairs (rows * seats_per_row)
        assert len(clean_axes.patches) > initial_patches

    def test_add_theater_seating_custom_config(self, clean_axes):
        """Test add_theater_seating with custom configuration."""
        theater = TheaterSeating(
            start_x=0,
            start_y=0,
            rows=5,
            seats_per_row=6,
            chair_width=3,
            chair_height=2,
            row_spacing=5,
            seat_spacing=4,
            chair_color="#333333",
        )
        add_theater_seating(clean_axes, theater)
        # Should add 5 * 6 = 30 chair rectangles
        assert len(clean_axes.patches) >= 30


class TestAddPoolArea:
    """Tests for the add_pool_area() function."""

    def test_add_pool_area(self, clean_axes):
        """Test that add_pool_area creates pool elements."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=40,
            area_height=30,
            pool_x=5,
            pool_y=5,
            pool_width=25,
            pool_height=15,
            hot_tub_x=35,
            hot_tub_y=5,
        )
        initial_patches = len(clean_axes.patches)
        add_pool_area(clean_axes, pool)
        # Should add pool area, pool, and hot tub
        assert len(clean_axes.patches) > initial_patches

    def test_add_pool_area_custom_colors(self, clean_axes):
        """Test add_pool_area with custom colors."""
        pool = PoolConfig(
            area_x=0,
            area_y=0,
            area_width=50,
            area_height=40,
            pool_x=10,
            pool_y=10,
            pool_width=30,
            pool_height=20,
            hot_tub_x=45,
            hot_tub_y=10,
            area_color="#a0d0e0",
            pool_color="#4080c0",
            hot_tub_color="#60c0b0",
        )
        add_pool_area(clean_axes, pool)
        assert len(clean_axes.patches) >= 3


class TestBatchDrawingFunctions:
    """Tests for batch drawing functions that process lists of elements."""

    def test_draw_rooms_from_data(self, clean_axes):
        """Test draw_rooms_from_data with list of room dicts."""
        rooms_data = [
            {
                "x": 0,
                "y": 0,
                "width": 10,
                "height": 10,
                "label": "Room 1",
                "color": "bedroom",
            },
            {
                "x": 10,
                "y": 0,
                "width": 15,
                "height": 10,
                "label": "Room 2",
                "color": "kitchen",
            },
        ]
        draw_rooms_from_data(clean_axes, rooms_data)
        # Should add patches for each room
        assert len(clean_axes.patches) >= 2

    def test_draw_rooms_from_data_empty_list(self, clean_axes):
        """Test draw_rooms_from_data with empty list."""
        draw_rooms_from_data(clean_axes, [])
        # Should complete without error
        assert True

    def test_draw_doors_from_data(self, clean_axes):
        """Test draw_doors_from_data with list of door dicts."""
        doors_data = [
            {"x": 10, "y": 5, "width": 3, "direction": "right", "swing": "up"},
            {"x": 25, "y": 5, "width": 3, "direction": "left", "swing": "down"},
        ]
        draw_doors_from_data(clean_axes, doors_data)
        # Should complete without error
        assert True

    def test_draw_windows_from_data(self, clean_axes):
        """Test draw_windows_from_data with list of window dicts."""
        windows_data = [
            {"x": 2, "y": 0, "width": 4, "orientation": "horizontal"},
            {"x": 0, "y": 5, "width": 3, "orientation": "vertical"},
        ]
        draw_windows_from_data(clean_axes, windows_data)
        assert len(clean_axes.patches) >= 2

    def test_draw_furniture_from_data(self, clean_axes):
        """Test draw_furniture_from_data with list of furniture dicts."""
        furniture_data = [
            {
                "furniture_type": "rectangle",
                "x": 5,
                "y": 5,
                "width": 4,
                "height": 2,
                "label": "Table",
            },
            {"furniture_type": "circle", "x": 15, "y": 15, "width": 2, "label": "Lamp"},
        ]
        draw_furniture_from_data(clean_axes, furniture_data)
        assert len(clean_axes.patches) >= 2

    def test_draw_stairs_from_data(self, clean_axes):
        """Test draw_stairs_from_data with list of stairs dicts."""
        stairs_data = [
            {"x": 20, "y": 0, "width": 4, "height": 10, "num_steps": 8},
        ]
        draw_stairs_from_data(clean_axes, stairs_data)
        assert len(clean_axes.patches) >= 1

    def test_draw_fireplaces_from_data(self, clean_axes):
        """Test draw_fireplaces_from_data with list of fireplace dicts."""
        fireplaces_data = [
            {"x": 30, "y": 15, "width": 5, "height": 2},
        ]
        draw_fireplaces_from_data(clean_axes, fireplaces_data)
        assert len(clean_axes.patches) >= 1

    def test_draw_text_annotations_from_data(self, clean_axes):
        """Test draw_text_annotations_from_data with list of annotation dicts."""
        annotations_data = [
            {"x": 10, "y": 10, "text": "Note 1", "fontsize": 8},
            {"x": 20, "y": 20, "text": "Note 2", "fontsize": 10, "color": "red"},
        ]
        draw_text_annotations_from_data(clean_axes, annotations_data)
        assert len(clean_axes.texts) >= 2

    def test_draw_lines_from_data(self, clean_axes):
        """Test draw_lines_from_data with list of line dicts."""
        lines_data = [
            {"x1": 0, "y1": 0, "x2": 10, "y2": 10, "color": "black"},
            {"x1": 10, "y1": 0, "x2": 20, "y2": 10, "color": "gray", "linestyle": "--"},
        ]
        draw_lines_from_data(clean_axes, lines_data)
        assert len(clean_axes.lines) >= 2


class TestDrawingWithScaling:
    """Tests for drawing functions with different scale factors."""

    def test_room_with_scale(self, clean_axes):
        """Test that rooms respect scale factor."""
        set_scale(2.0)
        add_room_simple(clean_axes, x=0, y=0, width=10, height=10, label="Scaled")
        # Room should be drawn at scaled coordinates
        assert len(clean_axes.patches) >= 1

    def test_door_with_scale(self, clean_axes):
        """Test that doors respect scale factor."""
        set_scale(1.5)
        add_door_simple(clean_axes, x=10, y=5, width=3, direction="right", swing="up")
        assert True


class TestDrawingEdgeCases:
    """Tests for edge cases in drawing functions."""

    def test_zero_size_room(self, clean_axes):
        """Test handling of zero-size room."""
        # Should not raise an error, but may not draw anything meaningful
        try:
            add_room_simple(clean_axes, x=0, y=0, width=0, height=0, label="Zero")
        except Exception:
            pass  # May raise, that's acceptable

    def test_negative_coordinates(self, clean_axes):
        """Test handling of negative coordinates."""
        add_room_simple(clean_axes, x=-10, y=-10, width=5, height=5, label="Negative")
        assert True

    def test_very_large_room(self, clean_axes):
        """Test handling of very large room."""
        add_room_simple(clean_axes, x=0, y=0, width=1000, height=1000, label="Large")
        assert len(clean_axes.patches) >= 1

    def test_empty_label(self, clean_axes):
        """Test room with empty label."""
        add_room_simple(clean_axes, x=0, y=0, width=10, height=10, label="")
        assert True

    def test_special_characters_in_label(self, clean_axes):
        """Test room with special characters in label."""
        add_room_simple(
            clean_axes, x=0, y=0, width=10, height=10, label="Room 1\n(Master)"
        )
        assert True
