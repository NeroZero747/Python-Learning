"""
Combine lesson05 (ORDER BY) into lesson03 (SELECT) for the SQL Foundations module.
1. Delete lesson05_sorting_data_with_order_by.html
2. Rename: lesson06 -> lesson05, lesson07 -> lesson06, lesson08 -> lesson07, lesson09 -> lesson08
3. Update all internal hrefs and lesson labels across all remaining files in the module.
"""
import os
import re

MOD_DIR = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations"

# Step 1: Delete lesson05
old_l05 = os.path.join(MOD_DIR, "lesson05_sorting_data_with_order_by.html")
if os.path.exists(old_l05):
    os.remove(old_l05)
    print(f"DELETED: {old_l05}")

# Step 2: Rename lessons 6->5, 7->6, 8->7, 9->8
renames = [
    ("lesson06_aggregations_count_sum_avg.html", "lesson05_aggregations_count_sum_avg.html"),
    ("lesson07_group_by.html",                    "lesson06_group_by.html"),
    ("lesson08_filtering_groups_with_having.html","lesson07_filtering_groups_with_having.html"),
    ("lesson09_joining_tables_join.html",         "lesson08_joining_tables_join.html"),
]
for old, new in renames:
    o = os.path.join(MOD_DIR, old)
    n = os.path.join(MOD_DIR, new)
    if os.path.exists(o):
        os.rename(o, n)
        print(f"RENAMED: {old} -> {new}")

# Step 3: For every remaining HTML file, update hrefs + lesson number labels in TOC sidebar.
# - href substitutions (apply to filename only):
href_map = {
    "lesson06_aggregations_count_sum_avg.html":  "lesson05_aggregations_count_sum_avg.html",
    "lesson07_group_by.html":                    "lesson06_group_by.html",
    "lesson08_filtering_groups_with_having.html":"lesson07_filtering_groups_with_having.html",
    "lesson09_joining_tables_join.html":         "lesson08_joining_tables_join.html",
}
# - TOC sidebar label substitutions (the "5. Sorting Data..." line must be removed; "6. Aggregations" -> "5. Aggregations" etc.)
toc_label_map = {
    '6. Aggregations (COUNT, SUM, AVG)':  '5. Aggregations (COUNT, SUM, AVG)',
    '7. GROUP BY':                         '6. GROUP BY',
    '8. Filtering Groups with HAVING':     '7. Filtering Groups with HAVING',
    '9. Joining Tables (JOIN)':            '8. Joining Tables (JOIN)',
}
# - Module-progress pills (e.g. "5/9", "6/9", "7/9", "8/9", "9/9" -> "4/8", "5/8", "6/8", "7/8", "8/8")
# We'll handle by file-specific position.
progress_map = {
    "lesson01_what_is_sql.html":                   ("1", "8"),
    "lesson02_tables_rows_and_columns.html":       ("2", "8"),
    "lesson03_the_select_statement.html":          ("3", "8"),
    "lesson04_filtering_data_with_where.html":     ("4", "8"),
    "lesson05_aggregations_count_sum_avg.html":    ("5", "8"),
    "lesson06_group_by.html":                      ("6", "8"),
    "lesson07_filtering_groups_with_having.html":  ("7", "8"),
    "lesson08_joining_tables_join.html":           ("8", "8"),
}

# The TOC sidebar contains a hardcoded link to the deleted lesson05 - REMOVE that block.
sorting_toc_block_re = re.compile(
    r'<a href="lesson05_sorting_data_with_order_by\.html"[^>]*>\s*'
    r'<span[^>]*></span>\s*'
    r'<span[^>]*>5\. Sorting Data with ORDER BY</span>\s*'
    r'</a>\s*',
    re.MULTILINE,
)

for fname in os.listdir(MOD_DIR):
    if not fname.endswith(".html"):
        continue
    fpath = os.path.join(MOD_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content

    # Remove the deleted lesson05 link block from TOC sidebar
    content = sorting_toc_block_re.sub("", content)

    # Replace hrefs (filename-only matches)
    for old_h, new_h in href_map.items():
        content = content.replace(old_h, new_h)

    # Replace TOC numbered labels
    for old_l, new_l in toc_label_map.items():
        content = content.replace(old_l, new_l)

    # Update progress pill: "X<span class="font-bold opacity-50">/9</span>" -> "X<...>/8</span>"
    content = re.sub(r'/9</span>', '/8</span>', content)

    # Per-file: update lesson position number in progress pill (the "X" before /8)
    if fname in progress_map:
        pos, total = progress_map[fname]
        # The hero progress pill pattern: <span class="font-extrabold">N<span class="font-bold opacity-50">/8</span>
        content = re.sub(
            r'(<span class="font-extrabold">)\d+(<span class="font-bold opacity-50">/8</span>)',
            r'\g<1>' + pos + r'\g<2>',
            content,
        )

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"UPDATED: {fname}")
    else:
        print(f"unchanged: {fname}")

print("\nDone.")
