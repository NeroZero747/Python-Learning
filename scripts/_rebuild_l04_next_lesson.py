"""
Replace <section id="next-lesson"> plus the old bottom nav in lesson04.
Next: Module 4 · Lesson 2 — Creating Your Own Modules
Bottom nav: ← lesson03 | All Lessons (hub) | → mod_04 lesson02
"""
import pathlib, sys, re

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_NEXT_SECTION = '''<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Lesson badge -->
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">2</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 4 · Lesson 2</p>
          <h3 class="text-base font-bold text-gray-800">Creating Your Own Modules</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <!-- 3-card preview grid -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:file-code"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Writing a module file</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:arrow-right-to-bracket"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Importing your code</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:boxes-stacked"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Reusing across projects</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>

<!-- Bottom nav — Previous / All Lessons / Next -->
<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <!-- Previous lesson -->
    <a href="lesson03_attributes_methods.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Attributes &amp; Methods</p>
      </div>
    </a>

    <!-- All Lessons hub link -->
    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <!-- Next lesson -->
    <a href="../mod_04_python_best_practices/lesson02_creating_your_own_modules.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Creating Your Own Modules</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>'''

html = TARGET.read_text(encoding='utf-8')

# ─── Step 1: replace <section id="next-lesson"> ───────────────────────────────
def replace_section(html, section_id, new_html):
    marker = f'<section id="{section_id}"'
    start = html.find(marker)
    if start == -1:
        print(f'❌ Could not find <section id="{section_id}">'); return html, False
    search = html[start:]
    depth, end, i = 0, -1, 0
    while i < len(search):
        if search[i:].startswith('<section'):
            depth += 1; i += len('<section')
        elif search[i:].startswith('</section>'):
            depth -= 1
            if depth == 0:
                end = start + i + len('</section>'); break
            i += len('</section>')
        else:
            i += 1
    if end == -1:
        print(f'❌ No closing </section> for #{section_id}'); return html, False
    old = html[start:end]
    print(f'  Old #{section_id}: {len(old):,} chars')
    return html[:start] + new_html + html[end:], True

html, ok = replace_section(html, 'next-lesson', NEW_NEXT_SECTION)
if not ok: sys.exit(1)

# ─── Step 2: remove the old bottom nav (a bare <div class="flex..."> block) ──
# The old nav is a bare div between </section> and </main>
# Pattern: find the div block that starts with flex flex-col sm:flex-row and ends before </main>
old_nav_pattern = re.compile(
    r'\s*<div class="flex flex-col sm:flex-row gap-3[^"]*">.*?</div>\s*(?=</main>)',
    re.DOTALL
)
html_after = old_nav_pattern.sub('\n', html, count=1)
if html_after == html:
    print('  ℹ️  Old bare bottom-nav div not found or already removed — skipping')
else:
    print('  ✅ Old bare bottom-nav div removed')
    html = html_after

TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
se_start = result.find('<section id="next-lesson"')
end_main = result.find('</main>', se_start)
s = result[se_start:end_main] if se_start != -1 and end_main != -1 else result

checks = [
    ("scroll-mt-24 on next-lesson",         'class="scroll-mt-24"'),
    ("Icon circle-arrow-right",             'data-icon="fa6-solid:circle-arrow-right"'),
    ("Header: Next Lesson",                 ">Next Lesson<"),
    ("Badge: Module 4 · Lesson 2",          "Module 4 · Lesson 2"),
    ("Badge number: 2",                     ">2<"),
    ("Badge title: Creating Your Own",      "Creating Your Own Modules"),
    ("3 preview cards",                     3),
    ("Card 1: Writing a module file",       "Writing a module file"),
    ("Card 2: Importing your code",         "Importing your code"),
    ("Card 3: Reusing across projects",     "Reusing across projects"),
    ("Bottom nav: Previous link",           "lesson03_attributes_methods.html"),
    ("Bottom nav: Prev label",              "Attributes &amp; Methods"),
    ("Bottom nav: All Lessons link",        "hub_home_page.html"),
    ("Bottom nav: All Lessons text",        ">All Lessons<"),
    ("Bottom nav: Next link",               "lesson02_creating_your_own_modules.html"),
    ("Bottom nav: Next label",              "Creating Your Own Modules"),
    ("arrow-left icon",                     'data-icon="fa6-solid:arrow-left"'),
    ("arrow-right icon",                    'data-icon="fa6-solid:arrow-right"'),
    ("table-cells-large icon",              'data-icon="fa6-solid:table-cells-large"'),
    ("No DataPipeline refs",                True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        ok2 = "DataPipeline" not in s
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        count = s.count('obj-card flex items-center')
        ok3 = count >= needle
        print(f'  {"✅" if ok3 else "❌"} {label} (found {count})')
        if ok3: passed += 1
        else: failed += 1
    elif needle in s:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
