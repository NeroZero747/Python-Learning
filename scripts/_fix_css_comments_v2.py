"""
Add CSS section comment headers to all 7 lesson/template files.
v2: works on raw text (not line indices) so there's no index-staleness bug.
"""

import os, re

TARGET_FILES = [
    "pages/track_01/mod_01_getting_started/lesson01_what_is_python.html",
    "pages/track_01/mod_01_getting_started/lesson02_how_to_request_access_software.html",
    "pages/track_01/mod_01_getting_started/lesson03_how_to_install_extensions_in_vs_code.html",
    "pages/track_01/mod_01_getting_started/lesson04_how_to_setup_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson05_how_to_install_libraries_in_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson06_how_to_run_a_python_notebook_or_script.html",
    "docs/new_lesson_template.html",
]

# (anchor_text, comment_label)
# anchor_text must appear at the START of a line (after leading whitespace)
# in the BASE CSS — i.e., before the Confluence isolation block.
INSERTIONS = [
    (":root {",                              "CSS Variables \u2014 font tokens (:root)"),
    ("* { scroll-behavior",                  "Global reset \u2014 smooth scroll"),
    ('pre[class*="language-"]',              "Prism.js \u2014 syntax highlighted code blocks"),
    ("h1, h2, h3, h4, h5, h6",             "Heading resets \u2014 strip Confluence default margins"),
    (".text-brand",                          "Brand utility classes"),
    (".kc-tab-active",                       "Key Concepts sidebar tabs  (.kc-tab / .kc-tab-active)"),
    (".ce-step:not(.ce-step-active)",        "Code Examples pill tabs   (.ce-step / .ce-step-active)"),
    (".mk-step:not(.mk-step-active)",        "Common Mistakes pill tabs (.mk-step / .mk-step-active)"),
    (".qz-step:not(.qz-step-active)",        "Knowledge Check quiz tabs (.qz-step / .qz-step-active)"),
    (".pe-step:not(.pe-step-active)",        "Practice Exercise tabs    (.pe-step / .pe-step-active)"),
    (".accordion-body",                      "Accordion \u2014 used in Overview & Key Ideas sections"),
    (".hero-container",                      "Hero banner \u2014 full-width gradient header"),
    (".scroll-progress",                     "Scroll progress bar \u2014 fixed top-of-page indicator"),
    (".lesson-layout",                       "Page layout \u2014 two-column: TOC sidebar + main content"),
    (".obj-card",                            "Objective cards \u2014 Learning Goals section grid"),
    (".tab-btn",                             "Generic outline tab buttons (.tab-btn / .tab-panel)"),
    (".copy-btn",                            "Code block copy button (.copy-btn)"),
    (".lesson-nav-link",                     "Bottom lesson navigation \u2014 Previous / All Lessons / Next"),
    (".back-to-top",                         "Back-to-top floating button"),
    (".quiz-btn.correct",                    "Quiz answer feedback buttons (.quiz-btn.correct / .incorrect)"),
    (".mistake-card",                        "Card hover animations \u2014 Mistake, Flow, Recap, Overview cards"),
    ("@media (max-width: 767px)",            "Responsive \u2014 mobile breakpoint (<768px)"),
    ("@media print",                         "Print styles \u2014 hide interactive chrome when printing"),
    (".iconify { vertical-align",            "Iconify icon alignment utility"),
]

BAR_WIDTH = 56  # desired total width of comment (inside /* … */)


def make_comment(label):
    dashes = "\u2500" * max(2, BAR_WIDTH - len(label) - 4)
    return f"/* \u2500\u2500 {label} {dashes} */"


def insert_comment_in_base_css(txt, anchor, comment):
    """
    Find the first occurrence of `anchor` that appears:
      - inside the <style>…</style> block
      - BEFORE the Confluence isolation block (identified by 'CONFLUENCE ISOLATION' comment)
    and prepend `comment` if not already present directly above the anchor.
    Returns (new_txt, changed: bool).
    """
    style_start = txt.find("<style>")
    style_end   = txt.find("</style>")
    if style_start == -1 or style_end == -1:
        return txt, False

    isolation_marker = "CONFLUENCE ISOLATION"
    iso_pos = txt.find(isolation_marker, style_start)
    search_end = iso_pos if iso_pos != -1 else style_end

    base_css = txt[style_start:search_end]

    # Find anchor as start of a stripped line
    # We match: newline + optional spaces + anchor
    pattern = re.compile(r'(\n[ \t]*)(' + re.escape(anchor) + r')')
    m = pattern.search(base_css)
    if not m:
        return txt, False  # anchor not in base CSS

    # Check if our comment (or any /* ── comment) immediately precedes the anchor
    before_anchor = base_css[:m.start()]
    # Find the last non-blank line before the anchor
    lines_before = before_anchor.rstrip("\n").split("\n")
    last_line = lines_before[-1].strip() if lines_before else ""

    if last_line.startswith("/* \u2500\u2500"):
        return txt, False  # already has a section comment above it

    # Remove any legacy weak comment (e.g. "/* Prism overrides */", "/* Headings */")
    # directly above the anchor (single-line old-style comments)
    if last_line.startswith("/*") and "CONFLUENCE" not in last_line:
        # Replace that old comment line with our new one
        old_comment_line = lines_before[-1]
        indent = len(old_comment_line) - len(old_comment_line.lstrip())
        new_comment_line = " " * indent + comment
        # Rebuild: replace last line of before_anchor
        new_before = "\n".join(lines_before[:-1] + [new_comment_line])
        new_base_css = new_before + base_css[m.start():]
        # Re-assemble full text
        new_txt = txt[:style_start] + new_base_css + txt[style_start + len(base_css):]
        return new_txt, True

    # Insert blank line + comment before the anchor
    indent_str = m.group(1)  # the "\n   " before anchor
    insertion = indent_str + comment + indent_str
    new_base_css = base_css[:m.start()] + insertion + base_css[m.start():]
    new_txt = txt[:style_start] + new_base_css + txt[style_start + len(base_css):]
    return new_txt, True


base_dir = os.path.dirname(os.path.abspath(__file__))

for rel in TARGET_FILES:
    path = os.path.join(base_dir, rel)
    with open(path, encoding="utf-8") as f:
        txt = f.read()

    total_changes = 0
    for anchor, label in INSERTIONS:
        comment = make_comment(label)
        txt, changed = insert_comment_in_base_css(txt, anchor, comment)
        if changed:
            total_changes += 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)

    name = os.path.basename(rel)
    if total_changes:
        print(f"\u2705 {total_changes:2d} new comments   {name}")
    else:
        print(f"\u26a0\ufe0f  already complete  {name}")
