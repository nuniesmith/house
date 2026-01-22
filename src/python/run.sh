#!/bin/bash

# Navigate to script directory
cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Determine the correct python path (handles different OS structures)
if [ -f ".venv/bin/python" ]; then
    PYTHON=".venv/bin/python"
elif [ -f ".venv/Scripts/python.exe" ]; then
    PYTHON=".venv/Scripts/python.exe"
else
    echo "Error: Could not find Python in virtual environment"
    exit 1
fi

# Update/install requirements using python -m pip (more reliable)
echo "Installing/updating dependencies..."
$PYTHON -m pip install -q -r requirements.txt

# Add src to PYTHONPATH for imports
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Parse arguments for --skip-tests flag
SKIP_TESTS=false
PROGRAM_ARGS=()

for arg in "$@"; do
    case $arg in
        --skip-tests)
            SKIP_TESTS=true
            ;;
        --help|-h)
            echo "Usage: ./run.sh [OPTIONS] [PROGRAM_ARGS]"
            echo ""
            echo "Options:"
            echo "  --skip-tests    Skip running tests before the program"
            echo "  --help, -h      Show this help message"
            echo ""
            echo "Program Arguments (passed to main.py):"
            echo "  --png-only      Only generate PNG files"
            echo "  --svg-only      Only generate SVG files"
            echo "  --pdf-only      Only generate combined PDF"
            echo "  --debug         Enable debug mode with grid overlay"
            echo "  --validate      Only validate config, don't generate"
            echo "  --config FILE   Path to custom config file"
            echo ""
            echo "Examples:"
            echo "  ./run.sh                    # Run tests then generate all formats"
            echo "  ./run.sh --skip-tests       # Skip tests, generate all formats"
            echo "  ./run.sh --svg-only         # Run tests then generate SVG only"
            echo "  ./run.sh --skip-tests --debug  # Skip tests, generate with debug grid"
            exit 0
            ;;
        *)
            PROGRAM_ARGS+=("$arg")
            ;;
    esac
done

# Run tests first (unless skipped)
if [ "$SKIP_TESTS" = false ]; then
    echo ""
    echo "========================================"
    echo "Running Tests"
    echo "========================================"
    echo ""

    $PYTHON -m pytest src/tests/ -v --tb=short
    TEST_EXIT_CODE=$?

    if [ $TEST_EXIT_CODE -ne 0 ]; then
        echo ""
        echo "========================================"
        echo "Tests failed! (exit code: $TEST_EXIT_CODE)"
        echo "Fix the failing tests or use --skip-tests to bypass."
        echo "========================================"
        exit $TEST_EXIT_CODE
    fi

    echo ""
    echo "========================================"
    echo "All tests passed!"
    echo "========================================"
    echo ""
fi

# Run the floor plan generator
echo "Running floor plan generator..."
$PYTHON src/main.py "${PROGRAM_ARGS[@]}"
