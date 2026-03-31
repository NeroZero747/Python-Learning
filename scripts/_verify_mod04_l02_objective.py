"""Verify the rewritten #objective section in lesson02_project_folder_structure.html."""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

checks = [
    # Section shell
    ('id="objective"',                                       'section id present'),
    ('data-icon="fa6-solid:bullseye"',                       'bullseye icon in header'),
    ('Lesson Objective',                                     'section title'),
    ('The goal and expected outcome of this lesson',         'section subtitle'),
    # Card 1
    ('data-icon="fa6-solid:folder-open"',                    'card 1 icon folder-open'),
    ('Why structure matters',                                 'card 1 title'),
    ('without hunting through one enormous file',             'card 1 description'),
    # Card 2
    ('data-icon="fa6-solid:folder-tree"',                    'card 2 icon folder-tree'),
    ('Organising projects into folders',                      'card 2 title'),
    ('gives every type of file a predictable home',          'card 2 description'),
    # Card 3
    ('data-icon="fa6-solid:file-code"',                      'card 3 icon file-code'),
    ('Splitting scripts by purpose',                          'card 3 title'),
    ("fixing one step won",                                   'card 3 description'),
    # Card 4
    ('data-icon="fa6-solid:layer-group"',                    'card 4 icon layer-group'),
    ('A typical analytics layout',                            'card 4 title'),
    ('start any new analytics project with a consistent structure', 'card 4 description'),
    # Amber tip
    ('bg-amber-tip',                                          'amber tip box class'),
    ('fa6-solid:circle-info',                                 'amber tip icon'),
    ('This lesson gives you a practical folder layout',       'amber tip text'),
    # Structure
    ('grid grid-cols-1 sm:grid-cols-2 gap-3',                '2-column grid'),
    ('obj-card',                                              'obj-card class present'),
    ('bg-brand-soft',                                         'bg-brand-soft on icons'),
    ('text-brand',                                            'text-brand on icons'),
]

passed = 0
failed = 0

for needle, label in checks:
    if needle in html:
        print(f"  ✅  {label}")
        passed += 1
    else:
        print(f"  ❌  MISSING: {label!r}  (needle: {needle!r})")
        failed += 1

# Count exactly 4 obj-card divs within the #objective section only
obj_start = html.index('id="objective"')
obj_end = html.index('</section>', obj_start) + len('</section>')
obj_chunk = html[obj_start:obj_end]
obj_card_count = obj_chunk.count('class="obj-card ')
if obj_card_count == 4:
    print(f"  ✅  exactly 4 obj-card divs")
    passed += 1
else:
    print(f"  ❌  expected 4 obj-card divs, found {obj_card_count}")
    failed += 1

# Confirm all 4 icons are different
icons = []
import re
icon_matches = re.findall(r'data-icon="(fa6-solid:[^"]+)"', obj_chunk)
# Exclude the header bullseye from the card icon count
card_icons = [i for i in icon_matches if i != 'fa6-solid:bullseye' and i != 'fa6-solid:circle-info']
if len(card_icons) == 4 and len(set(card_icons)) == 4:
    print(f"  ✅  4 unique card icons: {card_icons}")
    passed += 1
else:
    print(f"  ❌  expected 4 unique card icons, got: {card_icons}")
    failed += 1

total = passed + failed
print(f"\n{'='*50}")
print(f"{passed}/{total} checks — {'All checks passed.' if failed == 0 else f'{failed} FAILED.'}")
