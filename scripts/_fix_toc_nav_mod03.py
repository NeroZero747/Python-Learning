"""
Fix all TOC/nav issues across mod_03 lessons:

1. lesson04: Fix bottom nav Previous/Next hrefs + labels
2. lesson04: Add missing <section id="next-lesson"> preview
3. lesson06: Add missing <section id="next-lesson"> preview
4. lesson08: Fix bottom nav Previous href + Next href/label
5. ALL: Fix hub_home_page path from ../../../ to ../
"""
import re, glob, os

MOD = r"pages/mod_03_python_for_data_analysts"
files = sorted(glob.glob(os.path.join(MOD, "lesson*.html")))

changes = []

# ═══════════════════════════════════════════════════════════════════
# 1. Fix hub_home_page path in ALL files
# ═══════════════════════════════════════════════════════════════════
for fpath in files:
    fname = os.path.basename(fpath)
    content = open(fpath, encoding='utf-8').read()
    if '../../../hub_home_page.html' in content:
        content = content.replace('../../../hub_home_page.html', '../hub_home_page.html')
        open(fpath, 'w', encoding='utf-8').write(content)
        changes.append(f"{fname}: fixed hub path (../../../ -> ../)")

# ═══════════════════════════════════════════════════════════════════
# 2. Fix lesson04 bottom nav
# ═══════════════════════════════════════════════════════════════════
f04 = os.path.join(MOD, "lesson04_transforming_data.html")
content = open(f04, encoding='utf-8').read()

# Fix Previous link
content = content.replace(
    'href="lesson05_filtering_rows.html" class="lesson-nav-link group flex-1 flex items-center gap-4',
    'href="lesson03_selecting_and_filtering_data.html" class="lesson-nav-link group flex-1 flex items-center gap-4'
)
content = content.replace(
    '>Filtering Rows</p>\n      </div>\n    </a>\n\n    <a href="../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center',
    '>Selecting and Filtering Data</p>\n      </div>\n    </a>\n\n    <a href="../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center'
)

# Fix Next link
content = content.replace(
    'href="lesson07_aggregations_group_by.html" class="lesson-nav-link group flex-1 flex items-center justify-end',
    'href="lesson05_aggregations_and_group_by.html" class="lesson-nav-link group flex-1 flex items-center justify-end'
)
content = content.replace(
    '>Aggregations (GROUP BY)</p>', '>Aggregations and Group By</p>'
)

open(f04, 'w', encoding='utf-8').write(content)
changes.append("lesson04: fixed Previous href+label, Next href+label")

# ═══════════════════════════════════════════════════════════════════
# 3. Fix lesson08 bottom nav
# ═══════════════════════════════════════════════════════════════════
f08 = os.path.join(MOD, "lesson08_exporting_data.html")
content = open(f08, encoding='utf-8').read()

# Fix Previous href (label "Handling Missing Data" is correct, href is wrong)
content = content.replace(
    'href="lesson09_handling_missing_data.html"',
    'href="lesson07_handling_missing_data.html"'
)

# Fix Next link — points to wrong module entirely
content = content.replace(
    '<a href="../mod_02_working_with_data_sources/lesson01_reading_csv_files.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">\n      <div class="min-w-0">\n        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>\n        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Reading CSV Files</p>',
    '<a href="lesson09_connecting_to_databases_and_running_sql.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">\n      <div class="min-w-0">\n        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>\n        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Connecting to Databases and Running SQL</p>'
)

open(f08, 'w', encoding='utf-8').write(content)
changes.append("lesson08: fixed Previous href, Next href+label")

# ═══════════════════════════════════════════════════════════════════
# 4. Add missing <section id="next-lesson"> to lesson04
# ═══════════════════════════════════════════════════════════════════
NEXT_LESSON_04 = """
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

      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">5</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 3 &middot; Lesson 5</p>
          <h3 class="text-base font-bold text-gray-800">Aggregations and Group By</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:object-group"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">Grouping Data by Category</p>
      </div>
    </div>

    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-column"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">Computing Group Totals and Averages</p>
      </div>
    </div>

    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:sliders"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">Applying Multiple Aggregations at Once</p>
      </div>
    </div>
        </div>
      </div>

    </div>
  </div>
</section>

"""

content = open(f04, encoding='utf-8').read()
# Insert before the bare bottom nav <section>
# Find the last </section> before the bottom nav
marker = '\n<section>\n  <div class="flex flex-col sm:flex-row gap-3">'
if marker in content and 'id="next-lesson"' not in content:
    content = content.replace(marker, NEXT_LESSON_04 + '<section>\n  <div class="flex flex-col sm:flex-row gap-3">')
    open(f04, 'w', encoding='utf-8').write(content)
    changes.append("lesson04: added <section id='next-lesson'> preview")
else:
    changes.append("lesson04: next-lesson section already exists or marker not found")

# ═══════════════════════════════════════════════════════════════════
# 5. Add missing <section id="next-lesson"> to lesson06
# ═══════════════════════════════════════════════════════════════════
NEXT_LESSON_06 = """
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

      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">7</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 3 &middot; Lesson 7</p>
          <h3 class="text-base font-bold text-gray-800">Handling Missing Data</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:circle-question"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">Detecting Missing Values in a DataFrame</p>
      </div>
    </div>

    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:minus"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">Dropping Rows or Columns with Nulls</p>
      </div>
    </div>

    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:fill"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">Filling Missing Values with Sensible Defaults</p>
      </div>
    </div>
        </div>
      </div>

    </div>
  </div>
</section>

"""

f06 = os.path.join(MOD, "lesson06_joining_and_merging_data.html")
content = open(f06, encoding='utf-8').read()
if marker in content and 'id="next-lesson"' not in content:
    content = content.replace(marker, NEXT_LESSON_06 + '<section>\n  <div class="flex flex-col sm:flex-row gap-3">')
    open(f06, 'w', encoding='utf-8').write(content)
    changes.append("lesson06: added <section id='next-lesson'> preview")
else:
    changes.append("lesson06: next-lesson section already exists or marker not found")


# ═══════════════════════════════════════════════════════════════════
# Summary
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("TOC / Nav Fix Summary")
print("=" * 60)
for c in changes:
    print(f"  ✅ {c}")

# Final verification
print("\n--- Verification ---")
files = sorted(glob.glob(os.path.join(MOD, "lesson*.html")))
fnames = [os.path.basename(f) for f in files]
all_ok = True

for idx, fpath in enumerate(files):
    fname = fnames[idx]
    content = open(fpath, encoding='utf-8').read()
    
    # Check for stale hrefs
    hrefs = re.findall(r'href="(lesson\d+[^"]*\.html)"', content)
    existing = set(fnames)
    stale = [h for h in hrefs if h not in existing]
    if stale:
        print(f"  ❌ {fname}: stale hrefs: {set(stale)}")
        all_ok = False
    
    # Check hub path
    if '../../../hub_home_page.html' in content:
        print(f"  ❌ {fname}: still has ../../../hub_home_page.html")
        all_ok = False
    
    # Check next-lesson section (all except last lesson)
    has_nl = bool(re.search(r'<section[^>]*id="next-lesson"', content))
    if idx < len(fnames) - 1 and not has_nl:
        print(f"  ❌ {fname}: missing <section id='next-lesson'>")
        all_ok = False

if all_ok:
    print("  ✅ All files pass verification!")
