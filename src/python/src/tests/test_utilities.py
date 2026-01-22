"""
Tests for the utilities package.

This module tests all utility functions including:
- Scaling functions
- Dimension formatting
- Color resolution
- Coordinate transformations
- Room utilities
- Configuration validation
- Global state management
"""

from utilities import (
    COLORS,
    calculate_area,
    format_dimension,
    format_room_dimensions,
    get_auto_dimensions,
    get_debug_mode,
    get_grid_spacing,
    get_scale,
    get_total_floor_area,
    resolve_color,
    rooms_adjacent,
    rotate_90_ccw,
    rotate_90_cw,
    scale,
    set_auto_dimensions,
    set_debug_mode,
    set_grid_spacing,
    set_scale,
    update_colors,
    validate_config,
)


class TestScaleFunction:
    """Tests for the scale() function."""

    def test_scale_default(self):
        """Test scaling with default scale factor (1.0)."""
        set_scale(1.0)
        assert scale(10) == 10
        assert scale(5.5) == 5.5
        assert scale(0) == 0

    def test_scale_double(self):
        """Test scaling with 2x scale factor."""
        set_scale(2.0)
        assert scale(10) == 20
        assert scale(5.5) == 11.0
        assert scale(0) == 0

    def test_scale_half(self):
        """Test scaling with 0.5x scale factor."""
        set_scale(0.5)
        assert scale(10) == 5
        assert scale(5.5) == 2.75

    def test_scale_negative_value(self):
        """Test scaling negative values."""
        set_scale(2.0)
        assert scale(-5) == -10

    def test_scale_fractional_factor(self):
        """Test scaling with fractional scale factor."""
        set_scale(1.5)
        assert scale(10) == 15


class TestFormatDimension:
    """Tests for the format_dimension() function."""

    def test_whole_feet(self):
        """Test formatting whole feet values."""
        assert format_dimension(14.0) == "14'-0\""
        assert format_dimension(10.0) == "10'-0\""
        assert format_dimension(0.0) == "0'-0\""

    def test_feet_with_inches(self):
        """Test formatting feet with inches."""
        assert format_dimension(14.5) == "14'-6\""
        assert format_dimension(10.25) == "10'-3\""
        assert format_dimension(10.75) == "10'-9\""

    def test_rounding_inches(self):
        """Test that inches are properly rounded."""
        # 14.083... feet = 14'-1" (approximately)
        result = format_dimension(14.083)
        assert result == "14'-1\""

    def test_twelve_inches_rolls_over(self):
        """Test that 12 inches becomes next foot."""
        # When inches would round to 12, should become next foot
        result = format_dimension(14.99)
        assert result == "15'-0\""

    def test_without_inches(self):
        """Test formatting without showing inches."""
        assert format_dimension(14.0, include_inches=False) == "14'"
        assert format_dimension(14.25, include_inches=False) == "14'"
        assert format_dimension(14.5, include_inches=False) == "15'"  # Rounds up
        assert format_dimension(14.75, include_inches=False) == "15'"


class TestFormatRoomDimensions:
    """Tests for the format_room_dimensions() function."""

    def test_whole_dimensions(self):
        """Test formatting whole dimension values."""
        result = format_room_dimensions(14, 12)
        assert result == "14'-0\" x 12'-0\""

    def test_fractional_dimensions(self):
        """Test formatting fractional dimension values."""
        result = format_room_dimensions(14.5, 12.25)
        assert result == "14'-6\" x 12'-3\""

    def test_mixed_dimensions(self):
        """Test formatting mixed dimension values."""
        result = format_room_dimensions(20, 15.5)
        assert result == "20'-0\" x 15'-6\""


class TestCalculateArea:
    """Tests for the calculate_area() function."""

    def test_square_room(self):
        """Test calculating area of a square room."""
        assert calculate_area(10, 10) == 100

    def test_rectangular_room(self):
        """Test calculating area of a rectangular room."""
        assert calculate_area(15, 12) == 180

    def test_fractional_dimensions(self):
        """Test calculating area with fractional dimensions."""
        assert calculate_area(10.5, 8.5) == 89.25

    def test_zero_dimension(self):
        """Test calculating area with zero dimension."""
        assert calculate_area(10, 0) == 0
        assert calculate_area(0, 10) == 0


class TestResolveColor:
    """Tests for the resolve_color() function."""

    def test_hex_color_passthrough(self):
        """Test that hex colors are returned as-is."""
        assert resolve_color("#ff0000") == "#ff0000"
        assert resolve_color("#AABBCC") == "#AABBCC"

    def test_named_color_from_palette(self):
        """Test resolving named colors from COLORS dict."""
        assert resolve_color("bedroom") == COLORS["bedroom"]
        assert resolve_color("kitchen") == COLORS["kitchen"]
        assert resolve_color("garage") == COLORS["garage"]

    def test_empty_color(self):
        """Test that empty color returns white."""
        assert resolve_color("") == "#ffffff"

    def test_unknown_color(self):
        """Test that unknown color is returned as-is."""
        # CSS color names are passed through
        assert resolve_color("red") == "red"
        assert resolve_color("blue") == "blue"

    def test_all_palette_colors(self):
        """Test that all palette colors can be resolved."""
        for color_name, color_value in COLORS.items():
            assert resolve_color(color_name) == color_value


class TestUpdateColors:
    """Tests for the update_colors() function."""

    def test_add_new_color(self):
        """Test adding a new color to the palette."""
        update_colors({"test_color_unique": "#123456"})
        assert "test_color_unique" in COLORS
        assert COLORS["test_color_unique"] == "#123456"
        # Clean up
        del COLORS["test_color_unique"]

    def test_update_existing_color(self):
        """Test updating an existing color."""
        original = COLORS.get("bedroom", "#ffffff")
        update_colors({"bedroom": "#999999"})
        assert COLORS["bedroom"] == "#999999"
        # Restore original
        update_colors({"bedroom": original})


class TestRotate90CW:
    """Tests for the rotate_90_cw() function."""

    def test_basic_rotation(self):
        """Test basic 90° clockwise rotation."""
        result = rotate_90_cw(x=10, y=20, w=5, h=3, max_y=100)
        # new_x = max_y - y - h = 100 - 20 - 3 = 77
        # new_y = x = 10
        # new_w = h = 3
        # new_h = w = 5
        assert result == (77, 10, 3, 5)

    def test_origin_rotation(self):
        """Test rotation at origin."""
        result = rotate_90_cw(x=0, y=0, w=10, h=5, max_y=50)
        assert result == (45, 0, 5, 10)

    def test_dimensions_swap(self):
        """Test that width and height are swapped."""
        result = rotate_90_cw(x=0, y=0, w=20, h=10, max_y=100)
        assert result[2] == 10  # new width = old height
        assert result[3] == 20  # new height = old width


class TestRotate90CCW:
    """Tests for the rotate_90_ccw() function."""

    def test_basic_rotation(self):
        """Test basic 90° counter-clockwise rotation."""
        result = rotate_90_ccw(x=10, y=20, w=5, h=3, max_x=100)
        # new_x = y = 20
        # new_y = max_x - x - w = 100 - 10 - 5 = 85
        # new_w = h = 3
        # new_h = w = 5
        assert result == (20, 85, 3, 5)

    def test_origin_rotation(self):
        """Test rotation at origin."""
        result = rotate_90_ccw(x=0, y=0, w=10, h=5, max_x=50)
        assert result == (0, 40, 5, 10)


class TestRoomsAdjacent:
    """Tests for the rooms_adjacent() function."""

    def test_rooms_share_vertical_wall(self):
        """Test detecting rooms sharing a vertical wall."""
        room1: dict[str, float] = {"x": 0.0, "y": 0.0, "width": 10.0, "height": 10.0}
        room2: dict[str, float] = {"x": 10.0, "y": 0.0, "width": 10.0, "height": 10.0}
        assert rooms_adjacent(room1, room2) is True

    def test_rooms_share_horizontal_wall(self):
        """Test detecting rooms sharing a horizontal wall."""
        room1: dict[str, float] = {"x": 0.0, "y": 0.0, "width": 10.0, "height": 10.0}
        room2: dict[str, float] = {"x": 0.0, "y": 10.0, "width": 10.0, "height": 10.0}
        assert rooms_adjacent(room1, room2) is True

    def test_rooms_not_adjacent(self):
        """Test detecting rooms that are not adjacent."""
        room1: dict[str, float] = {"x": 0.0, "y": 0.0, "width": 10.0, "height": 10.0}
        room2: dict[str, float] = {
            "x": 20.0,
            "y": 0.0,
            "width": 10.0,
            "height": 10.0,
        }  # Gap between
        assert rooms_adjacent(room1, room2) is False

    def test_rooms_diagonal(self):
        """Test detecting rooms that touch diagonally (not adjacent)."""
        room1: dict[str, float] = {"x": 0.0, "y": 0.0, "width": 10.0, "height": 10.0}
        room2: dict[str, float] = {
            "x": 10.0,
            "y": 10.0,
            "width": 10.0,
            "height": 10.0,
        }  # Diagonal
        assert rooms_adjacent(room1, room2) is False

    def test_rooms_partial_overlap_vertical(self):
        """Test rooms sharing partial vertical wall."""
        room1: dict[str, float] = {"x": 0.0, "y": 0.0, "width": 10.0, "height": 10.0}
        room2: dict[str, float] = {
            "x": 10.0,
            "y": 5.0,
            "width": 10.0,
            "height": 10.0,
        }  # Partial overlap
        assert rooms_adjacent(room1, room2) is True

    def test_tolerance_parameter(self):
        """Test rooms with small gap within tolerance."""
        room1: dict[str, float] = {"x": 0.0, "y": 0.0, "width": 10.0, "height": 10.0}
        room2: dict[str, float] = {
            "x": 10.3,
            "y": 0.0,
            "width": 10.0,
            "height": 10.0,
        }  # Small gap
        assert rooms_adjacent(room1, room2, tolerance=0.5) is True
        assert rooms_adjacent(room1, room2, tolerance=0.1) is False


class TestGetTotalFloorArea:
    """Tests for the get_total_floor_area() function."""

    def test_single_room(self):
        """Test calculating area with single room."""
        rooms = [{"x": 0, "y": 0, "width": 10, "height": 10}]
        assert get_total_floor_area(rooms) == 100

    def test_multiple_rooms(self):
        """Test calculating area with multiple rooms."""
        rooms = [
            {"x": 0, "y": 0, "width": 10, "height": 10},  # 100 sq ft
            {"x": 10, "y": 0, "width": 15, "height": 12},  # 180 sq ft
        ]
        assert get_total_floor_area(rooms) == 280

    def test_empty_room_list(self):
        """Test calculating area with empty list."""
        assert get_total_floor_area([]) == 0

    def test_rooms_missing_dimensions(self):
        """Test that rooms missing dimensions are skipped."""
        rooms = [
            {"x": 0, "y": 0, "width": 10, "height": 10},  # 100 sq ft
            {"x": 10, "y": 0, "label": "No dimensions"},  # Skipped
        ]
        assert get_total_floor_area(rooms) == 100


class TestValidateConfig:
    """Tests for the validate_config() function."""

    def test_valid_config(self, sample_config):
        """Test that valid config passes validation."""
        warnings = validate_config(sample_config)
        # May have some warnings about overlap, etc., but should not fail
        assert isinstance(warnings, list)

    def test_invalid_scale_in_config(self):
        """Test that invalid scale generates warning."""
        config = {
            "settings": {"scale": -1.0},
            "main_floor": {"rooms": []},
            "basement": {"rooms": []},
        }
        warnings = validate_config(config)
        assert any("scale" in w.lower() for w in warnings)

    def test_missing_room_fields(self):
        """Test that missing room fields generate warnings."""
        config = {
            "settings": {},
            "main_floor": {
                "rooms": [
                    {"label": "Missing dimensions"}  # Missing x, y, width, height
                ]
            },
            "basement": {"rooms": []},
        }
        warnings = validate_config(config)
        assert any("missing" in w.lower() for w in warnings)

    def test_invalid_room_dimensions(self):
        """Test that invalid room dimensions generate warnings."""
        config = {
            "settings": {},
            "main_floor": {
                "rooms": [
                    {"x": 0, "y": 0, "width": -10, "height": 10, "label": "Bad width"}
                ]
            },
            "basement": {"rooms": []},
        }
        warnings = validate_config(config)
        assert any("width" in w.lower() for w in warnings)

    def test_overlapping_rooms_warning(self):
        """Test that significantly overlapping rooms generate warnings."""
        config = {
            "settings": {},
            "main_floor": {
                "rooms": [
                    {"x": 0, "y": 0, "width": 10, "height": 10, "label": "Room 1"},
                    {
                        "x": 2,
                        "y": 2,
                        "width": 10,
                        "height": 10,
                        "label": "Room 2",
                    },  # Overlaps
                ]
            },
            "basement": {"rooms": []},
        }
        warnings = validate_config(config)
        assert any("overlap" in w.lower() for w in warnings)

    def test_empty_config(self):
        """Test validation with empty config."""
        warnings = validate_config({})
        # Should handle gracefully
        assert isinstance(warnings, list)


class TestGlobalStateManagement:
    """Tests for global state getter/setter functions."""

    def test_scale_get_set(self):
        """Test scale getter and setter."""
        set_scale(2.5)
        assert get_scale() == 2.5
        set_scale(1.0)
        assert get_scale() == 1.0

    def test_debug_mode_get_set(self):
        """Test debug mode getter and setter."""
        set_debug_mode(True)
        assert get_debug_mode() is True
        set_debug_mode(False)
        assert get_debug_mode() is False

    def test_grid_spacing_get_set(self):
        """Test grid spacing getter and setter."""
        set_grid_spacing(20)
        assert get_grid_spacing() == 20
        set_grid_spacing(10)
        assert get_grid_spacing() == 10

    def test_auto_dimensions_get_set(self):
        """Test auto dimensions getter and setter."""
        set_auto_dimensions(False)
        assert get_auto_dimensions() is False
        set_auto_dimensions(True)
        assert get_auto_dimensions() is True


class TestColorsConstant:
    """Tests for the COLORS constant dictionary."""

    def test_main_floor_colors_exist(self):
        """Test that main floor colors are defined."""
        main_floor_colors = [
            "garage",
            "bedroom",
            "bathroom",
            "kitchen",
            "living",
            "dining",
            "office",
            "utility",
            "porch",
            "closet",
            "hall",
            "powder",
        ]
        for color in main_floor_colors:
            assert color in COLORS, f"Missing color: {color}"

    def test_basement_colors_exist(self):
        """Test that basement colors are defined."""
        basement_colors = [
            "theater",
            "gaming",
            "pool",
            "pool_area",
            "pool_utilities",
            "spa",
            "bar",
            "storage",
        ]
        for color in basement_colors:
            assert color in COLORS, f"Missing color: {color}"

    def test_furniture_colors_exist(self):
        """Test that furniture colors are defined."""
        furniture_colors = ["wood", "leather", "chair", "hammock"]
        for color in furniture_colors:
            assert color in COLORS, f"Missing color: {color}"

    def test_special_colors_exist(self):
        """Test that special element colors are defined."""
        special_colors = ["window", "fixture", "tub", "toilet", "sink"]
        for color in special_colors:
            assert color in COLORS, f"Missing color: {color}"

    def test_colors_are_valid_format(self):
        """Test that all colors are valid hex or named colors."""
        for name, color in COLORS.items():
            # Should be either a hex color or a recognized CSS color name
            is_hex = color.startswith("#") and len(color) in [4, 7]
            is_named = color in ["white", "black", "gray", "red", "blue", "green"]
            assert is_hex or is_named, f"Invalid color format for {name}: {color}"
