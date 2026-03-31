import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(TARGET).read()

# Extract just the key-ideas section
m = re.search(r'<section id="key-ideas".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

checks = [
    # Structure
    ("section present",             'id="key-ideas"' in sec),
    ("header icon lightbulb",       'fa6-solid:lightbulb' in sec),
    ("header title unchanged",      'Key Takeaways' in sec),
    ("space-y-4 body",              'bg-white px-8 py-7 space-y-4' in sec),

    # Card 1 — pink
    ("card 1 obj-card-kt",          'obj-card-kt' in sec),
    ("card 1 top bar pink",         'from-[#CB187D] to-[#e84aad]' in sec),
    ("card 1 icon wrench",          'fa6-solid:wrench' in sec),
    ("card 1 title",                'One Fix Updates Every Script' in sec),
    ("card 1 desc no-copy-paste",   'hunting through copies' in sec),
    ("card 1 pill 1",               'no duplication' in sec),
    ("card 1 pill 2",               'single source' in sec),
    ("card 1 pill 3",               'easy fixes' in sec),
    ("card 1 border gray-100",      'border border-gray-100 bg-white' in sec),

    # Card 2 — violet
    ("card 2 obj-card-violet",      'obj-card-violet' in sec),
    ("card 2 top bar violet",       'from-violet-500 to-purple-400' in sec),
    ("card 2 icon table-cells",     'fa6-solid:table-cells' in sec),
    ("card 2 title",                'Modules Work Like Shared Formulas' in sec),
    ("card 2 desc Excel ref",       'Excel' in sec),
    ("card 2 pill reusable",        'reusable' in sec),
    ("card 2 pill write once",      'write once' in sec),
    ("card 2 pill like Excel",      'like Excel' in sec),
    ("card 2 border violet-100",    'border border-violet-100 bg-white' in sec),

    # Card 3 — blue
    ("card 3 obj-card-blue",        'obj-card-blue' in sec),
    ("card 3 top bar blue",         'from-blue-500 to-indigo-400' in sec),
    ("card 3 icon list-check",      'fa6-solid:list-check' in sec),
    ("card 3 title",                'Split by Task, Not by Length' in sec),
    ("card 3 desc task-based",      'what job the code does' in sec),
    ("card 3 pill task-focused",    'task-focused' in sec),
    ("card 3 pill structure",       'structure' in sec),
    ("card 3 pill project layout",  'project layout' in sec),
    ("card 3 border blue-100",      'border border-blue-100 bg-white' in sec),

    # No old content
    ("old split layout gone",       'flex-col md:flex-row' not in sec),
    ("old code blocks gone",        'language-python' not in sec),
    ("old card title 1 gone",       'Modules Are Python Files' not in sec),
    ("old card title 2 gone",       'Modules Help Organize' not in sec),
]

# CSS checks (whole file)
css_checks = [
    ("CSS obj-card-kt:hover",       '.obj-card-kt:hover' in html),
    ("CSS obj-card-violet:hover",   '.obj-card-violet:hover' in html),
    ("CSS obj-card-blue:hover",     '.obj-card-blue:hover' in html),
    ("CSS kt bg-white on hover",    'obj-card-kt:hover' in html and '#ffffff' in html),
]

all_checks = checks + css_checks
passed = sum(1 for _, v in all_checks if v)
total  = len(all_checks)
print(f"\nKey Takeaways rewrite — {passed}/{total} checks\n")
for name, v in all_checks:
    print(f"  {'OK' if v else 'FAIL'} {name}")
