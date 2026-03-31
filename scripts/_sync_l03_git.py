"""
Sync lesson03_introduction_to_git_simple_workflow.html style block to match lesson01_what_is_programming.html.
Steps: 2 (replace style), 4 (hover fix). Steps 1 and 3 are already correct.
"""

L01 = 'pages/track_01_python_foundation/mod_02_programming_foundations/lesson01_what_is_programming.html'
L03 = 'pages/track_01_python_foundation/mod_04_python_best_practices/lesson03_introduction_to_git_simple_workflow.html'

l01_lines = open(L01).readlines()
l03_lines = open(L03).readlines()

# --- Find style block boundaries ---
def find_style(lines):
    start = next(i for i, l in enumerate(lines) if '<style>' in l)
    end   = next(i for i, l in enumerate(lines) if '</style>' in l)
    return start, end

s1, e1 = find_style(l01_lines)
s3, e3 = find_style(l03_lines)

print(f'lesson01 style block: lines {s1+1}–{e1+1}  ({e1-s1+1} lines)')
print(f'lesson03 style block: lines {s3+1}–{e3+1}  ({e3-s3+1} lines)')

style_l01 = l01_lines[s1:e1+1]
style_l03 = l03_lines[s3:e3+1]

if style_l01 == style_l03:
    print('Style blocks are already IDENTICAL — no replacement needed.')
else:
    diffs = sum(1 for a, b in zip(style_l01, style_l03) if a != b)
    print(f'Style blocks DIFFER ({diffs} lines differ, length diff {len(style_l01)-len(style_l03)})')
    for i, (a, b) in enumerate(zip(style_l01, style_l03)):
        if a != b:
            print(f'  offset {i}: L01={repr(a.rstrip()[:70])}')
            print(f'             L03={repr(b.rstrip()[:70])}')
            if i > 10:
                break

# --- Step 2: Replace style block ---
new_l03 = l03_lines[:s3] + style_l01 + l03_lines[e3+1:]

# --- Step 4: Apply white-hover fix ---
# Find and replace the three hover rules
BEFORE = [
    '    .obj-card-kt:hover { box-shadow: none; }\n',
    '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }\n',
    '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }\n',
]
AFTER = [
    '    .obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }\n',
    '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }\n',
    '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }\n',
]

content = ''.join(new_l03)

already_fixed = 'background-color: #ffffff; }' in content and '.obj-card-kt:hover' in content

if already_fixed:
    print('Step 4: hover fix already present — skipping.')
else:
    for b, a in zip(BEFORE, AFTER):
        if b in content:
            content = content.replace(b, a, 1)
            print(f'Step 4: fixed — {b.strip()[:60]}')
        else:
            print(f'Step 4: WARNING — could not find: {b.strip()[:60]}')

# --- Write output ---
with open(L03, 'w') as f:
    f.write(content)
print(f'\nWritten: {L03}')

# --- Verification ---
result = open(L03).readlines()
sr, er = find_style(result)
new_style = result[sr:er+1]
print('\n=== VERIFICATION ===')
print(f'  File starts with link tag: {result[0].strip().startswith("<link")}')
print(f'  File ends with </script>: {result[-1].strip() == "</script>"}')
hub_root_count = sum(1 for l in result if 'id="hub-root"' in l)
print(f'  id="hub-root" occurrences: {hub_root_count}')
print(f'  Style lines match lesson01: {new_style == style_l01}')
kt_ok = any('.obj-card-kt:hover' in l and 'background-color: #ffffff' in l for l in result)
vl_ok = any('.obj-card-violet:hover' in l and 'background-color: #ffffff' in l for l in result)
bl_ok = any('.obj-card-blue:hover' in l and 'background-color: #ffffff' in l for l in result)
print(f'  .obj-card-kt:hover has background-color: {kt_ok}')
print(f'  .obj-card-violet:hover has background-color: {vl_ok}')
print(f'  .obj-card-blue:hover has background-color: {bl_ok}')
