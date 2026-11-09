# Citation check: every code citation, re-run against the code library

**Result: 188 citation rows in eight Citation logs. All 188 reproduce from the code library, and 0 were bounced.**
- 185 matched by script: page, article number and verbatim quote.
- 3 were checked by hand and relabelled, because the page prints no article number (table below).
- Cost/VE (07) made no code claims. Its single "—" row is a placeholder, not a citation.

**Substance check (Code specialist, `findings/08-code.md`, "Citation-verification appendix").** The Code specialist read each cited page against the claim it supports, covering the 147 rows from 01–06.
- 146 support their findings.
- 1 doesn't: ARC-05's conclusion that a "compliant route exists on paper" for door M28. The same Table 9.5.5.1 has a separate 810 mm row for doors into stairs to a finished floor. The review publishes ARC-05 with CODE-02's corrected conclusion (Blocker list item B7).

**How the script checks** (`scripts/verify_citations.py`): for each row it opens the cited PDF page from `~/code-library/codes.db`.
- The article's base number must be printed on that page, or on the page before it (an article that started there).
- At least 80% of the quote's words must appear on the page in order. The tolerance allows for two-column PDF text.
- The library was rebuilt in the cloud session from `docs/codes/*.pdf` (sha256 prefixes: ABC 3d45376d6c71, NPC 64180d9de6dd, NECB 5f28b6f83f9a, AEUC 5ec8f7d4a282, SOP bf192797121b). "PDF page" means the page index in the file.

## Manual adjudications

| File | Finding | Doc p. | As logged | Coordinator check | Verdict |
|---|---|---|---|---|---|
| 02-structural | STR-15 (7 rows) | abc_2023 p.667-669 | Table C-2 | p.667 prints "Table C-2 Climatic Design Data for Selected Locations in Alberta"; p.668-669 print "Table C-2 (Continued)"; all quoted rows match 100% | CONFIRMED (script fixed; now passes) |
| 04-plumbing-septic | PLB-02 | sewage p.37 | "Table (fixture units)" | Quote matches 100%. The fixture-unit table on p.37 has no printed number; it belongs to Note 1 of Table 2.2.2.2.A (p.36: "Note: Table 2.2.2.2.A. — Fixture units are a value assigned...") | CONFIRMED, relabelled "SOP 2021 Table 2.2.2.2.A Note 1 (fixture-unit values), p.37" |
| 05-electrical | ELE-12 (2 rows) | electric_2022 p.7 | "Scope" | Quote matches 100%; AEUC prints "SECTION 0 - OBJECT, SCOPE, AND DEFINITIONS ... Scope ... This Code applies to (1)(a)...(b)" with no article number | CONFIRMED, relabelled "AEUC 2022 Section 0, Scope (1)(a)-(b), p.7" |

## Script output (all rows)

| File | Finding | Doc | PDF p. | Article | On page | Quote | Verdict |
|---|---|---|---|---|---|---|---|
| 01-architecture-flow | ARC-05 | abc_2023 | 842 | Table 9.5.5.1. | yes | 100% | CONFIRMED |
| 01-architecture-flow | ARC-05 | abc_2023 | 842 | Table 9.5.5.1. | yes | 100% | CONFIRMED |
| 01-architecture-flow | ARC-21 | abc_2023 | 841 | 9.5.4.1. | yes | 100% | CONFIRMED |
| 01-architecture-flow | ARC-28 | abc_2023 | 841 | Table 9.5.3.1. | yes | 100% | CONFIRMED |
| 02-structural | STR-01 | abc_2023 | 927 | 9.15.4.2. | yes | 100% | CONFIRMED |
| 02-structural | STR-01 | abc_2023 | 928 | Table 9.15.4.2.-A | yes | 100% | CONFIRMED |
| 02-structural | STR-01 | abc_2023 | 836 | 9.4.1.1. | yes | 100% | CONFIRMED |
| 02-structural | STR-03 | abc_2023 | 967 | 9.23.4.2. | yes | 100% | CONFIRMED |
| 02-structural | STR-03 | abc_2023 | 1315 | Table 9.23.4.2.-A | yes | 100% | CONFIRMED |
| 02-structural | STR-03 | abc_2023 | 1317 | Table 9.23.4.2.-B | yes | 100% | CONFIRMED |
| 02-structural | STR-04 | abc_2023 | 40 | 1.3.3.3. | yes | 100% | CONFIRMED |
| 02-structural | STR-04 | abc_2023 | 39 | 1.3.3.2. | yes | 100% | CONFIRMED |
| 02-structural | STR-04 | abc_2023 | 43 | 1.4.1.2. | yes | 100% | CONFIRMED |
| 02-structural | STR-06 | abc_2023 | 1338 | Table 9.23.12.3.-A | yes | 100% | CONFIRMED |
| 02-structural | STR-08 | abc_2023 | 852 | 9.8.2.2. | yes | 100% | CONFIRMED |
| 02-structural | STR-08 | abc_2023 | 852 | 9.8.2.2. | yes | 100% | CONFIRMED |
| 02-structural | STR-12 | abc_2023 | 915 | 9.12.2.2. | yes | 100% | CONFIRMED |
| 02-structural | STR-13 | abc_2023 | 986 | 9.23.14.11. | yes | 100% | CONFIRMED |
| 02-structural | STR-13 | abc_2023 | 837 | 9.4.2.1. | yes | 100% | CONFIRMED |
| 02-structural | STR-14 | abc_2023 | 838 | 9.4.2.3. | yes | 100% | CONFIRMED |
| 02-structural | STR-15 | abc_2023 | 667 | Table C-2 | yes | 100% | CONFIRMED |
| 02-structural | STR-15 | abc_2023 | 667 | Table C-2 | yes | 100% | CONFIRMED |
| 02-structural | STR-15 | abc_2023 | 667 | Table C-2 | yes | 100% | CONFIRMED |
| 02-structural | STR-15 | abc_2023 | 668 | Table C-2 | yes | 100% | CONFIRMED |
| 02-structural | STR-15 | abc_2023 | 668 | Table C-2 | yes | 100% | CONFIRMED |
| 02-structural | STR-15 | abc_2023 | 669 | Table C-2 | yes | 100% | CONFIRMED |
| 02-structural | STR-15 | abc_2023 | 669 | Table C-2 | yes | 100% | CONFIRMED |
| 02-structural | STR-16 | abc_2023 | 837 | 9.4.2.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-01 | abc_2023 | 923 | 9.14.6.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-01 | abc_2023 | 923 | 9.14.6.2. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-01 | abc_2023 | 923 | 9.14.6.4. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-02 | abc_2023 | 923 | 9.14.5.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-02 | abc_2023 | 923 | 9.14.5.2. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-02 | abc_2023 | 923 | 9.14.5.3. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-02 | abc_2023 | 923 | 9.14.5.3. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-04 | sewage | 59 | 4.2.2.3. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-05 | sewage | 106 | 8.2.2.9. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-05 | sewage | 120 | 8.5.2.2. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-06 | sewage | 59 | 4.2.2.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-06 | sewage | 58 | 4.2.1.2. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-09 | sewage | 103 | 8.2.2.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-13 | sewage | 59 | 4.2.2.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-13 | sewage | 103 | 8.2.2.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-04 | abc_2023 | 923 | 9.14.6.2. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-06 | sewage | 59 | 4.2.2.3. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-16 | sewage | 103 | 8.2.2.1. | yes | 100% | CONFIRMED |
| 03-site-landscape | SITE-18 | abc_2023 | 923 | 9.14.6.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-01 | sewage | 31 | 2.1.2.6. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-01 | sewage | 31 | 2.1.2.6. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-01 | sewage | 31 | 2.1.2.6. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-05 | sewage | 31 | 2.1.2.6. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-06 | sewage | 31 | 2.1.2.6. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-06 | sewage | 39 | Table 2.2.2.3. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-02 | sewage | 36 | Table 2.2.2.2.A. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-02 | sewage | 36 | Table 2.2.2.2.A. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-02 | sewage | 36 | 2.2.2.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-18 | sewage | 31 | 2.1.2.6. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-02 | sewage | 38 | Table 2.2.2.2.B. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-02 | sewage | 37 | Table (fixture units) | no | 100% | CHECK-ARTICLE |
| 04-plumbing-septic | PLB-02 | sewage | 58 | 4.2.1.1. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-02 | sewage | 59 | Table 4.2.2.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-02 | sewage | 103 | 8.2.1.13. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-15 | sewage | 59 | 4.2.2.1. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-15 | sewage | 103 | 8.2.2.1. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-15 | sewage | 103 | 8.2.2.1. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-15 | sewage | 58 | 4.2.1.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-16 | sewage | 89 | Appendix B-7.1.1.2.(7) | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-04 | plumbing | 103 | 2.4.6.3. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-04 | plumbing | 117 | 2.5.5.5. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-03 | plumbing | 105 | 2.4.7.1.(6) | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-03 | plumbing | 105 | Table 2.4.7.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-03 | plumbing | 106 | 2.4.7.4. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-03 | plumbing | 111 | Table 2.4.10.6.-C | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-03 | plumbing | 106 | 2.4.8.1. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-12 | plumbing | 106 | 2.4.9.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-12 | plumbing | 110 | Table 2.4.10.6.-A | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-12 | plumbing | 111 | Table 2.4.10.6.-B | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-13 | plumbing | 117 | Table 2.5.6.3. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-13 | plumbing | 117 | 2.5.6.3.(3) | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-13 | plumbing | 123 | 2.5.9.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-13 | plumbing | 106 | 2.4.8.2. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-14 | plumbing | 97 | 2.3.5.3. | yes | 100% | CONFIRMED |
| 04-plumbing-septic | PLB-09 | plumbing | 108 | Note A-2.4.9.3.(3) | yes | 100% | CONFIRMED |
| 05-electrical | ELE-01 | abc_2023 | 1064 | 9.34.1.1. | yes | 100% | CONFIRMED |
| 05-electrical | ELE-02 | electric_2022 | 13 | 2-024 | yes | 100% | CONFIRMED |
| 05-electrical | ELE-02 | electric_2022 | 14 | 2-024 | prev | 100% | CONFIRMED |
| 05-electrical | ELE-02 | electric_2022 | 14 | 2-024 | prev | 100% | CONFIRMED |
| 05-electrical | ELE-04 | electric_2022 | 13 | 2-020 | yes | 100% | CONFIRMED |
| 05-electrical | ELE-04 | electric_2022 | 13 | 2-020 | yes | 100% | CONFIRMED |
| 05-electrical | ELE-05 | electric_2022 | 14 | 2-024 | prev | 100% | CONFIRMED |
| 05-electrical | ELE-12 | electric_2022 | 7 | Scope | no | 100% | CHECK-ARTICLE |
| 05-electrical | ELE-12 | electric_2022 | 7 | Scope | no | 100% | CHECK-ARTICLE |
| 05-electrical | ELE-14 | abc_2023 | 1065 | 9.34.2.1. | yes | 100% | CONFIRMED |
| 05-electrical | ELE-14 | abc_2023 | 1065 | 9.34.2.3. | yes | 100% | CONFIRMED |
| 05-electrical | ELE-14 | abc_2023 | 909 | 9.10.19.4. | yes | 100% | CONFIRMED |
| 05-electrical | ELE-15 | abc_2023 | 1064 | 9.34.1.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-01 | abc_2023 | 1057 | 9.33.5.5. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-01 | abc_2023 | 1064 | 9.33.10.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-01 | abc_2023 | 1057 | 9.33.5.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-01 | abc_2023 | 1040 | 9.31.6.4. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-03 | abc_2023 | 1057 | 9.33.5.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-03 | abc_2023 | 1086 | Table 9.36.3.10. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-03 | abc_2023 | 1086 | Table 9.36.3.10. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-04 | abc_2023 | 1083 | 9.36.3.8. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-04 | abc_2023 | 1083 | 9.36.3.8. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-04 | abc_2023 | 1083 | 9.36.3.8. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-04 | abc_2023 | 999 | A-9.25.4.2.(3) | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-04 | abc_2023 | 1041 | 9.32.1.4. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-05 | abc_2023 | 1048 | 9.32.3.8. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-05 | abc_2023 | 1048 | 9.32.3.8. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-05 | abc_2023 | 1048 | 9.32.3.7. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-05 | abc_2023 | 1048 | 9.32.3.7. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-05 | abc_2023 | 1044 | Table 9.32.3.3. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-05 | abc_2023 | 1047 | 9.32.3.5. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-05 | abc_2023 | 1041 | 9.32.1.3. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-06 | abc_2023 | 1057 | 9.33.6.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-06 | abc_2023 | 1046 | 9.32.3.4. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-06 | abc_2023 | 1055 | 9.33.3.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-06 | abc_2023 | 1056 | 9.33.4.5. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-07 | abc_2023 | 1089 | Table 9.36.4.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-07 | abc_2023 | 1090 | 9.36.4.6. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-09 | National_Energy | 149 | 5.2.8.7. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-10 | abc_2023 | 1057 | 9.33.5.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-11 | abc_2023 | 1087 | 9.36.3.10. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-11 | abc_2023 | 1087 | Table 9.36.3.10. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-13 | abc_2023 | 1056 | 9.33.4.4. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-14 | abc_2023 | 1089 | 9.36.4.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-14 | abc_2023 | 1090 | 9.36.4.4. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-14 | abc_2023 | 1089 | Table 9.36.4.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-14 | abc_2023 | 1040 | 9.31.6.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-15 | abc_2023 | 1057 | 9.33.5.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-15 | abc_2023 | 1064 | 9.33.9.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-16 | abc_2023 | 1049 | 9.32.3.9. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-16 | abc_2023 | 1049 | 9.32.3.9. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-17 | abc_2023 | 1069 | 9.36.1.3. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-17 | abc_2023 | 1106 | Table 9.36.8.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-17 | abc_2023 | 1090 | 9.36.5.2. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-17 | abc_2023 | 1040 | 9.32.1.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | GAS-18 | abc_2023 | 1055 | 9.33.1.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | National_Energy | 154 | 5.2.11.4. | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | National_Energy | 154 | 5.2.11.4. | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | National_Energy | 154 | 5.2.11.5. | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | National_Energy | 166 | Table 5.2.12.1.-O | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | National_Energy | 167 | Table 5.2.12.1.-P | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | National_Energy | 167 | Table 5.2.12.1.-P | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | National_Energy | 150 | 5.2.9.1. | yes | 100% | CONFIRMED |
| 06-gas-hvac | Tunnel | abc_2023 | 1069 | 9.36.1.3. | yes | 100% | CONFIRMED |
| 07-cost-ve | — | — | — | — | - | 0% | BOUNCED |
| 08-code | CODE-01 | abc_2023 | 852 | 9.8.3.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-01 | abc_2023 | 853 | Table 9.8.4.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-02 | abc_2023 | 842 | Table 9.5.5.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-03 | abc_2023 | 40 | 1.3.3.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-03 | abc_2023 | 43 | 1.4.1.2. | yes | 100% | CONFIRMED |
| 08-code | CODE-03 | abc_2023 | 40 | 1.3.3.4. | yes | 100% | CONFIRMED |
| 08-code | CODE-03 | abc_2023 | 40 | 1.3.3.2. | prev | 100% | CONFIRMED |
| 08-code | CODE-04 | abc_2023 | 623 | 7.2.2.4. | yes | 100% | CONFIRMED |
| 08-code | CODE-04 | abc_2023 | 622 | 7.2.1.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-04 | abc_2023 | 622 | 7.2.2.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-04 | abc_2023 | 1083 | 9.36.3.8. | yes | 100% | CONFIRMED |
| 08-code | CODE-05 | abc_2023 | 860 | 9.8.8.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-05 | abc_2023 | 859 | 9.8.8.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 887 | 9.10.9.18. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 887 | 9.10.9.18. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 886 | 9.10.9.16. | yes | 100% | CONFIRMED |
| 08-code | CODE-07 | abc_2023 | 856 | 9.8.6.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-07 | abc_2023 | 856 | 9.8.6.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-08 | abc_2023 | 873 | 9.9.10.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-08 | abc_2023 | 859 | 9.8.8.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-09 | abc_2023 | 1069 | 9.36.1.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-09 | National_Energy | 56 | 1.1.1.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-10 | abc_2023 | 47 | 1.4.1.2. | yes | 100% | CONFIRMED |
| 08-code | CODE-10 | abc_2023 | 895 | 9.10.14.4. | yes | 100% | CONFIRMED |
| 08-code | CODE-10 | abc_2023 | 900 | 9.10.15.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-11 | abc_2023 | 857 | 9.8.7.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-11 | abc_2023 | 856 | 9.8.6.2. | yes | 100% | CONFIRMED |
| 08-code | CODE-11 | abc_2023 | 851 | 9.8.1.2. | yes | 100% | CONFIRMED |
| 08-code | CODE-12 | sewage | 87 | 7.1.1.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-13 | abc_2023 | 909 | 9.10.19.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-13 | abc_2023 | 910 | 9.10.19.5. | yes | 100% | CONFIRMED |
| 08-code | CODE-13 | abc_2023 | 1049 | 9.32.3.9. | yes | 100% | CONFIRMED |
| 08-code | CODE-13 | abc_2023 | 894 | 9.10.13.15. | yes | 100% | CONFIRMED |
| 08-code | CODE-13 | abc_2023 | 921 | 9.13.4.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-13 | abc_2023 | 907 | 9.10.17.10. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 1106 | Table 9.36.8.2. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 959 | 9.22.1.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 1044 | Table 9.32.3.3. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 857 | Table 9.8.7.1. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 852 | 9.8.2.2. | yes | 100% | CONFIRMED |
| 08-code | CODE-06 | abc_2023 | 851 | 9.8.2.1. | yes | 100% | CONFIRMED |

BOUNCED: 1, CHECK-ARTICLE: 3, CONFIRMED: 185
