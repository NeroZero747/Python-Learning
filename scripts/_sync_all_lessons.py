"""
Batch sync script — applies all 4 steps from lesson-sync-format.prompt.md
to every lesson file in track_01_python_foundation (or any target list).

Steps applied to each file:
  1. Strip forbidden HTML shell tags (DOCTYPE, html, head, body, /body, /html)
  2. Replace <style>…</style> block with lesson01's exact block
  3. Add id="hub-root" to the outer wrapper div (if missing)
  4. Add background-color: #ffffff to obj-card-kt/violet/blue :hover rules

Usage:
  python3 scripts/_sync_all_lessons.py              # all track_01 lessons
  python3 scripts/_sync_all_lessons.py mod_04       # only mod_04 lessons
  python3 scripts/_sync_all_lessons.py mod_04/lesson03  # single file
"""

import os
import re
import sys
import glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REFERENCE = os.path.join(
    BASE,
    'pages/track_01_python_foundation/mod_02_programming_foundations/lesson01_what_is_programming.html'
)

# All lesson files to process (skip lesson01 — it IS the reference)
ALL_LESSONS = sorted(glob.glob(
    os.path.join(BASE, 'pages/track_01_python_foundation/**/*.html'),
    recursive=True
))
ALL_LESSONS = [p for p in ALL_LESSONS if 'lesson' in os.path.basename(p) and p != REFERENCE]

# --- Filter by optional CLI argument (e.g. "mod_04" or "mod_04/lesson03") ---
filter_arg = sys.argv[1].replace('\\', '/') if len(sys.argv) > 1 else ''
if filter_arg:
    ALL_LESSONS = [p for p in ALL_LESSONS if filter_arg.replace('/', os.sep) in p]
    if not ALL_LESSONS:
        print(f'No files matched filter: {filter_arg}')
        sys.exit(1)

# ── Load reference style block ─────────────────────────────────────────────
ref_lines = open(REFERENCE).readlines()

def find_style(lines, path=''):
    try:
        start = next(i for i, l in enumerate(lines) if '<style>' in l)
        end   = next(i for i, l in enumerate(lines) if '</style>' in l)
        return start, end
    except StopIteration:
        raise ValueError(f'No <style> block found in {path}')

rs, re_ = find_style(ref_lines, REFERENCE)
REF_STYLE = ref_lines[rs:re_+1]   # includes the <style> and </style> lines

# ── Hover-fix strings ──────────────────────────────────────────────────────
HOVER_BEFORE = [
    '    .obj-card-kt:hover { box-shadow: none; }\n',
    '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }\n',
    '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }\n',
]
HOVER_AFTER = [
    '    .obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }\n',
    '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }\n',
    '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }\n',
]

# ── Shell-tag patterns to strip (Step 1) ──────────────────────────────────
SHELL_TAG_RE = re.compile(
    r'^\s*(<\!DOCTYPE[^>]*>|<html[^>]*>|</html>|<head>|</head>|<body>|</body>|<meta[^>]*>|<title>.*?</title>)\s*\n?',
    re.IGNORECASE
)


def sync_file(path):
    rel = os.path.relpath(path, BASE)
    lines = open(path).readlines()
    changed = []

    # ── Step 1: Strip HTML shell tags ─────────────────────────────────────
    original_first = lines[0].strip() if lines else ''
    new_lines = [l for l in lines if not SHELL_TAG_RE.match(l)]
    # Also catch blank lines left between </head> and <body>
    # Re-read as string and do a targeted strip
    content = ''.join(new_lines)
    # Remove stray blank lines at document start (before first <link>)
    content = re.sub(r'^\s*\n+(?=\s*<link)', '', content)
    new_lines = content.splitlines(keepends=True)

    if len(new_lines) != len(lines):
        changed.append(f'Step 1: removed {len(lines)-len(new_lines)} shell-tag lines')
    lines = new_lines

    # ── Step 2: Replace style block ───────────────────────────────────────
    try:
        ts, te = find_style(lines, path)
    except ValueError as e:
        print(f'  ⚠️  {e} — skipping.')
        return False

    target_style = lines[ts:te+1]
    if target_style == REF_STYLE:
        changed.append('Step 2: style already matches lesson01 — skipped')
    else:
        lines = lines[:ts] + REF_STYLE + lines[te+1:]
        changed.append(f'Step 2: replaced style block ({len(target_style)} → {len(REF_STYLE)} lines)')

    # ── Step 3: Add id="hub-root" ─────────────────────────────────────────
    content = ''.join(lines)
    if 'id="hub-root"' in content:
        changed.append('Step 3: id="hub-root" already present — skipped')
    else:
        new_content = content.replace(
            '<div class="bg-gray-50 min-h-screen">',
            '<div id="hub-root" class="bg-gray-50 min-h-screen">',
            1
        )
        if new_content == content:
            changed.append('Step 3: ⚠️ outer wrapper not found — manual check needed')
        else:
            content = new_content
            changed.append('Step 3: added id="hub-root"')
        lines = content.splitlines(keepends=True)

    # ── Step 4: Hover fix ─────────────────────────────────────────────────
    content = ''.join(lines)
    hover_already_fixed = all(
        a in content for a in [
            '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }',
        ]
    )
    if hover_already_fixed:
        changed.append('Step 4: hover fix already present — skipped')
    else:
        for b, a in zip(HOVER_BEFORE, HOVER_AFTER):
            content = content.replace(b, a, 1)
        changed.append('Step 4: applied hover background-color fix')

    # ── Write ─────────────────────────────────────────────────────────────
    with open(path, 'w') as f:
        f.write(content)

    return changed


def verify(path):
    lines = open(path).readlines()
    results = {}
    results['starts_with_link'] = lines[0].strip().startswith('<link')
    results['ends_with_script'] = lines[-1].strip() == '</script>'
    results['no_html_shell'] = not any(
        re.search(r'DOCTYPE|<html|</html>|<head>|</head>', l, re.I) for l in lines
    )
    results['hub_root_count'] = sum(1 for l in lines if 'id="hub-root"' in l)
    ts, te = find_style(lines, path)
    results['style_matches_ref'] = lines[ts:te+1] == REF_STYLE
    content = ''.join(lines)
    results['kt_hover_ok']     = '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }' in content
    results['violet_hover_ok'] = 'obj-card-violet:hover' in content and 'background-color: #ffffff' in content
    results['blue_hover_ok']   = 'obj-card-blue:hover' in content and 'background-color: #ffffff' in content
    return results


# ── Run ────────────────────────────────────────────────────────────────────
print(f'Reference: {os.path.relpath(REFERENCE, BASE)}')
print(f'Files to process: {len(ALL_LESSONS)}\n')
print('=' * 70)

all_ok = True
for path in ALL_LESSONS:
    rel = os.path.relpath(path, BASE)
    print(f'\n📄 {rel}')
    result = sync_file(path)
    if result is False:
        all_ok = False
        continue
    for msg in result:
        print(f'   {msg}')

    v = verify(path)
    ok = all([
        v['starts_with_link'], v['ends_with_script'],
        v['no_html_shell'], v['hub_root_count'] == 1,
        v['style_matches_ref'], v['kt_hover_ok'],
        v['violet_hover_ok'], v['blue_hover_ok'],
    ])
    status = '✅ PASS' if ok else '❌ FAIL'
    print(f'   {status}  (hub-root×{v["hub_root_count"]} | style_match={v["style_matches_ref"]} | hover={v["kt_hover_ok"]})')
    if not ok:
        all_ok = False
        for k, val in v.items():
            if val not in (True, 1):
                print(f'      ↳ FAIL: {k} = {val}')

print('\n' + '=' * 70)
print('ALL DONE — ' + ('✅ All files passed.' if all_ok else '❌ Some files need attention.'))
