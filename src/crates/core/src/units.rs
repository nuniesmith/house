//! # Units Module
//!
//! Provides types and utilities for handling architectural measurements
//! in feet and inches, with conversions and formatting.

use serde::{Deserialize, Serialize};
use std::fmt;
use std::ops::{Add, Div, Mul, Sub};

/// Represents a measurement in feet and inches (e.g., 14'-6")
#[derive(Debug, Clone, Copy, PartialEq, Serialize, Deserialize)]
pub struct FeetInches {
    /// Whole feet component
    pub feet: i32,
    /// Inches component (0-11)
    pub inches: i32,
}

impl FeetInches {
    /// Create a new FeetInches measurement
    pub fn new(feet: i32, inches: i32) -> Self {
        // Normalize: ensure inches is 0-11
        let total_inches = feet * 12 + inches;
        Self {
            feet: total_inches / 12,
            inches: total_inches % 12,
        }
    }

    /// Create from feet only
    pub fn from_feet(feet: i32) -> Self {
        Self { feet, inches: 0 }
    }

    /// Create from inches only
    pub fn from_inches(inches: i32) -> Self {
        Self::new(0, inches)
    }

    /// Create from a decimal feet value (e.g., 14.5 = 14'-6")
    pub fn from_decimal_feet(decimal_feet: f64) -> Self {
        let total_inches = (decimal_feet * 12.0).round() as i32;
        Self::new(0, total_inches)
    }

    /// Convert to total inches
    pub fn to_inches(&self) -> i32 {
        self.feet * 12 + self.inches
    }

    /// Convert to decimal feet
    pub fn to_decimal_feet(&self) -> f64 {
        self.feet as f64 + (self.inches as f64 / 12.0)
    }

    /// Convert to meters
    pub fn to_meters(&self) -> f64 {
        self.to_decimal_feet() * 0.3048
    }

    /// Convert to centimeters
    pub fn to_centimeters(&self) -> f64 {
        self.to_meters() * 100.0
    }

    /// Parse from architectural notation (e.g., "14'-6\"" or "14-6" or "14'6")
    pub fn parse(s: &str) -> Result<Self, ParseError> {
        let s = s.trim();

        // Try parsing different formats
        // Format: 14'-6" or 14'-6
        if let Some(feet_end) = s.find('\'') {
            let feet_str = &s[..feet_end];
            let feet: i32 = feet_str.parse().map_err(|_| ParseError::InvalidFeet)?;

            let inches_part = s[feet_end + 1..]
                .trim_start_matches('-')
                .trim_end_matches('"');
            let inches: i32 = if inches_part.is_empty() {
                0
            } else {
                inches_part.parse().map_err(|_| ParseError::InvalidInches)?
            };

            return Ok(Self::new(feet, inches));
        }

        // Format: 14-6 (feet-inches)
        if let Some(dash_pos) = s.find('-') {
            let feet: i32 = s[..dash_pos].parse().map_err(|_| ParseError::InvalidFeet)?;
            let inches: i32 = s[dash_pos + 1..]
                .trim_end_matches('"')
                .parse()
                .map_err(|_| ParseError::InvalidInches)?;
            return Ok(Self::new(feet, inches));
        }

        // Format: just a number (assume feet)
        if let Ok(feet) = s.parse::<i32>() {
            return Ok(Self::from_feet(feet));
        }

        // Format: decimal feet
        if let Ok(decimal) = s.parse::<f64>() {
            return Ok(Self::from_decimal_feet(decimal));
        }

        Err(ParseError::InvalidFormat)
    }

    /// Format as architectural notation (e.g., "14'-6\"")
    pub fn to_arch_string(&self) -> String {
        if self.inches == 0 {
            format!("{}'", self.feet)
        } else {
            format!("{}'-{}\"", self.feet, self.inches)
        }
    }
}

impl Default for FeetInches {
    fn default() -> Self {
        Self { feet: 0, inches: 0 }
    }
}

impl fmt::Display for FeetInches {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.to_arch_string())
    }
}

impl Add for FeetInches {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self::from_inches(self.to_inches() + other.to_inches())
    }
}

impl Sub for FeetInches {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        Self::from_inches(self.to_inches() - other.to_inches())
    }
}

impl Mul<i32> for FeetInches {
    type Output = Self;

    fn mul(self, scalar: i32) -> Self {
        Self::from_inches(self.to_inches() * scalar)
    }
}

impl Div<i32> for FeetInches {
    type Output = Self;

    fn div(self, scalar: i32) -> Self {
        Self::from_inches(self.to_inches() / scalar)
    }
}

/// Errors that can occur when parsing measurements
#[derive(Debug, Clone, PartialEq, thiserror::Error)]
pub enum ParseError {
    #[error("Invalid feet value")]
    InvalidFeet,
    #[error("Invalid inches value")]
    InvalidInches,
    #[error("Invalid measurement format")]
    InvalidFormat,
}

/// Represents area in square feet
#[derive(Debug, Clone, Copy, PartialEq, PartialOrd, Serialize, Deserialize)]
pub struct SquareFeet(pub f64);

impl SquareFeet {
    pub fn new(value: f64) -> Self {
        Self(value)
    }

    /// Create from dimensions
    pub fn from_dimensions(length: FeetInches, width: FeetInches) -> Self {
        Self(length.to_decimal_feet() * width.to_decimal_feet())
    }

    /// Convert to square meters
    pub fn to_square_meters(&self) -> f64 {
        self.0 * 0.092903
    }

    /// Get the raw value
    pub fn value(&self) -> f64 {
        self.0
    }
}

impl Default for SquareFeet {
    fn default() -> Self {
        Self(0.0)
    }
}

impl fmt::Display for SquareFeet {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:.2} sq ft", self.0)
    }
}

impl Add for SquareFeet {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self(self.0 + other.0)
    }
}

impl Sub for SquareFeet {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        Self(self.0 - other.0)
    }
}

/// Represents linear feet (for trim, wire, etc.)
#[derive(Debug, Clone, Copy, PartialEq, PartialOrd, Serialize, Deserialize)]
pub struct LinearFeet(pub f64);

impl LinearFeet {
    pub fn new(value: f64) -> Self {
        Self(value)
    }

    /// Create from a FeetInches measurement
    pub fn from_feet_inches(fi: FeetInches) -> Self {
        Self(fi.to_decimal_feet())
    }

    /// Convert to meters
    pub fn to_meters(&self) -> f64 {
        self.0 * 0.3048
    }

    /// Get the raw value
    pub fn value(&self) -> f64 {
        self.0
    }

    /// Calculate number of pieces needed given piece length
    pub fn pieces_needed(&self, piece_length: f64) -> u32 {
        (self.0 / piece_length).ceil() as u32
    }
}

impl Default for LinearFeet {
    fn default() -> Self {
        Self(0.0)
    }
}

impl fmt::Display for LinearFeet {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:.2} LF", self.0)
    }
}

impl Add for LinearFeet {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self(self.0 + other.0)
    }
}

impl Sub for LinearFeet {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        Self(self.0 - other.0)
    }
}

impl Mul<f64> for LinearFeet {
    type Output = Self;

    fn mul(self, scalar: f64) -> Self {
        Self(self.0 * scalar)
    }
}

/// Ceiling height type with support for standard and vaulted ceilings
#[derive(Debug, Clone, Copy, PartialEq, Serialize, Deserialize)]
pub enum CeilingHeight {
    /// Standard flat ceiling
    Standard(FeetInches),
    /// Vaulted ceiling with pitch (e.g., 7/12)
    Vaulted {
        /// Minimum height at walls
        min_height: FeetInches,
        /// Pitch expressed as rise/12 (e.g., 7 means 7/12 pitch)
        pitch: u8,
    },
    /// Cathedral ceiling (vaulted following roof line)
    Cathedral {
        min_height: FeetInches,
        max_height: FeetInches,
    },
    /// Tray ceiling with raised center
    Tray {
        perimeter_height: FeetInches,
        center_height: FeetInches,
        tray_width: FeetInches,
    },
}

impl CeilingHeight {
    /// Get the minimum (wall) height
    pub fn min_height(&self) -> FeetInches {
        match self {
            CeilingHeight::Standard(h) => *h,
            CeilingHeight::Vaulted { min_height, .. } => *min_height,
            CeilingHeight::Cathedral { min_height, .. } => *min_height,
            CeilingHeight::Tray {
                perimeter_height, ..
            } => *perimeter_height,
        }
    }

    /// Get the average height for calculations
    pub fn average_height(&self) -> FeetInches {
        match self {
            CeilingHeight::Standard(h) => *h,
            CeilingHeight::Vaulted { min_height, pitch } => {
                // Rough estimate: add half the rise for average
                let rise_per_foot = *pitch as f64 / 12.0;
                let avg_rise = rise_per_foot * 4.0; // Assume ~8ft span, so 4ft to center
                FeetInches::from_decimal_feet(min_height.to_decimal_feet() + avg_rise)
            }
            CeilingHeight::Cathedral {
                min_height,
                max_height,
            } => {
                let avg = (min_height.to_decimal_feet() + max_height.to_decimal_feet()) / 2.0;
                FeetInches::from_decimal_feet(avg)
            }
            CeilingHeight::Tray {
                perimeter_height,
                center_height,
                ..
            } => {
                // Weight towards perimeter since tray is usually smaller
                let avg = (perimeter_height.to_decimal_feet() * 0.7)
                    + (center_height.to_decimal_feet() * 0.3);
                FeetInches::from_decimal_feet(avg)
            }
        }
    }
}

impl Default for CeilingHeight {
    fn default() -> Self {
        // Standard 9' ceiling
        CeilingHeight::Standard(FeetInches::new(9, 0))
    }
}

impl fmt::Display for CeilingHeight {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            CeilingHeight::Standard(h) => write!(f, "{} CLG", h),
            CeilingHeight::Vaulted { min_height, pitch } => {
                write!(f, "{}/12 Vaulted ({})", pitch, min_height)
            }
            CeilingHeight::Cathedral {
                min_height,
                max_height,
            } => {
                write!(f, "Cathedral {}-{}", min_height, max_height)
            }
            CeilingHeight::Tray {
                perimeter_height,
                center_height,
                ..
            } => {
                write!(f, "Tray {} / {}", perimeter_height, center_height)
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_feet_inches_creation() {
        let fi = FeetInches::new(14, 6);
        assert_eq!(fi.feet, 14);
        assert_eq!(fi.inches, 6);
    }

    #[test]
    fn test_feet_inches_normalization() {
        let fi = FeetInches::new(14, 18);
        assert_eq!(fi.feet, 15);
        assert_eq!(fi.inches, 6);
    }

    #[test]
    fn test_feet_inches_parse() {
        assert_eq!(
            FeetInches::parse("14'-6\"").unwrap(),
            FeetInches::new(14, 6)
        );
        assert_eq!(FeetInches::parse("14'-6").unwrap(), FeetInches::new(14, 6));
        assert_eq!(FeetInches::parse("14-6").unwrap(), FeetInches::new(14, 6));
        assert_eq!(FeetInches::parse("14'").unwrap(), FeetInches::new(14, 0));
        assert_eq!(FeetInches::parse("14").unwrap(), FeetInches::new(14, 0));
    }

    #[test]
    fn test_feet_inches_to_decimal() {
        let fi = FeetInches::new(14, 6);
        assert!((fi.to_decimal_feet() - 14.5).abs() < 0.001);
    }

    #[test]
    fn test_feet_inches_arithmetic() {
        let a = FeetInches::new(10, 6);
        let b = FeetInches::new(5, 8);

        let sum = a + b;
        assert_eq!(sum, FeetInches::new(16, 2));

        let diff = a - b;
        assert_eq!(diff, FeetInches::new(4, 10));
    }

    #[test]
    fn test_square_feet_from_dimensions() {
        let length = FeetInches::new(14, 0);
        let width = FeetInches::new(12, 0);
        let area = SquareFeet::from_dimensions(length, width);
        assert!((area.0 - 168.0).abs() < 0.001);
    }

    #[test]
    fn test_linear_feet_pieces() {
        let lf = LinearFeet::new(25.0);
        // 25 LF with 8ft pieces = 4 pieces (25/8 = 3.125, ceil = 4)
        assert_eq!(lf.pieces_needed(8.0), 4);
    }

    #[test]
    fn test_ceiling_height_average() {
        let standard = CeilingHeight::Standard(FeetInches::new(9, 0));
        assert_eq!(standard.average_height(), FeetInches::new(9, 0));

        let cathedral = CeilingHeight::Cathedral {
            min_height: FeetInches::new(8, 0),
            max_height: FeetInches::new(16, 0),
        };
        assert_eq!(cathedral.average_height(), FeetInches::new(12, 0));
    }
}
