import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(TARGET).read()

# Extract just the overview section
m = re.search(r'<section id="overview".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

checks = [
    # Structure
    ("section present",             'id="overview"' in sec),
    ("space-y-5 on body",           'space-y-5' in sec),
    ("bg-white px-8 py-7 body",     'bg-white px-8 py-7 space-y-5' in sec),

    # Part 1 — hook banner
    ("hook banner wrapper",         'bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9]' in sec),
    ("hook uses items-center",      'flex items-center gap-4' in sec),
    ("hook NOT items-start",        'flex items-start gap-4' not in sec),
    ("no mt-0.5 on icon",           'shrink-0 mt-0.5' not in sec),
    ("hook sentence",               'any script in your project can share' in sec),
    ("quote-left icon",             'fa6-solid:quote-left' in sec),

    # Part 2 — analogy intro
    ("Think of intro",              'Think of your Python project as a workshop' in sec),
    ("module bolded",               '<strong>module</strong>' in sec),
    ("analogy closes correctly",    'language you use to fill it' in sec),

    # Part 3 — card grid
    ("grid wrapper",                'grid grid-cols-1 sm:grid-cols-2 gap-3' in sec),
    ("4 cards total",               sec.count('rounded-xl border border-gray-100 bg-gray-50 px-4 py-4') == 4),
    ("card 1 icon toolbox",         'fa6-solid:toolbox' in sec),
    ("card 1 title",                'The Module File' in sec),
    ("card 1 subtitle",             'The toolbox — one shared box for the whole workshop' in sec),
    ("card 1 desc",                 'One file on the shelf, ready for any script to reach into.' in sec),
    ("card 2 icon",                 'fa6-solid:arrow-right-from-bracket' in sec),
    ("card 2 title",                'Moving Functions Out' in sec),
    ("card 2 violet accent",        'bg-violet-50' in sec),
    ("card 2 subtitle",             'Packing the box' in sec),
    ("card 3 icon layer-group",     'fa6-solid:layer-group' in sec),
    ("card 3 title",                'Organizing Your Project' in sec),
    ("card 3 blue accent",          'bg-blue-50' in sec),
    ("card 3 subtitle",             'each toolbox in its own corner' in sec),
    ("card 4 icon arrow-right-to",  'fa6-solid:arrow-right-to-bracket' in sec),
    ("card 4 title",                'The import Statement' in sec),
    ("card 4 emerald accent",       'bg-emerald-50' in sec),
    ("card 4 subtitle",             'Grabbing a tool' in sec),

    # Part 4 — amber tip
    ("amber tip class",             'bg-amber-tip' in sec),
    ("amber tip icon",              'fa6-solid:circle-info' in sec),
    ("amber tip text",              'spreadsheet tabs' in sec),

    # Old content gone
    ("no old code blocks",          'language-python' not in sec),
    ("no old para text",            'Example large script' not in sec),
    ("no old module paragraph",     'logical components' not in sec),
]

passed = sum(1 for _, v in checks if v)
total  = len(checks)
print(f"\nOverview rewrite — {passed}/{total} checks\n")
for name, v in checks:
    print(f"  {'OK' if v else 'FAIL'} {name}")
