# Modern Farmhouse Construction Guide & Specifications

## Project Overview
This comprehensive guide details the construction of a 3,200 sq ft modern farmhouse combining traditional farmhouse aesthetics with contemporary functionality and energy efficiency.

## Programmatic Floor Plan Generation

This project includes tools to define floor plans in code and generate 2D SVG visualizations.

### Floor Plan Definition Formats

Floor plans can be defined in two ways:

1. **JSON files** - Edit `luxury_farmhouse.json` to modify room layouts
2. **Rust code** - Use the `FloorPlanBuilder` API for programmatic creation

### Generating Floor Plan Images

Use the `render_floorplan` CLI tool:

```bash
# Render built-in luxury farmhouse
cargo run --package floorplan-core --bin render_floorplan -- --output floorplan.html

# Load from JSON file
cargo run --package floorplan-core --bin render_floorplan -- \
  --input src/projects/farmhouse/luxury_farmhouse.json \
  --output my_plan.html

# Use blueprint style
cargo run --package floorplan-core --bin render_floorplan -- --style blueprint

# Get example JSON template
cargo run --package floorplan-core --bin render_floorplan -- --example-json > template.json

# Show floor plan info
cargo run --package floorplan-core --bin render_floorplan -- --info
```

### CLI Options

| Option | Description |
|--------|-------------|
| `-i, --input <FILE>` | Load floor plan from JSON file |
| `-o, --output <FILE>` | Save output to file (default: stdout) |
| `-s, --style <STYLE>` | Color scheme: `default`, `blueprint`, `color-coded` |
| `--scale <N>` | Pixels per foot (default: 10) |
| `--no-grid` | Hide grid lines |
| `--no-labels` | Hide room labels |
| `--no-dimensions` | Hide room dimensions |
| `--svg-only` | Output raw SVG instead of HTML |

### JSON Format Example

```json
{
  "name": "My Floor Plan",
  "description": "Example floor plan",
  "level": 1,
  "rooms": [
    {
      "name": "Living Room",
      "type": "living_room",
      "x": 0.0,
      "y": 0.0,
      "length": "20'-0\"",
      "width": "15'-0\"",
      "ceiling": "9'-0\""
    },
    {
      "name": "Kitchen",
      "type": "kitchen",
      "x": 20.0,
      "y": 0.0,
      "length": "15'-0\"",
      "width": "12'-0\""
    }
  ],
  "walls": []
}
```

### Available Room Types

`living_room`, `family_room`, `great_room`, `lounge`, `foyer`, `hallway`,
`master_suite`, `bedroom`, `guest_room`, `nursery`,
`master_bath`, `full_bath`, `half_bath`, `powder_room`,
`kitchen`, `dining_room`, `breakfast_nook`, `pantry`, `butlers_pantry`, `bar`,
`laundry`, `mud_room`, `utility`, `storage`, `closet`, `walk_in_closet`,
`office`, `study`, `library`,
`porch`, `deck`, `patio`, `sunroom`, `screened`,
`garage`, `carport`, `workshop`,
`basement`, `attic`, `mechanical`

### Generated Files

- `luxury_floorplan.html` - Color-coded floor plan
- `luxury_floorplan_blueprint.html` - Blueprint-style rendering
- `luxury_farmhouse.json` - Editable JSON definition

---

## Design Philosophy: Farmhouse Meets Modern

### Core Design Elements:
- **Exterior**: Clean lines with traditional proportions
- **Materials**: Natural and durable with authentic textures
- **Layout**: Open concept with defined functional zones
- **Lighting**: Abundant natural light with strategic artificial lighting
- **Technology**: Modern systems integrated seamlessly

## Enhanced Floor Plan Summary

### Total Square Footage: 3,200 sq ft
- **Living Space**: 2,100 sq ft
- **Garage**: 720 sq ft (3-car)
- **Utility/Storage**: 380 sq ft
- **Outdoor Living**: 800 sq ft (covered porches & decks)

### Room Layout Enhancements:

#### **Great Room (400 sq ft)**
- Open concept design connecting to kitchen and dining
- Stone fireplace as focal point with floor-to-ceiling surround
- Exposed wood beam ceiling (faux or real)
- Large windows for natural light
- Built-in entertainment center

#### **Kitchen (280 sq ft)**
- Modern farmhouse design with oversized island
- Quartz countertops with waterfall edge on island
- Shaker-style cabinets with soft-close hardware
- Farm sink with bridge faucet
- Professional-grade appliance package
- Walk-in pantry with organization systems

#### **Master Suite (420 sq ft total)**
- **Bedroom**: 300 sq ft with tray ceiling
- **Bathroom**: 120 sq ft with dual vanities, walk-in shower, soaking tub
- **Closet**: Walk-in with built-in organization
- **Private deck**: 150 sq ft outdoor retreat

#### **Secondary Spaces**
- **Office**: 150 sq ft with built-in desk and storage
- **Guest bedroom**: 200 sq ft with easy bathroom access
- **Dining room**: 220 sq ft with coffered ceiling detail

## 1. Foundation and Structural Systems

### 1.1 Foundation System

**Foundation Type**: Full basement with poured concrete walls
- **Depth**: 8 feet below grade
- **Wall thickness**: 10 inches with integral waterproofing
- **Footings**: 24" × 12" continuous reinforced concrete
- **Vapor barrier**: 6-mil polyethylene under slab
- **Insulation**: R-15 rigid foam on exterior walls
- **Drainage**: Full perimeter drain tile system

**Basement Finishing Options**:
- Finished recreation room: 600 sq ft
- Additional bedroom: 200 sq ft
- Storage areas: 400 sq ft
- Mechanical room: 200 sq ft

### 1.2 Framing System

**Wall Framing**:
- **Exterior walls**: 2×6 studs @ 16" O.C.
- **Interior walls**: 2×4 studs @ 16" O.C.
- **Headers**: Engineered lumber for spans over 4 feet
- **Sheathing**: 7/16" OSB with house wrap
- **Insulation**: R-21 fiberglass batts in exterior walls

**Floor System**:
- **First floor**: 2×10 engineered I-joists @ 16" O.C.
- **Subfloor**: 3/4" tongue-and-groove OSB
- **Insulation**: R-30 in floor system over basement

**Roof System**:
- **Trusses**: Engineered wood trusses, 7:12 pitch
- **Sheathing**: 7/16" OSB with synthetic underlayment
- **Ventilation**: Ridge and soffit vents for continuous airflow
- **Insulation**: R-49 blown-in cellulose in attic

### 1.3 Enhanced Structural Features

**Exposed Beam Details**:
- **Great room**: Faux wood beams (hollow composite)
- **Kitchen**: Single beam over island (structural LVL)
- **Dining**: Coffered ceiling with decorative beams

**Ceiling Heights**:
- **Great room**: 12 feet with exposed beams
- **Kitchen**: 10 feet with recessed lighting
- **Bedrooms**: 9 feet standard
- **Basement**: 9 feet finished ceiling

## 2. Exterior Design and Materials

### 2.1 Siding and Trim

**Primary Siding**: Fiber cement board and batten
- **Brand**: James Hardie or equivalent
- **Color**: Farmhouse white or light gray
- **Installation**: Horizontal with 8" reveal
- **Trim**: 1×4 composite trim boards

**Accent Materials**:
- **Stone veneer**: Natural fieldstone on foundation and accent walls
- **Metal accents**: Standing seam panels on gables
- **Wood elements**: Cedar posts and railings on porches

### 2.2 Roofing System

**Metal Roofing**: Standing seam system
- **Material**: 24-gauge steel with Kynar coating
- **Color**: Charcoal or dark bronze
- **Warranty**: 40-year paint, 25-year substrate
- **Accessories**: Snow guards, gutters, downspouts

**Roof Details**:
- **Exposed rafter tails**: Decorative beam ends
- **Gutters**: 6" seamless aluminum in bronze
- **Downspouts**: 3×4" rectangular, integrated design

### 2.3 Windows and Doors

**Windows**: Triple-pane, low-E coating
- **Frame material**: Vinyl or fiberglass
- **Style**: Double-hung and casement combinations
- **Grid pattern**: Divided lite for farmhouse aesthetic
- **Color**: Black exterior, white interior
- **Performance**: U-factor 0.22 or better

**Exterior Doors**:
- **Front door**: Wood or fiberglass with glass panels
- **Back door**: French doors to deck
- **Garage doors**: Carriage house style with windows
- **Hardware**: Oil-rubbed bronze finish

## 3. Interior Design and Finishes

### 3.1 Flooring Systems

**Hardwood Flooring**: 
- **Species**: White oak or hickory
- **Width**: 5" or 7" wide planks
- **Finish**: Matte polyurethane in natural or light stain
- **Installation**: Nail-down over subfloor
- **Coverage**: Living areas, bedrooms, hallways

**Tile Flooring**:
- **Bathrooms**: Large format porcelain (12"×24")
- **Laundry**: Luxury vinyl plank (waterproof)
- **Mudroom**: Slip-resistant ceramic tile

### 3.2 Kitchen Design Details

**Cabinetry**: Shaker style in painted or stained finish
- **Upper cabinets**: 42" height to ceiling
- **Lower cabinets**: Soft-close drawers and doors
- **Island**: Contrasting color with butcher block top
- **Hardware**: Cup pulls and knobs in matte black

**Countertops**:
- **Perimeter**: Quartz in neutral color
- **Island**: Butcher block or quartz waterfall edge
- **Backsplash**: Subway tile with dark grout

**Appliances**: Professional-style package
- **Range**: 36" dual-fuel or gas range
- **Hood**: Custom wood hood with metal insert
- **Refrigerator**: Counter-depth French door
- **Dishwasher**: Quiet operation, panel-ready
- **Microwave**: Built-in or over-range

### 3.3 Bathroom Finishes

**Master Bathroom**:
- **Vanity**: Double vanity with quartz tops
- **Shower**: Walk-in with glass enclosure
- **Tub**: Freestanding soaking tub
- **Tile**: Large format on walls, mosaic accent
- **Lighting**: Vanity sconces and recessed ceiling

**Guest Bathrooms**:
- **Vanity**: Single with storage
- **Shower/tub**: Combo unit with tile surround
- **Flooring**: Ceramic tile
- **Fixtures**: Brushed nickel finish

### 3.4 Interior Paint and Trim

**Paint Colors**:
- **Walls**: Warm whites and soft grays
- **Trim**: Crisp white semi-gloss
- **Accent walls**: Shiplap with natural or painted finish
- **Ceilings**: White flat paint

**Trim Details**:
- **Baseboards**: 5.5" MDF with shoe molding
- **Door/window casing**: 3.5" flat casing
- **Crown molding**: 4.5" in main living areas
- **Wainscoting**: Board and batten in dining room

## 4. Mechanical, Electrical, and Plumbing Systems

### 4.1 HVAC System

**Primary System**: High-efficiency heat pump
- **Capacity**: 3-4 tons based on load calculation
- **Efficiency**: 16+ SEER, 9+ HSPF rating
- **Backup heat**: Electric resistance coils
- **Distribution**: Conventional ducted system
- **Zoning**: Two zones minimum (living/sleeping areas)

**Ductwork**:
- **Supply ducts**: Insulated flexible duct in conditioned space
- **Return air**: Central returns with adequate sizing
- **Ventilation**: ERV for fresh air exchange
- **Filtration**: MERV 11 filters minimum

**Additional Comfort**:
- **Ceiling fans**: Energy-efficient in all bedrooms and living areas
- **Smart thermostat**: Wi-Fi enabled with scheduling
- **Humidity control**: Whole-house dehumidifier

### 4.2 Plumbing System

**Water Supply**:
- **Service line**: 1" copper or PEX from meter
- **Distribution**: PEX-A tubing throughout house
- **Water heater**: Tankless gas or hybrid electric
- **Pressure**: Expansion tank and pressure regulator

**Fixtures and Fittings**:
- **Kitchen sink**: Farmhouse apron-front style
- **Bathroom sinks**: Undermount with quartz tops
- **Toilets**: Comfort height, elongated bowl
- **Showers**: Thermostatic mixing valves
- **Finish**: Brushed nickel or matte black

**Special Features**:
- **Instant hot water**: Recirculation pump system
- **Water softener**: If required by water quality
- **Outdoor spigots**: Freeze-proof on multiple sides
- **Washing machine**: Hot and cold supply with drain

### 4.3 Electrical System

**Service and Distribution**:
- **Main panel**: 200-amp service with 40+ circuits
- **Subpanel**: In basement for future expansion
- **GFCI protection**: All bathrooms, kitchen, outdoor areas
- **AFCI protection**: All bedroom and living area circuits

**Lighting Design**:
- **Recessed lights**: LED throughout with dimmer controls
- **Pendant lights**: Over kitchen island and dining table
- **Chandeliers**: In foyer and dining room
- **Under-cabinet**: LED strips in kitchen
- **Outdoor**: Security and accent lighting

**Technology Integration**:
- **Smart home wiring**: Cat6 data cabling throughout
- **Security system**: Pre-wired for alarm and cameras
- **Audio/video**: Surround sound pre-wire in great room
- **Electric vehicle**: 240V outlet in garage

## 5. Energy Efficiency and Sustainability

### 5.1 Building Envelope

**Insulation Package**:
- **Walls**: R-21 fiberglass batts
- **Ceiling**: R-49 blown-in cellulose
- **Basement**: R-15 rigid foam exterior
- **Air sealing**: Comprehensive caulking and weatherstripping

**Windows and Doors**:
- **Performance**: ENERGY STAR certified
- **Installation**: Properly flashed and sealed
- **Orientation**: South-facing windows for solar gain

### 5.2 Efficient Systems

**HVAC Efficiency**:
- **Equipment**: High-efficiency heat pump
- **Ductwork**: Sealed and insulated
- **Controls**: Programmable thermostats
- **Maintenance**: Annual service contracts

**Water Efficiency**:
- **Fixtures**: WaterSense labeled products
- **Appliances**: ENERGY STAR dishwasher and washing machine
- **Landscaping**: Native plants and efficient irrigation

**Lighting**:
- **LED fixtures**: Throughout entire house
- **Controls**: Dimmer switches and timers
- **Daylight**: Strategic window placement

## 6. Outdoor Living Spaces

### 6.1 Front Porch Design

**Structure**:
- **Size**: 32' × 8' covered area
- **Foundation**: Concrete slab with decorative stamping
- **Columns**: 8×8 wood posts with decorative brackets
- **Ceiling**: Beadboard with recessed lighting
- **Railing**: Horizontal cable or traditional balusters

**Features**:
- **Seating**: Built-in benches or furniture grouping
- **Lighting**: Pendant lights and wall sconces
- **Fans**: Ceiling fans for comfort
- **Electrical**: Outlets for seasonal decorations

### 6.2 Back Deck System

**Structure**:
- **Size**: 28' × 18' elevated deck
- **Framing**: Pressure-treated lumber with proper joist spacing
- **Decking**: Composite or pressure-treated lumber
- **Railing**: Cable rail or composite balusters
- **Stairs**: Wide stairs to yard level

**Features**:
- **Grilling area**: Gas line for outdoor kitchen
- **Seating**: Built-in benches with storage
- **Lighting**: LED step lights and post caps
- **Pergola**: Optional overhead structure for shade

### 6.3 Landscaping Integration

**Hardscaping**:
- **Driveway**: Concrete or asphalt with decorative borders
- **Walkways**: Natural stone or decorative concrete
- **Retaining walls**: Stone or segmental block
- **Outdoor lighting**: Landscape accent lighting

**Softscaping**:
- **Foundation plantings**: Native shrubs and perennials
- **Shade trees**: Strategic placement for energy savings
- **Lawn areas**: Drought-resistant grass varieties
- **Garden beds**: Raised beds for vegetables/herbs

## 7. Construction Timeline and Phases

### Phase 1: Site Preparation and Foundation (Weeks 1-6)
- Site survey and utility locating
- Excavation and foundation forming
- Concrete pour and curing
- Waterproofing and backfill
- Basement floor slab

### Phase 2: Framing and Roof (Weeks 7-12)
- Floor system installation
- Wall framing and sheathing
- Roof truss installation
- Roof sheathing and underlayment
- Windows and exterior doors

### Phase 3: Mechanical Rough-In (Weeks 13-16)
- Electrical rough wiring
- Plumbing rough-in
- HVAC ductwork installation
- Insulation installation
- Drywall installation

### Phase 4: Exterior Finishes (Weeks 17-22)
- Siding installation
- Roofing completion
- Exterior trim and paint
- Driveway and walkways
- Landscaping preparation

### Phase 5: Interior Finishes (Weeks 23-28)
- Drywall finishing and paint
- Flooring installation
- Kitchen and bathroom cabinetry
- Trim carpentry
- Fixture installation

### Phase 6: Final Details (Weeks 29-32)
- Appliance installation
- Final plumbing and electrical
- Exterior landscaping
- Final cleanup and inspections
- Move-in preparation

## 8. Cost Estimation

### Construction Cost Breakdown:

**Site Work and Foundation**: $95,000
- Excavation, foundation, basement finishing

**Framing and Structure**: $125,000
- Lumber, trusses, sheathing, insulation

**Exterior**: $140,000
- Siding, roofing, windows, doors

**Mechanical Systems**: $85,000
- HVAC, plumbing, electrical

**Interior Finishes**: $180,000
- Flooring, kitchen, bathrooms, paint, trim

**Specialty Items**: $45,000
- Fireplace, built-ins, outdoor spaces

**General Conditions**: $40,000
- Permits, insurance, temporary utilities

**Contractor Profit/Overhead**: $75,000

**Total Estimated Cost**: $785,000

*Note: Costs vary significantly by location, material selections, and market conditions. This estimate assumes mid-to-upper level finishes and current material costs.*

## 9. Maintenance and Long-Term Care

### Annual Maintenance Tasks:
- HVAC system service and filter changes
- Roof and gutter inspection and cleaning
- Exterior caulk and paint touch-ups
- Deck staining and sealing
- Window and door hardware lubrication

### 5-Year Maintenance:
- Exterior paint refresh
- Deck refinishing
- HVAC ductwork cleaning
- Water heater service
- Appliance warranty service

### 10-Year Major Items:
- Roof inspection and minor repairs
- Exterior siding maintenance
- Interior paint refresh
- Flooring refinishing
- Landscape renovation

This modern farmhouse design successfully combines traditional aesthetics with contemporary functionality, creating a timeless home that will provide comfort and value for generations.