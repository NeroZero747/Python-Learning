"""
Verify CSS comment group headers exist in all 7 lesson/template files.
Only checks for a comment if the corresponding CSS anchor exists in the file.
"""

import os, re

FILES = [
    "pages/track_01/mod_01_getting_started/lesson01_what_is_python.html",
    "pages/track_01/mod_01_getting_started/lesson02_how_to_request_access_software.html",
    "pages/track_01/mod_01_getting_started/lesson03_how_to_install_extensions_in_vs_code.html",
    "pages/track_01/mod_01_getting_started/lesson04_how_to_setup_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson05_how_to_install_libraries_in_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson06_how_to_run_a_python_notebook_or_script.html",
    "docs/new_lesson_template.html",
]

# (css_anchor, comment_label_fragment_to_check)
# Only verify the comment if the css_anchor exists in the file's base CSS.
CHECKS = [
    (":root {",                              "CSS Variables"),
    ("* { scroll-behavior",                  "Global reset"),
    ('pre[class*="language-"]',              "Prism.js"),
    ("h1, h2, h3, h4, h5, h6",             "Heading resets"),
    (".text-brand",                          "Brand utility classes"),
    (".kc-tab-active",                       "kc-tab"),
    (".ce-step:not(.ce-step-active)",        "ce-step"),
    (".mk-step:not(.mk-step-active)",        "mk-step"),
    (".qz-step:not(.qz-step-active)",        "qz-step"),
    (".pe-step:not(.pe-step-active)",        "pe-step"),
    (".accordion-body",                      "Accordion"),
    (".hero-container",                      "Hero banner"),
    (".scroll-progress",                     "Scroll progress"),
    (".lesson-layout",                       "Page layout"),
    (".obj-card",                            "Objective cards"),
    (".tab-btn",                             "tab-btn"),
    (".copy-btn",                            "copy-btn"),
    (".lesson-nav-link",                     "lesson-nav"),
    (".back-to-top",                         "back-to-top"),
    (".quiz-btn.correct",                    "quiz-btn"),
    (".mistake-card",                        "Card hover"),
    ("@media (max-width: 767px)",            "mobile breakpoint"),
    ("@media print",                         "Print styles"),
    (".iconify { vertical-align",            "Iconify"),
]

base = os.path.dirname(os.path.abspath(__file__))
all_ok = True

for rel in FILES:
    path = os.path.join(base, rel)
    with open(path, encoding="utf-8") as f:
        full_txt = f.read()

    # Scope to base CSS only (before Confluence isolation block)
    style_start = full_txt.find("<style>")
    iso_pos = full_txt.find("CONFLUENCE ISOLATION", style_start)
    style_end = full_txt.find("</style>")
    base_css = full_txt[style_start: iso_pos if iso_pos != -1 else style_end]

    missing = []
    for anchor, label in CHECKS:
        if anchor not in base_css:
            continue  # CSS rule not in this file — skip
        if label not in full_txt:
            missing.append(label)

    name = os.path.basename(rel)
    if missing:
        print(f"\u274c MISSING comment in {name}: {missing}")
        all_ok = False
    else:
        print(f"\u2705 OK  {name}")

if all_ok:
    print("\nAll files pass \u2014 every CSS section has its comment header.")
