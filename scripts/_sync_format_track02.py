"""
Sync all track_02 lesson HTML files to match the CSS format of lesson01_what_is_programming.html.
Implements the four steps from lesson-sync-format.prompt.md.
"""
import re
import glob
import os

REFERENCE_FILE = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_02_programming_foundations\lesson01_what_is_programming.html'
TARGET_PATTERN = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics\**\*.html'

# ── Extract reference style block ──────────────────────────────────────────
with open(REFERENCE_FILE, encoding='utf-8') as f:
    ref_content = f.read()

style_match = re.search(r'(  <style>.*?  </style>)', ref_content, re.DOTALL)
if not style_match:
    raise RuntimeError('Could not find <style> block in reference file!')
ref_style_block = style_match.group(1)
print(f'Reference style block: {ref_style_block.count(chr(10))+1} lines\n')

# ── Step 4 fix: ensure obj-card hover rules include background-color:white ──
def apply_hover_fix(text):
    text = re.sub(
        r'\.obj-card-kt:hover \{ box-shadow: none; \}',
        '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }',
        text
    )
    text = re.sub(
        r'\.obj-card-violet:hover \{ border-color: #8b5cf6; box-shadow: none; \}',
        '.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }',
        text
    )
    text = re.sub(
        r'\.obj-card-blue:hover \{ border-color: #3b82f6; box-shadow: none; \}',
        '.obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }',
        text
    )
    return text

files = sorted(glob.glob(TARGET_PATTERN, recursive=True))
print(f'Found {len(files)} target files\n')

for filepath in files:
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    original = content
    issues = []

    # ── Step 1: Strip forbidden HTML shell tags ────────────────────────────
    # Remove everything before the first <link rel="preconnect"
    preconnect_marker = '  <link rel="preconnect" href="https://fonts.googleapis.com">'
    idx = content.find(preconnect_marker)
    if idx > 0:
        content = content[idx:]
        issues.append('stripped HTML shell (top)')

    # Remove </head> and <body> lines (with surrounding blank lines)
    content = re.sub(r'\n</head>\n\n<body>\n', '\n', content)
    content = re.sub(r'\n</head>\n<body>\n', '\n', content)
    # Fallback individual removals
    content = re.sub(r'^</head>\n?', '', content, flags=re.MULTILINE)
    content = re.sub(r'^<body>\n?', '', content, flags=re.MULTILINE)

    # Remove </body> and </html> from end
    content = re.sub(r'\n</body>\n?</html>\s*$', '', content)
    content = re.sub(r'\n?</body>\s*$', '', content)
    content = re.sub(r'\n?</html>\s*$', '', content)

    if content != original:
        issues.append('stripped shell tags')

    # ── Step 2: Replace the style block ───────────────────────────────────
    new_content, n_subs = re.subn(
        r'  <style>.*?  </style>',
        ref_style_block,
        content,
        count=1,
        flags=re.DOTALL
    )
    if n_subs:
        content = new_content
        issues.append('replaced style block')
    else:
        issues.append('WARNING: style block not found')

    # ── Step 3: Add id="hub-root" to outer wrapper ────────────────────────
    if 'id="hub-root"' not in content:
        content = content.replace(
            '<div class="bg-gray-50 min-h-screen">',
            '<div id="hub-root" class="bg-gray-50 min-h-screen">',
            1
        )
        issues.append('added id="hub-root"')

    # ── Step 4: Apply key takeaway card hover fix ─────────────────────────
    fixed = apply_hover_fix(content)
    if fixed != content:
        content = fixed
        issues.append('applied hover fix')

    # ── Write file ─────────────────────────────────────────────────────────
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅  {os.path.basename(filepath)} — {", ".join(issues)}')
    else:
        print(f'⚠️   {os.path.basename(filepath)} — no changes needed')

print('\nDone.')

# ── Verification summary ───────────────────────────────────────────────────
print('\n── Verification ──────────────────────────────────────────────────────')
fail = False
for filepath in files:
    with open(filepath, encoding='utf-8') as f:
        c = f.read()
    lines = c.split('\n')
    errs = []
    if not lines[0].startswith('  <link rel="preconnect" href="https://fonts.googleapis.com">'):
        errs.append('does not start with preconnect link')
    if c.rstrip('\n').split('\n')[-1].strip() not in ('</script>', ''):
        # allow blank trailing line
        last_nonempty = [l for l in lines if l.strip()][-1]
        if last_nonempty != '</script>':
            errs.append(f'does not end with </script> (ends: {repr(last_nonempty)})')
    for tag in ['<!DOCTYPE', '<html', '<head>', '<body>', '</body>', '</html>']:
        if tag in c:
            errs.append(f'still contains {tag}')
    if 'id="hub-root"' not in c:
        errs.append('missing id="hub-root"')
    if 'background-color: #ffffff' not in c:
        errs.append('missing hover white-bg fix')
    if errs:
        fail = True
        print(f'❌  {os.path.basename(filepath)}: {"; ".join(errs)}')
    else:
        print(f'✅  {os.path.basename(filepath)}: OK')

if not fail:
    print('\nAll files passed verification.')
