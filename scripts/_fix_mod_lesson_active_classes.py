import os

base = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"

files = [
    "lesson01_what_is_programming.html",
    "lesson02_variables_data_types.html",
    "lesson03_additional_python_data_types.html",
    "lesson04_lists_dictionaries.html",
    "lesson05_operators.html",
    "lesson06_if_statements.html",
    "lesson07_loops.html",
    "lesson08_functions.html",
    "lesson09_reading_understanding_errors.html",
]

OLD_SUFFIX = 'class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors"'
NEW_SUFFIX = 'class="mod-lesson-active flex items-center gap-2 px-3 py-2 rounded-lg border text-xs font-medium no-underline transition-colors"'

OLD_DOT = 'class="w-2 h-2 rounded-full bg-[#CB187D] shrink-0"'
NEW_DOT = 'class="lesson-dot w-2 h-2 rounded-full shrink-0"'

for fname in files:
    path = os.path.join(base, fname)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    orig = content

    # Build the exact href+class string to target only the active link for THIS file
    old_link = 'href="' + fname + '" ' + OLD_SUFFIX
    new_link = 'href="' + fname + '" ' + NEW_SUFFIX
    content = content.replace(old_link, new_link)

    # Replace the first occurrence of the pink active dot
    content = content.replace(OLD_DOT, NEW_DOT, 1)

    if content != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("patched: " + fname)
    else:
        print("no match: " + fname)
