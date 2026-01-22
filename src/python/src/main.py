#!/usr/bin/env python3
"""
Floor Plan Generator for House
Generates floor plan images for Main Floor and Basement levels using matplotlib.

Output files are saved to the 'output/' directory.

Features:
- YAML configuration file for easy editing
- Data-driven room definitions for easy modification
- Data-driven special elements (theater, pool, furniture)
- Scale factor for resizing
- Rotation helper functions
- Improved door swing logic
- Window support
- Multi-page PDF output option
- Reusable drawing functions to eliminate duplication
- Debug grid mode for development
- Auto-dimensioning for rooms
- Config validation for early error detection

This is the main entry point that uses modular packages:
- models.py      - Data classes for floor plan elements
- utilities.py   - Helper functions (scaling, validation, colors)
- drawing.py     - Drawing functions for matplotlib
- generators.py  - Floor plan generation and export functions
- defaults.py    - Default floor plan data constants
- config.py      - YAML configuration files
"""

import argparse
import logging
import sys
from pathlib import Path

# Add the src/python directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Import from our modular packages (must be after path modification)
from generators import (
    OUTPUT_DIR,
    apply_config_settings,
    generate_all_svg,
    generate_basement,
    generate_combined_pdf,
    generate_main_floor,
    load_config,
)
from utilities import (
    get_auto_dimensions,
    get_debug_mode,
    get_grid_spacing,
    get_scale,
    set_debug_mode,
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def _create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate house floor plans (PNG by default)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --config config.yaml              # Generate PNG files
  python main.py --config config.yaml --svg-only   # Generate only SVG files
  python main.py --config config.yaml --pdf-only   # Generate only combined PDF
  python main.py --config config.yaml --debug      # Generate with grid overlay
  python main.py --config config.yaml --validate   # Only validate config file
        """,
    )
    parser.add_argument("--png-only", action="store_true", help="Only generate PNG files (default)")
    parser.add_argument("--svg-only", action="store_true", help="Only generate SVG files")
    parser.add_argument("--pdf-only", action="store_true", help="Only generate combined PDF")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode with grid overlay")
    parser.add_argument(
        "--validate", action="store_true", help="Only validate config, don't generate"
    )
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to YAML config file (REQUIRED)",
    )
    return parser


def _print_settings() -> None:
    """Print current configuration settings."""
    print(f"  Scale: {get_scale()}")
    print(f"  Debug Mode: {get_debug_mode()}")
    print(f"  Grid Spacing: {get_grid_spacing()}")
    print(f"  Auto Dimensions: {get_auto_dimensions()}")
    print()


def _print_completion_message(output_files: list[Path]) -> None:
    """Print completion message with output file information."""
    print("=" * 60)
    print("Floor plan generation complete!")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    print("Output files:")
    for f in output_files:
        print(f"  - {f}")
    print()
    print("To modify the floor plans, edit 'config.yaml'")
    print("Set 'debug_mode: true' in the config to show grid overlay")
    print()
    print("SVG files can be opened in:")
    print("  - Web browsers (for viewing)")
    print("  - Inkscape, Adobe Illustrator (for editing)")
    print("  - CAD software (for import)")
    print("=" * 60)


def _generate_outputs(parsed_args: argparse.Namespace, config: dict) -> list[Path]:
    """Generate floor plan outputs based on command-line arguments."""
    # Determine which formats to generate
    # Default to PNG-only unless other formats explicitly requested
    generate_png = not (parsed_args.svg_only or parsed_args.pdf_only)
    generate_svg_files = parsed_args.svg_only
    generate_pdf = parsed_args.pdf_only

    output_files: list[Path] = []

    if generate_png:
        print("Generating PNG files...")
        print("  Main Floor Plan...")
        output_files.append(generate_main_floor(config))

        print("  Basement Floor Plan...")
        output_files.append(generate_basement(config))
        print()

    if generate_svg_files:
        print("Generating SVG files...")
        svg_paths = generate_all_svg(config)
        output_files.extend(svg_paths)
        print()

    if generate_pdf:
        print("Generating Combined PDF...")
        output_files.append(generate_combined_pdf(config=config))
        print()

    return output_files


def main(args: list[str] | None = None) -> int:
    """
    Generate floor plans (PNG by default).

    Supports command-line arguments:
        --png-only    Only generate PNG files (default behavior)
        --svg-only    Only generate SVG files
        --pdf-only    Only generate PDF file
        --debug       Enable debug mode (grid overlay)
        --validate    Only validate config without generating
        --config      Path to custom config file
        --help        Show help message

    Args:
        args: Command-line arguments (uses sys.argv if None)

    Returns:
        Exit code (0 for success)
    """
    parser = _create_argument_parser()
    parsed_args = parser.parse_args(args)

    print("=" * 60)
    print("House Floor Plan Generator")
    print("=" * 60)
    print()

    # Load configuration (--config is required)
    print(f"Loading configuration from: {parsed_args.config}")
    config = load_config(parsed_args.config)
    apply_config_settings(config)

    # Override debug mode if specified on command line
    if parsed_args.debug:
        set_debug_mode(True)

    _print_settings()

    # If validate-only mode, exit here
    if parsed_args.validate:
        print("Configuration validation complete.")
        print("=" * 60)
        return 0

    output_files = _generate_outputs(parsed_args, config)
    _print_completion_message(output_files)

    return 0


if __name__ == "__main__":
    sys.exit(main())
