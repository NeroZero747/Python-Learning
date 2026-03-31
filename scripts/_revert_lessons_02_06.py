import os
import re

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"

TARGET_FILES = [
    "lesson02_variables_data_types.html",
    "lesson03_additional_python_data_types.html",
    "lesson04_lists_dictionaries.html",
    "lesson05_operators.html",
    "lesson06_if_statements.html",
]

# The CSS block injected by _fix_mod_lesson_css.py (added right after .toc-link.active line)
MOD_LESSON_CSS = (
    "\n"
    "  /* \u2500\u2500 Module lessons list active link \u2500\u2500 */\n"
    "  #hub-root .mod-lesson-active {\n"
    "    background-color: #fdf0f7 !important; border-color: #CB187D !important; color: #CB187D !important;\n"
    "  }\n"
    "  #hub-root .mod-lesson-active .lesson-dot { background-color: #CB187D !important; }"
)

for f in TARGET_FILES:
    path = os.path.join(DIR, f)
    with open(path) as fh:
        content = fh.read()

    original = content

    # 1. Remove the injected mod-lesson-active CSS block
    content = content.replace(MOD_LESSON_CSS, "")

    # 2. Remove id="hub-root" from the outer wrapper div
    content = content.replace('<div id="hub-root" class="bg-gray-50 min-h-screen">', '<div class="bg-gray-50 min-h-screen">')

    # 3. Restore HTML shell at the top
    if not content.startswith("<!DOCTYPE"):
        content = (
            "<!DOCTYPE html>\n"
            '<html lang="en">\n'
            "<head>\n"
            '  <meta charset="UTF-8">\n'
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        ) + content

    # 4. Restore </head><body> between </style> and the scroll-progress div
    # The </style> is followed immediately by the scroll-progress div in current state
    content = content.replace(
        "  </style>\n<div class=\"scroll-progress\"",
        "  </style>\n</head>\n<body>\n\n<div class=\"scroll-progress\""
    )

    # 5. Restore </body></html> at the end
    if not content.rstrip().endswith("</html>"):
        content = content.rstrip() + "\n\n</body>\n</html>"

    if content != original:
        with open(path, "w") as fh:
            fh.write(content)
        print(f"reverted: {f}")
    else:
        print(f"no changes needed: {f}")
