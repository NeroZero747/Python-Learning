import re

path = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(path).read()

m = re.search(r'<section id="objective".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

checks = [
    ("section present",           'id="objective"' in sec),
    ("scroll-mt-24 class",        "scroll-mt-24" in sec),
    ("header icon bullseye",      "fa6-solid:bullseye" in sec),
    ("header title",              "Lesson Objective" in sec),
    ("header subtitle",           "The goal and expected outcome" in sec),
    ("body wrapper classes",      "bg-white px-8 py-7" in sec),
    ("grid 2-col",                "grid-cols-1 sm:grid-cols-2 gap-3" in sec),
    ("4 obj-cards",               sec.count("obj-card") == 4),
    ("icon cube",                 "fa6-solid:cube" in sec),
    ("icon file-code",            "fa6-solid:file-code" in sec),
    ("icon folder-tree",          "fa6-solid:folder-tree" in sec),
    ("icon arrow-right-to-bracket","fa6-solid:arrow-right-to-bracket" in sec),
    ("title What a Module Is",    "What a Module Is" in sec),
    ("title Splitting Code",      "Splitting Code into Files" in sec),
    ("title Organising Larger",   "Organising Larger Projects" in sec),
    ("title Importing from",      "Importing from a Module" in sec),
    ("desc 1 present",            "holds functions you want to reuse" in sec),
    ("desc 2 present",            "each part of your project has a clear home" in sec),
    ("desc 3 present",            "too large to read, test, or update" in sec),
    ("desc 4 present",            "the script that needs it" in sec),
    ("amber tip icon",            "fa6-solid:circle-info" in sec),
    ("amber tip text",            "maintainable as they grow beyond a single script" in sec),
    ("bg-amber-tip present",      "bg-amber-tip" in sec),
    ("old icon chart-column gone","fa6-solid:chart-column" not in sec),
    ("old icon scale-balanced gone","fa6-solid:scale-balanced" not in sec),
    ("old icon wrench gone",      "fa6-solid:wrench" not in sec),
    ("old lowercase title gone",  "what a Python module is" not in sec),
    ("old amber text gone",       "By the end of this lesson learners will understand" not in sec),
]

passed = sum(1 for _, v in checks if v)
total  = len(checks)
print(f"\nObjective rewrite — {passed}/{total} checks\n")
for name, v in checks:
    print(f"  {'OK' if v else 'FAIL'} {name}")
