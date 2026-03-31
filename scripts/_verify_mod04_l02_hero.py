"""Verify the rewritten hero section in lesson02_project_folder_structure.html."""

import re
from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

checks = [
    # Section present
    ('class="hero-container"',               'hero-container section present'),
    # Background layers (locked)
    ('class="hero-dots"',                    'hero-dots present'),
    ('class="hero-glow hero-glow-1"',        'hero-glow-1 present'),
    ('class="hero-glow hero-glow-2"',        'hero-glow-2 present'),
    ('class="hero-glow-line"',               'hero-glow-line present'),
    # Module badge
    ('data-icon="fa6-solid:star"',           'module icon star present'),
    ('Module 4',                             'Module 4 label present'),
    # Difficulty — Beginner (1 green dot)
    ('background:#22c55e',                   'green dot present'),
    ('background:#d1d5db',                   'gray dot(s) present'),
    ('Beginner',                             'Beginner difficulty label'),
    # Read time
    ('5 min read',                           '5 min read present'),
    # Lesson label
    ('Lesson 02',                            'Lesson 02 label (two-digit)'),
    # Title
    ('Project Folder Structure',             'lesson title present'),
    # Subtitle
    ('Discover how splitting a Python project', 'subtitle text present'),
    ('makes your work easier to find and update', 'subtitle ending present'),
    # Author row
    ('Python Learning Hub',                  'author name present'),
    ('fa6-solid:user',                       'user icon present'),
    ('fa6-regular:calendar',                 'calendar icon present'),
    ('text-white/30',                        'separator present'),
    ('March 29, 2026',                       'publication date present'),
    # Stat pills
    ('#objective',                           'Goals stat pill link present'),
    ('#code-examples',                       'Examples stat pill link present'),
    ('#practice',                            'Exercises stat pill link present'),
    ('fa6-solid:bullseye',                   'goals icon present'),
    ('fa6-solid:dumbbell',                   'exercises icon present'),
    ('fa6-solid:layer-group',                'progress icon present'),
    # Stat numbers
    ('>4<',                                  'Goals count 4'),
    ('>3<',                                  'Exercises count 3'),
    # Progress
    ('2<span class="font-bold opacity-50">/5</span>', 'progress 2/5'),
    # SVG locked elements
    ('viewBox="0 0 280 324"',                'SVG viewBox correct'),
    ('padding:0.25rem;opacity:0.75;',        'hero-abstract-card style correct'),
    ('id="hexFill"',                         'hexFill gradient present'),
    ('logos:python',                         'Python logo in SVG present'),
    ('>PYTHON<',                             'PYTHON text in SVG'),
    ('>LEARNING HUB<',                       'LEARNING HUB text in SVG'),
    # hero-pill class present on badge pills
    ('class="hero-pill',                     'hero-pill class present'),
    # No wrong lesson number or old module icon
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

# Extra checks
# Subtitle word count (rough)
subtitle_match = re.search(r'Discover how splitting a Python project(.*?)makes your work easier to find and update', html, re.DOTALL)
if subtitle_match:
    print(f"  ✅  subtitle found in one coherent block")
    passed += 1
else:
    print(f"  ❌  subtitle not found as coherent block")
    failed += 1

# Exactly 1 hero section
hero_count = html.count('class="hero-container"')
if hero_count == 1:
    print(f"  ✅  exactly 1 hero-container section")
    passed += 1
else:
    print(f"  ❌  expected 1 hero-container, found {hero_count}")
    failed += 1

# "Lesson 03" should not appear (old wrong label)
if 'Lesson 03' not in html:
    print(f"  ✅  old 'Lesson 03' label not present")
    passed += 1
else:
    print(f"  ❌  stale 'Lesson 03' label still in file")
    failed += 1

# "Intermediate" should not appear in hero (old difficulty)
hero_start = html.index('class="hero-container"')
hero_end = html.index('</section>', hero_start) + len('</section>')
hero_chunk = html[hero_start:hero_end]
if 'Intermediate' not in hero_chunk:
    print(f"  ✅  'Intermediate' not in hero section")
    passed += 1
else:
    print(f"  ❌  stale 'Intermediate' still in hero section")
    failed += 1

total = passed + failed
print(f"\n{'='*50}")
print(f"{passed}/{total} checks — {'All checks passed.' if failed == 0 else f'{failed} FAILED.'}")
