"""
Strip the html/head/body shell from new_lesson_template.html
to match the Confluence-ready format used by all mod_01 lesson files.

Removes:
  <!DOCTYPE html>, <html>, <head>, <meta charset>, <meta viewport>,
  <title>, <meta description>, </head>, <body>, </body>, </html>

Updates the master comment block to remove the <title>/<meta> REPLACE note.
"""

import re

TEMPLATE = "docs/new_lesson_template.html"

with open(TEMPLATE, "r", encoding="utf-8") as f:
    content = f.read()

# ── 1. Update the master comment block: remove <title>/<meta description> line ─
content = content.replace(
    "  ║    • <title> and <meta name=\"description\">                                  ║\n",
    ""
)

# ── 2. Remove <!DOCTYPE html>\n<html lang="en">\n<head>\n ─────────────────────
content = content.replace(
    '<!DOCTYPE html>\n<html lang="en">\n<head>\n',
    ""
)

# ── 3. Remove meta charset + meta viewport + REPLACE comment + <title> + <meta description> ──
# These 5 lines appear together; strip as a block
content = content.replace(
    '  <meta charset="UTF-8">\n'
    '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '  <!-- REPLACE: lesson number + title below -->\n'
    '  <title>Lesson 1 \u2014 What is Python? | Python Learning Hub</title>\n'
    '  <meta name="description" content="Learn What is Python? in Python. Part of the Getting Started module in the Python Learning Hub.">\n'
    '\n'
    '  <!-- Fonts -->\n',
    ""
)

# ── 4. Remove </head>\n<body>\n ─────────────────────────────────────────────────
content = content.replace('</head>\n<body>\n', "")

# ── 5. Remove </body>\n</html> at the end ────────────────────────────────────────
content = content.replace('\n</body>\n</html>', "")

# ── 6. Strip any leading blank line left after removing <head> block ─────────────
# The style block now may have a leading blank line from the removed meta section
# Find the pattern: comment ends → blank line → CDN links start
# Lesson02 format: comment block → CDN links immediately (no blank line between)
content = re.sub(r'(-->\n)\n(<link rel="preconnect")', r'\1\2', content)

with open(TEMPLATE, "w", encoding="utf-8") as f:
    f.write(content)

# Verify
with open(TEMPLATE) as f:
    lines = f.readlines()

checks = {
    "No DOCTYPE":        all("DOCTYPE" not in l for l in lines),
    "No <html>":         all("<html" not in l for l in lines),
    "No <head>":         all(l.strip() not in ("<head>", "</head>") for l in lines),
    "No <body>":         all(l.strip() not in ("<body>", "</body>") for l in lines),
    "No </html>":        all("</html>" not in l for l in lines),
    "CDN links present": any("fonts.googleapis.com" in l for l in lines),
    "Style block kept":  any("<style>" in l for l in lines),
    "Hub-root kept":     any('id="hub-root"' in l for l in lines),
}

print(f"Lines: {len(lines)}")
for label, ok in checks.items():
    print(f"  {'✅' if ok else '❌'} {label}")
