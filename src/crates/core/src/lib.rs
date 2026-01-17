//! # Floorplan Core Library
//!
//! Core library for floor plan design and material calculations.
//! This crate provides shared types and calculation logic used by both
//! the backend server and the WASM frontend.

pub mod calculations;
pub mod materials;
pub mod models;
pub mod plans;
pub mod svg_renderer;
pub mod units;

// Re-export commonly used types
pub use calculations::*;
pub use materials::*;
pub use models::*;
pub use plans::*;
pub use svg_renderer::*;
pub use units::*;
