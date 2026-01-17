//! # Floorplan Backend Server
//!
//! Axum-based web server providing REST API for floor plan design
//! and material calculations.

use std::sync::Arc;

use axum::{
    extract::{Path, State},
    http::{header, Method, StatusCode},
    response::{IntoResponse, Json},
    routing::{get, post},
    Router,
};
use serde::{Deserialize, Serialize};
use tokio::sync::RwLock;
use tower_http::{
    cors::{Any, CorsLayer},
    services::ServeDir,
    trace::TraceLayer,
};
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};
use uuid::Uuid;

use floorplan_core::{
    calculations::{CalculationConfig, CalculationResult, ProjectCalculator},
    materials::{all_standard_materials, Material, MaterialCategory},
    models::{FloorPlan, Point, Project, QualityTier, Room, RoomType, Wall, WallType},
    units::{CeilingHeight, FeetInches},
};

/// Application state shared across handlers
#[derive(Debug, Default)]
pub struct AppState {
    /// All projects in memory
    projects: RwLock<Vec<Project>>,
}

impl AppState {
    pub fn new() -> Self {
        Self {
            projects: RwLock::new(Vec::new()),
        }
    }

    /// Create with sample data
    pub fn with_sample_data() -> Self {
        let state = Self::new();
        // Sample data will be added via API
        state
    }
}

type SharedState = Arc<AppState>;

// ============================================================================
// API Response Types
// ============================================================================

#[derive(Debug, Serialize)]
pub struct ApiResponse<T> {
    pub success: bool,
    pub data: Option<T>,
    pub error: Option<String>,
}

impl<T: Serialize> ApiResponse<T> {
    pub fn success(data: T) -> Json<Self> {
        Json(Self {
            success: true,
            data: Some(data),
            error: None,
        })
    }

    pub fn error(message: impl Into<String>) -> Json<Self> {
        Json(Self {
            success: false,
            data: None,
            error: Some(message.into()),
        })
    }
}

// ============================================================================
// Request/Response DTOs
// ============================================================================

#[derive(Debug, Deserialize)]
pub struct CreateProjectRequest {
    pub name: String,
    pub description: Option<String>,
}

#[derive(Debug, Deserialize)]
pub struct CreateFloorPlanRequest {
    pub name: String,
    pub level: Option<i32>,
}

#[derive(Debug, Deserialize)]
pub struct CreateRoomRequest {
    pub name: String,
    pub room_type: RoomType,
    pub length_feet: i32,
    pub length_inches: i32,
    pub width_feet: i32,
    pub width_inches: i32,
    pub position_x: Option<f64>,
    pub position_y: Option<f64>,
    pub ceiling_height_feet: Option<i32>,
    pub ceiling_height_inches: Option<i32>,
}

#[derive(Debug, Deserialize)]
pub struct CreateWallRequest {
    pub wall_type: WallType,
    pub start_x: f64,
    pub start_y: f64,
    pub end_x: f64,
    pub end_y: f64,
}

#[derive(Debug, Deserialize)]
pub struct CalculateRequest {
    pub quality_tier: Option<QualityTier>,
    pub include_waste: Option<bool>,
    pub stud_spacing: Option<u8>,
}

#[derive(Debug, Serialize)]
pub struct ProjectSummary {
    pub id: Uuid,
    pub name: String,
    pub description: Option<String>,
    pub floor_count: usize,
    pub total_sqft: f64,
    pub bedroom_count: usize,
    pub bathroom_count: f32,
    pub created_at: chrono::DateTime<chrono::Utc>,
    pub updated_at: chrono::DateTime<chrono::Utc>,
}

impl From<&Project> for ProjectSummary {
    fn from(p: &Project) -> Self {
        Self {
            id: p.id,
            name: p.name.clone(),
            description: p.description.clone(),
            floor_count: p.floor_plans.len(),
            total_sqft: p.total_living_area().value(),
            bedroom_count: p.bedroom_count(),
            bathroom_count: p.bathroom_count(),
            created_at: p.created_at,
            updated_at: p.updated_at,
        }
    }
}

#[derive(Debug, Serialize)]
pub struct CalculationSummary {
    pub description: String,
    pub total_cost: f64,
    pub cost_per_sqft: Option<f64>,
    pub item_count: usize,
    pub notes: Vec<String>,
}

impl From<&CalculationResult> for CalculationSummary {
    fn from(r: &CalculationResult) -> Self {
        Self {
            description: r.description.clone(),
            total_cost: r.total_cost,
            cost_per_sqft: r.cost_per_sqft,
            item_count: r.materials.items.len(),
            notes: r.notes.clone(),
        }
    }
}

#[derive(Debug, Serialize)]
pub struct MaterialSummary {
    pub id: String,
    pub name: String,
    pub category: MaterialCategory,
    pub unit: String,
    pub price_economy: f64,
    pub price_standard: f64,
    pub price_premium: f64,
    pub price_luxury: f64,
}

impl From<&Material> for MaterialSummary {
    fn from(m: &Material) -> Self {
        Self {
            id: m.id.clone(),
            name: m.name.clone(),
            category: m.category,
            unit: m.unit.abbreviation().to_string(),
            price_economy: m.price_economy,
            price_standard: m.price_standard,
            price_premium: m.price_premium,
            price_luxury: m.price_luxury,
        }
    }
}

// ============================================================================
// API Handlers
// ============================================================================

/// Health check endpoint
async fn health_check() -> impl IntoResponse {
    Json(serde_json::json!({
        "status": "healthy",
        "version": env!("CARGO_PKG_VERSION"),
    }))
}

/// Get all projects
async fn list_projects(State(state): State<SharedState>) -> impl IntoResponse {
    let projects = state.projects.read().await;
    let summaries: Vec<ProjectSummary> = projects.iter().map(ProjectSummary::from).collect();
    ApiResponse::success(summaries)
}

/// Create a new project
async fn create_project(
    State(state): State<SharedState>,
    Json(req): Json<CreateProjectRequest>,
) -> impl IntoResponse {
    let mut project = Project::new(req.name);
    project.description = req.description;

    let summary = ProjectSummary::from(&project);

    let mut projects = state.projects.write().await;
    projects.push(project);

    (StatusCode::CREATED, ApiResponse::success(summary))
}

/// Get a specific project
async fn get_project(
    State(state): State<SharedState>,
    Path(project_id): Path<Uuid>,
) -> impl IntoResponse {
    let projects = state.projects.read().await;

    if let Some(project) = projects.iter().find(|p| p.id == project_id) {
        ApiResponse::success(project.clone())
    } else {
        ApiResponse::<Project>::error("Project not found")
    }
}

/// Delete a project
async fn delete_project(
    State(state): State<SharedState>,
    Path(project_id): Path<Uuid>,
) -> impl IntoResponse {
    let mut projects = state.projects.write().await;

    if let Some(pos) = projects.iter().position(|p| p.id == project_id) {
        projects.remove(pos);
        ApiResponse::success(serde_json::json!({"deleted": true}))
    } else {
        ApiResponse::<serde_json::Value>::error("Project not found")
    }
}

/// Add a floor plan to a project
async fn add_floor_plan(
    State(state): State<SharedState>,
    Path(project_id): Path<Uuid>,
    Json(req): Json<CreateFloorPlanRequest>,
) -> impl IntoResponse {
    let mut projects = state.projects.write().await;

    if let Some(project) = projects.iter_mut().find(|p| p.id == project_id) {
        let mut floor_plan = FloorPlan::new(req.name);
        floor_plan.level = req.level.unwrap_or(0);

        let _floor_id = project.add_floor_plan(floor_plan.clone());

        (StatusCode::CREATED, ApiResponse::success(floor_plan))
    } else {
        (
            StatusCode::NOT_FOUND,
            ApiResponse::<FloorPlan>::error("Project not found"),
        )
    }
}

/// Get floor plans for a project
async fn get_floor_plans(
    State(state): State<SharedState>,
    Path(project_id): Path<Uuid>,
) -> impl IntoResponse {
    let projects = state.projects.read().await;

    if let Some(project) = projects.iter().find(|p| p.id == project_id) {
        ApiResponse::success(project.floor_plans.clone())
    } else {
        ApiResponse::<Vec<FloorPlan>>::error("Project not found")
    }
}

/// Add a room to a floor plan
async fn add_room(
    State(state): State<SharedState>,
    Path((project_id, floor_id)): Path<(Uuid, Uuid)>,
    Json(req): Json<CreateRoomRequest>,
) -> impl IntoResponse {
    let mut projects = state.projects.write().await;

    if let Some(project) = projects.iter_mut().find(|p| p.id == project_id) {
        if let Some(floor) = project.floor_plans.iter_mut().find(|f| f.id == floor_id) {
            let length = FeetInches::new(req.length_feet, req.length_inches);
            let width = FeetInches::new(req.width_feet, req.width_inches);

            let mut room = Room::new(req.name, req.room_type, length, width);

            if let (Some(x), Some(y)) = (req.position_x, req.position_y) {
                room.position = Point::new(x, y);
            }

            if let (Some(feet), Some(inches)) = (req.ceiling_height_feet, req.ceiling_height_inches)
            {
                room.ceiling = CeilingHeight::Standard(FeetInches::new(feet, inches));
            }

            let room_clone = room.clone();
            floor.add_room(room);

            return (StatusCode::CREATED, ApiResponse::success(room_clone));
        }
        return (
            StatusCode::NOT_FOUND,
            ApiResponse::<Room>::error("Floor plan not found"),
        );
    }
    (
        StatusCode::NOT_FOUND,
        ApiResponse::<Room>::error("Project not found"),
    )
}

/// Get rooms for a floor plan
async fn get_rooms(
    State(state): State<SharedState>,
    Path((project_id, floor_id)): Path<(Uuid, Uuid)>,
) -> impl IntoResponse {
    let projects = state.projects.read().await;

    if let Some(project) = projects.iter().find(|p| p.id == project_id) {
        if let Some(floor) = project.floor_plans.iter().find(|f| f.id == floor_id) {
            return ApiResponse::success(floor.rooms.clone());
        }
        return ApiResponse::<Vec<Room>>::error("Floor plan not found");
    }
    ApiResponse::<Vec<Room>>::error("Project not found")
}

/// Add a wall to a floor plan
async fn add_wall(
    State(state): State<SharedState>,
    Path((project_id, floor_id)): Path<(Uuid, Uuid)>,
    Json(req): Json<CreateWallRequest>,
) -> impl IntoResponse {
    let mut projects = state.projects.write().await;

    if let Some(project) = projects.iter_mut().find(|p| p.id == project_id) {
        if let Some(floor) = project.floor_plans.iter_mut().find(|f| f.id == floor_id) {
            let wall = Wall::new(
                req.wall_type,
                Point::new(req.start_x, req.start_y),
                Point::new(req.end_x, req.end_y),
            );

            let wall_clone = wall.clone();
            floor.add_wall(wall);

            return (StatusCode::CREATED, ApiResponse::success(wall_clone));
        }
        return (
            StatusCode::NOT_FOUND,
            ApiResponse::<Wall>::error("Floor plan not found"),
        );
    }
    (
        StatusCode::NOT_FOUND,
        ApiResponse::<Wall>::error("Project not found"),
    )
}

/// Calculate materials for a project
async fn calculate_project_materials(
    State(state): State<SharedState>,
    Path(project_id): Path<Uuid>,
    Json(req): Json<CalculateRequest>,
) -> impl IntoResponse {
    let projects = state.projects.read().await;

    if let Some(project) = projects.iter().find(|p| p.id == project_id) {
        let mut config = CalculationConfig::default();
        if let Some(tier) = req.quality_tier {
            config.quality_tier = tier;
        }
        if let Some(waste) = req.include_waste {
            config.include_waste = waste;
        }
        if let Some(spacing) = req.stud_spacing {
            config.stud_spacing = spacing;
        }

        let results = ProjectCalculator::calculate_project(project, &config);
        let summaries: Vec<CalculationSummary> =
            results.iter().map(CalculationSummary::from).collect();

        let total_cost: f64 = results.iter().map(|r| r.total_cost).sum();
        let total_sqft = project.total_living_area().value();

        ApiResponse::success(serde_json::json!({
            "project_id": project_id,
            "project_name": project.name,
            "quality_tier": config.quality_tier,
            "total_cost": total_cost,
            "total_sqft": total_sqft,
            "cost_per_sqft": if total_sqft > 0.0 { total_cost / total_sqft } else { 0.0 },
            "categories": summaries,
        }))
    } else {
        ApiResponse::<serde_json::Value>::error("Project not found")
    }
}

/// Calculate materials for a specific floor plan
async fn calculate_floor_materials(
    State(state): State<SharedState>,
    Path((project_id, floor_id)): Path<(Uuid, Uuid)>,
    Json(req): Json<CalculateRequest>,
) -> impl IntoResponse {
    let projects = state.projects.read().await;

    if let Some(project) = projects.iter().find(|p| p.id == project_id) {
        if let Some(floor) = project.floor_plans.iter().find(|f| f.id == floor_id) {
            let mut config = CalculationConfig::default();
            if let Some(tier) = req.quality_tier {
                config.quality_tier = tier;
            }
            if let Some(waste) = req.include_waste {
                config.include_waste = waste;
            }
            if let Some(spacing) = req.stud_spacing {
                config.stud_spacing = spacing;
            }

            let results = ProjectCalculator::calculate_floor_plan(floor, &config);
            let summaries: Vec<CalculationSummary> =
                results.iter().map(CalculationSummary::from).collect();

            let total_cost: f64 = results.iter().map(|r| r.total_cost).sum();
            let total_sqft = floor.total_living_area().value();

            return ApiResponse::success(serde_json::json!({
                "floor_id": floor_id,
                "floor_name": floor.name,
                "quality_tier": config.quality_tier,
                "total_cost": total_cost,
                "total_sqft": total_sqft,
                "cost_per_sqft": if total_sqft > 0.0 { total_cost / total_sqft } else { 0.0 },
                "categories": summaries,
            }));
        }
        return ApiResponse::<serde_json::Value>::error("Floor plan not found");
    }
    ApiResponse::<serde_json::Value>::error("Project not found")
}

/// Get all available materials
async fn list_materials() -> impl IntoResponse {
    let materials = all_standard_materials();
    let summaries: Vec<MaterialSummary> = materials.iter().map(MaterialSummary::from).collect();
    ApiResponse::success(summaries)
}

/// Get materials by category
async fn list_materials_by_category(Path(category): Path<String>) -> impl IntoResponse {
    let category = match category.to_lowercase().as_str() {
        "lumber" => MaterialCategory::Lumber,
        "sheetgoods" | "sheet_goods" => MaterialCategory::SheetGoods,
        "flooring" => MaterialCategory::Flooring,
        "roofing" => MaterialCategory::Roofing,
        "insulation" => MaterialCategory::Insulation,
        "electrical" => MaterialCategory::Electrical,
        "plumbing" => MaterialCategory::Plumbing,
        "hvac" => MaterialCategory::Hvac,
        "doors" => MaterialCategory::Doors,
        "windows" => MaterialCategory::Windows,
        "trim" => MaterialCategory::Trim,
        "paint" => MaterialCategory::Paint,
        "hardware" => MaterialCategory::Hardware,
        "concrete" => MaterialCategory::Concrete,
        "fasteners" => MaterialCategory::Fasteners,
        "siding" => MaterialCategory::Siding,
        "cabinetry" => MaterialCategory::Cabinetry,
        "countertops" => MaterialCategory::Countertops,
        "appliances" => MaterialCategory::Appliances,
        _ => return ApiResponse::<Vec<MaterialSummary>>::error("Unknown category"),
    };

    let materials = all_standard_materials();
    let summaries: Vec<MaterialSummary> = materials
        .iter()
        .filter(|m| m.category == category)
        .map(MaterialSummary::from)
        .collect();

    ApiResponse::success(summaries)
}

/// Get room types
async fn list_room_types() -> impl IntoResponse {
    let types = vec![
        ("living_room", "Living Room"),
        ("family_room", "Family Room"),
        ("great_room", "Great Room"),
        ("lounge", "Lounge"),
        ("foyer", "Foyer"),
        ("hallway", "Hallway"),
        ("master_suite", "Master Suite"),
        ("bedroom", "Bedroom"),
        ("guest_room", "Guest Room"),
        ("nursery", "Nursery"),
        ("master_bath", "Master Bath"),
        ("full_bath", "Full Bath"),
        ("half_bath", "Half Bath"),
        ("powder_room", "Powder Room"),
        ("kitchen", "Kitchen"),
        ("dining_room", "Dining Room"),
        ("breakfast_nook", "Breakfast Nook"),
        ("pantry", "Pantry"),
        ("butlers_pantry", "Butler's Pantry"),
        ("bar", "Bar"),
        ("laundry", "Laundry"),
        ("mud_room", "Mud Room"),
        ("utility", "Utility"),
        ("storage", "Storage"),
        ("closet", "Closet"),
        ("walk_in_closet", "Walk-in Closet"),
        ("office", "Office"),
        ("study", "Study"),
        ("library", "Library"),
        ("porch", "Porch"),
        ("deck", "Deck"),
        ("patio", "Patio"),
        ("sunroom", "Sunroom"),
        ("screened", "Screened Porch"),
        ("garage", "Garage"),
        ("carport", "Carport"),
        ("workshop", "Workshop"),
    ];

    ApiResponse::success(
        types
            .into_iter()
            .map(|(id, name)| serde_json::json!({"id": id, "name": name}))
            .collect::<Vec<_>>(),
    )
}

/// Create the API router
fn api_routes() -> Router<SharedState> {
    Router::new()
        // Health
        .route("/health", get(health_check))
        // Projects
        .route("/projects", get(list_projects).post(create_project))
        .route(
            "/projects/:project_id",
            get(get_project).delete(delete_project),
        )
        // Floor plans
        .route(
            "/projects/:project_id/floors",
            get(get_floor_plans).post(add_floor_plan),
        )
        // Rooms
        .route(
            "/projects/:project_id/floors/:floor_id/rooms",
            get(get_rooms).post(add_room),
        )
        // Walls
        .route(
            "/projects/:project_id/floors/:floor_id/walls",
            post(add_wall),
        )
        // Calculations
        .route(
            "/projects/:project_id/calculate",
            post(calculate_project_materials),
        )
        .route(
            "/projects/:project_id/floors/:floor_id/calculate",
            post(calculate_floor_materials),
        )
        // Reference data
        .route("/materials", get(list_materials))
        .route("/materials/:category", get(list_materials_by_category))
        .route("/room-types", get(list_room_types))
}

#[tokio::main]
async fn main() {
    // Initialize tracing
    tracing_subscriber::registry()
        .with(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "floorplan_backend=debug,tower_http=debug".into()),
        )
        .with(tracing_subscriber::fmt::layer())
        .init();

    // Load environment variables
    dotenvy::dotenv().ok();

    // Create application state
    let state = Arc::new(AppState::with_sample_data());

    // Setup CORS
    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods([Method::GET, Method::POST, Method::PUT, Method::DELETE])
        .allow_headers([header::CONTENT_TYPE, header::AUTHORIZATION]);

    // Build the router
    let app = Router::new()
        .nest("/api/v1", api_routes())
        // Serve static files from the frontend build
        .nest_service("/", ServeDir::new("static"))
        .layer(cors)
        .layer(TraceLayer::new_for_http())
        .with_state(state);

    // Get the port from environment or use default
    let port = std::env::var("PORT").unwrap_or_else(|_| "3000".to_string());
    let addr = format!("0.0.0.0:{}", port);

    tracing::info!("Starting server on {}", addr);

    // Run the server
    let listener = tokio::net::TcpListener::bind(&addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
