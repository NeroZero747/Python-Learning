"""Fix the #next-lesson section AND the bottom navigation bar across all
12 lessons in pages/mod_06_sql_foundation/.

For each lesson N:
  - Rebuild the `<section id="next-lesson">` preview using lesson N+1's H1
    and its first 3 #objective cards (icon + title).
  - Rebuild the bottom-nav `<section>` with correct Previous (lesson N-1) and
    Next (lesson N+1) links and the canonical hub path `../hub_home_page.html`.
  - On lesson 1: drop the Previous link (replace with a spacer div).
  - On lesson 12: replace #next-lesson preview with a "Module Complete!"
    banner and drop the Next link from the bottom nav.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "pages" / "mod_06_sql_foundation"

# Canonical lesson list. Display title may differ from H1 (used in sidebar TOC + nav).
LESSONS: list[tuple[str, str]] = [
    ("lesson01_what_is_sql.html",                    "What is SQL?"),
    ("lesson02_tables_rows_and_columns.html",        "Tables, Rows, and Columns"),
    ("lesson03_the_select_statement.html",           "SELECT &amp; ORDER BY"),
    ("lesson04_filtering_data_with_where.html",      "Filtering Data with WHERE"),
    ("lesson05_aggregations_count_sum_avg.html",     "Aggregations (COUNT, SUM, AVG)"),
    ("lesson06_group_by_having.html",                "GROUP BY and HAVING"),
    ("lesson07_joining_tables.html",                 "Joining Tables (JOIN)"),
    ("lesson08_subqueries_ctes.html",                "Subqueries and CTEs"),
    ("lesson09_window_functions_partition_by.html",  "Window Functions"),
    ("lesson10_advanced_joins.html",                 "Advanced Joins"),
    ("lesson11_case_statements.html",                "CASE Statements &amp; NULL Handling"),
    ("lesson12_query_optimization.html",             "Query Optimization"),
]
TOTAL = len(LESSONS)
HUB_HREF = "../hub_home_page.html"

OBJ_CARD_RE = re.compile(
    r'obj-card[\s\S]*?data-icon="([^"]+)"[\s\S]*?<p class="text-sm font-semibold text-gray-800">([^<]+)</p>'
)


def extract_objectives(text: str) -> list[tuple[str, str]]:
    """Return [(icon, title), ...] for the 4 #objective cards (first 3 used)."""
    m = re.search(r'<section id="objective">(.*?)</section>', text, re.DOTALL)
    if not m:
        return []
    return OBJ_CARD_RE.findall(m.group(1))


def build_next_lesson_preview(next_no: int, next_title: str, objs: list[tuple[str, str]]) -> str:
    cards: list[str] = []
    for icon, title in objs[:3]:
        cards.append(
            f'''        <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
            <span class="iconify text-white text-sm" data-icon="{icon}"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-700">{title}</p>
          </div>
        </div>'''
        )
    cards_html = "\n".join(cards)

    return f'''<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">{next_no}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 6 &middot; Lesson {next_no}</p>
          <h3 class="text-base font-bold text-gray-800">{next_title}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
{cards_html}
        </div>
      </div>
    </div>
  </div>
</section>'''


def build_module_complete_banner() -> str:
    """Replaces #next-lesson on the final lesson."""
    return '''<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:trophy"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Module Complete</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">You have finished SQL Foundation</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Module 6 Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You have completed all 12 lessons in SQL Foundation. Return to the hub to pick your next module.</p>
          </div>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">Skills You Have Mastered</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
        <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
            <span class="iconify text-white text-sm" data-icon="fa6-solid:database"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-700">Read &amp; write SQL queries</p>
          </div>
        </div>
        <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
            <span class="iconify text-white text-sm" data-icon="fa6-solid:layer-group"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-700">Aggregate, group &amp; join data</p>
          </div>
        </div>
        <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
            <span class="iconify text-white text-sm" data-icon="fa6-solid:gauge-high"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-700">Optimize &amp; tune queries</p>
          </div>
        </div>
        </div>
      </div>
    </div>
  </div>
</section>'''


def build_bottom_nav(prev: tuple[str, str] | None, nxt: tuple[str, str] | None) -> str:
    parts: list[str] = []

    if prev is not None:
        href, label = prev
        parts.append(f'''    <a href="{href}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{label}</p>
      </div>
    </a>''')
    else:
        parts.append('    <div class="flex-1"></div>')

    parts.append(f'''    <a href="{HUB_HREF}" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>''')

    if nxt is not None:
        href, label = nxt
        parts.append(f'''    <a href="{href}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{label}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>''')
    else:
        parts.append('    <div class="flex-1"></div>')

    body = "\n\n".join(parts)
    return f'''<section>
  <div class="flex flex-col sm:flex-row gap-3">

{body}

  </div>
</section>'''


# Match the entire #next-lesson section + bottom-nav section, up to (but not
# including) the </main> close. The bottom-nav section starts with a bare
# `<section>\n  <div class="flex flex-col sm:flex-row gap-3">`.
BLOCK_RE = re.compile(
    r'<section id="next-lesson"[\s\S]*?</section>\s*</main>',
    re.DOTALL,
)


def main() -> None:
    # Pre-load every file's H1 + objective list (used to build neighbour previews).
    file_data: dict[str, list[tuple[str, str]]] = {}
    for fname, _ in LESSONS:
        p = MOD_DIR / fname
        text = p.read_text(encoding="utf-8")
        file_data[fname] = extract_objectives(text)

    print(f"Fixing #next-lesson + bottom-nav in {MOD_DIR}\n")

    for idx, (fname, title) in enumerate(LESSONS):
        path = MOD_DIR / fname
        if not path.exists():
            print(f"  [missing]  {fname}")
            continue

        text = path.read_text(encoding="utf-8")

        # Build next-lesson preview
        is_last = (idx == TOTAL - 1)
        if is_last:
            next_block = build_module_complete_banner()
        else:
            next_fname, next_title = LESSONS[idx + 1]
            next_objs = file_data[next_fname]
            next_block = build_next_lesson_preview(idx + 2, next_title, next_objs)

        # Build bottom nav
        prev_pair = None if idx == 0 else (LESSONS[idx - 1][0], LESSONS[idx - 1][1])
        nxt_pair  = None if is_last else (LESSONS[idx + 1][0], LESSONS[idx + 1][1])
        nav_block = build_bottom_nav(prev_pair, nxt_pair)

        replacement = f"{next_block}\n\n{nav_block}\n\n      </main>"

        new_text, n = BLOCK_RE.subn(replacement, text, count=1)
        if n == 0:
            print(f"  [!!]  {fname}  (no-match)")
            continue
        if new_text == text:
            print(f"  [--]  {fname}  (unchanged)")
            continue
        path.write_text(new_text, encoding="utf-8")
        print(f"  [OK]  {fname}  L{idx+1:02d}  prev={'-' if prev_pair is None else prev_pair[0]}  next={'-' if nxt_pair is None else nxt_pair[0]}")


if __name__ == "__main__":
    main()
