//! # Luxury Farmhouse Floor Plan
//!
//! This module defines the floor plan from the provided architectural drawing.
//! It's a large single-story luxury farmhouse with 4 bedrooms, multiple living spaces,
//! and extensive outdoor living areas.

use crate::models::{FloorPlan, RoomType};
use crate::svg_renderer::FloorPlanBuilder;
use crate::units::{CeilingHeight, FeetInches};

/// Create the luxury farmhouse main floor plan based on the provided image
///
/// This floor plan includes:
/// - 4 Bedrooms (including Master Suite)
/// - Family Room with vaulted ceiling
/// - Kitchen with Butler's Pantry
/// - Dining Room, Breakfast Nook
/// - Office, Lounge, Bar
/// - Multiple porches and outdoor living areas
/// - 2 Car Garage
pub fn create_luxury_farmhouse() -> FloorPlan {
    FloorPlanBuilder::new("Luxury Farmhouse")
        .description("Large single-story luxury farmhouse with 4 bedrooms, vaulted ceilings, and extensive outdoor living")
        .level(1)
        // === LEFT WING - Bedrooms 2, 3, 4 and Garage ===

        // 2 Car Garage
        .room_str("2 Car Garage", RoomType::Garage, 0.0, 0.0, "25'-2\"", "31'-9\"")

        // Bedroom 2 (upper left)
        .room_str("Bedroom 2", RoomType::Bedroom, 28.0, 0.0, "14'-2\"", "14'-5\"")

        // Bath 3 (attached to Bedroom 2)
        .room_str("Bath 3", RoomType::FullBath, 28.0, 14.5, "8'-0\"", "8'-0\"")

        // WIC for Bedroom 2
        .room_str("WIC", RoomType::WalkInCloset, 36.0, 14.5, "6'-0\"", "8'-0\"")

        // Bath 2
        .room_str("Bath 2", RoomType::FullBath, 42.0, 0.0, "8'-0\"", "10'-0\"")

        // Bedroom 3 (middle left)
        .room_str("Bedroom 3", RoomType::Bedroom, 28.0, 24.0, "17'-3\"", "13'-4\"")

        // Laundry
        .room_str("Laundry", RoomType::Laundry, 45.0, 24.0, "12'-0\"", "7'-0\"")

        // Powder Room
        .room_str("Powder Room", RoomType::PowderRoom, 57.0, 24.0, "6'-0\"", "7'-0\"")

        // Mud Room
        .room_str("Mud Room", RoomType::MudRoom, 28.0, 40.0, "11'-4\"", "7'-5\"")

        // Bath 4
        .room_str("Bath 4", RoomType::FullBath, 40.0, 40.0, "6'-0\"", "8'-0\"")

        // WIC for Bath 4 area
        .room_str("WIC", RoomType::WalkInCloset, 46.0, 40.0, "6'-0\"", "8'-0\"")

        // Bedroom 4 (lower left)
        .room_str("Bedroom 4", RoomType::Bedroom, 28.0, 52.0, "18'-4\"", "13'-11\"")

        // === CENTER SECTION - Kitchen, Living, Dining ===

        // Breakfast Nook
        .room_str("Breakfast Nook", RoomType::BreakfastNook, 50.0, 0.0, "14'-1\"", "14'-9\"")

        // Kitchen
        .room_str("Kitchen", RoomType::Kitchen, 64.0, 0.0, "14'-0\"", "14'-9\"")

        // Pantry
        .room_str("Pantry", RoomType::Pantry, 64.0, 15.0, "8'-0\"", "8'-0\"")

        // Butler's Pantry
        .room_str("Butler's Pantry", RoomType::ButlersPantry, 52.0, 40.0, "15'-10\"", "9'-0\"")

        // Family Room (with vaulted 7/12 ceiling)
        .room_str("Family Room", RoomType::FamilyRoom, 78.0, 15.0, "16'-6\"", "15'-2\"")

        // Front Hall
        .room_str("Front Hall", RoomType::Foyer, 68.0, 40.0, "10'-2\"", "12'-5\"")

        // Dining Room
        .room_str("Dining Room", RoomType::DiningRoom, 52.0, 52.0, "18'-4\"", "14'-6\"")

        // Foyer
        .room_str("Foyer", RoomType::Foyer, 70.0, 52.0, "11'-4\"", "13'-4\"")

        // Lounge
        .room_str("Lounge", RoomType::Lounge, 82.0, 52.0, "14'-2\"", "12'-2\"")

        // Bar
        .room_str("Bar", RoomType::Bar, 96.0, 40.0, "14'-4\"", "9'-0\"")

        // === RIGHT WING - Master Suite and Office ===

        // Office
        .room_str("Office", RoomType::Office, 96.0, 15.0, "12'-0\"", "12'-0\"")

        // Office Porch
        .room_str("Office Porch", RoomType::Porch, 96.0, 0.0, "11'-4\"", "10'-8\"")

        // Master Suite (with vaulted ceiling)
        .room_str("Master Suite", RoomType::MasterSuite, 110.0, 15.0, "17'-8\"", "22'-8\"")

        // WIC 1 (Master closet)
        .room_str("WIC", RoomType::WalkInCloset, 110.0, 40.0, "12'-0\"", "8'-0\"")

        // WIC 2 (Master closet)
        .room_str("WIC", RoomType::WalkInCloset, 122.0, 40.0, "12'-0\"", "8'-0\"")

        // Master Bath
        .room_str("Master Bath", RoomType::MasterBath, 122.0, 48.0, "12'-0\"", "14'-0\"")

        // === OUTDOOR SPACES ===

        // Breakfast Porch
        .room_str("Breakfast Porch", RoomType::Porch, 64.0, -12.0, "13'-4\"", "12'-4\"")

        // Outdoor Living (vaulted ceiling)
        .room_str("Outdoor Living", RoomType::Patio, 78.0, -15.0, "28'-2\"", "15'-4\"")

        // Master Porch (vaulted ceiling)
        .room_str("Master Porch", RoomType::Porch, 110.0, -10.0, "19'-2\"", "10'-0\"")

        // Side Porch
        .room_str("Side Porch", RoomType::Porch, 134.0, 15.0, "10'-0\"", "32'-0\"")

        // Front Porch
        .room_str("Front Porch", RoomType::Porch, 52.0, 70.0, "56'-8\"", "12'-4\"")

        // === EXTERIOR WALLS ===

        // Main exterior perimeter (simplified)
        .exterior_wall(0.0, 0.0, 144.0, 0.0)      // North wall
        .exterior_wall(144.0, 0.0, 144.0, 82.0)   // East wall
        .exterior_wall(144.0, 82.0, 0.0, 82.0)    // South wall
        .exterior_wall(0.0, 82.0, 0.0, 0.0)       // West wall

        .build()
}

/// Create the luxury farmhouse with vaulted ceiling information
pub fn create_luxury_farmhouse_detailed() -> FloorPlan {
    let mut plan = create_luxury_farmhouse();

    // Update rooms with vaulted ceilings
    for room in &mut plan.rooms {
        match room.name.as_str() {
            "Family Room" => {
                room.ceiling = CeilingHeight::Vaulted {
                    min_height: FeetInches::new(9, 0),
                    pitch: 7, // 7/12 pitch as shown in image
                };
            }
            "Outdoor Living" | "Master Suite" | "Master Porch" => {
                room.ceiling = CeilingHeight::Vaulted {
                    min_height: FeetInches::new(10, 0),
                    pitch: 6,
                };
            }
            "Front Porch" | "Breakfast Porch" => {
                room.ceiling = CeilingHeight::Standard(FeetInches::new(12, 8));
            }
            _ => {}
        }
    }

    plan
}

/// Room data structure for programmatic floor plan definition
/// (Named differently from serialization::RoomDefinition to avoid conflicts)
#[derive(Debug, Clone)]
pub struct LuxuryRoomDef {
    pub name: String,
    pub room_type: RoomType,
    pub x: f64,
    pub y: f64,
    pub length: String,
    pub width: String,
    pub ceiling_height: Option<String>,
    pub notes: Option<String>,
}

impl LuxuryRoomDef {
    pub fn new(name: &str, room_type: RoomType, x: f64, y: f64, length: &str, width: &str) -> Self {
        Self {
            name: name.to_string(),
            room_type,
            x,
            y,
            length: length.to_string(),
            width: width.to_string(),
            ceiling_height: None,
            notes: None,
        }
    }

    pub fn with_ceiling(mut self, height: &str) -> Self {
        self.ceiling_height = Some(height.to_string());
        self
    }

    pub fn with_notes(mut self, notes: &str) -> Self {
        self.notes = Some(notes.to_string());
        self
    }
}

/// Get all room definitions for the luxury farmhouse
pub fn get_luxury_farmhouse_rooms() -> Vec<LuxuryRoomDef> {
    vec![
        // Garage
        LuxuryRoomDef::new(
            "2 Car Garage",
            RoomType::Garage,
            0.0,
            0.0,
            "25'-2\"",
            "31'-9\"",
        )
        .with_ceiling("9'-8\"")
        .with_notes("A.F.F. ceiling"),
        // Bedrooms
        LuxuryRoomDef::new(
            "Bedroom 2",
            RoomType::Bedroom,
            28.0,
            0.0,
            "14'-2\"",
            "14'-5\"",
        )
        .with_ceiling("12'-0\""),
        LuxuryRoomDef::new(
            "Bedroom 3",
            RoomType::Bedroom,
            28.0,
            24.0,
            "17'-3\"",
            "13'-4\"",
        )
        .with_ceiling("12'-0\""),
        LuxuryRoomDef::new(
            "Bedroom 4",
            RoomType::Bedroom,
            28.0,
            52.0,
            "18'-4\"",
            "13'-11\"",
        )
        .with_ceiling("12'-0\""),
        LuxuryRoomDef::new(
            "Master Suite",
            RoomType::MasterSuite,
            110.0,
            15.0,
            "17'-8\"",
            "22'-8\"",
        )
        .with_ceiling("Vaulted"),
        // Bathrooms
        LuxuryRoomDef::new("Bath 3", RoomType::FullBath, 28.0, 14.5, "8'-0\"", "8'-0\""),
        LuxuryRoomDef::new("Bath 2", RoomType::FullBath, 42.0, 0.0, "8'-0\"", "10'-0\""),
        LuxuryRoomDef::new("Bath 4", RoomType::FullBath, 40.0, 40.0, "6'-0\"", "8'-0\""),
        LuxuryRoomDef::new(
            "Powder Room",
            RoomType::PowderRoom,
            57.0,
            24.0,
            "6'-0\"",
            "7'-0\"",
        ),
        LuxuryRoomDef::new(
            "Master Bath",
            RoomType::MasterBath,
            122.0,
            48.0,
            "12'-0\"",
            "14'-0\"",
        )
        .with_ceiling("12'-0\""),
        // Living Spaces
        LuxuryRoomDef::new(
            "Family Room",
            RoomType::FamilyRoom,
            78.0,
            15.0,
            "16'-6\"",
            "15'-2\"",
        )
        .with_ceiling("7/12 Vaulted"),
        LuxuryRoomDef::new("Lounge", RoomType::Lounge, 82.0, 52.0, "14'-2\"", "12'-2\"")
            .with_ceiling("14'-0\""),
        LuxuryRoomDef::new("Foyer", RoomType::Foyer, 70.0, 52.0, "11'-4\"", "13'-4\"")
            .with_ceiling("14'-0\""),
        LuxuryRoomDef::new(
            "Front Hall",
            RoomType::Foyer,
            68.0,
            40.0,
            "10'-2\"",
            "12'-5\"",
        )
        .with_ceiling("14'-0\""),
        // Kitchen & Dining
        LuxuryRoomDef::new(
            "Kitchen",
            RoomType::Kitchen,
            64.0,
            0.0,
            "14'-0\"",
            "14'-9\"",
        ),
        LuxuryRoomDef::new(
            "Breakfast Nook",
            RoomType::BreakfastNook,
            50.0,
            0.0,
            "14'-1\"",
            "14'-9\"",
        )
        .with_ceiling("14'-0\""),
        LuxuryRoomDef::new(
            "Dining Room",
            RoomType::DiningRoom,
            52.0,
            52.0,
            "18'-4\"",
            "14'-6\"",
        )
        .with_ceiling("14'-0\""),
        LuxuryRoomDef::new("Pantry", RoomType::Pantry, 64.0, 15.0, "8'-0\"", "8'-0\""),
        LuxuryRoomDef::new(
            "Butler's Pantry",
            RoomType::ButlersPantry,
            52.0,
            40.0,
            "15'-10\"",
            "9'-0\"",
        ),
        LuxuryRoomDef::new("Bar", RoomType::Bar, 96.0, 40.0, "14'-4\"", "9'-0\"")
            .with_ceiling("12'-0\""),
        // Utility
        LuxuryRoomDef::new(
            "Laundry",
            RoomType::Laundry,
            45.0,
            24.0,
            "12'-0\"",
            "7'-0\"",
        )
        .with_ceiling("12'-0\""),
        LuxuryRoomDef::new(
            "Mud Room",
            RoomType::MudRoom,
            28.0,
            40.0,
            "11'-4\"",
            "7'-5\"",
        )
        .with_ceiling("12'-0\""),
        // Closets
        LuxuryRoomDef::new(
            "WIC (BR2)",
            RoomType::WalkInCloset,
            36.0,
            14.5,
            "6'-0\"",
            "8'-0\"",
        ),
        LuxuryRoomDef::new(
            "WIC (BR4)",
            RoomType::WalkInCloset,
            46.0,
            40.0,
            "6'-0\"",
            "8'-0\"",
        ),
        LuxuryRoomDef::new(
            "WIC (Master 1)",
            RoomType::WalkInCloset,
            110.0,
            40.0,
            "12'-0\"",
            "8'-0\"",
        )
        .with_ceiling("12'-0\""),
        LuxuryRoomDef::new(
            "WIC (Master 2)",
            RoomType::WalkInCloset,
            122.0,
            40.0,
            "12'-0\"",
            "8'-0\"",
        )
        .with_ceiling("12'-0\""),
        // Office
        LuxuryRoomDef::new("Office", RoomType::Office, 96.0, 15.0, "12'-0\"", "12'-0\"")
            .with_ceiling("14'-0\""),
        // Outdoor Spaces
        LuxuryRoomDef::new(
            "Front Porch",
            RoomType::Porch,
            52.0,
            70.0,
            "56'-8\"",
            "12'-4\"",
        )
        .with_ceiling("12'-8\" A.F.F."),
        LuxuryRoomDef::new(
            "Breakfast Porch",
            RoomType::Porch,
            64.0,
            -12.0,
            "13'-4\"",
            "12'-4\"",
        )
        .with_ceiling("14'-0\""),
        LuxuryRoomDef::new(
            "Outdoor Living",
            RoomType::Patio,
            78.0,
            -15.0,
            "28'-2\"",
            "15'-4\"",
        )
        .with_ceiling("Vaulted"),
        LuxuryRoomDef::new(
            "Office Porch",
            RoomType::Porch,
            96.0,
            0.0,
            "11'-4\"",
            "10'-8\"",
        )
        .with_ceiling("14'-0\""),
        LuxuryRoomDef::new(
            "Master Porch",
            RoomType::Porch,
            110.0,
            -10.0,
            "19'-2\"",
            "10'-0\"",
        )
        .with_ceiling("Vaulted"),
        LuxuryRoomDef::new(
            "Side Porch",
            RoomType::Porch,
            134.0,
            15.0,
            "10'-0\"",
            "32'-0\"",
        ),
    ]
}

/// Calculate approximate total square footage from room definitions
pub fn calculate_total_sqft(rooms: &[LuxuryRoomDef]) -> f64 {
    rooms
        .iter()
        .map(|r| {
            let length = FeetInches::parse(&r.length).unwrap_or_default();
            let width = FeetInches::parse(&r.width).unwrap_or_default();
            length.to_decimal_feet() * width.to_decimal_feet()
        })
        .sum()
}

/// Calculate living area (excludes garage, porches, outdoor spaces)
pub fn calculate_living_sqft(rooms: &[LuxuryRoomDef]) -> f64 {
    rooms
        .iter()
        .filter(|r| {
            !matches!(
                r.room_type,
                RoomType::Garage
                    | RoomType::Carport
                    | RoomType::Porch
                    | RoomType::Deck
                    | RoomType::Patio
            )
        })
        .map(|r| {
            let length = FeetInches::parse(&r.length).unwrap_or_default();
            let width = FeetInches::parse(&r.width).unwrap_or_default();
            length.to_decimal_feet() * width.to_decimal_feet()
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_create_luxury_farmhouse() {
        let plan = create_luxury_farmhouse();
        assert_eq!(plan.name, "Luxury Farmhouse");
        assert!(plan.rooms.len() > 20, "Should have many rooms");
    }

    #[test]
    fn test_room_definitions() {
        let rooms = get_luxury_farmhouse_rooms();
        assert!(rooms.len() > 20);

        // Check for key rooms
        assert!(rooms.iter().any(|r| r.name == "Master Suite"));
        assert!(rooms.iter().any(|r| r.name == "Family Room"));
        assert!(rooms.iter().any(|r| r.name == "Kitchen"));
    }

    #[test]
    fn test_calculate_sqft() {
        let rooms = get_luxury_farmhouse_rooms();
        let total = calculate_total_sqft(&rooms);
        let living = calculate_living_sqft(&rooms);

        // Sanity checks - this is a large house
        assert!(total > 4000.0, "Total should be large");
        assert!(living > 3000.0, "Living area should be substantial");
        assert!(living < total, "Living area should be less than total");
    }
}
