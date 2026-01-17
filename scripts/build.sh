#!/bin/bash

# FloorPlan Designer - Build Script
# This script builds the Rust web application including both backend and WASM frontend

set -e

echo "🏠 FloorPlan Designer - Build Script"
echo "======================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check for required tools
check_requirements() {
    echo -e "\n${YELLOW}Checking requirements...${NC}"

    if ! command -v cargo &> /dev/null; then
        echo -e "${RED}Error: cargo is not installed. Please install Rust.${NC}"
        exit 1
    fi
    echo "  ✓ cargo found"

    if ! command -v wasm-pack &> /dev/null; then
        echo -e "${YELLOW}  ⚠ wasm-pack not found. Installing...${NC}"
        cargo install wasm-pack
    fi
    echo "  ✓ wasm-pack found"

    if ! command -v trunk &> /dev/null; then
        echo -e "${YELLOW}  ⚠ trunk not found. Installing...${NC}"
        cargo install trunk
    fi
    echo "  ✓ trunk found"

    # Check for wasm32 target
    if ! rustup target list --installed | grep -q "wasm32-unknown-unknown"; then
        echo -e "${YELLOW}  ⚠ wasm32-unknown-unknown target not found. Installing...${NC}"
        rustup target add wasm32-unknown-unknown
    fi
    echo "  ✓ wasm32-unknown-unknown target installed"
}

# Build the core library
build_core() {
    echo -e "\n${YELLOW}Building core library...${NC}"
    cargo build --package floorplan-core --release
    echo -e "${GREEN}  ✓ Core library built${NC}"
}

# Build the backend
build_backend() {
    echo -e "\n${YELLOW}Building backend server...${NC}"
    cargo build --package floorplan-backend --release
    echo -e "${GREEN}  ✓ Backend built${NC}"
}

# Build the WASM frontend
build_frontend() {
    echo -e "\n${YELLOW}Building WASM frontend...${NC}"

    cd crates/frontend

    # Build with trunk for development or wasm-pack for production
    if [ "$1" == "dev" ]; then
        trunk build
    else
        trunk build --release
    fi

    cd ../..

    # Copy built files to backend static directory
    if [ -d "crates/frontend/dist" ]; then
        cp -r crates/frontend/dist/* crates/backend/static/
    fi

    echo -e "${GREEN}  ✓ Frontend built${NC}"
}

# Run tests
run_tests() {
    echo -e "\n${YELLOW}Running tests...${NC}"
    cargo test --workspace
    echo -e "${GREEN}  ✓ All tests passed${NC}"
}

# Development mode - watch for changes
dev_mode() {
    echo -e "\n${YELLOW}Starting development mode...${NC}"
    echo "  Backend will run on http://localhost:3000"
    echo "  Press Ctrl+C to stop"

    # Start backend in background
    cargo run --package floorplan-backend &
    BACKEND_PID=$!

    # Cleanup on exit
    trap "kill $BACKEND_PID 2>/dev/null" EXIT

    # Watch frontend for changes
    cd crates/frontend
    trunk watch
}

# Production build
prod_build() {
    check_requirements
    build_core
    build_frontend "release"
    build_backend

    echo -e "\n${GREEN}======================================"
    echo "Build complete!"
    echo "======================================"
    echo -e "Binary location: target/release/floorplan-backend${NC}"
    echo ""
    echo "To run the server:"
    echo "  ./target/release/floorplan-backend"
    echo ""
    echo "Server will be available at http://localhost:3000"
}

# Show help
show_help() {
    echo "Usage: ./scripts/build.sh [command]"
    echo ""
    echo "Commands:"
    echo "  build     Build everything for production (default)"
    echo "  dev       Start development mode with hot reload"
    echo "  test      Run all tests"
    echo "  core      Build only the core library"
    echo "  backend   Build only the backend"
    echo "  frontend  Build only the frontend"
    echo "  clean     Clean build artifacts"
    echo "  help      Show this help message"
}

# Clean build artifacts
clean() {
    echo -e "\n${YELLOW}Cleaning build artifacts...${NC}"
    cargo clean
    rm -rf crates/frontend/dist
    echo -e "${GREEN}  ✓ Clean complete${NC}"
}

# Main script
case "${1:-build}" in
    build)
        prod_build
        ;;
    dev)
        check_requirements
        dev_mode
        ;;
    test)
        run_tests
        ;;
    core)
        build_core
        ;;
    backend)
        build_backend
        ;;
    frontend)
        build_frontend "$2"
        ;;
    clean)
        clean
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        show_help
        exit 1
        ;;
esac
