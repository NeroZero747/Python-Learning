#!/usr/bin/env python3
"""
Revert pill tab inactive state: dark bg (#1f2937) + white text (#ffffff).
Also restores the dark hover and removes the white-bg border from hub-root CSS.
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
    # ── CSS hover: restore dark hover ─────────────────────────────────────────
    (
        '.ce-step:not(.ce-step-active):hover { background: #f3f4f6; color: #111827; }',
        '.ce-step:not(.ce-step-active):hover { background: #374151; color: #ffffff; }',
    ),
    (
        '.mk-step:not(.mk-step-active):hover { background: #f3f4f6; color: #111827; }',
        '.mk-step:not(.mk-step-active):hover { background: #374151; color: #ffffff; }',
    ),
    (
        '.qz-step:not(.qz-step-active):hover { background: #f3f4f6; color: #111827; }',
        '.qz-step:not(.qz-step-active):hover { background: #374151; color: #ffffff; }',
    ),
    (
        '.pe-step:not(.pe-step-active):hover { background: #f3f4f6; color: #111827; }',
        '.pe-step:not(.pe-step-active):hover { background: #374151; color: #ffffff; }',
    ),
    # ── Hub-root CSS: dark bg + white text, no border ─────────────────────────
    (
        '  /* ── Dark pill tabs — white inactive state ── */\n'
        '  #hub-root .ce-step:not(.ce-step-active),\n'
        '  #hub-root .mk-step:not(.mk-step-active),\n'
        '  #hub-root .qz-step:not(.qz-step-active),\n'
        '  #hub-root .pe-step:not(.pe-step-active) {\n'
        '    background-color: #ffffff !important;\n'
        '    color: #374151 !important;\n'
        '    border: 1.5px solid #e5e7eb !important;\n'
        '  }\n'
        '  #hub-root .ce-step-active,\n'
        '  #hub-root .mk-step-active,\n'
        '  #hub-root .qz-step-active,\n'
        '  #hub-root .pe-step-active {\n'
        '    border: none !important;\n'
        '  }',
        '  /* ── Dark pill tabs — dark bg, white text ── */\n'
        '  #hub-root .ce-step:not(.ce-step-active),\n'
        '  #hub-root .mk-step:not(.mk-step-active),\n'
        '  #hub-root .qz-step:not(.qz-step-active),\n'
        '  #hub-root .pe-step:not(.pe-step-active) {\n'
        '    background-color: #1f2937 !important;\n'
        '    color: #ffffff !important;\n'
        '  }',
    ),
    # ── JS inactive: dark bg + white text ─────────────────────────────────────
    (
        "        s.style.background = '#ffffff';\n        s.style.color = '#374151';",
        "        s.style.background = '#1f2937';\n        s.style.color = '#ffffff';",
    ),
]


def fix_file(path: str) -> None:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for old, new in REPLACEMENTS:
        # replace ALL occurrences (4 JS functions use the same inactive pattern)
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
