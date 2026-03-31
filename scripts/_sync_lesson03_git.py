import re

TARGET = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01_python_foundation/mod_04_python_best_practices/lesson03_introduction_to_git_simple_workflow.html"
LESSON01 = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01_python_foundation/mod_02_programming_foundations/lesson01_what_is_programming.html"

with open(TARGET, "r", encoding="utf-8") as f:
    target = f.read()

with open(LESSON01, "r", encoding="utf-8") as f:
    ref = f.read()

# ── Step 1: Strip forbidden shell tags ──────────────────────────────────────
target = re.sub(r'<!DOCTYPE html>\n', '', target)
target = re.sub(r'<html[^>]*>\n', '', target)
target = re.sub(r'<head>\n', '', target)
target = re.sub(r'  <meta[^\n]*\n', '', target)
target = re.sub(r'  <title>[^\n]*\n', '', target)
target = re.sub(r'</head>\n', '', target)
target = re.sub(r'<body>\n\n', '\n', target)
target = re.sub(r'<body>\n', '', target)
target = re.sub(r'\n</body>\n</html>\s*$', '', target)
target = re.sub(r'\n</body>\s*$', '', target)
target = re.sub(r'\n</html>\s*$', '', target)
# Remove trailing newline after last </script>
target = target.rstrip('\n')

lines = target.splitlines()
print(f"Step 1 done.")
print(f"  First line: {repr(lines[0])}")
print(f"  Last line:  {repr(lines[-1])}")

# ── Step 2: Replace style block ───────────────────────────────────────────────
ref_style_match = re.search(r'(<style>.*?</style>)', ref, re.DOTALL)
if not ref_style_match:
    print("ERROR: Could not find style block in lesson01")
    exit(1)
ref_style = ref_style_match.group(1)
print(f"\nStep 2: lesson01 style block has {len(ref_style.splitlines())} lines")

target_style_match = re.search(r'<style>.*?</style>', target, re.DOTALL)
if not target_style_match:
    print("ERROR: Could not find style block in target")
    exit(1)
print(f"  Target style block had {len(target_style_match.group().splitlines())} lines")
target = target[:target_style_match.start()] + ref_style + target[target_style_match.end():]
print("  Style block replaced.")

# ── Step 3: Add id="hub-root" ─────────────────────────────────────────────────
if 'id="hub-root"' in target:
    print("\nStep 3 skipped — id=\"hub-root\" already present.")
else:
    target = target.replace(
        '<div class="bg-gray-50 min-h-screen">',
        '<div id="hub-root" class="bg-gray-50 min-h-screen">',
        1
    )
    if 'id="hub-root"' in target:
        print("\nStep 3 done — id=\"hub-root\" added.")
    else:
        print("\nERROR: Could not add id=\"hub-root\" — pattern not found")

# ── Step 4: White-hover fix ───────────────────────────────────────────────────
OLD_HOVER = (
    '    .obj-card-kt:hover { box-shadow: none; }\n'
    '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }\n'
    '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }'
)
NEW_HOVER = (
    '    .obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }\n'
    '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }\n'
    '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }'
)

# Check current state of hover rules
kt_lines = [l for l in target.splitlines() if 'obj-card-kt:hover' in l]
already_fixed = kt_lines and 'background-color: #ffffff' in kt_lines[0]

if already_fixed:
    print("\nStep 4 skipped — white-hover already present.")
elif OLD_HOVER in target:
    target = target.replace(OLD_HOVER, NEW_HOVER, 1)
    print("\nStep 4 done — white-hover fix applied.")
else:
    print("\nStep 4 WARNING: old hover pattern not found. Current state:")
    for line in target.splitlines():
        if 'obj-card-kt:hover' in line or 'obj-card-violet:hover' in line or 'obj-card-blue:hover' in line:
            print(f"  {repr(line)}")

# ── Write output ──────────────────────────────────────────────────────────────
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(target)

# ── Verification ──────────────────────────────────────────────────────────────
print("\n── Verification ──")
lines = target.splitlines()
print(f"  Total lines: {len(lines)}")
print(f"  Starts with: {repr(lines[0])}")
print(f"  Ends with:   {repr(lines[-1])}")
print(f"  id=\"hub-root\" count:  {target.count('id=\"hub-root\"')}")
print(f"  <!DOCTYPE count:      {target.count('<!DOCTYPE')}")
print(f"  <body> count:         {target.count('<body>')}")
print(f"  </body> count:        {target.count('</body>')}")
print(f"  </html> count:        {target.count('</html>')}")

style_match = re.search(r'<style>.*?</style>', target, re.DOTALL)
ref_style_match2 = re.search(r'<style>.*?</style>', ref, re.DOTALL)
print(f"  Style lines — target: {len(style_match.group().splitlines())}, lesson01: {len(ref_style_match2.group().splitlines())}")
print(f"  Style block matches lesson01: {style_match.group() == ref_style_match2.group()}")

for variant in ['obj-card-kt:hover', 'obj-card-violet:hover', 'obj-card-blue:hover']:
    for line in target.splitlines():
        if variant in line:
            has_bg = 'background-color: #ffffff' in line
            print(f"  {variant} has bg-white: {has_bg}  →  {line.strip()}")
