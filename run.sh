#!/bin/bash
# ===========================================
# FloorPlan Designer - Project Runner
# ===========================================
# Simple setup for house build planning project
#
# Usage: ./run.sh [command]
#
# Commands:
#   start       - Start the application
#   stop        - Stop the application
#   restart     - Restart the application
#   build       - Build the Docker image
#   logs        - View application logs
#   status      - Show status of services
#   clean       - Clean up containers and images
#   help        - Show this help message

set -e

# ===========================================
# Configuration
# ===========================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Default port
PORT="${PORT:-8666}"

# ===========================================
# Helper Functions
# ===========================================

print_header() {
    echo -e "${CYAN}"
    echo "╔═══════════════════════════════════════════╗"
    echo "║     🏠 FloorPlan Designer                 ║"
    echo "╚═══════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker not found. Please install Docker."
        exit 1
    fi
}

# ===========================================
# Commands
# ===========================================

cmd_start() {
    print_header
    check_docker
    cd "$PROJECT_DIR"

    print_info "Starting FloorPlan Designer..."
    docker compose up -d

    print_success "Started! Access at http://localhost:$PORT"
}

cmd_stop() {
    print_header
    check_docker
    cd "$PROJECT_DIR"

    print_info "Stopping FloorPlan Designer..."
    docker compose down

    print_success "Stopped"
}

cmd_restart() {
    cmd_stop
    sleep 1
    cmd_start
}

cmd_build() {
    print_header
    check_docker
    cd "$PROJECT_DIR"

    print_info "Building Docker image..."
    docker compose build

    print_success "Build complete!"
}

cmd_logs() {
    print_header
    check_docker
    cd "$PROJECT_DIR"

    print_info "Showing logs (Ctrl+C to exit)..."
    docker compose logs -f
}

cmd_status() {
    print_header
    check_docker
    cd "$PROJECT_DIR"

    print_info "Service Status:"
    echo ""

    if docker compose ps -q 2>/dev/null | grep -q .; then
        print_success "Container is running"
        docker compose ps
    else
        print_warn "Container is not running"
    fi

    echo ""
    print_info "Access URL: http://localhost:$PORT"
}

cmd_clean() {
    print_header
    check_docker
    cd "$PROJECT_DIR"

    print_info "Cleaning up..."

    # Stop containers
    docker compose down -v --rmi local 2>/dev/null || true

    print_success "Clean complete!"
}

cmd_help() {
    print_header
    echo "Usage: ./run.sh [command]"
    echo ""
    echo "Commands:"
    echo "  start       Start the application"
    echo "  stop        Stop the application"
    echo "  restart     Restart the application"
    echo "  build       Build the Docker image"
    echo "  logs        View application logs"
    echo "  status      Show status of services"
    echo "  clean       Clean up containers and images"
    echo "  help        Show this help message"
    echo ""
    echo "Environment Variables:"
    echo "  PORT        Server port (default: 8666)"
    echo ""
    echo "Examples:"
    echo "  ./run.sh start            # Start the application"
    echo "  ./run.sh logs             # View logs"
    echo "  PORT=9000 ./run.sh start  # Start on port 9000"
}

# ===========================================
# Main Entry Point
# ===========================================

main() {
    local command="${1:-help}"

    case "$command" in
        start)      cmd_start ;;
        stop)       cmd_stop ;;
        restart)    cmd_restart ;;
        build)      cmd_build ;;
        logs)       cmd_logs ;;
        status)     cmd_status ;;
        clean)      cmd_clean ;;
        help|--help|-h)
            cmd_help
            ;;
        *)
            print_error "Unknown command: $command"
            echo ""
            cmd_help
            exit 1
            ;;
    esac
}

main "$@"
