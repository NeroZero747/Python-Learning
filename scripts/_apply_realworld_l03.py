"""
Replace the entire <section id="real-world"> block in lesson03_attributes_methods.html
using section-depth counting.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson03_attributes_methods.html")
FRAGMENT = pathlib.Path("scripts/_realworld_l03_body.html")

html = TARGET.read_text(encoding="utf-8")
new_section = FRAGMENT.read_text(encoding="utf-8").rstrip("\n")

MARKER = '<section id="real-world">'
start = html.find(MARKER)
if start == -1:
    print('❌ Could not find <section id="real-world">')
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
rw_start   = result.find('<section id="real-world">')
recap_start = result.find('<section id="recap">')
rw_slice   = result[rw_start:recap_start] if rw_start != -1 and recap_start != -1 else result

checks = [
    # Subtitle updated
    ("Subtitle text",                         "How classes, attributes, and methods are used"),
    # Intro paragraph
    ("Intro: online product catalogue",       "online product catalogue"),
    ("Intro: no code blocks",                 "<pre"),
    # Cards structural checks
    ("3-col grid present",                    "grid-cols-1 md:grid-cols-3"),
    ("Card 1 violet border",                  "border-violet-100"),
    ("Card 1 icon: box-open",                 "fa6-solid:box-open"),
    ("Card 1 headline: 200 new products",     "200 new products"),
    ("Card 1 returns pill",                   "product object"),
    ("Card 2 pink border",                    "border-pink-100"),
    ("Card 2 icon: tag",                      "fa6-solid:tag"),
    ("Card 2 describe() mentioned",           "describe()"),
    ("Card 2 returns pill",                   "name — $price"),
    ("Card 3 emerald border",                 "border-emerald-100"),
    ("Card 3 icon: magnifying-glass",         "fa6-solid:magnifying-glass"),
    ("Card 3 in_stock mentioned",             "in_stock"),
    ("Card 3 returns pill",                   "True or False"),
    ("arrow-right-from-bracket icon",         "fa6-solid:arrow-right-from-bracket"),
    # Before/after table
    ("Without header: red",                   "Without classes"),
    ("With header: pink",                     "With classes"),
    ("Without row 1: 200 products",           "200 products"),
    ("With row 1: Product bolded",            "<strong class=\"text-gray-700\">Product</strong>"),
    ("With row 2: describe() bolded",         "<strong class=\"text-gray-700\">describe()</strong>"),
    ("With row 3: in_stock bolded",           "<strong class=\"text-gray-700\">in_stock</strong>"),
    ("circle-xmark icon",                     "fa6-solid:circle-xmark"),
    ("circle-check icon",                     "fa6-solid:circle-check"),
    # No code blocks
    ("No code blocks in section",            "<pre"),
    # No traffic-light dots
    ("No traffic-light dots",               "w-2.5 h-2.5 rounded-full bg-red-400"),
    # Adjacent sections intact
    ("#mistakes still intact",              'id="mistakes"'),
    ("#recap still intact",                 'id="recap"'),
]

print("\n--- Verification ---")
all_pass = True
for label, token in checks:
    if label.startswith("Intro: no code") or label.startswith("No code") or label.startswith("No traffic"):
        found = token in rw_slice
        ok = not found
        status = "✅" if ok else "❌"
        suffix = "absent ✓" if ok else "FOUND — must remove"
        print(f"  {status} {label} ({suffix})")
    elif label.startswith("#mistakes") or label.startswith("#recap"):
        ok = token in result
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    else:
        ok = token in rw_slice
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    if not ok:
        all_pass = False

print()
print("✅ All checks passed!" if all_pass else "❌ Some checks failed — review output above.")
