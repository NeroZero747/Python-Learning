#!/usr/bin/env python3
"""Sync lesson04_lists_dictionaries.html format to match lesson01_what_is_programming.html."""
import re, sys

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/"
L01 = DIR + "lesson01_what_is_programming.html"
L04 = DIR + "lesson04_lists_dictionaries.html"

c01 = open(L01, encoding="utf-8").read()
c04 = open(L04, encoding="utf-8").read()

# ── Audit ──────────────────────────────────────────────────────────────────
lines04 = c04.splitlines()
print("=== FIRST 5 LINES ===")
for i, l in enumerate(lines04[:5]):
    print(f"  {i+1}: {repr(l)}")
print("=== LAST 5 LINES ===")
for i, l in enumerate(lines04[-5:]):
    print(f"  {len(lines04)-4+i}: {repr(l)}")

forbidden = ["<!DOCTYPE", "<html", "<head>", "<body>", "</body>", "</html>"]
for tag in forbidden:
    found = tag.lower() in c04.lower()
    print(f"Has {tag}: {found}")

print(f"has id=\"hub-root\": {'id=\"hub-root\"' in c04}")
print(f"has bare bg-gray-50 div: {'<div class=\"bg-gray-50 min-h-screen\">' in c04}")

style01_m = re.search(r'<style>.*?</style>', c01, re.DOTALL)
style04_m = re.search(r'<style>.*?</style>', c04, re.DOTALL)
print(f"L01 style lines: {len(style01_m.group(0).splitlines()) if style01_m else 'NOT FOUND'}")
print(f"L04 style lines: {len(style04_m.group(0).splitlines()) if style04_m else 'NOT FOUND'}")

for rule in [".obj-card-kt:hover", ".obj-card-violet:hover", ".obj-card-blue:hover"]:
    idx = c04.find(rule)
    if idx >= 0:
        snippet = c04[idx:idx+90].split("\n")[0]
        print(f"{rule}: {repr(snippet)}")

# ── Step 1: strip forbidden shell tags ────────────────────────────────────
SHELL_RE = re.compile(
    r'<!DOCTYPE[^>]*>\s*\n?'
    r'|<html[^>]*>\s*\n?'
    r'|<head>\s*\n?'
    r'|<meta[^>]*/?\s*>\s*\n?'
    r'|<title>.*?</title>\s*\n?'
    r'|</head>\s*\n?'
    r'|<body>\s*\n?'
    r'|</body>\s*\n?'
    r'|</html>\s*\n?',
    re.IGNORECASE | re.DOTALL
)
c04_new = SHELL_RE.sub('', c04)

# trim leading blank lines (keep leading 2-space indent of first link tag)
c04_new = c04_new.lstrip('\n')

# trim trailing whitespace/newlines, ensure ends with </script>
c04_new = c04_new.rstrip()
if not c04_new.endswith('</script>'):
    print("WARNING: file does not end with </script> after stripping — check manually.")

# ── Step 2: replace <style> block with lesson01's ─────────────────────────
if not style01_m:
    print("ERROR: could not find <style> block in lesson01"); sys.exit(1)
if not style04_m:
    print("ERROR: could not find <style> block in lesson04"); sys.exit(1)

style01_block = style01_m.group(0)
c04_new = c04_new[:c04_new.find(style04_m.group(0))] + style01_block + c04_new[c04_new.find(style04_m.group(0)) + len(style04_m.group(0)):]

# ── Step 3: add id="hub-root" if missing ──────────────────────────────────
if 'id="hub-root"' not in c04_new:
    c04_new = c04_new.replace(
        '<div class="bg-gray-50 min-h-screen">',
        '<div id="hub-root" class="bg-gray-50 min-h-screen">',
        1
    )
    print("Step 3: added id=\"hub-root\"")
else:
    print("Step 3: id=\"hub-root\" already present — skipped")

# ── Step 4: white-hover fix on key-takeaway cards ─────────────────────────
fixes = [
    ('.obj-card-kt:hover { box-shadow: none; }',
     '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }'),
    ('.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }',
     '.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }'),
    ('.obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }',
     '.obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }'),
]
for old, new in fixes:
    if old in c04_new:
        c04_new = c04_new.replace(old, new, 1)
        print(f"Step 4: fixed {old[:30]}…")
    elif new in c04_new:
        print(f"Step 4: {old[:30]}… already has background-color — skipped")
    else:
        print(f"Step 4: WARNING — could not find rule: {old[:50]}")

# ── Write ──────────────────────────────────────────────────────────────────
with open(L04, "w", encoding="utf-8") as f:
    f.write(c04_new)
print("\nDone — lesson04 synced.")

# ── Final verification ─────────────────────────────────────────────────────
final = open(L04, encoding="utf-8").read()
final_lines = final.splitlines()
print("\n=== VERIFICATION ===")
print(f"First line: {repr(final_lines[0])}")
print(f"Last line:  {repr(final_lines[-1])}")
for tag in forbidden:
    found = tag.lower() in final.lower()
    print(f"{'FAIL' if found else 'OK  '} — no {tag}")
print(f"{'OK  ' if 'id=\"hub-root\"' in final else 'FAIL'} — id=\"hub-root\" present")
style_final = re.search(r'<style>.*?</style>', final, re.DOTALL)
print(f"{'OK  ' if style_final and len(style_final.group(0).splitlines()) == len(style01_block.splitlines()) else 'FAIL'} — style block line count matches L01 ({len(style01_block.splitlines())} lines)")
for rule in [".obj-card-kt:hover", ".obj-card-violet:hover", ".obj-card-blue:hover"]:
    idx = final.find(rule)
    snippet = final[idx:idx+90].split("\n")[0] if idx >= 0 else ""
    ok = "background-color: #ffffff" in snippet
    print(f"{'OK  ' if ok else 'FAIL'} — {rule} has background-color: #ffffff")
