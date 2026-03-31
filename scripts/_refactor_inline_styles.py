#!/usr/bin/env python3
"""
Refactor: replace inline styles with CSS classes.
  1. CSS: hero-abstract-card — move padding/opacity into CSS rule
  2. CSS: kc-indicator — add default height to CSS rule
  3. CSS: hero-pill .iconify — correct opacity from 1 → 0.5
  4. CSS: inactive step pills — add box-shadow: none
  5. CSS: active step pills — add full gradient background + shadow
  6. HTML: remove style="opacity:0.5;" from stat pill icons
  7. HTML: remove style="padding:0.25rem;opacity:0.75;" from hero-abstract-card
  8. HTML: remove style="height:68px;" from kc-indicator
  9. JS: remove s.style.background/color/boxShadow lines (CSS handles it now)
"""

import os, re

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

SIMPLE = [

    # ── 1a. hero-abstract-card CSS (multiline — lesson01 / template) ──────────
    (
        '      padding: 1rem;\n'
        '      display: flex;\n'
        '      align-items: center;\n'
        '      justify-content: center;\n'
        '    }',
        '      padding: 0.25rem;\n'
        '      opacity: 0.75;\n'
        '      display: flex;\n'
        '      align-items: center;\n'
        '      justify-content: center;\n'
        '    }',
    ),
    # ── 1b. hero-abstract-card CSS (inline — lessons 02-06) ──────────────────
    (
        'padding: 1rem; display: flex; align-items: center; justify-content: center; }',
        'padding: 0.25rem; opacity: 0.75; display: flex; align-items: center; justify-content: center; }',
    ),
    # Only targets that `}` inside .hero-abstract-card rule — safe due to context

    # ── 2. kc-indicator default height added after .kc-tab-active rule ────────
    (
        '.kc-tab-active { background: #fdf0f7; }',
        '.kc-tab-active { background: #fdf0f7; }\n    .kc-indicator { height: 68px; }',
    ),

    # ── 3. hero-pill .iconify opacity: 1 → 0.5 ───────────────────────────────
    (
        '#hub-root .hero-pill .iconify { opacity: 1 !important; }',
        '#hub-root .hero-pill .iconify { opacity: 0.5 !important; }',
    ),

    # ── 4 & 5. Inactive step: add box-shadow:none; Active step: full rule ─────
    (
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
        '  /* ── Dark pill tabs — inactive (dark bg) ── */\n'
        '  #hub-root .ce-step:not(.ce-step-active),\n'
        '  #hub-root .mk-step:not(.mk-step-active),\n'
        '  #hub-root .qz-step:not(.qz-step-active),\n'
        '  #hub-root .pe-step:not(.pe-step-active) {\n'
        '    background-color: #1f2937 !important;\n'
        '    color: #ffffff !important;\n'
        '    box-shadow: none !important;\n'
        '  }\n'
        '  /* ── Dark pill tabs — active (pink gradient) ── */\n'
        '  #hub-root .ce-step-active,\n'
        '  #hub-root .mk-step-active,\n'
        '  #hub-root .qz-step-active,\n'
        '  #hub-root .pe-step-active {\n'
        '    background: linear-gradient(to right, #CB187D, #e84aad) !important;\n'
        '    color: #ffffff !important;\n'
        '    box-shadow: 0 10px 25px -5px rgba(203,24,125,0.3) !important;\n'
        '  }',
    ),

    # ── 6. HTML: remove style="opacity:0.5;" from stat pill icons ─────────────
    (' style="opacity:0.5;"', ''),

    # ── 7. HTML: remove inline style from hero-abstract-card ──────────────────
    (' style="padding:0.25rem;opacity:0.75;"', ''),

    # ── 8. HTML: remove inline height from kc-indicator ──────────────────────
    (' style="height:68px;"', ''),
]

# ── 9. JS: remove s.style lines from active/inactive branches ─────────────────
STEP_TYPES = ['ce-step', 'mk-step', 'pe-step', 'qz-step']

JS_ACTIVE_OLD  = (
    "        s.classList.add('{t}-active');\n"
    "        s.classList.remove('text-gray-400');\n"
    "        s.style.background = 'linear-gradient(to right, #CB187D, #e84aad)';\n"
    "        s.style.color = '#fff';\n"
    "        s.style.boxShadow = '0 10px 25px -5px rgba(203,24,125,0.3)';"
)
JS_ACTIVE_NEW  = (
    "        s.classList.add('{t}-active');\n"
    "        s.classList.remove('text-gray-400');"
)
JS_INACTIVE_OLD = (
    "        s.classList.remove('{t}-active');\n"
    "        s.classList.add('text-gray-400');\n"
    "        s.style.background = '#1f2937';\n"
    "        s.style.color = '#ffffff';\n"
    "        s.style.boxShadow = 'none';"
)
JS_INACTIVE_NEW = (
    "        s.classList.remove('{t}-active');\n"
    "        s.classList.add('text-gray-400');"
)


def fix_file(path):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for old, new in SIMPLE:
        content = content.replace(old, new)

    for t in STEP_TYPES:
        content = content.replace(JS_ACTIVE_OLD.replace('{t}', t),  JS_ACTIVE_NEW.replace('{t}', t))
        content = content.replace(JS_INACTIVE_OLD.replace('{t}', t), JS_INACTIVE_NEW.replace('{t}', t))

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
