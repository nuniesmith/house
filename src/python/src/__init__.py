"""
Floor Plan Generator Package
============================

A modular Python package for generating architectural floor plans using matplotlib.

This package provides tools for creating, configuring, and exporting floor plans
in multiple formats (PNG, SVG, PDF).

Subpackages
-----------
- models     : Data classes for floor plan elements (Room, Door, Window, etc.)
- utilities  : Helper functions for scaling, validation, colors, and formatting
- drawing    : Matplotlib drawing functions for floor plan elements
- generators : Floor plan generation and export functions
- defaults   : Default floor plan data constants
- config     : YAML configuration files (not a Python module)

Quick Start
-----------
>>> from generators import load_config, generate_main_floor, generate_basement
>>> config = load_config()
>>> generate_main_floor(config)
>>> generate_basement(config)

Or run from command line:
    python main.py --help

Version History
---------------
- 1.0.0 : Initial modular release with YAML configuration support
"""

__version__ = "1.0.0"
__author__ = "House Floor Plan Generator"

# Re-export key classes and functions for convenience
# Users can either import from subpackages directly or from this top-level package

# Models - Data classes for floor plan elements
# Generators - Main generation functions
from generators import (
    OUTPUT_DIR,
    apply_config_settings,
    generate_all_svg,
    generate_basement,
    generate_combined_pdf,
    generate_main_floor,
    load_config,
)
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

# Utilities - Commonly used helper functions
from utilities import (
    COLORS,
    format_dimension,
    format_room_dimensions,
    get_debug_mode,
    get_scale,
    resolve_color,
    scale,
    set_debug_mode,
    set_scale,
    validate_config,
)

__all__ = [
    # Package metadata
    "__version__",
    "__author__",
    # Models
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
    # Generators
    "load_config",
    "apply_config_settings",
    "generate_main_floor",
    "generate_basement",
    "generate_all_svg",
    "generate_combined_pdf",
    "OUTPUT_DIR",
    # Utilities
    "COLORS",
    "scale",
    "format_dimension",
    "format_room_dimensions",
    "resolve_color",
    "validate_config",
    "get_scale",
    "set_scale",
    "get_debug_mode",
    "set_debug_mode",
]
