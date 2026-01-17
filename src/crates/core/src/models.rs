//! # Models Module
//!
//! Core data models for floor plan design including rooms, walls,
//! doors, windows, and complete floor plans.

use serde::{Deserialize, Serialize};
use uuid::Uuid;

use crate::units::{CeilingHeight, FeetInches, LinearFeet, SquareFeet};

/// Unique identifier for entities
pub type EntityId = Uuid;

/// Generate a new unique ID
pub fn new_id() -> EntityId {
    Uuid::new_v4()
}

/// Types of rooms in a floor plan
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
#[non_exhaustive]
pub enum RoomType {
    // Living spaces
    LivingRoom,
    FamilyRoom,
    GreatRoom,
    Lounge,
    Foyer,
    Hallway,

    // Bedrooms
    MasterSuite,
    Bedroom,
    GuestRoom,
    Nursery,

    // Bathrooms
    MasterBath,
    FullBath,
    HalfBath,
    PowderRoom,

    // Kitchen & Dining
    Kitchen,
    DiningRoom,
    BreakfastNook,
    Pantry,
    ButlersPantry,
    Bar,

    // Utility
    Laundry,
    MudRoom,
    Utility,
    Storage,
    Closet,
    WalkInCloset,

    // Work spaces
    Office,
    Study,
    Library,

    // Outdoor
    Porch,
    Deck,
    Patio,
    Sunroom,
    Screened,

    // Garage
    Garage,
    Carport,
    Workshop,

    // Other
    Basement,
    Attic,
    Mechanical,
    Other,
}

impl RoomType {
    /// Get default ceiling height for room type
    pub fn default_ceiling_height(&self) -> CeilingHeight {
        match self {
            RoomType::Garage | RoomType::Carport | RoomType::Workshop => {
                CeilingHeight::Standard(FeetInches::new(10, 0))
            }
            RoomType::Basement | RoomType::Mechanical => {
                CeilingHeight::Standard(FeetInches::new(8, 0))
            }
            RoomType::Porch | RoomType::Deck | RoomType::Patio => {
                CeilingHeight::Standard(FeetInches::new(10, 0))
            }
            RoomType::MasterSuite | RoomType::GreatRoom | RoomType::FamilyRoom => {
                CeilingHeight::Vaulted {
                    min_height: FeetInches::new(9, 0),
                    pitch: 7,
                }
            }
            _ => CeilingHeight::Standard(FeetInches::new(9, 0)),
        }
    }

    /// Check if this is an outdoor/exterior space
    pub fn is_outdoor(&self) -> bool {
        matches!(
            self,
            RoomType::Porch
                | RoomType::Deck
                | RoomType::Patio
                | RoomType::Screened
                | RoomType::Carport
        )
    }

    /// Check if this is a wet room (needs waterproofing)
    pub fn is_wet_room(&self) -> bool {
        matches!(
            self,
            RoomType::MasterBath
                | RoomType::FullBath
                | RoomType::HalfBath
                | RoomType::PowderRoom
                | RoomType::Kitchen
                | RoomType::Laundry
                | RoomType::ButlersPantry
        )
    }

    /// Get display name for the room type
    pub fn display_name(&self) -> &str {
        match self {
            RoomType::LivingRoom => "Living Room",
            RoomType::FamilyRoom => "Family Room",
            RoomType::GreatRoom => "Great Room",
            RoomType::Lounge => "Lounge",
            RoomType::Foyer => "Foyer",
            RoomType::Hallway => "Hallway",
            RoomType::MasterSuite => "Master Suite",
            RoomType::Bedroom => "Bedroom",
            RoomType::GuestRoom => "Guest Room",
            RoomType::Nursery => "Nursery",
            RoomType::MasterBath => "Master Bath",
            RoomType::FullBath => "Full Bath",
            RoomType::HalfBath => "Half Bath",
            RoomType::PowderRoom => "Powder Room",
            RoomType::Kitchen => "Kitchen",
            RoomType::DiningRoom => "Dining Room",
            RoomType::BreakfastNook => "Breakfast Nook",
            RoomType::Pantry => "Pantry",
            RoomType::ButlersPantry => "Butler's Pantry",
            RoomType::Bar => "Bar",
            RoomType::Laundry => "Laundry",
            RoomType::MudRoom => "Mud Room",
            RoomType::Utility => "Utility",
            RoomType::Storage => "Storage",
            RoomType::Closet => "Closet",
            RoomType::WalkInCloset => "Walk-in Closet",
            RoomType::Office => "Office",
            RoomType::Study => "Study",
            RoomType::Library => "Library",
            RoomType::Porch => "Porch",
            RoomType::Deck => "Deck",
            RoomType::Patio => "Patio",
            RoomType::Sunroom => "Sunroom",
            RoomType::Screened => "Screened Porch",
            RoomType::Garage => "Garage",
            RoomType::Carport => "Carport",
            RoomType::Workshop => "Workshop",
            RoomType::Basement => "Basement",
            RoomType::Attic => "Attic",
            RoomType::Mechanical => "Mechanical",
            RoomType::Other => "Other",
        }
    }
}

impl Default for RoomType {
    fn default() -> Self {
        RoomType::Bedroom
    }
}

/// Wall construction types
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum WallType {
    /// Exterior load-bearing wall (typically 2x6)
    ExteriorLoadBearing,
    /// Exterior non-load-bearing wall
    ExteriorNonBearing,
    /// Interior load-bearing wall (typically 2x4 or 2x6)
    InteriorLoadBearing,
    /// Interior partition wall (typically 2x4)
    InteriorPartition,
    /// Half wall / knee wall
    HalfWall,
    /// Pony wall (partial height)
    PonyWall,
    /// Foundation wall
    Foundation,
}

impl WallType {
    /// Get the typical stud depth for this wall type
    pub fn stud_depth(&self) -> FeetInches {
        match self {
            WallType::ExteriorLoadBearing | WallType::ExteriorNonBearing => {
                FeetInches::new(0, 6) // 2x6 = 5.5" actual
            }
            WallType::InteriorLoadBearing => FeetInches::new(0, 6),
            WallType::InteriorPartition | WallType::HalfWall | WallType::PonyWall => {
                FeetInches::new(0, 4) // 2x4 = 3.5" actual
            }
            WallType::Foundation => FeetInches::new(0, 8), // 8" concrete
        }
    }

    /// Check if this wall type is exterior
    pub fn is_exterior(&self) -> bool {
        matches!(
            self,
            WallType::ExteriorLoadBearing | WallType::ExteriorNonBearing | WallType::Foundation
        )
    }

    /// Check if this wall type is load-bearing
    pub fn is_load_bearing(&self) -> bool {
        matches!(
            self,
            WallType::ExteriorLoadBearing | WallType::InteriorLoadBearing | WallType::Foundation
        )
    }
}

impl Default for WallType {
    fn default() -> Self {
        WallType::InteriorPartition
    }
}

/// Door types
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum DoorType {
    /// Standard interior hinged door
    InteriorSingle,
    /// Double interior doors
    InteriorDouble,
    /// Pocket door (slides into wall)
    Pocket,
    /// Barn door (slides on track)
    Barn,
    /// Bi-fold doors (closets)
    BiFold,
    /// Exterior entry door
    ExteriorEntry,
    /// French doors
    French,
    /// Sliding glass door
    Sliding,
    /// Garage door
    Garage,
}

impl DoorType {
    /// Get the standard width for this door type
    pub fn standard_width(&self) -> FeetInches {
        match self {
            DoorType::InteriorSingle | DoorType::Pocket | DoorType::Barn => FeetInches::new(2, 8),
            DoorType::InteriorDouble => FeetInches::new(5, 4),
            DoorType::BiFold => FeetInches::new(4, 0),
            DoorType::ExteriorEntry => FeetInches::new(3, 0),
            DoorType::French => FeetInches::new(6, 0),
            DoorType::Sliding => FeetInches::new(6, 0),
            DoorType::Garage => FeetInches::new(16, 0),
        }
    }

    /// Get the standard height for this door type
    pub fn standard_height(&self) -> FeetInches {
        match self {
            DoorType::Garage => FeetInches::new(7, 0),
            _ => FeetInches::new(6, 8),
        }
    }
}

/// Window types
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum WindowType {
    /// Double-hung window
    DoubleHung,
    /// Single-hung window
    SingleHung,
    /// Casement window (hinged)
    Casement,
    /// Awning window
    Awning,
    /// Fixed/picture window
    Fixed,
    /// Sliding window
    Sliding,
    /// Bay window
    Bay,
    /// Bow window
    Bow,
    /// Skylight
    Skylight,
}

/// A door in the floor plan
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Door {
    pub id: EntityId,
    pub door_type: DoorType,
    pub width: FeetInches,
    pub height: FeetInches,
    /// Position along the wall (from start point)
    pub position: FeetInches,
    /// Which wall this door belongs to
    pub wall_id: EntityId,
    /// Swing direction (for hinged doors)
    pub swing_direction: Option<SwingDirection>,
}

impl Door {
    pub fn new(door_type: DoorType, wall_id: EntityId, position: FeetInches) -> Self {
        Self {
            id: new_id(),
            door_type,
            width: door_type.standard_width(),
            height: door_type.standard_height(),
            position,
            wall_id,
            swing_direction: Some(SwingDirection::Left),
        }
    }

    /// Calculate the rough opening width (typically door width + 2")
    pub fn rough_opening_width(&self) -> FeetInches {
        FeetInches::from_inches(self.width.to_inches() + 2)
    }

    /// Calculate the rough opening height (typically door height + 2")
    pub fn rough_opening_height(&self) -> FeetInches {
        FeetInches::from_inches(self.height.to_inches() + 2)
    }
}

/// Door swing direction
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum SwingDirection {
    Left,
    Right,
    In,
    Out,
}

/// A window in the floor plan
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Window {
    pub id: EntityId,
    pub window_type: WindowType,
    pub width: FeetInches,
    pub height: FeetInches,
    /// Height from floor to bottom of window
    pub sill_height: FeetInches,
    /// Position along the wall (from start point)
    pub position: FeetInches,
    /// Which wall this window belongs to
    pub wall_id: EntityId,
}

impl Window {
    pub fn new(
        window_type: WindowType,
        wall_id: EntityId,
        position: FeetInches,
        width: FeetInches,
        height: FeetInches,
    ) -> Self {
        Self {
            id: new_id(),
            window_type,
            width,
            height,
            sill_height: FeetInches::new(3, 0), // Standard 3' sill height
            position,
            wall_id,
        }
    }

    /// Calculate the rough opening width (typically window width + 1/2")
    pub fn rough_opening_width(&self) -> FeetInches {
        FeetInches::from_inches(self.width.to_inches() + 1)
    }

    /// Calculate the rough opening height (typically window height + 1/2")
    pub fn rough_opening_height(&self) -> FeetInches {
        FeetInches::from_inches(self.height.to_inches() + 1)
    }
}

/// A point in 2D space (in inches for precision)
#[derive(Debug, Clone, Copy, PartialEq, Serialize, Deserialize)]
pub struct Point {
    pub x: f64,
    pub y: f64,
}

impl Point {
    pub fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    pub fn origin() -> Self {
        Self { x: 0.0, y: 0.0 }
    }

    /// Distance to another point (in inches)
    pub fn distance_to(&self, other: &Point) -> f64 {
        let dx = other.x - self.x;
        let dy = other.y - self.y;
        (dx * dx + dy * dy).sqrt()
    }

    /// Convert to FeetInches for x coordinate
    pub fn x_feet_inches(&self) -> FeetInches {
        FeetInches::from_inches(self.x.round() as i32)
    }

    /// Convert to FeetInches for y coordinate
    pub fn y_feet_inches(&self) -> FeetInches {
        FeetInches::from_inches(self.y.round() as i32)
    }
}

impl Default for Point {
    fn default() -> Self {
        Self::origin()
    }
}

/// A wall segment in the floor plan
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Wall {
    pub id: EntityId,
    pub wall_type: WallType,
    /// Start point of the wall
    pub start: Point,
    /// End point of the wall
    pub end: Point,
    /// Wall height (if different from room ceiling)
    pub height: Option<FeetInches>,
    /// Doors on this wall
    pub doors: Vec<Door>,
    /// Windows on this wall
    pub windows: Vec<Window>,
}

impl Wall {
    pub fn new(wall_type: WallType, start: Point, end: Point) -> Self {
        Self {
            id: new_id(),
            wall_type,
            start,
            end,
            height: None,
            doors: Vec::new(),
            windows: Vec::new(),
        }
    }

    /// Calculate the length of the wall
    pub fn length(&self) -> LinearFeet {
        let inches = self.start.distance_to(&self.end);
        LinearFeet::new(inches / 12.0)
    }

    /// Calculate the length in FeetInches
    pub fn length_feet_inches(&self) -> FeetInches {
        FeetInches::from_inches(self.start.distance_to(&self.end).round() as i32)
    }

    /// Add a door to this wall
    pub fn add_door(&mut self, door_type: DoorType, position: FeetInches) -> EntityId {
        let door = Door::new(door_type, self.id, position);
        let id = door.id;
        self.doors.push(door);
        id
    }

    /// Add a window to this wall
    pub fn add_window(
        &mut self,
        window_type: WindowType,
        position: FeetInches,
        width: FeetInches,
        height: FeetInches,
    ) -> EntityId {
        let window = Window::new(window_type, self.id, position, width, height);
        let id = window.id;
        self.windows.push(window);
        id
    }

    /// Calculate total door width on this wall
    pub fn total_door_width(&self) -> FeetInches {
        self.doors
            .iter()
            .fold(FeetInches::default(), |acc, d| acc + d.width)
    }

    /// Calculate total window width on this wall
    pub fn total_window_width(&self) -> FeetInches {
        self.windows
            .iter()
            .fold(FeetInches::default(), |acc, w| acc + w.width)
    }
}

/// A room in the floor plan
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Room {
    pub id: EntityId,
    pub name: String,
    pub room_type: RoomType,
    /// Room dimensions (length x width)
    pub length: FeetInches,
    pub width: FeetInches,
    /// Ceiling configuration
    pub ceiling: CeilingHeight,
    /// Position of the room's origin point (bottom-left corner)
    pub position: Point,
    /// Wall IDs that form this room's boundary
    pub wall_ids: Vec<EntityId>,
    /// Custom notes for this room
    pub notes: Option<String>,
}

impl Room {
    pub fn new(
        name: impl Into<String>,
        room_type: RoomType,
        length: FeetInches,
        width: FeetInches,
    ) -> Self {
        Self {
            id: new_id(),
            name: name.into(),
            room_type,
            length,
            width,
            ceiling: room_type.default_ceiling_height(),
            position: Point::origin(),
            wall_ids: Vec::new(),
            notes: None,
        }
    }

    /// Calculate the floor area of the room
    pub fn floor_area(&self) -> SquareFeet {
        SquareFeet::from_dimensions(self.length, self.width)
    }

    /// Calculate the perimeter of the room
    pub fn perimeter(&self) -> LinearFeet {
        let total = (self.length + self.width) * 2;
        LinearFeet::from_feet_inches(total)
    }

    /// Calculate wall area (for paint, drywall, etc.)
    pub fn wall_area(&self) -> SquareFeet {
        let perimeter = self.perimeter();
        let height = self.ceiling.min_height().to_decimal_feet();
        SquareFeet::new(perimeter.value() * height)
    }

    /// Calculate ceiling area
    pub fn ceiling_area(&self) -> SquareFeet {
        // For vaulted ceilings, this is an approximation
        match &self.ceiling {
            CeilingHeight::Standard(_) => self.floor_area(),
            CeilingHeight::Vaulted { pitch, .. } => {
                // Increase area based on pitch
                let pitch_factor = 1.0 + (*pitch as f64 / 24.0);
                SquareFeet::new(self.floor_area().value() * pitch_factor)
            }
            CeilingHeight::Cathedral { .. } => {
                // Assume roughly 1.3x floor area
                SquareFeet::new(self.floor_area().value() * 1.3)
            }
            CeilingHeight::Tray { .. } => {
                // Tray adds some area
                SquareFeet::new(self.floor_area().value() * 1.1)
            }
        }
    }

    /// Set the room position
    pub fn with_position(mut self, position: Point) -> Self {
        self.position = position;
        self
    }

    /// Set the ceiling height
    pub fn with_ceiling(mut self, ceiling: CeilingHeight) -> Self {
        self.ceiling = ceiling;
        self
    }

    /// Add notes to the room
    pub fn with_notes(mut self, notes: impl Into<String>) -> Self {
        self.notes = Some(notes.into());
        self
    }
}

/// A complete floor plan
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FloorPlan {
    pub id: EntityId,
    pub name: String,
    pub description: Option<String>,
    /// Floor level (0 = ground, 1 = second floor, -1 = basement)
    pub level: i32,
    /// All rooms on this floor
    pub rooms: Vec<Room>,
    /// All walls (may be shared between rooms)
    pub walls: Vec<Wall>,
    /// Overall dimensions
    pub overall_length: FeetInches,
    pub overall_width: FeetInches,
}

impl FloorPlan {
    pub fn new(name: impl Into<String>) -> Self {
        Self {
            id: new_id(),
            name: name.into(),
            description: None,
            level: 0,
            rooms: Vec::new(),
            walls: Vec::new(),
            overall_length: FeetInches::default(),
            overall_width: FeetInches::default(),
        }
    }

    /// Add a room to the floor plan
    pub fn add_room(&mut self, room: Room) -> EntityId {
        let id = room.id;
        self.rooms.push(room);
        self.recalculate_dimensions();
        id
    }

    /// Add a wall to the floor plan
    pub fn add_wall(&mut self, wall: Wall) -> EntityId {
        let id = wall.id;
        self.walls.push(wall);
        id
    }

    /// Get a room by ID
    pub fn get_room(&self, id: EntityId) -> Option<&Room> {
        self.rooms.iter().find(|r| r.id == id)
    }

    /// Get a mutable room by ID
    pub fn get_room_mut(&mut self, id: EntityId) -> Option<&mut Room> {
        self.rooms.iter_mut().find(|r| r.id == id)
    }

    /// Get a wall by ID
    pub fn get_wall(&self, id: EntityId) -> Option<&Wall> {
        self.walls.iter().find(|w| w.id == id)
    }

    /// Get a mutable wall by ID
    pub fn get_wall_mut(&mut self, id: EntityId) -> Option<&mut Wall> {
        self.walls.iter_mut().find(|w| w.id == id)
    }

    /// Calculate total floor area
    pub fn total_floor_area(&self) -> SquareFeet {
        self.rooms
            .iter()
            .map(|r| r.floor_area())
            .fold(SquareFeet::default(), |a, b| a + b)
    }

    /// Calculate total living area (excludes garages, porches, etc.)
    pub fn total_living_area(&self) -> SquareFeet {
        self.rooms
            .iter()
            .filter(|r| !r.room_type.is_outdoor() && !matches!(r.room_type, RoomType::Garage))
            .map(|r| r.floor_area())
            .fold(SquareFeet::default(), |a, b| a + b)
    }

    /// Get rooms by type
    pub fn rooms_by_type(&self, room_type: RoomType) -> Vec<&Room> {
        self.rooms
            .iter()
            .filter(|r| r.room_type == room_type)
            .collect()
    }

    /// Count rooms by type
    pub fn count_rooms(&self, room_type: RoomType) -> usize {
        self.rooms
            .iter()
            .filter(|r| r.room_type == room_type)
            .count()
    }

    /// Count all bedrooms
    pub fn bedroom_count(&self) -> usize {
        self.rooms
            .iter()
            .filter(|r| {
                matches!(
                    r.room_type,
                    RoomType::MasterSuite | RoomType::Bedroom | RoomType::GuestRoom
                )
            })
            .count()
    }

    /// Count all bathrooms (full baths = 1, half baths = 0.5)
    pub fn bathroom_count(&self) -> f32 {
        self.rooms
            .iter()
            .map(|r| match r.room_type {
                RoomType::MasterBath | RoomType::FullBath => 1.0,
                RoomType::HalfBath | RoomType::PowderRoom => 0.5,
                _ => 0.0,
            })
            .sum()
    }

    /// Recalculate overall dimensions based on rooms
    fn recalculate_dimensions(&mut self) {
        let mut max_x: f64 = 0.0;
        let mut max_y: f64 = 0.0;

        for room in &self.rooms {
            let room_end_x = room.position.x + room.length.to_inches() as f64;
            let room_end_y = room.position.y + room.width.to_inches() as f64;

            max_x = max_x.max(room_end_x);
            max_y = max_y.max(room_end_y);
        }

        self.overall_length = FeetInches::from_inches(max_x.round() as i32);
        self.overall_width = FeetInches::from_inches(max_y.round() as i32);
    }
}

/// A complete project containing multiple floor plans
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Project {
    pub id: EntityId,
    pub name: String,
    pub description: Option<String>,
    /// All floor plans in this project
    pub floor_plans: Vec<FloorPlan>,
    /// Project metadata
    pub created_at: chrono::DateTime<chrono::Utc>,
    pub updated_at: chrono::DateTime<chrono::Utc>,
    /// Project-wide settings
    pub settings: ProjectSettings,
}

impl Project {
    pub fn new(name: impl Into<String>) -> Self {
        let now = chrono::Utc::now();
        Self {
            id: new_id(),
            name: name.into(),
            description: None,
            floor_plans: Vec::new(),
            created_at: now,
            updated_at: now,
            settings: ProjectSettings::default(),
        }
    }

    /// Add a floor plan to the project
    pub fn add_floor_plan(&mut self, floor_plan: FloorPlan) -> EntityId {
        let id = floor_plan.id;
        self.floor_plans.push(floor_plan);
        self.updated_at = chrono::Utc::now();
        id
    }

    /// Get total area across all floors
    pub fn total_area(&self) -> SquareFeet {
        self.floor_plans
            .iter()
            .map(|fp| fp.total_floor_area())
            .fold(SquareFeet::default(), |a, b| a + b)
    }

    /// Get total living area across all floors
    pub fn total_living_area(&self) -> SquareFeet {
        self.floor_plans
            .iter()
            .map(|fp| fp.total_living_area())
            .fold(SquareFeet::default(), |a, b| a + b)
    }

    /// Total bedroom count
    pub fn bedroom_count(&self) -> usize {
        self.floor_plans.iter().map(|fp| fp.bedroom_count()).sum()
    }

    /// Total bathroom count
    pub fn bathroom_count(&self) -> f32 {
        self.floor_plans.iter().map(|fp| fp.bathroom_count()).sum()
    }

    /// Get floor plan by level
    pub fn get_floor_by_level(&self, level: i32) -> Option<&FloorPlan> {
        self.floor_plans.iter().find(|fp| fp.level == level)
    }
}

/// Project-wide settings
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProjectSettings {
    /// Default ceiling height for new rooms
    pub default_ceiling_height: FeetInches,
    /// Default wall type for new interior walls
    pub default_interior_wall: WallType,
    /// Default wall type for new exterior walls
    pub default_exterior_wall: WallType,
    /// Default stud spacing (in inches, typically 16 or 24)
    pub stud_spacing: u8,
    /// Region for pricing/code purposes
    pub region: String,
    /// Quality tier (affects material selections)
    pub quality_tier: QualityTier,
}

impl Default for ProjectSettings {
    fn default() -> Self {
        Self {
            default_ceiling_height: FeetInches::new(9, 0),
            default_interior_wall: WallType::InteriorPartition,
            default_exterior_wall: WallType::ExteriorLoadBearing,
            stud_spacing: 16,
            region: "US".to_string(),
            quality_tier: QualityTier::Standard,
        }
    }
}

/// Quality tier for material selections
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum QualityTier {
    Economy,
    Standard,
    Premium,
    Luxury,
}

impl Default for QualityTier {
    fn default() -> Self {
        QualityTier::Standard
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_room_creation() {
        let room = Room::new(
            "Master Bedroom",
            RoomType::MasterSuite,
            FeetInches::new(17, 8),
            FeetInches::new(22, 8),
        );

        assert_eq!(room.name, "Master Bedroom");
        assert_eq!(room.room_type, RoomType::MasterSuite);
        // 17'-8" = 17.667 ft, 22'-8" = 22.667 ft
        // 17.667 * 22.667 = 400.30 sq ft
        assert!((room.floor_area().value() - 400.30).abs() < 1.0);
    }

    #[test]
    fn test_room_perimeter() {
        let room = Room::new(
            "Office",
            RoomType::Office,
            FeetInches::new(12, 0),
            FeetInches::new(12, 0),
        );

        let perimeter = room.perimeter();
        assert!((perimeter.value() - 48.0).abs() < 0.01);
    }

    #[test]
    fn test_floor_plan_area() {
        let mut floor_plan = FloorPlan::new("Main Floor");

        floor_plan.add_room(Room::new(
            "Living Room",
            RoomType::LivingRoom,
            FeetInches::new(20, 0),
            FeetInches::new(15, 0),
        ));

        floor_plan.add_room(Room::new(
            "Kitchen",
            RoomType::Kitchen,
            FeetInches::new(15, 0),
            FeetInches::new(12, 0),
        ));

        let total = floor_plan.total_floor_area();
        assert!((total.value() - 480.0).abs() < 0.01); // 300 + 180
    }

    #[test]
    fn test_wall_length() {
        let wall = Wall::new(
            WallType::ExteriorLoadBearing,
            Point::new(0.0, 0.0),
            Point::new(120.0, 0.0), // 10 feet in inches
        );

        assert!((wall.length().value() - 10.0).abs() < 0.01);
    }

    #[test]
    fn test_project_counts() {
        let mut project = Project::new("Test House");
        let mut floor = FloorPlan::new("Main");

        floor.add_room(Room::new(
            "Master",
            RoomType::MasterSuite,
            FeetInches::new(15, 0),
            FeetInches::new(15, 0),
        ));
        floor.add_room(Room::new(
            "Bedroom 2",
            RoomType::Bedroom,
            FeetInches::new(12, 0),
            FeetInches::new(12, 0),
        ));
        floor.add_room(Room::new(
            "Master Bath",
            RoomType::MasterBath,
            FeetInches::new(10, 0),
            FeetInches::new(8, 0),
        ));
        floor.add_room(Room::new(
            "Half Bath",
            RoomType::HalfBath,
            FeetInches::new(5, 0),
            FeetInches::new(5, 0),
        ));

        project.add_floor_plan(floor);

        assert_eq!(project.bedroom_count(), 2);
        assert!((project.bathroom_count() - 1.5).abs() < 0.01);
    }
}
