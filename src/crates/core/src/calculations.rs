//! # Calculations Module
//!
//! Provides material takeoff calculations and cost estimation
//! based on floor plans and room specifications.

use crate::materials::{self, Material, MaterialLineItem, MaterialList};
use crate::models::{FloorPlan, Project, QualityTier, Room, RoomType, Wall, WallType};
use crate::units::{FeetInches, LinearFeet};

/// Configuration for material calculations
#[derive(Debug, Clone)]
pub struct CalculationConfig {
    /// Stud spacing in inches (typically 16 or 24)
    pub stud_spacing: u8,
    /// Quality tier for pricing
    pub quality_tier: QualityTier,
    /// Include waste factor in calculations
    pub include_waste: bool,
    /// Default waste factor for lumber (e.g., 1.1 = 10% waste)
    pub lumber_waste_factor: f64,
    /// Default waste factor for sheet goods
    pub sheet_goods_waste_factor: f64,
    /// Default waste factor for flooring
    pub flooring_waste_factor: f64,
    /// Default waste factor for paint
    pub paint_waste_factor: f64,
}

impl Default for CalculationConfig {
    fn default() -> Self {
        Self {
            stud_spacing: 16,
            quality_tier: QualityTier::Standard,
            include_waste: true,
            lumber_waste_factor: 1.10,
            sheet_goods_waste_factor: 1.10,
            flooring_waste_factor: 1.10,
            paint_waste_factor: 1.15,
        }
    }
}

/// Result of a material calculation
#[derive(Debug, Clone)]
pub struct CalculationResult {
    /// Name/description of what was calculated
    pub description: String,
    /// The material list
    pub materials: MaterialList,
    /// Total cost at the configured quality tier
    pub total_cost: f64,
    /// Cost per square foot
    pub cost_per_sqft: Option<f64>,
    /// Any warnings or notes
    pub notes: Vec<String>,
}

impl CalculationResult {
    pub fn new(
        description: impl Into<String>,
        materials: MaterialList,
        config: &CalculationConfig,
    ) -> Self {
        let total_cost = materials.total_cost(&config.quality_tier);
        Self {
            description: description.into(),
            materials,
            total_cost,
            cost_per_sqft: None,
            notes: Vec::new(),
        }
    }

    pub fn with_sqft(mut self, sqft: f64) -> Self {
        if sqft > 0.0 {
            self.cost_per_sqft = Some(self.total_cost / sqft);
        }
        self
    }

    pub fn add_note(&mut self, note: impl Into<String>) {
        self.notes.push(note.into());
    }
}

/// Calculator for wall framing materials
pub struct WallFramingCalculator;

impl WallFramingCalculator {
    /// Calculate studs needed for a wall length
    pub fn studs_needed(wall_length: LinearFeet, stud_spacing: u8) -> u32 {
        let length_inches = wall_length.value() * 12.0;
        let spacing = stud_spacing as f64;

        // Number of bays + 1 for the end stud + extras for corners/intersections
        let base_studs = (length_inches / spacing).ceil() as u32 + 1;

        // Add corner studs (typically 3 studs per corner)
        // This is a simplified calculation
        base_studs + 2
    }

    /// Calculate plate material needed (top and bottom plates)
    pub fn plate_length(wall_length: LinearFeet) -> LinearFeet {
        // Single bottom plate + double top plate = 3x wall length
        LinearFeet::new(wall_length.value() * 3.0)
    }

    /// Calculate header material for an opening
    pub fn header_for_opening(opening_width: FeetInches) -> LinearFeet {
        // Header is typically opening width + 6" for king studs on each side
        // Double header, so 2x the length
        let header_length = opening_width.to_decimal_feet() + 0.5;
        LinearFeet::new(header_length * 2.0)
    }

    /// Calculate materials for a single wall
    pub fn calculate_wall(
        wall: &Wall,
        _ceiling_height: FeetInches,
        config: &CalculationConfig,
    ) -> MaterialList {
        let mut list = MaterialList::new(format!("Wall Framing"));
        let wall_length = wall.length();
        let is_exterior = wall.wall_type.is_exterior();

        // Determine stud size based on wall type
        let (stud_material, plate_material) = if is_exterior {
            (
                materials::lumber::stud_2x6_8ft(),
                materials::lumber::plate_2x6(),
            )
        } else {
            (
                materials::lumber::stud_2x4_8ft(),
                materials::lumber::plate_2x4(),
            )
        };

        // Calculate studs
        let stud_count = Self::studs_needed(wall_length, config.stud_spacing);
        let mut stud_item = MaterialLineItem::new(stud_material, stud_count as f64);
        if config.include_waste {
            stud_item = stud_item.with_waste(config.lumber_waste_factor);
        }
        list.add_item(stud_item);

        // Calculate plates
        let plate_lf = Self::plate_length(wall_length);
        let mut plate_item = MaterialLineItem::new(plate_material, plate_lf.value());
        if config.include_waste {
            plate_item = plate_item.with_waste(config.lumber_waste_factor);
        }
        list.add_item(plate_item);

        // Calculate headers for doors and windows
        let header_material = materials::lumber::header_2x10();
        for door in &wall.doors {
            let header_lf = Self::header_for_opening(door.width);
            list.add_item(
                MaterialLineItem::new(header_material.clone(), header_lf.value())
                    .with_location(format!("Door header")),
            );
        }
        for window in &wall.windows {
            let header_lf = Self::header_for_opening(window.width);
            list.add_item(
                MaterialLineItem::new(header_material.clone(), header_lf.value())
                    .with_location(format!("Window header")),
            );
        }

        list
    }

    /// Calculate framing for all walls in a floor plan
    pub fn calculate_floor_plan(
        floor_plan: &FloorPlan,
        config: &CalculationConfig,
    ) -> CalculationResult {
        let mut combined_list = MaterialList::new(format!("{} - Wall Framing", floor_plan.name));

        let default_ceiling = FeetInches::new(9, 0);

        for wall in &floor_plan.walls {
            let wall_list = Self::calculate_wall(wall, default_ceiling, config);
            combined_list.merge(wall_list);
        }

        let sqft = floor_plan.total_floor_area().value();
        CalculationResult::new(
            format!("{} - Wall Framing", floor_plan.name),
            combined_list,
            config,
        )
        .with_sqft(sqft)
    }
}

/// Calculator for drywall materials
pub struct DrywallCalculator;

impl DrywallCalculator {
    /// Calculate drywall sheets needed for a given square footage
    pub fn sheets_needed(sqft: f64, sheet_sqft: f64) -> f64 {
        (sqft / sheet_sqft).ceil()
    }

    /// Calculate drywall for a room
    pub fn calculate_room(room: &Room, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new(format!("{} - Drywall", room.name));

        // Wall area
        let wall_sqft = room.wall_area().value();

        // Ceiling area
        let ceiling_sqft = room.ceiling_area().value();

        // Total area
        let total_sqft = wall_sqft + ceiling_sqft;

        // Choose drywall type based on room
        let drywall = if room.room_type.is_wet_room() {
            // Use moisture-resistant or cement board for wet areas
            materials::sheet_goods::cement_board()
        } else {
            materials::sheet_goods::drywall_1_2()
        };

        let sheet_coverage = drywall.coverage.unwrap_or(32.0);
        let sheets = Self::sheets_needed(total_sqft, sheet_coverage);

        let mut item = MaterialLineItem::new(drywall, sheets).with_location(room.name.clone());
        if config.include_waste {
            item = item.with_waste(config.sheet_goods_waste_factor);
        }
        list.add_item(item);

        // Add drywall screws (approximately 1 box per 500 sqft)
        let screw_boxes = (total_sqft / 500.0).ceil();
        list.add_item(MaterialLineItem::new(
            materials::fasteners::drywall_screws(),
            screw_boxes,
        ));

        // Add joint compound and tape (approximation)
        // Typically need about 1 gallon of mud per 100 sqft

        list
    }

    /// Calculate drywall for entire floor plan
    pub fn calculate_floor_plan(
        floor_plan: &FloorPlan,
        config: &CalculationConfig,
    ) -> CalculationResult {
        let mut combined_list = MaterialList::new(format!("{} - Drywall", floor_plan.name));

        for room in &floor_plan.rooms {
            // Skip outdoor spaces
            if room.room_type.is_outdoor() {
                continue;
            }
            let room_list = Self::calculate_room(room, config);
            combined_list.merge(room_list);
        }

        let sqft = floor_plan.total_living_area().value();
        CalculationResult::new(
            format!("{} - Drywall", floor_plan.name),
            combined_list,
            config,
        )
        .with_sqft(sqft)
    }
}

/// Calculator for insulation materials
pub struct InsulationCalculator;

impl InsulationCalculator {
    /// Calculate insulation for exterior walls of a room
    pub fn calculate_exterior_walls(
        wall_sqft: f64,
        wall_type: WallType,
        config: &CalculationConfig,
    ) -> MaterialList {
        let mut list = MaterialList::new("Exterior Wall Insulation");

        let insulation = if matches!(
            wall_type,
            WallType::ExteriorLoadBearing | WallType::ExteriorNonBearing
        ) {
            // 2x6 walls get R-19
            materials::insulation::batt_r19()
        } else {
            // 2x4 walls get R-13
            materials::insulation::batt_r13()
        };

        let mut item = MaterialLineItem::new(insulation, wall_sqft);
        if config.include_waste {
            item = item.with_waste(config.lumber_waste_factor);
        }
        list.add_item(item);

        list
    }

    /// Calculate attic/ceiling insulation
    pub fn calculate_attic(ceiling_sqft: f64, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new("Attic Insulation");

        let insulation = materials::insulation::batt_r38();
        let mut item = MaterialLineItem::new(insulation, ceiling_sqft);
        if config.include_waste {
            item = item.with_waste(config.lumber_waste_factor);
        }
        list.add_item(item);

        list
    }
}

/// Calculator for flooring materials
pub struct FlooringCalculator;

impl FlooringCalculator {
    /// Determine appropriate flooring type for a room
    pub fn default_flooring_for_room(room_type: &RoomType) -> Material {
        match room_type {
            // Wet areas get tile or LVP
            RoomType::MasterBath
            | RoomType::FullBath
            | RoomType::HalfBath
            | RoomType::PowderRoom => materials::flooring::tile_porcelain(),
            RoomType::Kitchen | RoomType::Laundry | RoomType::MudRoom => materials::flooring::lvp(),
            // Bedrooms get carpet
            RoomType::MasterSuite | RoomType::Bedroom | RoomType::GuestRoom | RoomType::Nursery => {
                materials::flooring::carpet()
            }
            // Living areas get hardwood
            RoomType::LivingRoom
            | RoomType::FamilyRoom
            | RoomType::GreatRoom
            | RoomType::DiningRoom
            | RoomType::Office
            | RoomType::Study
            | RoomType::Library => materials::flooring::hardwood_oak(),
            // Utility areas
            RoomType::Garage | RoomType::Workshop | RoomType::Basement => {
                // Typically concrete, no additional flooring
                materials::flooring::lvp() // Return something; actual use would be concrete sealer
            }
            // Outdoor - composite decking or concrete
            RoomType::Porch | RoomType::Deck | RoomType::Patio | RoomType::Screened => {
                materials::flooring::tile_porcelain()
            }
            // Default
            _ => materials::flooring::lvp(),
        }
    }

    /// Calculate flooring for a room
    pub fn calculate_room(room: &Room, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new(format!("{} - Flooring", room.name));

        let floor_sqft = room.floor_area().value();
        let flooring = Self::default_flooring_for_room(&room.room_type);

        let mut item = MaterialLineItem::new(flooring, floor_sqft).with_location(room.name.clone());
        if config.include_waste {
            item = item.with_waste(config.flooring_waste_factor);
        }
        list.add_item(item);

        // Add underlayment for hardwood and LVP
        // (Tile doesn't need underlayment, carpet has pad included)
        match room.room_type {
            RoomType::LivingRoom
            | RoomType::FamilyRoom
            | RoomType::GreatRoom
            | RoomType::DiningRoom
            | RoomType::Office
            | RoomType::Study
            | RoomType::Library
            | RoomType::Kitchen
            | RoomType::Laundry
            | RoomType::MudRoom => {
                let mut underlayment =
                    MaterialLineItem::new(materials::flooring::underlayment(), floor_sqft);
                if config.include_waste {
                    underlayment = underlayment.with_waste(config.flooring_waste_factor);
                }
                list.add_item(underlayment);
            }
            _ => {}
        }

        list
    }

    /// Calculate flooring for entire floor plan
    pub fn calculate_floor_plan(
        floor_plan: &FloorPlan,
        config: &CalculationConfig,
    ) -> CalculationResult {
        let mut combined_list = MaterialList::new(format!("{} - Flooring", floor_plan.name));

        for room in &floor_plan.rooms {
            let room_list = Self::calculate_room(room, config);
            combined_list.merge(room_list);
        }

        let sqft = floor_plan.total_floor_area().value();
        CalculationResult::new(
            format!("{} - Flooring", floor_plan.name),
            combined_list,
            config,
        )
        .with_sqft(sqft)
    }
}

/// Calculator for trim and millwork
pub struct TrimCalculator;

impl TrimCalculator {
    /// Calculate baseboard for a room
    pub fn calculate_baseboard(room: &Room, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new(format!("{} - Baseboard", room.name));

        let perimeter = room.perimeter().value();

        // Use wood baseboard for premium/luxury, MDF for economy/standard
        let baseboard = match config.quality_tier {
            QualityTier::Economy | QualityTier::Standard => materials::trim::baseboard_mdf(),
            QualityTier::Premium | QualityTier::Luxury => materials::trim::baseboard_wood(),
        };

        let mut item = MaterialLineItem::new(baseboard, perimeter).with_location(room.name.clone());
        if config.include_waste {
            item = item.with_waste(config.lumber_waste_factor);
        }
        list.add_item(item);

        list
    }

    /// Calculate crown moulding for a room (if applicable)
    pub fn calculate_crown(room: &Room, config: &CalculationConfig) -> Option<MaterialList> {
        // Only add crown moulding to living areas for premium/luxury tiers
        if !matches!(
            config.quality_tier,
            QualityTier::Premium | QualityTier::Luxury
        ) {
            return None;
        }

        match room.room_type {
            RoomType::LivingRoom
            | RoomType::FamilyRoom
            | RoomType::GreatRoom
            | RoomType::DiningRoom
            | RoomType::MasterSuite
            | RoomType::Office
            | RoomType::Foyer
            | RoomType::Lounge => {
                let mut list = MaterialList::new(format!("{} - Crown Moulding", room.name));
                let perimeter = room.perimeter().value();

                let mut item = MaterialLineItem::new(materials::trim::crown_moulding(), perimeter)
                    .with_location(room.name.clone());
                if config.include_waste {
                    item = item.with_waste(config.lumber_waste_factor);
                }
                list.add_item(item);

                Some(list)
            }
            _ => None,
        }
    }

    /// Calculate door casing for a room based on door count
    pub fn calculate_door_casing(door_count: u32, _config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new("Door Casing");

        let item = MaterialLineItem::new(materials::trim::door_casing(), door_count as f64);
        list.add_item(item);

        list
    }

    /// Calculate all trim for a floor plan
    pub fn calculate_floor_plan(
        floor_plan: &FloorPlan,
        config: &CalculationConfig,
    ) -> CalculationResult {
        let mut combined_list = MaterialList::new(format!("{} - Trim", floor_plan.name));

        for room in &floor_plan.rooms {
            if room.room_type.is_outdoor() || matches!(room.room_type, RoomType::Garage) {
                continue;
            }

            // Baseboard for all interior rooms
            let baseboard_list = Self::calculate_baseboard(room, config);
            combined_list.merge(baseboard_list);

            // Crown moulding for select rooms
            if let Some(crown_list) = Self::calculate_crown(room, config) {
                combined_list.merge(crown_list);
            }
        }

        // Door casing
        let total_doors: u32 = floor_plan.walls.iter().map(|w| w.doors.len() as u32).sum();
        if total_doors > 0 {
            let door_casing = Self::calculate_door_casing(total_doors, config);
            combined_list.merge(door_casing);
        }

        // Window casing
        let total_windows: u32 = floor_plan
            .walls
            .iter()
            .map(|w| w.windows.len() as u32)
            .sum();
        if total_windows > 0 {
            let item =
                MaterialLineItem::new(materials::trim::window_casing(), total_windows as f64);
            combined_list.add_item(item);
        }

        let sqft = floor_plan.total_living_area().value();
        CalculationResult::new(format!("{} - Trim", floor_plan.name), combined_list, config)
            .with_sqft(sqft)
    }
}

/// Calculator for paint
pub struct PaintCalculator;

impl PaintCalculator {
    /// Calculate paint for walls
    pub fn calculate_wall_paint(wall_sqft: f64, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new("Wall Paint");

        let paint = materials::paint::interior_wall_paint();
        let coverage = paint.coverage.unwrap_or(400.0);

        // Two coats typically
        let gallons = (wall_sqft * 2.0 / coverage).ceil();

        let mut item = MaterialLineItem::new(paint, gallons);
        if config.include_waste {
            item = item.with_waste(config.paint_waste_factor);
        }
        list.add_item(item);

        // Add primer (one coat)
        let primer = materials::paint::primer();
        let primer_coverage = primer.coverage.unwrap_or(350.0);
        let primer_gallons = (wall_sqft / primer_coverage).ceil();
        list.add_item(MaterialLineItem::new(primer, primer_gallons));

        list
    }

    /// Calculate paint for ceiling
    pub fn calculate_ceiling_paint(ceiling_sqft: f64, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new("Ceiling Paint");

        let paint = materials::paint::interior_ceiling_paint();
        let coverage = paint.coverage.unwrap_or(400.0);

        // Usually one coat for ceiling
        let gallons = (ceiling_sqft / coverage).ceil();

        let mut item = MaterialLineItem::new(paint, gallons);
        if config.include_waste {
            item = item.with_waste(config.paint_waste_factor);
        }
        list.add_item(item);

        list
    }

    /// Calculate trim paint
    pub fn calculate_trim_paint(linear_feet: f64, _config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new("Trim Paint");

        let paint = materials::paint::trim_paint();

        // Trim is typically 4" tall, so about 0.33 sqft per linear foot
        let trim_sqft = linear_feet * 0.33;
        let coverage = paint.coverage.unwrap_or(400.0);

        // Two coats for trim
        let gallons = (trim_sqft * 2.0 / coverage).ceil().max(1.0);

        list.add_item(MaterialLineItem::new(paint, gallons));

        list
    }

    /// Calculate all paint for a room
    pub fn calculate_room(room: &Room, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new(format!("{} - Paint", room.name));

        // Skip outdoor and garage
        if room.room_type.is_outdoor() || matches!(room.room_type, RoomType::Garage) {
            return list;
        }

        let wall_list = Self::calculate_wall_paint(room.wall_area().value(), config);
        list.merge(wall_list);

        let ceiling_list = Self::calculate_ceiling_paint(room.ceiling_area().value(), config);
        list.merge(ceiling_list);

        // Trim paint based on perimeter
        let trim_list = Self::calculate_trim_paint(room.perimeter().value(), config);
        list.merge(trim_list);

        list
    }

    /// Calculate paint for entire floor plan
    pub fn calculate_floor_plan(
        floor_plan: &FloorPlan,
        config: &CalculationConfig,
    ) -> CalculationResult {
        let mut combined_list = MaterialList::new(format!("{} - Paint", floor_plan.name));

        for room in &floor_plan.rooms {
            let room_list = Self::calculate_room(room, config);
            combined_list.merge(room_list);
        }

        let sqft = floor_plan.total_living_area().value();
        CalculationResult::new(
            format!("{} - Paint", floor_plan.name),
            combined_list,
            config,
        )
        .with_sqft(sqft)
    }
}

/// Calculator for electrical rough-in
pub struct ElectricalCalculator;

impl ElectricalCalculator {
    /// Estimate outlets needed per room (based on code minimums + typical usage)
    pub fn outlets_for_room(room: &Room) -> u32 {
        let _sqft = room.floor_area().value();
        let perimeter = room.perimeter().value();

        // NEC requires outlet within 6' of any point along wall
        // So roughly one outlet per 12' of wall
        let code_minimum = (perimeter / 12.0).ceil() as u32;

        // Add extra for specific rooms
        let extras = match room.room_type {
            RoomType::Kitchen => 8, // Counter outlets, appliances
            RoomType::Office | RoomType::Study => 4,
            RoomType::MasterBath | RoomType::FullBath => 2, // GFCI
            RoomType::Garage | RoomType::Workshop => 6,
            RoomType::Laundry => 3,
            _ => 0,
        };

        code_minimum + extras
    }

    /// Estimate switches for a room
    pub fn switches_for_room(room: &Room) -> (u32, u32) {
        // Returns (single pole, 3-way)
        match room.room_type {
            RoomType::MasterSuite | RoomType::MasterBath => (2, 2),
            RoomType::Bedroom | RoomType::GuestRoom => (1, 1),
            RoomType::LivingRoom | RoomType::FamilyRoom | RoomType::GreatRoom => (2, 2),
            RoomType::Kitchen | RoomType::DiningRoom => (2, 1),
            RoomType::Hallway | RoomType::Foyer => (0, 2), // Typically 3-way
            RoomType::Garage => (2, 1),
            _ => (1, 0),
        }
    }

    /// Calculate recessed lights for a room
    pub fn recessed_lights_for_room(room: &Room) -> u32 {
        let sqft = room.floor_area().value();

        // General rule: one recessed light per 25 sqft for good coverage
        // Adjust based on room type
        let lights_per_sqft = match room.room_type {
            RoomType::Kitchen => 20.0, // More lights in kitchen
            RoomType::MasterBath | RoomType::FullBath => 20.0,
            RoomType::Office | RoomType::Study => 25.0,
            RoomType::Closet | RoomType::WalkInCloset => 40.0,
            RoomType::Garage | RoomType::Workshop => 50.0,
            _ => 30.0,
        };

        (sqft / lights_per_sqft).ceil() as u32
    }

    /// Calculate wire footage (rough estimate)
    pub fn wire_footage_for_room(room: &Room, _config: &CalculationConfig) -> (f64, f64) {
        // Returns (14/2 footage, 12/2 footage)
        let _sqft = room.floor_area().value();
        let outlets = Self::outlets_for_room(room);
        let lights = Self::recessed_lights_for_room(room);

        // Rough estimate:
        // - 20' of wire per outlet (home run + some in-room)
        // - 15' of wire per light
        // - 15' for switches

        let wire_14_2 = lights as f64 * 15.0; // Lights typically on 15A
        let mut wire_12_2 = outlets as f64 * 20.0; // Outlets on 20A

        // Kitchen and bathroom need dedicated 20A circuits
        if matches!(room.room_type, RoomType::Kitchen) {
            wire_12_2 += 100.0; // Extra circuits for appliances
        }

        (wire_14_2, wire_12_2)
    }

    /// Calculate electrical materials for a room
    pub fn calculate_room(room: &Room, config: &CalculationConfig) -> MaterialList {
        let mut list = MaterialList::new(format!("{} - Electrical", room.name));

        if room.room_type.is_outdoor() {
            return list;
        }

        // Outlets
        let outlet_count = Self::outlets_for_room(room);
        let gfci_rooms = matches!(
            room.room_type,
            RoomType::Kitchen
                | RoomType::MasterBath
                | RoomType::FullBath
                | RoomType::HalfBath
                | RoomType::PowderRoom
                | RoomType::Laundry
                | RoomType::Garage
        );

        if gfci_rooms {
            // Some GFCI, some regular
            let gfci_count = (outlet_count / 3).max(1);
            let regular_count = outlet_count - gfci_count;

            list.add_item(
                MaterialLineItem::new(materials::electrical::outlet_gfci(), gfci_count as f64)
                    .with_location(room.name.clone()),
            );
            if regular_count > 0 {
                list.add_item(
                    MaterialLineItem::new(
                        materials::electrical::outlet_standard(),
                        regular_count as f64,
                    )
                    .with_location(room.name.clone()),
                );
            }
        } else {
            list.add_item(
                MaterialLineItem::new(
                    materials::electrical::outlet_standard(),
                    outlet_count as f64,
                )
                .with_location(room.name.clone()),
            );
        }

        // Switches
        let (single_switches, three_way_switches) = Self::switches_for_room(room);
        if single_switches > 0 {
            list.add_item(MaterialLineItem::new(
                materials::electrical::switch_single(),
                single_switches as f64,
            ));
        }
        if three_way_switches > 0 {
            list.add_item(MaterialLineItem::new(
                materials::electrical::switch_3way(),
                three_way_switches as f64,
            ));
        }

        // Recessed lights
        let lights = Self::recessed_lights_for_room(room);
        if lights > 0 {
            list.add_item(
                MaterialLineItem::new(materials::electrical::recessed_light(), lights as f64)
                    .with_location(room.name.clone()),
            );
        }

        // Electrical boxes (one per device)
        let total_devices = outlet_count + single_switches + three_way_switches + lights;
        list.add_item(MaterialLineItem::new(
            materials::electrical::electrical_box(),
            total_devices as f64,
        ));

        // Wire
        let (wire_14, wire_12) = Self::wire_footage_for_room(room, config);
        if wire_14 > 0.0 {
            list.add_item(MaterialLineItem::new(
                materials::electrical::romex_14_2(),
                wire_14,
            ));
        }
        if wire_12 > 0.0 {
            list.add_item(MaterialLineItem::new(
                materials::electrical::romex_12_2(),
                wire_12,
            ));
        }

        list
    }

    /// Calculate electrical for entire floor plan
    pub fn calculate_floor_plan(
        floor_plan: &FloorPlan,
        config: &CalculationConfig,
    ) -> CalculationResult {
        let mut combined_list = MaterialList::new(format!("{} - Electrical", floor_plan.name));

        for room in &floor_plan.rooms {
            let room_list = Self::calculate_room(room, config);
            combined_list.merge(room_list);
        }

        // Add main panel
        combined_list.add_item(MaterialLineItem::new(
            materials::electrical::panel_200a(),
            1.0,
        ));

        // Estimate breakers based on circuits
        let total_circuits = floor_plan.rooms.len() as f64 * 2.5; // Rough estimate
        combined_list.add_item(MaterialLineItem::new(
            materials::electrical::breaker_15a(),
            (total_circuits * 0.4).ceil(),
        ));
        combined_list.add_item(MaterialLineItem::new(
            materials::electrical::breaker_20a(),
            (total_circuits * 0.6).ceil(),
        ));

        let sqft = floor_plan.total_living_area().value();
        CalculationResult::new(
            format!("{} - Electrical", floor_plan.name),
            combined_list,
            config,
        )
        .with_sqft(sqft)
    }
}

/// Complete project calculator that combines all calculators
pub struct ProjectCalculator;

impl ProjectCalculator {
    /// Calculate all materials for a floor plan
    pub fn calculate_floor_plan(
        floor_plan: &FloorPlan,
        config: &CalculationConfig,
    ) -> Vec<CalculationResult> {
        vec![
            WallFramingCalculator::calculate_floor_plan(floor_plan, config),
            DrywallCalculator::calculate_floor_plan(floor_plan, config),
            FlooringCalculator::calculate_floor_plan(floor_plan, config),
            TrimCalculator::calculate_floor_plan(floor_plan, config),
            PaintCalculator::calculate_floor_plan(floor_plan, config),
            ElectricalCalculator::calculate_floor_plan(floor_plan, config),
        ]
    }

    /// Calculate all materials for a complete project
    pub fn calculate_project(
        project: &Project,
        config: &CalculationConfig,
    ) -> Vec<CalculationResult> {
        let mut results = Vec::new();

        for floor_plan in &project.floor_plans {
            results.extend(Self::calculate_floor_plan(floor_plan, config));
        }

        results
    }

    /// Get total cost for a project
    pub fn total_project_cost(project: &Project, config: &CalculationConfig) -> f64 {
        Self::calculate_project(project, config)
            .iter()
            .map(|r| r.total_cost)
            .sum()
    }

    /// Get cost breakdown by category
    pub fn cost_breakdown_by_category(
        results: &[CalculationResult],
    ) -> std::collections::HashMap<String, f64> {
        let mut breakdown = std::collections::HashMap::new();

        for result in results {
            *breakdown.entry(result.description.clone()).or_insert(0.0) += result.total_cost;
        }

        breakdown
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_stud_calculation() {
        let wall_length = LinearFeet::new(10.0); // 10' wall
        let studs = WallFramingCalculator::studs_needed(wall_length, 16);

        // 10' = 120", 120/16 = 7.5, ceil = 8, +1 for end = 9, +2 for corners = 11
        assert_eq!(studs, 11);
    }

    #[test]
    fn test_plate_calculation() {
        let wall_length = LinearFeet::new(10.0);
        let plate = WallFramingCalculator::plate_length(wall_length);

        // 3x wall length (bottom + double top)
        assert!((plate.value() - 30.0).abs() < 0.01);
    }

    #[test]
    fn test_drywall_sheets() {
        let sqft = 500.0;
        let sheets = DrywallCalculator::sheets_needed(sqft, 32.0);

        // 500/32 = 15.625, ceil = 16
        assert!((sheets - 16.0).abs() < 0.01);
    }

    #[test]
    fn test_room_calculation() {
        let room = Room::new(
            "Living Room",
            RoomType::LivingRoom,
            FeetInches::new(20, 0),
            FeetInches::new(15, 0),
        );

        let config = CalculationConfig::default();

        // Test flooring
        let flooring = FlooringCalculator::calculate_room(&room, &config);
        assert!(!flooring.items.is_empty());

        // Test paint
        let paint = PaintCalculator::calculate_room(&room, &config);
        assert!(!paint.items.is_empty());

        // Test electrical
        let electrical = ElectricalCalculator::calculate_room(&room, &config);
        assert!(!electrical.items.is_empty());
    }

    #[test]
    fn test_outlets_calculation() {
        let kitchen = Room::new(
            "Kitchen",
            RoomType::Kitchen,
            FeetInches::new(15, 0),
            FeetInches::new(12, 0),
        );

        let outlets = ElectricalCalculator::outlets_for_room(&kitchen);

        // Kitchen should have extra outlets
        assert!(outlets >= 10);
    }
}
