#!/usr/bin/env python3
"""
Fix:
  1. kc-tab-num color coding lost — JS classList.remove/add so !important CSS
     doesn't override the dynamically-set inline background/color.
  2. Inactive dark pill tab text: #d1d5db → #ffffff (white).
"""

import os

BASE     = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started'
TEMPLATE = '/Users/graywolf/Documents/Project/Python-Learning/docs/new_lesson_template.html'

LESSONS = [
    'lesson01_what_is_python.html',
    'lesson02_how_to_request_access_software.html',
    'lesson03_how_to_install_extensions_in_vs_code.html',
    'lesson04_how_to_setup_a_virtual_environment.html',
    'lesson05_how_to_install_libraries_in_a_virtual_environment.html',
    'lesson06_how_to_run_a_python_notebook_or_script.html',
]

REPLACEMENTS = [
    # ── Fix 1a: active kc-tab-num — remove Tailwind classes so inline style wins ──
    (
        "if (num) { num.style.background = c.num; num.style.color = '#fff'; num.style.boxShadow = '0 2px 8px ' + c.numShadow; }",
        "if (num) { num.classList.remove('bg-gray-100','text-gray-400'); num.style.background = c.num; num.style.color = '#fff'; num.style.boxShadow = '0 2px 8px ' + c.numShadow; }",
    ),
    # ── Fix 1b: inactive kc-tab-num — restore Tailwind classes ──
    (
        "if (num) { num.style.background = '#f3f4f6'; num.style.color = '#9ca3af'; num.style.boxShadow = 'none'; }",
        "if (num) { num.classList.add('bg-gray-100','text-gray-400'); num.style.background = '#f3f4f6'; num.style.color = '#9ca3af'; num.style.boxShadow = 'none'; }",
    ),
    # ── Fix 2: inactive dark pill tab text → white ──
    (
        "    background-color: #1f2937 !important;\n    color: #d1d5db !important;\n  }",
        "    background-color: #1f2937 !important;\n    color: #ffffff !important;\n  }",
    ),
]


def fix_file(path: str) -> None:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for old, new in REPLACEMENTS:
        if old in content:
            content = content.replace(old, new, 1)
        else:
            print(f'  ⚠  Pattern not found in {name}:\n     {old[:80]}...')

    if content == original:
        print(f'  — No changes: {name}')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✅ Fixed: {name}')


for lesson in LESSONS:
    path = os.path.join(BASE, lesson)
    if os.path.exists(path):
        fix_file(path)
    else:
        print(f'  ❌ Not found: {lesson}')

if os.path.exists(TEMPLATE):
    fix_file(TEMPLATE)
else:
    print(f'  ❌ Template not found')

print('\nDone.')
