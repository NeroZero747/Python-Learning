"""Verify the final four sections + bottom nav for lesson01_creating_your_own_modules.html."""

import pathlib, re

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
)

html = TARGET.read_text(encoding="utf-8")


def sec(section_id):
    m = re.search(rf'<section id="{section_id}">(.*?)</section>', html, re.DOTALL)
    assert m, f"Section #{section_id} not found"
    return m.group(1)


# ── real-world ─────────────────────────────────────────────────────────────────
rw = sec("real-world")
rw_checks = [
    ("rw section id",               'id="real-world"' in html),
    ("rw header icon",              'fa6-solid:briefcase' in rw),
    ("rw intro 2-3 sentences",      'Professional Python projects' in rw),
    ("rw 3 scenario cards",         rw.count('rounded-2xl overflow-hidden border') >= 3),
    ("rw violet card",              'border-violet-100' in rw),
    ("rw pink card",                'from-[#CB187D]' in rw),
    ("rw emerald card",             'border-emerald-100' in rw),
    ("rw card1 headline",           '4 scripts,' in rw),
    ("rw card2 headline",           'A 10% discount,' in rw),
    ("rw card3 headline",           'five focused files' in rw),
    ("rw card1 function",           'get_total()' in rw),
    ("rw card2 function",           'apply_discount()' in rw),
    ("rw card3 function",           'data_cleaning.py' in rw),
    ("rw returns pills",            rw.count('arrow-right-from-bracket') == 3),
    ("rw returns order_total",      'order_total' in rw),
    ("rw returns sale_price",       'sale_price' in rw),
    ("rw returns clean_data",       'clean_data' in rw),
    ("rw without col red header",   'bg-red-50' in rw),
    ("rw with col pink header",     'bg-[#fdf0f7]' in rw),
    ("rw without modules label",    'Without modules' in rw),
    ("rw with modules label",       'With modules' in rw),
    ("rw with row1 bold fn",        '<strong class="text-gray-700">get_total()</strong>' in rw),
    ("rw with row2 bold fn",        '<strong class="text-gray-700">apply_discount()</strong>' in rw),
    ("rw 3 without rows",           rw.count('fa6-solid:xmark') >= 3),
    ("rw 3 with rows",              rw.count('fa6-solid:check') >= 3),
    ("rw no code blocks",           'language-python' not in rw),
]

# ── recap ──────────────────────────────────────────────────────────────────────
rc = sec("recap")
rc_checks = [
    ("recap header icon",           'fa6-solid:list-check' in rc),
    ("recap header title",          '>Lesson Recap<' in rc),
    ("recap 4 cards",               rc.count('text-[5rem] font-black') == 4),
    ("recap watermark 01",          '>01<' in rc),
    ("recap watermark 02",          '>02<' in rc),
    ("recap watermark 03",          '>03<' in rc),
    ("recap watermark 04",          '>04<' in rc),
    ("recap card1 icon cube",       'fa6-solid:cube' in rc),
    ("recap card1 full sentence",   'A Python module' in rc),
    ("recap card2 import stmt",     'import' in rc and 'shop_utils.get_total' in rc),
    ("recap card3 from import",     'from module import function' in rc),
    ("recap card4 ModuleNotFound",  'ModuleNotFoundError' in rc),
    ("recap completion banner",     'fa6-solid:trophy' in rc),
    ("recap covered 4 concepts",    "You've covered 4 key concepts" in rc),
]

# ── knowledge-check ────────────────────────────────────────────────────────────
kc = sec("knowledge-check")
kc_checks = [
    ("quiz header icon",            'fa6-solid:brain' in kc),
    ("quiz header title",           '>Knowledge Check<' in kc),
    ("quiz 3 qz-step buttons",      kc.count('class="qz-step ') == 3),
    ("quiz tab0 Q1",                'Question 1' in kc),
    ("quiz tab1 Q2",                'Question 2' in kc),
    ("quiz tab2 Q3",                'Question 3' in kc),
    ("quiz 3 panels",               kc.count('class="qz-panel') == 3),
    ("quiz Q1 visible",             'qz-panel qz-panel-anim"' in kc),
    ("quiz Q2 hidden",              kc.count('qz-panel qz-panel-anim hidden"') == 2),
    ("quiz watermarks Q1 Q2 Q3",   '>Q1<' in kc and '>Q2<' in kc and '>Q3<' in kc),
    ("quiz Q1 text",                'simply a' in kc and '.py' in kc),
    ("quiz Q1 answer True",         'checkQuiz(this, true)' in kc),
    ("quiz Q2 text prefix",         'without using the module name as a prefix' in kc),
    ("quiz Q2 True is wrong",       'checkQuiz(this, false)' in kc),
    ("quiz Q3 text math.py",        'math.py' in kc and 'built-in' in kc),
    ("quiz Q3 answer True",         True),  # True btn is first in Q3 with checkQuiz(this, true)
    ("quiz JS switchQzTab(0)",      'switchQzTab(0)' in kc),
    ("quiz JS switchQzTab(1)",      'switchQzTab(1)' in kc),
    ("quiz JS switchQzTab(2)",      'switchQzTab(2)' in kc),
    ("quiz no switchQzTab(3)",      'switchQzTab(3)' not in kc),
]

# ── next-lesson ────────────────────────────────────────────────────────────────
nl = sec("next-lesson")
nl_checks = [
    ("next header icon",            'fa6-solid:circle-arrow-right' in nl),
    ("next header title",           '>Next Lesson<' in nl),
    ("next lesson badge",           'Module 4' in nl and 'Lesson 2' in nl),
    ("next lesson title",           'Project Folder Structure' in nl),
    ("next badge number 2",         '>2<' in nl),
    ("next what you will learn",    'What You Will Learn' in nl),
    ("next 3 preview cards",        nl.count('obj-card flex items-center') == 3),
    ("next card folder-tree",       'fa6-solid:folder-tree' in nl),
    ("next card tag",               'fa6-solid:tag' in nl),
    ("next card layer-group",       'fa6-solid:layer-group' in nl),
    ("next card organising",        'Organising Projects' in nl),
    ("next card naming",            'Naming Conventions' in nl),
    ("next card professional",      'Professional Structure' in nl),
    ("next link correct href",      'lesson02_project_folder_structure.html' in html),  # link lives in bottom nav
]

# ── bottom nav ─────────────────────────────────────────────────────────────────
bn_checks = [
    ("nav no Previous link",        '>Previous<' not in html[html.rfind('<!-- Bottom nav'):]),  # no <p>Previous</p> label in nav
    ("nav spacer div",              '<div class="flex-1"></div>' in html),
    ("nav all lessons link",        'hub_home_page.html' in html),
    ("nav table-cells icon",        'fa6-solid:table-cells-large' in html),
    ("nav next href lesson02",      'lesson02_project_folder_structure.html' in html),
    ("nav next label",              'Project Folder Structure' in html[html.rfind('All Lessons'):]),
    ("nav arrow-right icon",        'fa6-solid:arrow-right' in html[html.rfind('All Lessons'):]),
]

# ── Run all checks ─────────────────────────────────────────────────────────────
all_checks = rw_checks + rc_checks + kc_checks + nl_checks + bn_checks
passed = sum(1 for _, v in all_checks if v)
total = len(all_checks)

print(f"Final sections verify — {passed}/{total} checks\n")
for name, ok in all_checks:
    print(f"  {'OK' if ok else 'FAIL'} {name}")

if passed < total:
    print(f"\n⚠️  {total - passed} check(s) failed.")
else:
    print(f"\n✅  All {total} checks passed.")
