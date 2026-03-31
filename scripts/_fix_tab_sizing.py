#!/usr/bin/env python3
"""
Fix pill tab size inconsistency.

Root cause: sizing lives on .pill-tab (specificity 0,0,1,0 / 0,1,1,0 in hub-root)
but the INACTIVE state uses :not(.ce-step-active) which has specificity 0,0,2,0
/ 0,1,2,0 in hub-root. If Confluence re-adds padding to <button> elements, the
:not() rule wins for inactive buttons but NOT for active buttons, causing a size
mismatch.

Fix: add the same sizing directly on .ce-step / .mk-step / .qz-step / .pe-step
(the semantic classes always present on ALL button states). This guarantees
identical sizing for active AND inactive at the same specificity level.
"""

import os

BASE = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started'
TEMPLATE = '/Users/graywolf/Documents/Project/Python-Learning/docs/new_lesson_template.html'

LESSONS = [
    'lesson01_what_is_python.html',
    'lesson02_how_to_request_access_software.html',
    'lesson03_how_to_install_extensions_in_vs_code.html',
    'lesson04_how_to_setup_a_virtual_environment.html',
    'lesson05_how_to_install_libraries_in_a_virtual_environment.html',
    'lesson06_how_to_run_a_python_notebook_or_script.html',
]

STEP_SIZE_BASE = (
    '\n'
    '    /* ─── Step tab consistent sizing\n'
    '         Always on the semantic class (ce-step / mk-step etc.) so active\n'
    '         and inactive are guaranteed identical — no specificity conflict. */\n'
    '    .ce-step, .mk-step, .qz-step, .pe-step {\n'
    '      display: inline-flex;\n'
    '      align-items: center;\n'
    '      gap: 0.5rem;\n'
    '      padding: 0.5rem 1rem;\n'
    '      border-radius: 9999px;\n'
    '      border: none;\n'
    '      cursor: pointer;\n'
    '      font-size: 0.75rem;\n'
    '      font-weight: 700;\n'
    '      line-height: 1.2;\n'
    '      white-space: nowrap;\n'
    '    }\n'
)

STEP_SIZE_HUB = (
    '\n'
    '  /* ── Step tab consistent sizing — semantic class beats Confluence button rules ── */\n'
    '  #hub-root .ce-step,\n'
    '  #hub-root .mk-step,\n'
    '  #hub-root .qz-step,\n'
    '  #hub-root .pe-step {\n'
    '    display: inline-flex !important;\n'
    '    align-items: center !important;\n'
    '    gap: 0.5rem !important;\n'
    '    padding: 0.5rem 1rem !important;\n'
    '    border-radius: 9999px !important;\n'
    '    border: none !important;\n'
    '    cursor: pointer !important;\n'
    '    font-size: 0.75rem !important;\n'
    '    font-weight: 700 !important;\n'
    '    line-height: 1.2 !important;\n'
    '    white-space: nowrap !important;\n'
    '  }\n'
)

SIMPLE = [
    # 1. Base CSS: insert after .pill-tab .iconify rule
    (
        '    .pill-tab .iconify { font-size: 13px; }\n'
        '\n'
        '    /* Key Concepts sidebar tabs */\n',

        '    .pill-tab .iconify { font-size: 13px; }\n'
        + STEP_SIZE_BASE +
        '\n'
        '    /* Key Concepts sidebar tabs */\n',
    ),

    # 2. Hub-root: insert after #hub-root .pill-tab .iconify rule
    (
        '  #hub-root .pill-tab .iconify { font-size: 13px !important; }\n'
        '\n'
        '  /* ── Skill dots ── */\n',

        '  #hub-root .pill-tab .iconify { font-size: 13px !important; }\n'
        + STEP_SIZE_HUB +
        '\n'
        '  /* ── Skill dots ── */\n',
    ),
]


def fix_file(path):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for old, new in SIMPLE:
        content = content.replace(old, new)

    if content == original:
        print(f'  — No changes: {name}')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✅ Updated: {name}')


for lesson in LESSONS:
    fix_file(os.path.join(BASE, lesson))

fix_file(TEMPLATE)
print('\nDone.')
