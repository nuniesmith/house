//! # Floor Plan Serialization
//!
//! Provides JSON and TOML serialization support for floor plan definitions.
//! This allows floor plans to be defined in external files and loaded at runtime.

use crate::models::{FloorPlan, Point, Room, RoomType, Wall, WallType};
use crate::units::{CeilingHeight, FeetInches};
use serde::{Deserialize, Serialize};

/// A serializable floor plan definition
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FloorPlanDefinition {
    /// Name of the floor plan
    pub name: String,
    /// Optional description
    #[serde(default)]
    pub description: Option<String>,
    /// Floor level (0 = ground, 1 = second, -1 = basement)
    #[serde(default)]
    pub level: i32,
    /// Overall dimensions (optional, will be calculated if not provided)
    #[serde(default)]
    pub overall_length: Option<String>,
    #[serde(default)]
    pub overall_width: Option<String>,
    /// Room definitions
    #[serde(default)]
    pub rooms: Vec<RoomDefinition>,
    /// Wall definitions
    #[serde(default)]
    pub walls: Vec<WallDefinition>,
}

/// A serializable room definition
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RoomDefinition {
    /// Room name
    pub name: String,
    /// Room type (lowercase snake_case)
    #[serde(rename = "type")]
    pub room_type: String,
    /// X position in feet
    pub x: f64,
    /// Y position in feet
    pub y: f64,
    /// Length dimension (e.g., "14'-6\"" or "14.5")
    pub length: String,
    /// Width dimension (e.g., "12'-0\"" or "12")
    pub width: String,
    /// Optional ceiling height specification
    #[serde(default)]
    pub ceiling: Option<CeilingDefinition>,
    /// Optional notes
    #[serde(default)]
    pub notes: Option<String>,
}

/// Ceiling height definition
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum CeilingDefinition {
    /// Standard flat ceiling with height string
    Standard(String),
    /// Vaulted ceiling with pitch
    Vaulted {
        #[serde(rename = "type")]
        ceiling_type: String,
        min_height: String,
        pitch: u8,
    },
    /// Tray ceiling
    Tray {
        #[serde(rename = "type")]
        ceiling_type: String,
        perimeter_height: String,
        center_height: String,
        #[serde(default = "default_tray_width")]
        tray_width: String,
    },
}

fn default_tray_width() -> String {
    "2'-0\"".to_string()
}

/// A serializable wall definition
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WallDefinition {
    /// Wall type
    #[serde(rename = "type")]
    pub wall_type: String,
    /// Start point
    pub start: PointDefinition,
    /// End point
    pub end: PointDefinition,
    /// Optional height override
    #[serde(default)]
    pub height: Option<String>,
    /// Doors on this wall
    #[serde(default)]
    pub doors: Vec<DoorDefinition>,
    /// Windows on this wall
    #[serde(default)]
    pub windows: Vec<WindowDefinition>,
}

/// Point definition
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PointDefinition {
    pub x: f64,
    pub y: f64,
}

/// Door definition
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DoorDefinition {
    /// Door type
    #[serde(rename = "type")]
    pub door_type: String,
    /// Position along the wall in feet
    pub position: String,
    /// Optional width override
    #[serde(default)]
    pub width: Option<String>,
    /// Optional height override
    #[serde(default)]
    pub height: Option<String>,
}

/// Window definition
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WindowDefinition {
    /// Window type
    #[serde(rename = "type")]
    pub window_type: String,
    /// Position along the wall in feet
    pub position: String,
    /// Width
    pub width: String,
    /// Height
    pub height: String,
    /// Sill height from floor
    #[serde(default)]
    pub sill_height: Option<String>,
}

impl FloorPlanDefinition {
    /// Load a floor plan definition from JSON
    pub fn from_json(json: &str) -> Result<Self, serde_json::Error> {
        serde_json::from_str(json)
    }

    /// Serialize to JSON
    pub fn to_json(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string_pretty(self)
    }

    /// Serialize to JSON (compact)
    pub fn to_json_compact(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string(self)
    }

    /// Convert to a FloorPlan model
    pub fn to_floor_plan(&self) -> FloorPlan {
        let mut plan = FloorPlan::new(&self.name);
        plan.description = self.description.clone();
        plan.level = self.level;

        // Add rooms
        for room_def in &self.rooms {
            let room = room_def.to_room();
            plan.add_room(room);
        }

        // Add walls
        for wall_def in &self.walls {
            let wall = wall_def.to_wall();
            plan.add_wall(wall);
        }

        // Set overall dimensions if provided
        if let Some(ref length) = self.overall_length {
            if let Ok(fi) = FeetInches::parse(length) {
                plan.overall_length = fi;
            }
        }
        if let Some(ref width) = self.overall_width {
            if let Ok(fi) = FeetInches::parse(width) {
                plan.overall_width = fi;
            }
        }

        plan
    }
}

impl RoomDefinition {
    /// Parse the room type string into a RoomType enum
    fn parse_room_type(&self) -> RoomType {
        match self.room_type.to_lowercase().as_str() {
            "living_room" | "livingroom" => RoomType::LivingRoom,
            "family_room" | "familyroom" => RoomType::FamilyRoom,
            "great_room" | "greatroom" => RoomType::GreatRoom,
            "lounge" => RoomType::Lounge,
            "foyer" => RoomType::Foyer,
            "hallway" => RoomType::Hallway,
            "master_suite" | "mastersuite" => RoomType::MasterSuite,
            "bedroom" => RoomType::Bedroom,
            "guest_room" | "guestroom" => RoomType::GuestRoom,
            "nursery" => RoomType::Nursery,
            "master_bath" | "masterbath" => RoomType::MasterBath,
            "full_bath" | "fullbath" | "bathroom" => RoomType::FullBath,
            "half_bath" | "halfbath" => RoomType::HalfBath,
            "powder_room" | "powderroom" => RoomType::PowderRoom,
            "kitchen" => RoomType::Kitchen,
            "dining_room" | "diningroom" | "dining" => RoomType::DiningRoom,
            "breakfast_nook" | "breakfastnook" | "nook" => RoomType::BreakfastNook,
            "pantry" => RoomType::Pantry,
            "butlers_pantry" | "butlerspantry" => RoomType::ButlersPantry,
            "bar" => RoomType::Bar,
            "laundry" => RoomType::Laundry,
            "mud_room" | "mudroom" => RoomType::MudRoom,
            "utility" => RoomType::Utility,
            "storage" => RoomType::Storage,
            "closet" => RoomType::Closet,
            "walk_in_closet" | "walkincloset" | "wic" => RoomType::WalkInCloset,
            "office" => RoomType::Office,
            "study" => RoomType::Study,
            "library" => RoomType::Library,
            "porch" => RoomType::Porch,
            "deck" => RoomType::Deck,
            "patio" => RoomType::Patio,
            "sunroom" => RoomType::Sunroom,
            "screened" | "screened_porch" => RoomType::Screened,
            "garage" => RoomType::Garage,
            "carport" => RoomType::Carport,
            "workshop" => RoomType::Workshop,
            "basement" => RoomType::Basement,
            "attic" => RoomType::Attic,
            "mechanical" => RoomType::Mechanical,
            _ => RoomType::Other,
        }
    }

    /// Parse the ceiling definition
    fn parse_ceiling(&self) -> CeilingHeight {
        match &self.ceiling {
            Some(CeilingDefinition::Standard(height)) => {
                let fi = FeetInches::parse(height).unwrap_or(FeetInches::new(9, 0));
                CeilingHeight::Standard(fi)
            }
            Some(CeilingDefinition::Vaulted {
                ceiling_type: _,
                min_height,
                pitch,
            }) => {
                let min = FeetInches::parse(min_height).unwrap_or(FeetInches::new(9, 0));
                CeilingHeight::Vaulted {
                    min_height: min,
                    pitch: *pitch,
                }
            }
            Some(CeilingDefinition::Tray {
                ceiling_type: _,
                perimeter_height,
                center_height,
                tray_width,
            }) => {
                let perimeter =
                    FeetInches::parse(perimeter_height).unwrap_or(FeetInches::new(9, 0));
                let center = FeetInches::parse(center_height).unwrap_or(FeetInches::new(10, 0));
                let width = FeetInches::parse(tray_width).unwrap_or(FeetInches::new(2, 0));
                CeilingHeight::Tray {
                    perimeter_height: perimeter,
                    center_height: center,
                    tray_width: width,
                }
            }
            None => {
                let room_type = self.parse_room_type();
                room_type.default_ceiling_height()
            }
        }
    }

    /// Convert to a Room model
    pub fn to_room(&self) -> Room {
        let length = FeetInches::parse(&self.length).unwrap_or_default();
        let width = FeetInches::parse(&self.width).unwrap_or_default();
        let room_type = self.parse_room_type();

        let mut room = Room::new(self.name.clone(), room_type, length, width);
        room.position = Point::new(self.x, self.y);
        room.ceiling = self.parse_ceiling();

        if let Some(ref notes) = self.notes {
            room.notes = Some(notes.clone());
        }

        room
    }
}

impl WallDefinition {
    /// Parse wall type
    fn parse_wall_type(&self) -> WallType {
        match self.wall_type.to_lowercase().as_str() {
            "exterior_load_bearing" | "exterior_loadbearing" | "exterior" => {
                WallType::ExteriorLoadBearing
            }
            "exterior_non_bearing" | "exterior_nonbearing" => WallType::ExteriorNonBearing,
            "interior_load_bearing" | "interior_loadbearing" => WallType::InteriorLoadBearing,
            "interior_partition" | "interior" | "partition" => WallType::InteriorPartition,
            "half_wall" | "halfwall" => WallType::HalfWall,
            "pony_wall" | "ponywall" => WallType::PonyWall,
            "foundation" => WallType::Foundation,
            _ => WallType::InteriorPartition,
        }
    }

    /// Convert to a Wall model
    pub fn to_wall(&self) -> Wall {
        let wall_type = self.parse_wall_type();
        let start = Point::new(self.start.x, self.start.y);
        let end = Point::new(self.end.x, self.end.y);

        let mut wall = Wall::new(wall_type, start, end);

        if let Some(ref height) = self.height {
            if let Ok(fi) = FeetInches::parse(height) {
                wall.height = Some(fi);
            }
        }

        wall
    }
}

/// Create an example floor plan definition for documentation
pub fn example_floor_plan_json() -> String {
    let definition = FloorPlanDefinition {
        name: "Example Floor Plan".to_string(),
        description: Some("A simple example floor plan".to_string()),
        level: 1,
        overall_length: Some("60'-0\"".to_string()),
        overall_width: Some("40'-0\"".to_string()),
        rooms: vec![
            RoomDefinition {
                name: "Living Room".to_string(),
                room_type: "living_room".to_string(),
                x: 0.0,
                y: 0.0,
                length: "20'-0\"".to_string(),
                width: "15'-0\"".to_string(),
                ceiling: Some(CeilingDefinition::Standard("9'-0\"".to_string())),
                notes: Some("Main living area".to_string()),
            },
            RoomDefinition {
                name: "Kitchen".to_string(),
                room_type: "kitchen".to_string(),
                x: 20.0,
                y: 0.0,
                length: "15'-0\"".to_string(),
                width: "12'-0\"".to_string(),
                ceiling: None,
                notes: None,
            },
            RoomDefinition {
                name: "Master Suite".to_string(),
                room_type: "master_suite".to_string(),
                x: 0.0,
                y: 15.0,
                length: "18'-0\"".to_string(),
                width: "16'-0\"".to_string(),
                ceiling: Some(CeilingDefinition::Vaulted {
                    ceiling_type: "vaulted".to_string(),
                    min_height: "9'-0\"".to_string(),
                    pitch: 6,
                }),
                notes: None,
            },
        ],
        walls: vec![
            WallDefinition {
                wall_type: "exterior".to_string(),
                start: PointDefinition { x: 0.0, y: 0.0 },
                end: PointDefinition { x: 60.0, y: 0.0 },
                height: None,
                doors: vec![],
                windows: vec![],
            },
            WallDefinition {
                wall_type: "interior".to_string(),
                start: PointDefinition { x: 20.0, y: 0.0 },
                end: PointDefinition { x: 20.0, y: 15.0 },
                height: None,
                doors: vec![DoorDefinition {
                    door_type: "interior_single".to_string(),
                    position: "5'-0\"".to_string(),
                    width: None,
                    height: None,
                }],
                windows: vec![],
            },
        ],
    };

    definition.to_json().unwrap_or_default()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_room_definition_parsing() {
        let room_def = RoomDefinition {
            name: "Test Room".to_string(),
            room_type: "bedroom".to_string(),
            x: 10.0,
            y: 20.0,
            length: "14'-6\"".to_string(),
            width: "12'-0\"".to_string(),
            ceiling: None,
            notes: None,
        };

        let room = room_def.to_room();
        assert_eq!(room.name, "Test Room");
        assert_eq!(room.room_type, RoomType::Bedroom);
        assert_eq!(room.length.feet, 14);
        assert_eq!(room.length.inches, 6);
    }

    #[test]
    fn test_json_serialization() {
        let json = example_floor_plan_json();
        assert!(json.contains("Example Floor Plan"));
        assert!(json.contains("living_room"));
    }

    #[test]
    fn test_json_deserialization() {
        let json = r#"{
            "name": "Test Plan",
            "level": 1,
            "rooms": [
                {
                    "name": "Bedroom",
                    "type": "bedroom",
                    "x": 0,
                    "y": 0,
                    "length": "12'-0\"",
                    "width": "10'-0\""
                }
            ],
            "walls": []
        }"#;

        let definition = FloorPlanDefinition::from_json(json).unwrap();
        assert_eq!(definition.name, "Test Plan");
        assert_eq!(definition.rooms.len(), 1);
    }

    #[test]
    fn test_to_floor_plan() {
        let definition = FloorPlanDefinition {
            name: "Conversion Test".to_string(),
            description: Some("Testing conversion".to_string()),
            level: 2,
            overall_length: None,
            overall_width: None,
            rooms: vec![RoomDefinition {
                name: "Room 1".to_string(),
                room_type: "office".to_string(),
                x: 0.0,
                y: 0.0,
                length: "10'-0\"".to_string(),
                width: "10'-0\"".to_string(),
                ceiling: None,
                notes: None,
            }],
            walls: vec![],
        };

        let plan = definition.to_floor_plan();
        assert_eq!(plan.name, "Conversion Test");
        assert_eq!(plan.level, 2);
        assert_eq!(plan.rooms.len(), 1);
        assert_eq!(plan.rooms[0].room_type, RoomType::Office);
    }

    #[test]
    fn test_wall_type_parsing() {
        let wall_def = WallDefinition {
            wall_type: "exterior".to_string(),
            start: PointDefinition { x: 0.0, y: 0.0 },
            end: PointDefinition { x: 10.0, y: 0.0 },
            height: None,
            doors: vec![],
            windows: vec![],
        };

        let wall = wall_def.to_wall();
        assert!(wall.wall_type.is_exterior());
    }
}
