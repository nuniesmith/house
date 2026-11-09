#!/usr/bin/env python3
"""Index every findings row (# | Severity | Location | Finding | ...) across findings files."""
import re, sys
from pathlib import Path
rows = []
for f in sys.argv[1:]:
    for line in Path(f).read_text().splitlines():
        m = re.match(r"\|\s*([A-Z]+-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if m and "Command" not in line:
            fid, sev, loc, txt = m.groups()
            sev = re.sub(r"[*_]", "", sev).strip()
            if not re.match(r"(Blocker|Should fix|Consider)", sev, re.I):
                continue
            txt = re.sub(r"<br>.*", "", re.sub(r"\*\*", "", txt))
            rows.append((fid, sev, loc[:60], txt[:170]))
order = {"blocker": 0, "should fix": 1, "consider": 2}
rows.sort(key=lambda r: (order.get(r[1].split(" (")[0].lower(), 3), r[0]))
from collections import Counter
c = Counter(r[1].split(" (")[0] for r in rows)
print(f"{len(rows)} findings: " + ", ".join(f"{k} {v}" for k, v in c.items()))
for r in rows:
    print(" | ".join(r))
