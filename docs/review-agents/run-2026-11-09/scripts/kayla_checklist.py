#!/usr/bin/env python3
"""Number every content bullet in KAYLAS-NOTES.md (K-001...) with its section path."""
import re, sys
src = sys.argv[1]
lines = open(src, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(lines) if l.strip() == "# Home Build")
section, stack, items = "General", [], []
raw = []
for l in lines[start + 1:]:
    if not l.strip():
        continue
    m = re.match(r"^(\s*)- (.*)$", l)
    if m:
        raw.append((len(m.group(1).replace("\t", "    ")), m.group(2).strip()))
    elif not l.lstrip().startswith("["):
        raw.append((-1, l.strip()))          # a top-level heading line
for i, (ind, text) in enumerate(raw):
    if ind < 0:
        section, stack = text.strip("# ").strip(), []
        continue
    while stack and stack[-1][0] >= ind:
        stack.pop()
    has_kids = i + 1 < len(raw) and raw[i + 1][0] > ind
    path = " > ".join([section] + [t for _, t in stack])
    words = len(text.split())
    heading_only = (has_kids and words <= 3) or (not has_kids and words <= 2 and section in ("Room Notes", "Room Wishlist") and not stack)
    if text and not heading_only:
        items.append((path, text))
    if has_kids:
        stack.append((ind, text.rstrip(":")))
print("| ID | Section | Item (verbatim) |\n|---|---|---|")
for n, (p, t) in enumerate(items, 1):
    print(f"| K-{n:03d} | {p} | {t.replace('|', '/')} |")
print(f"\n_{len(items)} items, numbered in note order from docs/review-agents/KAYLAS-NOTES.md._", file=sys.stderr)
