import re, os

REF_FILE = "pages/track_01_python_foundation/mod_02_programming_foundations/lesson01_what_is_programming.html"
MOD04_DIR = "pages/track_01_python_foundation/mod_04_python_best_practices"
LESSONS = [
    "lesson01_creating_your_own_modules.html",
    "lesson02_project_folder_structure.html",
    "lesson03_introduction_to_git_simple_workflow.html",
    "lesson04_git_in_vs_code.html",
    "lesson05_logging_basics.html",
]

# ── Extract reference style block ─────────────────────────────────────────────
ref_html = open(REF_FILE).read()
ref_style_start = ref_html.index("  <style>")
ref_style_end   = ref_html.index("  </style>", ref_style_start) + len("  </style>")
REF_STYLE = ref_html[ref_style_start:ref_style_end]
REF_STYLE_LINES = REF_STYLE.count('\n') + 1
print(f"Reference style block: {REF_STYLE_LINES} lines\n")

def sync(fname):
    path = os.path.join(MOD04_DIR, fname)
    html = open(path).read()

    # ── Step 1: Strip HTML shell tags ────────────────────────────────────────
    # Strip everything before first <link rel="preconnect"
    link_pos = html.index('<link rel="preconnect"')
    html = html[link_pos:]

    # Strip </head> and <body> lines (with surrounding blank lines)
    html = re.sub(r'\n?</head>\n?', '\n', html)
    html = re.sub(r'\n?<body>\n?', '\n', html)

    # Strip </body> and </html> from the end
    html = re.sub(r'\n?</body>\n?</html>\s*$', '', html)

    # Normalise: no trailing whitespace at end of file
    html = html.rstrip()

    # ── Step 2: Replace style block ──────────────────────────────────────────
    style_start = html.index('<style>')
    # Find opening tag with any leading whitespace
    style_open_match = re.search(r'[ \t]*<style>', html)
    if not style_open_match:
        print(f"  ❌ <style> not found")
        return False
    style_start = style_open_match.start()

    close_tag = '</style>'
    style_end = html.index(close_tag, style_start) + len(close_tag)
    old_style = html[style_start:style_end]
    html = html[:style_start] + REF_STYLE + html[style_end:]

    # ── Step 3: Add id="hub-root" ────────────────────────────────────────────
    if 'id="hub-root"' not in html:
        html = html.replace(
            '<div class="bg-gray-50 min-h-screen">',
            '<div id="hub-root" class="bg-gray-50 min-h-screen">',
            1
        )

    open(path, 'w').write(html)

    # ── Verify ───────────────────────────────────────────────────────────────
    synced = open(path).read()
    file_style_m = re.search(r'[ \t]*<style>.*?</style>', synced, re.DOTALL)
    file_style_lines = file_style_m.group(0).count('\n') + 1 if file_style_m else 0

    checks = [
        ("starts with <link>",            synced.lstrip().startswith('<link rel="preconnect"')),
        ("ends with </script>",           synced.rstrip().endswith('</script>')),
        ("no <!DOCTYPE",                  '<!DOCTYPE' not in synced),
        ("no <html",                      '<html' not in synced),
        ("no <head>",                     '<head>' not in synced),
        ("no <body>",                     '<body>' not in synced),
        ("no </body>",                    '</body>' not in synced),
        ("no </html>",                    '</html>' not in synced),
        ("id=hub-root present once",      synced.count('id="hub-root"') == 1),
        ("style line count matches ref",  file_style_lines == REF_STYLE_LINES),
        ("obj-card-kt white hover",       '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }' in synced),
        ("obj-card-violet white hover",   'obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }' in synced),
        ("obj-card-blue white hover",     'obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }' in synced),
    ]

    fails = [name for name, v in checks if not v]
    if fails:
        print(f"  ❌ {fname}  FAIL: {fails}")
        return False
    else:
        print(f"  ✅ {fname}  (style: {file_style_lines} lines)")
        return True

all_pass = True
for fname in LESSONS:
    ok = sync(fname)
    if not ok:
        all_pass = False

print()
print("All done — all checks passed." if all_pass else "⚠️  Some checks failed.")
