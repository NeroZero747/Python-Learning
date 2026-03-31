"""
Replace the entire <section id="recap"> block in lesson03_attributes_methods.html
using section-depth counting.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson03_attributes_methods.html")
FRAGMENT = pathlib.Path("scripts/_recap_l03_body.html")

html = TARGET.read_text(encoding="utf-8")
new_section = FRAGMENT.read_text(encoding="utf-8").rstrip("\n")

MARKER = '<section id="recap">'
start = html.find(MARKER)
if start == -1:
    print('❌ Could not find <section id="recap">')
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
recap_start    = result.find('<section id="recap">')
kc_start       = result.find('<section id="knowledge-check">')
recap_slice    = result[recap_start:kc_start] if recap_start != -1 and kc_start != -1 else result

checks = [
    # Section shell preserved
    ("Section id=recap",                    '<section id="recap">'),
    ("Header icon list-check",              'data-icon="fa6-solid:list-check"'),
    ("Header title Lesson Recap",           "Lesson Recap"),
    ("Header subtitle unchanged",           "A quick summary of what you learned"),
    # Card 01
    ("Watermark 01",                        ">01<"),
    ("Card 01 icon database",               'data-icon="fa6-solid:database"'),
    ("Card 01 label exact",                 "What attributes are"),
    ("Card 01 sentence: attributes",        "attributes"),
    ("Card 01 code tag",                    '<code class="font-mono">attributes</code>'),
    # Card 02
    ("Watermark 02",                        ">02<"),
    ("Card 02 icon wrench",                 'data-icon="fa6-solid:wrench"'),
    ("Card 02 label exact",                 "What methods are"),
    ("Card 02 sentence: method code tag",   '<code class="font-mono">method</code>'),
    # Card 03
    ("Watermark 03",                        ">03<"),
    ("Card 03 icon box-archive",            'data-icon="fa6-solid:box-archive"'),
    ("Card 03 label exact",                 "Attributes give objects memory"),
    ("Card 03 sentence: independent copy",  "independent copy"),
    # Card 04
    ("Watermark 04",                        ">04<"),
    ("Card 04 icon gears",                  'data-icon="fa6-solid:gears"'),
    ("Card 04 label exact",                 "Methods act on that data"),
    ("Card 04 sentence: reads or updates",  "reads or updates"),
    # Banner
    ("Completion banner trophy icon",       'data-icon="fa6-solid:trophy"'),
    ("Banner text: 4 key concepts",         "You&#39;ve covered 4 key concepts"),
    ("Banner text: Lesson Complete",        "Lesson Complete!"),
    # No old lowercase fragments
    ("No bare lowercase 'what attributes'", "what attributes are</p>"),
    ("No bare lowercase 'what methods'",    "what methods are</p>"),
    # Adjacent sections intact
    ("#knowledge-check still intact",       'id="knowledge-check"'),
    ("#real-world still intact",             'id="real-world"'),
]

print("\n--- Verification ---")
all_pass = True
for label, token in checks:
    if label.startswith("No bare"):
        ok = token not in recap_slice
        status = "✅" if ok else "❌"
        suffix = "absent ✓" if ok else "FOUND — must remove"
        print(f"  {status} {label} ({suffix})")
    elif label.startswith("#knowledge") or label.startswith("#real-world"):
        ok = token in result
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    else:
        ok = token in recap_slice
        status = "✅" if ok else "❌"
        print(f"  {status} {label}")
    if not ok:
        all_pass = False

print()
print("✅ All checks passed!" if all_pass else "❌ Some checks failed — review output above.")
