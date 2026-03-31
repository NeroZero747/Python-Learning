import os
import re

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"

TARGET_FILES = [
    "lesson02_variables_data_types.html",
    "lesson03_additional_python_data_types.html",
    "lesson04_lists_dictionaries.html",
    "lesson05_operators.html",
    "lesson06_if_statements.html",
    "lesson07_loops.html",
    "lesson08_functions.html",
    "lesson09_reading_understanding_errors.html",
]

for f in TARGET_FILES:
    path = os.path.join(DIR, f)
    with open(path) as fh:
        lines = fh.readlines()

    # Strip forbidden opening tags from the top
    # Keep removing lines until we hit a <link line (the preconnect fonts CDN line)
    STRIP_TOP_PATTERNS = [
        r'^\s*<!DOCTYPE',
        r'^\s*<html',
        r'^\s*<head>',
        r'^\s*<meta\s',
        r'^\s*<title>',
    ]
    while lines:
        stripped = lines[0].strip()
        if any(re.match(p, lines[0], re.IGNORECASE) for p in STRIP_TOP_PATTERNS):
            lines.pop(0)
        else:
            break

    # Strip </head> and <body> lines anywhere in the file
    lines = [l for l in lines if not re.match(r'^\s*</head>\s*$', l, re.IGNORECASE)
                               and not re.match(r'^\s*<body>\s*$', l, re.IGNORECASE)]

    # Strip </body> and </html> from the tail
    while lines and re.match(r'^\s*(<\/body>|<\/html>)\s*$', lines[-1].strip(), re.IGNORECASE):
        lines.pop()

    # Also strip any trailing blank lines introduced by the removal
    while lines and lines[-1].strip() == '':
        lines.pop()

    # Write back (no trailing newline added — match lesson01's style)
    with open(path, "w") as fh:
        fh.writelines(lines)

    print(f"stripped: {f} — now starts with: {lines[0].strip()[:70]}")
    print(f"          ends with: {lines[-1].strip()[:70]}")
