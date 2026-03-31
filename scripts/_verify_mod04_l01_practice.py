import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(TARGET).read()

m = re.search(r'<section id="practice".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

checks = [
    # Shell
    ("section id practice",              'id="practice"' in sec),
    ("header icon fa6-solid:pencil",     'fa6-solid:pencil' in sec),
    ("header title Practice Exercises",  '>Practice Exercises<' in sec),
    ("body class px-8 py-7 space-y-6",  'class="bg-white px-8 py-7 space-y-6"' in sec),

    # Tab pills
    ("3 pe-step buttons",                sec.count('"pe-step ') == 3),
    ("tab 0 active",                     'pe-step pe-step-active' in sec),
    ("tab 0 label Build a Module",       'Build a Module' in sec),
    ("tab 1 label Import and Use",       'Import and Use' in sec),
    ("tab 2 label Pick One Function",    'Pick One Function' in sec),
    ("no Exercise N labels",             'Exercise 1' not in sec and 'Exercise 2' not in sec),

    # Panels
    ("panel 1 visible",                  'class="pe-panel pe-panel-anim"' in sec),
    ("panels 2 and 3 hidden",            sec.count('class="pe-panel pe-panel-anim hidden"') == 2),

    # Panel 1 — Build a Module
    ("p1 watermark 01",                  '>01<' in sec),
    ("p1 title Build a Module",          '>Build a Module<' in sec),
    ("p1 Beginner badge",                sec.count('fa6-solid:leaf') >= 3),
    ("p1 School badge",                  sec.count('>School<') >= 1),
    ("p1 def badge",                     '>def<' in sec),
    ("p1 task grade_utils.py",           'grade_utils.py' in sec),
    ("p1 no traffic-light dots",         'bg-red-400/80' not in sec),
    ("p1 filename grade_utils.py",       '>grade_utils.py<' in sec),
    ("p1 code to_percentage",            'def to_percentage(score, total)' in sec),
    ("p1 code get_grade",                'def get_grade(percentage)' in sec),
    ("p1 code all commented",            '# convert a raw score to a percentage' in sec),
    ("p1 code html-encoded >",           '&gt;= 50' in sec),
    ("p1 code html-encoded \"",          '&quot;Pass&quot;' in sec),
    ("p1 terminal pane",                 'bg-[#11111b]' in sec),
    ("p1 terminal cmd",                  '$ python grade_utils.py' in sec),
    ("p1 terminal output 76 Pass",       '>76<' in sec and '>Pass<' in sec),
    ("p1 accordion toggle",              sec.count('toggleAccordion(this)') >= 1),
    ("p1 accordion body",                'accordion-body' in sec),
    ("p1 tip",                           'quick test at the bottom of the module file' in sec),

    # Panel 2 — Import and Use
    ("p2 watermark 02",                  '>02<' in sec),
    ("p2 title Import and Use",          '>Import and Use<' in sec),
    ("p2 import badge",                  '>import<' in sec),
    ("p2 dot notation badge",            '>dot notation<' in sec),
    ("p2 task report.py",                'report.py' in sec),
    ("p2 filename report.py",            '>report.py<' in sec),
    ("p2 code import grade_utils",       'import grade_utils' in sec),
    ("p2 code alice_pct",                'alice_pct = grade_utils.to_percentage' in sec),
    ("p2 code bob_pct",                  'bob_pct = grade_utils.to_percentage' in sec),
    ("p2 code cara_pct",                 'cara_pct = grade_utils.to_percentage' in sec),
    ("p2 code html-encoded &",           '&quot;Alice:&quot;' in sec),
    ("p2 terminal cmd",                  '$ python report.py' in sec),
    ("p2 terminal output alice",         'Alice: 90 % Pass' in sec),
    ("p2 terminal output bob",           'Bob: 44 % Fail' in sec),
    ("p2 terminal output cara",          'Cara: 62 % Pass' in sec),
    ("p2 tip",                           'contains no calculation logic' in sec),

    # Panel 3 — Pick One Function
    ("p3 watermark 03",                  '>03<' in sec),
    ("p3 title Pick One Function",       '>Pick One Function<' in sec),
    ("p3 from import badge",             '>from \u2026 import<' in sec),
    ("p3 task quick_check.py",           'quick_check.py' in sec),
    ("p3 filename quick_check.py",       '>quick_check.py<' in sec),
    ("p3 code from import",              'from grade_utils import to_percentage' in sec),
    ("p3 code scores list",              'scores = [54, 30, 42, 58, 21]' in sec),
    ("p3 code for loop",                 'for raw_score in scores' in sec),
    ("p3 code no prefix call",           'pct = to_percentage(raw_score, 60)' in sec),
    ("p3 terminal cmd",                  '$ python quick_check.py' in sec),
    ("p3 terminal output",               '54 \u2192 90 %' in sec),
    ("p3 tip from import",               'from \u2026 import' in sec),

    # Global
    ("no traffic-light dots anywhere",   'bg-red-400/80' not in sec),
    ("JS switchPeTab(0)",                'switchPeTab(0)' in sec),
    ("JS switchPeTab(1)",                'switchPeTab(1)' in sec),
    ("JS switchPeTab(2)",                'switchPeTab(2)' in sec),
    ("no switchPeTab(3)",                'switchPeTab(3)' not in sec),
    ("JS switchPeTab in file",           'function switchPeTab' in html),
]

passed = sum(1 for _, v in checks if v)
total  = len(checks)
print(f"\nPractice Exercises rewrite — {passed}/{total} checks\n")
for name, v in checks:
    print(f"  {'OK' if v else 'FAIL'} {name}")
