"""
Floor Plan Generator Package
============================

A modular Python package for generating architectural floor plans using matplotlib.

This package provides tools for creating, configuring, and exporting floor plans
in multiple formats (PNG, SVG, PDF).

Modules
-------
- models     : Data classes for floor plan elements (Room, Door, Window, etc.)
- utilities  : Helper functions for scaling, validation, colors, and formatting
- drawing    : Matplotlib drawing functions for floor plan elements
- generators : Floor plan generation and export functions
- defaults   : Default floor plan data constants

Configuration
-------------
Floor plans are configured via YAML files. See `config.yaml` for
the default configuration with all available options documented.

Quick Start
-----------
>>> from generators import load_config, generate_main_floor, generate_basement
>>> config = load_config()
>>> generate_main_floor(config)
>>> generate_basement(config)

Using the DrawingConfig class (recommended):
>>> from utilities import DrawingConfig
>>> config = DrawingConfig(scale=1.5, debug_mode=True)
>>> # Pass config to drawing functions for explicit configuration

Using the caching utilities:
>>> from cache import MemoryCache, cached
>>> cache = MemoryCache(max_size=100)
>>> @cached(cache=cache)
... def expensive_calculation(x):
...     return x ** 2

Or run from command line:
    python main.py --help
    python main.py                  # Generate PNG files (default)
    python main.py --svg-only       # Generate only SVG files
    python main.py --pdf-only       # Generate only combined PDF
    python main.py --debug          # Generate with grid overlay

Version History
---------------
- 1.2.0 : Added caching utilities, FloorPlanBuilder, and RoomTemplates
- 1.1.0 : Added DrawingConfig class for better configuration management
- 1.0.0 : Initial modular release with YAML configuration support
"""

__version__ = "1.2.0"
__author__ = "House Floor Plan Generator"
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
    "FloorPlan",
    "FloorPlanBuilder",
    "RoomTemplates",
    # Generators
    "load_config",
    "apply_config_settings",
    "generate_main_floor",
    "generate_basement",
    "generate_all_svg",
    "generate_combined_pdf",
    "OUTPUT_DIR",
    # Utilities - Configuration
    "DrawingConfig",
    "get_default_config",
    "set_default_config",
    # Utilities - Colors
    "COLORS",
    "resolve_color",
    "update_colors",
    "is_valid_hex_color",
    "lighten_color",
    "darken_color",
    # Utilities - Scaling and formatting
    "scale",
    "format_dimension",
    "format_room_dimensions",
    "format_area",
    "calculate_area",
    # Utilities - Validation
    "validate_config",
    # Utilities - State management
    "get_scale",
    "set_scale",
    "get_debug_mode",
    "set_debug_mode",
    # Caching utilities
    "MemoryCache",
    "DiskCache",
    "CacheStats",
    "cached",
    "generate_config_hash",
    "get_calculation_cache",
    "get_render_cache",
    "clear_all_caches",
]

# =============================================================================
# Models - Data classes for floor plan elements
# =============================================================================
# =============================================================================
# Generators - Main generation functions
# =============================================================================
from cache import (
    CacheStats,
    DiskCache,
    MemoryCache,
    cached,
    clear_all_caches,
    generate_config_hash,
    get_calculation_cache,
    get_render_cache,
)
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
# Utilities - Helper functions and configuration
# =============================================================================
from utilities import (
    # Color constants and functions
    COLORS,
    # Configuration class (preferred for new code)
    DrawingConfig,
    calculate_area,
    darken_color,
    format_area,
    format_dimension,
    format_room_dimensions,
    get_debug_mode,
    get_default_config,
    # State management
    get_scale,
    is_valid_hex_color,
    lighten_color,
    resolve_color,
    # Scaling and formatting
    scale,
    set_debug_mode,
    set_default_config,
    set_scale,
    update_colors,
    # Validation
    validate_config,
)
