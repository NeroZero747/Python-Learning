"""Fix hero badges (difficulty + progress) on all 12 lessons in
pages/mod_06_sql_foundation/.

Curriculum source: docs/mod_06_sql_curriculum_analysis.md
- Module label is kept as "Module 5" (matches the track_05_sql_foundation path).
- Progress denominator is forced to /12 (12 lessons in module).
- Difficulty pill (3-dot indicator + label) is set per the curriculum:
    L01-L03  Beginner       (1 green / 2 gray)
    L04-L07  Intermediate   (2 green / 1 gray)
    L08-L12  Advanced       (3 green)
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "pages" / "mod_06_sql_foundation"

# (filename, lesson_no, difficulty)
LESSONS: list[tuple[str, int, str]] = [
    ("lesson01_what_is_sql.html",                    1,  "Beginner"),
    ("lesson02_tables_rows_and_columns.html",        2,  "Beginner"),
    ("lesson03_the_select_statement.html",           3,  "Beginner"),
    ("lesson04_filtering_data_with_where.html",      4,  "Intermediate"),
    ("lesson05_aggregations_count_sum_avg.html",     5,  "Intermediate"),
    ("lesson06_group_by_having.html",                6,  "Intermediate"),
    ("lesson07_joining_tables.html",                 7,  "Intermediate"),
    ("lesson08_subqueries_ctes.html",                8,  "Advanced"),
    ("lesson09_window_functions_partition_by.html",  9,  "Advanced"),
    ("lesson10_advanced_joins.html",                10,  "Advanced"),
    ("lesson11_case_statements.html",               11,  "Advanced"),
    ("lesson12_query_optimization.html",            12,  "Advanced"),
]
TOTAL_LESSONS = len(LESSONS)

GREEN_DOT = '<span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span>'
GRAY_DOT  = '<span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>'

DIFFICULTY_TO_DOTS = {
    "Beginner":     GREEN_DOT + GRAY_DOT  + GRAY_DOT,
    "Intermediate": GREEN_DOT + GREEN_DOT + GRAY_DOT,
    "Advanced":     GREEN_DOT + GREEN_DOT + GREEN_DOT,
}

# Regex: the difficulty pill — the inner <span class="inline-flex ..."> holding 3 dots,
# followed by " Label" (Beginner/Intermediate/Advanced) before the closing </span>.
DIFF_PILL_RE = re.compile(
    r'(<span class="inline-flex items-center gap-1">)'
    r'.*?'
    r'(</span>)\s*(?:Beginner|Intermediate|Advanced)\s*(\n\s*</span>)',
    re.DOTALL,
)

# Regex: the progress pill numerator/denominator: "<span class=\"font-extrabold\">N<span class=\"font-bold opacity-50\">/X</span></span>"
PROGRESS_RE = re.compile(
    r'(<span class="font-extrabold">)(\d+)(<span class="font-bold opacity-50">/)(\d+)(</span></span>)'
)


def fix_file(path: Path, lesson_no: int, difficulty: str) -> tuple[bool, bool]:
    text = path.read_text(encoding="utf-8")
    orig = text

    # 1) Difficulty pill
    dots = DIFFICULTY_TO_DOTS[difficulty]
    diff_replacement = rf'\g<1>{dots}\g<2> {difficulty}\g<3>'
    text, n_diff = DIFF_PILL_RE.subn(diff_replacement, text, count=1)

    # 2) Progress pill: force numerator to lesson_no, denominator to TOTAL_LESSONS
    def _prog_sub(m: re.Match[str]) -> str:
        return f'{m.group(1)}{lesson_no}{m.group(3)}{TOTAL_LESSONS}{m.group(5)}'
    text, n_prog = PROGRESS_RE.subn(_prog_sub, text, count=1)

    if text != orig:
        path.write_text(text, encoding="utf-8")
    return (n_diff > 0, n_prog > 0)


def main() -> None:
    print(f"Fixing hero badges in {MOD_DIR}\n")
    for fname, lesson_no, difficulty in LESSONS:
        p = MOD_DIR / fname
        if not p.exists():
            print(f"  [missing]  {fname}")
            continue
        diff_ok, prog_ok = fix_file(p, lesson_no, difficulty)
        flags = []
        flags.append("diff:OK"   if diff_ok else "diff:!!")
        flags.append("prog:OK"   if prog_ok else "prog:!!")
        print(f"  {fname:<46}  L{lesson_no:02d}  {difficulty:<12}  /{TOTAL_LESSONS}   [{' '.join(flags)}]")


if __name__ == "__main__":
    main()
