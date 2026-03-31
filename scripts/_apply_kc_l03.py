"""
Replace the entire <section id="knowledge-check"> block in lesson03_attributes_methods.html
using section-depth counting.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson03_attributes_methods.html")
FRAGMENT = pathlib.Path("scripts/_kc_l03_body.html")

html = TARGET.read_text(encoding="utf-8")
new_section = FRAGMENT.read_text(encoding="utf-8").rstrip("\n")

MARKER = '<section id="knowledge-check">'
start = html.find(MARKER)
if start == -1:
    print("Could not find section id=knowledge-check")
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
    print("Could not find matching close tag")
    sys.exit(1)

old_section = html[start:end]
print(f"OK old section: {len(old_section):,} chars")

new_html = html[:start] + new_section + html[end:]
TARGET.write_text(new_html, encoding="utf-8")
print(f"OK new section: {len(new_section):,} chars")
print(f"OK file total: {len(new_html):,} chars")

result = TARGET.read_text(encoding="utf-8")
kc_start = result.find('<section id="knowledge-check">')
nl_start = result.find('<section id="next-lesson">')
kc_slice = result[kc_start:nl_start] if kc_start != -1 and nl_start != -1 else result

checks = [
    (True,  '<section id="knowledge-check">' in kc_slice,       "Section id=knowledge-check"),
    (True,  'data-icon="fa6-solid:brain"' in kc_slice,          "Header icon brain"),
    (True,  "Knowledge Check" in kc_slice,                       "Header title"),
    (True,  "switchQzTab(0)" in kc_slice,                        "tab 0"),
    (True,  "switchQzTab(1)" in kc_slice,                        "tab 1"),
    (True,  "switchQzTab(2)" in kc_slice,                        "tab 2"),
    (True,  "switchQzTab(3)" in kc_slice,                        "tab 3"),
    (True,  "flex-wrap" in kc_slice,                             "flex-wrap on tab row"),
    (True,  ">Q1<" in kc_slice,                                  "Q1 watermark"),
    (True,  ">Q2<" in kc_slice,                                  "Q2 watermark"),
    (True,  ">Q3<" in kc_slice,                                  "Q3 watermark"),
    (True,  ">Q4<" in kc_slice,                                  "Q4 watermark"),
    (True,  'data-qid="quiz-q0"' in kc_slice,                   "quiz-q0"),
    (True,  'data-qid="quiz-q1"' in kc_slice,                   "quiz-q1"),
    (True,  'data-qid="quiz-q2"' in kc_slice,                   "quiz-q2"),
    (True,  'data-qid="quiz-q3"' in kc_slice,                   "quiz-q3"),
    (True,  "qz-panel qz-panel-anim hidden" in kc_slice,        "hidden panels"),
    (True,  "An attribute is a variable attached" in kc_slice,   "Q1 statement"),
    (True,  "define it outside the class" in kc_slice,           "Q2 statement"),
    (True,  "Coffee Maker product and a Laptop" in kc_slice,     "Q3 statement"),
    (True,  "can only read an object" in kc_slice,               "Q4 statement"),
    (False, "what attributes are &#8212;" in kc_slice,           "No old placeholder text"),
    (True,  'id="recap"' in result,                              "#recap intact"),
    (True,  'id="next-lesson"' in result,                        "#next-lesson intact"),
]

print("\n--- Verification ---")
all_pass = True
for expect_true, condition, label in checks:
    ok = condition if expect_true else not condition
    status = "OK" if ok else "FAIL"
    print(f"  {status}  {label}")
    if not ok:
        all_pass = False

print()
print("All checks passed!" if all_pass else "Some checks FAILED.")
