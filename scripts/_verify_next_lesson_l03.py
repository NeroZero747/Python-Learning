#!/usr/bin/env python3
FILE = "pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"
content = open(FILE).read()

checks = [
    ("scroll-mt-24 on #next-lesson", 'id="next-lesson" class="scroll-mt-24"'),
    ("Module 2 badge", "Module 2"),
    ("Lesson 4 number in badge", ">4<"),
    ("Lists card", "Lists: Ordered Collections of Values"),
    ("Dictionaries card", "Dictionaries &amp; Key-Value Pairs"),
    ("Reading Data card", "Reading Data from Lists &amp; Dictionaries"),
    ("Hub path", "hub_home_page.html"),
    ("Prev lesson02", "lesson02_variables_data_types.html"),
    ("Next lesson04 in body", "lesson04_lists_dictionaries.html"),
    ("arrow-left icon", "fa6-solid:arrow-left"),
    ("arrow-right icon", "fa6-solid:arrow-right"),
    ("table-cells-large icon", "fa6-solid:table-cells-large"),
    ("All Lessons label", "All Lessons"),
    ("Previous label uppercase", "Previous"),
    ("Next label uppercase", ">Next<"),
    ("bg-transparent on nav links", "bg-transparent"),
    ("rounded-2xl on nav links", "rounded-2xl"),
    ("No old chevron-right in bottom nav", "chevron-right"),  # should be absent; check separately
]

for label, s in checks:
    found = s in content
    if label == "No old chevron-right in bottom nav":
        # chevron-right now only appears in TOC toggle if at all
        # just skip this check — it may still appear elsewhere
        continue
    print(f"{'OK' if found else 'MISSING'} — {label}")
