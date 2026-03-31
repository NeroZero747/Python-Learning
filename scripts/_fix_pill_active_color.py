#!/usr/bin/env python3
"""
Fix active pill tab font color: remove 'text-gray-400' class when tab becomes
active (so !important CSS class rule doesn't override inline style white text),
and restore it when going inactive.
Also add hub-root CSS anchoring white text on active steps.
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

# For each step type, fix active (remove text-gray-400) and inactive (add it back)
STEP_TYPES = ['ce-step', 'mk-step', 'pe-step', 'qz-step']

REPLACEMENTS = []
for st in STEP_TYPES:
    # active branch: remove text-gray-400 before setting inline color
    REPLACEMENTS.append((
        f"        s.classList.add('{st}-active');\n"
        f"        s.style.background = 'linear-gradient(to right, #CB187D, #e84aad)';\n"
        f"        s.style.color = '#fff';",
        f"        s.classList.add('{st}-active');\n"
        f"        s.classList.remove('text-gray-400');\n"
        f"        s.style.background = 'linear-gradient(to right, #CB187D, #e84aad)';\n"
        f"        s.style.color = '#fff';",
    ))
    # inactive branch: re-add text-gray-400 (though inline style also sets dark bg)
    REPLACEMENTS.append((
        f"        s.classList.remove('{st}-active');\n"
        f"        s.style.background = '#1f2937';\n"
        f"        s.style.color = '#ffffff';",
        f"        s.classList.remove('{st}-active');\n"
        f"        s.classList.add('text-gray-400');\n"
        f"        s.style.background = '#1f2937';\n"
        f"        s.style.color = '#ffffff';",
    ))

# Hub-root CSS: add explicit active-step white text rule
REPLACEMENTS.append((
    '  /* ── Dark pill tabs — dark bg, white text ── */\n'
    '  #hub-root .ce-step:not(.ce-step-active),\n'
    '  #hub-root .mk-step:not(.mk-step-active),\n'
    '  #hub-root .qz-step:not(.qz-step-active),\n'
    '  #hub-root .pe-step:not(.pe-step-active) {\n'
    '    background-color: #1f2937 !important;\n'
    '    color: #ffffff !important;\n'
    '  }',
    '  /* ── Dark pill tabs — dark bg, white text ── */\n'
    '  #hub-root .ce-step:not(.ce-step-active),\n'
    '  #hub-root .mk-step:not(.mk-step-active),\n'
    '  #hub-root .qz-step:not(.qz-step-active),\n'
    '  #hub-root .pe-step:not(.pe-step-active) {\n'
    '    background-color: #1f2937 !important;\n'
    '    color: #ffffff !important;\n'
    '  }\n'
    '  #hub-root .ce-step-active,\n'
    '  #hub-root .mk-step-active,\n'
    '  #hub-root .qz-step-active,\n'
    '  #hub-root .pe-step-active { color: #ffffff !important; }',
))


def fix_file(path: str) -> None:
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
