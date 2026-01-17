//! # Materials Module
//!
//! Defines construction materials, their properties, and pricing.
//! Used for material takeoffs and cost estimation.

use serde::{Deserialize, Serialize};

/// Categories of construction materials
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum MaterialCategory {
    /// Structural lumber (studs, joists, beams)
    Lumber,
    /// Sheet goods (plywood, OSB, drywall)
    SheetGoods,
    /// Flooring materials
    Flooring,
    /// Roofing materials
    Roofing,
    /// Insulation
    Insulation,
    /// Electrical
    Electrical,
    /// Plumbing
    Plumbing,
    /// HVAC
    Hvac,
    /// Doors
    Doors,
    /// Windows
    Windows,
    /// Trim and millwork
    Trim,
    /// Paint and finishes
    Paint,
    /// Hardware
    Hardware,
    /// Concrete and masonry
    Concrete,
    /// Fasteners
    Fasteners,
    /// Exterior siding
    Siding,
    /// Cabinetry
    Cabinetry,
    /// Countertops
    Countertops,
    /// Appliances
    Appliances,
}

impl MaterialCategory {
    pub fn display_name(&self) -> &str {
        match self {
            MaterialCategory::Lumber => "Lumber",
            MaterialCategory::SheetGoods => "Sheet Goods",
            MaterialCategory::Flooring => "Flooring",
            MaterialCategory::Roofing => "Roofing",
            MaterialCategory::Insulation => "Insulation",
            MaterialCategory::Electrical => "Electrical",
            MaterialCategory::Plumbing => "Plumbing",
            MaterialCategory::Hvac => "HVAC",
            MaterialCategory::Doors => "Doors",
            MaterialCategory::Windows => "Windows",
            MaterialCategory::Trim => "Trim & Millwork",
            MaterialCategory::Paint => "Paint & Finishes",
            MaterialCategory::Hardware => "Hardware",
            MaterialCategory::Concrete => "Concrete & Masonry",
            MaterialCategory::Fasteners => "Fasteners",
            MaterialCategory::Siding => "Exterior Siding",
            MaterialCategory::Cabinetry => "Cabinetry",
            MaterialCategory::Countertops => "Countertops",
            MaterialCategory::Appliances => "Appliances",
        }
    }
}

/// Unit of measurement for materials
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum MaterialUnit {
    /// Each/piece
    Each,
    /// Linear feet
    LinearFoot,
    /// Square feet
    SquareFoot,
    /// Board feet (lumber volume)
    BoardFoot,
    /// Cubic yards (concrete)
    CubicYard,
    /// Bundle (shingles, etc.)
    Bundle,
    /// Roll (insulation, roofing paper)
    Roll,
    /// Gallon (paint, stain)
    Gallon,
    /// Bag (concrete mix, mortar)
    Bag,
    /// Box (fasteners, etc.)
    Box,
    /// Sheet (plywood, drywall)
    Sheet,
    /// Pair (hinges, etc.)
    Pair,
}

impl MaterialUnit {
    pub fn abbreviation(&self) -> &str {
        match self {
            MaterialUnit::Each => "ea",
            MaterialUnit::LinearFoot => "LF",
            MaterialUnit::SquareFoot => "SF",
            MaterialUnit::BoardFoot => "BF",
            MaterialUnit::CubicYard => "CY",
            MaterialUnit::Bundle => "bdl",
            MaterialUnit::Roll => "roll",
            MaterialUnit::Gallon => "gal",
            MaterialUnit::Bag => "bag",
            MaterialUnit::Box => "box",
            MaterialUnit::Sheet => "sht",
            MaterialUnit::Pair => "pr",
        }
    }
}

/// A specific material with pricing
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Material {
    pub id: String,
    pub name: String,
    pub category: MaterialCategory,
    pub unit: MaterialUnit,
    /// Base price per unit (economy tier)
    pub price_economy: f64,
    /// Base price per unit (standard tier)
    pub price_standard: f64,
    /// Base price per unit (premium tier)
    pub price_premium: f64,
    /// Base price per unit (luxury tier)
    pub price_luxury: f64,
    /// Description or notes
    pub description: Option<String>,
    /// Typical coverage (e.g., 1 gallon covers 400 SF)
    pub coverage: Option<f64>,
    /// Coverage unit (what the coverage value refers to)
    pub coverage_unit: Option<MaterialUnit>,
}

impl Material {
    pub fn new(
        id: impl Into<String>,
        name: impl Into<String>,
        category: MaterialCategory,
        unit: MaterialUnit,
        price: f64,
    ) -> Self {
        Self {
            id: id.into(),
            name: name.into(),
            category,
            unit,
            price_economy: price * 0.75,
            price_standard: price,
            price_premium: price * 1.5,
            price_luxury: price * 2.5,
            description: None,
            coverage: None,
            coverage_unit: None,
        }
    }

    /// Set tiered pricing
    pub fn with_tiered_pricing(
        mut self,
        economy: f64,
        standard: f64,
        premium: f64,
        luxury: f64,
    ) -> Self {
        self.price_economy = economy;
        self.price_standard = standard;
        self.price_premium = premium;
        self.price_luxury = luxury;
        self
    }

    /// Set coverage information
    pub fn with_coverage(mut self, coverage: f64, unit: MaterialUnit) -> Self {
        self.coverage = Some(coverage);
        self.coverage_unit = Some(unit);
        self
    }

    /// Set description
    pub fn with_description(mut self, description: impl Into<String>) -> Self {
        self.description = Some(description.into());
        self
    }

    /// Get price for a quality tier
    pub fn price_for_tier(&self, tier: &crate::models::QualityTier) -> f64 {
        match tier {
            crate::models::QualityTier::Economy => self.price_economy,
            crate::models::QualityTier::Standard => self.price_standard,
            crate::models::QualityTier::Premium => self.price_premium,
            crate::models::QualityTier::Luxury => self.price_luxury,
        }
    }
}

/// A line item in a material list
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MaterialLineItem {
    pub material: Material,
    pub quantity: f64,
    /// Waste factor (e.g., 1.1 = 10% waste)
    pub waste_factor: f64,
    /// Room or area this material is for
    pub location: Option<String>,
    /// Notes about this line item
    pub notes: Option<String>,
}

impl MaterialLineItem {
    pub fn new(material: Material, quantity: f64) -> Self {
        Self {
            material,
            quantity,
            waste_factor: 1.0,
            location: None,
            notes: None,
        }
    }

    /// Set waste factor
    pub fn with_waste(mut self, factor: f64) -> Self {
        self.waste_factor = factor;
        self
    }

    /// Set location
    pub fn with_location(mut self, location: impl Into<String>) -> Self {
        self.location = Some(location.into());
        self
    }

    /// Get quantity with waste factor
    pub fn quantity_with_waste(&self) -> f64 {
        self.quantity * self.waste_factor
    }

    /// Get total cost for a quality tier
    pub fn total_cost(&self, tier: &crate::models::QualityTier) -> f64 {
        self.quantity_with_waste() * self.material.price_for_tier(tier)
    }
}

/// A complete material list for a project or room
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MaterialList {
    pub name: String,
    pub items: Vec<MaterialLineItem>,
}

impl MaterialList {
    pub fn new(name: impl Into<String>) -> Self {
        Self {
            name: name.into(),
            items: Vec::new(),
        }
    }

    /// Add an item to the list
    pub fn add_item(&mut self, item: MaterialLineItem) {
        self.items.push(item);
    }

    /// Add a material with quantity
    pub fn add(&mut self, material: Material, quantity: f64) {
        self.items.push(MaterialLineItem::new(material, quantity));
    }

    /// Get items by category
    pub fn items_by_category(&self, category: MaterialCategory) -> Vec<&MaterialLineItem> {
        self.items
            .iter()
            .filter(|i| i.material.category == category)
            .collect()
    }

    /// Get total cost for a quality tier
    pub fn total_cost(&self, tier: &crate::models::QualityTier) -> f64 {
        self.items.iter().map(|i| i.total_cost(tier)).sum()
    }

    /// Get total cost by category
    pub fn cost_by_category(
        &self,
        category: MaterialCategory,
        tier: &crate::models::QualityTier,
    ) -> f64 {
        self.items
            .iter()
            .filter(|i| i.material.category == category)
            .map(|i| i.total_cost(tier))
            .sum()
    }

    /// Merge another material list into this one
    pub fn merge(&mut self, other: MaterialList) {
        self.items.extend(other.items);
    }
}

// ============================================================================
// Standard Material Definitions
// ============================================================================

/// Standard lumber materials
pub mod lumber {
    use super::*;

    pub fn stud_2x4_8ft() -> Material {
        Material::new(
            "LUM-2x4-8",
            "2x4x8' Stud",
            MaterialCategory::Lumber,
            MaterialUnit::Each,
            4.50,
        )
        .with_tiered_pricing(3.50, 4.50, 6.00, 8.00)
        .with_description("Kiln-dried SPF stud grade")
    }

    pub fn stud_2x4_10ft() -> Material {
        Material::new(
            "LUM-2x4-10",
            "2x4x10' Stud",
            MaterialCategory::Lumber,
            MaterialUnit::Each,
            5.75,
        )
        .with_tiered_pricing(4.50, 5.75, 7.50, 10.00)
    }

    pub fn stud_2x6_8ft() -> Material {
        Material::new(
            "LUM-2x6-8",
            "2x6x8' Stud",
            MaterialCategory::Lumber,
            MaterialUnit::Each,
            7.50,
        )
        .with_tiered_pricing(6.00, 7.50, 10.00, 14.00)
        .with_description("Kiln-dried SPF stud grade")
    }

    pub fn stud_2x6_10ft() -> Material {
        Material::new(
            "LUM-2x6-10",
            "2x6x10' Stud",
            MaterialCategory::Lumber,
            MaterialUnit::Each,
            9.25,
        )
        .with_tiered_pricing(7.50, 9.25, 12.00, 16.00)
    }

    pub fn plate_2x4() -> Material {
        Material::new(
            "LUM-2x4-PLT",
            "2x4 Plate Stock",
            MaterialCategory::Lumber,
            MaterialUnit::LinearFoot,
            0.60,
        )
        .with_tiered_pricing(0.45, 0.60, 0.80, 1.10)
    }

    pub fn plate_2x6() -> Material {
        Material::new(
            "LUM-2x6-PLT",
            "2x6 Plate Stock",
            MaterialCategory::Lumber,
            MaterialUnit::LinearFoot,
            0.95,
        )
        .with_tiered_pricing(0.75, 0.95, 1.25, 1.75)
    }

    pub fn header_2x10() -> Material {
        Material::new(
            "LUM-2x10-HDR",
            "2x10 Header Stock",
            MaterialCategory::Lumber,
            MaterialUnit::LinearFoot,
            1.85,
        )
        .with_tiered_pricing(1.50, 1.85, 2.50, 3.50)
    }

    pub fn header_2x12() -> Material {
        Material::new(
            "LUM-2x12-HDR",
            "2x12 Header Stock",
            MaterialCategory::Lumber,
            MaterialUnit::LinearFoot,
            2.25,
        )
        .with_tiered_pricing(1.85, 2.25, 3.00, 4.25)
    }

    pub fn lvl_beam() -> Material {
        Material::new(
            "LUM-LVL",
            "LVL Beam",
            MaterialCategory::Lumber,
            MaterialUnit::LinearFoot,
            4.50,
        )
        .with_tiered_pricing(3.75, 4.50, 5.50, 7.00)
        .with_description("Laminated Veneer Lumber")
    }
}

/// Sheet goods (plywood, OSB, drywall)
pub mod sheet_goods {
    use super::*;

    pub fn osb_7_16() -> Material {
        Material::new(
            "SHT-OSB-7/16",
            "7/16\" OSB Sheathing",
            MaterialCategory::SheetGoods,
            MaterialUnit::Sheet,
            14.00,
        )
        .with_tiered_pricing(12.00, 14.00, 18.00, 24.00)
        .with_description("4x8 sheet, wall sheathing")
        .with_coverage(32.0, MaterialUnit::SquareFoot)
    }

    pub fn plywood_1_2_cdx() -> Material {
        Material::new(
            "SHT-PLY-1/2",
            "1/2\" CDX Plywood",
            MaterialCategory::SheetGoods,
            MaterialUnit::Sheet,
            28.00,
        )
        .with_tiered_pricing(24.00, 28.00, 35.00, 45.00)
        .with_coverage(32.0, MaterialUnit::SquareFoot)
    }

    pub fn plywood_3_4_cdx() -> Material {
        Material::new(
            "SHT-PLY-3/4",
            "3/4\" CDX Plywood",
            MaterialCategory::SheetGoods,
            MaterialUnit::Sheet,
            42.00,
        )
        .with_tiered_pricing(36.00, 42.00, 52.00, 65.00)
        .with_description("Subfloor grade")
        .with_coverage(32.0, MaterialUnit::SquareFoot)
    }

    pub fn drywall_1_2() -> Material {
        Material::new(
            "SHT-DW-1/2",
            "1/2\" Drywall",
            MaterialCategory::SheetGoods,
            MaterialUnit::Sheet,
            12.00,
        )
        .with_tiered_pricing(10.00, 12.00, 15.00, 20.00)
        .with_description("4x8 standard drywall")
        .with_coverage(32.0, MaterialUnit::SquareFoot)
    }

    pub fn drywall_5_8() -> Material {
        Material::new(
            "SHT-DW-5/8",
            "5/8\" Drywall",
            MaterialCategory::SheetGoods,
            MaterialUnit::Sheet,
            14.00,
        )
        .with_tiered_pricing(12.00, 14.00, 18.00, 24.00)
        .with_description("4x8 fire-rated drywall")
        .with_coverage(32.0, MaterialUnit::SquareFoot)
    }

    pub fn cement_board() -> Material {
        Material::new(
            "SHT-CB",
            "1/2\" Cement Board",
            MaterialCategory::SheetGoods,
            MaterialUnit::Sheet,
            18.00,
        )
        .with_tiered_pricing(15.00, 18.00, 22.00, 28.00)
        .with_description("3x5 backer board for tile")
        .with_coverage(15.0, MaterialUnit::SquareFoot)
    }
}

/// Insulation materials
pub mod insulation {
    use super::*;

    pub fn batt_r13() -> Material {
        Material::new(
            "INS-R13",
            "R-13 Fiberglass Batt",
            MaterialCategory::Insulation,
            MaterialUnit::SquareFoot,
            0.50,
        )
        .with_tiered_pricing(0.40, 0.50, 0.75, 1.00)
        .with_description("3.5\" thick for 2x4 walls")
    }

    pub fn batt_r19() -> Material {
        Material::new(
            "INS-R19",
            "R-19 Fiberglass Batt",
            MaterialCategory::Insulation,
            MaterialUnit::SquareFoot,
            0.65,
        )
        .with_tiered_pricing(0.55, 0.65, 0.90, 1.25)
        .with_description("6.25\" thick for 2x6 walls")
    }

    pub fn batt_r38() -> Material {
        Material::new(
            "INS-R38",
            "R-38 Fiberglass Batt",
            MaterialCategory::Insulation,
            MaterialUnit::SquareFoot,
            1.10,
        )
        .with_tiered_pricing(0.90, 1.10, 1.50, 2.00)
        .with_description("12\" thick for attic")
    }

    pub fn spray_foam_closed() -> Material {
        Material::new(
            "INS-SPF-CC",
            "Closed Cell Spray Foam",
            MaterialCategory::Insulation,
            MaterialUnit::SquareFoot,
            2.50,
        )
        .with_tiered_pricing(2.00, 2.50, 3.25, 4.50)
        .with_description("Per inch of thickness")
    }

    pub fn rigid_foam_1in() -> Material {
        Material::new(
            "INS-RIGID-1",
            "1\" Rigid Foam Board",
            MaterialCategory::Insulation,
            MaterialUnit::Sheet,
            22.00,
        )
        .with_tiered_pricing(18.00, 22.00, 28.00, 36.00)
        .with_description("4x8 XPS or EPS board")
        .with_coverage(32.0, MaterialUnit::SquareFoot)
    }
}

/// Flooring materials
pub mod flooring {
    use super::*;

    pub fn hardwood_oak() -> Material {
        Material::new(
            "FLR-OAK",
            "Oak Hardwood Flooring",
            MaterialCategory::Flooring,
            MaterialUnit::SquareFoot,
            6.00,
        )
        .with_tiered_pricing(4.00, 6.00, 9.00, 15.00)
        .with_description("3/4\" solid oak, unfinished")
    }

    pub fn engineered_hardwood() -> Material {
        Material::new(
            "FLR-ENG",
            "Engineered Hardwood",
            MaterialCategory::Flooring,
            MaterialUnit::SquareFoot,
            5.00,
        )
        .with_tiered_pricing(3.50, 5.00, 8.00, 12.00)
    }

    pub fn lvp() -> Material {
        Material::new(
            "FLR-LVP",
            "Luxury Vinyl Plank",
            MaterialCategory::Flooring,
            MaterialUnit::SquareFoot,
            3.50,
        )
        .with_tiered_pricing(2.00, 3.50, 5.50, 8.00)
    }

    pub fn tile_ceramic() -> Material {
        Material::new(
            "FLR-TILE-CER",
            "Ceramic Tile",
            MaterialCategory::Flooring,
            MaterialUnit::SquareFoot,
            2.50,
        )
        .with_tiered_pricing(1.50, 2.50, 5.00, 12.00)
    }

    pub fn tile_porcelain() -> Material {
        Material::new(
            "FLR-TILE-POR",
            "Porcelain Tile",
            MaterialCategory::Flooring,
            MaterialUnit::SquareFoot,
            4.00,
        )
        .with_tiered_pricing(2.50, 4.00, 8.00, 18.00)
    }

    pub fn carpet() -> Material {
        Material::new(
            "FLR-CARPET",
            "Carpet with Pad",
            MaterialCategory::Flooring,
            MaterialUnit::SquareFoot,
            4.00,
        )
        .with_tiered_pricing(2.50, 4.00, 7.00, 12.00)
    }

    pub fn underlayment() -> Material {
        Material::new(
            "FLR-UNDER",
            "Flooring Underlayment",
            MaterialCategory::Flooring,
            MaterialUnit::SquareFoot,
            0.50,
        )
        .with_tiered_pricing(0.30, 0.50, 0.80, 1.25)
    }
}

/// Trim and millwork
pub mod trim {
    use super::*;

    pub fn baseboard_mdf() -> Material {
        Material::new(
            "TRM-BASE-MDF",
            "MDF Baseboard 3.25\"",
            MaterialCategory::Trim,
            MaterialUnit::LinearFoot,
            1.00,
        )
        .with_tiered_pricing(0.75, 1.00, 1.50, 2.50)
    }

    pub fn baseboard_wood() -> Material {
        Material::new(
            "TRM-BASE-WOOD",
            "Wood Baseboard 3.25\"",
            MaterialCategory::Trim,
            MaterialUnit::LinearFoot,
            2.00,
        )
        .with_tiered_pricing(1.50, 2.00, 3.50, 6.00)
    }

    pub fn crown_moulding() -> Material {
        Material::new(
            "TRM-CROWN",
            "Crown Moulding 4.5\"",
            MaterialCategory::Trim,
            MaterialUnit::LinearFoot,
            2.50,
        )
        .with_tiered_pricing(1.75, 2.50, 4.50, 8.00)
    }

    pub fn door_casing() -> Material {
        Material::new(
            "TRM-CASE",
            "Door Casing Set",
            MaterialCategory::Trim,
            MaterialUnit::Each,
            25.00,
        )
        .with_tiered_pricing(18.00, 25.00, 45.00, 80.00)
        .with_description("Both sides of door opening")
    }

    pub fn window_casing() -> Material {
        Material::new(
            "TRM-WIN",
            "Window Casing Set",
            MaterialCategory::Trim,
            MaterialUnit::Each,
            30.00,
        )
        .with_tiered_pricing(22.00, 30.00, 55.00, 95.00)
    }

    pub fn chair_rail() -> Material {
        Material::new(
            "TRM-CHAIR",
            "Chair Rail",
            MaterialCategory::Trim,
            MaterialUnit::LinearFoot,
            1.75,
        )
        .with_tiered_pricing(1.25, 1.75, 3.00, 5.50)
    }
}

/// Paint and finishes
pub mod paint {
    use super::*;

    pub fn interior_wall_paint() -> Material {
        Material::new(
            "PNT-INT-WALL",
            "Interior Wall Paint",
            MaterialCategory::Paint,
            MaterialUnit::Gallon,
            35.00,
        )
        .with_tiered_pricing(25.00, 35.00, 55.00, 85.00)
        .with_description("Eggshell/satin finish")
        .with_coverage(400.0, MaterialUnit::SquareFoot)
    }

    pub fn interior_ceiling_paint() -> Material {
        Material::new(
            "PNT-INT-CEIL",
            "Interior Ceiling Paint",
            MaterialCategory::Paint,
            MaterialUnit::Gallon,
            30.00,
        )
        .with_tiered_pricing(22.00, 30.00, 45.00, 70.00)
        .with_description("Flat white")
        .with_coverage(400.0, MaterialUnit::SquareFoot)
    }

    pub fn primer() -> Material {
        Material::new(
            "PNT-PRIMER",
            "Primer",
            MaterialCategory::Paint,
            MaterialUnit::Gallon,
            28.00,
        )
        .with_tiered_pricing(20.00, 28.00, 40.00, 55.00)
        .with_coverage(350.0, MaterialUnit::SquareFoot)
    }

    pub fn exterior_paint() -> Material {
        Material::new(
            "PNT-EXT",
            "Exterior Paint",
            MaterialCategory::Paint,
            MaterialUnit::Gallon,
            45.00,
        )
        .with_tiered_pricing(32.00, 45.00, 65.00, 95.00)
        .with_coverage(350.0, MaterialUnit::SquareFoot)
    }

    pub fn trim_paint() -> Material {
        Material::new(
            "PNT-TRIM",
            "Trim Paint (Semi-Gloss)",
            MaterialCategory::Paint,
            MaterialUnit::Gallon,
            40.00,
        )
        .with_tiered_pricing(28.00, 40.00, 60.00, 90.00)
        .with_coverage(400.0, MaterialUnit::SquareFoot)
    }

    pub fn stain() -> Material {
        Material::new(
            "PNT-STAIN",
            "Wood Stain",
            MaterialCategory::Paint,
            MaterialUnit::Gallon,
            35.00,
        )
        .with_tiered_pricing(25.00, 35.00, 50.00, 75.00)
        .with_coverage(300.0, MaterialUnit::SquareFoot)
    }
}

/// Door materials
pub mod doors {
    use super::*;

    pub fn interior_hollow_core() -> Material {
        Material::new(
            "DR-INT-HC",
            "Interior Hollow Core Door",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            65.00,
        )
        .with_tiered_pricing(45.00, 65.00, 120.00, 200.00)
        .with_description("6-panel, primed")
    }

    pub fn interior_solid_core() -> Material {
        Material::new(
            "DR-INT-SC",
            "Interior Solid Core Door",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            150.00,
        )
        .with_tiered_pricing(100.00, 150.00, 250.00, 450.00)
    }

    pub fn exterior_steel() -> Material {
        Material::new(
            "DR-EXT-STL",
            "Exterior Steel Entry Door",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            350.00,
        )
        .with_tiered_pricing(250.00, 350.00, 600.00, 1200.00)
    }

    pub fn exterior_fiberglass() -> Material {
        Material::new(
            "DR-EXT-FG",
            "Exterior Fiberglass Door",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            450.00,
        )
        .with_tiered_pricing(300.00, 450.00, 800.00, 1800.00)
    }

    pub fn sliding_glass() -> Material {
        Material::new(
            "DR-SLIDE",
            "Sliding Glass Door 6'",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            650.00,
        )
        .with_tiered_pricing(450.00, 650.00, 1200.00, 2500.00)
    }

    pub fn french_doors() -> Material {
        Material::new(
            "DR-FRENCH",
            "French Doors (Pair)",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            800.00,
        )
        .with_tiered_pricing(550.00, 800.00, 1500.00, 3500.00)
    }

    pub fn bifold() -> Material {
        Material::new(
            "DR-BIFOLD",
            "Bi-Fold Closet Door",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            85.00,
        )
        .with_tiered_pricing(55.00, 85.00, 150.00, 280.00)
    }

    pub fn garage_door() -> Material {
        Material::new(
            "DR-GARAGE",
            "Garage Door 16x7",
            MaterialCategory::Doors,
            MaterialUnit::Each,
            1200.00,
        )
        .with_tiered_pricing(800.00, 1200.00, 2200.00, 4500.00)
    }
}

/// Window materials
pub mod windows {
    use super::*;

    pub fn double_hung_vinyl() -> Material {
        Material::new(
            "WIN-DH-VIN",
            "Double Hung Vinyl Window",
            MaterialCategory::Windows,
            MaterialUnit::Each,
            275.00,
        )
        .with_tiered_pricing(180.00, 275.00, 450.00, 800.00)
        .with_description("Standard 3'x4' size")
    }

    pub fn double_hung_wood() -> Material {
        Material::new(
            "WIN-DH-WOOD",
            "Double Hung Wood Window",
            MaterialCategory::Windows,
            MaterialUnit::Each,
            450.00,
        )
        .with_tiered_pricing(300.00, 450.00, 750.00, 1400.00)
    }

    pub fn casement() -> Material {
        Material::new(
            "WIN-CASE",
            "Casement Window",
            MaterialCategory::Windows,
            MaterialUnit::Each,
            350.00,
        )
        .with_tiered_pricing(250.00, 350.00, 550.00, 950.00)
    }

    pub fn picture() -> Material {
        Material::new(
            "WIN-PIC",
            "Picture Window",
            MaterialCategory::Windows,
            MaterialUnit::Each,
            400.00,
        )
        .with_tiered_pricing(280.00, 400.00, 700.00, 1200.00)
    }

    pub fn bay() -> Material {
        Material::new(
            "WIN-BAY",
            "Bay Window",
            MaterialCategory::Windows,
            MaterialUnit::Each,
            1500.00,
        )
        .with_tiered_pricing(1000.00, 1500.00, 2500.00, 5000.00)
    }

    pub fn skylight() -> Material {
        Material::new(
            "WIN-SKY",
            "Skylight",
            MaterialCategory::Windows,
            MaterialUnit::Each,
            600.00,
        )
        .with_tiered_pricing(400.00, 600.00, 1100.00, 2200.00)
    }
}

/// Electrical materials
pub mod electrical {
    use super::*;

    pub fn romex_14_2() -> Material {
        Material::new(
            "ELEC-14-2",
            "14/2 Romex Wire",
            MaterialCategory::Electrical,
            MaterialUnit::LinearFoot,
            0.45,
        )
        .with_tiered_pricing(0.35, 0.45, 0.55, 0.70)
        .with_description("15 amp circuits")
    }

    pub fn romex_12_2() -> Material {
        Material::new(
            "ELEC-12-2",
            "12/2 Romex Wire",
            MaterialCategory::Electrical,
            MaterialUnit::LinearFoot,
            0.65,
        )
        .with_tiered_pricing(0.50, 0.65, 0.80, 1.00)
        .with_description("20 amp circuits")
    }

    pub fn outlet_standard() -> Material {
        Material::new(
            "ELEC-OUT-STD",
            "Standard Outlet",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            3.00,
        )
        .with_tiered_pricing(2.00, 3.00, 8.00, 20.00)
    }

    pub fn outlet_gfci() -> Material {
        Material::new(
            "ELEC-OUT-GFCI",
            "GFCI Outlet",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            18.00,
        )
        .with_tiered_pricing(12.00, 18.00, 30.00, 50.00)
    }

    pub fn switch_single() -> Material {
        Material::new(
            "ELEC-SW-1",
            "Single Pole Switch",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            3.00,
        )
        .with_tiered_pricing(2.00, 3.00, 10.00, 25.00)
    }

    pub fn switch_3way() -> Material {
        Material::new(
            "ELEC-SW-3",
            "3-Way Switch",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            5.00,
        )
        .with_tiered_pricing(3.50, 5.00, 15.00, 35.00)
    }

    pub fn electrical_box() -> Material {
        Material::new(
            "ELEC-BOX",
            "Electrical Box",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            2.00,
        )
        .with_tiered_pricing(1.50, 2.00, 3.50, 6.00)
    }

    pub fn breaker_15a() -> Material {
        Material::new(
            "ELEC-BRK-15",
            "15A Circuit Breaker",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            8.00,
        )
        .with_tiered_pricing(6.00, 8.00, 12.00, 18.00)
    }

    pub fn breaker_20a() -> Material {
        Material::new(
            "ELEC-BRK-20",
            "20A Circuit Breaker",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            10.00,
        )
        .with_tiered_pricing(8.00, 10.00, 15.00, 22.00)
    }

    pub fn panel_200a() -> Material {
        Material::new(
            "ELEC-PNL-200",
            "200A Main Panel",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            350.00,
        )
        .with_tiered_pricing(250.00, 350.00, 500.00, 750.00)
    }

    pub fn recessed_light() -> Material {
        Material::new(
            "ELEC-REC",
            "Recessed Light (Can)",
            MaterialCategory::Electrical,
            MaterialUnit::Each,
            25.00,
        )
        .with_tiered_pricing(15.00, 25.00, 50.00, 100.00)
    }
}

/// Fasteners
pub mod fasteners {
    use super::*;

    pub fn framing_nails() -> Material {
        Material::new(
            "FAST-NAIL-FR",
            "Framing Nails (16d)",
            MaterialCategory::Fasteners,
            MaterialUnit::Box,
            45.00,
        )
        .with_tiered_pricing(35.00, 45.00, 55.00, 70.00)
        .with_description("5 lb box")
    }

    pub fn drywall_screws() -> Material {
        Material::new(
            "FAST-SCR-DW",
            "Drywall Screws 1-5/8\"",
            MaterialCategory::Fasteners,
            MaterialUnit::Box,
            12.00,
        )
        .with_tiered_pricing(9.00, 12.00, 15.00, 20.00)
        .with_description("1 lb box")
    }

    pub fn deck_screws() -> Material {
        Material::new(
            "FAST-SCR-DK",
            "Deck Screws 3\"",
            MaterialCategory::Fasteners,
            MaterialUnit::Box,
            35.00,
        )
        .with_tiered_pricing(28.00, 35.00, 45.00, 60.00)
        .with_description("5 lb box")
    }

    pub fn construction_adhesive() -> Material {
        Material::new(
            "FAST-ADH",
            "Construction Adhesive",
            MaterialCategory::Fasteners,
            MaterialUnit::Each,
            6.00,
        )
        .with_tiered_pricing(4.50, 6.00, 8.00, 12.00)
        .with_description("28 oz tube")
    }

    pub fn simpson_ties() -> Material {
        Material::new(
            "FAST-TIE",
            "Simpson Strong-Tie",
            MaterialCategory::Fasteners,
            MaterialUnit::Each,
            3.50,
        )
        .with_tiered_pricing(2.50, 3.50, 4.50, 6.00)
    }
}

/// Get all standard materials as a vector
pub fn all_standard_materials() -> Vec<Material> {
    vec![
        // Lumber
        lumber::stud_2x4_8ft(),
        lumber::stud_2x4_10ft(),
        lumber::stud_2x6_8ft(),
        lumber::stud_2x6_10ft(),
        lumber::plate_2x4(),
        lumber::plate_2x6(),
        lumber::header_2x10(),
        lumber::header_2x12(),
        lumber::lvl_beam(),
        // Sheet goods
        sheet_goods::osb_7_16(),
        sheet_goods::plywood_1_2_cdx(),
        sheet_goods::plywood_3_4_cdx(),
        sheet_goods::drywall_1_2(),
        sheet_goods::drywall_5_8(),
        sheet_goods::cement_board(),
        // Insulation
        insulation::batt_r13(),
        insulation::batt_r19(),
        insulation::batt_r38(),
        insulation::spray_foam_closed(),
        insulation::rigid_foam_1in(),
        // Flooring
        flooring::hardwood_oak(),
        flooring::engineered_hardwood(),
        flooring::lvp(),
        flooring::tile_ceramic(),
        flooring::tile_porcelain(),
        flooring::carpet(),
        flooring::underlayment(),
        // Trim
        trim::baseboard_mdf(),
        trim::baseboard_wood(),
        trim::crown_moulding(),
        trim::door_casing(),
        trim::window_casing(),
        trim::chair_rail(),
        // Paint
        paint::interior_wall_paint(),
        paint::interior_ceiling_paint(),
        paint::primer(),
        paint::exterior_paint(),
        paint::trim_paint(),
        paint::stain(),
        // Doors
        doors::interior_hollow_core(),
        doors::interior_solid_core(),
        doors::exterior_steel(),
        doors::exterior_fiberglass(),
        doors::sliding_glass(),
        doors::french_doors(),
        doors::bifold(),
        doors::garage_door(),
        // Windows
        windows::double_hung_vinyl(),
        windows::double_hung_wood(),
        windows::casement(),
        windows::picture(),
        windows::bay(),
        windows::skylight(),
        // Electrical
        electrical::romex_14_2(),
        electrical::romex_12_2(),
        electrical::outlet_standard(),
        electrical::outlet_gfci(),
        electrical::switch_single(),
        electrical::switch_3way(),
        electrical::electrical_box(),
        electrical::breaker_15a(),
        electrical::breaker_20a(),
        electrical::panel_200a(),
        electrical::recessed_light(),
        // Fasteners
        fasteners::framing_nails(),
        fasteners::drywall_screws(),
        fasteners::deck_screws(),
        fasteners::construction_adhesive(),
        fasteners::simpson_ties(),
    ]
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::models::QualityTier;

    #[test]
    fn test_material_pricing() {
        let stud = lumber::stud_2x4_8ft();
        assert_eq!(stud.price_for_tier(&QualityTier::Economy), 3.50);
        assert_eq!(stud.price_for_tier(&QualityTier::Standard), 4.50);
        assert_eq!(stud.price_for_tier(&QualityTier::Premium), 6.00);
        assert_eq!(stud.price_for_tier(&QualityTier::Luxury), 8.00);
    }

    #[test]
    fn test_material_line_item() {
        let stud = lumber::stud_2x4_8ft();
        let item = MaterialLineItem::new(stud, 100.0).with_waste(1.1);

        assert!((item.quantity_with_waste() - 110.0).abs() < 0.01);
        assert!((item.total_cost(&QualityTier::Standard) - 495.0).abs() < 0.01);
    }

    #[test]
    fn test_material_list() {
        let mut list = MaterialList::new("Test Room");
        list.add(lumber::stud_2x4_8ft(), 50.0);
        list.add(sheet_goods::drywall_1_2(), 10.0);

        let lumber_cost = list.cost_by_category(MaterialCategory::Lumber, &QualityTier::Standard);
        assert!((lumber_cost - 225.0).abs() < 0.01); // 50 * 4.50

        let sheet_cost =
            list.cost_by_category(MaterialCategory::SheetGoods, &QualityTier::Standard);
        assert!((sheet_cost - 120.0).abs() < 0.01); // 10 * 12.00
    }

    #[test]
    fn test_all_materials_loaded() {
        let materials = all_standard_materials();
        assert!(materials.len() > 50);
    }
}
