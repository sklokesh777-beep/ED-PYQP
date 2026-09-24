# Entrepreneurship Development Past-Paper Frequency Analysis

> **Scope and caution.** This is a descriptive analysis of seven programme-variant papers, not seven independent annual samples. It supports revision prioritisation, not statistical certainty or a guaranteed 2026 paper. The six current module analyses are used only to align names and present-syllabus scope; they are not counted as historical question evidence.

## Executive findings

- Corpus: **7 papers**, **154 official numbered slots**, and **168 conservative assessed-prompt units**.
- Every paper uses the same required-mark architecture: **Section A 10 + Section B 18 + Section C 30 + Section D 12 = 70 marks**.
- Mechanically exact top-level wording groups: **5**. Curated near-repeat task groups: **15**.
- The strongest paper-spanning topic families are business-plan formulation/evaluation and MSME/support institutions (both represented across all seven papers), followed by international-market entry and the entrepreneurial process/venture life cycle.
- High historical frequency is not a probability estimate. Programme variants from the same year may reflect shared setters/syllabi, and the current six-module structure contains topics with little historical exposure.

## Corpus and source audit

| Paper | Programme | Analysis source | Top-level slots | Required marks |
|---|---|---|---:|---:|
| 2018 Regular | BCom Regular | `.analysis/output/paper-analysis/2018.json` | 22 | 70 |
| 2018 IAF | BCom International Accounting & Finance | `.analysis/output/paper-analysis/2018.json` | 22 | 70 |
| 2019 Regular | BCom Regular | `.analysis/output/paper-analysis/2019.json` | 22 | 70 |
| 2019 IAF | BCom International Accounting & Finance | `.analysis/output/paper-analysis/2019.json` | 22 | 70 |
| 2022 IAF | BCom International Accounting & Finance | `.analysis/output/paper-analysis/2022.json` | 22 | 70 |
| 2023 Regular | BCom Regular | `.analysis/output/paper-analysis/2023.json` | 22 | 70 |
| 2023 Strategic Finance | BCom Strategic Finance | `.analysis/output/paper-analysis/2023.json` | 22 | 70 |

All four JSON files were parsed: `paper-analysis/2018.json`, `2019.json`, `2022.json`, and `2023.json`. Together they contain the seven paper records listed above.

## Counting and marks rule

1. **Official slot:** Q1–Q22 remains the unit for section choice and official marks.
2. **Thematic occurrence:** a normalized topic is counted at most once in a top-level numbered question, even if the wording repeats the topic within that question.
3. **Permitted independent units:** an explicitly assessed case subquestion or an encoded OR alternative may contribute a separate occurrence when it independently tests the topic. Thus the seven Q22 parents are replaced by 19 case directives, and the two encoded OR parents are replaced by four alternatives.
4. **Conjunctive subparts:** non-case conjunctive lists remain one top-level occurrence. For example, `2018 Regular Q13` contributes once to crowdfunding and once to angel/VC finance, but only once to their shared broad finance theme.
5. **Compound topics:** one prompt may map to more than one specific family when it genuinely tests both; within a broad theme it is deduplicated. Topic rows therefore must not be summed as if mutually exclusive.
6. **Marks:** printed child marks are used when available. OR alternatives inherit the full parent-slot marks. No equal split is invented where a case gives only a parent total; those rows report an unknown occurrence and the distinct parent-mark pool. ‘Known mark exposure’ describes offered prompts, not marks a student necessarily answered after choice. A zero in a year/programme/section mark breakdown means that occurrences exist but none has a known child allocation—not that any question carried zero marks.
7. **Papers denominator:** distinct-paper coverage is always out of **7**, while year and programme columns expose clustering among variants.

This yields `154 - 7 case parents - 2 OR parents + 19 case directives + 4 OR alternatives = 168` assessed-prompt counting units.

## Historically invariant 70-mark pattern

| Section | Questions offered | Answer rule | Marks each | Required marks | Seven-paper result |
|---|---:|---:|---:|---:|---|
| A | 12 | Answer any 10 | 1 | 10 | 7/7 identical |
| B | 5 | Answer any 3 | 6 | 18 | 7/7 identical |
| C | 4 | Answer any 2 | 15 | 30 | 7/7 identical |
| D | 1 case | Compulsory | 12 | 12 | 7/7 identical |
| **Total** | **22 numbered slots** | **16 answered slots** | — | **70** | **7/7 identical** |

The offered slot-mark inventory is 114 per paper (12 + 30 + 60 + 12), but choice reduces the required score to 70. Across seven papers that is 798 offered slot marks and 490 required marks; 798 must not be mistaken for attainable marks.

## Exact versus near-repeat wording

**Exact** means identical after only Unicode normalization, lowercasing, punctuation removal, and whitespace collapse—no synonym replacement or stemming. **Near repeat** means the assessed task and expected answer core are substantially the same but command verb, scope, context, or mark depth differs. Everything else can still recur thematically without being called a wording repeat. A near-repeat task family may contain an exact-wording subset; for that pair, exact takes precedence, and exact/near totals must not be added.

### Mechanically exact top-level wording groups

| Group | Normalized wording | Occurrences | Papers | Evidence |
|---|---|---:|---:|---|
| ER01 | explain the stages of entrepreneurial process | 2 | 2/7 | 2018 IAF Q21; 2023 Regular Q18 |
| ER02 | what is crowd funding | 2 | 2/7 | 2018 IAF Q3; 2019 Regular Q9 |
| ER03 | what is meant by intellectual property | 2 | 2/7 | 2018 Regular Q5; 2023 Regular Q9 |
| ER04 | what is the meaning of tax holiday | 2 | 2/7 | 2018 Regular Q8; 2023 Regular Q3 |
| ER05 | write short notes on a crowd funding b angel investing | 2 | 2/7 | 2018 Regular Q13; 2023 Regular Q16 |

### Curated near-repeat assessed-task groups

| Group | Common assessed task | Occurrences | Papers | Evidence |
|---|---|---:|---:|---|
| NR01 | International-market entry methods | 6 | 6/7 | 2018 Regular Q20; 2019 Regular Q20; 2019 IAF Q21; 2022 IAF Q21; 2023 Regular Q21; 2023 Strategic Finance Q19 |
| NR02 | Entrepreneurial process / steps in establishing a venture | 5 | 5/7 | 2018 Regular Q19; 2018 IAF Q21; 2019 Regular Q21; 2019 IAF Q18; 2023 Regular Q18 |
| NR03 | Entrepreneurship's contribution to economic development | 3 | 3/7 | 2019 Regular Q14; 2019 IAF Q20; 2022 IAF Q18 |
| NR04 | Purpose, importance or objectives of a business plan | 3 | 3/7 | 2018 Regular Q4; 2019 IAF Q2; 2023 Regular Q6 |
| NR05 | Business-plan content, components or functional sections | 5 | 5/7 | 2018 Regular Q14; 2019 Regular Q19; 2022 IAF Q15; 2023 Regular Q20; 2023 Strategic Finance Q17 |
| NR06 | Women entrepreneurs' problems or challenges | 3 | 3/7 | 2018 Regular Q18; 2019 IAF Q13; 2023 Regular Q22.3 |
| NR07 | Entrepreneurial traits or competencies | 5 | 5/7 | 2018 Regular Q22(a); 2019 Regular Q17; 2019 IAF Q22(a); 2022 IAF Q13; 2023 Regular Q22.2 |
| NR08 | Sources of business or project ideas | 3 | 3/7 | 2018 Regular Q10; 2022 IAF Q19; 2023 Strategic Finance Q1 |
| NR09 | Sources of fixed capital | 2 | 2/7 | 2019 Regular Q10; 2022 IAF Q8 |
| NR10 | Exit-strategy concept or selection | 3 | 2/7 | 2018 IAF Q17; 2018 IAF Q22 directive 2; 2019 IAF Q12 |
| NR11 | Challenges in international markets or trade | 2 | 2/7 | 2019 IAF Q17; 2023 Regular Q15 |
| NR12 | Types of startups | 2 | 2/7 | 2018 Regular Q15; 2023 Regular Q17 |
| NR13 | Meaning of franchising | 2 | 2/7 | 2018 Regular Q6; 2019 IAF Q11 |
| NR14 | Types of business models | 2 | 2/7 | 2019 IAF Q16; 2023 Regular Q2 |
| NR15 | Tax holiday meaning or benefit | 3 | 3/7 | 2018 Regular Q8; 2023 Regular Q3; 2023 Strategic Finance Q6 |

## Broad-theme frequency

| Rank | Broad theme | Prompt occurrences | Distinct papers | Years | Programmes | Sections | Latest | Known mark exposure* |
|---:|---|---:|---:|---|---|---|---:|---|
| 1 | Business models, plans, validation, growth and exit | 37 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C, D | 2023 | 140 + 4 unallocated occurrence(s) within 36 marks of distinct parent pool(s) |
| 2 | Ownership, venture process, legal framework and intellectual property | 24 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C | 2023 | 142 |
| 3 | Entrepreneurship foundations, types, traits and development | 23 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C, D | 2023 | 84 + 2 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 4 | Environment, policy, support ecosystem and technology | 22 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C | 2023 | 98 |
| 5 | International entrepreneurship, market entry and trade | 21 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C | 2023 | 140 |
| 6 | Entrepreneurial finance and valuation | 17 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C, D | 2023 | 63 |
| 7 | Ideas, opportunity, innovation, marketing and strategic analysis | 14 | 6/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C, D | 2023 | 61 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 8 | Women, social, green and sustainable entrepreneurship | 10 | 6/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C, D | 2023 | 37 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 9 | Venture operations, people, profitability and risk | 5 | 2/7 | 2018, 2023 | BCom International Accounting & Finance, BCom Strategic Finance | C, D | 2023 | 27 |

\*Known mark exposure is non-additive across interdisciplinary prompts and excludes unprinted case splits; see the counting rule.

## Specific-topic frequency

| Rank | Stable topic family | Occurrences | Papers | Years | Programmes | Sections | Latest (gap to 2026) | Known mark exposure* |
|---:|---|---:|---:|---|---|---|---|---|
| 1 | MSME and entrepreneurship-support institutions | 12 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C | 2023 (3y) | 74 |
| 2 | Business-plan purpose, components, formulation and evaluation | 12 | 7/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C, D | 2023 (3y) | 69 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 3 | International-market entry modes | 9 | 6/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, C | 2023 (3y) | 93 |
| 4 | Entrepreneurial process, enterprise establishment and venture life cycle | 6 | 6/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | B, C | 2023 (3y) | 81 |
| 5 | Business models, Business Model Canvas and value proposition | 10 | 5/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, D | 2023 (3y) | 19 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 6 | Seed, angel, venture-capital and equity finance | 7 | 5/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular | A, B, C | 2023 (3y) | 41 |
| 7 | Entrepreneurial traits, competencies, mindset and resilience | 6 | 5/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular | B, D | 2023 (3y) | 20 + 2 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 8 | Government policy, incentives, tax holidays and Startup India | 6 | 5/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, C | 2023 (3y) | 20 |
| 9 | Intellectual property and protection | 6 | 5/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B | 2023 (3y) | 16 |
| 10 | Entrepreneur types and profiles | 5 | 5/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, C | 2023 (3y) | 19 |
| 11 | Trade blocs, protectionism, WTO and international trade institutions | 7 | 4/7 | 2018, 2019, 2022 | BCom International Accounting & Finance, BCom Regular | A, B | 2022 (4y) | 22 |
| 12 | Entrepreneurship and economic, social or regional development | 5 | 4/7 | 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C | 2023 (3y) | 38 |
| 13 | Feasibility, location and capital-cost estimation | 5 | 4/7 | 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular | A, C | 2023 (3y) | 33 |
| 14 | Global markets, international opportunities and challenges | 5 | 4/7 | 2019, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B | 2023 (3y) | 25 |
| 15 | Startup or venture challenges, failure and recovery | 5 | 4/7 | 2019, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, B, C | 2023 (3y) | 24 |
| 16 | Business ideas, opportunity recognition and project selection | 5 | 4/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, C, D | 2023 (3y) | 18 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 17 | Crowdfunding | 4 | 4/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular | A, B | 2023 (3y) | 14 |
| 18 | Scaling, diversification and growth strategy | 4 | 4/7 | 2018, 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular | A, D | 2023 (3y) | 7 + 2 unallocated occurrence(s) within 24 marks of distinct parent pool(s) |
| 19 | Entrepreneurial marketing, customers and sales forecasting | 6 | 3/7 | 2018, 2022, 2023 | BCom International Accounting & Finance, BCom Strategic Finance | A, B, C, D | 2023 (3y) | 37 |
| 20 | Women entrepreneurs, gender barriers and support | 6 | 3/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular | A, B, C, D | 2023 (3y) | 34 |
| 21 | Forms of ownership, legal forms and family business | 4 | 3/7 | 2018, 2023 | BCom Regular, BCom Strategic Finance | A, C | 2023 (3y) | 18 |
| 22 | Exit strategies | 4 | 3/7 | 2018, 2019, 2022 | BCom International Accounting & Finance | A, B, D | 2022 (4y) | 13 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 23 | Social, green and sustainable entrepreneurship | 4 | 3/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, D | 2023 (3y) | 3 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 24 | Capital needs, sources and financial management | 3 | 3/7 | 2019, 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A, D | 2023 (3y) | 5 |
| 25 | Bootstrapping, personal, family and love money | 3 | 3/7 | 2018, 2019, 2022 | BCom International Accounting & Finance, BCom Regular | A | 2022 (4y) | 3 |
| 26 | Entrepreneur meaning, foundations, evolution and roles | 3 | 3/7 | 2022, 2023 | BCom International Accounting & Finance, BCom Regular, BCom Strategic Finance | A | 2023 (3y) | 3 |
| 27 | Entrepreneurial environment, ecosystem, incubators and accelerators | 3 | 3/7 | 2018, 2019, 2023 | BCom International Accounting & Finance, BCom Regular | A | 2023 (3y) | 3 |
| 28 | Operations, financial control, profitability and risk management | 4 | 2/7 | 2018, 2023 | BCom International Accounting & Finance, BCom Strategic Finance | C, D | 2023 (3y) | 24 |
| 29 | Startup definitions and typologies | 2 | 2/7 | 2018, 2023 | BCom Regular | B | 2023 (3y) | 12 |
| 30 | SWOT and strategic analysis | 2 | 2/7 | 2019, 2023 | BCom Regular | D | 2023 (3y) | 4 + 1 unallocated occurrence(s) within 12 marks of distinct parent pool(s) |
| 31 | Franchising as a venture or entry model | 2 | 2/7 | 2018, 2019 | BCom International Accounting & Finance, BCom Regular | A | 2019 (7y) | 2 |
| 32 | Innovation, invention and resources for innovation | 2 | 2/7 | 2018, 2022 | BCom International Accounting & Finance | A | 2022 (4y) | 2 |
| 33 | Intrapreneurship | 2 | 2/7 | 2018, 2023 | BCom Regular, BCom Strategic Finance | A | 2023 (3y) | 2 |
| 34 | Entrepreneurship measurement: GEM and TEA | 2 | 1/7 | 2018 | BCom International Accounting & Finance | A | 2018 (8y) | 2 |
| 35 | Proof of concept, prototype, MVP and pivot | 2 | 1/7 | 2018 | BCom International Accounting & Finance | A | 2018 (8y) | 2 |
| 36 | Business valuation | 1 | 1/7 | 2018 | BCom Regular | B | 2018 (8y) | 6 |
| 37 | Debt, equity, term sheets and financing instruments | 1 | 1/7 | 2018 | BCom International Accounting & Finance | B | 2018 (8y) | 6 |
| 38 | Human resources, recruitment and team formation | 1 | 1/7 | 2023 | BCom Strategic Finance | D | 2023 (3y) | 3 |
| 39 | Business technology and digital tools | 1 | 1/7 | 2023 | BCom Strategic Finance | A | 2023 (3y) | 1 |
| 40 | Registration, single-window support and legal compliance | 1 | 1/7 | 2022 | BCom International Accounting & Finance | A | 2022 (4y) | 1 |

### Evidence ledger by topic

The full machine-readable evidence—including paper, year, programme, section, question, marks basis, source ID, and source path—is in `questions_master.json` and `frequency_analysis.json`. Readable labels below make the major recurrence chains auditable.

- **MSME and entrepreneurship-support institutions (12 prompts; 7/7):** 2018 IAF Q4; 2018 IAF Q13; 2018 Regular Q11; 2018 Regular Q21; 2019 IAF Q5; 2019 IAF Q19; 2019 Regular Q18; 2022 IAF Q10; 2022 IAF Q16; 2023 Regular Q10; 2023 Regular Q14; 2023 Strategic Finance Q15.
- **Business-plan purpose, components, formulation and evaluation (12 prompts; 7/7):** 2018 IAF Q22 directive 1; 2018 Regular Q4; 2018 Regular Q14; 2019 IAF Q2; 2019 IAF Q14; 2019 Regular Q16; 2019 Regular Q19; 2022 IAF Q15; 2022 IAF Q22.1; 2023 Regular Q6; 2023 Regular Q20; 2023 Strategic Finance Q17.
- **International-market entry modes (9 prompts; 6/7):** 2018 Regular Q20; 2019 IAF Q21; 2019 Regular Q20; 2022 IAF Q11; 2022 IAF Q12; 2022 IAF Q21; 2023 Regular Q8; 2023 Regular Q21; 2023 Strategic Finance Q19.
- **Entrepreneurial process, enterprise establishment and venture life cycle (6 prompts; 6/7):** 2018 IAF Q21; 2018 Regular Q19; 2019 IAF Q18; 2019 Regular Q21; 2023 Regular Q18; 2023 Strategic Finance Q14.
- **Business models, Business Model Canvas and value proposition (10 prompts; 5/7):** 2018 IAF Q9; 2018 IAF Q12; 2018 IAF Q14 OR-2; 2018 IAF Q22 directive 1; 2019 IAF Q16; 2022 IAF Q5; 2022 IAF Q6; 2023 Regular Q2; 2023 Strategic Finance Q5; 2023 Strategic Finance Q8.
- **Seed, angel, venture-capital and equity finance (7 prompts; 5/7):** 2018 IAF Q20; 2018 Regular Q7; 2018 Regular Q13; 2019 IAF Q15; 2019 Regular Q6; 2019 Regular Q13; 2023 Regular Q16.
- **Entrepreneurial traits, competencies, mindset and resilience (6 prompts; 5/7):** 2018 Regular Q22(a); 2018 Regular Q22(c); 2019 IAF Q22(a); 2019 Regular Q17; 2022 IAF Q13; 2023 Regular Q22.2.
- **Government policy, incentives, tax holidays and Startup India (6 prompts; 5/7):** 2018 Regular Q8; 2019 IAF Q10; 2019 Regular Q8; 2023 Regular Q3; 2023 Regular Q19; 2023 Strategic Finance Q6.
- **Intellectual property and protection (6 prompts; 5/7):** 2018 IAF Q15; 2018 Regular Q5; 2019 Regular Q5; 2019 Regular Q11; 2023 Regular Q9; 2023 Strategic Finance Q13.
- **Entrepreneur types and profiles (5 prompts; 5/7):** 2018 IAF Q5; 2019 Regular Q1; 2022 IAF Q2; 2023 Regular Q12; 2023 Strategic Finance Q18.
- **Trade blocs, protectionism, WTO and international trade institutions (7 prompts; 4/7):** 2018 IAF Q16 OR-2; 2018 Regular Q2; 2018 Regular Q17; 2019 IAF Q4; 2019 IAF Q6; 2019 IAF Q8; 2022 IAF Q17.
- **Entrepreneurship and economic, social or regional development (5 prompts; 4/7):** 2019 IAF Q20; 2019 Regular Q3; 2019 Regular Q14; 2022 IAF Q18; 2023 Strategic Finance Q9.
- **Feasibility, location and capital-cost estimation (5 prompts; 4/7):** 2019 IAF Q9; 2019 Regular Q19; 2022 IAF Q4; 2022 IAF Q20; 2023 Regular Q4.
- **Global markets, international opportunities and challenges (5 prompts; 4/7):** 2019 IAF Q17; 2019 Regular Q7; 2019 Regular Q15; 2023 Regular Q15; 2023 Strategic Finance Q16.
- **Startup or venture challenges, failure and recovery (5 prompts; 4/7):** 2019 IAF Q7; 2019 Regular Q2; 2019 Regular Q12; 2023 Regular Q13; 2023 Strategic Finance Q20.
- **Business ideas, opportunity recognition and project selection (5 prompts; 4/7):** 2018 Regular Q3; 2018 Regular Q10; 2019 Regular Q22(a); 2022 IAF Q19; 2023 Strategic Finance Q1.
- **Crowdfunding (4 prompts; 4/7):** 2018 IAF Q3; 2018 Regular Q13; 2019 Regular Q9; 2023 Regular Q16.
- **Scaling, diversification and growth strategy (4 prompts; 4/7):** 2018 Regular Q22(b); 2019 Regular Q22(b); 2022 IAF Q22.2; 2023 Regular Q1.
- **Entrepreneurial marketing, customers and sales forecasting (6 prompts; 3/7):** 2018 IAF Q14 OR-1; 2018 IAF Q14 OR-2; 2018 IAF Q18; 2022 IAF Q22.2; 2023 Strategic Finance Q11; 2023 Strategic Finance Q22.3.
- **Women entrepreneurs, gender barriers and support (6 prompts; 3/7):** 2018 Regular Q18; 2019 IAF Q1; 2019 IAF Q13; 2019 IAF Q22(2); 2019 IAF Q22(3); 2023 Regular Q22.3.
- **Forms of ownership, legal forms and family business (4 prompts; 3/7):** 2018 Regular Q12; 2023 Regular Q11; 2023 Strategic Finance Q10; 2023 Strategic Finance Q21.
- **Exit strategies (4 prompts; 3/7):** 2018 IAF Q17; 2018 IAF Q22 directive 2; 2019 IAF Q12; 2022 IAF Q14.
- **Social, green and sustainable entrepreneurship (4 prompts; 3/7):** 2018 IAF Q7; 2019 Regular Q22(a); 2023 Strategic Finance Q3; 2023 Strategic Finance Q12.
- **Capital needs, sources and financial management (3 prompts; 3/7):** 2019 Regular Q10; 2022 IAF Q8; 2023 Strategic Finance Q22.2.
- **Bootstrapping, personal, family and love money (3 prompts; 3/7):** 2018 Regular Q9; 2019 IAF Q3; 2022 IAF Q7.
- **Entrepreneur meaning, foundations, evolution and roles (3 prompts; 3/7):** 2022 IAF Q1; 2023 Regular Q7; 2023 Strategic Finance Q7.
- **Entrepreneurial environment, ecosystem, incubators and accelerators (3 prompts; 3/7):** 2018 IAF Q10; 2019 Regular Q4; 2023 Regular Q5.
- **Operations, financial control, profitability and risk management (4 prompts; 2/7):** 2018 IAF Q19; 2023 Strategic Finance Q22.2; 2023 Strategic Finance Q22.3; 2023 Strategic Finance Q22.4.

## Interpretation for 2026 preparation

- **Very broad historical reach:** business planning, support institutions/MSMEs, international entry, venture process, business models, finance, and entrepreneur/development questions. These span sections rather than belonging to one fixed mark band.
- **High-mark persistence:** international entry repeatedly occupies Section C; enterprise establishment/process and business planning also recur at 15 marks or in the compulsory case. This justifies long-answer preparation, not a claim that the same questions must return.
- **Recent but programme-sensitive:** legal forms, startup challenges, digital tools, and operational case questions are especially visible in the 2023 Strategic Finance variant. Programme clustering should be treated as breadth evidence, not independent replication.
- **Current-syllabus hedge:** responsible innovation, DPDPA/data compliance, PoC/prototype/MVP, social-impact measurement, AI/IoT/AR/VR/Blockchain, cross-cultural entrepreneurship, and international regulation are explicit in the present modules but have sparse or no direct historical counterparts. They remain legitimate model-paper material despite low historical frequency.

### Current-syllabus alignment boundaries

- The historical S18 family bundles feasibility, business-location and capital-cost prompts. Feasibility is directly current; location/cost are retained as historical variants and are not represented as equally explicit present-module headings.
- The historical S13 family includes failure/recovery language. Its direct current anchors are entrepreneurial risk, resilience and scaling challenges, not a standalone turnaround unit.
- GEM/TEA remains in the historical ledger (S39), but it is not promoted into the model paper because it is not an explicit core item in the present six-module map.

## Limitations

1. Seven papers across four exam years are too few for statistical certainty, and same-year programme variants are not independent draws.
2. Historical syllabi/programme emphases differ; current-module alignment does not retroactively turn old questions into current-syllabus evidence.
3. Offered questions are analysed, not the subset any one student answered.
4. Unknown case mark splits are left unknown; multi-topic and OR evidence makes mark totals deliberately non-additive.
5. Near-repeat classification is a documented analytical judgment. Exact-repeat groups are mechanically reproducible under the stated normalization.

The accompanying `prediction_2026.md` is therefore a **predicted/model paper only**, not an official paper or guarantee.
