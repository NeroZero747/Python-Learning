"""
Replace the entire <section id="mistakes"> block in lesson03_attributes_methods.html
using section-depth counting.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson03_attributes_methods.html")
FRAGMENT = pathlib.Path("scripts/_mistakes_l03_body.html")

html = TARGET.read_text(encoding="utf-8")
new_section = FRAGMENT.read_text(encoding="utf-8").rstrip("\n")

MARKER = '<section id="mistakes">'
start = html.find(MARKER)
if start == -1:
    print('❌ Could not find <section id="mistakes">')
    sys.exit(1)

search = html[start:]
depth = 0
end = -1
i = 0
while i < len(search):
    if search[i:].startswith("<section"):
        depth += 1
        i += len("<section")
    elif search[i:].startswith("</section"):
        depth -= 1
        if depth == 0:
            end = start + i + len("</section>")
            break
        i += len("</section")
    else:
        i += 1

if end == -1:
    print("❌ Could not find matching </section>")
    sys.exit(1)

old_section = html[start:end]
print(f"✅ Old section found: {len(old_section):,} chars")

new_html = html[:start] + new_section + html[end:]
TARGET.write_text(new_html, encoding="utf-8")
print(f"✅ New section written: {len(new_section):,} chars")
print(f"✅ File written: {len(new_html):,} chars total")

# --- Verification ---
result = TARGET.read_text(encoding="utf-8")
mk_start   = result.find('<section id="mistakes">')
rw_start   = result.find('<section id="real-world">')
mk_slice   = result[mk_start:rw_start] if mk_start != -1 and rw_start != -1 else result

checks = [
    # Tab labels
    ("Tab 1: Missing self",                     "Missing self"),
    ("Tab 2: Skipping self.",                   "Skipping self."),
    ("Tab 3: Wrong Indentation",                "Wrong Indentation"),
    # No generic labels
    ("No 'Mistake 1' label",                    "Mistake 1"),
    # Titles
    ("Title 1: Forgetting self",                "Forgetting self as the First Parameter"),
    ("Title 2: Plain Variable Name",            "Reading a Plain Variable Name Instead"),
    ("Title 3: Method Outside",                 "Defining a Method Outside the Class Body"),
    # Explanation paragraphs
    ("Explanation 1: TypeError",                "TypeError: __init__() takes 0 positional"),
    ("Explanation 2: NameError",                "NameError: name 'name' is not defined"),
    ("Explanation 3: top level",                "starts at the leftmost column"),
    # Split panels
    ("Wrong label 1: self omitted",             "self omitted"),
    ("Wrong label 2: plain variable",           "plain variable"),
    ("Wrong label 3: method outside class",     "method outside class"),
    ("Correct label 1: self first",             "self first"),
    ("Correct label 2: use self.",              "use self."),
    ("Correct label 3: indented inside class",  "indented inside class"),
    # Arrow dividers present (3 of them)
    ("Arrow dividers present",                  "fa6-solid:arrow-right"),
    # Amber tips
    ("Amber tip 1: lightbulb icon",             "fa6-solid:lightbulb"),
    # Panels 2 & 3 hidden
    ("Panel 2 has hidden class",                "mk-panel mk-panel-anim hidden"),
    # Section still correct
    ("#practice still intact",                  'id="practice"'),
    ("#real-world still intact",                'id="real-world"'),
]

print("\n--- Verification ---")
all_pass = True
for label, token in checks:
    if label.startswith("No "):
        found = token in mk_slice
        ok = not found
        status = "✅" if ok else "❌"
        suffix = "absent ✓" if ok else "FOUND — must remove"
        print(f"  {status} {label} ({suffix})")
    elif label.startswith("#practice") or label.startswith("#real-world"):
        ok = token in result
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    else:
        ok = token in mk_slice
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    if not ok:
        all_pass = False

print()
print("✅ All checks passed!" if all_pass else "❌ Some checks failed — review output above.")
