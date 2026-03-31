import os, re

BASE = "pages/track_01_python_foundation/mod_04_python_best_practices"
FILES = [
    "lesson01_creating_your_own_modules.html",
    "lesson02_project_folder_structure.html",
    "lesson03_introduction_to_git_simple_workflow.html",
    "lesson04_git_in_vs_code.html",
    "lesson05_logging_basics.html",
]
CORRECT_HREFS = [
    "lesson01_creating_your_own_modules.html",
    "lesson02_project_folder_structure.html",
    "lesson03_introduction_to_git_simple_workflow.html",
    "lesson04_git_in_vs_code.html",
    "lesson05_logging_basics.html",
]
CORRECT_LABELS = ["1. Creating", "2. Project", "3. Introduction to Git", "4. Git in VS Code", "5. Logging"]
DEAD_HREFS = ["lesson02_creating", "lesson03_project", "lesson04_introduction", "lesson05_git_in", "lesson06_logging"]

all_pass = True
for i, fname in enumerate(FILES):
    path = os.path.join(BASE, fname)
    html = open(path).read()
    m = re.search(r'<div class="space-y-1">.*?</div>', html, re.DOTALL)
    block = m.group(0) if m else ""

    checks = []
    checks.append(("5 lesson links", block.count('<a href=') == 5))
    for href in CORRECT_HREFS:
        checks.append((f'href {href}', f'href="{href}"' in block))
    for label in CORRECT_LABELS:
        checks.append((f'label contains "{label}"', label in block))
    for dead in DEAD_HREFS:
        checks.append((f'no dead "{dead}"', dead not in block))
    active_marker = f'href="{FILES[i]}" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7]'
    checks.append((f'active = lesson {i+1}', active_marker in block))

    fails = [name for name, v in checks if not v]
    status = "OK" if not fails else f"FAIL: {fails}"
    print(f"  {'OK' if not fails else 'FAIL'}  {fname}  ({status})")
    if fails:
        all_pass = False

print()
print("All clear." if all_pass else "Some checks failed.")
