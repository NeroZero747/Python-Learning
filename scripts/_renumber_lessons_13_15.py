"""Renumber lesson13→11, lesson14→12, lesson15→13 in mod_03.

Changes applied to every HTML file in the module:
1. Sidebar TOC: href filenames and label numbers (13→11, 14→12, 15→13)
2. Bottom nav: href filenames and label text
3. #next-lesson: badge numbers, hrefs, titles
4. Hero banners: "Lesson NN" badge text
5. Rename the three physical files last
"""
import os, re

BASE = os.path.join(os.path.dirname(__file__), "..",
                    "pages", "mod_03_python_for_data_analysts")

# Files to process (all lessons that currently exist, using OLD names)
LESSON_SLUGS = [
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
    "lesson13_building_and_automating_reports.html",
    "lesson14_handling_large_data.html",
    "lesson15_parquet_and_performance_profiling.html",
]

ALL_FILES = [os.path.join(BASE, s) for s in LESSON_SLUGS]

# ── Filename renaming map ───────────────────────────────────────────────
RENAME_MAP = {
    "lesson13_building_and_automating_reports":     "lesson11_building_and_automating_reports",
    "lesson14_handling_large_data":                 "lesson12_handling_large_data",
    "lesson15_parquet_and_performance_profiling":   "lesson13_parquet_and_performance_profiling",
}

# ── Text replacements (applied globally inside every file) ──────────────
# Order matters: do 15→13 first, then 14→12, then 13→11 to avoid
# double-replacing (e.g. 13→11 then catching the new "13" from 15→13).
# Actually, since filenames are unique strings, we can do them safely
# by targeting the full filename string.

REPLACEMENTS = [
    # --- Sidebar TOC label numbers ---
    # "13. Building &amp; Automating Reports" → "11. ..."
    ('>13. Building &amp; Automating Reports<', '>11. Building &amp; Automating Reports<'),
    # "14. Handling Large Data" → "12. ..."
    ('>14. Handling Large Data<',               '>12. Handling Large Data<'),
    # "15. Parquet &amp; Performance Profiling" → "13. ..."
    ('>15. Parquet &amp; Performance Profiling<', '>13. Parquet &amp; Performance Profiling<'),

    # --- href filename references (sidebar TOC, bottom nav) ---
    ('lesson13_building_and_automating_reports.html',   'lesson11_building_and_automating_reports.html'),
    ('lesson14_handling_large_data.html',               'lesson12_handling_large_data.html'),
    ('lesson15_parquet_and_performance_profiling.html',  'lesson13_parquet_and_performance_profiling.html'),
]

# ── Hero badge and #next-lesson badge number fixes ──────────────────────
# These are more targeted — only in specific files.
# Pattern: "Lesson 13" in hero or next-lesson context
HERO_FIXES = {
    "lesson13_building_and_automating_reports.html": [
        # Hero badge: "Lesson 13" → "Lesson 11"
        ('Lesson 13', 'Lesson 11'),
    ],
    "lesson14_handling_large_data.html": [
        ('Lesson 14', 'Lesson 12'),
    ],
    "lesson15_parquet_and_performance_profiling.html": [
        ('Lesson 15', 'Lesson 13'),
    ],
}

# #next-lesson badge fixes (these are in the PREVIOUS lesson's file)
NEXT_LESSON_FIXES = {
    # lesson10 already says "Lesson 11" for the next-lesson badge — correct!
    # lesson13 (old name) has "Lesson 14" → "Lesson 12"
    "lesson13_building_and_automating_reports.html": [
        # next-lesson badge number
        ('>Lesson 14<', '>Lesson 12<'),
        # next-lesson "Module X · Lesson N" label
        ('>Module 3 · Lesson 14<', '>Module 3 · Lesson 12<'),
    ],
    # lesson14 (old name) has "Lesson 15" → "Lesson 13"
    "lesson14_handling_large_data.html": [
        ('>Lesson 15<', '>Lesson 13<'),
        ('>Module 3 · Lesson 15<', '>Module 3 · Lesson 13<'),
    ],
}


def main():
    # ── Step 1: Apply global text replacements to all files ──────────────
    print("── Step 1: Global text replacements (hrefs + sidebar labels) ──")
    for fpath in ALL_FILES:
        fname = os.path.basename(fpath)
        if not os.path.exists(fpath):
            print(f"  ⚠️  {fname} — not found, skipping")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        original = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)

        if text != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  ✅ {fname} — updated")
        else:
            print(f"  ⚠️  {fname} — no changes needed")

    # ── Step 2: Hero badge fixes (only in lesson13/14/15) ────────────────
    print("\n── Step 2: Hero badge 'Lesson NN' fixes ──")
    for fname, fixes in HERO_FIXES.items():
        # Use new filename if already renamed... but we haven't renamed yet
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath):
            print(f"  ⚠️  {fname} — not found")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        changed = False
        for old, new in fixes:
            if old in text:
                text = text.replace(old, new)
                changed = True

        if changed:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  ✅ {fname} — hero badge updated")
        else:
            print(f"  ⚠️  {fname} — hero badge already correct or not found")

    # ── Step 3: #next-lesson badge fixes ─────────────────────────────────
    print("\n── Step 3: #next-lesson badge number fixes ──")
    for fname, fixes in NEXT_LESSON_FIXES.items():
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath):
            print(f"  ⚠️  {fname} — not found")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        changed = False
        for old, new in fixes:
            if old in text:
                text = text.replace(old, new)
                changed = True

        if changed:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  ✅ {fname} — next-lesson badge updated")
        else:
            print(f"  ⚠️  {fname} — next-lesson badge not found (may use different format)")

    # ── Step 4: Rename the physical files ────────────────────────────────
    print("\n── Step 4: Rename files ──")
    for old_stem, new_stem in RENAME_MAP.items():
        old_path = os.path.join(BASE, old_stem + ".html")
        new_path = os.path.join(BASE, new_stem + ".html")
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"  ✅ {old_stem}.html → {new_stem}.html")
        else:
            print(f"  ⚠️  {old_stem}.html — not found")

    print("\n✅ Done. Lessons renumbered: 13→11, 14→12, 15→13.")


if __name__ == "__main__":
    main()
