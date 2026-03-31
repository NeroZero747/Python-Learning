import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_03_object_oriented_programming/"
    "lesson03_attributes_methods.html"
)
BODY_FILE = pathlib.Path("scripts/_ce_mod03_l03_body.html")

new_body = BODY_FILE.read_text(encoding="utf-8")
content = TARGET.read_text(encoding="utf-8")

section_pat = re.compile(
    r'(<section id="code-examples">.*?)'
    r'<div class="bg-white px-8 py-7 space-y-6">.*?</div>'
    r'(\s*\n\s*</div>\s*\n</section>)',
    re.DOTALL,
)

match = section_pat.search(content)
if not match:
    print("ERROR: pattern did not match")
    exit(1)

old_len = len(match.group(0))
new_section = match.group(1) + new_body + match.group(2)
result = content[:match.start()] + new_section + content[match.end():]
TARGET.write_text(result, encoding="utf-8")

print(f"OK: Replaced #code-examples body ({old_len} chars -> {len(new_section)} chars)")

checks = [
    ("Store Member Data tab", "Store Member Data", True),
    ("Check Claim Status tab", "Check Claim Status", True),
    ("Multiple Provider Records tab", "Multiple Provider Records", True),
    ("No traffic-light dots", "bg-red-400/80", False),
    ("member_record.py present", "member_record.py", True),
    ("claim_status.py present", "claim_status.py", True),
    ("provider_records.py present", "provider_records.py", True),
    ("3 panels only (no 04 watermark)", ">04<", False),
]
for label, needle, should_exist in checks:
    found = needle in new_section
    ok = found == should_exist
    print(f"{'OK' if ok else 'FAIL'} {label}")
