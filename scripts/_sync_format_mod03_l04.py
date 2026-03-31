"""
Sync lesson04_refactoring_a_script_into_a_class.html to match lesson01_what_is_programming.html
structure and CSS. Implements all 4 steps from lesson-sync-format.prompt.md.
"""
import pathlib, re, sys

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_03_object_oriented_programming"
    "/lesson04_refactoring_a_script_into_a_class.html"
)
LESSON01 = pathlib.Path(
    "pages/track_01_python_foundation/mod_02_programming_foundations"
    "/lesson01_what_is_programming.html"
)

html = TARGET.read_text(encoding="utf-8")
ref  = LESSON01.read_text(encoding="utf-8")

# ── Step 1: Strip forbidden HTML shell tags ───────────────────────────────────
# Remove everything from start up to (and including) </head>\n<body>
# Then strip </body> and </html> at the end.

# Strip top shell: <!DOCTYPE ... <body> block
# Find first <link rel="preconnect"
first_link = html.find('  <link rel="preconnect" href="https://fonts.googleapis.com">')
if first_link == -1:
    print("ERROR: cannot find first <link rel=preconnect>")
    sys.exit(1)
html = html[first_link:]
print(f"OK Step 1a: stripped top shell ({first_link} chars removed)")

# Strip </head> + blank line + <body>
html = re.sub(r'\s*</head>\s*\n\s*<body[^>]*>\s*\n?', '\n', html)
print("OK Step 1b: stripped </head>/<body>")

# Strip </body> and </html> at end
html = re.sub(r'\s*</body>\s*\n?\s*</html>\s*$', '', html, flags=re.MULTILINE)
print("OK Step 1c: stripped </body>/</html>")

# ── Step 2: Replace <style> block with lesson01's ────────────────────────────
ref_style_m = re.search(r'(<style>.*?</style>)', ref, re.DOTALL)
if not ref_style_m:
    print("ERROR: cannot find <style> block in lesson01")
    sys.exit(1)
ref_style = ref_style_m.group(1)

target_style_m = re.search(r'<style>.*?</style>', html, re.DOTALL)
if not target_style_m:
    print("ERROR: cannot find <style> block in target")
    sys.exit(1)

html = html[:target_style_m.start()] + ref_style + html[target_style_m.end():]
print(f"OK Step 2: style block replaced ({len(ref_style):,} chars)")

# ── Step 3: Add id="hub-root" to outer wrapper ───────────────────────────────
if 'id="hub-root"' in html:
    print("OK Step 3: id=hub-root already present — skipped")
else:
    old_div = '<div class="bg-gray-50 min-h-screen">'
    new_div = '<div id="hub-root" class="bg-gray-50 min-h-screen">'
    if old_div not in html:
        print("ERROR: cannot find outer wrapper div")
        sys.exit(1)
    html = html.replace(old_div, new_div, 1)
    print("OK Step 3: id=hub-root added to outer wrapper")

# ── Step 4: white-hover fix (already in synced style block — verify) ─────────
if 'background-color: #ffffff' in html:
    print("OK Step 4: background-color:#ffffff already present — no action needed")
else:
    print("WARNING: background-color:#ffffff NOT found — manual fix required")

# ── Write file ────────────────────────────────────────────────────────────────
# Ensure file ends with </script> and no trailing blank lines
html = html.rstrip()
TARGET.write_text(html, encoding="utf-8")
print(f"OK written: {len(html):,} chars")

# ── Verification ──────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding="utf-8")

ref_style_lines = ref_style.count('\n')
tgt_style_m2    = re.search(r'<style>.*?</style>', result, re.DOTALL)
tgt_style_lines = tgt_style_m2.group(0).count('\n') if tgt_style_m2 else -1

checks = [
    (True,  result.startswith('  <link rel="preconnect" href="https://fonts.googleapis.com">'),
             "File starts with first <link rel=preconnect>"),
    (True,  result.rstrip().endswith('</script>'),
             "File ends with </script>"),
    (False, '<!DOCTYPE' in result,                             "No <!DOCTYPE"),
    (False, '<html' in result,                                 "No <html>"),
    (False, '<head>' in result,                                "No <head>"),
    (False, '<body' in result,                                 "No <body>"),
    (False, '</body>' in result,                               "No </body>"),
    (False, '</html>' in result,                               "No </html>"),
    (True,  result.count('id="hub-root"') == 1,               "id=hub-root present exactly once"),
    (True,  tgt_style_lines == ref_style_lines,
             f"Style block line count matches lesson01 ({tgt_style_lines} vs {ref_style_lines})"),
    (True,  '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }' in result,
             ".obj-card-kt:hover has background-color:#ffffff"),
    (True,  'background-color: #ffffff' in result,             ".obj-card-violet/blue:hover has background-color:#ffffff"),
]

print("\n--- Verification ---")
all_pass = True
for expect_true, condition, label in checks:
    ok = condition if expect_true else not condition
    status = "OK  " if ok else "FAIL"
    print(f"  {status}  {label}")
    if not ok:
        all_pass = False

print()
print("All checks passed!" if all_pass else "Some checks FAILED.")
