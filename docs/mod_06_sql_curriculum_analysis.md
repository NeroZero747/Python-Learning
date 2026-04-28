# SQL Foundation — Lesson Analysis & Curriculum Design

**Date:** April 27, 2026
**Source material:** 19 lessons across two sub-modules
- `pages/mod_06_sql_foundation/mod_05_sql_foundations/` — 9 lessons (Foundations)
- `pages/mod_06_sql_foundation/mod_06_advanced_sql_for_data_analysis/` — 10 lessons (Advanced)

---

## Complete Lesson Inventory

### mod_05 — SQL Foundations (9 lessons)

| # | File | Title | Read Time | Difficulty |
|---|---|---|---|---|
| 1 | `lesson01_what_is_sql.html` | What is SQL? | 5 min | Beginner |
| 2 | `lesson02_tables_rows_and_columns.html` | Tables, Rows, and Columns | 6 min | Beginner |
| 3 | `lesson03_the_select_statement.html` | The SELECT Statement | 5 min | Beginner |
| 4 | `lesson04_filtering_data_with_where.html` | Filtering Data with WHERE | 6 min | Intermediate |
| 5 | `lesson05_sorting_data_with_order_by.html` | Sorting Data with ORDER BY | 5 min | Beginner |
| 6 | `lesson06_aggregations_count_sum_avg.html` | Aggregations: COUNT, SUM, AVG | 5 min | Intermediate |
| 7 | `lesson07_group_by.html` | GROUP BY | 6 min | Intermediate |
| 8 | `lesson08_filtering_groups_with_having.html` | Filtering Groups with HAVING | 6 min | Intermediate |
| 9 | `lesson09_joining_tables_join.html` | Joining Tables (JOIN) | 8 min | Intermediate |

### mod_06 — Advanced SQL for Data Analysis (10 lessons)

| # | File | Title | Read Time | Difficulty |
|---|---|---|---|---|
| A1 | `lesson01_subqueries.html` | Subqueries | ~5 min | Advanced |
| A2 | `lesson02_common_table_expressions_ctes.html` | Common Table Expressions (CTEs) | 6 min | Advanced |
| A3 | `lesson03_window_functions_partition_by.html` | Window Functions (PARTITION BY) | 6 min | Advanced |
| A4 | `lesson04_ranking_functions.html` | Ranking Functions | 6 min | Advanced |
| A5 | `lesson05_running_totals.html` | Running Totals | 6 min | Advanced |
| A6 | `lesson06_advanced_joins.html` | Advanced Joins | 6 min | Advanced |
| A7 | `lesson07_case_statements.html` | CASE Statements | 6 min | Advanced |
| A8 | `lesson08_null_handling.html` | NULL Handling | 5 min | Advanced |
| A9 | `lesson09_query_optimization.html` | Query Optimization | 5 min | Advanced |
| A10 | `lesson10_sql_for_analytics_workflows.html` | SQL for Analytics Workflows | 5 min | Advanced |

---

## Combine Candidates

Three pairs are strong merge candidates — each shares a tight conceptual bond and at least one lesson in the pair is thin enough to absorb cleanly.

### Combine 1 — Subqueries + CTEs (A1 + A2) ✅ Low Risk

**Rationale:** Subqueries (A1) has only 1 key-concept tab — the thinnest lesson in the entire advanced module. CTEs (A2) already contains a dedicated **"CTE vs Subquery"** comparison tab, meaning it partially re-teaches A1 content anyway. Combining them as **"Nested Queries: Subqueries & CTEs"** eliminates redundancy and teaches both tools in one cognitive session (write a subquery → refactor it as a CTE).

**Risk:** Low. The topics sequence naturally and the content volume is balanced.

### Combine 2 — GROUP BY + HAVING (L7 + L8) ✅ Low Risk

**Rationale:** `HAVING` exists *only* as a complement to `GROUP BY` — it cannot be taught without it. L8's entire premise is the contrast between `WHERE` (pre-aggregation) and `HAVING` (post-aggregation). They are already taught as a conceptual pair and share the same sample data queries.

**Risk:** Low. L7 opens with "in the previous lesson you learned aggregations" and L8 opens with "WHERE filters rows, GROUP BY summarizes" — both reference each other explicitly.

### Combine 3 — Query Optimization + Analytics Workflows (A9 + A10) ✅ Low Risk

**Rationale:** Both are 5-minute read, both are best-practices capstone lessons with no new syntax. A10 is deliberately high-level and conceptual (SQL + Python, SQL for dashboards, SQL in pipelines) — a natural second act to the optimization principles in A9. Combined: **"Efficient SQL for Analytics Workflows."**

**Risk:** Low. No complex syntax in either lesson; total combined content fits well within a single lesson.

### Optional Combine — CASE Statements + NULL Handling (A7 + A8) ⚠️ Medium Risk

**Rationale:** Both are data transformation tools. `COALESCE()` is effectively shorthand for `CASE WHEN col IS NULL THEN … END`, making the concepts naturally complementary. A8 has 5 key-concept tabs (largest in the module), so if merging, the CASE section would need trimming.

**Risk:** Medium. A8 is content-heavy — monitor total lesson length. Keep separate if lesson page length is a concern.

---

## Recommended 11-Lesson Curriculum

This selection covers all three skill tiers and applies the three low-risk combinations to reduce 19 lessons down to 11.

| # | Lesson | Source | Tier | Rationale |
|---|---|---|---|---|
| 1 | **What is SQL?** | mod_05/L01 | Beginner | The only true entry point — context, vocabulary, why SQL matters |
| 2 | **Tables, Rows, and Columns** | mod_05/L02 | Beginner | Database structure is prerequisite knowledge for every SQL query |
| 3 | **The SELECT Statement** | mod_05/L03 | Beginner | First real SQL syntax; every subsequent lesson builds on `SELECT … FROM` |
| 4 | **Filtering Data with WHERE** | mod_05/L04 | Intermediate | The most-used SQL clause in practice; teaches comparison operators and `AND`/`OR` |
| 5 | **Aggregations: COUNT, SUM, AVG** | mod_05/L06 | Intermediate | Foundational analytics skill; gateway to GROUP BY |
| 6 | **GROUP BY & HAVING** *(combined)* | mod_05/L07 + L08 | Intermediate | Natural conceptual pair; HAVING is only taught in context of GROUP BY |
| 7 | **Joining Tables** | mod_05/L09 | Intermediate | INNER/LEFT JOIN — the most critical skill for working with real multi-table databases |
| 8 | **Subqueries & CTEs** *(combined)* | mod_06/A1 + A2 | Advanced | Nested query tools together; A1 is thin, A2 already references A1 |
| 9 | **Window Functions (PARTITION BY)** | mod_06/A3 | Advanced | Gateway to ranking and running totals; must stand alone as the cognitive anchor |
| 10 | **Advanced Joins** | mod_06/A6 | Advanced | Self joins, aggregated joins, multi-table chains — 3 genuinely distinct patterns |
| 11 | **CASE Statements & NULL Handling** *(combined)* | mod_06/A7 + A8 | Advanced | Data transformation pair; `COALESCE()` links both topics naturally |

### Optional 12th Lesson

| 12 | **Query Optimization & Analytics Workflows** *(combined)* | mod_06/A9 + A10 | Advanced | Capstone: write efficient SQL, then see it in a real analytics pipeline context |

---

## Lessons Omitted and Why

| Lesson | Why Omitted |
|---|---|
| **L05 — ORDER BY** | Simple one-clause concept; can be introduced as a single code block within the SELECT lesson (L03) rather than a standalone lesson |
| **A4 — Ranking Functions** | `ROW_NUMBER`, `RANK`, `DENSE_RANK` are best introduced as a practical extension within the Window Functions lesson (A3 already introduces `OVER()` and `PARTITION BY`) |
| **A5 — Running Totals** | `SUM() OVER (ORDER BY …)` is a direct application of Window Functions; can be a code example tab within A3 rather than a full lesson |

---

## Visual Curriculum Map

```
BEGINNER              INTERMEDIATE                  ADVANCED
──────────────────    ──────────────────────────    ──────────────────────────────────────
1  What is SQL?       4  WHERE Filtering             8  Subqueries & CTEs (combined)
2  Tables & DB        5  Aggregations: COUNT/SUM/AVG 9  Window Functions (PARTITION BY)
   Structure          6  GROUP BY & HAVING           10 Advanced Joins
3  SELECT Statement      (combined)                 11 CASE & NULL Handling (combined)
                      7  JOINs (INNER / LEFT)       12 Optimization & Workflows (optional)
```

---

## Reduction Summary

| Action | Lessons Saved |
|---|---|
| Combine Subqueries + CTEs | −1 |
| Combine GROUP BY + HAVING | −1 |
| Combine CASE + NULL Handling | −1 |
| Combine Optimization + Workflows | −1 |
| Omit ORDER BY (reference in SELECT) | −1 |
| Omit Ranking Functions (extend Window Functions) | −1 |
| Omit Running Totals (extend Window Functions) | −1 |
| **Total** | **19 → 11 lessons (or 12 with capstone)** |
