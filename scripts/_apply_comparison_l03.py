"""
Replace the entire <section id="comparison"> block in lesson03_attributes_methods.html
using section-depth counting (same technique as _apply_ce_l03_v4.py).
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson03_attributes_methods.html")
FRAGMENT = pathlib.Path("scripts/_comparison_l03_body.html")

html = TARGET.read_text(encoding="utf-8")
new_section = FRAGMENT.read_text(encoding="utf-8").rstrip("\n")

MARKER = '<section id="comparison">'
start = html.find(MARKER)
if start == -1:
    print("❌ Could not find <section id=\"comparison\">")
    sys.exit(1)

# Walk forward from MARKER counting section open/close tags to find the matching </section>
pos = start
depth = 0
end = -1
search = html[start:]
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
checks = [
    ("Intro paragraph present",             "If you already store data in a SQL table"),
    ("Row 1 label",                          "store a value"),
    ("Row 2 label",                          "perform an action"),
    ("Row 3 label",                          "one complete record"),
    ("Row 1 Python chip",                    ">attribute<"),
    ("Row 2 Python chip",                    ">method<"),
    ("Row 3 Python chip",                    ">object<"),
    ("Row 1 SQL chip",                       ">column value<"),
    ("Row 2 SQL chip",                       ">stored procedure<"),
    ("Row 1 Excel chip",                     ">cell<"),
    ("Divider label",                        "Same product description, three tools"),
    ("Python code block",                    "product.describe()"),
    ("SQL code block",                       "language-sql"),
    ("Excel code block",                     "language-text"),
    ("Caption starts with All three",        "All three combine a product name"),
    ("Closing amber tip",                    "just bundles them together inside a class"),
    ("No traffic-light dots in comparison",  "w-2.5 h-2.5 rounded-full bg-red-400"),
    ("#practice still intact",              'id="practice"'),
    ("#decision-flow still intact",         'id="decision-flow"'),
]

result = TARGET.read_text(encoding="utf-8")
comp_start = result.find('<section id="comparison">')
comp_end   = result.find('<section id="practice">')
comp_slice = result[comp_start:comp_end] if comp_start != -1 and comp_end != -1 else result

print("\n--- Verification ---")
all_pass = True
for label, token in checks:
    if label.startswith("No traffic"):
        found = token in comp_slice
        ok = not found
        status = "✅" if ok else "❌"
        print(f"  {status} {label} ({'absent ✓' if ok else 'PRESENT — remove traffic dots'})")
    elif label.startswith("#practice") or label.startswith("#decision"):
        ok = token in result
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    else:
        ok = token in comp_slice
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    if not ok:
        all_pass = False

print()
print("✅ All checks passed!" if all_pass else "❌ Some checks failed — review output above.")
