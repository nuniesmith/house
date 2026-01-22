# Floor Plan Generator

A Python-based floor plan generator using matplotlib that creates professional architectural floor plans from YAML configuration files.

## Features

- **YAML Configuration**: All floor plan data is stored in an easy-to-edit YAML file
- **Modular Architecture**: Clean separation of concerns with dedicated packages
- **Data-Driven Design**: Rooms, doors, windows, furniture, and annotations are defined as structured data
- **Auto-Dimensioning**: Automatically adds dimension labels to rooms
- **Debug Grid Mode**: Optional grid overlay for development and alignment
- **Multiple Output Formats**: PNG images, SVG vectors, and multi-page PDF
- **Scalable**: Global scale factor for easy resizing
- **Color Theming**: Centralized color scheme for consistent styling
- **Config Validation**: Early error detection for configuration issues

## Project Structure

```
src/python/
├── main.py                 # Entry point - run this to generate floor plans
├── config/
│   └── config.yaml  # YAML configuration file
├── models/
│   └── __init__.py         # Data classes (Room, Door, Window, etc.)
├── utilities/
│   └── __init__.py         # Helper functions (scale, colors, validation)
├── drawing/
│   └── __init__.py         # Matplotlib drawing functions
├── generators/
│   └── __init__.py         # Floor plan generation and export functions
├── defaults/
│   └── __init__.py         # Default floor plan data constants
├── output/                 # Generated floor plan files
├── reference/              # Reference images
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install matplotlib PyYAML
```

## Usage

### Basic Usage

Run the generator to create all floor plans:

```bash
python main.py
```

This will generate in the `output/` directory:
- `main_floor_plan.png` - Main floor plan image
- `basement_floor_plan.png` - Basement floor plan image
- `main_floor_plan.svg` - Main floor plan vector graphic
- `basement_floor_plan.svg` - Basement floor plan vector graphic
- `floor_plans.pdf` - Combined multi-page PDF

### Command Line Options

```bash
python main.py --help           # Show help message
python main.py --png-only       # Only generate PNG files
python main.py --svg-only       # Only generate SVG files
python main.py --pdf-only       # Only generate combined PDF
python main.py --debug          # Enable debug mode (grid overlay)
python main.py --validate       # Only validate config, don't generate
python main.py --config my.yaml # Use custom config file
```

### Configuration

All floor plan data is stored in `config/config.yaml`. Edit this file to modify:

#### Global Settings

```yaml
settings:
  scale: 1.0           # Scale factor for all dimensions
  debug_mode: false    # Set to true to show grid overlay
  grid_spacing: 10     # Grid line spacing in feet
  auto_dimensions: true # Automatically add room dimension labels
  output_dpi: 300      # Output image resolution
  show_north_arrow: true # Display north arrow indicator
```

#### Colors

Define your color palette:

```yaml
colors:
  bedroom: "#fffacd"
  bathroom: "#e6f3ff"
  kitchen: "#e8f5e9"
  living: "#fff3e0"
  # ... add more colors
```

#### Rooms

Add or modify rooms:

```yaml
rooms:
  - x: 45              # X coordinate (feet from origin)
    y: 81              # Y coordinate
    width: 25          # Room width
    height: 29         # Room height
    label: "Garage"    # Room name
    color: garage      # Color (references colors section or hex)
    label_fontsize: 10
    auto_dimension: true
    dimension_text: "25' x 29'"
    notes: "2 Car"     # Optional additional notes
```

#### Doors

Define door locations and swing directions:

```yaml
doors:
  - x: 58
    y: 70
    width: 3
    direction: down    # right, left, up, down
    swing: right       # right, left, up, down
```

#### Windows

Add windows to walls:

```yaml
windows:
  - x: 5
    y: 81
    width: 8
    orientation: horizontal  # horizontal or vertical
```

#### Furniture

Add furniture and special elements:

```yaml
furniture:
  - type: rectangle    # rectangle, circle, or ellipse
    x: 23
    y: 35
    width: 4
    height: 12
    color: wood
    label: "Bar Counter"
    rotation: 90
```

#### Stairs

Define stairways:

```yaml
stairs:
  - x: 20
    y: 45
    width: 12
    height: 6
    num_steps: 10
    orientation: horizontal
    label: "DN"
```

#### Fireplaces

Add fireplace symbols:

```yaml
fireplaces:
  - x: 35
    y: 63
    width: 4
    height: 3
    label: "Gas Fireplace"
```

### Debug Mode

Enable debug mode to show a grid overlay for easier positioning:

1. Edit `config/config.yaml`:
   ```yaml
   settings:
     debug_mode: true
     grid_spacing: 10
   ```

2. Or use the command line flag:
   ```bash
   python main.py --debug
   ```

### Programmatic Usage

You can also use the generator as a module:

```python
import sys
from pathlib import Path

# Add the src/python directory to path
sys.path.insert(0, str(Path(__file__).parent))

from generators import (
    load_config,
    apply_config_settings,
    generate_main_floor,
    generate_basement,
    generate_combined_pdf,
    generate_svg,
)

# Load configuration
config = load_config("config/config.yaml")
apply_config_settings(config)

# Generate individual floor plans
generate_main_floor(config)
generate_basement(config)

# Generate SVG files
generate_svg("main", config)
generate_svg("basement", config)

# Or generate combined PDF
generate_combined_pdf("my_floor_plans.pdf", config)
```

### Using Individual Modules

```python
# Models - Data classes for floor plan elements
from models import Room, Door, Window, Furniture, Stairs

# Utilities - Helper functions
from utilities import (
    scale,
    format_dimension,
    resolve_color,
    validate_config,
    rooms_adjacent,
)

# Drawing - Matplotlib drawing functions
from drawing import (
    add_room,
    add_door,
    add_window,
    add_furniture,
    draw_rooms_from_data,
)

# Defaults - Default floor plan data
from defaults import (
    MAIN_FLOOR_ROOMS_DEFAULT,
    BASEMENT_ROOMS_DEFAULT,
)
```

## Output Formats

### PNG (Raster)
- High-resolution bitmap images
- Best for: Printing, presentations, quick viewing
- Default DPI: 300 (configurable)

### SVG (Vector)
- Scalable vector graphics
- Best for: Web embedding, CAD import, editing in Inkscape/Illustrator
- Infinite scaling without quality loss

### PDF (Multi-page)
- Combined document with all floor plans
- Best for: Professional documentation, sharing, printing multiple pages

## Customization Tips

1. **Adding a new room type**: Add a new color to the `colors` section, then reference it in your room definitions.

2. **Changing the scale**: Modify `settings.scale` to resize all elements proportionally.

3. **Fine-tuning positions**: Enable `debug_mode` to see the grid, then adjust coordinates.

4. **Adding annotations**: Use `text_annotations` for labels that aren't attached to rooms.

5. **Custom furniture**: Use the `furniture` section with `rectangle`, `circle`, or `ellipse` types.

6. **Extending functionality**: Add new drawing functions to `drawing/__init__.py` or new data classes to `models/__init__.py`.

## Troubleshooting

### Import errors
Make sure you're running from the `src/python` directory:
```bash
cd src/python
python main.py
```

### PyYAML not installed
If PyYAML is not available, the generator will use built-in default configuration. Install it with:
```bash
pip install PyYAML
```

### Matplotlib not installed
Install matplotlib:
```bash
pip install matplotlib
```

### Output files not generating
Check that the `output/` directory exists and you have write permissions.

### Config validation warnings
Run with `--validate` to see all configuration issues:
```bash
python main.py --validate
```

## License

This project is for personal use.