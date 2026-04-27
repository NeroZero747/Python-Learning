"""
Clean up all orphaned comparison and real-world content in lesson06.
"""
from pathlib import Path
import re

TARGET = Path(__file__).parent.parent / "pages/mod_05_data_application/lesson06_shiny_for_python.html"
html = TARGET.read_text(encoding="utf-8")
original_len = len(html)

# ─── 1. Remove orphaned comparison body ─────────────────────────────────────
# It starts right after `</section>\n\n` (end of code-examples) with a stray
# `      <div class="rounded-2xl border...>` and ends just before
# `\n<section id="practice">`.
start_marker = '\n</section>\n\n      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">'
end_marker = '\n<section id="practice">'

s = html.find(start_marker)
e = html.find(end_marker, s if s != -1 else 0)
if s != -1 and e != -1:
    removed = len(html[s + len('\n</section>'):e])
    html = html[:s + len('\n</section>')] + '\n' + html[e:]
    print(f"✅ Removed orphaned comparison body ({removed} chars)")
else:
    print(f"⚠️  Comparison orphan start={s}, end={e}")

# ─── 2. Remove orphaned real-world content ───────────────────────────────────
# After the partial replacement, real-world content got wrapped in a fake
# `<section id="recap">` tag. It runs from that fake section tag up to
# (not including) the real `<section id="recap">`.
#
# Pattern: `<section id="recap">\n        <span class="iconify...earth-americas`
# — the fake one has `earth-americas` immediately after the section opening.
fake_recap_start = '<section id="recap">\n        <span class="iconify'
real_recap_start = '\n<section id="recap">\n  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">'

s2 = html.find(fake_recap_start)
e2 = html.find(real_recap_start, s2 if s2 != -1 else 0)
if s2 != -1 and e2 != -1:
    removed2 = len(html[s2:e2])
    html = html[:s2] + html[e2 + 1:]  # +1 to consume the leading \n
    print(f"✅ Removed orphaned real-world body ({removed2} chars)")
else:
    print(f"⚠️  Real-world orphan start={s2}, end={e2}")

# ─── 3. Verify no comparison/real-world content remains ─────────────────────
remaining = []
for check in ['SQL / Excel Comparison', 'Real-World Use', 'Practical applications in real-world']:
    if check in html:
        remaining.append(check)
if remaining:
    print(f"⚠️  Still found: {remaining}")
else:
    print("✅ No comparison/real-world content remaining")

# ─── 4. Check section order ──────────────────────────────────────────────────
sections = re.findall(r'<section id="([^"]+)"', html)
print(f"   Sections: {sections}")

TARGET.write_text(html, encoding="utf-8")
print(f"\nFile: {original_len} → {len(html)} chars (removed {original_len - len(html)} chars)")
