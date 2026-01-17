# 🏠 FloorPlan Designer

A web application for designing floor plans and calculating construction materials for our house build.

## 📋 Features

- **Interactive Floor Plan Designer** - Design rooms, walls, doors, and windows visually
- **Material Calculator** - Automatically calculate materials needed based on your floor plan
- **Cost Estimation** - Get cost estimates across different quality tiers (Economy, Standard, Premium, Luxury)
- **Multi-room Support** - Support for all room types (bedrooms, bathrooms, kitchen, garage, porches, etc.)

## 🏗️ Project Structure

```
house/
├── docker-compose.yml            # Docker Compose configuration
├── run.sh                        # Project runner script
├── docker/
│   └── Dockerfile                # Docker build file
├── config/
│   └── nginx.conf                # Nginx configuration
└── src/
    ├── html/                     # Static HTML frontend
    │   ├── index.html
    │   ├── assets/               # Static assets
    │   │   ├── farmhouse_floorplan.jpg
    │   │   ├── css/              # Stylesheets
    │   │   │   └── main.css      # Main stylesheet
    │   │   ├── js/               # JavaScript files
    │   │   └── data/             # Data files
    │   ├── components/           # UI components
    │   └── projects/             # Project-specific pages
    │       ├── farmhouse/
    │       ├── cabin/
    │       └── bunker/
    └── crates/                   # Rust libraries (for future use)
        ├── core/
        ├── backend/
        └── frontend/
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed

### Using the Run Script (Recommended)

```bash
# Make run.sh executable
chmod +x run.sh

# Start the application
./run.sh start

# View all available commands
./run.sh help
```

The application will be available at **http://localhost:8666**

### Manual Docker Commands

```bash
# Build the Docker image
docker compose build

# Start the application
docker compose up -d

# View logs
docker compose logs -f

# Stop the application
docker compose down
```

## 📜 Run Script Commands

| Command | Description |
|---------|-------------|
| `./run.sh start` | Start the application |
| `./run.sh stop` | Stop the application |
| `./run.sh restart` | Restart the application |
| `./run.sh build` | Build the Docker image |
| `./run.sh logs` | View application logs |
| `./run.sh status` | Show status of services |
| `./run.sh clean` | Clean up containers and images |
| `./run.sh help` | Show help message |

## 🌐 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8666` | Port to access the application |

Example:
```bash
PORT=9000 ./run.sh start
```

## 📁 Project Files

### HTML Frontend

The static HTML frontend is located in `src/html/` and includes:

- `index.html` - Main entry point
- `components/` - Reusable UI components (calculator, dashboard, scheduler)
- `projects/` - Project-specific pages for different house plans

### Assets

Static assets are in `src/html/assets/`:

- `farmhouse_floorplan.jpg` - Reference floor plan image
- `css/main.css` - Main stylesheet with CSS variables and common styles
- `js/` - JavaScript modules
- `data/` - Data files

### Configuration

- `config/nginx.conf` - Nginx web server configuration with caching and security headers

## 🏠 House Projects

This tool supports multiple house project configurations:

- **Farmhouse** - Main house build project
- **Cabin** - Cabin/guest house planning
- **Bunker** - Storage/utility building

## 📄 License

Personal project for house build planning.