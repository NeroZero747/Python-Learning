"""Rewrite the #next-lesson section body and add the bottom nav
for lesson01_creating_your_own_modules.html.

Lesson01 is the FIRST lesson in mod_04 — no Previous link.
Next: lesson02_project_folder_structure.html
"""

import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
)

# ── New #next-lesson body ──────────────────────────────────────────────────────
NEXT_LESSON_BODY = """\
        <!-- Lesson badge -->
        <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
          <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
            <span class="text-white font-bold text-lg">2</span>
          </span>
          <div class="min-w-0">
            <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 4 &middot; Lesson 2</p>
            <h3 class="text-base font-bold text-gray-800">Project Folder Structure</h3>
            <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
          </div>
        </div>

        <!-- 3-card preview grid -->
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
              <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:folder-tree"></span>
              </span>
              <div>
                <p class="text-sm font-semibold text-gray-700">Organising Projects</p>
              </div>
            </div>
            <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
              <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:tag"></span>
              </span>
              <div>
                <p class="text-sm font-semibold text-gray-700">Naming Conventions</p>
              </div>
            </div>
            <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
              <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:layer-group"></span>
              </span>
              <div>
                <p class="text-sm font-semibold text-gray-700">Professional Structure</p>
              </div>
            </div>
          </div>
        </div>
"""

# ── Bottom navigation bar ──────────────────────────────────────────────────────
BOTTOM_NAV = """\

      <!-- Bottom nav — Previous / All Lessons / Next -->
      <section>
        <div class="flex flex-col sm:flex-row gap-3">

          <!-- No Previous link — lesson01 is the first in mod_04 -->
          <div class="flex-1"></div>

          <!-- All Lessons hub link -->
          <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
            <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
            <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
          </a>

          <!-- Next lesson -->
          <a href="lesson02_project_folder_structure.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
            <div class="min-w-0">
              <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
              <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Project Folder Structure</p>
            </div>
            <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
          </a>

        </div>
      </section>
"""

# ── Apply replacements ─────────────────────────────────────────────────────────
html = TARGET.read_text(encoding="utf-8")

# 1. Replace the #next-lesson section body
next_pattern = re.compile(
    r'(<section id="next-lesson">.*?<div class="bg-white px-8 py-7 space-y-[46]">)'
    r'(.*?)'
    r'(</div>\s*</div>\s*</section>)',
    re.DOTALL,
)
m = next_pattern.search(html)
if not m:
    print("❌  #next-lesson pattern not found — aborting.")
    exit(1)

before_next = len(m.group(2))
html = html[: m.start(2)] + "\n" + NEXT_LESSON_BODY + "\n      " + html[m.start(3):]
print(f"✅  #next-lesson body replaced  ({before_next:,} chars → {len(NEXT_LESSON_BODY):,} chars)")

# 2. Insert bottom nav before </main>
# Find the closing </section> (end of #next-lesson) + </main>
nav_pattern = re.compile(r'(</section>)(\s*</main>)', re.DOTALL)
nm = nav_pattern.search(html, html.rfind('<section id="next-lesson">'))
if not nm:
    print("❌  </main> anchor not found — aborting.")
    exit(1)

html = html[: nm.end(1)] + BOTTOM_NAV + html[nm.start(2):]
print(f"✅  Bottom nav inserted")

TARGET.write_text(html, encoding="utf-8")
print(f"   File size: {len(html):,} chars")
