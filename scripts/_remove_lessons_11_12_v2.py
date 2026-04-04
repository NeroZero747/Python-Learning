"""
Remove lesson11_building_and_automating_reports.html and lesson12_handling_large_data.html
from mod_03. Rename lesson13 → lesson11. Update TOC, nav, hero, and progress in all files.
"""
import os, re, shutil

FOLDER = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_03_python_for_data_analysts"

OLD_11 = "lesson11_building_and_automating_reports.html"
OLD_12 = "lesson12_handling_large_data.html"
OLD_13 = "lesson13_parquet_and_performance_profiling.html"
NEW_11 = "lesson11_parquet_and_performance_profiling.html"

# All files that will remain after deletion (before rename)
REMAINING = [
    "lesson01_pandas_and_dataframes.html",
    "lesson02_reading_files_csv_excel_json.html",
    "lesson03_selecting_and_filtering_data.html",
    "lesson04_transforming_data.html",
    "lesson05_aggregations_and_group_by.html",
    "lesson06_joining_and_merging_data.html",
    "lesson07_handling_missing_data.html",
    "lesson08_exporting_data.html",
    "lesson09_connecting_to_databases_and_running_sql.html",
    "lesson10_writing_to_databases_and_managing_credentials.html",
    OLD_13,  # will be renamed after patching
]

TOTAL_LESSONS = 11

# ─── Helper: remove a TOC <a> block for a given href ───────────────────
def remove_toc_entry(content, href):
    """Remove the 4-line <a href="...">...</a> block from the TOC lesson list."""
    pattern = (
        r'\n?\s*<a href="' + re.escape(href) + r'"'
        r' class="flex items-center gap-2 px-3 py-2 rounded-lg border[^"]*"[^>]*>\s*'
        r'<span class="w-2 h-2 rounded-full[^"]*"></span>\s*'
        r'<span class="truncate">[^<]*</span>\s*'
        r'</a>'
    )
    new_content, count = re.subn(pattern, '', content, flags=re.DOTALL)
    return new_content, count


# ─── Helper: update progress pill ──────────────────────────────────────
def update_progress_pill(content, lesson_num):
    """Set progress pill to lesson_num/TOTAL_LESSONS."""
    pattern = r'(font-extrabold">)\d+(<span class="font-bold opacity-50">)/\d+'
    replacement = rf'\g<1>{lesson_num}\g<2>/{TOTAL_LESSONS}'
    return re.sub(pattern, replacement, content)


def patch_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # ─── 1. Remove TOC entries for deleted lessons ───────────────────
    content, c1 = remove_toc_entry(content, OLD_11)
    content, c2 = remove_toc_entry(content, OLD_12)

    # ─── 2. Rename lesson13 → lesson11 in TOC and everywhere ────────
    content = content.replace(
        'href="' + OLD_13 + '"',
        'href="' + NEW_11 + '"'
    )
    content = content.replace(
        '>13. Parquet &amp; Performance Profiling<',
        '>11. Parquet &amp; Performance Profiling<'
    )

    # ─── 3. Update progress pill ────────────────────────────────────
    m = re.search(r'lesson(\d+)_', filename)
    if m:
        lesson_num = int(m.group(1))
        if lesson_num == 13:
            lesson_num = 11
        content = update_progress_pill(content, lesson_num)

    # ─── 4. Lesson-specific fixes ───────────────────────────────────

    # --- lesson10: update Next link and #next-lesson preview ---
    if 'lesson10_' in filename:
        # Bottom nav Next href
        content = content.replace(
            'href="' + OLD_11 + '"',
            'href="' + NEW_11 + '"'
        )
        # Bottom nav Next title
        content = content.replace(
            'Building &amp; Automating Reports</p>\n'
            '      </div>\n'
            '      <span class="iconify text-gray-300 text-xl',
            'Parquet &amp; Performance Profiling</p>\n'
            '      </div>\n'
            '      <span class="iconify text-gray-300 text-xl'
        )

        # #next-lesson subtitle
        content = content.replace(
            'Lesson 11</p>\n'
            '          <h3 class="text-base font-bold text-gray-800">Building &amp; Automating Reports</h3>',
            'Module 3 &middot; Lesson 11</p>\n'
            '          <h3 class="text-base font-bold text-gray-800">Parquet &amp; Performance Profiling</h3>'
        )

        # Replace the 3 preview cards
        old_cards = (
            '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
            '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
            '              <span class="iconify text-white text-sm" data-icon="fa6-solid:sitemap"></span>\n'
            '            </span>\n'
            '            <div>\n'
            '              <p class="text-sm font-semibold text-gray-700">Structure a Report Script</p>\n'
            '            </div>\n'
            '          </div>\n'
            '\n'
            '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
            '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
            '              <span class="iconify text-white text-sm" data-icon="fa6-solid:file-lines"></span>\n'
            '            </span>\n'
            '            <div>\n'
            '              <p class="text-sm font-semibold text-gray-700">Export with Multiple Sheets</p>\n'
            '            </div>\n'
            '          </div>\n'
            '\n'
            '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
            '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
            '              <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-bar"></span>\n'
            '            </span>\n'
            '            <div>\n'
            '              <p class="text-sm font-semibold text-gray-700">Add Summary Statistics</p>\n'
            '            </div>\n'
            '          </div>'
        )
        new_cards = (
            '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
            '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
            '              <span class="iconify text-white text-sm" data-icon="fa6-solid:bars"></span>\n'
            '            </span>\n'
            '            <div>\n'
            '              <p class="text-sm font-semibold text-gray-700">Columnar Storage Basics</p>\n'
            '            </div>\n'
            '          </div>\n'
            '\n'
            '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
            '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
            '              <span class="iconify text-white text-sm" data-icon="fa6-solid:scale-balanced"></span>\n'
            '            </span>\n'
            '            <div>\n'
            '              <p class="text-sm font-semibold text-gray-700">Row vs. Columnar Layouts</p>\n'
            '            </div>\n'
            '          </div>\n'
            '\n'
            '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
            '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
            '              <span class="iconify text-white text-sm" data-icon="fa6-solid:cube"></span>\n'
            '            </span>\n'
            '            <div>\n'
            '              <p class="text-sm font-semibold text-gray-700">Working with Parquet Files</p>\n'
            '            </div>\n'
            '          </div>'
        )
        content = content.replace(old_cards, new_cards)

    # --- lesson13 (will become lesson11): hero, nav, module complete ---
    if 'lesson13_' in filename:
        # Hero lesson number
        content = re.sub(
            r'(tracking-\[0\.2em\] text-white/90 mb-2">)Lesson\s+13',
            r'\g<1>Lesson 11',
            content
        )
        # Bottom nav Previous href
        content = content.replace(
            'href="' + OLD_12 + '"',
            'href="lesson10_writing_to_databases_and_managing_credentials.html"'
        )
        # Bottom nav Previous title
        content = content.replace(
            '>Handling Large Data</p>',
            '>Writing to Databases &amp; Managing Credentials</p>'
        )
        # Module Complete text
        content = content.replace(
            'finished all 13 lessons',
            'finished all 11 lessons'
        )
        content = content.replace(
            'completed all 13 lessons',
            'completed all 11 lessons'
        )

    # ─── Write if changed ───────────────────────────────────────────
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════
print("=" * 60)
print("Removing lesson11_building and lesson12_handling from mod_03")
print("=" * 60)

# Step 1: Patch all remaining files
print("\n-- Patching files --")
for fname in REMAINING:
    path = os.path.join(FOLDER, fname)
    if not os.path.exists(path):
        print(f"  X NOT FOUND: {fname}")
        continue
    changed = patch_file(path)
    print(f"  {'OK' if changed else '?? no changes'} {fname}")

# Step 2: Rename lesson13 -> lesson11
old_path = os.path.join(FOLDER, OLD_13)
new_path = os.path.join(FOLDER, NEW_11)
if os.path.exists(old_path):
    os.rename(old_path, new_path)
    print(f"\n-- Renamed: {OLD_13} -> {NEW_11}")
else:
    print(f"\n  X Cannot rename: {OLD_13} not found")

# Step 3: Delete old lesson11 and lesson12
for fname in [OLD_11, OLD_12]:
    path = os.path.join(FOLDER, fname)
    if os.path.exists(path):
        os.remove(path)
        print(f"-- Deleted: {fname}")
    else:
        print(f"  Already gone: {fname}")

# Step 4: Verify final state
print("\n-- Final files --")
files = sorted(f for f in os.listdir(FOLDER) if f.endswith('.html'))
for f in files:
    print(f"  {f}")
print(f"\nTotal: {len(files)} lesson files")
