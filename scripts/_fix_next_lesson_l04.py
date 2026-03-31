"""
Rewrite the #next-lesson section + bottom nav in lesson04.

Next lesson:  Lesson 5 — Operators (lesson05_operators.html)
Previous:     lesson03_additional_python_data_types.html — Additional Python Data Types
Hub:          ../../../hub_home_page.html
"""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

OLD_BLOCK = '''<section id="next-lesson">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
  <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
    <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
  </span>
  <div class="min-w-0">
    <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
    <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Continue your journey</p>
  </div>
</div>
    <div class="bg-white px-8 py-7 space-y-4"><p class="text-sm text-gray-600 leading-relaxed">Next we will learn:</p>
<p class="text-sm text-gray-600 leading-relaxed"><strong>Lesson 5 — Operators</strong></p>
<p class="text-sm text-gray-600 leading-relaxed">You will learn:</p>
<ul class="space-y-2">
  <li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-sm">arithmetic operators</span></li>
  <li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-sm">comparison operators</span></li>
  <li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-sm">logical operators</span></li>
</ul>
<p class="text-sm text-gray-600 leading-relaxed">Operators are essential because they allow Python programs to <strong>perform calculations and evaluate conditions</strong>.</p>
<a href="lesson05_operators.html" class="lesson-nav-link group mt-5 flex items-center gap-4 rounded-xl border border-gray-100 bg-gray-50 px-5 py-4 no-underline hover:border-[#CB187D] transition-colors">
  <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-[#CB187D] shrink-0">
    <span class="iconify text-white text-sm" data-icon="fa6-solid:arrow-right"></span>
  </span>
  <div class="min-w-0">
    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors">Next: Operators</p>
    <p class="text-xs text-gray-400">Continue your learning journey</p>
  </div>
  <span class="iconify text-gray-300 text-sm ml-auto shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-right"></span>
</a></div>
  </div>
</section>


        <div class="flex flex-col sm:flex-row gap-3 mt-6"><a href="lesson03_additional_python_data_types.html" class="lesson-nav-link group flex-1 flex items-center gap-3 rounded-xl border border-gray-100 bg-white px-5 py-4 no-underline hover:border-[#CB187D] transition-colors">
  <span class="iconify text-gray-300 text-sm shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-left"></span>
  <div class="min-w-0">
    <p class="text-xs text-gray-400">Previous</p>
    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">Additional Python Data Types</p>
  </div>
</a><a href="lesson05_operators.html" class="lesson-nav-link group flex-1 flex items-center gap-3 rounded-xl border border-gray-100 bg-white px-5 py-4 no-underline hover:border-[#CB187D] transition-colors text-right">
  <div class="min-w-0 ml-auto">
    <p class="text-xs text-gray-400">Next</p>
    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">Operators</p>
  </div>
  <span class="iconify text-gray-300 text-sm shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-right"></span>
</a></div>
      </main>'''

NEW_BLOCK = '''<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
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
          <span class="text-white font-bold text-lg">5</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 2 · Lesson 5</p>
          <h3 class="text-base font-bold text-gray-800">Operators</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <!-- Preview card grid -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:calculator"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Arithmetic Operators &amp; Calculations</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:scale-balanced"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Comparison Operators for Conditions</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:code-branch"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Logical Operators to Combine Conditions</p>
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
    <a href="lesson03_additional_python_data_types.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Additional Python Data Types</p>
      </div>
    </a>

    <!-- All Lessons hub link -->
    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <!-- Next lesson -->
    <a href="lesson05_operators.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Operators</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>
      </main>'''

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

if OLD_BLOCK not in content:
    print("❌ OLD_BLOCK not found — check whitespace or content")
else:
    new_content = content.replace(OLD_BLOCK, NEW_BLOCK, 1)
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ #next-lesson + bottom nav replaced")

# --- Verify ---
with open(TARGET, 'r', encoding='utf-8') as f:
    c = f.read()

sec_start = c.index('<section id="next-lesson"')
# Find the bottom nav section closing tag (the </main> comes right after)
main_close = c.index('      </main>', sec_start)
section = c[sec_start:main_close]

checks = [
    ("scroll-mt-24 class present",                         'scroll-mt-24' in section),
    ("Section header icon unchanged (circle-arrow-right)", 'data-icon="fa6-solid:circle-arrow-right"' in section),
    ("Header title unchanged (Next Lesson)",               '>Next Lesson<' in section),
    ("Header subtitle updated (Preview of what comes next)", 'Preview of what comes next' in section),
    ("Lesson badge — number 5",                            '>5<' in section),
    ("Lesson badge — Module 2 · Lesson 5",                 'Module 2 · Lesson 5' in section),
    ("Lesson badge — title Operators",                     '>Operators<' in section),
    ("'What You Will Learn' label",                        'What You Will Learn' in section),
    ("Card 1 — calculator icon",                           'data-icon="fa6-solid:calculator"' in section),
    ("Card 1 — Arithmetic Operators text",                 'Arithmetic Operators' in section),
    ("Card 1 — &amp; used for ampersand",                  '&amp;' in section),
    ("Card 2 — scale-balanced icon",                       'data-icon="fa6-solid:scale-balanced"' in section),
    ("Card 2 — Comparison Operators text",                 'Comparison Operators' in section),
    ("Card 3 — code-branch icon",                          'data-icon="fa6-solid:code-branch"' in section),
    ("Card 3 — Logical Operators text",                    'Logical Operators' in section),
    ("3 obj-card divs in grid",                            section.count('class="obj-card') >= 3),
    ("Bottom nav — Previous link present",                 'lesson03_additional_python_data_types.html' in section),
    ("Bottom nav — Previous display title",                'Additional Python Data Types' in section),
    ("Bottom nav — All Lessons link (hub)",                'hub_home_page.html' in section),
    ("Bottom nav — table-cells-large icon",                'data-icon="fa6-solid:table-cells-large"' in section),
    ("Bottom nav — Next link (lesson05)",                  'lesson05_operators.html' in section),
    ("Bottom nav — arrow-left icon",                       'data-icon="fa6-solid:arrow-left"' in section),
    ("Bottom nav — arrow-right icon",                      'data-icon="fa6-solid:arrow-right"' in section),
    ("No old chevron-right icons in bottom nav",           'chevron-right' not in section),
    ("No old chevron-left icons in bottom nav",            'chevron-left' not in section),
    ("No old 'Continue your journey' subtitle",            'Continue your journey' not in section),
    ("No old inline Next: Operators link",                 'Next: Operators' not in section),
]

all_pass = True
for label, result in checks:
    status = "YES" if result else "NO "
    if not result:
        all_pass = False
    print(f"  {status}: {label}")

print()
print("All checks passed!" if all_pass else "Some checks FAILED — review above.")
