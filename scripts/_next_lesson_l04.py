"""
Rewrite #next-lesson section + add bottom navigation bar in lesson04_logging_basics.html.

lesson04 is the last lesson of mod_04. No next lesson exists yet.
- #next-lesson body: module-complete badge + 3 "What you can explore next" cards
- Bottom nav: Previous (lesson03) + All Lessons (hub), no Next link
"""

TARGET = (
    r"c:\Users\nightwolf\Projects\Python-Learning\pages"
    r"\track_01_python_foundation\mod_04_python_best_practices"
    r"\lesson04_logging_basics.html"
)

# ── New #next-lesson section ──────────────────────────────────────────────

NEW_NEXT_LESSON = '''\
<section id="next-lesson" class="scroll-mt-24">
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

      <!-- Module-complete badge -->
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 4 · Complete</p>
          <h3 class="text-base font-bold text-gray-800">Python Best Practices</h3>
          <p class="text-sm text-gray-500 mt-0.5">You've finished the module. Here's what to explore next:</p>
        </div>
      </div>

      <!-- 3-card "What to explore next" grid -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Can Explore Next</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-line"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Track 2: Data Analysis with Python</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:database"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Track 5: SQL Foundations</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:table-cells-large"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">The Hub: All Learning Paths</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>'''

# ── Bottom nav (no Next link — last lesson of module) ─────────────────────

NEW_BOTTOM_NAV = '''\

<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <a href="lesson03_introduction_to_git_simple_workflow.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Introduction to Git (Simple Workflow)</p>
      </div>
    </a>

    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <!-- No Next link — last lesson of module -->
    <div class="flex-1"></div>

  </div>
</section>'''

# ── Read file ──────────────────────────────────────────────────────────────

with open(TARGET, encoding="utf-8") as f:
    html = f.read()

# ── Find #next-lesson section boundaries ──────────────────────────────────

NEXT_START = '<section id="next-lesson">'
END_MARKER = '</main>'

start_idx = html.find(NEXT_START)
main_end_idx = html.find(END_MARKER)

if start_idx == -1:
    print("ERROR: <section id=\"next-lesson\"> not found")
    raise SystemExit(1)

if main_end_idx == -1:
    print("ERROR: </main> not found")
    raise SystemExit(1)

# Extract the fragment from next-lesson start up to (but not incl.) </main>
old_fragment = html[start_idx:main_end_idx]

# Verify it ends with </section> (possibly with whitespace)
stripped = old_fragment.rstrip()
if not stripped.endswith('</section>'):
    print(f"WARNING: fragment does not end cleanly with </section>. Last 80 chars:")
    print(repr(stripped[-80:]))

# Build replacement: new next-lesson + bottom nav + newline before </main>
replacement = NEW_NEXT_LESSON + "\n" + NEW_BOTTOM_NAV + "\n\n      "

new_html = html[:start_idx] + replacement + html[main_end_idx:]

# ── Verify ─────────────────────────────────────────────────────────────────

section_html = NEW_NEXT_LESSON + NEW_BOTTOM_NAV

checks = [
    ("Section id=next-lesson",                   'id="next-lesson"'                          in NEW_NEXT_LESSON),
    ("scroll-mt-24 class present",               'class="scroll-mt-24"'                      in NEW_NEXT_LESSON or 'scroll-mt-24' in NEW_NEXT_LESSON),
    ("Header icon circle-arrow-right",           'data-icon="fa6-solid:circle-arrow-right"'   in NEW_NEXT_LESSON),
    ("Header title Next Lesson",                 ">Next Lesson<"                             in NEW_NEXT_LESSON),
    ("Header subtitle unchanged",                "Preview of what comes next"                in NEW_NEXT_LESSON),
    ("Module 4 Complete badge",                  "Module 4 · Complete"                       in NEW_NEXT_LESSON),
    ("Trophy icon in badge",                     "fa6-solid:trophy"                          in NEW_NEXT_LESSON),
    ("Python Best Practices badge title",        "Python Best Practices"                     in NEW_NEXT_LESSON),
    ("3 preview cards (obj-card)",               NEW_NEXT_LESSON.count('class="obj-card') == 3),
    ("Card 1: Data Analysis track",             "Data Analysis with Python"                  in NEW_NEXT_LESSON),
    ("Card 2: SQL Foundations track",           "SQL Foundations"                            in NEW_NEXT_LESSON),
    ("Card 3: Hub / all learning paths",        "All Learning Paths"                         in NEW_NEXT_LESSON),
    ("What You Can Explore Next label",          "What You Can Explore Next"                 in NEW_NEXT_LESSON),
    ("Body uses space-y-6",                      "space-y-6"                                 in NEW_NEXT_LESSON),
    ("Previous link to lesson03",                "lesson03_introduction_to_git_simple_workflow.html" in NEW_BOTTOM_NAV),
    ("Previous label text",                      "Introduction to Git (Simple Workflow)"     in NEW_BOTTOM_NAV),
    ("All Lessons hub link",                     "../../../hub_home_page.html"               in NEW_BOTTOM_NAV),
    ("All Lessons icon table-cells-large",       "fa6-solid:table-cells-large"               in NEW_BOTTOM_NAV),
    ("No Next arrow link (last lesson)",         "fa6-solid:arrow-right"                     not in NEW_BOTTOM_NAV),
    ("Flex-1 spacer for missing Next slot",      'class="flex-1"'                            in NEW_BOTTOM_NAV),
]

print("Running checks:")
all_ok = True
for label, result in checks:
    status = "OK  " if result else "FAIL"
    print(f"  {status}: {label}")
    if not result:
        all_ok = False

if not all_ok:
    print("\nChecks failed — file NOT written.")
    raise SystemExit(1)

# ── Write ──────────────────────────────────────────────────────────────────

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(new_html)

print("\nSection written successfully.")
print("All checks passed.")
