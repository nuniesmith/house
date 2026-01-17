//! # Floor Plan Renderer CLI
//!
//! Command-line tool to generate SVG images from floor plan definitions.
//!
//! Usage:
//!   render_floorplan [OPTIONS]
//!
//! Examples:
//!   render_floorplan                          # Render luxury farmhouse with default settings
//!   render_floorplan --output my_plan.html    # Save to specific file
//!   render_floorplan --style blueprint        # Use blueprint color scheme
//!   render_floorplan --scale 15               # Larger scale (15 pixels per foot)
//!   render_floorplan --svg-only               # Output raw SVG instead of HTML
//!   render_floorplan --input plan.json        # Load floor plan from JSON file

use floorplan_core::{
    calculate_living_sqft, calculate_total_sqft, create_luxury_farmhouse_detailed,
    get_luxury_farmhouse_rooms, ColorScheme, FloorPlanDefinition, RenderConfig, SvgRenderer,
};
use std::env;
use std::fs;
use std::io::{self, Write};

fn print_help() {
    eprintln!(
        r#"Floor Plan Renderer - Generate SVG images from floor plan definitions

USAGE:
    render_floorplan [OPTIONS]

OPTIONS:
    -i, --input <FILE>      Load floor plan from JSON file (default: built-in luxury farmhouse)
    -o, --output <FILE>     Output file path (default: stdout)
    -s, --style <STYLE>     Color scheme: default, blueprint, color-coded
    --scale <SCALE>         Pixels per foot (default: 10)
    --no-grid               Hide grid lines
    --no-labels             Hide room labels
    --no-dimensions         Hide room dimensions
    --svg-only              Output raw SVG (default: HTML with embedded SVG)
    --info                  Show floor plan information and exit
    --example-json          Output example JSON format and exit
    -h, --help              Show this help message

EXAMPLES:
    render_floorplan --output farmhouse.html
    render_floorplan --style blueprint --scale 12 -o blueprint.html
    render_floorplan --svg-only > floorplan.svg
    render_floorplan --info
    render_floorplan --input my_plan.json --output my_plan.html
    render_floorplan --example-json > template.json
"#
    );
}

fn print_info() {
    let rooms = get_luxury_farmhouse_rooms();
    let total_sqft = calculate_total_sqft(&rooms);
    let living_sqft = calculate_living_sqft(&rooms);

    println!("Luxury Farmhouse Floor Plan");
    println!("===========================");
    println!();
    println!("Total Square Footage: {:.0} sq ft", total_sqft);
    println!("Living Area: {:.0} sq ft", living_sqft);
    println!("Total Rooms: {}", rooms.len());
    println!();
    println!("Room List:");
    println!("-----------");

    for room in &rooms {
        let ceiling_info = room
            .ceiling_height
            .as_ref()
            .map(|c| format!(" ({})", c))
            .unwrap_or_default();
        println!(
            "  {:20} {:10} x {:10}{}",
            room.name, room.length, room.width, ceiling_info
        );
    }

    println!();
    println!("Room Types Summary:");
    println!("-------------------");

    let bedrooms = rooms
        .iter()
        .filter(|r| {
            matches!(
                r.room_type,
                floorplan_core::RoomType::Bedroom
                    | floorplan_core::RoomType::MasterSuite
                    | floorplan_core::RoomType::GuestRoom
            )
        })
        .count();

    let bathrooms = rooms
        .iter()
        .filter(|r| {
            matches!(
                r.room_type,
                floorplan_core::RoomType::FullBath
                    | floorplan_core::RoomType::HalfBath
                    | floorplan_core::RoomType::MasterBath
                    | floorplan_core::RoomType::PowderRoom
            )
        })
        .count();

    println!("  Bedrooms: {}", bedrooms);
    println!("  Bathrooms: {}", bathrooms);
}

fn print_example_json() {
    let example = floorplan_core::example_floor_plan_json();
    println!("{}", example);
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let mut input_file: Option<String> = None;
    let mut output_file: Option<String> = None;
    let mut style = "default";
    let mut scale = 10.0;
    let mut show_grid = true;
    let mut show_labels = true;
    let mut show_dimensions = true;
    let mut svg_only = false;

    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "-h" | "--help" => {
                print_help();
                return;
            }
            "--info" => {
                print_info();
                return;
            }
            "--example-json" => {
                print_example_json();
                return;
            }
            "-i" | "--input" => {
                i += 1;
                if i < args.len() {
                    input_file = Some(args[i].clone());
                } else {
                    eprintln!("Error: --input requires a file path");
                    std::process::exit(1);
                }
            }
            "-o" | "--output" => {
                i += 1;
                if i < args.len() {
                    output_file = Some(args[i].clone());
                } else {
                    eprintln!("Error: --output requires a file path");
                    std::process::exit(1);
                }
            }
            "-s" | "--style" => {
                i += 1;
                if i < args.len() {
                    style = match args[i].as_str() {
                        "default" | "blueprint" | "color-coded" => &args[i],
                        _ => {
                            eprintln!(
                                "Error: Unknown style '{}'. Use: default, blueprint, color-coded",
                                args[i]
                            );
                            std::process::exit(1);
                        }
                    };
                } else {
                    eprintln!("Error: --style requires a style name");
                    std::process::exit(1);
                }
            }
            "--scale" => {
                i += 1;
                if i < args.len() {
                    scale = args[i].parse().unwrap_or_else(|_| {
                        eprintln!("Error: Invalid scale value");
                        std::process::exit(1);
                    });
                } else {
                    eprintln!("Error: --scale requires a number");
                    std::process::exit(1);
                }
            }
            "--no-grid" => show_grid = false,
            "--no-labels" => show_labels = false,
            "--no-dimensions" => show_dimensions = false,
            "--svg-only" => svg_only = true,
            _ => {
                eprintln!("Unknown option: {}", args[i]);
                eprintln!("Use --help for usage information");
                std::process::exit(1);
            }
        }
        i += 1;
    }

    // Configure renderer
    let colors = match style {
        "blueprint" => ColorScheme::blueprint(),
        "color-coded" => ColorScheme::color_coded(),
        _ => ColorScheme::default(),
    };

    let config = RenderConfig {
        scale,
        show_grid,
        show_labels,
        show_dimensions,
        colors,
        ..Default::default()
    };

    let renderer = SvgRenderer::with_config(config);

    // Load or create the floor plan
    let floor_plan = match input_file {
        Some(path) => {
            let json = fs::read_to_string(&path).unwrap_or_else(|e| {
                eprintln!("Error reading {}: {}", path, e);
                std::process::exit(1);
            });

            let definition = FloorPlanDefinition::from_json(&json).unwrap_or_else(|e| {
                eprintln!("Error parsing JSON from {}: {}", path, e);
                std::process::exit(1);
            });

            eprintln!("Loaded floor plan: {}", definition.name);
            definition.to_floor_plan()
        }
        None => {
            eprintln!("Using built-in Luxury Farmhouse floor plan");
            create_luxury_farmhouse_detailed()
        }
    };

    // Get title for HTML
    let title = format!("{} - Floor Plan", floor_plan.name);

    // Render
    let output = if svg_only {
        renderer.render(&floor_plan)
    } else {
        renderer.render_html(&floor_plan, &title)
    };

    // Write output
    match output_file {
        Some(path) => {
            fs::write(&path, &output).unwrap_or_else(|e| {
                eprintln!("Error writing to {}: {}", path, e);
                std::process::exit(1);
            });
            eprintln!("Floor plan saved to: {}", path);
        }
        None => {
            io::stdout()
                .write_all(output.as_bytes())
                .unwrap_or_else(|e| {
                    eprintln!("Error writing to stdout: {}", e);
                    std::process::exit(1);
                });
        }
    }
}
