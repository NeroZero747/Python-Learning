"""
Fix hero banner module number, lesson number, and progress pill
for all 8 lessons in track_02 / mod_02_programming_foundations_part_2.

Changes per file:
  1. Module pill:  "Module 3" or "Module 4"  →  "Module 2"
  2. Lesson label:  old numbering (01-04)      →  correct 01-08
  3. Progress pill: "N/4"                       →  "N/8"
"""

import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MOD_DIR = ROOT / "pages" / "track_02_python_foundation" / "mod_02_programming_foundations_part_2"

FILES = [
    (MOD_DIR / "lesson01_why_classes_help_data_projects.html",        "01"),
    (MOD_DIR / "lesson02_creating_a_class.html",                      "02"),
    (MOD_DIR / "lesson03_attributes_methods.html",                    "03"),
    (MOD_DIR / "lesson04_refactoring_a_script_into_a_class.html",     "04"),
    (MOD_DIR / "lesson05_creating_your_own_modules.html",             "05"),
    (MOD_DIR / "lesson06_project_folder_structure.html",              "06"),
    (MOD_DIR / "lesson07_introduction_to_git_simple_workflow.html",   "07"),
    (MOD_DIR / "lesson08_logging_basics.html",                        "08"),
]


def fix_hero(html: str, correct_lesson_num: str, lesson_index: int) -> str:
    # 1. Fix Module pill text:  "Module 3" or "Module 4"  →  "Module 2"
    #    These appear inside the hero-pill span, e.g.:
    #    <span class="iconify ..." data-icon="..."></span> Module 3
    html = re.sub(
        r'(data-icon="fa6-solid:(?:diagram-project|star)">\s*</span>\s*)Module\s+\d+',
        r'\g<1>Module 2',
        html,
    )

    # 2. Fix Lesson number label: ">Lesson XX<"
    #    Located in: <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson XX</p>
    html = re.sub(
        r'(tracking-\[0\.2em\]\s+text-white/90\s+mb-2">Lesson\s+)\d{2}',
        r'\g<1>' + correct_lesson_num,
        html,
    )

    # 3. Fix Progress pill: "N/4" → "N/8"
    #    Pattern: <span class="font-extrabold">N<span class="font-bold opacity-50">/4</span></span>
    progress_num = lesson_index + 1
    html = re.sub(
        r'(<span class="font-extrabold">)\d+(<span class="font-bold opacity-50">/)\d+(</span></span>\s*<span class="font-semibold opacity-55">Progress)',
        rf'\g<1>{progress_num}\g<2>8\3',
        html,
    )

    return html


def main():
    for i, (fpath, num) in enumerate(FILES):
        if not fpath.exists():
            print(f"❌ {fpath.name} — file not found")
            continue

        html = fpath.read_text(encoding="utf-8")
        original = html

        html = fix_hero(html, num, i)

        if html != original:
            fpath.write_text(html, encoding="utf-8")
            print(f"✅ {fpath.name} — hero patched")
        else:
            print(f"⚠️  {fpath.name} — no changes needed")


if __name__ == "__main__":
    main()
