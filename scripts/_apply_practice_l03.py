"""
Replace the entire <section id="practice"> block in lesson03_attributes_methods.html
using section-depth counting.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson03_attributes_methods.html")
FRAGMENT = pathlib.Path("scripts/_practice_l03_body.html")

html = TARGET.read_text(encoding="utf-8")
new_section = FRAGMENT.read_text(encoding="utf-8").rstrip("\n")

MARKER = '<section id="practice">'
start = html.find(MARKER)
if start == -1:
    print('❌ Could not find <section id="practice">')
    sys.exit(1)

# Walk forward counting section open/close tags to find the matching </section>
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
practice_start = result.find('<section id="practice">')
mistakes_start = result.find('<section id="mistakes">')
practice_slice = result[practice_start:mistakes_start] if practice_start != -1 and mistakes_start != -1 else result

checks = [
    # Tab labels
    ("Tab 1 label: Build a Product",              "Build a Product"),
    ("Tab 2 label: Add a Method",                 "Add a Method"),
    ("Tab 3 label: Create Two Objects",           "Create Two Objects"),
    # No generic Exercise N labels
    ("No 'Exercise 1' label",                     "Exercise 1"),
    # Panel watermarks
    ("Watermark 01 present",                      ">01<"),
    ("Watermark 02 present",                      ">02<"),
    ("Watermark 03 present",                      ">03<"),
    # Domain badges
    ("Domain badge: Products",                    ">Products<"),
    ("Domain badge: Students",                    ">Students<"),
    ("Domain badge: Books",                       ">Books<"),
    # Filenames
    ("Filename: product_info.py",                 "product_info.py"),
    ("Filename: student_result.py",               "student_result.py"),
    ("Filename: book_summary.py",                 "book_summary.py"),
    # Code content
    ("Ex1 code: coffee_maker",                    "coffee_maker"),
    ("Ex2 code: result()",                        "def result(self):"),
    ("Ex3 code: summary()",                       "def summary(self):"),
    # Terminal panes
    ("Terminal pane Ex1",                         "$ python product_info.py"),
    ("Terminal pane Ex2",                         "$ python student_result.py"),
    ("Terminal pane Ex3",                         "$ python book_summary.py"),
    # Terminal output
    ("Output Ex1: Coffee Maker",                  "Coffee Maker"),
    ("Output Ex2: Maria / Pass",                  "Maria"),
    ("Output Ex3: Clean Code",                    "Clean Code by Robert Martin"),
    # No traffic-light dots
    ("No traffic-light dots",                     "w-2.5 h-2.5 rounded-full bg-red-400"),
    # Panels 2 and 3 are hidden
    ("Panel 2 has hidden class",                  'pe-panel pe-panel-anim hidden'),
    # Adjacent sections intact
    ("#comparison still intact",                 'id="comparison"'),
    ("#mistakes still intact",                   'id="mistakes"'),
]

print("\n--- Verification ---")
all_pass = True
for label, token in checks:
    if label.startswith("No traffic") or label.startswith("No 'Exercise"):
        found = token in practice_slice
        ok = not found
        status = "✅" if ok else "❌"
        suffix = "absent ✓" if ok else f"FOUND — must remove"
        print(f"  {status} {label} ({suffix})")
    elif label.startswith("#comparison") or label.startswith("#mistakes"):
        ok = token in result
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    else:
        ok = token in practice_slice
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    if not ok:
        all_pass = False

print()
print("✅ All checks passed!" if all_pass else "❌ Some checks failed — review output above.")
