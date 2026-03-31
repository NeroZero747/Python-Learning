import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(TARGET).read()

m = re.search(r'<section id="key-concepts".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

checks = [
    # Structure
    ("section present",                  'id="key-concepts"' in sec),
    ("scroll-mt-24",                     'scroll-mt-24' in sec),
    ("section header icon book-open",    'fa6-solid:book-open' in sec),
    ("section title Key Concepts",       '>Key Concepts<' in sec),
    ("section subtitle set",             'Creating, importing, and selectively' in sec),
    ("body uses px-6 py-7",              'px-6 py-7' in sec),
    ("sidebar uses md:w-52",             'md:w-52' in sec),
    ("kc-indicator present",             'kc-indicator' in sec),
    ("panels use md:pl-5",               'md:pl-5' in sec),

    # Sidebar tabs
    ("3 kc-tab buttons",                 sec.count('"kc-tab ') == 3),
    ("tab 0 active",                     'kc-tab kc-tab-active' in sec),
    ("tab 0 inline style pink",          'background:#CB187D;color:#fff' in sec),
    ("tab 1 inline style gray",          sec.count('background:#f3f4f6;color:#9ca3af') >= 2),
    ("tab 0 label",                      'Creating a Module' in sec),
    ("tab 1 label",                      'Importing a Module' in sec),
    ("tab 2 label",                      'Specific Imports' in sec),
    ("sidebar icons set",                'fa6-solid:file-code' in sec and 'fa6-solid:arrow-right-to-bracket' in sec and 'fa6-solid:filter' in sec),

    # Panel 0 — pink
    ("panel 0 no hidden",                'class="kc-panel kc-panel-anim"' in sec),
    ("panel 0 pink border",              'border-pink-100' in sec),
    ("panel 0 gradient bar",             'from-[#CB187D] via-pink-400 to-rose-300' in sec),
    ("panel 0 header icon",              'from-[#CB187D] to-[#e84aad]' in sec),
    ("panel 0 subtitle",                 'A reusable Python file' in sec),
    ("panel 0 type badge",               '.py file' in sec),
    ("panel 0 definition",               'module is a plain Python file that holds functions' in sec),
    ("panel 0 widget rules-table",       'Module File Rules' in sec),
    ("panel 0 widget good pill",         'bg-green-100 text-green-800' in sec),
    ("panel 0 widget bad pill",          'bg-red-100 text-red-700' in sec),
    ("panel 0 code present",             'sales_utils.py' in sec),
    ("panel 0 all lines commented",      '# sales_utils.py' in sec and '# a reusable function' in sec),
    ("panel 0 tip pink",                 'bg-pink-50 border border-pink-100' in sec),
    ("panel 0 tip icon lightbulb",       'fa6-solid:lightbulb' in sec),
    ("panel 0 tip code pill pink-200",   'bg-pink-200 text-[#CB187D] border border-pink-300' in sec),

    # Panel 1 — violet
    ("panel 1 hidden",                   sec.count('class="kc-panel kc-panel-anim hidden"') >= 2),
    ("panel 1 violet border",            'border-violet-100' in sec),
    ("panel 1 gradient bar",             'from-violet-500 via-purple-400 to-fuchsia-300' in sec),
    ("panel 1 subtitle",                 'Use the whole module at once' in sec),
    ("panel 1 type badge",               '>import<' in sec),
    ("panel 1 definition",               'statement loads your module' in sec),
    ("panel 1 comparison-strip widget",  'Import Syntax' in sec),
    ("panel 1 strip load step",          'Load the module' in sec),
    ("panel 1 strip result",             'Result returned' in sec),
    ("panel 1 code present",             'import sales_utils' in sec),
    ("panel 1 tip violet",               'bg-violet-50 border border-violet-100' in sec),
    ("panel 1 tip warning icon",         'fa6-solid:triangle-exclamation' in sec),
    ("panel 1 tip code violet-200",      'bg-violet-200 text-violet-800 border border-violet-300' in sec),

    # Panel 2 — blue
    ("panel 2 blue border",              'border-blue-100' in sec),
    ("panel 2 gradient bar",             'from-blue-500 via-cyan-400 to-teal-300' in sec),
    ("panel 2 subtitle",                 'Pick only what you need' in sec),
    ("panel 2 type badge",               'from … import' in sec),
    ("panel 2 definition",               'pulls one function directly' in sec),
    ("panel 2 comparison-table widget",  'import vs from' in sec),
    ("panel 2 table col violet badge",   'import module' in sec),
    ("panel 2 table col blue badge",     'from module import fn' in sec),
    ("panel 2 code present",             'from sales_utils import calculate_total' in sec),
    ("panel 2 tip blue",                 'bg-blue-50 border border-blue-100' in sec),
    ("panel 2 tip code blue-200",        'bg-blue-200 text-blue-800 border border-blue-300' in sec),

    # CSS rules present in whole file
    ("CSS kc-tab-active",                '.kc-tab-active { background: #fdf0f7; }' in html),
    ("CSS kc-tab hover",                 '.kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }' in html),
    ("CSS kc-panel-anim",                'kc-panel-anim' in html),
    ("JS kcColors present",              'const kcColors' in html),
    ("JS switchKcTab present",           'function switchKcTab' in html),

    # Old content gone
    ("old panel content gone",           'The module name acts like a namespace' not in sec),
    ("old Definition label gone",        'uppercase tracking-widest">Definition<' not in sec),
    ("no panel body space-y-3",          'space-y-3 mb-4' not in sec),
]

passed = sum(1 for _, v in checks if v)
total  = len(checks)
print(f"\nKey Concepts rewrite — {passed}/{total} checks\n")
for name, v in checks:
    print(f"  {'OK' if v else 'FAIL'} {name}")
