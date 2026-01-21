# Floor Plan Generator

A Python-based floor plan generator using matplotlib that creates professional architectural floor plans from YAML configuration files.

## Features

- **YAML Configuration**: All floor plan data is stored in an easy-to-edit YAML file
- **Data-Driven Design**: Rooms, doors, windows, furniture, and annotations are defined as structured data
- **Auto-Dimensioning**: Automatically adds dimension labels to rooms
- **Debug Grid Mode**: Optional grid overlay for development and alignment
- **Multiple Output Formats**: PNG images and multi-page PDF
- **Scalable**: Global scale factor for easy resizing
- **Color Theming**: Centralized color scheme for consistent styling

## Installation

1. Install the required dependencies:

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
python floor_plan_generator.py
```

This will generate:
- `main_floor_plan.png` - Main floor plan image
- `basement_floor_plan.png` - Basement floor plan image
- `floor_plans.pdf` - Combined multi-page PDF

### Configuration

All floor plan data is stored in `floor_plan_config.yaml`. Edit this file to modify:

#### Global Settings

```yaml
settings:
  scale: 1.0           # Scale factor for all dimensions
  debug_mode: false    # Set to true to show grid overlay
  grid_spacing: 10     # Grid line spacing in feet
  auto_dimensions: true # Automatically add room dimension labels
  output_dpi: 300      # Output image resolution
```

#### Colors

Define your color palette:

```yaml
colors:
  bedroom: "#fffacd"
  bathroom: "#e6f3ff"
  kitchen: "#e8f5e9"
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

1. Edit `floor_plan_config.yaml`:
   ```yaml
   settings:
     debug_mode: true
     grid_spacing: 10
   ```

2. Run the generator - grid lines will appear on the output

### Programmatic Usage

You can also use the generator as a module:

```python
from floor_plan_generator import (
    load_config,
    apply_config_settings,
    generate_main_floor,
    generate_basement,
    generate_combined_pdf,
)

# Load configuration
config = load_config("custom_config.yaml")
apply_config_settings(config)

# Generate individual floor plans
generate_main_floor(config)
generate_basement(config)

# Or generate combined PDF
generate_combined_pdf("my_floor_plans.pdf", config)
```

## File Structure

```
src/python/
├── floor_plan_generator.py  # Main generator script
├── floor_plan_config.yaml   # Configuration file
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Output Examples

The generator creates detailed floor plans with:
- Room outlines with labels and dimensions
- Door swings with arc indicators
- Window symbols
- Stairway symbols with step lines
- Fireplace symbols
- Furniture and special elements
- Dimension arrows for overall size
- Color-coded rooms by type

## Customization Tips

1. **Adding a new room type**: Add a new color to the `colors` section, then reference it in your room definitions.

2. **Changing the scale**: Modify `settings.scale` to resize all elements proportionally.

3. **Fine-tuning positions**: Enable `debug_mode` to see the grid, then adjust coordinates.

4. **Adding annotations**: Use `text_annotations` for labels that aren't attached to rooms.

5. **Custom furniture**: Use the `furniture` section with `rectangle`, `circle`, or `ellipse` types.

## Troubleshooting

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
Check that you have write permissions in the current directory.

## License

This project is for personal use.