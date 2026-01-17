//! # Floor Plan Definitions Module
//!
//! Pre-defined floor plans that can be loaded and rendered.
//! Includes the luxury farmhouse layout from the provided floor plan image.

pub mod luxury_farmhouse;
pub mod serialization;

pub use luxury_farmhouse::*;
pub use serialization::*;
