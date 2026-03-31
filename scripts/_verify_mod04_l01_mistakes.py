"""Verify the #mistakes section rewrite for lesson01_creating_your_own_modules.html."""

import pathlib, re

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
)

html = TARGET.read_text(encoding="utf-8")

# Extract the #mistakes section
m = re.search(r'<section id="mistakes">(.*?)</section>', html, re.DOTALL)
assert m, "❌  #mistakes section not found"
sec = m.group(1)

checks = [
    # Section shell
    ("section id",              'id="mistakes"' in html),
    ("header icon",             'fa6-solid:triangle-exclamation' in sec),
    ("header title",            '>Common Mistakes<' in sec),
    ("body wrapper",            'bg-white px-8 py-7 space-y-6' in sec),

    # Tab pills
    ("3 mk-step buttons",       sec.count('class="mk-step ') == 3),
    ("tab 0 active",            'mk-step-active' in sec),
    ("tab 0 label",             'Shadowing a Library' in sec),
    ("tab 1 label",             'Dropping the Prefix' in sec),
    ("tab 2 label",             'Wrong File Location' in sec),
    ("no Mistake N labels",     'Mistake 1' not in sec and 'Mistake 2' not in sec),

    # Panels
    ("3 mk-panel divs",         sec.count('class="mk-panel') == 3),
    ("panel 1 visible",         'mk-panel mk-panel-anim"' in sec),
    ("panel 2 hidden",          sec.count('mk-panel mk-panel-anim hidden"') >= 2),

    # Panel 1 — Shadowing a Library
    ("p1 title",                'Naming Your Module File the Same as a Python Library' in sec),
    ("p1 subtitle",             'Python loads your file instead of the real library' in sec),
    ("p1 explanation math.py",  'math.py' in sec),
    ("p1 explanation AttributeError", 'AttributeError' in sec),
    ("p1 wrong label",          'shadows built-in math' in sec),
    ("p1 correct label",        'project-specific filename' in sec),
    ("p1 wrong code shop_utils","shop_utils.py" in sec),
    ("p1 correct code import math", 'import math' in sec),
    ("p1 tip task-based names", 'grade_utils.py' in sec and 'data_cleaning.py' in sec),

    # Panel 2 — Dropping the Prefix
    ("p2 title",                'Calling a Function Without Its Module Name' in sec),
    ("p2 subtitle NameError",   'NameError' in sec),
    ("p2 explanation import",   'import shop_utils' in sec),
    ("p2 explanation get_total","get_total' is not defined" in sec),
    ("p2 wrong label",          'bare function name fails' in sec),
    ("p2 correct label",        'use the module prefix' in sec),
    ("p2 wrong code",           'get_total(10, 3)   # NameError' in sec),
    ("p2 correct code prefix",  'shop_utils.get_total(10, 3)' in sec),
    ("p2 tip Excel analogy",    'workbook name in Excel' in sec),

    # Panel 3 — Wrong File Location
    ("p3 title",                'Placing the Module in a Different Folder' in sec),
    ("p3 subtitle ModuleNotFoundError", 'ModuleNotFoundError' in sec),
    ("p3 explanation subfolder","subfolder" in sec),
    ("p3 wrong label",          'module in wrong directory' in sec),
    ("p3 correct label",        'both files in same folder' in sec),
    ("p3 wrong code tree",      'utils/' in sec),
    ("p3 correct code tree",    'same level' in sec),
    ("p3 tip file manager",     'file manager' in sec),

    # Arrow dividers present
    ("arrow divider 1",         sec.count('fa6-solid:arrow-right') >= 3),
    # Red/emerald panels
    ("red panel bg",            'bg-red-50/30' in sec),
    ("emerald panel bg",        'bg-emerald-50/30' in sec),
    # Amber tips
    ("3 amber tips",            sec.count('bg-amber-50/40') == 3),

    # JS switchMkTab
    ("JS switchMkTab(0)",       'switchMkTab(0)' in sec),
    ("JS switchMkTab(1)",       'switchMkTab(1)' in sec),
    ("JS switchMkTab(2)",       'switchMkTab(2)' in sec),
    ("no switchMkTab(3)",       'switchMkTab(3)' not in sec),
]

passed = sum(1 for _, v in checks if v)
total = len(checks)

print(f"Common Mistakes rewrite — {passed}/{total} checks\n")
for name, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'} {name}")

if passed < total:
    print(f"\n⚠️  {total - passed} check(s) failed.")
else:
    print("\n✅  All checks passed.")
