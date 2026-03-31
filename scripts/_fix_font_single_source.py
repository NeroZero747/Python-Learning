#!/usr/bin/env python3
"""
Make :root the single source of truth for fonts.
All CSS rules reference var(--font-body) / var(--font-mono) instead of
repeating the full stack. Removes the redundant bare h1-h6 font-family
declaration (covered by #hub-root * with !important).
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
    # 1. #hub-root, #hub-root * — use var() instead of hardcoded stack
    (
        "    font-family: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif !important;\n"
        "    box-sizing: border-box !important;",
        "    font-family: var(--font-body) !important;\n"
        "    box-sizing: border-box !important;",
    ),
    # 2. #hub-root code/pre — use var() instead of hardcoded mono stack
    (
        "    font-family: 'Fira Code', ui-monospace, 'Cascadia Code', monospace !important;",
        "    font-family: var(--font-mono) !important;",
    ),
    # 3. Remove the redundant bare h1-h6 font-family line
    #    (hub-root * !important covers this for Confluence; :root var covers standalone)
    (
        "    /* Headings */\n"
        "    h1, h2, h3, h4, h5, h6 {\n"
        "      font-family: var(--font-body) !important;\n"
        "      margin-top: 0;\n"
        "      margin-bottom: 0;\n"
        "      padding: 0;\n"
        "      line-height: 1.3;\n"
        "    }",
        "    /* Headings */\n"
        "    h1, h2, h3, h4, h5, h6 {\n"
        "      margin-top: 0;\n"
        "      margin-bottom: 0;\n"
        "      padding: 0;\n"
        "      line-height: 1.3;\n"
        "    }",
    ),
    # 4. Inline version of heading block (lessons 02-06)
    (
        "    h1, h2, h3, h4, h5, h6 { font-family: var(--font-body) !important; margin-top: 0; margin-bottom: 0; padding: 0; line-height: 1.3; }",
        "    h1, h2, h3, h4, h5, h6 { margin-top: 0; margin-bottom: 0; padding: 0; line-height: 1.3; }",
    ),
]


def fix_file(path):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for old, new in REPLACEMENTS:
        content = content.replace(old, new)

    if content == original:
        print(f'  — No changes: {name}')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✅ Fixed: {name}')


for lesson in LESSONS:
    fix_file(os.path.join(BASE, lesson))

fix_file(TEMPLATE)
print('\nDone.')
