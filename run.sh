#!/bin/bash

# =============================================================================
# Floor Plan Generator - Run Script
# =============================================================================
# Usage:
#   ./run.sh                          # Run with default floorplan.yaml
#   ./run.sh --config floorplan.yaml  # Run with custom config file
#   ./run.sh --skip-tests             # Skip pytest and just run main.py
#   ./run.sh --tests-only             # Only run tests, don't generate
#   ./run.sh --debug                  # Enable debug grid overlay
#   ./run.sh --pdf                    # Also generate combined PDF
# =============================================================================

# 1. Define Paths
VENV_DIR="./.venv"
SCRIPT_FILE="src/main.py"
CONFIG_FILE="./config/floorplan.yaml"
SKIP_TESTS=false
TESTS_ONLY=false
DEBUG_FLAG=""
PDF_FLAG=""
EXTRA_ARGS=""

# 2. Parse Arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)
            CONFIG_FILE="$2"
            shift 2
            ;;
        --skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        --tests-only)
            TESTS_ONLY=true
            shift
            ;;
        --debug)
            DEBUG_FLAG="--debug"
            shift
            ;;
        --pdf)
            PDF_FLAG="--pdf"
            shift
            ;;
        --svg-only|--pdf-only|--png-only|--validate)
            EXTRA_ARGS="$EXTRA_ARGS $1"
            shift
            ;;
        *)
            echo "⚠️  Unknown argument: $1"
            echo ""
            echo "Usage: ./run.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --config <file>   Path to YAML config file (default: floorplan.yaml)"
            echo "  --skip-tests      Skip running pytest before generation"
            echo "  --tests-only      Only run tests, don't generate floor plans"
            echo "  --debug           Enable debug grid overlay"
            echo "  --pdf             Also generate combined PDF output"
            echo "  --svg-only        Only generate SVG files"
            echo "  --pdf-only        Only generate combined PDF"
            echo "  --png-only        Only generate PNG files (default)"
            echo "  --validate        Only validate config, don't generate"
            exit 1
            ;;
    esac
done

# 3. Create virtual environment if missing, upgrade pip, install requirements
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Virtual environment not found at $VENV_DIR — creating it..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to create virtual environment."
        echo "   Make sure python3 and the venv module are installed."
        exit 1
    fi
    echo "✅ Virtual environment created."
    echo ""
fi

# Determine python executable from venv (needed early for pip steps)
if [ -f "$VENV_DIR/bin/python" ]; then
    PYTHON="$VENV_DIR/bin/python"
elif [ -f "$VENV_DIR/Scripts/python.exe" ]; then
    PYTHON="$VENV_DIR/Scripts/python.exe"
else
    echo "❌ Error: Cannot find python executable in $VENV_DIR"
    exit 1
fi

# Upgrade pip to latest
echo "⬆️  Upgrading pip..."
"$PYTHON" -m pip install --upgrade pip --quiet
echo ""

# Install / update requirements
if [ -f "requirements.txt" ]; then
    echo "📥 Installing/updating requirements..."
    "$PYTHON" -m pip install --upgrade -r requirements.txt --quiet
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to install requirements."
        exit 1
    fi
    echo "✅ Requirements up to date."
    echo ""
else
    echo "⚠️  No requirements.txt found — skipping dependency install."
    echo ""
fi

# 4. Check if the Python script exists
if [ ! -f "$SCRIPT_FILE" ]; then
    echo "❌ Error: Script not found at $SCRIPT_FILE"
    echo "   Make sure main.py is in the 'src' folder."
    exit 1
fi

# 5. Check if the config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Error: Config file not found at $CONFIG_FILE"
    echo "   Please provide a valid YAML config file."
    echo "   Use --config <path> to specify a different config file."
    exit 1
fi

echo "============================================================"
echo "  Floor Plan Generator"
echo "============================================================"
echo "  Config: $CONFIG_FILE"
echo "  Python: $PYTHON"
echo "============================================================"
echo ""

# 6. Run Tests (unless skipped)
if [ "$SKIP_TESTS" = false ]; then
    echo "🧪 Running tests..."
    echo "------------------------------------------------------------"
    "$PYTHON" -m pytest tests/ -v --tb=short
    TEST_EXIT_CODE=$?

    if [ $TEST_EXIT_CODE -ne 0 ]; then
        echo ""
        echo "❌ Tests failed with exit code $TEST_EXIT_CODE"
        echo "   Fix the failing tests before generating floor plans."
        echo "   Use --skip-tests to bypass this check."
        exit $TEST_EXIT_CODE
    fi

    echo ""
    echo "✅ All tests passed!"
    echo "------------------------------------------------------------"
    echo ""
fi

# 7. If tests-only mode, exit here
if [ "$TESTS_ONLY" = true ]; then
    echo "✅ Tests-only mode complete."
    exit 0
fi

# 8. Run the floor plan generator
echo "🚀 Running $SCRIPT_FILE with config: $CONFIG_FILE"
echo ""

"$PYTHON" "$SCRIPT_FILE" --config "$CONFIG_FILE" $DEBUG_FLAG $PDF_FLAG $EXTRA_ARGS
RUN_EXIT_CODE=$?

echo ""
if [ $RUN_EXIT_CODE -eq 0 ]; then
    echo "✅ Done. Check the 'output' directory for generated files."
else
    echo "⚠️  Script finished with errors (exit code: $RUN_EXIT_CODE)."
fi

exit $RUN_EXIT_CODE
