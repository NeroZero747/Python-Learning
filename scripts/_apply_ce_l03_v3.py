"""Replace the #code-examples body div in lesson03_attributes_methods.html.
Uses div-depth counting to find the correct matching closing tag.
"""
import pathlib

LESSON = pathlib.Path(
    "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01_python_foundation"
    "/mod_03_object_oriented_programming/lesson03_attributes_methods.html"
)
BODY = pathlib.Path(
    "/Users/graywolf/Documents/Project/Python-Learning/scripts/_ce_mod03_l03_v2_body.html"
)

old_html = LESSON.read_text(encoding="utf-8")
new_body  = BODY.read_text(encoding="utf-8").rstrip("\n")

# Scope to the code-examples section only
section_start = old_html.index('<section id="code-examples">')
section_end   = old_html.index('<section id="comparison">', section_start)
section_html  = old_html[section_start:section_end]

# Find the body div marker
BODY_MARKER = '<div class="bg-white px-8 py-7 space-y-6">'
marker_pos = section_html.index(BODY_MARKER)

# Walk forward from marker, counting open/close divs to find the matching </div>
depth = 0
i = marker_pos
while i < len(section_html):
    if section_html[i:i+4] == '<div':
        depth += 1
        i += 4
    elif section_html[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            end_pos = i + 6  # include the closing </div>
            break
        i += 6
    else:
        i += 1

old_body = section_html[marker_pos:end_pos]
print(f"✅  Found body div  ({len(old_body):,} chars)")

new_section_html = section_html[:marker_pos] + new_body + "\n" + section_html[end_pos:]
new_html = old_html[:section_start] + new_section_html + old_html[section_end:]

LESSON.write_text(new_html, encoding="utf-8")

# Sanity checks (scope to the section only)
section_new = new_html[new_html.index('<section id="code-examples">'):
                       new_html.index('<section id="comparison">')]

checks = [
    ("Store a Product"    in section_new, "tab 1 label present"),
    ("Update a Score"     in section_new, "tab 2 label present"),
    ("List All Books"     in section_new, "tab 3 label present"),
    ("store_product.py"   in section_new, "filename 1 present"),
    ("update_score.py"    in section_new, "filename 2 present"),
    ("list_books.py"      in section_new, "filename 3 present"),
    ("Wireless Mouse"     in section_new, "product output present"),
    ("Fail<br>Pass"       in section_new, "student output present"),
    ("Clean Code"         in section_new, "book output present"),
    ("HealthRecord"   not in section_new, "HealthRecord gone"),
    ("claim_status"   not in section_new, "claim_status gone"),
    ("provider_records" not in section_new, "provider_records gone"),
    ('id="comparison"'    in new_html,    "#comparison still intact"),
]
for ok, label in checks:
    print(f"  {'✅' if ok else '❌'}  {label}")

print(f"\n✅  Written  ({len(new_html):,} chars total)")
