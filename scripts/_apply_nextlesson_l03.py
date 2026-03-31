"""
Replace <section id="next-lesson"> and the old bottom nav in lesson03_attributes_methods.html.
Two replacements:
  1. #next-lesson section via section-depth counting
  2. Old <div> bottom nav replaced with new <section> bottom nav
"""
import pathlib, sys

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_03_object_oriented_programming"
    "/lesson03_attributes_methods.html"
)
FRAGMENT = pathlib.Path("scripts/_nextlesson_l03_body.html")

html = TARGET.read_text(encoding="utf-8")
new_section = FRAGMENT.read_text(encoding="utf-8").rstrip("\n")

# ── Step 1: replace #next-lesson section ────────────────────────────────────
MARKER = '<section id="next-lesson">'
start = html.find(MARKER)
if start == -1:
    print("ERROR: could not find <section id=\"next-lesson\">")
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
    print("ERROR: could not find matching </section>")
    sys.exit(1)

old_section_text = html[start:end]
print(f"OK #next-lesson old: {len(old_section_text):,} chars")
html = html[:start] + new_section + html[end:]
print(f"OK #next-lesson new: {len(new_section):,} chars")

# ── Step 2: replace old <div> bottom nav with new <section> bottom nav ───────
OLD_NAV = (
    '        <div class="flex flex-col sm:flex-row gap-3 mt-6">'
    '<a href="lesson02_creating_a_class.html" class="lesson-nav-link group flex-1 flex items-center gap-3 rounded-xl border border-gray-100 bg-white px-5 py-4 no-underline hover:border-[#CB187D] transition-colors">\n'
    '  <span class="iconify text-gray-300 text-sm shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-left"></span>\n'
    '  <div class="min-w-0">\n'
    '    <p class="text-xs text-gray-400">Previous</p>\n'
    '    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">Creating a Class</p>\n'
    '  </div>\n'
    '</a><a href="lesson04_refactoring_a_script_into_a_class.html" class="lesson-nav-link group flex-1 flex items-center gap-3 rounded-xl border border-gray-100 bg-white px-5 py-4 no-underline hover:border-[#CB187D] transition-colors text-right">\n'
    '  <div class="min-w-0 ml-auto">\n'
    '    <p class="text-xs text-gray-400">Next</p>\n'
    '    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">Refactoring a Script into a Class</p>\n'
    '  </div>\n'
    '  <span class="iconify text-gray-300 text-sm shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-right"></span>\n'
    '</a></div>'
)

NEW_NAV = """<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <a href="lesson02_creating_a_class.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Creating a Class</p>
      </div>
    </a>

    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <a href="lesson04_refactoring_a_script_into_a_class.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Refactoring a Script into a Class</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>"""

if OLD_NAV not in html:
    print("ERROR: could not find old bottom nav div")
    sys.exit(1)

html = html.replace(OLD_NAV, NEW_NAV, 1)
print("OK bottom nav replaced")

TARGET.write_text(html, encoding="utf-8")
print(f"OK file total: {len(html):,} chars")

# ── Verification ─────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding="utf-8")
nl_start   = result.find('<section id="next-lesson"')
script_start = result.find("<script>")
nl_slice   = result[nl_start:script_start] if nl_start != -1 and script_start != -1 else result

checks = [
    (True,  'id="next-lesson"' in nl_slice,                           "section id=next-lesson"),
    (True,  'scroll-mt-24' in nl_slice,                               "scroll-mt-24 class"),
    (True,  'data-icon="fa6-solid:circle-arrow-right"' in nl_slice,  "header icon circle-arrow-right"),
    (True,  "Preview of what comes next" in nl_slice,                 "header subtitle"),
    (True,  "Module 3" in nl_slice,                                   "module number in badge"),
    (True,  ">4<" in nl_slice,                                        "lesson number 4 in badge"),
    (True,  "Refactoring a Script into a Class" in nl_slice,          "next lesson title"),
    (True,  "What You Will Learn" in nl_slice,                        "grid heading"),
    (True,  "fa6-solid:arrows-rotate" in nl_slice,                    "card 1 icon"),
    (True,  "Converting a Script into a Class" in nl_slice,           "card 1 text"),
    (True,  "fa6-solid:sitemap" in nl_slice,                          "card 2 icon"),
    (True,  "Why Refactoring Improves Code Organisation" in nl_slice, "card 2 text"),
    (True,  "fa6-solid:layer-group" in nl_slice,                      "card 3 icon"),
    (True,  "Managing Complex Workflows with OOP" in nl_slice,        "card 3 text"),
    # bottom nav
    (True,  "fa6-solid:arrow-left" in nl_slice,                       "bottom nav: prev arrow-left"),
    (True,  "fa6-solid:table-cells-large" in nl_slice,                "bottom nav: all lessons icon"),
    (True,  "../../../hub_home_page.html" in nl_slice,                "bottom nav: hub path"),
    (True,  "fa6-solid:arrow-right" in nl_slice,                      "bottom nav: next arrow-right"),
    (True,  "All Lessons" in nl_slice,                                "bottom nav: All Lessons text"),
    (True,  'href="lesson02_creating_a_class.html"' in nl_slice,      "bottom nav: prev link"),
    (True,  'href="lesson04_refactoring_a_script_into_a_class.html"' in nl_slice, "bottom nav: next link"),
    # old style gone
    (False, "gap-3 mt-6" in nl_slice,                                 "no old mt-6 nav div"),
    (False, "fa6-solid:chevron-right" in nl_slice,                    "no old chevron-right"),
    (False, "Continue your journey" in nl_slice,                      "no old subtitle"),
    # adjacent sections intact
    (True,  'id="knowledge-check"' in result,                         "#knowledge-check intact"),
    (True,  'id="recap"' in result,                                   "#recap intact"),
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
