#!/usr/bin/env python3
"""
Fix active tab pill state in Confluence:
- Add gradient background !important so active tab is visible
- Add box-shadow for the slight glow
"""
import os

BASE = 'pages/track_01/mod_01_getting_started'
TEMPLATE = 'docs/new_lesson_template.html'

FILES = sorted(
    [os.path.join(BASE, f) for f in os.listdir(BASE) if f.endswith('.html')]
) + [TEMPLATE]

OLD = (
    '  #hub-root .ce-step-active,\n'
    '  #hub-root .mk-step-active,\n'
    '  #hub-root .qz-step-active,\n'
    '  #hub-root .pe-step-active { color: #ffffff !important; }'
)

NEW = (
    '  #hub-root .ce-step-active,\n'
    '  #hub-root .mk-step-active,\n'
    '  #hub-root .qz-step-active,\n'
    '  #hub-root .pe-step-active {\n'
    '    background: linear-gradient(to right, #CB187D, #e84aad) !important;\n'
    '    color: #ffffff !important;\n'
    '    box-shadow: 0 4px 12px rgba(203,24,125,0.35) !important;\n'
    '  }'
)

for path in FILES:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if OLD not in content:
        print(f'  - not found: {name}')
        continue
    content = content.replace(OLD, NEW)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {name}')

print('\nDone.')
