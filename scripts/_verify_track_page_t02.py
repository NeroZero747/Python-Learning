#!/usr/bin/env python3
"""Verify track_01_python_foundation.html fixes."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(BASE, "pages", "track_02_python_foundation", "track_01_python_foundation.html")

with open(TARGET, "r", encoding="utf-8") as f:
    html = f.read()

# Hero stats
assert ">2</p>" in html and "Modules</p>" in html, "Hero modules FAIL"
assert ">17</p>" in html and "Lessons</p>" in html, "Hero lessons FAIL"
print("OK Hero: 2 Modules, 17 Lessons")

# No old folder refs
assert "mod_02_programming_foundations/" not in html, "Old mod_02_programming_foundations/ refs remain!"
assert "mod_03_object_oriented_programming/" not in html, "Old mod_03 refs remain!"
assert "mod_04_python_best_practices/" not in html, "Old mod_04 refs remain!"
print("OK No old folder references")

# New folder hrefs
mod01_count = html.count("mod_01_programming_foundations_part_1/")
mod02_count = html.count("mod_02_programming_foundations_part_2/")
print(f"OK mod_01 hrefs: {mod01_count}, mod_02 hrefs: {mod02_count}")

# Section IDs
assert 'id="module-01"' in html, "module-01 id missing"
assert 'id="module-02"' in html, "module-02 id missing"
assert 'id="module-03"' not in html, "Old module-03 id still present!"
assert 'id="module-04"' not in html, "Old module-04 id still present!"
print("OK Section IDs: module-01 + module-02 (no module-03/04)")

# Module titles
assert "Programming Foundations Part 1</h2>" in html, "Part 1 title missing"
assert "Programming Foundations Part 2</h2>" in html, "Part 2 title missing"
print("OK Module titles: Part 1 + Part 2")

# Stepper nodes
assert 'module-icon-pink">01</div>' in html, "Stepper node 01 missing"
assert 'module-icon-violet">02</div>' in html, "Stepper node 02 missing"
print("OK Stepper: 2 nodes (01 pink, 02 violet)")

# Module 01 lesson count
mod01_start = html.index('id="module-01"')
mod01_end = html.index("</section>", mod01_start)
mod01_block = html[mod01_start:mod01_end]
mod01_lessons = mod01_block.count("lesson-accordion mod-pink")
print(f"OK Module 01: {mod01_lessons} lesson accordions")

# Module 02 lesson count
mod02_start = html.index('id="module-02"')
mod02_end = html.index("</section>", mod02_start)
mod02_block = html[mod02_start:mod02_end]
mod02_lessons = mod02_block.count("lesson-accordion mod-violet")
print(f"OK Module 02: {mod02_lessons} lesson accordions")

# Amber tip
assert "before beginning Module 1." in html, "Amber tip not updated"
print("OK Amber tip: Module 1")

# Milestones grid
assert "sm:grid-cols-2" in html, "Milestones grid not 2-col"
assert "sm:grid-cols-3" not in html, "Old 3-col milestones grid still present!"
print("OK Milestones: 2-column grid")

# No Git in VS Code lesson
assert "Git in VS Code" not in html, "Removed lesson still present!"
print("OK 'Git in VS Code' lesson removed")

# All 8 mod_02 lesson hrefs
expected = [
    "lesson01_why_classes_help_data_projects.html",
    "lesson02_creating_a_class.html",
    "lesson03_attributes_methods.html",
    "lesson04_refactoring_a_script_into_a_class.html",
    "lesson05_creating_your_own_modules.html",
    "lesson06_project_folder_structure.html",
    "lesson07_introduction_to_git_simple_workflow.html",
    "lesson08_logging_basics.html",
]
for fn in expected:
    full = f"mod_02_programming_foundations_part_2/{fn}"
    assert full in html, f"Missing href: {full}"
print("OK All 8 Module 02 lesson hrefs verified")

print("\nALL CHECKS PASSED")
