"""Replace the #code-examples body div in lesson03_attributes_methods.html."""
import re, pathlib

LESSON = pathlib.Path(
    "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01_python_foundation"
    "/mod_03_object_oriented_programming/lesson03_attributes_methods.html"
)
BODY = pathlib.Path(
    "/Users/graywolf/Documents/Project/Python-Learning/scripts/_ce_mod03_l03_v2_body.html"
)

old_html = LESSON.read_text(encoding="utf-8")
new_body  = BODY.read_text(encoding="utf-8").rstrip("\n")

# Match the body div inside #code-examples section.
# The body starts with the first <div class="bg-white px-8 py-7 space-y-6"> AFTER the section header.
# We scope the search to within the code-examples section only.

# Find the section boundaries
section_start = old_html.index('<section id="code-examples">')
section_end   = old_html.index('<section id="comparison">', section_start)
section_html  = old_html[section_start:section_end]

# Inside the section, find the body div
body_pattern = re.compile(
    r'(<div class="bg-white px-8 py-7 space-y-6">.*?</div>\s*)',
    re.DOTALL,
)
m = body_pattern.search(section_html)
if not m:
    print("❌  Body div not found inside #code-examples")
    raise SystemExit(1)

old_body = m.group(0)
print(f"✅  Found body div  ({len(old_body):,} chars)")

new_section_html = section_html[:m.start()] + new_body + "\n" + section_html[m.end():]
new_html = old_html[:section_start] + new_section_html + old_html[section_end:]

LESSON.write_text(new_html, encoding="utf-8")

# Quick sanity checks
checks = [
    ("Store a Product"        in new_html, "tab 1 label present"),
    ("Update a Score"         in new_html, "tab 2 label present"),
    ("List All Books"         in new_html, "tab 3 label present"),
    ("store_product.py"       in new_html, "filename 1 present"),
    ("update_score.py"        in new_html, "filename 2 present"),
    ("list_books.py"          in new_html, "filename 3 present"),
    ("Wireless Mouse"         in new_html, "product output present"),
    ("Fail<br>Pass"           in new_html, "student output present"),
    ("Clean Code"             in new_html, "book output present"),
    ('id="comparison"'        in new_html, "#comparison still intact"),
    ("HealthRecord"     not in new_html[new_html.index('<section id="code-examples">'):
                                        new_html.index('<section id="comparison">')],
                                           "HealthRecord gone from section"),
]
for ok, label in checks:
    print(f"  {'✅' if ok else '❌'}  {label}")

print(f"\n✅  Written  ({len(new_html):,} chars total)")
