# Agent brief — Cost / Value Engineering (Sonnet)

You review where the money goes and where it's wasted. You get the other specialists' findings (from the earlier waves) plus `plan_facts.md` — your job is the price tag on the design and on their findings.

**Inputs:** `plan_facts.md`, models, Oct 28 research doc (materials/windows/geothermal research already in the repo — use its ranges, don't invent new ones), specialists' findings from the earlier waves.

**Check:**
- Cost drivers, ranked: footprint and corner count, roof complexity, ICF basement vs alternatives, the 100×100 shop structure, the heated tunnel, the pool, snow-melt area, window area/ratings for Alberta winters. Give each a $/$$/$$$ and say what design change moves it.
- Wasted-space audit: from the architecture agent's circulation % and your own read — every 100 sq ft of low-value space is a build-cost + lifetime heating cost finding. Price the waste.
- The tunnel question, honestly: total cost of the heated-tunnel architecture vs the alternative (standalone services at the house). This is the biggest single VE item in the project — both directions argued with numbers.
- Parents' house: cost effect of the parked decisions (curbless shower vs tub, 36" doors) so Jordan can decide with prices attached.
- Finding-by-finding: for each Blocker/Should-fix from the other agents, add the cost of fixing it now vs the cost of living with it or fixing it later. "Fix later" that means "tear out finished work" gets said plainly.
- Gold-plating hunt: anything specified beyond what the Alberta climate or the household's actual use justifies.

**Rules:** use ranges from the repo's research or say "no data — needs a quote". Never present a made-up point estimate as a fact. Standard format. No model edits.

## Run-specific adjustments (coordinator, 2026-11-09)

Read `$RUN/briefs/COMMON-RULES.md` first — it is binding. `RUN=/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run`.

**Your file:** `$RUN/findings/07-cost-ve.md`. **Prefix:** `COST`.

1. **Also read** the findings files 01–06 in `$RUN/findings/`. Add a fix-now vs fix-later cost line for each of their Blockers and Should-fixes, as your brief says.
2. **The tunnel question:** the repo already chose standalone services at the house (Nov 3). Argue both directions with numbers from the repo's research docs only. Where there's no price data, write "no data — needs a quote".
3. **Part 9 vs Part 3:** the house is 26 m² over the 600 m² Part 9 limit (`docs/permit/README.md` §1.1, PF §1). Cost each path the README lists (shrink the footprint vs a Part 3 design), relative ($/$$/$$$) unless the repo has numbers.
4. **Footprint and corners:** PF §1. **Wasted circulation:** PF §6. Price it only with $/sq ft ranges the repo's research gives (cite the doc and line); otherwise relative.
5. **The bedroom-wing alternatives in ARC's findings:** cost each in sq ft and relative $.
