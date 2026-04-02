"""
Update the track_02 landing page (track_01_python_foundation.html) to reflect
the merged single module structure.

Changes:
  1. Hero CTA href → new merged folder
  2. Module overview: replace 2-card grid with 1-card
  3. Module 01 section: update header, lesson list (add L10-15), footer tags/CTA
  4. Remove entire Module 02 section
  5. All lesson hrefs in Module 01: old folder → new merged folder
"""

import re, os

TRACK_PAGE = r'c:/Users/nightwolf/Projects/Python-Learning/pages/track_02_python_foundation/track_01_python_foundation.html'

with open(TRACK_PAGE, 'r', encoding='utf-8') as f:
    c = f.read()

orig = c  # keep for safety check

# ── 1. All hrefs: old mod folders → new merged folder ────────────────────────
c = c.replace(
    'mod_01_programming_foundations_part_1/',
    'mod_01_python_foundations/'
)
c = c.replace(
    'mod_02_programming_foundations_part_2/',
    'mod_01_python_foundations/'
)

# ── 2. Lesson hrefs inside new folder — old lesson names from mod_02 ─────────
# The old mod_02 accordion items pointed to old filenames (lesson01_why_classes...,
# lesson02_creating_a_class..., etc.) — update to the merged lesson10-15 filenames.
MOD02_RENAMES = {
    'lesson01_why_classes_help_data_projects.html': 'lesson10_introduction_to_classes.html',
    'lesson02_creating_a_class.html':               'lesson10_introduction_to_classes.html',
    'lesson03_attributes_methods.html':             'lesson11_attributes_methods.html',
    'lesson04_refactoring_a_script_into_a_class.html': 'lesson12_refactoring_a_script_into_a_class.html',
    'lesson05_creating_your_own_modules.html':      'lesson13_modules_and_project_structure.html',
    'lesson06_project_folder_structure.html':       'lesson13_modules_and_project_structure.html',
    'lesson07_introduction_to_git_simple_workflow.html': 'lesson14_introduction_to_git_simple_workflow.html',
    'lesson08_logging_basics.html':                 'lesson15_logging_basics.html',
}
for old, new in MOD02_RENAMES.items():
    c = c.replace(old, new)

# ── 3. Module overview subtitle + 2-card grid → single card ──────────────────
OLD_OVERVIEW_HEADER = '''        <div>
          <h2 class="text-xl font-bold text-gray-900 leading-tight">Module Overview</h2>
          <p class="text-sm text-gray-400 leading-snug mt-0.5">Two modules, taken in sequence &mdash; each one builds on the last</p>
        </div>
      </div>
      <div class="bg-white px-8 py-7">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

          <!-- Module 01 summary -->
          <a href="#module-01" class="block rounded-2xl border border-gray-100 overflow-hidden hover:border-[#f5c6e0] hover:shadow-lg transition-all duration-200" style="text-decoration:none;">
            <div class="h-1.5 module-bar-pink"></div>
            <div class="px-5 py-5">
              <div class="flex items-center gap-3 mb-3">
                <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl module-icon-pink shrink-0">
                  <span class="iconify text-white text-base" data-icon="fa6-solid:terminal"></span>
                </span>
                <div>
                  <p class="text-[10px] font-bold uppercase tracking-widest text-[#CB187D]">Module 01</p>
                  <p class="text-sm font-bold text-gray-900">Programming Foundations Part 1</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed mb-3">Variables, data types, control flow, functions, and debugging &mdash; the essential tools of every Python program.</p>
              <div class="flex items-center gap-3">
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">
                  <span class="iconify text-[9px]" data-icon="fa6-solid:book-open"></span> 9 lessons
                </span>
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">
                  <span class="iconify text-[9px]" data-icon="fa6-regular:clock"></span> ~2.5 hours
                </span>
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-gray-100 text-gray-500">
                  <span class="iconify text-[9px]" data-icon="fa6-solid:star"></span> Beginner
                </span>
              </div>
            </div>
          </a>

          <!-- Module 02 summary -->
          <a href="#module-02" class="block rounded-2xl border border-gray-100 overflow-hidden hover:border-violet-200 hover:shadow-lg transition-all duration-200" style="text-decoration:none;">
            <div class="h-1.5 module-bar-violet"></div>
            <div class="px-5 py-5">
              <div class="flex items-center gap-3 mb-3">
                <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl module-icon-violet shrink-0">
                  <span class="iconify text-white text-base" data-icon="fa6-solid:cube"></span>
                </span>
                <div>
                  <p class="text-[10px] font-bold uppercase tracking-widest text-violet-600">Module 02</p>
                  <p class="text-sm font-bold text-gray-900">Programming Foundations Part 2</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed mb-3">Classes, attributes, methods, project structure, Git version control, and logging &mdash; write code like a professional.</p>
              <div class="flex items-center gap-3">
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">
                  <span class="iconify text-[9px]" data-icon="fa6-solid:book-open"></span> 8 lessons
                </span>
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">
                  <span class="iconify text-[9px]" data-icon="fa6-regular:clock"></span> ~2 hours
                </span>
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-gray-100 text-gray-500">
                  <span class="iconify text-[9px]" data-icon="fa6-solid:star"></span> Intermediate
                </span>
              </div>
            </div>
          </a>

        </div>
      </div>'''

NEW_OVERVIEW_HEADER = '''        <div>
          <h2 class="text-xl font-bold text-gray-900 leading-tight">Module Overview</h2>
          <p class="text-sm text-gray-400 leading-snug mt-0.5">One module, 15 lessons &mdash; from your first variable to production-ready scripts</p>
        </div>
      </div>
      <div class="bg-white px-8 py-7">
        <div class="grid grid-cols-1 gap-4">

          <!-- Module 01 summary -->
          <a href="#module-01" class="block rounded-2xl border border-gray-100 overflow-hidden hover:border-[#f5c6e0] hover:shadow-lg transition-all duration-200" style="text-decoration:none;">
            <div class="h-1.5 module-bar-pink"></div>
            <div class="px-5 py-5">
              <div class="flex items-center gap-3 mb-3">
                <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl module-icon-pink shrink-0">
                  <span class="iconify text-white text-base" data-icon="fa6-solid:terminal"></span>
                </span>
                <div>
                  <p class="text-[10px] font-bold uppercase tracking-widest text-[#CB187D]">Module 01</p>
                  <p class="text-sm font-bold text-gray-900">Programming Foundations</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed mb-3">Variables, data types, control flow, functions, debugging, classes, modules, Git, and logging &mdash; everything you need to write clean, professional Python scripts.</p>
              <div class="flex items-center gap-3">
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">
                  <span class="iconify text-[9px]" data-icon="fa6-solid:book-open"></span> 15 lessons
                </span>
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">
                  <span class="iconify text-[9px]" data-icon="fa6-regular:clock"></span> ~4.5 hours
                </span>
                <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-gray-100 text-gray-500">
                  <span class="iconify text-[9px]" data-icon="fa6-solid:star"></span> Beginner–Intermediate
                </span>
              </div>
            </div>
          </a>

        </div>
      </div>'''

if OLD_OVERVIEW_HEADER in c:
    c = c.replace(OLD_OVERVIEW_HEADER, NEW_OVERVIEW_HEADER, 1)
    print('✅ Module overview updated')
else:
    print('⚠  Module overview block not found — check spacing/content')

# ── 4. Module 01 section header ───────────────────────────────────────────────
c = c.replace(
    'Module 01 &middot; 9 Lessons &middot; ~2.5 hours',
    'Module 01 &middot; 15 Lessons &middot; ~4.5 hours'
)
c = c.replace(
    '<h2 class="text-xl font-bold text-gray-900 leading-tight">Programming Foundations Part 1</h2>',
    '<h2 class="text-xl font-bold text-gray-900 leading-tight">Programming Foundations</h2>'
)
c = c.replace(
    '<p class="text-sm text-gray-500 mt-1 leading-relaxed">Master the essential building blocks of Python &mdash; from variables and data types to loops, functions, and reading errors like a pro.</p>',
    '<p class="text-sm text-gray-500 mt-1 leading-relaxed">Master Python from first principles &mdash; variables, data types, loops, functions, classes, modules, version control, and logging.</p>'
)
c = c.replace(
    '<span class="iconify text-[9px]" data-icon="fa6-solid:book-open"></span> 9 lessons\n          </span>',
    '<span class="iconify text-[9px]" data-icon="fa6-solid:book-open"></span> 15 lessons\n          </span>'
)

# ── 5. Lessons 10-15: insert after L9 accordion, before the closing </div></div> ─
NEW_ACCORDION_ITEMS = '''
          <!-- L10 -->
          <div class="lesson-accordion mod-pink">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <div class="lesson-num num-pink">10</div>
              <div class="lesson-info"><p class="lesson-category">OOP</p><p class="lesson-name">Introduction to Classes</p></div>
              <span class="lesson-badge">Intermediate</span>
              <span class="lesson-time"><span class="iconify" data-icon="fa6-solid:clock" style="font-size:10px;"></span> 15 min</span>
              <div class="accordion-chevron"><span class="iconify" data-icon="fa6-solid:chevron-down" style="font-size:12px;"></span></div>
            </div>
            <div class="accordion-body"><div class="accordion-body-inner"><hr class="accordion-divider">
              <p class="lesson-goal"><strong>Goal:</strong> Understand why classes exist, define your first class with <code>__init__</code>, and create objects from a blueprint.</p>
              <ul class="lesson-checklist">
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Why classes exist and what problems they solve</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> The class keyword and the __init__ constructor</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> What self represents and how it works</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Creating multiple objects from one class</li>
              </ul>
              <a href="mod_01_python_foundations/lesson10_introduction_to_classes.html" class="start-lesson-btn">Start Lesson <span class="iconify" data-icon="fa6-solid:play" style="font-size:10px;"></span></a>
            </div></div>
          </div>

          <!-- L11 -->
          <div class="lesson-accordion mod-pink">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <div class="lesson-num num-pink">11</div>
              <div class="lesson-info"><p class="lesson-category">OOP</p><p class="lesson-name">Attributes &amp; Methods</p></div>
              <span class="lesson-badge">Intermediate</span>
              <span class="lesson-time"><span class="iconify" data-icon="fa6-solid:clock" style="font-size:10px;"></span> 15 min</span>
              <div class="accordion-chevron"><span class="iconify" data-icon="fa6-solid:chevron-down" style="font-size:12px;"></span></div>
            </div>
            <div class="accordion-body"><div class="accordion-body-inner"><hr class="accordion-divider">
              <p class="lesson-goal"><strong>Goal:</strong> Add data and behavior to your classes using attributes and custom methods that operate on that data.</p>
              <ul class="lesson-checklist">
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Instance attributes vs class attributes</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Writing and calling methods on an object</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Returning values from methods</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Keeping methods focused on a single responsibility</li>
              </ul>
              <a href="mod_01_python_foundations/lesson11_attributes_methods.html" class="start-lesson-btn">Start Lesson <span class="iconify" data-icon="fa6-solid:play" style="font-size:10px;"></span></a>
            </div></div>
          </div>

          <!-- L12 -->
          <div class="lesson-accordion mod-pink">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <div class="lesson-num num-pink">12</div>
              <div class="lesson-info"><p class="lesson-category">OOP</p><p class="lesson-name">Refactoring a Script into a Class</p></div>
              <span class="lesson-badge">Intermediate</span>
              <span class="lesson-time"><span class="iconify" data-icon="fa6-solid:clock" style="font-size:10px;"></span> 20 min</span>
              <div class="accordion-chevron"><span class="iconify" data-icon="fa6-solid:chevron-down" style="font-size:12px;"></span></div>
            </div>
            <div class="accordion-body"><div class="accordion-body-inner"><hr class="accordion-divider">
              <p class="lesson-goal"><strong>Goal:</strong> Convert a working procedural script into a clean class-based design that is easier to read, test, and reuse.</p>
              <ul class="lesson-checklist">
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Identifying what data and logic belongs in a class</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Moving standalone functions into methods</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Testing the refactored class against the original</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Benefits of the class approach for readability and reuse</li>
              </ul>
              <a href="mod_01_python_foundations/lesson12_refactoring_a_script_into_a_class.html" class="start-lesson-btn">Start Lesson <span class="iconify" data-icon="fa6-solid:play" style="font-size:10px;"></span></a>
            </div></div>
          </div>

          <!-- L13 -->
          <div class="lesson-accordion mod-pink">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <div class="lesson-num num-pink">13</div>
              <div class="lesson-info"><p class="lesson-category">Modules</p><p class="lesson-name">Modules &amp; Project Structure</p></div>
              <span class="lesson-badge">Intermediate</span>
              <span class="lesson-time"><span class="iconify" data-icon="fa6-solid:clock" style="font-size:10px;"></span> 20 min</span>
              <div class="accordion-chevron"><span class="iconify" data-icon="fa6-solid:chevron-down" style="font-size:12px;"></span></div>
            </div>
            <div class="accordion-body"><div class="accordion-body-inner"><hr class="accordion-divider">
              <p class="lesson-goal"><strong>Goal:</strong> Split code across files, import from your own modules, and organize a project folder following real-world analytics conventions.</p>
              <ul class="lesson-checklist">
                <li><span class="iconify" data-icon="fa6-solid:check"></span> What a module is and why splitting code across files matters</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Importing functions from your own .py files</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> A standard analytics project folder layout</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Running scripts reliably from the project root</li>
              </ul>
              <a href="mod_01_python_foundations/lesson13_modules_and_project_structure.html" class="start-lesson-btn">Start Lesson <span class="iconify" data-icon="fa6-solid:play" style="font-size:10px;"></span></a>
            </div></div>
          </div>

          <!-- L14 -->
          <div class="lesson-accordion mod-pink">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <div class="lesson-num num-pink">14</div>
              <div class="lesson-info"><p class="lesson-category">Version Control</p><p class="lesson-name">Introduction to Git (Simple Workflow)</p></div>
              <span class="lesson-badge">Intermediate</span>
              <span class="lesson-time"><span class="iconify" data-icon="fa6-solid:clock" style="font-size:10px;"></span> 15 min</span>
              <div class="accordion-chevron"><span class="iconify" data-icon="fa6-solid:chevron-down" style="font-size:12px;"></span></div>
            </div>
            <div class="accordion-body"><div class="accordion-body-inner"><hr class="accordion-divider">
              <p class="lesson-goal"><strong>Goal:</strong> Understand what version control is and run a basic Git workflow &mdash; the professional baseline for every coding project.</p>
              <ul class="lesson-checklist">
                <li><span class="iconify" data-icon="fa6-solid:check"></span> What Git is and why version control exists</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> git init, git add, and git commit</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Reading the Git status and commit log</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Why every coding project should use version control from day one</li>
              </ul>
              <a href="mod_01_python_foundations/lesson14_introduction_to_git_simple_workflow.html" class="start-lesson-btn">Start Lesson <span class="iconify" data-icon="fa6-solid:play" style="font-size:10px;"></span></a>
            </div></div>
          </div>

          <!-- L15 -->
          <div class="lesson-accordion mod-pink">
            <div class="accordion-header" onclick="toggleAccordion(this)">
              <div class="lesson-num num-pink">15</div>
              <div class="lesson-info"><p class="lesson-category">Best Practices</p><p class="lesson-name">Logging Basics</p></div>
              <span class="lesson-badge">Intermediate</span>
              <span class="lesson-time"><span class="iconify" data-icon="fa6-solid:clock" style="font-size:10px;"></span> 15 min</span>
              <div class="accordion-chevron"><span class="iconify" data-icon="fa6-solid:chevron-down" style="font-size:12px;"></span></div>
            </div>
            <div class="accordion-body"><div class="accordion-body-inner"><hr class="accordion-divider">
              <p class="lesson-goal"><strong>Goal:</strong> Add structured logging to your scripts so you can monitor execution, understand what ran, and catch problems before they become incidents.</p>
              <ul class="lesson-checklist">
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Why print() is not enough for production scripts</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> The logging module and its five log levels</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Writing logs to a file alongside the console</li>
                <li><span class="iconify" data-icon="fa6-solid:check"></span> Formatting log messages for readability</li>
              </ul>
              <a href="mod_01_python_foundations/lesson15_logging_basics.html" class="start-lesson-btn">Start Lesson <span class="iconify" data-icon="fa6-solid:play" style="font-size:10px;"></span></a>
            </div></div>
          </div>'''

# Find the end of the L9 accordion and insert new lessons before the closing </div></div>
INSERT_AFTER = '''          </div>

        </div>
      </div>

      <div class="flex items-center justify-between px-6 pb-5 gap-4">
        <div class="flex flex-wrap gap-2">
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">variables</span>'''

REPLACEMENT_BLOCK = NEW_ACCORDION_ITEMS + '''

        </div>
      </div>

      <div class="flex items-center justify-between px-6 pb-5 gap-4">
        <div class="flex flex-wrap gap-2">
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">variables</span>'''

if INSERT_AFTER in c:
    c = c.replace(INSERT_AFTER, REPLACEMENT_BLOCK, 1)
    print('✅ Lessons 10-15 inserted into Module 01')
else:
    print('⚠  Could not find insertion point for lessons 10-15')

# ── 6. Module 01 footer: add classes/modules/git/logging tags ─────────────────
OLD_M1_FOOTER_TAGS = '''          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">variables</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">loops</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">functions</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">debugging</span>'''

NEW_M1_FOOTER_TAGS = '''          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">variables</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">loops</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">functions</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">classes</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">modules</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">git</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">logging</span>'''

c = c.replace(OLD_M1_FOOTER_TAGS, NEW_M1_FOOTER_TAGS, 1)

# ── 7. Remove entire Module 02 section ────────────────────────────────────────
# The section starts with the comment and ends before the blank lines before </div></div>
MOD02_SECTION_PATTERN = r'\n\n\n  <!-- ={5,}\s*\n\s*MODULE 02.*?</section>\s*\n'
m = re.search(MOD02_SECTION_PATTERN, c, re.DOTALL)
if m:
    c = c[:m.start()] + '\n\n\n' + c[m.end():]
    print('✅ Module 02 section removed')
else:
    print('⚠  Module 02 section pattern not found — trying simpler pattern')
    # Fallback: look for section id="module-02"
    m2 = re.search(r'\n\n\n  <!-- =+\s*\n\s*MODULE 02', c, re.DOTALL)
    if m2:
        # Find the </section> after this point
        end_idx = c.find('</section>', m2.start()) + len('</section>')
        c = c[:m2.start()] + '\n' + c[end_idx:]
        print('✅ Module 02 section removed (fallback)')
    else:
        print('⚠  Module 02 section NOT removed — manual cleanup needed at section id="module-02"')

# ── Write output ──────────────────────────────────────────────────────────────
with open(TRACK_PAGE, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'\n✅ Track landing page updated: {TRACK_PAGE}')
print(f'   Lines before: {orig.count(chr(10))+1} → after: {c.count(chr(10))+1}')
