//! # Floorplan Frontend
//!
//! Leptos-based WASM frontend for floor plan design and material calculations.

use leptos::*;
use serde::{Deserialize, Serialize};
use wasm_bindgen::prelude::*;

// Re-export core types for use in components
pub use floorplan_core::models::{FloorPlan, Project, QualityTier, Room, RoomType};
pub use floorplan_core::units::FeetInches;

/// API base URL - configurable via environment
#[allow(dead_code)]
const API_BASE: &str = "/api/v1";

// ============================================================================
// API Types
// ============================================================================

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ApiResponse<T> {
    pub success: bool,
    pub data: Option<T>,
    pub error: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ProjectSummary {
    pub id: String,
    pub name: String,
    pub description: Option<String>,
    pub floor_count: usize,
    pub total_sqft: f64,
    pub bedroom_count: usize,
    pub bathroom_count: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CalculationSummary {
    pub description: String,
    pub total_cost: f64,
    pub cost_per_sqft: Option<f64>,
    pub item_count: usize,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MaterialSummary {
    pub id: String,
    pub name: String,
    pub category: String,
    pub unit: String,
    pub price_standard: f64,
}

// ============================================================================
// State Management
// ============================================================================

/// Global application state
#[derive(Debug, Clone, Default)]
pub struct AppState {
    pub current_project: Option<Project>,
    pub current_floor: Option<usize>,
    pub selected_room: Option<usize>,
    pub quality_tier: QualityTier,
}

// ============================================================================
// Components
// ============================================================================

/// Main application component
#[component]
pub fn App() -> impl IntoView {
    // Application state
    let (projects, _set_projects) = create_signal(Vec::<ProjectSummary>::new());
    let (current_project, _set_current_project) = create_signal(None::<Project>);
    let (view, set_view) = create_signal("dashboard".to_string());

    view! {
        <div class="app-container">
            <Sidebar
                view=view
                set_view=set_view
            />
            <main class="main-content">
                <Header />
                <div class="content-area">
                    {move || match view.get().as_str() {
                        "dashboard" => view! { <Dashboard projects=projects /> }.into_view(),
                        "designer" => view! { <FloorPlanDesigner project=current_project /> }.into_view(),
                        "calculator" => view! { <MaterialCalculator _project=current_project /> }.into_view(),
                        "materials" => view! { <MaterialsLibrary /> }.into_view(),
                        _ => view! { <Dashboard projects=projects /> }.into_view(),
                    }}
                </div>
            </main>
        </div>
    }
}

/// Sidebar navigation component
#[component]
fn Sidebar(view: ReadSignal<String>, set_view: WriteSignal<String>) -> impl IntoView {
    let nav_items = vec![
        ("dashboard", "Dashboard", "📊"),
        ("designer", "Floor Plan Designer", "📐"),
        ("calculator", "Material Calculator", "🧮"),
        ("materials", "Materials Library", "🏗️"),
    ];

    view! {
        <nav class="sidebar">
            <div class="logo">
                <h1>"🏠 FloorPlan"</h1>
                <span class="subtitle">"Design & Calculate"</span>
            </div>
            <ul class="nav-menu">
                {nav_items.into_iter().map(|(id, label, icon)| {
                    let id_clone = id.to_string();
                    let is_active = move || view.get() == id;
                    view! {
                        <li
                            class:active=is_active
                            on:click=move |_| set_view.set(id_clone.clone())
                        >
                            <span class="icon">{icon}</span>
                            <span class="label">{label}</span>
                        </li>
                    }
                }).collect_view()}
            </ul>
        </nav>
    }
}

/// Header component
#[component]
fn Header() -> impl IntoView {
    view! {
        <header class="header">
            <div class="breadcrumb">
                <span>"Home"</span>
            </div>
            <div class="header-actions">
                <button class="btn btn-secondary">"Export"</button>
                <button class="btn btn-primary">"Save Project"</button>
            </div>
        </header>
    }
}

/// Dashboard view
#[component]
fn Dashboard(projects: ReadSignal<Vec<ProjectSummary>>) -> impl IntoView {
    view! {
        <div class="dashboard">
            <section class="welcome-section">
                <h2>"Welcome to FloorPlan Designer"</h2>
                <p>"Design your floor plans and calculate materials with precision."</p>
            </section>

            <section class="stats-section">
                <div class="stat-card">
                    <div class="stat-value">{move || projects.get().len()}</div>
                    <div class="stat-label">"Projects"</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">"0"</div>
                    <div class="stat-label">"Total Sq Ft"</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">"$0"</div>
                    <div class="stat-label">"Estimated Cost"</div>
                </div>
            </section>

            <section class="projects-section">
                <div class="section-header">
                    <h3>"Recent Projects"</h3>
                    <button class="btn btn-primary">"+ New Project"</button>
                </div>
                <div class="projects-grid">
                    {move || {
                        let projs = projects.get();
                        if projs.is_empty() {
                            view! {
                                <div class="empty-state">
                                    <p>"No projects yet. Create your first floor plan!"</p>
                                </div>
                            }.into_view()
                        } else {
                            projs.iter().map(|p| {
                                view! {
                                    <ProjectCard project=p.clone() />
                                }
                            }).collect_view()
                        }
                    }}
                </div>
            </section>
        </div>
    }
}

/// Project card component
#[component]
fn ProjectCard(project: ProjectSummary) -> impl IntoView {
    view! {
        <div class="project-card">
            <h4>{&project.name}</h4>
            <div class="project-meta">
                <span>{format!("{:.0} sq ft", project.total_sqft)}</span>
                <span>{format!("{} BR / {} BA", project.bedroom_count, project.bathroom_count)}</span>
            </div>
            <div class="project-actions">
                <button class="btn btn-small">"Open"</button>
                <button class="btn btn-small btn-secondary">"Calculate"</button>
            </div>
        </div>
    }
}

/// Floor plan designer view
#[component]
fn FloorPlanDesigner(project: ReadSignal<Option<Project>>) -> impl IntoView {
    let (scale, set_scale) = create_signal(1.0_f64);
    let (selected_tool, set_selected_tool) = create_signal("select".to_string());

    view! {
        <div class="designer">
            <div class="designer-toolbar">
                <div class="tool-group">
                    <button
                        class:active=move || selected_tool.get() == "select"
                        on:click=move |_| set_selected_tool.set("select".to_string())
                    >"Select"</button>
                    <button
                        class:active=move || selected_tool.get() == "room"
                        on:click=move |_| set_selected_tool.set("room".to_string())
                    >"Add Room"</button>
                    <button
                        class:active=move || selected_tool.get() == "wall"
                        on:click=move |_| set_selected_tool.set("wall".to_string())
                    >"Draw Wall"</button>
                    <button
                        class:active=move || selected_tool.get() == "door"
                        on:click=move |_| set_selected_tool.set("door".to_string())
                    >"Add Door"</button>
                    <button
                        class:active=move || selected_tool.get() == "window"
                        on:click=move |_| set_selected_tool.set("window".to_string())
                    >"Add Window"</button>
                </div>
                <div class="zoom-controls">
                    <button on:click=move |_| set_scale.update(|s| *s = (*s - 0.1).max(0.25))>"-"</button>
                    <span>{move || format!("{:.0}%", scale.get() * 100.0)}</span>
                    <button on:click=move |_| set_scale.update(|s| *s = (*s + 0.1).min(3.0))>"+"</button>
                </div>
            </div>

            <div class="designer-canvas-container">
                <svg
                    class="designer-canvas"
                    viewBox="0 0 1200 800"
                    style=move || format!("transform: scale({})", scale.get())
                >
                    // Grid
                    <defs>
                        <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
                            <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#e0e0e0" stroke-width="0.5"/>
                        </pattern>
                        <pattern id="grid-large" width="96" height="96" patternUnits="userSpaceOnUse">
                            <rect width="96" height="96" fill="url(#grid)"/>
                            <path d="M 96 0 L 0 0 0 96" fill="none" stroke="#ccc" stroke-width="1"/>
                        </pattern>
                    </defs>
                    <rect width="100%" height="100%" fill="url(#grid-large)"/>

                    // Rooms will be rendered here based on project data
                    {move || {
                        if let Some(proj) = project.get() {
                            if let Some(floor) = proj.floor_plans.first() {
                                floor.rooms.iter().enumerate().map(|(_i, room)| {
                                    let x = room.position.x / 12.0 * 24.0; // Convert inches to pixels
                                    let y = room.position.y / 12.0 * 24.0;
                                    let w = room.length.to_decimal_feet() * 24.0;
                                    let h = room.width.to_decimal_feet() * 24.0;

                                    view! {
                                        <g class="room">
                                            <rect
                                                x=x
                                                y=y
                                                width=w
                                                height=h
                                                fill="#f0f7ff"
                                                stroke="#2563eb"
                                                stroke-width="2"
                                            />
                                            <text
                                                x=x + w / 2.0
                                                y=y + h / 2.0
                                                text-anchor="middle"
                                                dominant-baseline="middle"
                                                font-size="12"
                                            >
                                                {&room.name}
                                            </text>
                                        </g>
                                    }
                                }).collect_view()
                            } else {
                                view! {}.into_view()
                            }
                        } else {
                            view! {
                                <text x="600" y="400" text-anchor="middle" fill="#999">
                                    "Create or load a project to start designing"
                                </text>
                            }.into_view()
                        }
                    }}
                </svg>
            </div>

            <RoomPropertiesPanel />
        </div>
    }
}

/// Room properties side panel
#[component]
fn RoomPropertiesPanel() -> impl IntoView {
    view! {
        <div class="properties-panel">
            <h3>"Room Properties"</h3>
            <div class="property-group">
                <label>"Name"</label>
                <input type="text" placeholder="Room name" />
            </div>
            <div class="property-group">
                <label>"Type"</label>
                <select>
                    <option value="bedroom">"Bedroom"</option>
                    <option value="bathroom">"Bathroom"</option>
                    <option value="kitchen">"Kitchen"</option>
                    <option value="living_room">"Living Room"</option>
                    <option value="dining_room">"Dining Room"</option>
                    <option value="office">"Office"</option>
                    <option value="garage">"Garage"</option>
                </select>
            </div>
            <div class="property-group">
                <label>"Dimensions"</label>
                <div class="dimension-inputs">
                    <input type="number" placeholder="Length (ft)" />
                    <span>"×"</span>
                    <input type="number" placeholder="Width (ft)" />
                </div>
            </div>
            <div class="property-group">
                <label>"Ceiling Height"</label>
                <input type="number" placeholder="Height (ft)" value="9" />
            </div>
        </div>
    }
}

/// Material calculator view
#[component]
fn MaterialCalculator(_project: ReadSignal<Option<Project>>) -> impl IntoView {
    let (_quality_tier, set_quality_tier) = create_signal(QualityTier::Standard);
    let (include_waste, set_include_waste) = create_signal(true);

    view! {
        <div class="calculator">
            <div class="calculator-header">
                <h2>"Material Calculator"</h2>
                <p>"Calculate materials needed for your floor plan"</p>
            </div>

            <div class="calculator-controls">
                <div class="control-group">
                    <label>"Quality Tier"</label>
                    <select on:change=move |ev| {
                        let value = event_target_value(&ev);
                        let tier = match value.as_str() {
                            "economy" => QualityTier::Economy,
                            "premium" => QualityTier::Premium,
                            "luxury" => QualityTier::Luxury,
                            _ => QualityTier::Standard,
                        };
                        set_quality_tier.set(tier);
                    }>
                        <option value="economy">"Economy"</option>
                        <option value="standard" selected>"Standard"</option>
                        <option value="premium">"Premium"</option>
                        <option value="luxury">"Luxury"</option>
                    </select>
                </div>

                <div class="control-group">
                    <label>
                        <input
                            type="checkbox"
                            checked=include_waste
                            on:change=move |ev| set_include_waste.set(event_target_checked(&ev))
                        />
                        " Include 10% waste factor"
                    </label>
                </div>

                <button class="btn btn-primary">"Calculate Materials"</button>
            </div>

            <div class="calculation-results">
                <div class="result-section">
                    <h3>"Framing"</h3>
                    <table class="results-table">
                        <thead>
                            <tr>
                                <th>"Material"</th>
                                <th>"Quantity"</th>
                                <th>"Unit"</th>
                                <th>"Cost"</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>"2x4x8' Studs"</td>
                                <td>"0"</td>
                                <td>"ea"</td>
                                <td>"$0.00"</td>
                            </tr>
                            <tr>
                                <td>"2x4 Plates"</td>
                                <td>"0"</td>
                                <td>"LF"</td>
                                <td>"$0.00"</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="result-section">
                    <h3>"Drywall"</h3>
                    <table class="results-table">
                        <thead>
                            <tr>
                                <th>"Material"</th>
                                <th>"Quantity"</th>
                                <th>"Unit"</th>
                                <th>"Cost"</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>"1/2\" Drywall Sheets"</td>
                                <td>"0"</td>
                                <td>"sht"</td>
                                <td>"$0.00"</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="total-section">
                    <div class="total-row">
                        <span>"Total Materials Cost:"</span>
                        <span class="total-value">"$0.00"</span>
                    </div>
                    <div class="total-row">
                        <span>"Cost per Sq Ft:"</span>
                        <span class="total-value">"$0.00"</span>
                    </div>
                </div>
            </div>
        </div>
    }
}

/// Materials library view
#[component]
fn MaterialsLibrary() -> impl IntoView {
    let (selected_category, set_selected_category) = create_signal("all".to_string());

    let categories = vec![
        ("all", "All Materials"),
        ("lumber", "Lumber"),
        ("sheetgoods", "Sheet Goods"),
        ("flooring", "Flooring"),
        ("insulation", "Insulation"),
        ("electrical", "Electrical"),
        ("trim", "Trim & Millwork"),
        ("paint", "Paint"),
        ("doors", "Doors"),
        ("windows", "Windows"),
    ];

    view! {
        <div class="materials-library">
            <div class="library-header">
                <h2>"Materials Library"</h2>
                <p>"Browse available materials and pricing"</p>
            </div>

            <div class="category-tabs">
                {categories.into_iter().map(|(id, name)| {
                    let id_clone = id.to_string();
                    view! {
                        <button
                            class:active=move || selected_category.get() == id
                            on:click=move |_| set_selected_category.set(id_clone.clone())
                        >
                            {name}
                        </button>
                    }
                }).collect_view()}
            </div>

            <div class="materials-grid">
                <MaterialCard
                    name="2x4x8' Stud"
                    category="Lumber"
                    unit="ea"
                    price_economy=3.50
                    price_standard=4.50
                    price_premium=6.00
                    price_luxury=8.00
                />
                <MaterialCard
                    name="2x6x8' Stud"
                    category="Lumber"
                    unit="ea"
                    price_economy=6.00
                    price_standard=7.50
                    price_premium=10.00
                    price_luxury=14.00
                />
                <MaterialCard
                    name="1/2\" Drywall"
                    category="Sheet Goods"
                    unit="sht"
                    price_economy=10.00
                    price_standard=12.00
                    price_premium=15.00
                    price_luxury=20.00
                />
            </div>
        </div>
    }
}

/// Material card component
#[component]
fn MaterialCard(
    name: &'static str,
    category: &'static str,
    unit: &'static str,
    price_economy: f64,
    price_standard: f64,
    price_premium: f64,
    price_luxury: f64,
) -> impl IntoView {
    view! {
        <div class="material-card">
            <div class="material-header">
                <h4>{name}</h4>
                <span class="category-badge">{category}</span>
            </div>
            <div class="material-pricing">
                <div class="price-tier">
                    <span class="tier-label">"Economy"</span>
                    <span class="tier-price">{format!("${:.2}/{}", price_economy, unit)}</span>
                </div>
                <div class="price-tier standard">
                    <span class="tier-label">"Standard"</span>
                    <span class="tier-price">{format!("${:.2}/{}", price_standard, unit)}</span>
                </div>
                <div class="price-tier">
                    <span class="tier-label">"Premium"</span>
                    <span class="tier-price">{format!("${:.2}/{}", price_premium, unit)}</span>
                </div>
                <div class="price-tier">
                    <span class="tier-label">"Luxury"</span>
                    <span class="tier-price">{format!("${:.2}/{}", price_luxury, unit)}</span>
                </div>
            </div>
        </div>
    }
}

// ============================================================================
// WASM Entry Point
// ============================================================================

/// Initialize the application
#[wasm_bindgen(start)]
pub fn start() {
    // Set up panic hook for better error messages
    console_error_panic_hook::set_once();

    // Initialize logging
    let _ = console_log::init_with_level(log::Level::Debug);

    log::info!("FloorPlan Designer starting...");

    // Mount the application
    mount_to_body(|| view! { <App /> });
}

/// Hydrate the application (for SSR)
#[wasm_bindgen]
pub fn hydrate() {
    console_error_panic_hook::set_once();
    leptos::mount_to_body(App);
}
