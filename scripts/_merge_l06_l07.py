"""Merge lesson07 (HAVING) into lesson06 (GROUP BY) and rewire navigation.

The combined lesson is renamed "GROUP BY and HAVING" and lives in lesson06.
After running:
  - lesson07 is deleted
  - all module TOC sidebars (lessons 01-06, 08) drop the lesson07 entry,
    rename lesson06 to "GROUP BY and HAVING", and renumber lesson08 → 7
  - lesson05 / lesson06 / lesson08 navigation links are rewired
"""
from __future__ import annotations
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSON_DIR = ROOT / "pages" / "mod_06a_sql_foundation" / "mod_05_sql_foundations"

L01 = LESSON_DIR / "lesson01_what_is_sql.html"
L02 = LESSON_DIR / "lesson02_tables_rows_and_columns.html"
L03 = LESSON_DIR / "lesson03_the_select_statement.html"
L04 = LESSON_DIR / "lesson04_filtering_data_with_where.html"
L05 = LESSON_DIR / "lesson05_aggregations_count_sum_avg.html"
L06 = LESSON_DIR / "lesson06_group_by.html"
L07 = LESSON_DIR / "lesson07_filtering_groups_with_having.html"
L08 = LESSON_DIR / "lesson08_joining_tables_join.html"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write(p: Path, c: str) -> None:
    p.write_text(c, encoding="utf-8")


# -------- Shared TOC sidebar fixes (apply to lessons 01–06 and 08) --------

LESSON07_TOC_BLOCK_RE = re.compile(
    r'<a href="lesson07_filtering_groups_with_having\.html"[^>]*>\s*'
    r'<span[^>]*></span>\s*'
    r'<span class="truncate">7\. Filtering Groups with HAVING</span>\s*'
    r'</a>\s*',
    re.DOTALL,
)


def fix_toc_sidebar(content: str) -> str:
    # 1) Remove the lesson07 entry from the module list
    content, n_removed = LESSON07_TOC_BLOCK_RE.subn("", content)

    # 2) Rename lesson06 entry: "6. GROUP BY" → "6. GROUP BY and HAVING"
    content = content.replace(
        '<span class="truncate">6. GROUP BY</span>',
        '<span class="truncate">6. GROUP BY and HAVING</span>',
    )

    # 3) Renumber lesson08 entry: "8. Joining Tables (JOIN)" → "7. Joining Tables (JOIN)"
    content = content.replace(
        '<span class="truncate">8. Joining Tables (JOIN)</span>',
        '<span class="truncate">7. Joining Tables (JOIN)</span>',
    )
    return content


# -------- Lesson05-specific: next-lesson preview + bottom nav next label --------

def patch_l05(content: str) -> str:
    content = fix_toc_sidebar(content)
    # next-lesson preview heading
    content = content.replace(
        '<h3 class="text-base font-bold text-gray-800">GROUP BY</h3>',
        '<h3 class="text-base font-bold text-gray-800">GROUP BY and HAVING</h3>',
    )
    # bottom nav next label
    content = content.replace(
        'transition-colors truncate">GROUP BY</p>',
        'transition-colors truncate">GROUP BY and HAVING</p>',
    )
    return content


# -------- Lesson06-specific: hero, next-lesson section, bottom nav --------

def patch_l06(content: str) -> str:
    content = fix_toc_sidebar(content)

    # Hero: wrong lesson number "Lesson 07" → "Lesson 06"
    content = content.replace(
        '<p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson 07</p>',
        '<p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson 06</p>',
    )

    # Hero <h1>: GROUP BY → GROUP BY and HAVING
    content = content.replace(
        '<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">GROUP BY</h1>',
        '<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">GROUP BY and HAVING</h1>',
    )

    # Next-lesson section: rewrite badge + preview cards to point to lesson 7 (JOIN)
    new_next_body = (
        '    <div class="bg-white px-8 py-7 space-y-6">\n'
        '      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">\n'
        '        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">\n'
        '          <span class="text-white font-bold text-lg">7</span>\n'
        '        </span>\n'
        '        <div class="min-w-0">\n'
        '          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 5 &middot; Lesson 7</p>\n'
        '          <h3 class="text-base font-bold text-gray-800">Joining Tables (JOIN)</h3>\n'
        '          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>\n'
        '        </div>\n'
        '      </div>\n\n'
        '      <div>\n'
        '        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>\n'
        '        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">\n'
        '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
        '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
        '              <span class="iconify text-white text-sm" data-icon="fa6-solid:link"></span>\n'
        '            </span>\n'
        '            <div><p class="text-sm font-semibold text-gray-700">What an INNER JOIN Does</p></div>\n'
        '          </div>\n'
        '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
        '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
        '              <span class="iconify text-white text-sm" data-icon="fa6-solid:key"></span>\n'
        '            </span>\n'
        '            <div><p class="text-sm font-semibold text-gray-700">Joining Tables on a Shared Key</p></div>\n'
        '          </div>\n'
        '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
        '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
        '              <span class="iconify text-white text-sm" data-icon="fa6-solid:code-compare"></span>\n'
        '            </span>\n'
        '            <div><p class="text-sm font-semibold text-gray-700">INNER vs LEFT JOIN Differences</p></div>\n'
        '          </div>\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>'
    )

    # Replace the entire body of #next-lesson
    nl_body_re = re.compile(
        r'(<section id="next-lesson"[^>]*>.*?<p class="text-sm text-gray-400 leading-snug mt-0\.5 line-clamp-1">Preview of what comes next</p>\s*</div>\s*</div>\s*)'
        r'(    <div class="bg-white px-8 py-7 space-y-6">.*?</div>\s*</div>\s*</div>)\s*</section>',
        re.DOTALL,
    )

    def _repl_next(m):
        return m.group(1) + new_next_body + "\n  </div>\n</section>"

    new_content, n = nl_body_re.subn(_repl_next, content)
    if n != 1:
        raise RuntimeError(f"lesson06 next-lesson replacement matched {n} times (expected 1)")
    content = new_content

    # Bottom nav next link: lesson07 → lesson08, label "Filtering Groups with HAVING" → "Joining Tables (JOIN)"
    content = content.replace(
        '<a href="lesson07_filtering_groups_with_having.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4',
        '<a href="lesson08_joining_tables_join.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4',
    )
    content = content.replace(
        'transition-colors truncate">Filtering Groups with HAVING</p>',
        'transition-colors truncate">Joining Tables (JOIN)</p>',
    )

    # Remove the duplicate old-style chevron nav block
    old_chevron_re = re.compile(
        r'\s*<div class="flex flex-col sm:flex-row gap-3 mt-6"><a href="lesson05_aggregations_count_sum_avg\.html"'
        r'.*?fa6-solid:chevron-right"></span>\s*</a></div>',
        re.DOTALL,
    )
    content, n_chev = old_chevron_re.subn("", content)

    return content


# -------- Lesson08-specific: hero number, prev link --------

def patch_l08(content: str) -> str:
    # TOC: rewrite the active lesson08 entry so its number reads "7."
    content = content.replace(
        '<span class="truncate">8. Joining Tables (JOIN)</span>',
        '<span class="truncate">7. Joining Tables (JOIN)</span>',
    )
    # And drop the lesson07 row
    content, _ = LESSON07_TOC_BLOCK_RE.subn("", content)
    # Rename lesson06 entry
    content = content.replace(
        '<span class="truncate">6. GROUP BY</span>',
        '<span class="truncate">6. GROUP BY and HAVING</span>',
    )

    # Hero "Lesson 08" → "Lesson 07"
    content = content.replace(
        '<p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson 08</p>',
        '<p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson 07</p>',
    )

    # Bottom nav prev link: lesson07 → lesson06; label "Filtering Groups with HAVING" → "GROUP BY and HAVING"
    content = content.replace(
        '<a href="lesson07_filtering_groups_with_having.html" class="lesson-nav-link group flex-1 flex items-center gap-4',
        '<a href="lesson06_group_by.html" class="lesson-nav-link group flex-1 flex items-center gap-4',
    )
    content = content.replace(
        'transition-colors truncate">Filtering Groups with HAVING</p>',
        'transition-colors truncate">GROUP BY and HAVING</p>',
    )

    # Old chevron-style nav: same fix
    content = content.replace(
        '<a href="lesson07_filtering_groups_with_having.html" class="lesson-nav-link group flex-1 flex items-center gap-3',
        '<a href="lesson06_group_by.html" class="lesson-nav-link group flex-1 flex items-center gap-3',
    )
    content = content.replace(
        'group-hover:text-[#CB187D] transition-colors truncate">Filtering Groups with HAVING</p>',
        'group-hover:text-[#CB187D] transition-colors truncate">GROUP BY and HAVING</p>',
    )

    return content


# -------- Run --------

def run():
    # Lessons 01-04: only TOC sidebar fix
    for p in (L01, L02, L03, L04):
        before = read(p)
        after = fix_toc_sidebar(before)
        write(p, after)
        delta = "patched" if after != before else "no-op"
        print(f"  {delta:7s}  {p.name}")

    # Lesson 05: TOC + next-lesson preview + bottom nav next label
    before = read(L05)
    after = patch_l05(before)
    write(L05, after)
    print(f"  patched  {L05.name}")

    # Lesson 06: full identity rewrite
    before = read(L06)
    after = patch_l06(before)
    write(L06, after)
    print(f"  patched  {L06.name}")

    # Lesson 08: TOC + hero number + prev link
    before = read(L08)
    after = patch_l08(before)
    write(L08, after)
    print(f"  patched  {L08.name}")

    # Delete lesson07
    if L07.exists():
        os.remove(L07)
        print(f"  deleted  {L07.name}")
    else:
        print(f"  missing  {L07.name}")

    print("\n✅ Merge complete: lesson06 now covers GROUP BY and HAVING.")


if __name__ == "__main__":
    run()
