"""
Sync lesson03_additional_python_data_types.html to lesson01 format.
Steps: strip forbidden tags → sync style block → add hub-root id → verify hover fix.
"""
import re

BASE = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"
TARGET = f"{BASE}/lesson03_additional_python_data_types.html"
REF    = f"{BASE}/lesson01_what_is_programming.html"

with open(TARGET, encoding="utf-8") as f:
    content = f.read()

with open(REF, encoding="utf-8") as f:
    ref = f.read()

original = content

# ── Step 1: Strip forbidden HTML shell tags ────────────────────────────────

lines = content.splitlines(keepends=True)

# Remove top: everything before first <link rel="preconnect"
first_link = next((i for i, l in enumerate(lines) if '<link rel="preconnect"' in l), None)
if first_link is not None and first_link > 0:
    lines = lines[first_link:]
    print(f"Step 1a: Stripped {first_link} lines from top")
else:
    print("Step 1a: Top already clean")

content = "".join(lines)

# Remove </head> and <body> (and the blank line between them)
if "</head>" in content or "<body>" in content:
    content = re.sub(r'\s*</head>\s*\n\s*<body>\s*\n', "\n", content)
    content = re.sub(r'\s*</head>\s*\n', "\n", content)
    content = re.sub(r'\s*<body>\s*\n', "\n", content)
    print("Step 1b: Stripped </head>/<body>")
else:
    print("Step 1b: No </head>/<body> found")

# Remove end: </body> and </html>
if "</body>" in content or "</html>" in content:
    content = re.sub(r'\s*</body>\s*\n?\s*</html>\s*$', "", content.rstrip())
    content = re.sub(r'\s*</body>\s*$', "", content.rstrip())
    content = re.sub(r'\s*</html>\s*$', "", content.rstrip())
    print("Step 1c: Stripped </body>/</html>")
else:
    print("Step 1c: No </body>/</html> found")

content = content.rstrip()

# ── Step 2: Sync style block from lesson01 ─────────────────────────────────

ref_style_match = re.search(r'<style>.*?</style>', ref, re.DOTALL)
if not ref_style_match:
    print("ERROR: Could not find <style> block in reference file!")
    exit(1)
ref_style = ref_style_match.group(0)

target_style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
if target_style_match:
    old_style = target_style_match.group(0)
    if old_style == ref_style:
        print("Step 2: Style block already matches lesson01 — no change")
    else:
        content = content.replace(old_style, ref_style, 1)
        ref_lines = len(ref_style.splitlines())
        print(f"Step 2: Style block replaced ({ref_lines} lines from lesson01)")
else:
    print("ERROR: Could not find <style> block in target file!")
    exit(1)

# ── Step 3: Add id="hub-root" ──────────────────────────────────────────────

if 'id="hub-root"' in content:
    print('Step 3: id="hub-root" already present — skipped')
else:
    old_div = '<div class="bg-gray-50 min-h-screen">'
    new_div = '<div id="hub-root" class="bg-gray-50 min-h-screen">'
    if old_div in content:
        content = content.replace(old_div, new_div, 1)
        print('Step 3: Added id="hub-root"')
    else:
        print('Step 3: WARNING — could not find outer wrapper div!')

# ── Step 4: White hover fix ────────────────────────────────────────────────

kt_old    = ".obj-card-kt:hover { box-shadow: none; }"
violet_old = ".obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }"
blue_old   = ".obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }"

kt_new    = ".obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }"
violet_new = ".obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }"
blue_new   = ".obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }"

if "background-color: #ffffff" in content and "obj-card-kt:hover" in content:
    print("Step 4: Hover fix already applied — skipped")
else:
    changed = 0
    for old, new in [(kt_old, kt_new), (violet_old, violet_new), (blue_old, blue_new)]:
        if old in content:
            content = content.replace(old, new, 1)
            changed += 1
    print(f"Step 4: Hover fix applied to {changed}/3 rules")

# ── Write file ─────────────────────────────────────────────────────────────

if content != original:
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(content)
    print("\n✅ File written.")
else:
    print("\n✅ File already clean — no changes needed.")

# ── Verification ───────────────────────────────────────────────────────────

print("\n=== VERIFICATION ===")
with open(TARGET, encoding="utf-8") as f:
    final = f.read()
final_lines = final.splitlines()

checks = {
    "Starts with <link rel=\"preconnect\">": final_lines[0].strip().startswith('<link rel="preconnect"'),
    "Ends with </script>":                   final_lines[-1].strip() == "</script>",
    "No <!DOCTYPE":                          "<!DOCTYPE" not in final,
    "No <html":                              "<html" not in final,
    "No <head>":                             "<head>" not in final,
    "No <body>":                             "<body>" not in final,
    "No </body>":                            "</body>" not in final,
    "No </html>":                            "</html>" not in final,
    'id="hub-root" present once':            final.count('id="hub-root"') == 1,
    "Style block line count matches ref":    len(re.search(r'<style>.*?</style>', final, re.DOTALL).group(0).splitlines()) == len(ref_style.splitlines()),
    "obj-card-kt hover has bg-white":        "obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }" in final,
    "obj-card-violet hover has bg-white":    "obj-card-violet:hover" in final and "background-color: #ffffff" in final,
    "obj-card-blue hover has bg-white":      "obj-card-blue:hover" in final and "background-color: #ffffff" in final,
}

all_pass = True
for label, ok in checks.items():
    icon = "✅" if ok else "❌"
    print(f"  {icon} {label}")
    if not ok:
        all_pass = False

print()
if all_pass:
    print("All checks passed — lesson03 is Confluence-ready.")
else:
    print("FAILURES detected — review output above.")
