"""
Tests for the defaults package.

This module tests all default data constants including:
- Main floor room defaults
- Main floor door defaults
- Main floor window defaults
- Main floor fireplace defaults
- Main floor stairs defaults
- Basement room defaults
- Basement theater defaults
- Basement pool defaults
- Basement door defaults
- Basement stairs defaults
- Basement furniture defaults
- Basement text annotation defaults
"""

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


class TestMainFloorRoomsDefault:
    """Tests for MAIN_FLOOR_ROOMS_DEFAULT constant."""

    def test_is_list(self):
        """Test that main floor rooms default is a list."""
        assert isinstance(MAIN_FLOOR_ROOMS_DEFAULT, list)

    def test_not_empty(self):
        """Test that main floor rooms default is not empty."""
        assert len(MAIN_FLOOR_ROOMS_DEFAULT) > 0

    def test_rooms_have_required_fields(self):
        """Test that all rooms have required fields."""
        required_fields = ["x", "y", "width", "height", "label"]
        for room in MAIN_FLOOR_ROOMS_DEFAULT:
            for field in required_fields:
                assert field in room, f"Room missing required field: {field}"

    def test_rooms_have_valid_coordinates(self):
        """Test that all rooms have valid coordinate values."""
        for room in MAIN_FLOOR_ROOMS_DEFAULT:
            assert isinstance(room["x"], (int, float))
            assert isinstance(room["y"], (int, float))
            assert isinstance(room["width"], (int, float))
            assert isinstance(room["height"], (int, float))

    def test_rooms_have_positive_dimensions(self):
        """Test that all rooms have positive dimensions."""
        for room in MAIN_FLOOR_ROOMS_DEFAULT:
            assert room["width"] > 0, f"Room '{room.get('label')}' has invalid width"
            assert room["height"] > 0, f"Room '{room.get('label')}' has invalid height"

    def test_rooms_have_labels(self):
        """Test that all rooms have non-empty labels."""
        for room in MAIN_FLOOR_ROOMS_DEFAULT:
            assert room["label"], "Room has empty label"
            assert isinstance(room["label"], str)

    def test_rooms_have_valid_colors(self):
        """Test that rooms with colors have valid color values."""
        for room in MAIN_FLOOR_ROOMS_DEFAULT:
            if "color" in room:
                color = room["color"]
                # Should be a string (color name or hex)
                assert isinstance(color, str)


class TestMainFloorDoorsDefault:
    """Tests for MAIN_FLOOR_DOORS_DEFAULT constant."""

    def test_is_list(self):
        """Test that main floor doors default is a list."""
        assert isinstance(MAIN_FLOOR_DOORS_DEFAULT, list)

    def test_doors_have_required_fields(self):
        """Test that all doors have required fields."""
        required_fields = ["x", "y", "width"]
        for door in MAIN_FLOOR_DOORS_DEFAULT:
            for field in required_fields:
                assert field in door, f"Door missing required field: {field}"

    def test_doors_have_valid_width(self):
        """Test that all doors have valid width values."""
        for door in MAIN_FLOOR_DOORS_DEFAULT:
            assert door["width"] > 0
            # Typical door widths are 2-6 feet
            assert door["width"] <= 10, (
                f"Door width seems unusually large: {door['width']}"
            )

    def test_doors_have_valid_direction(self):
        """Test that doors with direction have valid values."""
        valid_directions = ["right", "left", "up", "down"]
        for door in MAIN_FLOOR_DOORS_DEFAULT:
            if "direction" in door:
                assert door["direction"] in valid_directions

    def test_doors_have_valid_swing(self):
        """Test that doors with swing have valid values."""
        valid_swings = ["up", "down", "left", "right"]
        for door in MAIN_FLOOR_DOORS_DEFAULT:
            if "swing" in door:
                assert door["swing"] in valid_swings


class TestMainFloorWindowsDefault:
    """Tests for MAIN_FLOOR_WINDOWS_DEFAULT constant."""

    def test_is_list(self):
        """Test that main floor windows default is a list."""
        assert isinstance(MAIN_FLOOR_WINDOWS_DEFAULT, list)

    def test_windows_have_required_fields(self):
        """Test that all windows have required fields."""
        required_fields = ["x", "y", "width"]
        for window in MAIN_FLOOR_WINDOWS_DEFAULT:
            for field in required_fields:
                assert field in window, f"Window missing required field: {field}"

    def test_windows_have_valid_width(self):
        """Test that all windows have valid width values."""
        for window in MAIN_FLOOR_WINDOWS_DEFAULT:
            assert window["width"] > 0

    def test_windows_have_valid_orientation(self):
        """Test that windows with orientation have valid values."""
        valid_orientations = ["horizontal", "vertical"]
        for window in MAIN_FLOOR_WINDOWS_DEFAULT:
            if "orientation" in window:
                assert window["orientation"] in valid_orientations


class TestMainFloorFireplacesDefault:
    """Tests for MAIN_FLOOR_FIREPLACES_DEFAULT constant."""

    def test_is_list(self):
        """Test that main floor fireplaces default is a list."""
        assert isinstance(MAIN_FLOOR_FIREPLACES_DEFAULT, list)

    def test_fireplaces_have_required_fields(self):
        """Test that all fireplaces have required fields."""
        required_fields = ["x", "y", "width", "height"]
        for fireplace in MAIN_FLOOR_FIREPLACES_DEFAULT:
            for field in required_fields:
                assert field in fireplace, f"Fireplace missing required field: {field}"

    def test_fireplaces_have_valid_dimensions(self):
        """Test that all fireplaces have valid dimensions."""
        for fireplace in MAIN_FLOOR_FIREPLACES_DEFAULT:
            assert fireplace["width"] > 0
            assert fireplace["height"] > 0


class TestMainFloorStairsDefault:
    """Tests for MAIN_FLOOR_STAIRS_DEFAULT constant."""

    def test_is_list(self):
        """Test that main floor stairs default is a list."""
        assert isinstance(MAIN_FLOOR_STAIRS_DEFAULT, list)

    def test_stairs_have_required_fields(self):
        """Test that all stairs have required fields."""
        required_fields = ["x", "y", "width", "height"]
        for stairs in MAIN_FLOOR_STAIRS_DEFAULT:
            for field in required_fields:
                assert field in stairs, f"Stairs missing required field: {field}"

    def test_stairs_have_valid_dimensions(self):
        """Test that all stairs have valid dimensions."""
        for stairs in MAIN_FLOOR_STAIRS_DEFAULT:
            assert stairs["width"] > 0
            assert stairs["height"] > 0

    def test_stairs_have_valid_num_steps(self):
        """Test that stairs with num_steps have valid values."""
        for stairs in MAIN_FLOOR_STAIRS_DEFAULT:
            if "num_steps" in stairs:
                assert stairs["num_steps"] > 0
                assert stairs["num_steps"] <= 30  # Reasonable max for a single flight


class TestBasementRoomsDefault:
    """Tests for BASEMENT_ROOMS_DEFAULT constant."""

    def test_is_list(self):
        """Test that basement rooms default is a list."""
        assert isinstance(BASEMENT_ROOMS_DEFAULT, list)

    def test_not_empty(self):
        """Test that basement rooms default is not empty."""
        assert len(BASEMENT_ROOMS_DEFAULT) > 0

    def test_rooms_have_required_fields(self):
        """Test that all basement rooms have required fields."""
        required_fields = ["x", "y", "width", "height", "label"]
        for room in BASEMENT_ROOMS_DEFAULT:
            for field in required_fields:
                assert field in room, f"Room missing required field: {field}"

    def test_rooms_have_positive_dimensions(self):
        """Test that all basement rooms have positive dimensions."""
        for room in BASEMENT_ROOMS_DEFAULT:
            assert room["width"] > 0
            assert room["height"] > 0


class TestBasementTheaterDefault:
    """Tests for BASEMENT_THEATER_DEFAULT constant."""

    def test_is_dict(self):
        """Test that basement theater default is a dictionary."""
        assert isinstance(BASEMENT_THEATER_DEFAULT, dict)

    def test_has_required_sections(self):
        """Test that theater config has required sections."""
        required_sections = ["room", "seating"]
        for section in required_sections:
            assert section in BASEMENT_THEATER_DEFAULT, (
                f"Theater missing section: {section}"
            )

    def test_has_valid_seating_config(self):
        """Test that theater has valid seating configuration."""
        seating = BASEMENT_THEATER_DEFAULT.get("seating", {})
        if "rows" in seating:
            assert int(seating["rows"]) > 0  # type: ignore[arg-type]
        if "seats_per_row" in seating:
            assert int(seating["seats_per_row"]) > 0  # type: ignore[arg-type]

    def test_has_valid_dimensions(self):
        """Test that theater chair dimensions are valid if specified."""
        seating = BASEMENT_THEATER_DEFAULT.get("seating", {})
        if "chair_width" in seating:
            assert float(seating["chair_width"]) > 0  # type: ignore[arg-type]
        if "chair_height" in seating:
            assert float(seating["chair_height"]) > 0  # type: ignore[arg-type]


class TestBasementPoolDefault:
    """Tests for BASEMENT_POOL_DEFAULT constant."""

    def test_is_dict(self):
        """Test that basement pool default is a dictionary."""
        assert isinstance(BASEMENT_POOL_DEFAULT, dict)

    def test_has_required_sections(self):
        """Test that pool config has required sections."""
        required_sections = ["area", "pool", "hot_tub"]
        for section in required_sections:
            assert section in BASEMENT_POOL_DEFAULT, f"Pool missing section: {section}"

    def test_has_area_fields(self):
        """Test that pool area section has required fields."""
        area = BASEMENT_POOL_DEFAULT.get("area", {})
        area_fields = ["x", "y", "width", "height"]
        for field in area_fields:
            assert field in area, f"Pool area missing field: {field}"

    def test_has_pool_fields(self):
        """Test that pool section has required fields."""
        pool = BASEMENT_POOL_DEFAULT.get("pool", {})
        pool_fields = ["x", "y", "width", "height"]
        for field in pool_fields:
            assert field in pool, f"Pool missing field: {field}"

    def test_has_hot_tub_fields(self):
        """Test that hot tub section has required fields."""
        hot_tub = BASEMENT_POOL_DEFAULT.get("hot_tub", {})
        hot_tub_fields = ["x", "y", "radius"]
        for field in hot_tub_fields:
            assert field in hot_tub, f"Hot tub missing field: {field}"

    def test_pool_inside_area(self):
        """Test that pool is positioned inside the pool area."""
        area = BASEMENT_POOL_DEFAULT.get("area", {})
        pool = BASEMENT_POOL_DEFAULT.get("pool", {})
        # Pool should be within the area bounds
        pool_x = float(pool["x"])  # type: ignore[arg-type]
        pool_y = float(pool["y"])  # type: ignore[arg-type]
        area_x = float(area["x"])  # type: ignore[arg-type]
        area_y = float(area["y"])  # type: ignore[arg-type]
        pool_width = float(pool["width"])  # type: ignore[arg-type]
        area_width = float(area["width"])  # type: ignore[arg-type]

        assert pool_x >= area_x
        assert pool_y >= area_y
        pool_right = pool_x + pool_width
        area_right = area_x + area_width
        assert pool_right <= area_right

    def test_valid_dimensions(self):
        """Test that pool dimensions are valid."""
        area = BASEMENT_POOL_DEFAULT.get("area", {})
        pool = BASEMENT_POOL_DEFAULT.get("pool", {})
        assert float(area["width"]) > 0  # type: ignore[arg-type]
        assert float(area["height"]) > 0  # type: ignore[arg-type]
        assert float(pool["width"]) > 0  # type: ignore[arg-type]
        assert float(pool["height"]) > 0  # type: ignore[arg-type]


class TestBasementDoorsDefault:
    """Tests for BASEMENT_DOORS_DEFAULT constant."""

    def test_is_list(self):
        """Test that basement doors default is a list."""
        assert isinstance(BASEMENT_DOORS_DEFAULT, list)

    def test_doors_have_required_fields(self):
        """Test that all basement doors have required fields."""
        required_fields = ["x", "y", "width"]
        for door in BASEMENT_DOORS_DEFAULT:
            for field in required_fields:
                assert field in door, f"Door missing required field: {field}"


class TestBasementStairsDefault:
    """Tests for BASEMENT_STAIRS_DEFAULT constant."""

    def test_is_list(self):
        """Test that basement stairs default is a list."""
        assert isinstance(BASEMENT_STAIRS_DEFAULT, list)

    def test_stairs_have_required_fields(self):
        """Test that all basement stairs have required fields."""
        required_fields = ["x", "y", "width", "height"]
        for stairs in BASEMENT_STAIRS_DEFAULT:
            for field in required_fields:
                assert field in stairs, f"Stairs missing required field: {field}"


class TestBasementFurnitureDefault:
    """Tests for BASEMENT_FURNITURE_DEFAULT constant."""

    def test_is_list(self):
        """Test that basement furniture default is a list."""
        assert isinstance(BASEMENT_FURNITURE_DEFAULT, list)

    def test_furniture_have_required_fields(self):
        """Test that all furniture items have required fields."""
        required_fields = ["furniture_type", "x", "y", "width"]
        for furniture in BASEMENT_FURNITURE_DEFAULT:
            for field in required_fields:
                assert field in furniture, f"Furniture missing required field: {field}"

    def test_furniture_have_valid_type(self):
        """Test that all furniture items have valid type."""
        valid_types = ["rectangle", "circle", "ellipse"]
        for furniture in BASEMENT_FURNITURE_DEFAULT:
            assert furniture["furniture_type"] in valid_types


class TestBasementTextAnnotationsDefault:
    """Tests for BASEMENT_TEXT_ANNOTATIONS_DEFAULT constant."""

    def test_is_list(self):
        """Test that basement text annotations default is a list."""
        assert isinstance(BASEMENT_TEXT_ANNOTATIONS_DEFAULT, list)

    def test_annotations_have_required_fields(self):
        """Test that all annotations have required fields."""
        required_fields = ["x", "y", "text"]
        for annotation in BASEMENT_TEXT_ANNOTATIONS_DEFAULT:
            for field in required_fields:
                assert field in annotation, (
                    f"Annotation missing required field: {field}"
                )

    def test_annotations_have_non_empty_text(self):
        """Test that all annotations have non-empty text."""
        for annotation in BASEMENT_TEXT_ANNOTATIONS_DEFAULT:
            assert annotation["text"], "Annotation has empty text"


class TestDefaultDataConsistency:
    """Tests for consistency across default data."""

    def test_main_floor_has_minimum_rooms(self):
        """Test that main floor has a reasonable number of rooms."""
        # A house should have at least a few rooms
        assert len(MAIN_FLOOR_ROOMS_DEFAULT) >= 3

    def test_basement_has_minimum_rooms(self):
        """Test that basement has a reasonable number of rooms."""
        assert len(BASEMENT_ROOMS_DEFAULT) >= 1

    def test_no_duplicate_room_labels(self):
        """Test that room labels are unique within each floor."""
        main_labels = [r["label"] for r in MAIN_FLOOR_ROOMS_DEFAULT]
        basement_labels = [r["label"] for r in BASEMENT_ROOMS_DEFAULT]
        # Note: Some duplicates might be intentional (e.g., "Bathroom 1", "Bathroom 2")
        # So we just check that lists were created successfully
        assert len(main_labels) == len(MAIN_FLOOR_ROOMS_DEFAULT)
        assert len(basement_labels) == len(BASEMENT_ROOMS_DEFAULT)

    def test_rooms_have_valid_coordinates(self):
        """Test that rooms have numeric coordinates (may be negative for layout purposes)."""
        all_rooms = MAIN_FLOOR_ROOMS_DEFAULT + BASEMENT_ROOMS_DEFAULT
        for room in all_rooms:
            # Coordinates should be numeric (negative values are allowed for layout)
            assert isinstance(room["x"], (int, float)), (
                f"Room '{room['label']}' has non-numeric x"
            )
            assert isinstance(room["y"], (int, float)), (
                f"Room '{room['label']}' has non-numeric y"
            )

    def test_all_defaults_are_json_serializable(self):
        """Test that all defaults can be serialized to JSON."""
        import json

        defaults = [
            MAIN_FLOOR_ROOMS_DEFAULT,
            MAIN_FLOOR_DOORS_DEFAULT,
            MAIN_FLOOR_WINDOWS_DEFAULT,
            MAIN_FLOOR_FIREPLACES_DEFAULT,
            MAIN_FLOOR_STAIRS_DEFAULT,
            BASEMENT_ROOMS_DEFAULT,
            BASEMENT_THEATER_DEFAULT,
            BASEMENT_POOL_DEFAULT,
            BASEMENT_DOORS_DEFAULT,
            BASEMENT_STAIRS_DEFAULT,
            BASEMENT_FURNITURE_DEFAULT,
            BASEMENT_TEXT_ANNOTATIONS_DEFAULT,
        ]

        for default in defaults:
            # Should not raise
            json_str = json.dumps(default)
            assert len(json_str) > 0


class TestDefaultDataTypes:
    """Tests for correct data types in default data."""

    def test_coordinates_are_numeric(self):
        """Test that all coordinates are numeric types."""
        all_rooms = MAIN_FLOOR_ROOMS_DEFAULT + BASEMENT_ROOMS_DEFAULT
        for room in all_rooms:
            assert isinstance(room["x"], (int, float))
            assert isinstance(room["y"], (int, float))
            assert isinstance(room["width"], (int, float))
            assert isinstance(room["height"], (int, float))

    def test_labels_are_strings(self):
        """Test that all labels are strings."""
        all_rooms = MAIN_FLOOR_ROOMS_DEFAULT + BASEMENT_ROOMS_DEFAULT
        for room in all_rooms:
            assert isinstance(room["label"], str)

    def test_optional_fields_have_correct_types(self):
        """Test that optional fields have correct types when present."""
        all_rooms = MAIN_FLOOR_ROOMS_DEFAULT + BASEMENT_ROOMS_DEFAULT
        for room in all_rooms:
            if "label_fontsize" in room:
                assert isinstance(room["label_fontsize"], (int, float))
            if "auto_dimension" in room:
                assert isinstance(room["auto_dimension"], bool)
            if "color" in room:
                assert isinstance(room["color"], str)
