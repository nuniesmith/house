"""
Pytest configuration and shared fixtures for floor plan generator tests.

This module provides common fixtures used across all test modules.
"""

import sys
from pathlib import Path

import pytest

# Add the src directory to the path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_room_data():
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
def sample_door_data():
    """Provide sample door data for testing."""
    return {
        "x": 10,
        "y": 20,
        "width": 3,
        "direction": "right",
        "swing": "up",
    }


@pytest.fixture
def sample_window_data():
    """Provide sample window data for testing."""
    return {
        "x": 15,
        "y": 20,
        "width": 4,
        "orientation": "horizontal",
    }


@pytest.fixture
def sample_stairs_data():
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
def sample_furniture_data():
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
def sample_config():
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
        },
        "main_floor": {
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
        },
        "basement": {
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
        },
    }


@pytest.fixture
def temp_output_dir(tmp_path):
    """Provide a temporary output directory for test file generation."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture(autouse=True)
def reset_global_state():
    """Reset global state before each test."""
    from utilities import (
        set_auto_dimensions,
        set_debug_mode,
        set_grid_spacing,
        set_scale,
    )

    # Set defaults before test
    set_scale(1.0)
    set_debug_mode(False)
    set_grid_spacing(10)
    set_auto_dimensions(True)

    yield

    # Reset after test
    set_scale(1.0)
    set_debug_mode(False)
    set_grid_spacing(10)
    set_auto_dimensions(True)
