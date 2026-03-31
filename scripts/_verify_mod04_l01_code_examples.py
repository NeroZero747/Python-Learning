import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(TARGET).read()

m = re.search(r'<section id="code-examples".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

checks = [
    # Section structure
    ("section present",                  'id="code-examples"' in sec),
    ("section header fa6-solid:code",    'data-icon="fa6-solid:code"' in sec),
    ("section title Code Examples",      '>Code Examples<' in sec),
    ("body class bg-white px-8 py-7",    'class="bg-white px-8 py-7 space-y-6"' in sec),

    # Tab pills — 3 tabs, no 4th
    ("3 ce-step buttons",                sec.count('"ce-step ') == 3),
    ("tab 0 active",                     'ce-step ce-step-active' in sec),
    ("tab 0 label Create a Module",      'Create a Module' in sec),
    ("tab 1 label Import a Module",      'Import a Module' in sec),
    ("tab 2 label Pick Specific",        'Pick Specific Functions' in sec),
    ("no Example 1/2/3/4 labels",        'Example 1' not in sec and 'Example 4' not in sec),

    # 3 panels
    ("panel 1 visible",                  'class="ce-panel ce-panel-anim"' in sec),
    ("panels 2 and 3 hidden",            sec.count('class="ce-panel ce-panel-anim hidden"') == 2),

    # Panel 1 — Create a Module
    ("p1 watermark 01",                  '>01<' in sec),
    ("p1 header title",                  '>Create a Module<' in sec),
    ("p1 Beginner badge",                'fa6-solid:leaf' in sec),
    ("p1 Shop pill",                     '>Shop<' in sec),
    ("p1 .py file pill",                 '>.py file<' in sec),
    ("p1 What This Does present",        'What This Does' in sec),
    ("p1 desc mentions shop_utils.py",   'shop_utils.py' in sec),
    ("p1 filename pill",                 '>shop_utils.py<' in sec),
    ("p1 no traffic-light dots",         'bg-red-400/80' not in sec),
    ("p1 code get_total function",       'def get_total(price, quantity)' in sec),
    ("p1 code apply_discount function",  'def apply_discount(total, percent)' in sec),
    ("p1 code all lines commented",      '# multiply price by number of items' in sec and '# return the total cost' in sec),
    ("p1 terminal pane",                 'bg-[#11111b]' in sec),
    ("p1 terminal cmd",                  '$ python shop_utils.py' in sec),
    ("p1 terminal output 48",            '>48<' in sec),
    ("p1 amber tip",                     'Save this file in your project folder' in sec),

    # Panel 2 — Import a Module
    ("p2 watermark 02",                  '>02<' in sec),
    ("p2 header title Import a Module",  sec.count('>Import a Module<') >= 1),
    ("p2 import pill",                   '>import<' in sec),
    ("p2 dot notation pill",             '>dot notation<' in sec),
    ("p2 desc mentions import",          'loads every function' in sec),
    ("p2 filename main_shop.py",         '>main_shop.py<' in sec),
    ("p2 code import shop_utils",        'import shop_utils' in sec),
    ("p2 code dot notation call",        'shop_utils.get_total' in sec),
    ("p2 code apply_discount call",      'shop_utils.apply_discount' in sec),
    ("p2 code get_total commented",      '# call get_total using dot notation' in sec),
    ("p2 terminal cmd",                  '$ python main_shop.py' in sec),
    ("p2 terminal output 75 67.5",       '>75<' in sec and '67.5' in sec),
    ("p2 amber tip",                     'prefix tells Python exactly' in sec),

    # Panel 3 — Pick Specific Functions
    ("p3 watermark 03",                  '>03<' in sec),
    ("p3 header title Pick Specific",    '>Pick Specific Functions<' in sec),
    ("p3 from import pill",              '>from \u2026 import<' in sec),
    ("p3 desc mentions from import",     'from \u2026 import' in sec),
    ("p3 filename daily_report.py",      '>daily_report.py<' in sec),
    ("p3 code from import get_total",    'from shop_utils import get_total' in sec),
    ("p3 code from import apply_disc",   'from shop_utils import apply_discount' in sec),
    ("p3 code jacket_cost",             'jacket_cost = get_total' in sec),
    ("p3 code discounted",               'discounted = apply_discount' in sec),
    ("p3 code commented",                '# import get_total directly' in sec),
    ("p3 terminal cmd",                  '$ python daily_report.py' in sec),
    ("p3 terminal output 160 136",       '>160<' in sec and '136.0' in sec),
    ("p3 amber tip one-liner import",    'from shop_utils import get_total, apply_discount' in sec),

    # Global rules
    ("no traffic-light dots anywhere",   'bg-red-400/80' not in sec),
    ("switchCeTab JS switches",          'switchCeTab(0)' in sec and 'switchCeTab(1)' in sec and 'switchCeTab(2)' in sec),
    ("no switchCeTab(3)",                'switchCeTab(3)' not in sec),
    ("CSS ce-step-active in file",       '.ce-step-active' in html or 'ce-step-active' in html),
    ("JS switchCeTab in file",           'function switchCeTab' in html),
]

passed = sum(1 for _, v in checks if v)
total  = len(checks)
print(f"\nCode Examples rewrite — {passed}/{total} checks\n")
for name, v in checks:
    print(f"  {'OK' if v else 'FAIL'} {name}")
