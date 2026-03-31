"""
Restore #hub-root .lesson-nav-link:hover override that was dropped during refactoring.
This makes the previous/all-lessons/next nav buttons highlight pink on hover in Confluence.
"""

import os

TARGET_FILES = [
    "pages/track_01/mod_01_getting_started/lesson01_what_is_python.html",
    "pages/track_01/mod_01_getting_started/lesson02_how_to_request_access_software.html",
    "pages/track_01/mod_01_getting_started/lesson03_how_to_install_extensions_in_vs_code.html",
    "pages/track_01/mod_01_getting_started/lesson04_how_to_setup_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson05_how_to_install_libraries_in_a_virtual_environment.html",
    "pages/track_01/mod_01_getting_started/lesson06_how_to_run_a_python_notebook_or_script.html",
    "docs/new_lesson_template.html",
]

# The rule to insert — restore the hub-root override that was in the original template
NEW_RULE = """
  /* -- Bottom nav link hover — all child text/icons turn brand pink -- */
  #hub-root .lesson-nav-link:hover p,
  #hub-root .lesson-nav-link:hover span,
  #hub-root .lesson-nav-link:hover svg {
    color: #CB187D !important;
    transition: color 0.15s !important;
  }
  </style>"""

OLD_ENDING = """  }
</style>"""

# More specific anchor pattern to avoid ambiguous matches (last occurrence only)
ANCHOR = """  #hub-root .toc-link.active {
    color: #CB187D !important;
    font-weight: 600 !important;
    border-left: 3px solid #CB187D !important;
    padding-left: 8px !important;
    background-color: #fdf0f7 !important;
  }
</style>"""

REPLACEMENT = """  #hub-root .toc-link.active {
    color: #CB187D !important;
    font-weight: 600 !important;
    border-left: 3px solid #CB187D !important;
    padding-left: 8px !important;
    background-color: #fdf0f7 !important;
  }

  /* -- Bottom nav link hover — all child text/icons turn brand pink -- */
  #hub-root .lesson-nav-link:hover p,
  #hub-root .lesson-nav-link:hover span,
  #hub-root .lesson-nav-link:hover svg {
    color: #CB187D !important;
    transition: color 0.15s !important;
  }
  </style>"""

base = os.path.dirname(os.path.abspath(__file__))

for rel_path in TARGET_FILES:
    path = os.path.join(base, rel_path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "#hub-root .lesson-nav-link:hover" in content:
        print(f"⚠️  already patched  {rel_path}")
        continue

    if ANCHOR not in content:
        print(f"❌ anchor not found  {rel_path}")
        continue

    updated = content.replace(ANCHOR, REPLACEMENT, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"✅ patched            {rel_path}")
