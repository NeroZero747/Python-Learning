import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(TARGET).read()

m = re.search(r'<section id="comparison".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

checks = [
    # Shell preserved
    ("section id comparison",             'id="comparison"' in sec),
    ("header icon table-columns",         'fa6-solid:table-columns' in sec),
    ("header title SQL / Excel",          '>SQL / Excel Comparison<' in sec),
    ("body class px-8 py-7 space-y-5",   'class="bg-white px-8 py-7 space-y-5"' in sec),

    # Intro
    ("intro If you already",              'If you already use SQL stored procedures' in sec),

    # Tool header cards
    ("Python header card",                'fa6-brands:python' in sec),
    ("SQL header card",                   'fa6-solid:database' in sec),
    ("Excel header card",                 'fa6-solid:table' in sec),

    # Row 1 — reusable logic container
    ("row1 label",                        'reusable logic container' in sec),
    ("row1 icon box-archive",             'fa6-solid:box-archive' in sec),
    ("row1 py chip",                      'module (.py file)' in sec),
    ("row1 sql chip",                     'stored procedure' in sec),
    ("row1 xl chip",                      'macro (VBA module)' in sec),
    ("row1 chip colours py",              'bg-indigo-50 text-indigo-700' in sec),
    ("row1 chip colours sql",             'bg-orange-50 text-orange-700' in sec),
    ("row1 chip colours xl",              'bg-emerald-50 text-emerald-700' in sec),

    # Row 2 — single reusable unit
    ("row2 label",                        'single reusable unit' in sec),
    ("row2 icon gear",                    'fa6-solid:gear' in sec),
    ("row2 py chip function",             '>function<' in sec),
    ("row2 sql chip udf",                 'user-defined function' in sec),
    ("row2 xl chip udf",                  'custom formula / UDF' in sec),

    # Row 3 — loading the logic
    ("row3 label",                        'loading the logic' in sec),
    ("row3 icon arrow-right-to-bracket",  'fa6-solid:arrow-right-to-bracket' in sec),
    ("row3 py chip import",               'import module' in sec),
    ("row3 sql chip exec",                'EXEC / CALL' in sec),
    ("row3 xl chip =MacroName()",         '=MacroName() / Run' in sec),

    # Divider
    ("divider label",                     'Same discount calculation, three tools' in sec),
    ("divider icon code-compare",         'fa6-solid:code-compare' in sec),
    ("divider hairlines",                 sec.count('flex-1 h-px bg-gray-100') >= 2),

    # Code blocks
    ("py code col label",                 'Python code' in sec),
    ("sql code col label",                'SQL query' in sec),
    ("xl code col label",                 'Excel formula' in sec),
    ("py language-python",                'language-python' in sec),
    ("sql language-sql",                  'language-sql' in sec),
    ("xl language-text",                  'language-text' in sec),
    ("py code from shop_utils",           'from shop_utils import apply_discount' in sec),
    ("py code sale_price",                'sale_price = apply_discount(200, 10)' in sec),
    ("sql code EXEC apply_discount",      'EXEC apply_discount' in sec),
    ("xl code ApplyDiscount",             '=ApplyDiscount(B2, 10)' in sec),
    ("no traffic-light dots",             'bg-red-400/80' not in sec),
    ("3 copy buttons",                    sec.count('copyCode(this)') >= 3),

    # Caption
    ("caption All three",                 'All three apply a 10% discount' in sec),

    # Tip
    ("tip present",                       'idea of splitting logic into reusable' in sec),
    ("tip amber bg-amber-tip",            'bg-amber-tip' in sec),
    ("tip not repeating intro",           'already use SQL stored procedures' not in sec.split('bg-amber-tip')[1]),
]

passed = sum(1 for _, v in checks if v)
total  = len(checks)
print(f"\nComparison rewrite — {passed}/{total} checks\n")
for name, v in checks:
    print(f"  {'OK' if v else 'FAIL'} {name}")
