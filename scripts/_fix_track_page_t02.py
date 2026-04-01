#!/usr/bin/env python3
"""
_fix_track_page_t02.py

Fixes track_01_python_foundation.html to match the actual 2-module filesystem:
  Module 01 = Programming Foundations Part 1 (9 lessons, pink)   → mod_01_programming_foundations_part_1/
  Module 02 = Programming Foundations Part 2 (8 lessons, violet) → mod_02_programming_foundations_part_2/

Changes applied:
  1. Hero stats:  3 Modules → 2,  18 Lessons → 17
  2. Hero + bottom CTA hrefs: mod_02_programming_foundations/ → mod_01_programming_foundations_part_1/
  3. Amber tip: "Module 2" → "Module 1"
  4. Section rename: MODULE 02 → MODULE 01, id + header + title
  5. Learning-path stepper: 3-node → 2-node, milestones 3-col → 2-col
  6. Module 03 + Module 04 → merged Module 02 (8 lessons, violet)
"""

import os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(BASE, "pages", "track_02_python_foundation", "track_01_python_foundation.html")

with open(TARGET, "r", encoding="utf-8") as f:
    html = f.read()

original = html
changes = 0


# ═══════════════════════════════════════════════════════════════════
# 1. Hero: 3 → 2 Modules
# ═══════════════════════════════════════════════════════════════════
old = '>3</p>\n                <p class="text-white/65 text-[10px] font-semibold uppercase tracking-wide leading-none mt-0.5">Modules</p>'
new = '>2</p>\n                <p class="text-white/65 text-[10px] font-semibold uppercase tracking-wide leading-none mt-0.5">Modules</p>'
assert old in html, "Hero modules stat not found"
html = html.replace(old, new, 1)
changes += 1
print("✅ 1. Hero: 3 Modules → 2")


# ═══════════════════════════════════════════════════════════════════
# 2. Hero: 18 → 17 Lessons
# ═══════════════════════════════════════════════════════════════════
old = '>18</p>\n                <p class="text-white/65 text-[10px] font-semibold uppercase tracking-wide leading-none mt-0.5">Lessons</p>'
new = '>17</p>\n                <p class="text-white/65 text-[10px] font-semibold uppercase tracking-wide leading-none mt-0.5">Lessons</p>'
assert old in html, "Hero lessons stat not found"
html = html.replace(old, new, 1)
changes += 1
print("✅ 2. Hero: 18 Lessons → 17")


# ═══════════════════════════════════════════════════════════════════
# 3. All hrefs: mod_02_programming_foundations/ → mod_01_programming_foundations_part_1/
#    (Hero CTA, Module 01 lesson links, Module CTA, Bottom nav)
# ═══════════════════════════════════════════════════════════════════
n = html.count('mod_02_programming_foundations/')
assert n > 0, "No mod_02_programming_foundations/ hrefs found"
html = html.replace('mod_02_programming_foundations/', 'mod_01_programming_foundations_part_1/')
changes += 1
print(f"✅ 3. Replaced {n} href(s): mod_02_programming_foundations/ → mod_01_programming_foundations_part_1/")


# ═══════════════════════════════════════════════════════════════════
# 4. Amber tip: Module 2 → Module 1
# ═══════════════════════════════════════════════════════════════════
old = 'before beginning Module 2.'
new = 'before beginning Module 1.'
assert old in html, "Amber tip text not found"
html = html.replace(old, new, 1)
changes += 1
print("✅ 4. Amber tip: Module 2 → Module 1")


# ═══════════════════════════════════════════════════════════════════
# 5. Section comment: MODULE 02 → MODULE 01
# ═══════════════════════════════════════════════════════════════════
old = '       MODULE 02 \u2014 PROGRAMMING FOUNDATIONS\n'
new = '       MODULE 01 \u2014 PROGRAMMING FOUNDATIONS PART 1\n'
assert old in html, "MODULE 02 comment not found"
html = html.replace(old, new, 1)
changes += 1
print("✅ 5a. Section comment: MODULE 02 → MODULE 01")

# Section id
old = '<section id="module-02">'
new = '<section id="module-01">'
assert old in html, "id=module-02 not found"
html = html.replace(old, new, 1)
print("✅ 5b. Section id: module-02 → module-01")


# ═══════════════════════════════════════════════════════════════════
# 6. Module header label + title
# ═══════════════════════════════════════════════════════════════════
old = 'Module 02 &middot; 9 Lessons &middot; ~2.5 hours'
new = 'Module 01 &middot; 9 Lessons &middot; ~2.5 hours'
assert old in html, "Module 02 header label not found"
html = html.replace(old, new, 1)

old = '<h2 class="text-xl font-bold text-gray-900 leading-tight">Programming Foundations</h2>'
new = '<h2 class="text-xl font-bold text-gray-900 leading-tight">Programming Foundations Part 1</h2>'
assert old in html, "Module title not found"
html = html.replace(old, new, 1)
changes += 1
print("✅ 6. Module header: 02 → 01, title → Part 1")


# ═══════════════════════════════════════════════════════════════════
# 7. Replace stepper + milestones (3-node → 2-node)
# ═══════════════════════════════════════════════════════════════════
stepper_start_marker = '        <!-- Stepper -->'
# The stepper+milestones block ends right before the bg-white div closing
# sequence:  "\n\n      </div>\n    </div>\n  </section>"
stepper_end_marker = '\n\n      </div>\n    </div>\n  </section>'

stepper_start = html.index(stepper_start_marker)
stepper_end = html.index(stepper_end_marker, stepper_start)

NEW_STEPPER = """        <!-- Stepper -->
        <div class="flex items-center path-row gap-0">

          <div class="path-step">
            <div class="path-node module-icon-pink">01</div>
            <p class="text-xs font-bold text-gray-800 text-center mt-1">Programming<br>Foundations Part 1</p>
            <p class="text-[10px] text-gray-400 text-center mt-0.5">9 lessons</p>
          </div>

          <div class="path-connector"></div>

          <div class="path-step">
            <div class="path-node module-icon-violet">02</div>
            <p class="text-xs font-bold text-gray-800 text-center mt-1">Programming<br>Foundations Part 2</p>
            <p class="text-[10px] text-gray-400 text-center mt-0.5">8 lessons</p>
          </div>

        </div>

        <!-- Milestone labels -->
        <div class="mt-8 grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div class="flex items-start gap-3 rounded-xl bg-[#fdf0f7] border border-pink-100 px-4 py-3.5">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg module-icon-pink shrink-0 mt-0.5">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:terminal"></span>
            </span>
            <div>
              <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">Module 01</p>
              <p class="text-sm font-semibold text-gray-800 mt-0.5">Core Python Syntax</p>
              <p class="text-xs text-gray-500 mt-0.5 leading-relaxed">Variables, data types, control flow, and functions &mdash; the essential tools of every Python program.</p>
            </div>
          </div>
          <div class="flex items-start gap-3 rounded-xl bg-violet-50 border border-violet-100 px-4 py-3.5">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg module-icon-violet shrink-0 mt-0.5">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:cube"></span>
            </span>
            <div>
              <p class="text-xs font-bold text-violet-600 uppercase tracking-wide">Module 02</p>
              <p class="text-sm font-semibold text-gray-800 mt-0.5">OOP, Modules &amp; Best Practices</p>
              <p class="text-xs text-gray-500 mt-0.5 leading-relaxed">Classes, attributes, methods, project structure, Git version control, and logging &mdash; write code like a professional.</p>
            </div>
          </div>
        </div>"""

html = html[:stepper_start] + NEW_STEPPER + html[stepper_end:]
changes += 1
print("✅ 7. Stepper: 3-node → 2-node, milestones 3-col → 2-col")


# ═══════════════════════════════════════════════════════════════════
# 8. Replace Module 03 + Module 04 → new combined Module 02
# ═══════════════════════════════════════════════════════════════════

# Find Module 03 comment start
mod03_marker = '  <!-- \u2550\u2550\u2550'  # start of the box comment
# We need the MODULE 03 comment — search for "MODULE 03"
mod03_comment_start = html.index('MODULE 03')
# Walk back to the start of the comment line (the "  <!-- ═" line before it)
mod03_block_start = html.rfind('  <!-- ', 0, mod03_comment_start)

# Find Module 04 closing </section>
mod04_section_start = html.index('<section id="module-04">')
# The closing </section> is the first one after <section id="module-04">
mod04_section_close = html.index('</section>', mod04_section_start)
mod04_block_end = mod04_section_close + len('</section>')

# Build the new Module 02 section
LESSON_DATA = [
    {
        "num": 1,
        "category": "Introduction",
        "name": "Why Classes Help Data Projects",
        "badge": "Intermediate",
        "time": "10 min",
        "goal": "Understand the problem that classes solve and recognize the analytics scenarios where they are most valuable.",
        "checklist": [
            "What object-oriented programming is and why it exists",
            "Problems that arise with flat, procedural scripts",
            "How classes group related data and behavior together",
            "Real analytics scenarios where classes clean up code",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson01_why_classes_help_data_projects.html",
    },
    {
        "num": 2,
        "category": "OOP",
        "name": "Creating a Class",
        "badge": "Intermediate",
        "time": "15 min",
        "goal": "Define a class with an <code>__init__</code> method and create multiple instances from a single blueprint.",
        "checklist": [
            "The class keyword and naming conventions",
            "The __init__ constructor and what it does",
            "Creating and using instances of a class",
            "What self represents and why it appears everywhere",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson02_creating_a_class.html",
    },
    {
        "num": 3,
        "category": "OOP",
        "name": "Attributes &amp; Methods",
        "badge": "Intermediate",
        "time": "15 min",
        "goal": "Add data and behavior to your classes using attributes and custom methods that operate on that data.",
        "checklist": [
            "Instance attributes vs class attributes",
            "Writing and calling methods on an object",
            "Returning values from methods",
            "Keeping methods focused on a single responsibility",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson03_attributes_methods.html",
    },
    {
        "num": 4,
        "category": "OOP",
        "name": "Refactoring a Script into a Class",
        "badge": "Intermediate",
        "time": "20 min",
        "goal": "Convert a working procedural script into a clean class-based design that is easier to read, test, and reuse.",
        "checklist": [
            "Identifying what data and logic belongs in a class",
            "Moving standalone functions into methods",
            "Testing the refactored class against the original",
            "Benefits of the class approach for readability and reuse",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson04_refactoring_a_script_into_a_class.html",
    },
    {
        "num": 5,
        "category": "Modules",
        "name": "Creating Your Own Modules",
        "badge": "Intermediate",
        "time": "15 min",
        "goal": "Split code across files and import functions from your own modules &mdash; the first step toward writing properly organized projects.",
        "checklist": [
            "What a module is and why splitting code across files matters",
            "Importing functions from your own .py files",
            "__init__.py and how packages work",
            "Avoiding circular imports",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson05_creating_your_own_modules.html",
    },
    {
        "num": 6,
        "category": "Best Practices",
        "name": "Project Folder Structure",
        "badge": "Intermediate",
        "time": "15 min",
        "goal": "Organize scripts, data, and modules into a clean, navigable project layout following the conventions used in production analytics work.",
        "checklist": [
            "A standard analytics project folder layout",
            "modules/, data/raw/, and data/processed/ folders",
            "Why flat project folders become hard to manage",
            "Running scripts reliably from the project root",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson06_project_folder_structure.html",
    },
    {
        "num": 7,
        "category": "Version Control",
        "name": "Introduction to Git (Simple Workflow)",
        "badge": "Intermediate",
        "time": "15 min",
        "goal": "Understand what version control is and run a basic Git workflow &mdash; the professional baseline for every coding project.",
        "checklist": [
            "What Git is and why version control exists",
            "git init, git add, and git commit",
            "Reading the Git status and commit log",
            "Why every coding project should use version control from day one",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson07_introduction_to_git_simple_workflow.html",
    },
    {
        "num": 8,
        "category": "Best Practices",
        "name": "Logging Basics",
        "badge": "Intermediate",
        "time": "15 min",
        "goal": "Add structured logging to your scripts so you can monitor execution, understand what ran, and catch problems before they become incidents.",
        "checklist": [
            "Why print() is not enough for production scripts",
            "The logging module and its five log levels",
            "Writing logs to a file alongside the console",
            "Formatting log messages for readability",
        ],
        "href": "mod_02_programming_foundations_part_2/lesson08_logging_basics.html",
    },
]


def build_lesson_accordion(lesson, is_first=False):
    """Generate one lesson-accordion div for the new Module 02 (violet theme)."""
    active = " active" if is_first else ""
    lines = []
    lines.append(f'          <!-- Lesson {lesson["num"]} -->')
    lines.append(f'          <div class="lesson-accordion mod-violet{active}">')
    lines.append(f'            <div class="accordion-header" onclick="toggleAccordion(this)">')
    lines.append(f'              <div class="lesson-num num-violet">{lesson["num"]}</div>')
    lines.append(f'              <div class="lesson-info">')
    lines.append(f'                <p class="lesson-category">{lesson["category"]}</p>')
    lines.append(f'                <p class="lesson-name">{lesson["name"]}</p>')
    lines.append(f'              </div>')
    lines.append(f'              <span class="lesson-badge">{lesson["badge"]}</span>')
    lines.append(f'              <span class="lesson-time"><span class="iconify" data-icon="fa6-solid:clock" style="font-size:10px;"></span> {lesson["time"]}</span>')
    lines.append(f'              <div class="accordion-chevron"><span class="iconify" data-icon="fa6-solid:chevron-down" style="font-size:12px;"></span></div>')
    lines.append(f'            </div>')
    lines.append(f'            <div class="accordion-body">')
    lines.append(f'              <div class="accordion-body-inner">')
    lines.append(f'                <hr class="accordion-divider">')
    lines.append(f'                <p class="lesson-goal"><strong>Goal:</strong> {lesson["goal"]}</p>')
    lines.append(f'                <ul class="lesson-checklist">')
    for item in lesson["checklist"]:
        lines.append(f'                  <li><span class="iconify" data-icon="fa6-solid:check"></span> {item}</li>')
    lines.append(f'                </ul>')
    lines.append(f'                <a href="{lesson["href"]}" class="start-lesson-btn">')
    lines.append(f'                  Start Lesson <span class="iconify" data-icon="fa6-solid:play" style="font-size:10px;"></span>')
    lines.append(f'                </a>')
    lines.append(f'              </div>')
    lines.append(f'            </div>')
    lines.append(f'          </div>')
    return "\n".join(lines)


# Build all lesson accordions
accordion_blocks = []
for i, lesson in enumerate(LESSON_DATA):
    accordion_blocks.append(build_lesson_accordion(lesson, is_first=(i == 0)))

all_accordions = "\n\n".join(accordion_blocks)

NEW_MODULE_02 = f"""  <!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
       MODULE 02 \u2014 PROGRAMMING FOUNDATIONS PART 2
       \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
  <section id="module-02">
    <div class="module-card">

      <div class="h-1.5 module-bar-violet"></div>

      <div class="flex items-center gap-5 px-7 py-5 border-b border-gray-100">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl module-icon-violet shrink-0">
          <span class="iconify text-white text-lg" data-icon="fa6-solid:cube"></span>
        </span>
        <div class="min-w-0 flex-1">
          <p class="text-xs font-bold uppercase tracking-widest text-violet-600 mb-0.5">Module 02 &middot; 8 Lessons &middot; ~2 hours</p>
          <h2 class="text-xl font-bold text-gray-900 leading-tight">Programming Foundations Part 2</h2>
          <p class="text-sm text-gray-500 mt-1 leading-relaxed">Build on your Python basics with object-oriented programming, custom modules, project structure, Git version control, and logging.</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 shrink-0 hidden sm:flex">
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">
            <span class="iconify text-[9px]" data-icon="fa6-solid:star"></span><span class="iconify text-[9px]" data-icon="fa6-solid:star"></span> Intermediate
          </span>
          <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-[11px] font-semibold bg-gray-100 text-gray-600">
            <span class="iconify text-[9px]" data-icon="fa6-solid:book-open"></span> 8 lessons
          </span>
        </div>
      </div>

      <div class="px-6 py-5">
        <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-3">Lessons in this module</p>
        <div class="space-y-2">

{all_accordions}

        </div>
      </div>

      <div class="flex items-center justify-between px-6 pb-5 gap-4">
        <div class="flex flex-wrap gap-2">
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">classes</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">modules</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">git</span>
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">logging</span>
        </div>
        <a href="mod_02_programming_foundations_part_2/lesson01_why_classes_help_data_projects.html" class="module-cta module-cta-violet shrink-0">
          Start Module <span class="iconify text-[11px]" data-icon="fa6-solid:arrow-right"></span>
        </a>
      </div>

    </div>
  </section>"""

html = html[:mod03_block_start] + NEW_MODULE_02 + html[mod04_block_end:]
changes += 1
print("✅ 8. Replaced Module 03 + Module 04 → new combined Module 02 (8 lessons, violet)")


# ═══════════════════════════════════════════════════════════════════
# WRITE
# ═══════════════════════════════════════════════════════════════════
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n🎉 Done! {changes} change groups applied to track_01_python_foundation.html")
