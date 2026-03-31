"""
Replace the entire #code-examples section (header + body) cleanly.
Builds the final section from scratch using the correct header + new body fragment.
"""
import pathlib, re

LESSON = pathlib.Path(
    "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01_python_foundation"
    "/mod_03_object_oriented_programming/lesson03_attributes_methods.html"
)
BODY_FRAG = pathlib.Path(
    "/Users/graywolf/Documents/Project/Python-Learning/scripts/_ce_mod03_l03_v2_body.html"
)

old_html   = LESSON.read_text(encoding="utf-8")
new_body   = BODY_FRAG.read_text(encoding="utf-8").rstrip("\n")

# Build the new section — header is identical to what is already there
SECTION_HEADER = """\
<section id="code-examples">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
  <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
    <span class="iconify text-white text-base" data-icon="fa6-solid:code"></span>
  </span>
  <div class="min-w-0">
    <h2 class="text-xl font-bold text-gray-900 leading-tight">Code Examples</h2>
    <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Hands-on code snippets to explore the concepts</p>
  </div>
</div>\n"""

SECTION_FOOTER = "\n  </div>\n</section>\n"

new_section = SECTION_HEADER + new_body + SECTION_FOOTER

# Locate the old section precisely using depth-counting on the outer wrapper
start_idx = old_html.index('<section id="code-examples">')

# Walk from start_idx to find the matching </section>
depth = 0
i = start_idx
while i < len(old_html):
    if old_html[i:i+8] == '<section':
        depth += 1
        i += 8
    elif old_html[i:i+9] == '</section':
        depth -= 1
        if depth == 0:
            end_idx = old_html.index('>', i) + 1  # include the >
            break
        i += 9
    else:
        i += 1

old_section = old_html[start_idx:end_idx]
print(f"✅  Old section:  {len(old_section):,} chars")
print(f"✅  New section:  {len(new_section):,} chars")

new_html = old_html[:start_idx] + new_section + old_html[end_idx:]
LESSON.write_text(new_html, encoding="utf-8")

# Sanity checks inside the replaced section
section_new = new_html[new_html.index('<section id="code-examples">'):
                       new_html.index('<section id="comparison">')]

checks = [
    ("Store a Product"      in section_new, "tab 1 label present"),
    ("Update a Score"       in section_new, "tab 2 label present"),
    ("List All Books"       in section_new, "tab 3 label present"),
    ("store_product.py"     in section_new, "filename 1 present"),
    ("update_score.py"      in section_new, "filename 2 present"),
    ("list_books.py"        in section_new, "filename 3 present"),
    ("Wireless Mouse"       in section_new, "product output present"),
    ("Fail<br>Pass"         in section_new, "student output present"),
    ("Clean Code"           in section_new, "book output present"),
    ("HealthRecord"     not in section_new, "HealthRecord gone"),
    ("claim_status"     not in section_new, "claim_status gone"),
    ("provider_records" not in section_new, "provider_records gone"),
    ('id="comparison"'      in new_html,    "#comparison still intact"),
    ('id="decision-flow"'   in new_html,    "#decision-flow still intact"),
]
for ok, label in checks:
    print(f"  {'✅' if ok else '❌'}  {label}")

print(f"\n✅  Written  ({len(new_html):,} chars total)")
