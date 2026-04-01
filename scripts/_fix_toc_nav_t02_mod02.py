"""
Fix TOC sidebar, #next-lesson, and bottom nav for all 8 lessons in
track_02 / mod_02_programming_foundations_part_2.

The 8 lessons were previously in two separate modules (mod_03 OOP 1-4,
mod_04 Best Practices 1-4) and got combined.  This script:
  1. Replaces the 4-lesson TOC sidebar with the full 8-lesson list.
  2. Fixes module labels from "Module 3"/"Module 4" → "Module 2".
  3. Fixes next-lesson badge numbers and links.
  4. Fixes bottom-nav Previous/Next hrefs.
"""

import re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MOD_DIR = ROOT / "pages" / "track_02_python_foundation" / "mod_02_programming_foundations_part_2"

FILES = [
    MOD_DIR / "lesson01_why_classes_help_data_projects.html",
    MOD_DIR / "lesson02_creating_a_class.html",
    MOD_DIR / "lesson03_attributes_methods.html",
    MOD_DIR / "lesson04_refactoring_a_script_into_a_class.html",
    MOD_DIR / "lesson05_creating_your_own_modules.html",
    MOD_DIR / "lesson06_project_folder_structure.html",
    MOD_DIR / "lesson07_introduction_to_git_simple_workflow.html",
    MOD_DIR / "lesson08_logging_basics.html",
]

LESSONS = [
    ("lesson01_why_classes_help_data_projects.html",   "1. Why Classes Help Data Projects"),
    ("lesson02_creating_a_class.html",                 "2. Creating a Class"),
    ("lesson03_attributes_methods.html",               "3. Attributes &amp; Methods"),
    ("lesson04_refactoring_a_script_into_a_class.html","4. Refactoring a Script into a Class"),
    ("lesson05_creating_your_own_modules.html",        "5. Creating Your Own Modules"),
    ("lesson06_project_folder_structure.html",         "6. Project Folder Structure"),
    ("lesson07_introduction_to_git_simple_workflow.html","7. Introduction to Git (Simple Workflow)"),
    ("lesson08_logging_basics.html",                   "8. Logging Basics"),
]

# ── helpers ──────────────────────────────────────────────────────────

ACTIVE_LINK = (
    '<a href="{href}" class="flex items-center gap-2 px-3 py-2 rounded-lg border '
    'bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span>\n'
    '  <span class="truncate">{label}</span>\n'
    '</a>'
)

INACTIVE_LINK = (
    '<a href="{href}" class="flex items-center gap-2 px-3 py-2 rounded-lg border '
    'bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    '  <span class="truncate">{label}</span>\n'
    '</a>'
)

def build_toc_block(active_index: int) -> str:
    """Build the full 8-lesson TOC sidebar block for a given active lesson."""
    links = []
    for i, (href, label) in enumerate(LESSONS):
        tpl = ACTIVE_LINK if i == active_index else INACTIVE_LINK
        links.append(tpl.format(href=href, label=label))
    return '\n'.join(links)


def replace_toc(html: str, active_index: int) -> str:
    """Replace the old 4-lesson Module Lessons block with the full 8-lesson block."""
    # Pattern: from the <div class="space-y-1"> that wraps lesson links
    # up to (but not including) the closing </div> of that div.
    pattern = re.compile(
        r'(<div class="space-y-1">)'   # opening wrapper div
        r'(.*?)'                          # all lesson links
        r'(\n</div>\s*\n\s*</div>)',      # closing wrappers
        re.DOTALL
    )
    new_block = build_toc_block(active_index)
    replacement = r'\g<1>' + new_block + '\n' + r'</div>\n          </div>'

    result, n = pattern.subn(lambda m: m.group(1) + new_block + '\n</div>\n          </div>', html, count=1)
    return result, n


# ── next-lesson badge fixes ──────────────────────────────────────────

# Mapping: for lesson N, what the next-lesson badge should say
# (badge_number, module_label, next_title)
NEXT_LESSON_INFO = {
    0: ("2", "Module 2 · Lesson 2",  "Creating a Class"),
    1: ("3", "Module 2 · Lesson 3",  "Attributes &amp; Methods"),
    2: ("4", "Module 2 · Lesson 4",  "Refactoring a Script into a Class"),
    3: ("5", "Module 2 · Lesson 5",  "Creating Your Own Modules"),
    4: ("6", "Module 2 · Lesson 6",  "Project Folder Structure"),
    5: ("7", "Module 2 · Lesson 7",  "Introduction to Git (Simple Workflow)"),
    6: ("8", "Module 2 · Lesson 8",  "Logging Basics"),
    7: (None, "Module 2 · Complete", "Programming Foundations Part 2"),  # module complete
}


def fix_next_lesson_badge(html: str, lesson_index: int) -> str:
    """Fix the badge number, module label, and title in the #next-lesson section."""
    info = NEXT_LESSON_INFO[lesson_index]
    badge_num, mod_label, title = info

    # Fix module label — match various encodings of middot
    # Pattern: >Module N · Lesson M< or >Module N &middot; Lesson M< or >Module N · Complete<
    html = re.sub(
        r'(>Module\s+)\d+(\s*(?:·|&middot;)\s*(?:Lesson\s+\d+|Complete))',
        lambda m: m.group(1) + '2' + m.group(2),
        html
    )
    # Now fix the lesson number in the label
    if badge_num is not None:
        html = re.sub(
            r'(>Module 2\s*(?:·|&middot;)\s*Lesson\s+)\d+',
            r'\g<1>' + badge_num,
            html
        )
    else:
        # Complete case — fix "Python Best Practices" → "Programming Foundations Part 2"
        html = re.sub(
            r'(<h3 class="text-base font-bold text-gray-800">)Python Best Practices(</h3>)',
            r'\g<1>Programming Foundations Part 2\2',
            html
        )

    # Fix badge number in the circle
    if badge_num is not None:
        # The badge number appears as: <span class="text-white font-bold text-lg">N</span>
        # inside the #next-lesson section. We need to be careful to only change the one in next-lesson.
        # Strategy: find the section and replace within it
        nl_match = re.search(r'(<section id="next-lesson".*?</section>)', html, re.DOTALL)
        if nl_match:
            nl_section = nl_match.group(1)
            nl_fixed = re.sub(
                r'(<span class="text-white font-bold text-lg">)\d+(</span>)',
                r'\g<1>' + badge_num + r'\2',
                nl_section,
                count=1
            )
            html = html[:nl_match.start()] + nl_fixed + html[nl_match.end():]

    return html


# ── bottom nav fixes ──────────────────────────────────────────────────

BOTTOM_NAV_PREV = {
    # lesson_index: (href, title)  — None means keep as-is
    0: None,  # lesson01 previous points to prior module — keep
    1: None,  # correct already
    2: None,  # correct already
    3: None,  # correct already
    4: ("lesson04_refactoring_a_script_into_a_class.html", "Refactoring a Script into a Class"),
    5: ("lesson05_creating_your_own_modules.html", "Creating Your Own Modules"),
    6: ("lesson06_project_folder_structure.html", "Project Folder Structure"),
    7: ("lesson07_introduction_to_git_simple_workflow.html", "Introduction to Git (Simple Workflow)"),
}

BOTTOM_NAV_NEXT = {
    # lesson_index: (href, title)  — None means keep / no change needed
    0: None,  # correct already
    1: None,  # correct already
    2: None,  # correct already
    3: ("lesson05_creating_your_own_modules.html", "Creating Your Own Modules"),
    4: ("lesson06_project_folder_structure.html", "Project Folder Structure"),
    5: ("lesson07_introduction_to_git_simple_workflow.html", "Introduction to Git (Simple Workflow)"),
    6: ("lesson08_logging_basics.html", "Logging Basics"),
    7: None,  # last lesson — no next
}


def fix_bottom_nav(html: str, lesson_index: int) -> str:
    """Fix the bottom nav Previous/Next links."""

    # Fix Previous link
    prev_info = BOTTOM_NAV_PREV.get(lesson_index)
    if prev_info is not None and lesson_index == 4:
        # lesson05 has a spacer instead of a Previous link — need to add one
        old_spacer = '<div class="flex-1"></div>'
        # Find the spacer that's inside the bottom nav section (after #next-lesson)
        # The bottom nav is the <section> right after #next-lesson
        nl_end = html.rfind('</section>', 0, html.rfind('</section>'))
        # Actually, let's find the bottom nav section more precisely
        # It's the last <section> before </main>
        # Strategy: replace the spacer div with a proper Previous link
        new_prev = (
            f'<a href="{prev_info[0]}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">\n'
            f'      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>\n'
            f'      <div class="min-w-0">\n'
            f'        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>\n'
            f'        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{prev_info[1]}</p>\n'
            f'      </div>\n'
            f'    </a>'
        )
        # Find the spacer inside the bottom nav (the one closest to end of file)
        # We need to be careful - only replace the spacer in the bottom nav, not elsewhere
        # The bottom nav spacer is preceded by the flex container
        spacer_pattern = re.compile(
            r'(<!-- No Previous.*?-->\s*)?<div class="flex-1"></div>',
            re.DOTALL
        )
        # Find all matches, replace the last one (which is in the bottom nav)
        matches = list(spacer_pattern.finditer(html))
        if matches:
            m = matches[-1]
            html = html[:m.start()] + new_prev + html[m.end():]
    elif prev_info is not None:
        # For lessons 5-7: fix the href and title of the existing Previous link
        # Find the bottom nav section - it's after the last #next-lesson section
        bottom_nav_start = html.rfind('<!-- Bottom nav')
        if bottom_nav_start == -1:
            # Try finding the section after next-lesson differently
            bottom_nav_start = len(html) - 2000  # approximate

        # Fix previous href
        prev_pattern = re.compile(
            r'(<a href=")([^"]*?)(" class="lesson-nav-link group flex-1 flex items-center gap-4.*?<p class="text-sm font-bold text-gray-700.*?>)(.*?)(</p>)',
            re.DOTALL
        )
        matches = list(prev_pattern.finditer(html))
        if matches:
            m = matches[-1]  # last one is in bottom nav (Previous link)
            old = m.group(0)
            new = m.group(1) + prev_info[0] + m.group(3) + prev_info[1] + m.group(5)
            html = html[:m.start()] + new + html[m.end():]

    # Fix Next link
    next_info = BOTTOM_NAV_NEXT.get(lesson_index)
    if next_info is not None:
        # Fix the Next link href and title
        next_pattern = re.compile(
            r'(<a href=")([^"]*?)(" class="lesson-nav-link group flex-1 flex items-center justify-end.*?<p class="text-sm font-bold text-gray-700.*?>)(.*?)(</p>)',
            re.DOTALL
        )
        matches = list(next_pattern.finditer(html))
        if matches:
            m = matches[-1]
            old = m.group(0)
            new = m.group(1) + next_info[0] + m.group(3) + next_info[1] + m.group(5)
            html = html[:m.start()] + new + html[m.end():]

    # Fix next link in bottom nav for lesson05 (was lesson02_... → lesson06_...)
    if lesson_index == 4:
        html = html.replace(
            'href="lesson02_project_folder_structure.html"',
            'href="lesson06_project_folder_structure.html"'
        )

    return html


# ── lesson 07 next-lesson content fix ────────────────────────────────

def fix_lesson07_next_content(html: str) -> str:
    """Lesson 07 next-lesson previews 'Git in VS Code' which doesn't exist.
    Replace with 'Logging Basics' preview."""
    old_title = "Git in VS Code"
    new_title = "Logging Basics"
    html = html.replace(
        f'<h3 class="text-base font-bold text-gray-800">{old_title}</h3>',
        f'<h3 class="text-base font-bold text-gray-800">{new_title}</h3>'
    )

    # Replace the 3 preview cards
    old_cards = '''          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-brands:git-alt"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">The Source Control Panel in VS Code</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:code-branch"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Staging &amp; Committing With a Few Clicks</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:rotate-left"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Undoing &amp; Reviewing Changes in the Editor</p>
            </div>
          </div>'''

    new_cards = '''          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:scroll"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">What Logging Is and Why It Matters</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Understanding Logging Levels</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:file-lines"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Writing Logs to a File</p>
            </div>
          </div>'''

    html = html.replace(old_cards, new_cards)
    return html


# ── main ──────────────────────────────────────────────────────────────

def main():
    for i, fpath in enumerate(FILES):
        if not fpath.exists():
            print(f"❌ {fpath.name} — file not found")
            continue

        html = fpath.read_text(encoding="utf-8")
        original = html

        # 1. Fix TOC sidebar
        html, n = replace_toc(html, i)
        toc_ok = n > 0

        # 2. Fix next-lesson badge / module labels
        html = fix_next_lesson_badge(html, i)

        # 3. Fix lesson 07 next-lesson content (Git in VS Code → Logging Basics)
        if i == 6:
            html = fix_lesson07_next_content(html)

        # 4. Fix bottom nav
        html = fix_bottom_nav(html, i)

        if html != original:
            fpath.write_text(html, encoding="utf-8")
            print(f"✅ {fpath.name} — patched (TOC: {'yes' if toc_ok else 'no change'})")
        else:
            print(f"⚠️  {fpath.name} — no changes needed")


if __name__ == "__main__":
    main()
