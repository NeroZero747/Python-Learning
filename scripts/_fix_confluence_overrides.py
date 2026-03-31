#!/usr/bin/env python3
"""
Add three Confluence-specific #hub-root override blocks to all lesson files:
1. Stat pill link color (a.hero-pill gets Confluence's blue link color)
2. Pill tab consistent sizing (Tailwind px-4 py-2 stripped by Confluence)
3. TOC active item pink highlight
"""
import os

BASE = 'pages/track_01/mod_01_getting_started'
TEMPLATE = 'docs/new_lesson_template.html'

FILES = sorted(
    [os.path.join(BASE, f) for f in os.listdir(BASE) if f.endswith('.html')]
) + [TEMPLATE]

NEW_RULES = (
    '\n'
    '  /* -- Stat pill link color (Confluence link-color override) -- */\n'
    '  #hub-root a.hero-pill { color: #CB187D !important; }\n'
    '\n'
    '  /* -- Pill tab consistent sizing (Confluence Tailwind fix) -- */\n'
    '  #hub-root .ce-step, #hub-root .mk-step,\n'
    '  #hub-root .qz-step, #hub-root .pe-step {\n'
    '    display: inline-flex !important;\n'
    '    align-items: center !important;\n'
    '    gap: 0.5rem !important;\n'
    '    padding: 0.375rem 1rem !important;\n'
    '    border-radius: 9999px !important;\n'
    '    font-size: 0.75rem !important;\n'
    '    font-weight: 700 !important;\n'
    '    line-height: 1.2 !important;\n'
    '    white-space: nowrap !important;\n'
    '    border: none !important;\n'
    '    cursor: pointer !important;\n'
    '  }\n'
    '\n'
    '  /* -- TOC active item pink highlight -- */\n'
    '  #hub-root .toc-link:hover { color: #CB187D !important; }\n'
    '  #hub-root .toc-link.active {\n'
    '    color: #CB187D !important;\n'
    '    font-weight: 600 !important;\n'
    '    border-left: 3px solid #CB187D !important;\n'
    '    padding-left: 8px !important;\n'
    '    background-color: #fdf0f7 !important;\n'
    '  }'
)

ANCHOR = '  #hub-root .hero-pill .opacity-50 { opacity: 1 !important; }'

for path in FILES:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if ANCHOR not in content:
        print(f'  - anchor not found: {name}')
        continue
    if 'a.hero-pill' in content:
        print(f'  - already patched: {name}')
        continue
    content = content.replace(ANCHOR, ANCHOR + NEW_RULES)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {name}')

print('\nDone.')
