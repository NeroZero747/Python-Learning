"""Verify #objective section in lesson04."""
import pathlib

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")
html = TARGET.read_text(encoding='utf-8')

start = html.find('<section', html.find('id="objective"') - 10)
search = html[start:]
depth, end, i = 0, -1, 0
while i < len(search):
    if search[i:].startswith('<section'):
        depth += 1; i += len('<section')
    elif search[i:].startswith('</section>'):
        depth -= 1
        if depth == 0:
            end = start + i + len('</section>'); break
        i += len('</section>')
    else:
        i += 1

s = html[start:end]

checks = [
    ('Header: Lesson Objective',           '>Lesson Objective<'),
    ('Subtitle: goal and expected outcome', 'The goal and expected outcome of this lesson'),
    ('Card 1 icon: arrows-rotate',         'fa6-solid:arrows-rotate'),
    ('Card 1 title: What Refactoring',     '>What Refactoring Means<'),
    ('Card 2 icon: triangle-exclamation',  'fa6-solid:triangle-exclamation'),
    ('Card 2 title: Why Scripts',          '>Why Scripts Grow Messy<'),
    ('Card 3 icon: code',                  'fa6-solid:code'),
    ('Card 3 title: Converting Scripts',   '>Converting Scripts to Classes<'),
    ('Card 4 icon: layer-group',           'fa6-solid:layer-group'),
    ('Card 4 title: Benefits of a Class',  '>Benefits of a Class Structure<'),
    ('Amber tip wrapper div mt-5',         '<div class="mt-5">'),
    ('Amber tip inner div classes',        'class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"'),
    ('Amber tip starts: This lesson',      'This lesson gives you'),
    ('circle-info icon',                   'fa6-solid:circle-info'),
    ('No old header text',                 'Learning Objectives'),
]

passed, failed = 0, 0
for label, needle in checks:
    # last check is a NOT check
    if label.startswith('No old'):
        ok = needle not in s
        print(f'  {"✅" if ok else "❌"} {label}')
    else:
        ok = needle in s
        print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
print(f'File size: {len(html):,} chars')
