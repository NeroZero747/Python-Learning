#!/usr/bin/env python3
"""Add margin-bottom to the #hub-root .hero-title-main rule so Confluence renders it."""

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

OLD = (
    '  #hub-root .hero-title-main {\n'
    '    font-size: 2.25rem !important;\n'
    '    font-weight: 800 !important;\n'
    '    line-height: 1.15 !important;\n'
    '  }'
)
NEW = (
    '  #hub-root .hero-title-main {\n'
    '    font-size: 2.25rem !important;\n'
    '    font-weight: 800 !important;\n'
    '    line-height: 1.15 !important;\n'
    '    margin-bottom: 2rem !important;\n'
    '  }'
)


def fix_file(path):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if OLD not in content:
        print(f'  — No match: {name}')
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.replace(OLD, NEW, 1))
    print(f'  ✅ Fixed: {name}')


for lesson in LESSONS:
    fix_file(os.path.join(BASE, lesson))

fix_file(TEMPLATE)
print('\nDone.')
