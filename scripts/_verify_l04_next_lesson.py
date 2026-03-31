import pathlib

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")
html = TARGET.read_text(encoding="utf-8")

# Extract #next-lesson section + following bottom nav section
idx = html.find('id="next-lesson"')
# find two </section> tags — first closes #next-lesson, second closes bottom nav
first_sec_end = html.find("</section>", idx) + len("</section>")
second_sec_end = html.find("</section>", first_sec_end) + len("</section>")
s = html[idx:second_sec_end]

checks = [
    # Section shell preserved
    ('Shell: id=next-lesson',                     'id="next-lesson"'),
    ('Shell: scroll-mt-24',                        'scroll-mt-24'),
    ('Shell: fa6-solid:circle-arrow-right',        'data-icon="fa6-solid:circle-arrow-right"'),
    ('Shell: Next Lesson title',                   '>Next Lesson<'),
    ('Shell: Preview subtitle',                    'Preview of what comes next'),
    # Badge — correct lesson number and module
    ('Badge number: 1',                            '>1<'),
    ('Badge label: Module 4 · Lesson 1',           'Module 4 \u00b7 Lesson 1'),
    ('Badge title: Creating Your Own Modules',     '>Creating Your Own Modules<'),
    ('Badge: Next you will learn',                 'Next you will learn:'),
    # Old badge values gone
    ('Old badge number 2 gone',                    '>2<' not in s),
    ('Old Lesson 2 label gone',                    'Lesson 2' not in s),
    # Preview cards — icons
    ('Card 1 icon: fa6-solid:cube',                'data-icon="fa6-solid:cube"'),
    ('Card 2 icon: fa6-solid:file-code',           'data-icon="fa6-solid:file-code"'),
    ('Card 3 icon: fa6-solid:arrow-right-to-bracket', 'data-icon="fa6-solid:arrow-right-to-bracket"'),
    # Preview cards — text (noun phrases)
    ('Card 1 text: What a Python Module Is',       'What a Python Module Is'),
    ('Card 2 text: Moving Functions into a Separate File', 'Moving Functions into a Separate File'),
    ('Card 3 text: Importing Your Module into a Script', 'Importing Your Module into a Script'),
    # Old card texts gone
    ('Old Writing a module file gone',             'Writing a module file' not in s),
    ('Old Importing your code gone',               'Importing your code' not in s),
    ('Old Reusing across projects gone',           'Reusing across projects' not in s),
    ('Old fa6-solid:boxes-stacked gone',           'fa6-solid:boxes-stacked' not in s),
    # 3 preview cards total
    ('3 obj-card preview items',                   s.count('class="obj-card flex items-center gap-3') == 3),
    # What You Will Learn label
    ('What You Will Learn label',                  'What You Will Learn'),
    # Bottom nav — Previous
    ('Bottom nav: Previous link correct file',     'href="lesson03_attributes_methods.html"'),
    ('Bottom nav: Previous label',                 '>Previous<'),
    ('Bottom nav: Attributes &amp; Methods',       'Attributes &amp; Methods'),
    # Bottom nav — All Lessons
    ('Bottom nav: All Lessons hub link',           'href="../../../hub_home_page.html"'),
    ('Bottom nav: table-cells-large icon',         'fa6-solid:table-cells-large'),
    # Bottom nav — Next
    ('Bottom nav: Next link correct file (lesson01)', 'href="../mod_04_python_best_practices/lesson01_creating_your_own_modules.html"'),
    ('Bottom nav: Next label',                     '>Next<'),
    ('Bottom nav: Next title matches section',     '>Creating Your Own Modules<'),
    # Old next link (lesson02) gone
    ('Old lesson02 link gone',                     'lesson02_creating_your_own_modules' not in s),
    # lesson-nav-link class on all 3 nav links
    ('3 lesson-nav-link anchors',                  s.count('lesson-nav-link') == 3),
]

passed = failed = 0
for label, check in checks:
    ok = check if isinstance(check, bool) else (check in s)
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f"\n{passed}/{passed+failed} checks passed")
print(f"File size: {len(html):,} chars")
