#!/usr/bin/env python3
"""
Make hero pills non-clickable via CSS only:
- Add pointer-events: none; cursor: default; to .hero-pill
- Remove transition: transform ... and the :hover rule
Keep <a href="..."> HTML structure intact.
"""
import os, re

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

def fix_css(content):
    # ── Multiline format (lesson01 & template) ──────────────────────────────
    # Remove "transition: transform 0.2s ease;" line and add pointer-events/cursor
    content = content.replace(
        '      transition: transform 0.2s ease;\n'
        '    }\n'
        '    .hero-pill:hover {\n'
        '      transform: translateY(-1px);\n'
        '    }',
        '      pointer-events: none;\n'
        '      cursor: default;\n'
        '    }'
    )
    # Template has no :hover block, just remove transition and add the two props
    content = content.replace(
        '      transition: transform 0.2s ease;\n'
        '    }',
        '      pointer-events: none;\n'
        '      cursor: default;\n'
        '    }'
    )

    # ── Inline format (lessons 02-06) ────────────────────────────────────────
    # .hero-pill inline rule: strip transition, add pointer-events & cursor
    content = re.sub(
        r'(\.hero-pill \{ background: #ffffff; border: none; color: #7F004C; font-weight: 700; )transition: transform 0\.2s ease; \}',
        r'\1pointer-events: none; cursor: default; }',
        content
    )
    # Remove the inline hover rule line entirely
    content = re.sub(
        r'    \.hero-pill:hover \{ transform: translateY\(-1px\); \}\n',
        '',
        content
    )
    return content


def fix_file(path):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    content = fix_css(original)
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
