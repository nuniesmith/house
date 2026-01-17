//! # SVG Renderer Module
//!
//! Provides functionality to render floor plans as SVG images for 2D visualization.
//! Supports customizable styles, colors, and annotations.

use crate::models::{Door, FloorPlan, Room, RoomType, Wall, Window};
use crate::units::FeetInches;

/// Configuration for SVG rendering
#[derive(Debug, Clone)]
pub struct RenderConfig {
    /// Pixels per foot scale factor
    pub scale: f64,
    /// Padding around the floor plan in pixels
    pub padding: f64,
    /// Wall stroke width in pixels
    pub wall_stroke_width: f64,
    /// Show room labels
    pub show_labels: bool,
    /// Show dimensions
    pub show_dimensions: bool,
    /// Show grid
    pub show_grid: bool,
    /// Grid spacing in feet
    pub grid_spacing_feet: i32,
    /// Color scheme
    pub colors: ColorScheme,
    /// Font family for labels
    pub font_family: String,
    /// Label font size in pixels
    pub label_font_size: f64,
    /// Dimension font size in pixels
    pub dimension_font_size: f64,
}

impl Default for RenderConfig {
    fn default() -> Self {
        Self {
            scale: 10.0, // 10 pixels per foot
            padding: 50.0,
            wall_stroke_width: 4.0,
            show_labels: true,
            show_dimensions: true,
            show_grid: true,
            grid_spacing_feet: 5,
            colors: ColorScheme::default(),
            font_family: "Arial, sans-serif".to_string(),
            label_font_size: 12.0,
            dimension_font_size: 10.0,
        }
    }
}

/// Color scheme for rendering
#[derive(Debug, Clone)]
pub struct ColorScheme {
    pub background: String,
    pub grid: String,
    pub exterior_wall: String,
    pub interior_wall: String,
    pub living_room: String,
    pub bedroom: String,
    pub bathroom: String,
    pub kitchen: String,
    pub utility: String,
    pub outdoor: String,
    pub garage: String,
    pub default_room: String,
    pub door: String,
    pub window: String,
    pub label_text: String,
    pub dimension_text: String,
    pub room_stroke: String,
}

impl Default for ColorScheme {
    fn default() -> Self {
        Self {
            background: "#ffffff".to_string(),
            grid: "#e0e0e0".to_string(),
            exterior_wall: "#2c3e50".to_string(),
            interior_wall: "#34495e".to_string(),
            living_room: "#fffde7".to_string(), // Light yellow
            bedroom: "#e3f2fd".to_string(),     // Light blue
            bathroom: "#e8f5e9".to_string(),    // Light green
            kitchen: "#fff3e0".to_string(),     // Light orange
            utility: "#f5f5f5".to_string(),     // Light gray
            outdoor: "#c8e6c9".to_string(),     // Green
            garage: "#eceff1".to_string(),      // Blue gray
            default_room: "#fafafa".to_string(),
            door: "#8b4513".to_string(),   // Brown
            window: "#4fc3f7".to_string(), // Light blue
            label_text: "#212121".to_string(),
            dimension_text: "#757575".to_string(),
            room_stroke: "#999999".to_string(),
        }
    }
}

impl ColorScheme {
    /// Blueprint-style dark theme
    pub fn blueprint() -> Self {
        Self {
            background: "#0f0f23".to_string(),
            grid: "#1a1a3a".to_string(),
            exterior_wall: "#00ff88".to_string(),
            interior_wall: "#00cc66".to_string(),
            living_room: "rgba(255, 255, 100, 0.15)".to_string(),
            bedroom: "rgba(100, 150, 255, 0.15)".to_string(),
            bathroom: "rgba(100, 255, 150, 0.15)".to_string(),
            kitchen: "rgba(255, 200, 100, 0.15)".to_string(),
            utility: "rgba(150, 150, 150, 0.15)".to_string(),
            outdoor: "rgba(100, 200, 150, 0.15)".to_string(),
            garage: "rgba(120, 120, 150, 0.15)".to_string(),
            default_room: "rgba(200, 200, 200, 0.1)".to_string(),
            door: "#ff6600".to_string(),
            window: "#00aaff".to_string(),
            label_text: "#00ff88".to_string(),
            dimension_text: "#888888".to_string(),
            room_stroke: "#555555".to_string(),
        }
    }

    /// Color-coded style similar to the provided floor plan image
    pub fn color_coded() -> Self {
        Self {
            background: "#ffffff".to_string(),
            grid: "#e0e0e0".to_string(),
            exterior_wall: "#1a1a1a".to_string(),
            interior_wall: "#333333".to_string(),
            living_room: "#fffde7".to_string(),  // Light yellow
            bedroom: "#bbdefb".to_string(),      // Light blue
            bathroom: "#c8e6c9".to_string(),     // Light green
            kitchen: "#ffe0b2".to_string(),      // Light orange
            utility: "#e0e0e0".to_string(),      // Gray
            outdoor: "#b2dfdb".to_string(),      // Teal
            garage: "#cfd8dc".to_string(),       // Blue gray
            default_room: "#fff9c4".to_string(), // Very light yellow
            door: "#5d4037".to_string(),         // Brown
            window: "#29b6f6".to_string(),       // Blue
            label_text: "#212121".to_string(),
            dimension_text: "#616161".to_string(),
            room_stroke: "#666666".to_string(),
        }
    }
}

/// SVG Renderer for floor plans
pub struct SvgRenderer {
    config: RenderConfig,
}

impl SvgRenderer {
    /// Create a new SVG renderer with default config
    pub fn new() -> Self {
        Self {
            config: RenderConfig::default(),
        }
    }

    /// Create a new SVG renderer with custom config
    pub fn with_config(config: RenderConfig) -> Self {
        Self { config }
    }

    /// Get room fill color based on room type
    fn room_color(&self, room_type: &RoomType) -> &str {
        match room_type {
            RoomType::LivingRoom
            | RoomType::FamilyRoom
            | RoomType::GreatRoom
            | RoomType::Lounge
            | RoomType::Foyer
            | RoomType::Hallway => &self.config.colors.living_room,

            RoomType::MasterSuite | RoomType::Bedroom | RoomType::GuestRoom | RoomType::Nursery => {
                &self.config.colors.bedroom
            }

            RoomType::MasterBath
            | RoomType::FullBath
            | RoomType::HalfBath
            | RoomType::PowderRoom => &self.config.colors.bathroom,

            RoomType::Kitchen | RoomType::DiningRoom | RoomType::BreakfastNook | RoomType::Bar => {
                &self.config.colors.kitchen
            }

            RoomType::Pantry
            | RoomType::ButlersPantry
            | RoomType::Laundry
            | RoomType::MudRoom
            | RoomType::Utility
            | RoomType::Storage
            | RoomType::Closet
            | RoomType::WalkInCloset => &self.config.colors.utility,

            RoomType::Porch
            | RoomType::Deck
            | RoomType::Patio
            | RoomType::Sunroom
            | RoomType::Screened => &self.config.colors.outdoor,

            RoomType::Garage | RoomType::Carport | RoomType::Workshop => &self.config.colors.garage,

            _ => &self.config.colors.default_room,
        }
    }

    /// Convert feet to pixels
    fn feet_to_px(&self, feet: f64) -> f64 {
        feet * self.config.scale
    }

    /// Convert FeetInches to pixels
    fn fi_to_px(&self, fi: &FeetInches) -> f64 {
        self.feet_to_px(fi.to_decimal_feet())
    }

    /// Render a complete floor plan to SVG string
    pub fn render(&self, floor_plan: &FloorPlan) -> String {
        let width = self.fi_to_px(&floor_plan.overall_length) + self.config.padding * 2.0;
        let height = self.fi_to_px(&floor_plan.overall_width) + self.config.padding * 2.0;

        let mut svg = format!(
            r#"<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}" viewBox="0 0 {} {}">"#,
            width, height, width, height
        );

        // Add styles
        svg.push_str(&self.render_styles());

        // Background
        svg.push_str(&format!(
            r#"<rect width="100%" height="100%" fill="{}"/>"#,
            self.config.colors.background
        ));

        // Grid
        if self.config.show_grid {
            svg.push_str(&self.render_grid(width, height));
        }

        // Rooms
        for room in &floor_plan.rooms {
            svg.push_str(&self.render_room(room));
        }

        // Walls
        for wall in &floor_plan.walls {
            svg.push_str(&self.render_wall(wall));
        }

        // Close SVG
        svg.push_str("</svg>");
        svg
    }

    /// Render CSS styles for SVG
    fn render_styles(&self) -> String {
        format!(
            r#"
<style>
    .room-label {{
        font-family: {};
        font-size: {}px;
        font-weight: bold;
        text-anchor: middle;
        fill: {};
    }}
    .dimension {{
        font-family: {};
        font-size: {}px;
        text-anchor: middle;
        fill: {};
    }}
    .exterior-wall {{
        stroke: {};
        stroke-width: {};
        fill: none;
    }}
    .interior-wall {{
        stroke: {};
        stroke-width: {};
        fill: none;
    }}
    .door {{
        stroke: {};
        stroke-width: 2;
        fill: none;
    }}
    .window {{
        stroke: {};
        stroke-width: 3;
    }}
</style>
"#,
            self.config.font_family,
            self.config.label_font_size,
            self.config.colors.label_text,
            self.config.font_family,
            self.config.dimension_font_size,
            self.config.colors.dimension_text,
            self.config.colors.exterior_wall,
            self.config.wall_stroke_width,
            self.config.colors.interior_wall,
            self.config.wall_stroke_width * 0.75,
            self.config.colors.door,
            self.config.colors.window,
        )
    }

    /// Render the grid
    fn render_grid(&self, width: f64, height: f64) -> String {
        let spacing = self.feet_to_px(self.config.grid_spacing_feet as f64);
        let mut grid = String::new();

        grid.push_str(&format!(
            r#"<defs><pattern id="grid" width="{}" height="{}" patternUnits="userSpaceOnUse">"#,
            spacing, spacing
        ));
        grid.push_str(&format!(
            r#"<path d="M {} 0 L 0 0 0 {}" fill="none" stroke="{}" stroke-width="0.5"/>"#,
            spacing, spacing, self.config.colors.grid
        ));
        grid.push_str("</pattern></defs>");
        grid.push_str(&format!(
            r#"<rect width="{}" height="{}" fill="url(#grid)"/>"#,
            width, height
        ));

        grid
    }

    /// Render a room
    fn render_room(&self, room: &Room) -> String {
        let x = self.fi_to_px(&room.position.x_feet_inches()) + self.config.padding;
        let y = self.fi_to_px(&room.position.y_feet_inches()) + self.config.padding;
        let w = self.fi_to_px(&room.length);
        let h = self.fi_to_px(&room.width);
        let fill = self.room_color(&room.room_type);

        let mut svg = format!(
            r#"<rect x="{}" y="{}" width="{}" height="{}" fill="{}" stroke="{}" stroke-width="1"/>"#,
            x, y, w, h, fill, self.config.colors.room_stroke
        );

        if self.config.show_labels {
            let cx = x + w / 2.0;
            let cy = y + h / 2.0;

            svg.push_str(&format!(
                r#"<text x="{}" y="{}" class="room-label">{}</text>"#,
                cx,
                cy - 5.0,
                room.name.to_uppercase()
            ));

            if self.config.show_dimensions {
                svg.push_str(&format!(
                    r#"<text x="{}" y="{}" class="dimension">{} x {}</text>"#,
                    cx,
                    cy + 12.0,
                    room.length.to_arch_string(),
                    room.width.to_arch_string()
                ));
            }
        }

        svg
    }

    /// Render a wall
    fn render_wall(&self, wall: &Wall) -> String {
        let x1 = self.feet_to_px(wall.start.x) + self.config.padding;
        let y1 = self.feet_to_px(wall.start.y) + self.config.padding;
        let x2 = self.feet_to_px(wall.end.x) + self.config.padding;
        let y2 = self.feet_to_px(wall.end.y) + self.config.padding;

        let class = if wall.wall_type.is_exterior() {
            "exterior-wall"
        } else {
            "interior-wall"
        };

        let mut svg = format!(
            r#"<line x1="{}" y1="{}" x2="{}" y2="{}" class="{}"/>"#,
            x1, y1, x2, y2, class
        );

        // Render doors on this wall
        for door in &wall.doors {
            svg.push_str(&self.render_door(door, wall));
        }

        // Render windows on this wall
        for window in &wall.windows {
            svg.push_str(&self.render_window(window, wall));
        }

        svg
    }

    /// Render a door
    fn render_door(&self, door: &Door, wall: &Wall) -> String {
        let wall_start_x = self.feet_to_px(wall.start.x) + self.config.padding;
        let wall_start_y = self.feet_to_px(wall.start.y) + self.config.padding;
        let wall_end_x = self.feet_to_px(wall.end.x) + self.config.padding;
        let wall_end_y = self.feet_to_px(wall.end.y) + self.config.padding;

        let wall_length = wall.length().value();
        let t = if wall_length > 0.0 {
            door.position.to_decimal_feet() / wall_length
        } else {
            0.0
        };
        let door_x = wall_start_x + (wall_end_x - wall_start_x) * t;
        let door_y = wall_start_y + (wall_end_y - wall_start_y) * t;
        let door_width = self.fi_to_px(&door.width);

        // Determine wall orientation
        let is_horizontal = (wall_start_y - wall_end_y).abs() < 0.1;

        if is_horizontal {
            // Door on horizontal wall - draw swing arc
            format!(
                r#"<path d="M {} {} A {} {} 0 0 1 {} {}" class="door"/>"#,
                door_x,
                door_y,
                door_width,
                door_width,
                door_x + door_width,
                door_y + door_width
            )
        } else {
            // Door on vertical wall
            format!(
                r#"<path d="M {} {} A {} {} 0 0 1 {} {}" class="door"/>"#,
                door_x,
                door_y,
                door_width,
                door_width,
                door_x + door_width,
                door_y + door_width
            )
        }
    }

    /// Render a window
    fn render_window(&self, window: &Window, wall: &Wall) -> String {
        let wall_start_x = self.feet_to_px(wall.start.x) + self.config.padding;
        let wall_start_y = self.feet_to_px(wall.start.y) + self.config.padding;
        let wall_end_x = self.feet_to_px(wall.end.x) + self.config.padding;
        let wall_end_y = self.feet_to_px(wall.end.y) + self.config.padding;

        let wall_length = wall.length().value();
        let t = if wall_length > 0.0 {
            window.position.to_decimal_feet() / wall_length
        } else {
            0.0
        };
        let window_x = wall_start_x + (wall_end_x - wall_start_x) * t;
        let window_y = wall_start_y + (wall_end_y - wall_start_y) * t;
        let window_width = self.fi_to_px(&window.width);

        let is_horizontal = (wall_start_y - wall_end_y).abs() < 0.1;

        if is_horizontal {
            format!(
                r#"<line x1="{}" y1="{}" x2="{}" y2="{}" class="window"/>"#,
                window_x,
                window_y,
                window_x + window_width,
                window_y
            )
        } else {
            format!(
                r#"<line x1="{}" y1="{}" x2="{}" y2="{}" class="window"/>"#,
                window_x,
                window_y,
                window_x,
                window_y + window_width
            )
        }
    }

    /// Render to a standalone HTML file with the SVG embedded
    pub fn render_html(&self, floor_plan: &FloorPlan, title: &str) -> String {
        let svg = self.render(floor_plan);
        format!(
            r#"<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}</title>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
            font-family: Arial, sans-serif;
        }}
        .container {{
            max-width: 100%;
            overflow-x: auto;
        }}
        h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .info {{
            color: #666;
            margin-bottom: 20px;
        }}
        svg {{
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <h1>{}</h1>
    <div class="info">
        Total Area: {:.0} sq ft | Rooms: {} | Level: {}
    </div>
    <div class="container">
        {}
    </div>
</body>
</html>"#,
            title,
            title,
            floor_plan.total_floor_area().0,
            floor_plan.rooms.len(),
            floor_plan.level,
            svg
        )
    }
}

impl Default for SvgRenderer {
    fn default() -> Self {
        Self::new()
    }
}

/// Builder for creating floor plans programmatically with a fluent API
pub struct FloorPlanBuilder {
    name: String,
    description: Option<String>,
    level: i32,
    rooms: Vec<Room>,
    walls: Vec<Wall>,
}

impl FloorPlanBuilder {
    /// Create a new floor plan builder
    pub fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
            description: None,
            level: 1,
            rooms: Vec::new(),
            walls: Vec::new(),
        }
    }

    /// Set the description
    pub fn description(mut self, desc: &str) -> Self {
        self.description = Some(desc.to_string());
        self
    }

    /// Set the level/floor number
    pub fn level(mut self, level: i32) -> Self {
        self.level = level;
        self
    }

    /// Add a room at a specific position
    pub fn room(
        mut self,
        name: &str,
        room_type: RoomType,
        x: f64,
        y: f64,
        length_ft: i32,
        length_in: i32,
        width_ft: i32,
        width_in: i32,
    ) -> Self {
        let length = FeetInches::new(length_ft, length_in);
        let width = FeetInches::new(width_ft, width_in);

        let mut room = Room::new(name.to_string(), room_type, length, width);
        room.position = crate::models::Point::new(x, y);

        self.rooms.push(room);
        self
    }

    /// Add a room using the simpler dimension string format "14'-6"" x "12'-0""
    pub fn room_str(
        mut self,
        name: &str,
        room_type: RoomType,
        x: f64,
        y: f64,
        length: &str,
        width: &str,
    ) -> Self {
        let length = FeetInches::parse(length).unwrap_or_default();
        let width = FeetInches::parse(width).unwrap_or_default();

        let mut room = Room::new(name.to_string(), room_type, length, width);
        room.position = crate::models::Point::new(x, y);

        self.rooms.push(room);
        self
    }

    /// Add an exterior wall
    pub fn exterior_wall(mut self, x1: f64, y1: f64, x2: f64, y2: f64) -> Self {
        let wall = Wall::new(
            crate::models::WallType::ExteriorLoadBearing,
            crate::models::Point::new(x1, y1),
            crate::models::Point::new(x2, y2),
        );
        self.walls.push(wall);
        self
    }

    /// Add an interior wall
    pub fn interior_wall(mut self, x1: f64, y1: f64, x2: f64, y2: f64) -> Self {
        let wall = Wall::new(
            crate::models::WallType::InteriorPartition,
            crate::models::Point::new(x1, y1),
            crate::models::Point::new(x2, y2),
        );
        self.walls.push(wall);
        self
    }

    /// Build the floor plan
    pub fn build(self) -> FloorPlan {
        let mut plan = FloorPlan::new(self.name);
        plan.description = self.description;
        plan.level = self.level;

        for room in self.rooms {
            plan.add_room(room);
        }

        for wall in self.walls {
            plan.add_wall(wall);
        }

        plan
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_render_config_default() {
        let config = RenderConfig::default();
        assert_eq!(config.scale, 10.0);
        assert!(config.show_labels);
        assert!(config.show_dimensions);
    }

    #[test]
    fn test_color_scheme_blueprint() {
        let colors = ColorScheme::blueprint();
        assert_eq!(colors.background, "#0f0f23");
    }

    #[test]
    fn test_floor_plan_builder() {
        let plan = FloorPlanBuilder::new("Test Plan")
            .level(1)
            .description("Test description")
            .room("Living Room", RoomType::LivingRoom, 0.0, 0.0, 20, 0, 15, 0)
            .room("Kitchen", RoomType::Kitchen, 20.0, 0.0, 15, 0, 12, 0)
            .build();

        assert_eq!(plan.name, "Test Plan");
        assert_eq!(plan.rooms.len(), 2);
    }

    #[test]
    fn test_room_str_parsing() {
        let plan = FloorPlanBuilder::new("Test")
            .room_str(
                "Master",
                RoomType::MasterSuite,
                0.0,
                0.0,
                "17'-8\"",
                "22'-8\"",
            )
            .build();

        assert_eq!(plan.rooms.len(), 1);
        let room = &plan.rooms[0];
        assert_eq!(room.length.feet, 17);
        assert_eq!(room.length.inches, 8);
    }

    #[test]
    fn test_svg_renderer() {
        let plan = FloorPlanBuilder::new("Simple Plan")
            .room("Room 1", RoomType::Bedroom, 0.0, 0.0, 12, 0, 10, 0)
            .build();

        let renderer = SvgRenderer::new();
        let svg = renderer.render(&plan);

        assert!(svg.contains("<svg"));
        assert!(svg.contains("ROOM 1"));
        assert!(svg.contains("</svg>"));
    }
}
