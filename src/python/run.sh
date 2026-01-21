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

# Run the floor plan generator
echo "Running floor plan generator..."
$PYTHON floor_plan_generator.py
