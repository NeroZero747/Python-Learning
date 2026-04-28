"""
Sync all lesson files under mod_06a_sql_foundation to Confluence format,
matching lesson01_what_is_programming.html structure and CSS exactly.

Steps per file:
1. Strip forbidden HTML shell tags (DOCTYPE, html, head, meta, title, body, /body, /html)
2. Replace <style>...</style> block with reference lesson01's exact block
3. Add id="hub-root" to outer wrapper div
4. Apply white-hover fix to obj-card-kt/violet/blue (if rules exist)
"""

import re
from pathlib import Path

REF = Path("c:/Users/nightwolf/Projects/Python-Learning/pages/mod_02_python_foundations/lesson01_what_is_programming.html")
BASE = Path("c:/Users/nightwolf/Projects/Python-Learning/pages/mod_06a_sql_foundation")

TARGET_FILES = sorted([
    *BASE.glob("mod_05_sql_foundations/lesson*.html"),
    *BASE.glob("mod_06_advanced_sql_for_data_analysis/lesson*.html"),
])

# ── Extract reference style block once ────────────────────────────────────────
ref_html = REF.read_text(encoding="utf-8")
ref_style_match = re.search(r'(\s*<style>.*?</style>)', ref_html, re.DOTALL)
if not ref_style_match:
    raise ValueError("Could not find <style> block in reference file")
ref_style = ref_style_match.group(1)
ref_style_lines = len(ref_style.split('\n'))
print(f"Reference style block: {ref_style_lines} lines\n")

results = []

for fpath in TARGET_FILES:
    html = fpath.read_text(encoding="utf-8")
    steps = []

    # ── Step 1: Strip HTML shell tags ─────────────────────────────────────────
    if '<!DOCTYPE' in html or '<html' in html:
        # Remove everything before the first <link rel="preconnect"
        html = re.sub(
            r'^.*?(?=[ \t]*<link rel="preconnect" href="https://fonts\.googleapis\.com">)',
            '',
            html,
            flags=re.DOTALL
        )
        # Remove </head> + optional blank + <body>
        html = re.sub(r'\n[ \t]*</head>\n[ \t]*\n[ \t]*<body>', '', html)
        html = re.sub(r'\n[ \t]*</head>\n[ \t]*<body>', '', html)
        html = re.sub(r'\n[ \t]*</head>', '', html)
        html = re.sub(r'\n[ \t]*<body>', '', html)
        # Remove trailing </body> and </html>
        html = re.sub(r'\n[ \t]*</body>\s*\n[ \t]*</html>\s*$', '', html)
        html = re.sub(r'\n[ \t]*</body>\s*$', '', html)
        html = re.sub(r'\n[ \t]*</html>\s*$', '', html)
        html = html.lstrip('\n')
        steps.append("stripped shell tags")
    else:
        steps.append("shell tags already absent")

    # ── Step 2: Replace <style> block ─────────────────────────────────────────
    html = re.sub(r'\s*<style>.*?</style>', ref_style, html, count=1, flags=re.DOTALL)
    steps.append("style block replaced")

    # ── Step 3: Add id="hub-root" ─────────────────────────────────────────────
    hub_attr = 'id="hub-root"'
    if hub_attr not in html:
        html = html.replace(
            '<div class="bg-gray-50 min-h-screen">',
            '<div id="hub-root" class="bg-gray-50 min-h-screen">',
            1
        )
        steps.append("hub-root id added")
    else:
        steps.append("hub-root already present")

    # ── Step 4: White-hover fix ───────────────────────────────────────────────
    white_hover_fixes = [
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
    hover_applied = 0
    for old, new in white_hover_fixes:
        if old in html:
            html = html.replace(old, new, 1)
            hover_applied += 1
    if hover_applied:
        steps.append(f"white-hover fix applied ({hover_applied}/3)")
    else:
        steps.append("white-hover rules not present (N/A)")

    # ── Strip trailing whitespace ─────────────────────────────────────────────
    html = html.rstrip()

    # ── Write ─────────────────────────────────────────────────────────────────
    fpath.write_text(html, encoding="utf-8")

    # ── Verify ────────────────────────────────────────────────────────────────
    lines = html.split('\n')
    hub_count = html.count('id="hub-root"')
    target_style_match = re.search(r'\s*<style>.*?</style>', html, re.DOTALL)
    target_style_lines = len(target_style_match.group(0).split('\n')) if target_style_match else 0

    ok = all([
        lines[0].strip().startswith('<link rel="preconnect"'),
        lines[-1].strip() == '</script>',
        '<!DOCTYPE' not in html,
        '<html' not in html,
        '<head' not in html,
        '<body' not in html,
        '</body>' not in html,
        '</html>' not in html,
        hub_count == 1,
        target_style_lines == ref_style_lines,
    ])

    status = "✅" if ok else "❌"
    results.append((status, fpath.name, target_style_lines, hub_count, steps))

# ── Report ────────────────────────────────────────────────────────────────────
print(f"{'Status':<4} {'File':<55} {'Style':>6} {'hub':>4}  Steps")
print("-" * 100)
all_ok = True
for status, name, slines, hcount, steps in results:
    if status == "❌":
        all_ok = False
    print(f"{status}   {name:<55} {slines:>6} {hcount:>4}  {', '.join(steps)}")

print(f"\nRef style lines: {ref_style_lines}")
print(f"\n{'✅ All files synced successfully.' if all_ok else '❌ Some files failed verification — review above.'}")
