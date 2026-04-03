"""Remove lesson11 and lesson12 from mod_03 and update all nav references.

Changes:
1. All lesson files (01-10, 13-15): Remove lesson11 & lesson12 sidebar TOC entries
2. lesson10: Replace #next-lesson preview (now points to lesson13)
3. lesson10: Replace bottom nav Next link (now points to lesson13)
4. lesson13: Update bottom nav Previous link (now points to lesson10)
5. Delete lesson11 and lesson12 HTML files
"""
import os, re

BASE = os.path.join(os.path.dirname(__file__), "..",
                    "pages", "mod_03_python_for_data_analysts")

# All lesson files EXCEPT 11 and 12
LESSON_FILES = [
    os.path.join(BASE, f"lesson{n:02d}_{slug}.html")
    for n, slug in [
        (1,  "pandas_and_dataframes"),
        (2,  "reading_files_csv_excel_json"),
        (3,  "selecting_and_filtering_data"),
        (4,  "transforming_data"),
        (5,  "aggregations_and_group_by"),
        (6,  "joining_and_merging_data"),
        (7,  "handling_missing_data"),
        (8,  "exporting_data"),
        (9,  "connecting_to_databases_and_running_sql"),
        (10, "writing_to_databases_and_managing_credentials"),
        (13, "building_and_automating_reports"),
        (14, "handling_large_data"),
        (15, "parquet_and_performance_profiling"),
    ]
]

DELETE_FILES = [
    os.path.join(BASE, "lesson11_replacing_excel_workflows_with_python.html"),
    os.path.join(BASE, "lesson12_automating_repetitive_data_tasks.html"),
]

# ── Sidebar TOC: remove the lesson11 and lesson12 <a> blocks ────────────
# Each sidebar entry is an <a> tag + 2 child lines (span dot + span label) + closing </a>
# Pattern: the <a href="lesson1[12]_..."> block and its contents up to and including </a>
SIDEBAR_11_RE = re.compile(
    r'<a href="lesson11_replacing_excel_workflows_with_python\.html"[^>]*>\s*\n'
    r'\s*<span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\s*\n'
    r'\s*<span class="truncate">11\. Replacing Excel Workflows</span>\s*\n'
    r'</a>\s*\n',
    re.MULTILINE
)

SIDEBAR_12_RE = re.compile(
    r'<a href="lesson12_automating_repetitive_data_tasks\.html"[^>]*>\s*\n'
    r'\s*<span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\s*\n'
    r'\s*<span class="truncate">12\. Automating Repetitive Tasks</span>\s*\n'
    r'</a>\s*\n',
    re.MULTILINE
)

# ── lesson10: Replace #next-lesson section content ──────────────────────
# The entire next-lesson preview block from the lesson badge through the 3-card grid
NEXT_LESSON_OLD = '''      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">11</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Lesson 11</p>
          <h3 class="text-base font-bold text-gray-800">Replacing Excel Workflows with Python</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:table"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Reproducing PivotTables with Pandas</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:code-merge"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Replacing VLOOKUP with merge()</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:file-excel"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Exporting Formatted Worksheets</p>
            </div>
          </div>
        </div>
      </div>'''

NEXT_LESSON_NEW = '''      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">11</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Lesson 11</p>
          <h3 class="text-base font-bold text-gray-800">Building &amp; Automating Reports</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:sitemap"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Structure a Report Script</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:file-lines"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Export with Multiple Sheets</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-bar"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Add Summary Statistics</p>
            </div>
          </div>
        </div>
      </div>'''

# ── lesson10: Replace bottom nav Next link ──────────────────────────────
BOTTOM_NAV_NEXT_OLD = '''    <a href="lesson11_replacing_excel_workflows_with_python.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Replacing Excel Workflows with Python</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>'''

BOTTOM_NAV_NEXT_NEW = '''    <a href="lesson13_building_and_automating_reports.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Building &amp; Automating Reports</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>'''

# ── lesson13: Replace bottom nav Previous link ──────────────────────────
BOTTOM_NAV_PREV_OLD = '''    <a href="lesson12_automating_repetitive_data_tasks.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Automating Repetitive Data Tasks</p>
      </div>
    </a>'''

BOTTOM_NAV_PREV_NEW = '''    <a href="lesson10_writing_to_databases_and_managing_credentials.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Writing to Databases &amp; Managing Credentials</p>
      </div>
    </a>'''


def main():
    # ── Step 1: Remove sidebar TOC entries from all lesson files ─────────
    print("── Step 1: Remove lesson11/12 from sidebar TOC ──")
    for fpath in LESSON_FILES:
        fname = os.path.basename(fpath)
        if not os.path.exists(fpath):
            print(f"  ⚠️  {fname} — file not found, skipping")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        original = text
        text = SIDEBAR_11_RE.sub("", text)
        text = SIDEBAR_12_RE.sub("", text)

        if text != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  ✅ {fname} — sidebar entries removed")
        else:
            print(f"  ⚠️  {fname} — no sidebar entries found")

    # ── Step 2: lesson10 — update #next-lesson preview ───────────────────
    print("\n── Step 2: Update lesson10 #next-lesson preview ──")
    l10 = os.path.join(BASE, "lesson10_writing_to_databases_and_managing_credentials.html")
    with open(l10, "r", encoding="utf-8") as f:
        text = f.read()

    if NEXT_LESSON_OLD in text:
        text = text.replace(NEXT_LESSON_OLD, NEXT_LESSON_NEW)
        print("  ✅ #next-lesson preview updated → lesson13")
    else:
        print("  ⚠️  #next-lesson preview — old text not found")

    # ── Step 3: lesson10 — update bottom nav Next link ───────────────────
    print("\n── Step 3: Update lesson10 bottom nav Next ──")
    if BOTTOM_NAV_NEXT_OLD in text:
        text = text.replace(BOTTOM_NAV_NEXT_OLD, BOTTOM_NAV_NEXT_NEW)
        print("  ✅ Bottom nav Next → lesson13")
    else:
        print("  ⚠️  Bottom nav Next — old text not found")

    with open(l10, "w", encoding="utf-8") as f:
        f.write(text)

    # ── Step 4: lesson13 — update bottom nav Previous link ───────────────
    print("\n── Step 4: Update lesson13 bottom nav Previous ──")
    l13 = os.path.join(BASE, "lesson13_building_and_automating_reports.html")
    with open(l13, "r", encoding="utf-8") as f:
        text = f.read()

    if BOTTOM_NAV_PREV_OLD in text:
        text = text.replace(BOTTOM_NAV_PREV_OLD, BOTTOM_NAV_PREV_NEW)
        with open(l13, "w", encoding="utf-8") as f:
            f.write(text)
        print("  ✅ Bottom nav Previous → lesson10")
    else:
        print("  ⚠️  Bottom nav Previous — old text not found")

    # ── Step 5: Delete lesson11 and lesson12 ─────────────────────────────
    print("\n── Step 5: Delete lesson11 and lesson12 ──")
    for fpath in DELETE_FILES:
        fname = os.path.basename(fpath)
        if os.path.exists(fpath):
            os.remove(fpath)
            print(f"  🗑️  {fname} — deleted")
        else:
            print(f"  ⚠️  {fname} — already gone")

    print("\n✅ Done. Lessons 11 & 12 removed; nav updated across all files.")


if __name__ == "__main__":
    main()
