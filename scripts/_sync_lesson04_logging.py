"""
Sync lesson04_logging_basics.html to match lesson01_what_is_programming.html's
CSS structure per the lesson-sync-format prompt.
"""
import re

LESSON01 = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_02_programming_foundations\lesson01_what_is_programming.html'
TARGET   = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

with open(LESSON01, 'r', encoding='utf-8') as f:
    l01 = f.read()

with open(TARGET, 'r', encoding='utf-8') as f:
    target = f.read()

print('=== BEFORE AUDIT ===')

# --- Check forbidden tags ---
forbidden = ['<!DOCTYPE', '</html>', '</body>', '<html', '<head>', '</head>', '<body>']
for tag in forbidden:
    if tag.lower() in target.lower():
        print(f'  FOUND forbidden tag: {tag}')
    else:
        print(f'  OK  no forbidden tag: {tag}')

# --- Check hub-root ---
has_hub = 'id="hub-root"' in target
print(f'  hub-root present: {has_hub}')

# --- Style block lines ---
s_start = target.find('<style>')
s_end   = target.find('</style>') + len('</style>')
print(f'  Target style lines: {target[s_start:s_end].count(chr(10))}')

# --- Extract lesson01 style block ---
l01_s_start = l01.find('<style>')
l01_s_end   = l01.find('</style>') + len('</style>')
l01_style   = l01[l01_s_start:l01_s_end]
print(f'  Lesson01 style lines: {l01_style.count(chr(10))}')

# --- Check hover rules ---
for rule in ['.obj-card-kt:hover', '.obj-card-violet:hover', '.obj-card-blue:hover']:
    idx = target.find(rule)
    if idx >= 0:
        print(f'  {rule}: {repr(target[idx:idx+90])}')
    else:
        print(f'  {rule}: NOT FOUND in target')

print()
print('=== APPLYING FIXES ===')

# STEP 1: Strip forbidden shell tags
# The file already appears clean — just verify and strip if present
lines = target.split('\n')
new_lines = []
skip_patterns = [
    r'^\s*<!DOCTYPE',
    r'^\s*<html',
    r'^\s*</html',
    r'^\s*<head>',
    r'^\s*</head>',
    r'^\s*<body>',
    r'^\s*</body>',
    r'^\s*<meta ',
    r'^\s*<title>',
    r'^\s*</title>',
]
stripped_count = 0
for line in lines:
    skip = False
    for pat in skip_patterns:
        if re.match(pat, line, re.IGNORECASE):
            skip = True
            stripped_count += 1
            print(f'  STRIPPED: {repr(line[:80])}')
            break
    if not skip:
        new_lines.append(line)
target = '\n'.join(new_lines)
print(f'  Step 1: stripped {stripped_count} forbidden lines')

# STEP 2: Replace style block
s_start = target.find('<style>')
s_end   = target.find('</style>') + len('</style>')
if s_start == -1:
    print('  ERROR: No <style> block found in target!')
else:
    target = target[:s_start] + l01_style + target[s_end:]
    print(f'  Step 2: replaced style block with lesson01 style ({l01_style.count(chr(10))} lines)')

# STEP 3: Add id="hub-root"
if 'id="hub-root"' in target:
    print('  Step 3: hub-root already present — skipping')
else:
    old = '<div class="bg-gray-50 min-h-screen">'
    new = '<div id="hub-root" class="bg-gray-50 min-h-screen">'
    if old in target:
        target = target.replace(old, new, 1)
        print('  Step 3: added id="hub-root"')
    else:
        print('  Step 3: WARNING — could not find outer wrapper div!')

# STEP 4: Apply white-hover fix to key takeaway cards
fixes = [
    ('.obj-card-kt:hover { box-shadow: none; }',
     '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }'),
    ('.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }',
     '.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }'),
    ('.obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }',
     '.obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }'),
]
for old, new in fixes:
    if 'background-color: #ffffff' in target and old.split('{')[0].strip() + ':hover' in target:
        print(f'  Step 4: {old[:40]}... already has white bg — skipping')
    elif old in target:
        target = target.replace(old, new)
        print(f'  Step 4: fixed {old[:40]}...')
    else:
        print(f'  Step 4: WARNING — could not find: {old[:60]}')

# --- Write result ---
with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(target)
print()
print('=== WRITTEN ===')

# --- Post-write verification ---
print()
print('=== POST-WRITE VERIFICATION ===')
with open(TARGET, 'r', encoding='utf-8') as f:
    result = f.read()

lines_result = result.split('\n')
# Check start
first_nonempty = next((l for l in lines_result if l.strip()), '')
print(f'  Starts with: {repr(first_nonempty[:70])}')
# Check end
last_nonempty = next((l for l in reversed(lines_result) if l.strip()), '')
print(f'  Ends with: {repr(last_nonempty[:70])}')

for tag in forbidden:
    if tag.lower() in result.lower():
        print(f'  FAIL: forbidden tag still present: {tag}')
    else:
        print(f'  OK  : no forbidden tag: {tag}')

hub_count = result.count('id="hub-root"')
print(f'  hub-root count: {hub_count} (expected 1)')

s_start = result.find('<style>')
s_end   = result.find('</style>') + len('</style>')
print(f'  Style block lines: {result[s_start:s_end].count(chr(10))} (lesson01: {l01_style.count(chr(10))})')

for rule in ['.obj-card-kt:hover', '.obj-card-violet:hover', '.obj-card-blue:hover']:
    idx = result.find(rule)
    if idx >= 0:
        snippet = result[idx:idx+90]
        has_white = 'background-color: #ffffff' in snippet
        print(f'  {rule}: white-bg={has_white} | {repr(snippet[:80])}')
    else:
        print(f'  {rule}: NOT FOUND')

print()
print('Done.')
