#!/usr/bin/env python3
"""
Fix:
  1. Tab pill inactive state → white bg, dark text, subtle border
  2. Hero h1 → more space before subtitle (mb-3 → mb-5)
  3. Stat pill icon/label opacity → consistent and fully visible
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
    # ── 1a. Hover states: dark → light hover ──────────────────────────────────
    (
        '.ce-step:not(.ce-step-active):hover { background: #374151; color: #d1d5db; }',
        '.ce-step:not(.ce-step-active):hover { background: #f3f4f6; color: #111827; }',
    ),
    (
        '.mk-step:not(.mk-step-active):hover { background: #374151; color: #d1d5db; }',
        '.mk-step:not(.mk-step-active):hover { background: #f3f4f6; color: #111827; }',
    ),
    (
        '.qz-step:not(.qz-step-active):hover { background: #374151; color: #d1d5db; }',
        '.qz-step:not(.qz-step-active):hover { background: #f3f4f6; color: #111827; }',
    ),
    (
        '.pe-step:not(.pe-step-active):hover { background: #374151; color: #d1d5db; }',
        '.pe-step:not(.pe-step-active):hover { background: #f3f4f6; color: #111827; }',
    ),
    # ── 1b. Hub-root CSS: inactive step pill → white with border ──────────────
    (
        '  /* ── Dark pill tabs — white inactive state ── */\n  #hub-root .ce-step:not(.ce-step-active),\n  #hub-root .mk-step:not(.mk-step-active),\n  #hub-root .qz-step:not(.qz-step-active),\n  #hub-root .pe-step:not(.pe-step-active) {\n    background-color: #1f2937 !important;\n    color: #ffffff !important;\n  }',
        '  /* ── Dark pill tabs — white inactive state ── */\n  #hub-root .ce-step:not(.ce-step-active),\n  #hub-root .mk-step:not(.mk-step-active),\n  #hub-root .qz-step:not(.qz-step-active),\n  #hub-root .pe-step:not(.pe-step-active) {\n    background-color: #ffffff !important;\n    color: #374151 !important;\n    border: 1.5px solid #e5e7eb !important;\n  }\n  #hub-root .ce-step-active,\n  #hub-root .mk-step-active,\n  #hub-root .qz-step-active,\n  #hub-root .pe-step-active {\n    border: none !important;\n  }',
    ),
    # older name in case some files still have old comment text
    (
        '  /* ── Dark pill tabs: ensure dark bg renders in Confluence ── */\n  #hub-root .ce-step:not(.ce-step-active),\n  #hub-root .mk-step:not(.mk-step-active),\n  #hub-root .qz-step:not(.qz-step-active),\n  #hub-root .pe-step:not(.pe-step-active) {\n    background-color: #1f2937 !important;\n    color: #ffffff !important;\n  }',
        '  /* ── Dark pill tabs — white inactive state ── */\n  #hub-root .ce-step:not(.ce-step-active),\n  #hub-root .mk-step:not(.mk-step-active),\n  #hub-root .qz-step:not(.qz-step-active),\n  #hub-root .pe-step:not(.pe-step-active) {\n    background-color: #ffffff !important;\n    color: #374151 !important;\n    border: 1.5px solid #e5e7eb !important;\n  }\n  #hub-root .ce-step-active,\n  #hub-root .mk-step-active,\n  #hub-root .qz-step-active,\n  #hub-root .pe-step-active {\n    border: none !important;\n  }',
    ),
    # ── 1c. JS: inactive step pill → white bg, dark text ─────────────────────
    (
        "        s.style.background = '#1f2937';",
        "        s.style.background = '#ffffff';",
    ),
    (
        "        s.style.color = '#9ca3af';",
        "        s.style.color = '#374151';",
    ),
    # ── 2. Hero h1: more space before subtitle ────────────────────────────────
    (
        'text-white mb-3 leading-[1.15] tracking-tight',
        'text-white mb-5 leading-[1.15] tracking-tight',
    ),
    # ── 3. Stat pill icons + labels: remove faded opacity ─────────────────────
    # Add CSS rule for hero-pill icon/label consistency after the bg-gray-900 line
    (
        '  #hub-root .bg-gray-900 { background-color: #111827 !important; }',
        '  #hub-root .bg-gray-900 { background-color: #111827 !important; }\n\n  /* ── Stat pill icons and labels — consistent full visibility ── */\n  #hub-root .hero-pill .iconify { opacity: 1 !important; }\n  #hub-root .hero-pill .opacity-55 { opacity: 0.7 !important; }',
    ),
]


def fix_file(path: str) -> None:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for old, new in REPLACEMENTS:
        if old in content:
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
