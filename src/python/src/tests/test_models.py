"""
Tests for the models package.

This module tests all data classes and their validation methods:
- FloorPlanSettings
- Room
- Door
- Window
- Stairs
- Fireplace
- Furniture
- TextAnnotation
- LineAnnotation
- TheaterSeating
- PoolConfig
"""

from models import (
    Door,
    Fireplace,
    FloorPlanSettings,
    Furniture,
    LineAnnotation,
    PoolConfig,
    Room,
    Stairs,
    TextAnnotation,
    TheaterSeating,
    Window,
)


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

    def test_custom_values(self):
        """Test creating settings with custom values."""
        settings = FloorPlanSettings(
            scale=2.0,
            debug_mode=True,
            grid_spacing=5,
            auto_dimensions=False,
            output_dpi=150,
            output_format="svg",
            show_north_arrow=False,
        )
        assert settings.scale == 2.0
        assert settings.debug_mode is True
        assert settings.grid_spacing == 5
        assert settings.auto_dimensions is False
        assert settings.output_dpi == 150
        assert settings.output_format == "svg"
        assert settings.show_north_arrow is False

    def test_validate_valid_settings(self):
        """Test that valid settings pass validation."""
        settings = FloorPlanSettings(scale=1.5, grid_spacing=20, output_dpi=300)
        warnings = settings.validate()
        assert len(warnings) == 0

    def test_validate_invalid_scale(self):
        """Test that invalid scale triggers warning and correction."""
        settings = FloorPlanSettings(scale=-1.0)
        warnings = settings.validate()
        assert any("scale" in w.lower() for w in warnings)
        assert settings.scale == 1.0  # Should be corrected

    def test_validate_zero_scale(self):
        """Test that zero scale triggers warning and correction."""
        settings = FloorPlanSettings(scale=0)
        warnings = settings.validate()
        assert any("scale" in w.lower() for w in warnings)
        assert settings.scale == 1.0

    def test_validate_invalid_grid_spacing(self):
        """Test that invalid grid spacing triggers warning."""
        settings = FloorPlanSettings(grid_spacing=-5)
        warnings = settings.validate()
        assert any("grid_spacing" in w.lower() for w in warnings)
        assert settings.grid_spacing == 10  # Should be corrected

    def test_validate_low_dpi_warning(self):
        """Test that low DPI triggers a warning."""
        settings = FloorPlanSettings(output_dpi=50)
        warnings = settings.validate()
        assert any("dpi" in w.lower() for w in warnings)


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
        """Test creating room with custom values."""
        room = Room(
            x=10,
            y=20,
            width=15,
            height=12,
            label="Bedroom",
            color="bedroom",
            label_fontsize=12,
            auto_dimension=True,
            dimension_text="15' x 12'",
        )
        assert room.x == 10
        assert room.y == 20
        assert room.width == 15
        assert room.height == 12
        assert room.label == "Bedroom"
        assert room.color == "bedroom"

    def test_validate_valid_room(self):
        """Test that valid room passes validation."""
        room = Room(x=0, y=0, width=10, height=10, label="Valid Room")
        warnings = room.validate()
        assert len(warnings) == 0

    def test_validate_invalid_width(self):
        """Test that invalid width triggers warning."""
        room = Room(x=0, y=0, width=-5, height=10, label="Invalid Room")
        warnings = room.validate()
        assert any("width" in w.lower() for w in warnings)

    def test_validate_invalid_height(self):
        """Test that invalid height triggers warning."""
        room = Room(x=0, y=0, width=10, height=0, label="Invalid Room")
        warnings = room.validate()
        assert any("height" in w.lower() for w in warnings)

    def test_validate_both_invalid(self):
        """Test that both invalid dimensions trigger warnings."""
        room = Room(x=0, y=0, width=-5, height=-10, label="Invalid Room")
        warnings = room.validate()
        assert len(warnings) == 2

    def test_center_property(self):
        """Test center property calculation."""
        room = Room(x=10, y=20, width=10, height=8, label="Test")
        center = room.center
        assert center == (15.0, 24.0)

    def test_bounds_property(self):
        """Test bounds property calculation."""
        room = Room(x=10, y=20, width=15, height=12, label="Test")
        bounds = room.bounds
        assert bounds == (10, 20, 25, 32)


class TestDoor:
    """Tests for Door dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        door = Door(x=0, y=0, width=3)
        assert door.direction == "right"
        assert door.swing == "up"

    def test_custom_values(self):
        """Test creating door with custom values."""
        door = Door(x=10, y=20, width=3, direction="left", swing="down")
        assert door.x == 10
        assert door.y == 20
        assert door.width == 3
        assert door.direction == "left"
        assert door.swing == "down"

    def test_validate_valid_door(self):
        """Test that valid door passes validation."""
        door = Door(x=0, y=0, width=3)
        warnings = door.validate()
        assert len(warnings) == 0

    def test_validate_invalid_width(self):
        """Test that invalid width triggers warning."""
        door = Door(x=0, y=0, width=-1)
        warnings = door.validate()
        assert any("width" in w.lower() for w in warnings)

    def test_validate_unusually_wide_door(self):
        """Test that unusually wide door triggers warning."""
        door = Door(x=0, y=0, width=10)
        warnings = door.validate()
        assert any("wide" in w.lower() for w in warnings)


class TestWindow:
    """Tests for Window dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        window = Window(x=0, y=0, width=4)
        assert window.orientation == "horizontal"

    def test_custom_values(self):
        """Test creating window with custom values."""
        window = Window(x=15, y=25, width=6, orientation="vertical")
        assert window.x == 15
        assert window.y == 25
        assert window.width == 6
        assert window.orientation == "vertical"

    def test_validate_valid_window(self):
        """Test that valid window passes validation."""
        window = Window(x=0, y=0, width=4)
        warnings = window.validate()
        assert len(warnings) == 0

    def test_validate_invalid_width(self):
        """Test that invalid width triggers warning."""
        window = Window(x=0, y=0, width=0)
        warnings = window.validate()
        assert any("width" in w.lower() for w in warnings)


class TestStairs:
    """Tests for Stairs dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        stairs = Stairs(x=0, y=0, width=4, height=10)
        assert stairs.num_steps == 8
        assert stairs.orientation == "horizontal"
        assert stairs.label == ""

    def test_custom_values(self):
        """Test creating stairs with custom values."""
        stairs = Stairs(
            x=30,
            y=40,
            width=5,
            height=12,
            num_steps=10,
            orientation="vertical",
            label="Main Stairs",
        )
        assert stairs.x == 30
        assert stairs.y == 40
        assert stairs.width == 5
        assert stairs.height == 12
        assert stairs.num_steps == 10
        assert stairs.orientation == "vertical"
        assert stairs.label == "Main Stairs"


class TestFireplace:
    """Tests for Fireplace dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        fireplace = Fireplace(x=0, y=0, width=5, height=2)
        assert fireplace.label == ""

    def test_custom_values(self):
        """Test creating fireplace with custom values."""
        fireplace = Fireplace(x=20, y=30, width=6, height=3, label="Stone Fireplace")
        assert fireplace.x == 20
        assert fireplace.y == 30
        assert fireplace.width == 6
        assert fireplace.height == 3
        assert fireplace.label == "Stone Fireplace"


class TestFurniture:
    """Tests for Furniture dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        furniture = Furniture(furniture_type="rectangle", x=0, y=0, width=5)
        assert furniture.height == 0
        assert furniture.color == "#8b4513"
        assert furniture.edge_color == "black"
        assert furniture.label == ""
        assert furniture.label_fontsize == 7
        assert furniture.label_color == "black"
        assert furniture.rotation == 0
        assert furniture.linewidth == 1

    def test_rectangle_furniture(self):
        """Test creating rectangle furniture."""
        furniture = Furniture(
            furniture_type="rectangle",
            x=10,
            y=20,
            width=8,
            height=4,
            color="#654321",
            label="Couch",
        )
        assert furniture.furniture_type == "rectangle"
        assert furniture.width == 8
        assert furniture.height == 4

    def test_circle_furniture(self):
        """Test creating circle furniture."""
        furniture = Furniture(
            furniture_type="circle", x=15, y=25, width=3, label="Table"
        )
        assert furniture.furniture_type == "circle"
        assert furniture.width == 3  # Radius for circle

    def test_ellipse_furniture(self):
        """Test creating ellipse furniture."""
        furniture = Furniture(
            furniture_type="ellipse", x=20, y=30, width=6, height=4, label="Rug"
        )
        assert furniture.furniture_type == "ellipse"
        assert furniture.width == 6
        assert furniture.height == 4


class TestTextAnnotation:
    """Tests for TextAnnotation dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        annotation = TextAnnotation(x=0, y=0, text="Test")
        assert annotation.fontsize == 8
        assert annotation.color == "black"
        assert annotation.ha == "center"
        assert annotation.va == "center"
        assert annotation.rotation == 0
        assert annotation.fontweight == "normal"
        assert annotation.style == "normal"

    def test_custom_values(self):
        """Test creating annotation with custom values."""
        annotation = TextAnnotation(
            x=50,
            y=60,
            text="Important Note",
            fontsize=12,
            color="red",
            ha="left",
            va="bottom",
            rotation=45,
            fontweight="bold",
            style="italic",
        )
        assert annotation.x == 50
        assert annotation.y == 60
        assert annotation.text == "Important Note"
        assert annotation.fontsize == 12
        assert annotation.color == "red"
        assert annotation.rotation == 45


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
        """Test creating line with custom values."""
        line = LineAnnotation(
            x1=5,
            y1=10,
            x2=25,
            y2=30,
            color="blue",
            linewidth=3,
            linestyle="--",
            zorder=10,
        )
        assert line.x1 == 5
        assert line.y1 == 10
        assert line.x2 == 25
        assert line.y2 == 30
        assert line.color == "blue"
        assert line.linestyle == "--"


class TestTheaterSeating:
    """Tests for TheaterSeating dataclass."""

    def test_default_values(self):
        """Test that default values are set correctly."""
        theater = TheaterSeating(start_x=0, start_y=0)
        assert theater.rows == 4
        assert theater.seats_per_row == 5
        assert theater.chair_width == 4
        assert theater.chair_height == 3
        assert theater.row_spacing == 6
        assert theater.seat_spacing == 5
        assert theater.chair_color == "#4a4a4a"
        assert theater.edge_color == "gray"

    def test_custom_values(self):
        """Test creating theater seating with custom values."""
        theater = TheaterSeating(
            start_x=10,
            start_y=20,
            rows=3,
            seats_per_row=4,
            chair_width=5,
            chair_height=4,
            row_spacing=8,
            seat_spacing=6,
            chair_color="#333333",
            edge_color="black",
        )
        assert theater.start_x == 10
        assert theater.start_y == 20
        assert theater.rows == 3
        assert theater.seats_per_row == 4


class TestPoolConfig:
    """Tests for PoolConfig dataclass."""

    def test_required_fields(self):
        """Test creating pool config with required fields."""
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
        assert pool.area_x == 0
        assert pool.area_width == 40
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
            pool_height=15,
            hot_tub_x=35,
            hot_tub_y=5,
        )
        assert pool.area_color == "#e0f7fa"
        assert pool.area_label == "Pool Area"
        assert pool.pool_color == "#63b3ed"
        assert pool.pool_edge_color == "#0288d1"
        assert pool.pool_label == "Salt Water\nPool"
        assert pool.hot_tub_radius == 4
        assert pool.hot_tub_color == "#81e6d9"
        assert pool.hot_tub_label == "Hot\nTub"

    def test_custom_values(self):
        """Test creating pool config with custom values."""
        pool = PoolConfig(
            area_x=10,
            area_y=20,
            area_width=50,
            area_height=40,
            pool_x=15,
            pool_y=25,
            pool_width=30,
            pool_height=20,
            hot_tub_x=48,
            hot_tub_y=25,
            area_color="#a0d0e0",
            pool_label="Indoor Pool",
            hot_tub_radius=5,
            hot_tub_label="Spa",
        )
        assert pool.area_color == "#a0d0e0"
        assert pool.pool_label == "Indoor Pool"
        assert pool.hot_tub_radius == 5
        assert pool.hot_tub_label == "Spa"


class TestModelEquality:
    """Tests for dataclass equality comparisons."""

    def test_room_equality(self):
        """Test that identical rooms are equal."""
        room1 = Room(x=0, y=0, width=10, height=10, label="Test")
        room2 = Room(x=0, y=0, width=10, height=10, label="Test")
        assert room1 == room2

    def test_room_inequality(self):
        """Test that different rooms are not equal."""
        room1 = Room(x=0, y=0, width=10, height=10, label="Test1")
        room2 = Room(x=0, y=0, width=10, height=10, label="Test2")
        assert room1 != room2

    def test_door_equality(self):
        """Test that identical doors are equal."""
        door1 = Door(x=5, y=10, width=3, direction="left", swing="down")
        door2 = Door(x=5, y=10, width=3, direction="left", swing="down")
        assert door1 == door2


class TestModelCreationFromDict:
    """Tests for creating models from dictionary data (common use case)."""

    def test_room_from_dict(self, sample_room_data):
        """Test creating Room from dictionary."""
        # Filter to only include valid Room fields
        valid_fields = Room.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in sample_room_data.items() if k in valid_fields}
        room = Room(**filtered_data)
        assert room.x == sample_room_data["x"]
        assert room.y == sample_room_data["y"]
        assert room.label == sample_room_data["label"]

    def test_door_from_dict(self, sample_door_data):
        """Test creating Door from dictionary."""
        door = Door(**sample_door_data)
        assert door.x == sample_door_data["x"]
        assert door.width == sample_door_data["width"]
        assert door.direction == sample_door_data["direction"]

    def test_window_from_dict(self, sample_window_data):
        """Test creating Window from dictionary."""
        window = Window(**sample_window_data)
        assert window.x == sample_window_data["x"]
        assert window.width == sample_window_data["width"]
        assert window.orientation == sample_window_data["orientation"]


class TestModelTypeHints:
    """Tests for verifying type hints are enforced where applicable."""

    def test_door_direction_values(self):
        """Test that door direction accepts valid literal values."""
        door_right = Door(x=0, y=0, width=3, direction="right")
        assert door_right.direction == "right"
        door_left = Door(x=0, y=0, width=3, direction="left")
        assert door_left.direction == "left"
        door_up = Door(x=0, y=0, width=3, direction="up")
        assert door_up.direction == "up"
        door_down = Door(x=0, y=0, width=3, direction="down")
        assert door_down.direction == "down"

    def test_door_swing_values(self):
        """Test that door swing accepts valid literal values."""
        door_up = Door(x=0, y=0, width=3, swing="up")
        assert door_up.swing == "up"
        door_down = Door(x=0, y=0, width=3, swing="down")
        assert door_down.swing == "down"
        door_left = Door(x=0, y=0, width=3, swing="left")
        assert door_left.swing == "left"
        door_right = Door(x=0, y=0, width=3, swing="right")
        assert door_right.swing == "right"

    def test_window_orientation_values(self):
        """Test that window orientation accepts valid literal values."""
        window_horizontal = Window(x=0, y=0, width=4, orientation="horizontal")
        assert window_horizontal.orientation == "horizontal"
        window_vertical = Window(x=0, y=0, width=4, orientation="vertical")
        assert window_vertical.orientation == "vertical"

    def test_furniture_type_values(self):
        """Test that furniture type accepts valid literal values."""
        furniture_rect = Furniture(furniture_type="rectangle", x=0, y=0, width=5)
        assert furniture_rect.furniture_type == "rectangle"
        furniture_circle = Furniture(furniture_type="circle", x=0, y=0, width=5)
        assert furniture_circle.furniture_type == "circle"
        furniture_ellipse = Furniture(furniture_type="ellipse", x=0, y=0, width=5)
        assert furniture_ellipse.furniture_type == "ellipse"
