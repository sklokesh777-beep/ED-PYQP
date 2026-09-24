# Independent audit of the Entrepreneurship Development deliverables

**Audited:** `questions_master.json`, `frequency_analysis.json`, `frequency_report.md`, and `prediction_2026.md` against all records in `paper-analysis/2018.json`, `2019.json`, `2022.json`, and `2023.json`.

## Verdict

**PASS — no discrepancy was found in the four deliverables, so no corrective edit to them was necessary.** The totals below were recomputed from the source records and normalized question/unit evidence rather than accepted from the deliverables’ summary or validation fields. Both JSON files parse successfully.

## Corpus, counting units, marks, and architecture

- Source inventory: **4 annual JSON files, 7 papers, 4 exam years (2018, 2019, 2022, 2023)**.
- Every source paper contains exactly **Q1–Q22**: **7 × 22 = 154** official parent slots.
- The sources contain **30 explicit children**: **19 case directives + 4 OR alternatives + 7 conjunctive children**.
- Conjunctive children stay within one parent-level unit. The seven Q22 parents and two OR parents are replaced by their independently assessed children: **154 − 7 − 2 + 19 + 4 = 168 units**.
- Recomputed unit types: **145 top-level slots, 19 case subquestions, 4 OR alternatives**.

| Paper | Parent slots | Explicit children | Case | OR | Conjunctive | Assessed units |
|---|---:|---:|---:|---:|---:|---:|
| 2018 Regular | 22 | 5 | 3 | 0 | 2 | 24 |
| 2018 IAF | 22 | 6 | 2 | 4 | 0 | 25 |
| 2019 Regular | 22 | 2 | 2 | 0 | 0 | 23 |
| 2019 IAF | 22 | 3 | 3 | 0 | 0 | 24 |
| 2022 IAF | 22 | 2 | 2 | 0 | 0 | 23 |
| 2023 Regular | 22 | 5 | 3 | 0 | 2 | 24 |
| 2023 Strategic Finance | 22 | 7 | 4 | 0 | 3 | 25 |
| **Total** | **154** | **30** | **19** | **4** | **7** | **168** |

- Printed child marks are retained; each OR alternative inherits its full 6-mark parent. Seven case directives have unknown shares—2018 Regular Q22(a–c), 2018 IAF Q22 directives 1–2, and 2019 Regular Q22(a–b)—within **three distinct 12-mark parent pools (36 marks)**. No equal split or zero mark was imputed.
- All seven source section rules independently reduce to the same pattern:

| Section | Offered | Answer rule | Marks each | Required |
|---|---:|---:|---:|---:|
| A | 12 | Any 10 | 1 | 10 |
| B | 5 | Any 3 | 6 | 18 |
| C | 4 | Any 2 | 15 | 30 |
| D | 1 | Compulsory | 12 | 12 |
| **Total** | **22** | **16 numbered answers** | — | **70** |

The offered inventory is **114 marks per paper** and **798 across seven papers**; the required score is **70 per paper** and **490 across the corpus**. The deliverables correctly distinguish offered exposure from attainable marks.

## Exact-repeat recomputation

After NFKC Unicode normalization, lowercasing, Unicode-punctuation removal, and whitespace collapse, the 154 parent texts produce exactly these **five** duplicate groups and no others:

| Normalized wording | Occurrences / papers | Evidence |
|---|---:|---|
| `explain the stages of entrepreneurial process` | 2 / 2 | 2018 IAF Q21; 2023 Regular Q18 |
| `what is crowd funding` | 2 / 2 | 2018 IAF Q3; 2019 Regular Q9 |
| `what is meant by intellectual property` | 2 / 2 | 2018 Regular Q5; 2023 Regular Q9 |
| `what is the meaning of tax holiday` | 2 / 2 | 2018 Regular Q8; 2023 Regular Q3 |
| `write short notes on a crowd funding b angel investing` | 2 / 2 | 2018 Regular Q13; 2023 Regular Q16 |

The 15 curated near-repeat groups also have valid unit references, source fields, occurrence totals, and distinct-paper totals; their semantic grouping remains an explicitly judgment-based layer.

## Recomputed broad themes

Broad themes were deduplicated within each assessed unit. Counts are therefore non-additive where a unit maps across themes.

| Rank | ID | Theme | Occurrences | Papers |
|---:|---|---|---:|---:|
| 1 | B05 | Business models, plans, validation, growth and exit | 37 | 7/7 |
| 2 | B04 | Ownership, venture process, legal framework and intellectual property | 24 | 7/7 |
| 3 | B01 | Entrepreneurship foundations, types, traits and development | 23 | 7/7 |
| 4 | B06 | Environment, policy, support ecosystem and technology | 22 | 7/7 |
| 5 | B08 | International entrepreneurship, market entry and trade | 21 | 7/7 |
| 6 | B07 | Entrepreneurial finance and valuation | 17 | 7/7 |
| 7 | B03 | Ideas, opportunity, innovation, marketing and strategic analysis | 14 | 6/7 |
| 8 | B02 | Women, social, green and sustainable entrepreneurship | 10 | 6/7 |
| 9 | B09 | Venture operations, people, profitability and risk | 5 | 2/7 |

All occurrence, paper, year, programme, section, known-mark, unknown-mark, and evidence fields in the nine JSON rows reconcile with the 168-unit ledger.

## Recomputed top 20 specific topics and evidence labels

Each occurrence below is one unique `(counting unit, topic)` pair. Every label was checked against its source question or independently assessed child.

1. **S24 — MSME and entrepreneurship-support institutions: 12, 7/7.** 2018 IAF Q4; 2018 IAF Q13; 2018 Regular Q11; 2018 Regular Q21; 2019 IAF Q5; 2019 IAF Q19; 2019 Regular Q18; 2022 IAF Q10; 2022 IAF Q16; 2023 Regular Q10; 2023 Regular Q14; 2023 Strategic Finance Q15.
2. **S17 — Business-plan purpose, components, formulation and evaluation: 12, 7/7.** 2018 IAF Q22 directive 1; 2018 Regular Q4; 2018 Regular Q14; 2019 IAF Q2; 2019 IAF Q14; 2019 Regular Q16; 2019 Regular Q19; 2022 IAF Q15; 2022 IAF Q22.1; 2023 Regular Q6; 2023 Regular Q20; 2023 Strategic Finance Q17.
3. **S31 — International-market entry modes: 9, 6/7.** 2018 Regular Q20; 2019 IAF Q21; 2019 Regular Q20; 2022 IAF Q11; 2022 IAF Q12; 2022 IAF Q21; 2023 Regular Q8; 2023 Regular Q21; 2023 Strategic Finance Q19.
4. **S12 — Entrepreneurial process, enterprise establishment and venture life cycle: 6, 6/7.** 2018 IAF Q21; 2018 Regular Q19; 2019 IAF Q18; 2019 Regular Q21; 2023 Regular Q18; 2023 Strategic Finance Q14.
5. **S16 — Business models, Business Model Canvas and value proposition: 10, 5/7.** 2018 IAF Q9; 2018 IAF Q12; 2018 IAF Q14 OR-2; 2018 IAF Q22 directive 1; 2019 IAF Q16; 2022 IAF Q5; 2022 IAF Q6; 2023 Regular Q2; 2023 Strategic Finance Q5; 2023 Strategic Finance Q8.
6. **S27 — Seed, angel, venture-capital and equity finance: 7, 5/7.** 2018 IAF Q20; 2018 Regular Q7; 2018 Regular Q13; 2019 IAF Q15; 2019 Regular Q6; 2019 Regular Q13; 2023 Regular Q16.
7. **S03 — Entrepreneurial traits, competencies, mindset and resilience: 6, 5/7.** 2018 Regular Q22(a); 2018 Regular Q22(c); 2019 IAF Q22(a); 2019 Regular Q17; 2022 IAF Q13; 2023 Regular Q22.2.
8. **S23 — Government policy, incentives, tax holidays and Startup India: 6, 5/7.** 2018 Regular Q8; 2019 IAF Q10; 2019 Regular Q8; 2023 Regular Q3; 2023 Regular Q19; 2023 Strategic Finance Q6.
9. **S14 — Intellectual property and protection: 6, 5/7.** 2018 IAF Q15; 2018 Regular Q5; 2019 Regular Q5; 2019 Regular Q11; 2023 Regular Q9; 2023 Strategic Finance Q13.
10. **S02 — Entrepreneur types and profiles: 5, 5/7.** 2018 IAF Q5; 2019 Regular Q1; 2022 IAF Q2; 2023 Regular Q12; 2023 Strategic Finance Q18.
11. **S33 — Trade blocs, protectionism, WTO and international trade institutions: 7, 4/7.** 2018 IAF Q16 OR-2; 2018 Regular Q2; 2018 Regular Q17; 2019 IAF Q4; 2019 IAF Q6; 2019 IAF Q8; 2022 IAF Q17.
12. **S04 — Entrepreneurship and economic, social or regional development: 5, 4/7.** 2019 IAF Q20; 2019 Regular Q3; 2019 Regular Q14; 2022 IAF Q18; 2023 Strategic Finance Q9.
13. **S18 — Feasibility, location and capital-cost estimation: 5, 4/7.** 2019 IAF Q9; 2019 Regular Q19; 2022 IAF Q4; 2022 IAF Q20; 2023 Regular Q4.
14. **S32 — Global markets, international opportunities and challenges: 5, 4/7.** 2019 IAF Q17; 2019 Regular Q7; 2019 Regular Q15; 2023 Regular Q15; 2023 Strategic Finance Q16.
15. **S13 — Startup or venture challenges, failure and recovery: 5, 4/7.** 2019 IAF Q7; 2019 Regular Q2; 2019 Regular Q12; 2023 Regular Q13; 2023 Strategic Finance Q20.
16. **S08 — Business ideas, opportunity recognition and project selection: 5, 4/7.** 2018 Regular Q3; 2018 Regular Q10; 2019 Regular Q22(a); 2022 IAF Q19; 2023 Strategic Finance Q1.
17. **S26 — Crowdfunding: 4, 4/7.** 2018 IAF Q3; 2018 Regular Q13; 2019 Regular Q9; 2023 Regular Q16.
18. **S20 — Scaling, diversification and growth strategy: 4, 4/7.** 2018 Regular Q22(b); 2019 Regular Q22(b); 2022 IAF Q22.2; 2023 Regular Q1.
19. **S10 — Entrepreneurial marketing, customers and sales forecasting: 6, 3/7.** 2018 IAF Q14 OR-1; 2018 IAF Q14 OR-2; 2018 IAF Q18; 2022 IAF Q22.2; 2023 Strategic Finance Q11; 2023 Strategic Finance Q22.3.
20. **S06 — Women entrepreneurs, gender barriers and support: 6, 3/7.** 2018 Regular Q18; 2019 IAF Q1; 2019 IAF Q13; 2019 IAF Q22(2); 2019 IAF Q22(3); 2023 Regular Q22.3.

The remaining 20 specific-topic rows were also recomputed; their counts, dimensions, mark exposure, unknown pools, and evidence records agree with `frequency_analysis.json`.

## 2026 model-paper audit

- Offered questions: **12 / 5 / 4 / 1**, numbered exactly **Q1–Q22**.
- Answer rules: **any 10 / any 3 / any 2 / compulsory Q22**.
- Section totals: **10 / 18 / 30 / 12 = 70**.
- Q22 has exactly four compulsory parts, each worth 3 marks: **3 + 3 + 3 + 3 = 12**.
- Present-module coverage is substantive rather than label-only:

| Module | Model coverage |
|---|---|
| 1 — foundations, traits, types, development | Q1–2, Q13, Q18, Q22(a) |
| 2 — ideas, opportunities, verticals, responsible innovation | Q3–4, Q14, Q19, Q22(a) |
| 3 — ownership, process, legal/compliance | Q5–6, Q15, Q22(b) |
| 4 — model, plan, prototype, scaling, impact | Q7–8, Q20, Q22(c) |
| 5 — environment, ecosystem, institutions, technology | Q9–10, Q16, Q22(d) |
| 6 — finance and global aspects | Q11–12, Q17, Q21, Q22(d) |

## Audit scope note

This audit verifies the four deliverables against every supplied paper-analysis JSON and the present Module 1–6 analyses. It does not re-transcribe the PDFs; the paper-analysis JSONs are the requested source-of-truth layer. Topic-family mapping and near-repeat grouping necessarily retain documented semantic judgment, while all resulting arithmetic and evidence references were independently recomputed.
