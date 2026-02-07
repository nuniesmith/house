#!/usr/bin/env python3
"""
Floor Plan Generator - REST API
================================
A FastAPI-based REST API that wraps the Python floor plan generator,
allowing the web interface to trigger floor plan generation and
retrieve results via HTTP endpoints.

Endpoints:
    GET  /api/health          - Health check
    GET  /api/config          - Return current config.yaml contents
    POST /api/config          - Update config.yaml
    POST /api/generate        - Generate floor plans (PNG/SVG/PDF)
    GET  /api/output/<file>   - Retrieve generated output files
    GET  /api/outputs         - List all generated output files
    POST /api/generate/svg    - Generate and return SVG inline
    POST /api/validate        - Validate a config without generating
    GET  /api/rooms           - Room summary from current config
"""

import logging
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

# Ensure src/ is on the path for local imports
sys.path.insert(0, str(Path(__file__).parent))

from generators import (
    OUTPUT_DIR,
    apply_config_settings,
    generate_all_svg,
    generate_basement,
    generate_combined_pdf,
    generate_main_floor,
    load_config,
)
from utilities import validate_config

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Floor Plan Generator API",
    description="REST API for generating and managing floor plans.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("floorplan-api")

# Resolve paths relative to the project root (one level above src/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path(os.environ.get("CONFIG_PATH", str(PROJECT_ROOT / "config.yaml")))
OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", str(OUTPUT_DIR)))

# Ensure output directory exists
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------


class ConfigUpdateBody(BaseModel):
    yaml: str


class GenerateBody(BaseModel):
    format: str = "png"
    floor: str = "both"


class GenerateSvgBody(BaseModel):
    floor: str = "both"


class ValidateBody(BaseModel):
    yaml: str = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _read_config_raw() -> str:
    """Return the raw YAML text from the config file."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")
    return CONFIG_PATH.read_text(encoding="utf-8")


def _load_config() -> dict:
    """Load and return parsed config dict."""
    return load_config(str(CONFIG_PATH))


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _make_json_safe(obj: Any) -> Any:
    """
    Recursively convert a nested dict/list structure so it is JSON
    serialisable (handles Path objects, sets, etc.).
    """
    if isinstance(obj, dict):
        return {k: _make_json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_make_json_safe(v) for v in obj]
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, set):
        return list(obj)
    return obj


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.get("/api/health")
async def health():
    """Health-check endpoint used by Docker HEALTHCHECK and monitoring."""
    config_exists = CONFIG_PATH.exists()
    output_exists = OUTPUT_PATH.exists()
    output_files = list(OUTPUT_PATH.glob("*")) if output_exists else []

    return {
        "status": "healthy",
        "timestamp": _utcnow_iso(),
        "config_file": str(CONFIG_PATH),
        "config_exists": config_exists,
        "output_dir": str(OUTPUT_PATH),
        "output_file_count": len(output_files),
        "python_version": sys.version,
    }


@app.get("/api/config")
async def get_config():
    """Return the current YAML configuration as JSON + raw YAML."""
    try:
        raw_yaml = _read_config_raw()
        parsed = _load_config()

        return {
            "status": "ok",
            "raw_yaml": raw_yaml,
            "parsed": _make_json_safe(parsed),
            "path": str(CONFIG_PATH),
            "timestamp": _utcnow_iso(),
        }
    except FileNotFoundError as exc:
        return JSONResponse(
            status_code=404,
            content={"status": "error", "message": str(exc)},
        )
    except Exception as exc:
        logger.exception("Error reading config")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(exc)},
        )


@app.post("/api/config")
async def update_config(request: Request, body: Optional[ConfigUpdateBody] = None):
    """
    Update config.yaml with new content.

    Accepts JSON body with key ``yaml`` containing the raw YAML string,
    or a raw YAML body with Content-Type text/yaml.
    """
    try:
        content_type = request.headers.get("content-type", "")

        if "application/json" in content_type:
            if body is None or body.yaml is None:
                return JSONResponse(
                    status_code=400,
                    content={
                        "status": "error",
                        "message": "JSON body must include a 'yaml' key with raw YAML text.",
                    },
                )
            yaml_content = body.yaml
        elif "text/yaml" in content_type or "text/plain" in content_type:
            raw = await request.body()
            yaml_content = raw.decode("utf-8")
        else:
            # Default: try to parse as JSON with yaml key
            try:
                data = await request.json()
                yaml_content = data.get("yaml")
                if yaml_content is None:
                    return JSONResponse(
                        status_code=415,
                        content={
                            "status": "error",
                            "message": "Unsupported Content-Type. Use application/json or text/yaml.",
                        },
                    )
            except Exception:
                return JSONResponse(
                    status_code=415,
                    content={
                        "status": "error",
                        "message": "Unsupported Content-Type. Use application/json or text/yaml.",
                    },
                )

        # Validate before writing ---
        import yaml

        try:
            parsed = yaml.safe_load(yaml_content)
        except yaml.YAMLError as ye:
            return JSONResponse(
                status_code=400,
                content={"status": "error", "message": f"Invalid YAML: {ye}"},
            )

        if parsed is None:
            return JSONResponse(
                status_code=400,
                content={"status": "error", "message": "YAML content is empty."},
            )

        warnings = validate_config(parsed)

        # Write to disk
        CONFIG_PATH.write_text(yaml_content, encoding="utf-8")
        logger.info("Config updated at %s", CONFIG_PATH)

        return {
            "status": "ok",
            "message": "Configuration updated successfully.",
            "warnings": warnings,
            "timestamp": _utcnow_iso(),
        }

    except Exception as exc:
        logger.exception("Error updating config")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(exc)},
        )


@app.post("/api/validate")
async def validate_config_endpoint(
    request: Request, body: Optional[ValidateBody] = None
):
    """
    Validate a YAML config without writing or generating anything.

    Accepts the same body formats as POST /api/config.
    """
    try:
        content_type = request.headers.get("content-type", "")

        if "application/json" in content_type and body is not None:
            yaml_text = body.yaml
        else:
            raw = await request.body()
            yaml_text = raw.decode("utf-8")

        import yaml

        try:
            parsed = yaml.safe_load(yaml_text)
        except yaml.YAMLError as ye:
            return JSONResponse(
                status_code=400,
                content={"status": "invalid", "errors": [str(ye)], "warnings": []},
            )

        if parsed is None:
            return JSONResponse(
                status_code=400,
                content={
                    "status": "invalid",
                    "errors": ["YAML content is empty."],
                    "warnings": [],
                },
            )

        warnings = validate_config(parsed)

        return {
            "status": "valid" if not warnings else "valid_with_warnings",
            "errors": [],
            "warnings": warnings,
            "room_count": len(parsed.get("main_floor", {}).get("rooms", []))
            + len(parsed.get("basement", {}).get("rooms", [])),
            "timestamp": _utcnow_iso(),
        }

    except Exception as exc:
        logger.exception("Error validating config")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(exc)},
        )


@app.post("/api/generate")
async def generate(
    body: Optional[GenerateBody] = None,
    format: Optional[str] = Query(None, alias="format"),
    floor: Optional[str] = Query(None, alias="floor"),
):
    """
    Generate floor plan outputs from the current config.yaml.

    Query parameters / JSON body options:
        format : str — ``png`` (default), ``svg``, ``pdf``, or ``all``
        floor  : str — ``main``, ``basement``, or ``both`` (default)

    Returns JSON with a list of generated file paths.
    """
    try:
        # Resolve from body first, then query params, then defaults
        fmt = "png"
        flr = "both"

        if body is not None:
            fmt = body.format.lower()
            flr = body.floor.lower()

        if format is not None:
            fmt = format.lower()
        if floor is not None:
            flr = floor.lower()

        logger.info("Generating floor plans: format=%s, floor=%s", fmt, flr)

        config = _load_config()
        apply_config_settings(config)

        generated_files: list[str] = []

        # --- PNG ---
        if fmt in ("png", "all"):
            if flr in ("main", "both"):
                path = generate_main_floor(config)
                generated_files.append(str(path))
                logger.info("Generated main floor PNG: %s", path)

            if flr in ("basement", "both"):
                path = generate_basement(config)
                generated_files.append(str(path))
                logger.info("Generated basement PNG: %s", path)

        # --- SVG ---
        if fmt in ("svg", "all"):
            svg_paths = generate_all_svg(config)
            for p in svg_paths:
                generated_files.append(str(p))
                logger.info("Generated SVG: %s", p)

        # --- PDF ---
        if fmt in ("pdf", "all"):
            path = generate_combined_pdf(config=config)
            generated_files.append(str(path))
            logger.info("Generated combined PDF: %s", path)

        return {
            "status": "ok",
            "message": f"Generated {len(generated_files)} file(s).",
            "files": generated_files,
            "format": fmt,
            "floor": flr,
            "timestamp": _utcnow_iso(),
        }

    except FileNotFoundError as exc:
        return JSONResponse(
            status_code=404,
            content={"status": "error", "message": str(exc)},
        )
    except Exception as exc:
        logger.exception("Error during generation")
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(exc),
                "traceback": traceback.format_exc(),
            },
        )


@app.post("/api/generate/svg")
async def generate_svg_inline(body: Optional[GenerateSvgBody] = None):
    """
    Generate floor plan SVGs and return them inline in the JSON response.

    This is useful for the web UI to display generated SVGs without
    needing a separate file download step.

    JSON body options:
        floor : str — ``main``, ``basement``, or ``both`` (default)
    """
    try:
        floor = (body.floor if body else "both").lower()

        config = _load_config()
        apply_config_settings(config)

        svg_results = {}

        svg_paths = generate_all_svg(config)
        for p in svg_paths:
            p = Path(p)
            name = p.stem  # e.g. "main_floor" or "basement"

            if floor == "main" and "basement" in name:
                continue
            if floor == "basement" and "main" in name:
                continue

            svg_content = p.read_text(encoding="utf-8")
            svg_results[name] = svg_content

        return {
            "status": "ok",
            "svgs": svg_results,
            "count": len(svg_results),
            "timestamp": _utcnow_iso(),
        }

    except Exception as exc:
        logger.exception("Error generating inline SVG")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(exc)},
        )


@app.get("/api/outputs")
async def list_outputs():
    """List all files currently in the output directory."""
    try:
        if not OUTPUT_PATH.exists():
            return {"status": "ok", "files": []}

        files = []
        for f in sorted(OUTPUT_PATH.iterdir()):
            if f.is_file():
                stat = f.stat()
                files.append(
                    {
                        "name": f.name,
                        "size_bytes": stat.st_size,
                        "modified": datetime.fromtimestamp(
                            stat.st_mtime, tz=timezone.utc
                        ).isoformat(),
                        "url": f"/api/output/{f.name}",
                    }
                )

        return {
            "status": "ok",
            "output_dir": str(OUTPUT_PATH),
            "files": files,
            "count": len(files),
        }

    except Exception as exc:
        logger.exception("Error listing outputs")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(exc)},
        )


@app.get("/api/output/{filename:path}")
async def get_output_file(filename: str, download: str = "false"):
    """Serve a generated output file (PNG, SVG, PDF)."""
    try:
        filepath = OUTPUT_PATH / filename

        if not filepath.exists():
            return JSONResponse(
                status_code=404,
                content={"status": "error", "message": f"File not found: {filename}"},
            )

        # Prevent directory traversal
        if not filepath.resolve().is_relative_to(OUTPUT_PATH.resolve()):
            return JSONResponse(
                status_code=403,
                content={"status": "error", "message": "Invalid path"},
            )

        # Determine media type from suffix
        suffix_map = {
            ".png": "image/png",
            ".svg": "image/svg+xml",
            ".pdf": "application/pdf",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
        }
        media_type = suffix_map.get(filepath.suffix.lower(), "application/octet-stream")

        if download.lower() == "true":
            return FileResponse(
                path=str(filepath),
                media_type=media_type,
                filename=filepath.name,
            )

        return FileResponse(
            path=str(filepath),
            media_type=media_type,
        )

    except Exception as exc:
        logger.exception("Error serving output file")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(exc)},
        )


@app.get("/api/rooms")
async def get_rooms():
    """
    Return a summary of all rooms from the current config,
    useful for the web UI to display room lists and stats.
    """
    try:
        config = _load_config()

        main_rooms = config.get("main_floor", {}).get("rooms", [])
        basement_rooms = config.get("basement", {}).get("rooms", [])

        def _summarize_room(room: dict) -> dict:
            w = room.get("width", 0)
            h = room.get("height", 0)
            return {
                "label": room.get("label", "Unknown"),
                "x": room.get("x", 0),
                "y": room.get("y", 0),
                "width": w,
                "height": h,
                "area_sqft": round(w * h, 1),
                "color": room.get("color", ""),
                "dimension_text": room.get("dimension_text", f"{w}' x {h}'"),
            }

        main_summary = [_summarize_room(r) for r in main_rooms]
        basement_summary = [_summarize_room(r) for r in basement_rooms]

        total_main = sum(r["area_sqft"] for r in main_summary)
        total_basement = sum(r["area_sqft"] for r in basement_summary)

        return {
            "status": "ok",
            "main_floor": {
                "rooms": main_summary,
                "count": len(main_summary),
                "total_sqft": round(total_main, 1),
            },
            "basement": {
                "rooms": basement_summary,
                "count": len(basement_summary),
                "total_sqft": round(total_basement, 1),
            },
            "grand_total_sqft": round(total_main + total_basement, 1),
        }

    except Exception as exc:
        logger.exception("Error reading rooms")
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(exc)},
        )


# ---------------------------------------------------------------------------
# Exception handlers
# ---------------------------------------------------------------------------


@app.exception_handler(404)
async def not_found(_request: Request, _exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"status": "error", "message": "Endpoint not found"},
    )


@app.exception_handler(405)
async def method_not_allowed(_request: Request, _exc: HTTPException):
    return JSONResponse(
        status_code=405,
        content={"status": "error", "message": "Method not allowed"},
    )


@app.exception_handler(500)
async def internal_error(_request: Request, _exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "Internal server error"},
    )
