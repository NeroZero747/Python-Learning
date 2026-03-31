"""Add the :root CSS Variables comment header to all 7 lesson/template files."""

TARGET_FILES = [
    "pages/track_01/mod_01_getting_started/lesson01_what_is_python.html",
    "pages/track_01/mod_01_getting_started/lesson02_how_to_request_access_software.html",
    "pages/track_01/mod_01_getting_started/lesson03_how_to_install_extensions_in_vs_code.html",
    "pages/track_01/mod_01_getting_started/lesson04_how_to_setup_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson05_how_to_install_libraries_in_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson06_how_to_run_a_python_notebook_or_script.html",
    "docs/new_lesson_template.html",
]

COMMENT = "    /* \u2500\u2500 CSS Variables \u2014 font tokens (:root) \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 */\n"
ANCHOR = "    :root {"

import os
base = os.path.dirname(os.path.abspath(__file__))

for rel in TARGET_FILES:
    path = os.path.join(base, rel)
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    if COMMENT.strip() in txt:
        print(f"\u26a0\ufe0f  already done   {rel}")
        continue
    if ANCHOR not in txt:
        print(f"\u274c anchor not found  {rel}")
        continue
    txt = txt.replace(ANCHOR, COMMENT + ANCHOR, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"\u2705 root comment added  {rel}")
