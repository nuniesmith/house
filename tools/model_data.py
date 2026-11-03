#!/usr/bin/env python3
"""Read the house model's tables (models/export.scad) into Python.

    from model_data import load
    m = load()            # dict: m["main_rooms"], m["levels"]["grade"], ...

Needs `openscad` on PATH (run under xvfb-run on a headless machine).
`python3 tools/model_data.py > model.json` writes them as JSON.
"""
import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MODELS = Path(__file__).resolve().parent.parent / "models"
PAIRS = {"levels", "stair", "pool", "spa", "theatre", "exit_stair"}   # [[name, value], ...] tables


def _lit(s):
    return ast.literal_eval(s.replace("true", "True").replace("false", "False").replace("undef", "None"))


def load():
    cmd = ["openscad"] if shutil.which("xvfb-run") is None else ["xvfb-run", "-a", "openscad"]
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "model.echo"
        subprocess.run(cmd + ["-o", str(out), str(MODELS / "export.scad")],
                       capture_output=True, text=True, check=False)
        text = out.read_text() if out.exists() else ""
    if "WARNING" in text:
        sys.exit("export.scad warnings:\n" + "\n".join(l for l in text.splitlines() if "WARNING" in l))
    data = {}
    for line in text.splitlines():
        m = re.match(r"ECHO: (\w+) = (.*)$", line)
        if m:
            v = _lit(m.group(2))
            data[m.group(1)] = dict(v) if m.group(1) in PAIRS else v
    if "main_rooms" not in data:
        sys.exit("no output from export.scad")
    return data


if __name__ == "__main__":
    json.dump(load(), sys.stdout, indent=1)
