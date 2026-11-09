#!/usr/bin/env python3
"""Re-check specialists' Citation log tables against the code library (codes.db).

    verify_citations.py findings/*.md            # markdown report on stdout

For every row | Finding | Command | Doc | PDF page | Article as printed | Quote |
  * the doc prefix must resolve to one library document and the page must exist;
  * the article's base number (e.g. 9.10.15.4) must be printed on that page,
    or on the page before it (an article that starts on the previous page);
  * the quote's words must appear on the page in order (>= 80 % of them inside a
    window, which tolerates the two-column interleaving of pdftotext -layout).
Verdicts: CONFIRMED, CHECK-ARTICLE (quote found, number not on page/prev page),
CHECK-QUOTE (number found, quote not), BOUNCED (neither, or bad doc/page).
"""
import re
import sqlite3
import sys
from pathlib import Path

DB = Path.home() / "code-library" / "codes.db"
con = sqlite3.connect(DB)
STEMS = [r[0] for r in con.execute("select stem from docs")]


def norm_words(s):
    s = s.lower().replace("’", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    return re.findall(r"[a-z0-9]+(?:[.'][a-z0-9]+)*", s)


def page_text(stem, n):
    row = con.execute("select body from pages where doc=? and page=?", (stem, n)).fetchone()
    return row[0] if row else None


def quote_score(quote, text):
    q, t = norm_words(quote), norm_words(text)
    if not q:
        return 0.0
    best = 0
    window = max(60, 6 * len(q))
    for start, tok in enumerate(t):
        if tok != q[0] and (len(q) < 2 or tok != q[1]):
            continue
        qi, hits = 0, 0
        for tok2 in t[start:start + window]:
            if qi < len(q) and tok2 == q[qi]:
                hits += 1
                qi += 1
        best = max(best, hits)
        if best == len(q):
            break
    return best / len(q)


def base_article(a):
    m = re.search(r"[A-Z]?-?\d+(?:[.\-]\d+)+", a)
    return m.group(0).rstrip(".") if m else None


def on_page(base, text):
    if not base or not text:
        return False
    flat = re.sub(r"\s+", "", text)
    return base in flat


def rows(md):
    lines = md.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if re.match(r"#+\s*Citation log", l, re.I))
    except StopIteration:
        return
    for l in lines[start + 1:]:
        if re.match(r"#+\s", l):
            break
        if not l.startswith("|") or re.match(r"\|\s*-+", l) or "Finding" in l and "Command" in l:
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 6:
            yield None, l
            continue
        yield cells[:5] + [" | ".join(cells[5:])], l


def main():
    out = ["| File | Finding | Doc | PDF p. | Article | On page | Quote | Verdict |", "|---|---|---|---|---|---|---|---|"]
    tally = {}
    for f in sys.argv[1:]:
        for cells, raw in rows(Path(f).read_text()):
            name = Path(f).stem
            if cells is None:
                out.append(f"| {name} | (unparsed row) | | | | | | BOUNCED |")
                tally["BOUNCED"] = tally.get("BOUNCED", 0) + 1
                continue
            fid, cmd, doc, page, art, quote = cells
            quote = quote.strip("`\"' ")
            stems = [s for s in STEMS if s.lower().startswith(doc.strip("` ").lower())] if doc else []
            pnum = re.sub(r"\D", "", page)
            verdict, where, score = "BOUNCED", "-", 0.0
            if len(stems) == 1 and pnum:
                n = int(pnum)
                text = page_text(stems[0], n)
                if text is not None:
                    base = base_article(art)
                    if on_page(base, text):
                        where = "yes"
                    elif on_page(base, page_text(stems[0], n - 1) or ""):
                        where = "prev"
                    else:
                        where = "no"
                    score = quote_score(quote, text)
                    if where != "no" and score >= 0.8:
                        verdict = "CONFIRMED"
                    elif score >= 0.8:
                        verdict = "CHECK-ARTICLE"
                    elif where != "no":
                        verdict = "CHECK-QUOTE"
            tally[verdict] = tally.get(verdict, 0) + 1
            out.append(f"| {name} | {fid} | {doc} | {page} | {art} | {where} | {score:.0%} | {verdict} |")
    print("\n".join(out))
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(tally.items())))


if __name__ == "__main__":
    main()
