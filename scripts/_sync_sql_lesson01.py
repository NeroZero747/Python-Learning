"""
Sync lesson01_what_is_sql.html to match lesson01_what_is_programming.html structure.

Steps:
1. Strip forbidden HTML shell tags (DOCTYPE, html, head, meta, title, body, /body, /html)
2. Replace <style>...</style> block with reference lesson01's exact block
3. Add id="hub-root" to outer wrapper div
4. Apply white-hover fix to obj-card-kt/violet/blue
"""

import re
from pathlib import Path

REF = Path("c:/Users/nightwolf/Projects/Python-Learning/pages/mod_02_python_foundations/lesson01_what_is_programming.html")
TARGET = Path("c:/Users/nightwolf/Projects/Python-Learning/pages/mod_06_sql_foundation/lesson01_what_is_sql.html")

# ── Read files ────────────────────────────────────────────────────────────────
ref_html = REF.read_text(encoding="utf-8")
html = TARGET.read_text(encoding="utf-8")

# ── Step 1: Strip HTML shell tags ─────────────────────────────────────────────
# Remove everything before the first <link rel="preconnect"
html = re.sub(
    r'^.*?(?=\s*<link rel="preconnect" href="https://fonts\.googleapis\.com">)',
    '',
    html,
    flags=re.DOTALL
)

# Remove </head> line and blank line + <body> line
html = re.sub(r'\n[ \t]*</head>\n[ \t]*\n[ \t]*<body>', '', html)
html = re.sub(r'\n[ \t]*</head>\n[ \t]*<body>', '', html)
html = re.sub(r'\n[ \t]*</head>', '', html)
html = re.sub(r'\n[ \t]*<body>', '', html)

# Remove trailing </body> and </html>
html = re.sub(r'\n[ \t]*</body>\s*\n[ \t]*</html>\s*$', '', html)
html = re.sub(r'\n[ \t]*</body>\s*$', '', html)
html = re.sub(r'\n[ \t]*</html>\s*$', '', html)

# Strip leading newlines
html = html.lstrip('\n')

# ── Step 2: Replace <style>...</style> block ──────────────────────────────────
ref_style_match = re.search(r'(\s*<style>.*?</style>)', ref_html, re.DOTALL)
if not ref_style_match:
    raise ValueError("Could not find <style> block in reference file")
ref_style = ref_style_match.group(1)

html = re.sub(r'\s*<style>.*?</style>', ref_style, html, count=1, flags=re.DOTALL)

# ── Step 3: Add id="hub-root" ─────────────────────────────────────────────────
if 'id="hub-root"' not in html:
    html = html.replace(
        '<div class="bg-gray-50 min-h-screen">',
        '<div id="hub-root" class="bg-gray-50 min-h-screen">',
        1
    )

# ── Step 4: White-hover fix ───────────────────────────────────────────────────
fixes = [
    (
        '.obj-card-kt:hover { box-shadow: none; }',
        '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }'
    ),
    (
        '.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }',
        '.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }'
    ),
    (
        '.obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }',
        '.obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }'
    ),
]
for old, new in fixes:
    if old in html:
        html = html.replace(old, new, 1)

# ── Strip trailing whitespace / ensure ends with </script> ───────────────────
html = html.rstrip()

# ── Write ─────────────────────────────────────────────────────────────────────
TARGET.write_text(html, encoding="utf-8")

# ── Verification ──────────────────────────────────────────────────────────────
lines = html.split('\n')
print("=== Verification ===")
print(f"First line: {repr(lines[0])}")
print(f"Last line:  {repr(lines[-1])}")
print(f"Has <!DOCTYPE: {'<!DOCTYPE' in html}")
print(f"Has <html:     {'<html' in html}")
print(f"Has <head:     {'<head' in html}")
print(f"Has <body:     {'<body' in html}")
print(f"Has </body:    {'</body>' in html}")
print(f"Has </html:    {'</html>' in html}")
hub_attr = 'id="hub-root"'
print(f"Has id=hub-root: {hub_attr in html}")
hub_count = html.count(hub_attr)
print(f"hub-root count: {hub_count}")

# Count style lines vs reference
ref_style_lines = len(ref_style.split('\n'))
target_style_match = re.search(r'\s*<style>.*?</style>', html, re.DOTALL)
target_style_lines = len(target_style_match.group(0).split('\n')) if target_style_match else 0
print(f"Ref style lines:    {ref_style_lines}")
print(f"Target style lines: {target_style_lines}")
print(f"Style lines match:  {ref_style_lines == target_style_lines}")

# Check white-hover fix
print(f"kt hover has white bg:     {'obj-card-kt:hover { box-shadow: none; background-color: #ffffff' in html}")
print(f"violet hover has white bg: {'obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff' in html}")
print(f"blue hover has white bg:   {'obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff' in html}")
print("\n✅ Sync complete.")
