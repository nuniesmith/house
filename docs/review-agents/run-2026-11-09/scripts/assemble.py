#!/usr/bin/env python3
"""Fill template.md with computed/secN.md -> ../plan_facts.md (run plan_facts.py first)."""
import re
from pathlib import Path
here = Path(__file__).resolve().parent; run = here.parent
t = (here / "template.md").read_text()
t = re.sub(r"\{\{sec(\d+)\}\}", lambda m: (run / "computed" / f"sec{m.group(1)}.md").read_text(), t)
(run / "plan_facts.md").write_text(t)
print(len(t))
