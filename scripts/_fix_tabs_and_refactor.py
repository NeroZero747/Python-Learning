#!/usr/bin/env python3
"""
Fix tab colour contrast and refactor CSS across mod_01_getting_started lessons.

Changes per file:
  1. Remove `body {}` rule (only applies to the outer Confluence page body, not our content).
  2. Add dark-pill tab inactive background/colour CSS to the #hub-root block.
  3. Add `#hub-root .kc-tab-active .kc-tab-label` rule so JS colour switch isn't
     overridden by `#hub-root .text-gray-400 { color: ... !important }`.
  4. Add bg-colour utility overrides (bg-white, bg-gray-50/100/800/900) so
     Confluence renders them correctly.
  5. Merge the two <style> blocks into one to reduce duplication.
"""

import os
import re

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

# New CSS rules appended inside the #hub-root isolation block
NEW_CSS_BLOCK = """
  /* ── Dark pill tabs: ensure dark bg renders in Confluence ── */
  #hub-root .ce-step:not(.ce-step-active),
  #hub-root .mk-step:not(.mk-step-active),
  #hub-root .qz-step:not(.qz-step-active),
  #hub-root .pe-step:not(.pe-step-active) {
    background-color: #1f2937 !important;
    color: #d1d5db !important;
  }

  /* ── Key Concepts: active label must override .text-gray-400 !important ── */
  #hub-root .kc-tab-active .kc-tab-label { color: #111827 !important; }
  #hub-root .kc-tab:not(.kc-tab-active) .kc-tab-label { color: #9ca3af !important; }

  /* ── Background-colour utilities ── */
  #hub-root .bg-white    { background-color: #ffffff !important; }
  #hub-root .bg-gray-50  { background-color: #f9fafb !important; }
  #hub-root .bg-gray-100 { background-color: #f3f4f6 !important; }
  #hub-root .bg-gray-200 { background-color: #e5e7eb !important; }
  #hub-root .bg-gray-800 { background-color: #1f2937 !important; }
  #hub-root .bg-gray-900 { background-color: #111827 !important; }"""

# The closing anchor of the hub-root style block (same across all files)
HUB_ANCHOR = (
    '  #hub-root .text-xl.font-bold,\n'
    '  #hub-root h2.text-xl { font-size: 1.25rem !important; font-weight: 700 !important; }\n'
    '</style>'
)

HUB_ANCHOR_NEW = (
    '  #hub-root .text-xl.font-bold,\n'
    '  #hub-root h2.text-xl { font-size: 1.25rem !important; font-weight: 700 !important; }'
    + NEW_CSS_BLOCK + '\n'
    '</style>'
)


def fix_file(path: str) -> None:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # ── Step 1: Remove body {} (multiline version — lesson01 / template) ──
    content = re.sub(
        r'\n\n    /\* Root styling \*/\n    body \{[^}]+\}',
        '',
        content,
    )

    # ── Step 1b: Remove body {} (inline version — lessons 02-06) ──
    content = re.sub(
        r'\n    body \{ font-family:[^\n]+\}',
        '',
        content,
    )

    # ── Step 2: Inject new CSS before the hub-root block closing </style> ──
    if HUB_ANCHOR in content:
        content = content.replace(HUB_ANCHOR, HUB_ANCHOR_NEW, 1)
    else:
        print(f'  ⚠  Hub-root anchor not found in {name} — new CSS NOT added')

    # ── Step 3: Merge the two <style> blocks into one ──
    # Pattern:  (end of block 1)  "  </style>\n\n<style>\n"
    # Replace with a divider comment so there is only one <style> tag.
    merged, count = re.subn(
        r'  </style>\n\n<style>\n(?=\s*/\* ={40,})',
        '',
        content,
        count=1,
    )
    if count:
        content = merged
    else:
        print(f'  ⚠  Style-block merge pattern not found in {name} — blocks left separate')

    if content == original:
        print(f'  — No changes: {name}')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✅ Fixed: {name}')


# ── Process all lessons ──
for lesson in LESSONS:
    path = os.path.join(BASE, lesson)
    if os.path.exists(path):
        fix_file(path)
    else:
        print(f'  ❌ Not found: {lesson}')

# ── Process the template ──
if os.path.exists(TEMPLATE):
    fix_file(TEMPLATE)
else:
    print(f'  ❌ Template not found: {TEMPLATE}')

print('\nDone.')
