"""
Pytest configuration and shared fixtures for floor plan generator tests.

This module provides common fixtures used across all test modules.
"""

import shutil
import sys
from pathlib import Path
from typing import Any

import pytest

# Add the src directory to the path for imports
# The tests directory is at: src/python/tests
# The source modules are at: src/python/src
# We need to ensure 'src' is on the path so imports like 'from utilities import ...'
# work correctly and resolve to the same module instance as used by generators.py
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Also add parent for 'src.utilities' style imports to resolve to same modules
parent_path = Path(__file__).parent.parent
if str(parent_path) not in sys.path:
    sys.path.insert(0, str(parent_path))


# =============================================================================
# Test Output Cleanup
# =============================================================================

# Path to the output directory that gets populated during tests
OUTPUT_DIR = Path(__file__).parent.parent / "output"


@pytest.fixture(scope="session", autouse=True)
def cleanup_test_output():
    """
    Session-scoped fixture to clean up test output files.

    This fixture runs automatically at the end of all tests and removes
    any files generated in the output/ directory during test execution.
    """
    # Let all tests run first
    yield

    # Clean up output directory after all tests complete
    if OUTPUT_DIR.exists():
        for item in OUTPUT_DIR.iterdir():
            try:
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
            except OSError as e:
                # Log but don't fail if cleanup has issues
                print(f"Warning: Could not remove {item}: {e}")


# =============================================================================
# Sample Data Fixtures
# =============================================================================


@pytest.fixture
def sample_room_data() -> dict[str, Any]:
    """Provide sample room data for testing."""
    return {
        "x": 10,
        "y": 20,
        "width": 15,
        "height": 12,
        "label": "Test Room",
        "color": "bedroom",
        "label_fontsize": 10,
        "auto_dimension": True,
        "dimension_text": "15'-0\" x 12'-0\"",
    }


@pytest.fixture
def sample_door_data() -> dict[str, Any]:
    """Provide sample door data for testing."""
    return {
        "x": 10,
        "y": 20,
        "width": 3,
        "direction": "right",
        "swing": "up",
    }


@pytest.fixture
def sample_window_data() -> dict[str, Any]:
    """Provide sample window data for testing."""
    return {
        "x": 15,
        "y": 20,
        "width": 4,
        "orientation": "horizontal",
    }


@pytest.fixture
def sample_stairs_data() -> dict[str, Any]:
    """Provide sample stairs data for testing."""
    return {
        "x": 30,
        "y": 40,
        "width": 4,
        "height": 10,
        "num_steps": 8,
        "orientation": "vertical",
        "label": "Stairs",
    }


@pytest.fixture
def sample_furniture_data() -> dict[str, Any]:
    """Provide sample furniture data for testing."""
    return {
        "furniture_type": "rectangle",
        "x": 12,
        "y": 22,
        "width": 6,
        "height": 4,
        "color": "#8b4513",
        "label": "Table",
    }


@pytest.fixture
def sample_fireplace_data() -> dict[str, Any]:
    """Provide sample fireplace data for testing."""
    return {
        "x": 20,
        "y": 30,
        "width": 4,
        "height": 3,
        "label": "Fireplace",
    }


@pytest.fixture
def sample_text_annotation_data() -> dict[str, Any]:
    """Provide sample text annotation data for testing."""
    return {
        "x": 50,
        "y": 50,
        "text": "Test Annotation",
        "fontsize": 10,
        "color": "black",
        "ha": "center",
        "va": "center",
    }


@pytest.fixture
def sample_line_annotation_data() -> dict[str, Any]:
    """Provide sample line annotation data for testing."""
    return {
        "x1": 0,
        "y1": 0,
        "x2": 10,
        "y2": 10,
        "color": "red",
        "linewidth": 2,
        "linestyle": "--",
    }


@pytest.fixture
def sample_config() -> dict[str, Any]:
    """Provide a minimal sample configuration for testing."""
    return {
        "settings": {
            "scale": 1.0,
            "debug_mode": False,
            "grid_spacing": 10,
            "auto_dimensions": True,
            "output_dpi": 300,
            "output_format": "png",
            "show_north_arrow": True,
            "wall_thick": 2,
        },
        "colors": {
            "bedroom": "#fffacd",
            "bathroom": "#e6f3ff",
            "kitchen": "#e8f5e9",
            "living": "#fff3e0",
            "garage": "#e0e0e0",
            "porch": "#c8e6c9",
        },
        "main_floor": {
            "figure": {
                "width": 16,
                "height": 20,
                "title": "Main Floor Plan",
                "x_min": -5,
                "x_max": 100,
                "y_min": -5,
                "y_max": 80,
            },
            "rooms": [
                {
                    "x": 0,
                    "y": 0,
                    "width": 20,
                    "height": 15,
                    "label": "Living Room",
                    "color": "living",
                },
                {
                    "x": 20,
                    "y": 0,
                    "width": 15,
                    "height": 15,
                    "label": "Kitchen",
                    "color": "kitchen",
                },
            ],
            "doors": [
                {"x": 20, "y": 5, "width": 3, "direction": "right", "swing": "up"},
            ],
            "windows": [
                {"x": 5, "y": 0, "width": 4, "orientation": "horizontal"},
            ],
            "stairs": [],
            "fireplaces": [],
        },
        "basement": {
            "figure": {
                "width": 12,
                "height": 18,
                "title": "Basement Floor Plan",
                "x_min": -5,
                "x_max": 65,
                "y_min": -5,
                "y_max": 105,
            },
            "rooms": [
                {
                    "x": 0,
                    "y": 0,
                    "width": 30,
                    "height": 20,
                    "label": "Recreation Room",
                    "color": "gaming",
                },
            ],
            "doors": [],
            "stairs": [],
            "theater": {
                "room": {
                    "x": 0,
                    "y": 25,
                    "width": 30,
                    "height": 15,
                    "label": "Theater",
                    "color": "theater",
                },
                "seating": {
                    "start_x": 5,
                    "start_y": 27,
                    "rows": 2,
                    "seats_per_row": 3,
                },
                "false_wall": {
                    "x1": 0,
                    "y1": 25,
                    "x2": 30,
                    "y2": 25,
                },
            },
            "pool": {
                "area": {"x": 35, "y": 0, "width": 25, "height": 40},
                "pool": {"x": 37, "y": 5, "width": 15, "height": 25},
                "hot_tub": {"x": 55, "y": 15, "radius": 4},
                "spa_label": {"x": 55, "y": 25},
            },
        },
    }


@pytest.fixture
def temp_output_dir(tmp_path: Path) -> Path:
    """Provide a temporary output directory for test file generation."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def temp_config_file(tmp_path: Path, sample_config: dict[str, Any]) -> Path:
    """Create a temporary YAML config file for testing."""
    import yaml

    config_path = tmp_path / "test_config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(sample_config, f)
    return config_path


@pytest.fixture(autouse=True)
def reset_global_state():
    """Reset global state before and after each test."""
    from utilities import (
        set_auto_dimensions,
        set_debug_mode,
        set_grid_spacing,
        set_scale,
        set_wall_thick,
    )

    # Set defaults before test
    set_scale(1.0)
    set_debug_mode(False)
    set_grid_spacing(10)
    set_auto_dimensions(True)
    set_wall_thick(2)

    yield

    # Reset after test
    set_scale(1.0)
    set_debug_mode(False)
    set_grid_spacing(10)
    set_auto_dimensions(True)
    set_wall_thick(2)


@pytest.fixture
def drawing_config():
    """Provide a DrawingConfig instance for testing."""
    from utilities import DrawingConfig

    return DrawingConfig(
        scale=1.0,
        debug_mode=False,
        grid_spacing=10,
        auto_dimensions=True,
        wall_thick=2,
    )


@pytest.fixture
def mock_axes(mocker):
    """Provide a mock matplotlib axes object for testing drawing functions."""
    mock_ax = mocker.MagicMock()
    mock_ax.add_patch = mocker.MagicMock()
    mock_ax.plot = mocker.MagicMock()
    mock_ax.text = mocker.MagicMock()
    mock_ax.annotate = mocker.MagicMock()
    mock_ax.axhline = mocker.MagicMock()
    mock_ax.axvline = mocker.MagicMock()
    return mock_ax


# =============================================================================
# Helper functions for tests
# =============================================================================


def assert_room_dimensions(room, expected_width: float, expected_height: float) -> None:
    """Assert that a room has the expected dimensions."""
    assert room.width == expected_width, f"Expected width {expected_width}, got {room.width}"
    assert room.height == expected_height, f"Expected height {expected_height}, got {room.height}"


def assert_position(obj, expected_x: float, expected_y: float) -> None:
    """Assert that an object has the expected position."""
    assert obj.x == expected_x, f"Expected x {expected_x}, got {obj.x}"
    assert obj.y == expected_y, f"Expected y {expected_y}, got {obj.y}"


def create_test_rooms(count: int = 3) -> list[dict[str, Any]]:
    """Create a list of test room dictionaries."""
    rooms = []
    for i in range(count):
        rooms.append(
            {
                "x": i * 20,
                "y": 0,
                "width": 15,
                "height": 12,
                "label": f"Room {i + 1}",
                "color": "bedroom",
            }
        )
    return rooms
