"""
Add section comments to the base CSS (Layer 1 & 2) in the <style> block
of all 6 mod_01 lesson files + master template.

Each comment marks the start of a logical component group so it's easy
to see what every class / rule is for at a glance.
"""

import re

TARGET_FILES = [
    "pages/track_01/mod_01_getting_started/lesson01_what_is_python.html",
    "pages/track_01/mod_01_getting_started/lesson02_how_to_request_access_software.html",
    "pages/track_01/mod_01_getting_started/lesson03_how_to_install_extensions_in_vs_code.html",
    "pages/track_01/mod_01_getting_started/lesson04_how_to_setup_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson05_how_to_install_libraries_in_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson06_how_to_run_a_python_notebook_or_script.html",
    "docs/new_lesson_template.html",
]

# ── Each entry: (anchor_starts_with, comment_label)
# The script matches any line inside <style> that starts with 4 spaces + anchor.
# It inserts a blank line + comment on the line immediately before the anchor.
INSERTIONS = [
    # Layer 1 — Base resets
    ("* { scroll-behavior",            "Global reset — smooth scroll"),
    ("pre[class*=\"language-\"]",      "Prism.js — syntax highlighted code blocks"),
    ("h1, h2, h3, h4, h5, h6",        "Heading resets — strip Confluence default margins"),
    (".text-brand",                    "Brand utility classes"),
    # Layer 2 — Tab systems
    (".kc-tab-active",                 "Key Concepts sidebar tabs  (.kc-tab / .kc-tab-active)"),
    (".ce-step:not(.ce-step-active)",  "Code Examples pill tabs   (.ce-step / .ce-step-active)"),
    (".mk-step:not(.mk-step-active)",  "Common Mistakes pill tabs (.mk-step / .mk-step-active)"),
    (".qz-step:not(.qz-step-active)",  "Knowledge Check quiz tabs (.qz-step / .qz-step-active)"),
    (".pe-step:not(.pe-step-active)",  "Practice Exercise tabs    (.pe-step / .pe-step-active)"),
    # Layer 2 — Accordion
    (".accordion-body",                "Accordion — used in Overview & Key Ideas sections"),
    # Layer 2 — Hero banner
    (".hero-container",                "Hero banner — full-width gradient header"),
    # Layer 2 — UI chrome
    (".scroll-progress",              "Scroll progress bar — fixed top-of-page indicator"),
    # Layer 2 — Layout
    (".lesson-layout",                 "Page layout — two-column: TOC sidebar + main content"),
    # Layer 2 — Content cards
    (".obj-card",                      "Objective cards — Learning Goals section grid"),
    # Layer 2 — Generic tabs (secondary system)
    (".tab-btn",                       "Generic outline tab buttons (.tab-btn / .tab-panel)"),
    # Layer 2 — Code copy
    (".copy-btn",                      "Code block copy button (.copy-btn)"),
    # Layer 2 — Navigation
    (".lesson-nav-link",               "Bottom lesson navigation — Previous / All Lessons / Next"),
    # Layer 2 — Back to top
    (".back-to-top",                   "Back-to-top floating button"),
    # Layer 2 — Quiz feedback
    (".quiz-btn.correct",              "Quiz answer feedback buttons (.quiz-btn.correct / .incorrect)"),
    # Layer 2 — Card hover animations
    (".mistake-card",                  "Card hover animations — Mistake, Flow, Recap, Overview cards"),
    # Responsive + Print
    ("@media (max-width: 767px)",      "Responsive — mobile breakpoint (<768px)"),
    ("@media print",                   "Print styles — hide interactive chrome when printing"),
    # Icon utility
    (".iconify { vertical-align",      "Iconify icon alignment utility"),
]

INDENT = "    "  # 4 spaces — matches CSS indentation inside <style>


def comment_line(label):
    bar = "─" * (56 - len(label))
    return f"{INDENT}/* ── {label} {bar} */\n"


def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")

    # Find the <style> … </style> bounds (first occurrence only)
    style_start = next((i for i, l in enumerate(lines) if "<style>" in l), None)
    style_end   = next((i for i, l in enumerate(lines) if "</style>" in l), None)
    if style_start is None or style_end is None:
        print(f"❌ no <style> found  {path}")
        return

    # Find the Confluence isolation comment to stop before it
    isolation_line = next(
        (i for i, l in enumerate(lines) if "CONFLUENCE ISOLATION" in l), style_end
    )

    changes = 0

    for anchor, label in INSERTIONS:
        cmnt = comment_line(label)

        # Search for the anchor line within base CSS (before isolation block)
        for i in range(style_start + 1, isolation_line):
            stripped = lines[i].lstrip()
            if not stripped.startswith(anchor):
                continue

            # Check if comment already directly above (skip blank lines)
            prev = i - 1
            while prev >= style_start and lines[prev].strip() == "":
                prev -= 1

            if prev >= style_start and lines[prev].strip().startswith("/* ──"):
                break  # already commented — skip

            # Remove any existing weak comment immediately above (e.g. "/* Prism overrides */", "/* Headings */")
            if prev >= style_start and lines[prev].strip().startswith("/*") and "CONFLUENCE" not in lines[prev]:
                old_comment = lines[prev]
                # Replace it with our standardised comment
                lines[prev] = cmnt.rstrip("\n")
                changes += 1
                break

            # Insert blank line + comment before this anchor line
            lines.insert(i, cmnt.rstrip("\n"))
            # Insert blank line before comment for spacing (unless prev line is already blank)
            if lines[i - 1].strip() != "":
                lines.insert(i, "")
            changes += 1
            break  # only insert once per anchor

    new_content = "\n".join(lines)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    if changes:
        print(f"✅ {changes:2d} comments added   {path}")
    else:
        print(f"⚠️  already commented  {path}")


import os
base = os.path.dirname(os.path.abspath(__file__))
for rel in TARGET_FILES:
    process_file(os.path.join(base, rel))
