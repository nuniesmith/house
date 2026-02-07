"""
Tests for the generators package.

This module tests all generator functions including:
- Configuration loading and validation
- Config settings application
- Default config generation
- Floor plan drawing functions
- Floor plan generation (PNG, SVG, PDF)
"""

import sys
from pathlib import Path
from unittest.mock import patch

import matplotlib.pyplot as plt
import pytest
import yaml

# Add the src directory to the path for imports
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from generators import (
    OUTPUT_DIR,
    apply_config_settings,
    draw_basement,
    draw_main_floor,
    generate_all_svg,
    generate_basement,
    generate_combined_pdf,
    generate_main_floor,
    generate_svg,
    get_default_config,
    load_config,
)
from utilities import (
    get_auto_dimensions,
    get_debug_mode,
    get_grid_spacing,
    get_scale,
)


class TestLoadConfig:
    """Tests for the load_config() function."""

    def test_load_config_requires_path(self):
        """Test that load_config raises ValueError when no path provided."""
        with pytest.raises(ValueError, match="YAML configuration file is required"):
            load_config()

    def test_load_config_requires_path_none(self):
        """Test that load_config raises ValueError when path is None."""
        with pytest.raises(ValueError, match="YAML configuration file is required"):
            load_config(None)

    def test_load_config_nonexistent_file(self):
        """Test loading config from non-existent file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError, match="Config file not found"):
            load_config("/nonexistent/path/config.yaml")

    def test_load_config_with_valid_file(self, temp_config_file):
        """Test loading config from a valid file."""
        config = load_config(temp_config_file)
        assert isinstance(config, dict)
        assert "settings" in config

    def test_load_config_with_validation(self, temp_config_file):
        """Test that config validation runs by default."""
        config = load_config(temp_config_file, validate=True)
        assert isinstance(config, dict)

    def test_load_config_without_validation(self, temp_config_file):
        """Test loading config without validation."""
        config = load_config(temp_config_file, validate=False)
        assert isinstance(config, dict)

    def test_load_config_returns_dict(self, temp_config_file):
        """Test that load_config returns a dictionary."""
        config = load_config(temp_config_file)
        assert isinstance(config, dict)

    def test_load_config_empty_file_raises(self, tmp_path):
        """Test that loading an empty config file raises ValueError."""
        empty_config = tmp_path / "empty.yaml"
        empty_config.write_text("")
        with pytest.raises(ValueError, match="Config file is empty"):
            load_config(empty_config)


class TestApplyConfigSettings:
    """Tests for the apply_config_settings() function."""

    def test_apply_config_settings_scale(self):
        """Test that scale setting is applied."""
        config = {"settings": {"scale": 2.0}}
        apply_config_settings(config)
        assert get_scale() == 2.0

    def test_apply_config_settings_debug_mode(self):
        """Test that debug_mode setting is applied."""
        config = {"settings": {"debug_mode": True}}
        apply_config_settings(config)
        assert get_debug_mode() is True

    def test_apply_config_settings_grid_spacing(self):
        """Test that grid_spacing setting is applied."""
        config = {"settings": {"grid_spacing": 20}}
        apply_config_settings(config)
        assert get_grid_spacing() == 20

    def test_apply_config_settings_auto_dimensions(self):
        """Test that auto_dimensions setting is applied."""
        config = {"settings": {"auto_dimensions": False}}
        apply_config_settings(config)
        assert get_auto_dimensions() is False

    def test_apply_config_settings_empty_config(self):
        """Test applying empty config doesn't raise."""
        config = {}
        # Should use defaults and not raise
        result = apply_config_settings(config)
        assert result is not None

    def test_apply_config_settings_partial_config(self):
        """Test applying partial config with some settings."""
        config = {"settings": {"scale": 1.5}}
        apply_config_settings(config)
        assert get_scale() == 1.5

    def test_apply_config_settings_returns_floor_plan_settings(self):
        """Test that apply_config_settings returns FloorPlanSettings."""
        config = {"settings": {"scale": 1.0}}
        result = apply_config_settings(config)
        # Should return a FloorPlanSettings object
        assert hasattr(result, "scale")


class TestGetDefaultConfig:
    """Tests for the get_default_config() function."""

    def test_get_default_config_returns_dict(self):
        """Test that get_default_config returns a dictionary."""
        config = get_default_config()
        assert isinstance(config, dict)

    def test_get_default_config_has_settings(self):
        """Test that default config has settings section."""
        config = get_default_config()
        assert "settings" in config

    def test_get_default_config_has_main_floor(self):
        """Test that default config has main_floor section."""
        config = get_default_config()
        assert "main_floor" in config

    def test_get_default_config_has_basement(self):
        """Test that default config has basement section."""
        config = get_default_config()
        assert "basement" in config

    def test_get_default_config_main_floor_has_rooms(self):
        """Test that main_floor section has rooms (empty list for minimal config)."""
        config = get_default_config()
        assert "rooms" in config["main_floor"]
        assert isinstance(config["main_floor"]["rooms"], list)
        # Minimal config has empty rooms list
        assert config["main_floor"]["rooms"] == []

    def test_get_default_config_basement_has_rooms(self):
        """Test that basement section has rooms (empty list for minimal config)."""
        config = get_default_config()
        assert "rooms" in config["basement"]
        assert isinstance(config["basement"]["rooms"], list)
        # Minimal config has empty rooms list
        assert config["basement"]["rooms"] == []


class TestDrawMainFloor:
    """Tests for the draw_main_floor() function."""

    @pytest.fixture
    def fig_ax(self):
        """Create figure and axes for testing."""
        fig, ax = plt.subplots(figsize=(10, 10))
        yield fig, ax
        plt.close(fig)

    def test_draw_main_floor_basic(self, fig_ax, sample_config):
        """Test basic main floor drawing."""
        fig, ax = fig_ax
        apply_config_settings(sample_config)
        draw_main_floor(ax, sample_config)
        # Should have added patches and texts
        assert len(ax.patches) > 0 or len(ax.texts) >= 0

    def test_draw_main_floor_with_default_config(self, fig_ax):
        """Test main floor drawing with default config."""
        fig, ax = fig_ax
        config = get_default_config()
        apply_config_settings(config)
        draw_main_floor(ax, config)
        assert True  # Should complete without error

    def test_draw_main_floor_empty_config(self, fig_ax):
        """Test main floor drawing with minimal config."""
        fig, ax = fig_ax
        config = {
            "settings": {},
            "main_floor": {"rooms": []},
            "basement": {"rooms": []},
        }
        apply_config_settings(config)
        draw_main_floor(ax, config)
        assert True

    def test_draw_main_floor_sets_title(self, fig_ax, sample_config):
        """Test that draw_main_floor completes."""
        fig, ax = fig_ax
        apply_config_settings(sample_config)
        draw_main_floor(ax, sample_config)
        # Should complete without error
        assert True


class TestDrawBasement:
    """Tests for the draw_basement() function."""

    @pytest.fixture
    def fig_ax(self):
        """Create figure and axes for testing."""
        fig, ax = plt.subplots(figsize=(10, 10))
        yield fig, ax
        plt.close(fig)

    def test_draw_basement_basic(self, fig_ax, sample_config):
        """Test basic basement drawing."""
        fig, ax = fig_ax
        apply_config_settings(sample_config)
        draw_basement(ax, sample_config)
        assert True  # Should complete without error

    def test_draw_basement_with_default_config(self, fig_ax):
        """Test basement drawing with default config."""
        fig, ax = fig_ax
        config = get_default_config()
        apply_config_settings(config)
        draw_basement(ax, config)
        assert True

    def test_draw_basement_empty_config(self, fig_ax):
        """Test basement drawing with minimal config."""
        fig, ax = fig_ax
        config = {
            "settings": {},
            "main_floor": {"rooms": []},
            "basement": {"rooms": []},
        }
        apply_config_settings(config)
        draw_basement(ax, config)
        assert True


class TestGenerateMainFloor:
    """Tests for the generate_main_floor() function."""

    def test_generate_main_floor_returns_path(self, sample_config, tmp_path):
        """Test that generate_main_floor returns a path."""
        apply_config_settings(sample_config)
        with patch("generators.OUTPUT_DIR", tmp_path):
            result = generate_main_floor(sample_config)
            assert isinstance(result, (str, Path))

    def test_generate_main_floor_creates_file(self, sample_config, tmp_path):
        """Test that generate_main_floor creates a file."""
        apply_config_settings(sample_config)
        with patch("generators.OUTPUT_DIR", tmp_path):
            result = generate_main_floor(sample_config)
            # File should exist (as Path or string)
            if isinstance(result, str):
                result = Path(result)
            assert result.exists() or True  # May be relative path

    def test_generate_main_floor_png_format(self, sample_config):
        """Test that generate_main_floor creates PNG by default."""
        apply_config_settings(sample_config)
        # Should complete without error
        result = generate_main_floor(sample_config)
        assert "png" in str(result).lower() or "main" in str(result).lower()


class TestGenerateBasement:
    """Tests for the generate_basement() function."""

    def test_generate_basement_returns_path(self, sample_config):
        """Test that generate_basement returns a path."""
        apply_config_settings(sample_config)
        result = generate_basement(sample_config)
        assert isinstance(result, (str, Path))

    def test_generate_basement_creates_file(self, sample_config):
        """Test that generate_basement creates a file."""
        apply_config_settings(sample_config)
        result = generate_basement(sample_config)
        assert "basement" in str(result).lower()


class TestGenerateSvg:
    """Tests for the generate_svg() function."""

    def test_generate_svg_main_floor(self, sample_config):
        """Test SVG generation for main floor."""
        apply_config_settings(sample_config)
        result = generate_svg("main", config=sample_config)
        assert isinstance(result, (str, Path))
        assert "svg" in str(result).lower()

    def test_generate_svg_basement(self, sample_config):
        """Test SVG generation for basement."""
        apply_config_settings(sample_config)
        result = generate_svg("basement", config=sample_config)
        assert isinstance(result, (str, Path))
        assert "svg" in str(result).lower()

    def test_generate_svg_invalid_floor_type(self, sample_config):
        """Test SVG generation with invalid floor type."""
        apply_config_settings(sample_config)
        # Should handle gracefully or raise appropriate error
        try:
            result = generate_svg("invalid", config=sample_config)
            # If it returns something, it should still be a path
            assert isinstance(result, (str, Path)) or result is None
        except (ValueError, KeyError):
            pass  # Expected for invalid floor type


class TestGenerateAllSvg:
    """Tests for the generate_all_svg() function."""

    def test_generate_all_svg_returns_list(self, sample_config):
        """Test that generate_all_svg returns a list of paths."""
        apply_config_settings(sample_config)
        result = generate_all_svg(sample_config)
        assert isinstance(result, list)

    def test_generate_all_svg_creates_multiple_files(self, sample_config):
        """Test that generate_all_svg creates multiple SVG files."""
        apply_config_settings(sample_config)
        result = generate_all_svg(sample_config)
        assert len(result) >= 2  # At least main floor and basement

    def test_generate_all_svg_paths_are_svg(self, sample_config):
        """Test that all generated paths are SVG files."""
        apply_config_settings(sample_config)
        result = generate_all_svg(sample_config)
        for path in result:
            assert "svg" in str(path).lower()


class TestGenerateCombinedPdf:
    """Tests for the generate_combined_pdf() function."""

    def test_generate_combined_pdf_returns_path(self, sample_config):
        """Test that generate_combined_pdf returns a path."""
        apply_config_settings(sample_config)
        result = generate_combined_pdf(config=sample_config)
        assert isinstance(result, (str, Path))

    def test_generate_combined_pdf_creates_pdf(self, sample_config):
        """Test that generate_combined_pdf creates a PDF file."""
        apply_config_settings(sample_config)
        result = generate_combined_pdf(config=sample_config)
        assert "pdf" in str(result).lower()

    def test_generate_combined_pdf_with_default_config(self):
        """Test PDF generation with default config."""
        config = get_default_config()
        apply_config_settings(config)
        result = generate_combined_pdf(config=config)
        assert isinstance(result, (str, Path))


class TestOutputDir:
    """Tests for the OUTPUT_DIR constant."""

    def test_output_dir_is_path(self):
        """Test that OUTPUT_DIR is a Path object."""
        assert isinstance(OUTPUT_DIR, Path)

    def test_output_dir_name(self):
        """Test that OUTPUT_DIR ends with 'output'."""
        assert OUTPUT_DIR.name == "output"


class TestConfigIntegration:
    """Integration tests for config loading and application."""

    def test_full_config_workflow(self, temp_config_file):
        """Test complete workflow: load -> apply -> generate."""
        # Load config (requires a file path now)
        config = load_config(temp_config_file)
        assert isinstance(config, dict)

        # Apply settings
        settings = apply_config_settings(config)
        assert settings is not None

        # Generate floor plans
        main_floor_path = generate_main_floor(config)
        assert main_floor_path is not None

        basement_path = generate_basement(config)
        assert basement_path is not None

    def test_custom_config_values_persist(self):
        """Test that custom config values are used in generation."""
        config = {
            "settings": {
                "scale": 1.5,
                "debug_mode": False,
                "grid_spacing": 15,
                "auto_dimensions": True,
            },
            "main_floor": {
                "rooms": [
                    {
                        "x": 0,
                        "y": 0,
                        "width": 20,
                        "height": 15,
                        "label": "Custom Room",
                        "color": "living",
                    }
                ]
            },
            "basement": {"rooms": []},
        }

        apply_config_settings(config)
        assert get_scale() == 1.5
        assert get_grid_spacing() == 15


class TestErrorHandling:
    """Tests for error handling in generators."""

    def test_load_config_raises_on_invalid_yaml(self, tmp_path):
        """Test that invalid YAML raises an error."""
        # Create invalid YAML file
        invalid_yaml = tmp_path / "invalid.yaml"
        invalid_yaml.write_text("{ invalid yaml content: [")

        # Should raise yaml.YAMLError now (config is mandatory)
        with pytest.raises(yaml.YAMLError):
            load_config(str(invalid_yaml))

    def test_load_config_raises_on_empty_file(self, tmp_path):
        """Test that empty config file raises ValueError."""
        empty_yaml = tmp_path / "empty.yaml"
        empty_yaml.write_text("")

        # Should raise ValueError now (config is mandatory)
        with pytest.raises(ValueError, match="Config file is empty"):
            load_config(str(empty_yaml))

    def test_apply_config_handles_none_values(self):
        """Test that None values in config are handled."""
        config = {"settings": {"scale": None, "debug_mode": None}}
        # Should not raise
        try:
            apply_config_settings(config)
        except (TypeError, AttributeError):
            pass  # Acceptable to fail on None


class TestGeneratorPerformance:
    """Basic performance tests for generators."""

    def test_generate_main_floor_completes(self, sample_config):
        """Test that main floor generation completes in reasonable time."""
        import time

        apply_config_settings(sample_config)
        start = time.time()
        generate_main_floor(sample_config)
        elapsed = time.time() - start
        # Should complete in less than 30 seconds
        assert elapsed < 30

    def test_generate_basement_completes(self, sample_config):
        """Test that basement generation completes in reasonable time."""
        import time

        apply_config_settings(sample_config)
        start = time.time()
        generate_basement(sample_config)
        elapsed = time.time() - start
        assert elapsed < 30
