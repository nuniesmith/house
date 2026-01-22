# =============================================================================
# Floor Plan Generator - Makefile
# =============================================================================
# Common development tasks for the floor plan generator project.
#
# Usage:
#   make help       - Show this help message
#   make install    - Install dependencies
#   make test       - Run tests
#   make lint       - Run linters
#   make format     - Format code
#   make generate   - Generate floor plans
#   make clean      - Clean generated files
# =============================================================================

.PHONY: help install install-dev test test-cov lint format type-check \
        generate generate-png generate-svg generate-pdf clean clean-output \
        clean-cache clean-all venv debug validate

# Default Python interpreter
PYTHON ?= python3
PIP ?= pip3

# Directories
SRC_DIR := src
TEST_DIR := src/tests
OUTPUT_DIR := output
VENV_DIR := .venv

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m  # No Color

# =============================================================================
# Help
# =============================================================================

help:
	@echo "$(BLUE)Floor Plan Generator - Available Commands$(NC)"
	@echo ""
	@echo "$(GREEN)Installation:$(NC)"
	@echo "  make install      Install production dependencies"
	@echo "  make install-dev  Install development dependencies"
	@echo "  make venv         Create virtual environment"
	@echo ""
	@echo "$(GREEN)Testing:$(NC)"
	@echo "  make test         Run all tests"
	@echo "  make test-cov     Run tests with coverage report"
	@echo "  make test-fast    Run tests (skip slow tests)"
	@echo ""
	@echo "$(GREEN)Code Quality:$(NC)"
	@echo "  make lint         Run all linters"
	@echo "  make format       Format code with black and isort"
	@echo "  make type-check   Run mypy type checker"
	@echo "  make check        Run all checks (lint + type-check + test)"
	@echo ""
	@echo "$(GREEN)Generation:$(NC)"
	@echo "  make generate     Generate all floor plans (PNG, SVG, PDF)"
	@echo "  make generate-png Generate PNG files only"
	@echo "  make generate-svg Generate SVG files only"
	@echo "  make generate-pdf Generate combined PDF only"
	@echo "  make debug        Generate with debug grid overlay"
	@echo "  make validate     Validate configuration only"
	@echo ""
	@echo "$(GREEN)Cleanup:$(NC)"
	@echo "  make clean        Clean all generated files and caches"
	@echo "  make clean-output Clean output directory only"
	@echo "  make clean-cache  Clean Python cache files only"

# =============================================================================
# Installation
# =============================================================================

venv:
	@echo "$(BLUE)Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "$(GREEN)Virtual environment created. Activate with:$(NC)"
	@echo "  source $(VENV_DIR)/bin/activate  (Linux/macOS)"
	@echo "  $(VENV_DIR)\\Scripts\\activate   (Windows)"

install:
	@echo "$(BLUE)Installing production dependencies...$(NC)"
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)Dependencies installed.$(NC)"

install-dev: install
	@echo "$(BLUE)Installing development dependencies...$(NC)"
	$(PIP) install pytest pytest-cov pytest-mock mypy ruff black isort pre-commit
	@echo "$(GREEN)Development dependencies installed.$(NC)"

# =============================================================================
# Testing
# =============================================================================

test:
	@echo "$(BLUE)Running tests...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) -m pytest tests -v

test-cov:
	@echo "$(BLUE)Running tests with coverage...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) -m pytest tests -v --cov=. --cov-report=term-missing --cov-report=html
	@echo "$(GREEN)Coverage report generated in htmlcov/$(NC)"

test-fast:
	@echo "$(BLUE)Running fast tests (skipping slow tests)...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) -m pytest tests -v -m "not slow"

# =============================================================================
# Code Quality
# =============================================================================

lint:
	@echo "$(BLUE)Running linters...$(NC)"
	-$(PYTHON) -m ruff check $(SRC_DIR)
	@echo "$(GREEN)Linting complete.$(NC)"

format:
	@echo "$(BLUE)Formatting code...$(NC)"
	-$(PYTHON) -m black $(SRC_DIR)
	-$(PYTHON) -m isort $(SRC_DIR)
	@echo "$(GREEN)Formatting complete.$(NC)"

type-check:
	@echo "$(BLUE)Running type checker...$(NC)"
	-cd $(SRC_DIR) && $(PYTHON) -m mypy . --ignore-missing-imports
	@echo "$(GREEN)Type checking complete.$(NC)"

check: lint type-check test
	@echo "$(GREEN)All checks passed!$(NC)"

# =============================================================================
# Generation
# =============================================================================

generate: generate-png generate-svg generate-pdf
	@echo "$(GREEN)All floor plans generated in $(OUTPUT_DIR)/$(NC)"

generate-png:
	@echo "$(BLUE)Generating PNG files...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) main.py --png-only
	@echo "$(GREEN)PNG files generated.$(NC)"

generate-svg:
	@echo "$(BLUE)Generating SVG files...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) main.py --svg-only
	@echo "$(GREEN)SVG files generated.$(NC)"

generate-pdf:
	@echo "$(BLUE)Generating PDF file...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) main.py --pdf-only
	@echo "$(GREEN)PDF file generated.$(NC)"

debug:
	@echo "$(BLUE)Generating floor plans with debug grid...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) main.py --debug
	@echo "$(GREEN)Debug floor plans generated.$(NC)"

validate:
	@echo "$(BLUE)Validating configuration...$(NC)"
	cd $(SRC_DIR) && $(PYTHON) main.py --validate
	@echo "$(GREEN)Validation complete.$(NC)"

# =============================================================================
# Cleanup
# =============================================================================

clean: clean-output clean-cache
	@echo "$(GREEN)Cleanup complete.$(NC)"

clean-output:
	@echo "$(BLUE)Cleaning output directory...$(NC)"
	rm -rf $(OUTPUT_DIR)/*.png $(OUTPUT_DIR)/*.svg $(OUTPUT_DIR)/*.pdf
	@echo "$(GREEN)Output files removed.$(NC)"

clean-cache:
	@echo "$(BLUE)Cleaning Python cache files...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "$(GREEN)Cache files removed.$(NC)"

clean-all: clean
	@echo "$(BLUE)Cleaning virtual environment...$(NC)"
	rm -rf $(VENV_DIR)
	@echo "$(GREEN)Full cleanup complete.$(NC)"

# =============================================================================
# Development Shortcuts
# =============================================================================

# Quick development cycle: format, lint, test
dev: format lint test
	@echo "$(GREEN)Development cycle complete!$(NC)"

# Watch for changes and run tests (requires pytest-watch)
watch:
	cd $(SRC_DIR) && $(PYTHON) -m pytest_watch tests

# Run the main script directly
run:
	cd $(SRC_DIR) && $(PYTHON) main.py

# Open generated PNG in default viewer (Linux)
view: generate-png
	xdg-open $(OUTPUT_DIR)/main_floor_plan.png 2>/dev/null || \
	open $(OUTPUT_DIR)/main_floor_plan.png 2>/dev/null || \
	start $(OUTPUT_DIR)/main_floor_plan.png 2>/dev/null || \
	echo "$(YELLOW)Could not open image viewer$(NC)"
