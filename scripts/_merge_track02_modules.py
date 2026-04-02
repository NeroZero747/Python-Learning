"""
Merge mod_01 + mod_02 into a single mod_01_python_foundations folder for track_02.

- Lessons 01-09  come from mod_01_programming_foundations_part_1  (filenames unchanged)
- Lessons 10-15 come from mod_02_programming_foundations_part_2  (renumbered: lesson01→lesson10, …)

For every output file this script:
  1. Updates the TOC module-lessons list (all 15 lessons, correct active link)
  2. Updates the progress pill denominator (/9 or /8 → /15)
  3. Updates mod_02 progress numerators and hero "Lesson 0X" labels
  4. Renames all internal href= references in the mod_02 files to the new lesson10-15 names
  5. Updates #next-lesson badge numbers and "Module 2 · Lesson N" labels
  6. Rewrites lesson09's special "module-transition" #next-lesson section to a plain next-lesson card
  7. Adds a Previous nav link to lesson10 (first lesson of merged mod_02 block)

The original files are NOT touched. Output goes to mod_01_python_foundations/
"""

import os, re

BASE    = r'c:/Users/nightwolf/Projects/Python-Learning/pages/track_02_python_foundation'
OLD_M1  = os.path.join(BASE, 'mod_01_programming_foundations_part_1')
OLD_M2  = os.path.join(BASE, 'mod_02_programming_foundations_part_2')
NEW_DIR = os.path.join(BASE, 'mod_01_python_foundations')

os.makedirs(NEW_DIR, exist_ok=True)

# ── Lesson manifest ──────────────────────────────────────────────────────────
# (new_filename, toc_label, source_path)
LESSONS = [
    ('lesson01_what_is_programming.html',                 '1. What is Programming?',               OLD_M1),
    ('lesson02_variables_data_types.html',                '2. Variables &amp; Data Types',          OLD_M1),
    ('lesson03_additional_python_data_types.html',        '3. Additional Python Data Types',        OLD_M1),
    ('lesson04_lists_dictionaries.html',                  '4. Lists &amp; Dictionaries',            OLD_M1),
    ('lesson05_operators.html',                           '5. Operators',                           OLD_M1),
    ('lesson06_if_statements.html',                       '6. If Statements',                       OLD_M1),
    ('lesson07_loops.html',                               '7. Loops',                               OLD_M1),
    ('lesson08_functions.html',                           '8. Functions',                           OLD_M1),
    ('lesson09_reading_understanding_errors.html',        '9. Reading &amp; Understanding Errors',  OLD_M1),
    ('lesson10_introduction_to_classes.html',             '10. Introduction to Classes',            OLD_M2),
    ('lesson11_attributes_methods.html',                  '11. Attributes &amp; Methods',           OLD_M2),
    ('lesson12_refactoring_a_script_into_a_class.html',   '12. Refactoring a Script into a Class',  OLD_M2),
    ('lesson13_modules_and_project_structure.html',       '13. Modules &amp; Project Structure',    OLD_M2),
    ('lesson14_introduction_to_git_simple_workflow.html', '14. Introduction to Git',                OLD_M2),
    ('lesson15_logging_basics.html',                      '15. Logging Basics',                     OLD_M2),
]

# Source filename inside each mod folder (old name for mod_02 files)
MOD2_OLD_NAMES = {
    'lesson10_introduction_to_classes.html':             'lesson01_introduction_to_classes.html',
    'lesson11_attributes_methods.html':                  'lesson02_attributes_methods.html',
    'lesson12_refactoring_a_script_into_a_class.html':   'lesson03_refactoring_a_script_into_a_class.html',
    'lesson13_modules_and_project_structure.html':       'lesson04_modules_and_project_structure.html',
    'lesson14_introduction_to_git_simple_workflow.html': 'lesson05_introduction_to_git_simple_workflow.html',
    'lesson15_logging_basics.html':                      'lesson06_logging_basics.html',
}

# ── TOC module-list generator ─────────────────────────────────────────────────
def make_toc_module_list(active_num):
    lines = [
        '<div class="toc-module-list px-3 py-3">',
        '            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2 px-1">Module Lessons</p>',
        '            <div class="space-y-1">',
    ]
    for i, (fname, label, _) in enumerate(LESSONS):
        n = i + 1
        if n == active_num:
            lines.append(
                f'<a href="{fname}" class="mod-lesson-active flex items-center gap-2 px-3 py-2 '
                f'rounded-lg border text-xs font-medium no-underline transition-colors">'
            )
            lines.append('  <span class="w-2 h-2 rounded-full lesson-dot shrink-0"></span>')
        else:
            lines.append(
                f'<a href="{fname}" class="flex items-center gap-2 px-3 py-2 rounded-lg border '
                f'bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium '
                f'no-underline transition-colors">'
            )
            lines.append('  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>')
        lines.append(f'  <span class="truncate">{label}</span>')
        lines.append('</a>')
    lines += ['</div>', '          </div>']
    return '\n'.join(lines)

def replace_toc_module_list(content, active_num):
    new_block = make_toc_module_list(active_num)
    pattern = r'<div class="toc-module-list px-3 py-3">.*?</div>\s*</div>'
    result, n = re.subn(pattern, new_block, content, count=1, flags=re.DOTALL)
    if n == 0:
        print('  ⚠  toc-module-list block NOT found')
    return result

# ── Lesson 09 replacement blocks ─────────────────────────────────────────────
LESSON09_NEXT_SECTION = '''\
<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Lesson badge -->
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">10</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 2 &middot; Lesson 10</p>
          <h3 class="text-base font-bold text-gray-800">Introduction to Classes</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <!-- 3-card preview grid -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:lightbulb"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Why Classes Exist</p>
            </div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:cube"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">How to Define a Class</p>
            </div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:circle-nodes"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Creating Objects from a Class</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- Bottom nav — Previous / All Lessons / Next -->
<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <a href="lesson08_functions.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Functions</p>
      </div>
    </a>

    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <a href="lesson10_introduction_to_classes.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Introduction to Classes</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>'''

# ── Per-lesson transformation config ─────────────────────────────────────────
# For mod_02 files: (old_lesson_label, new_lesson_label, old_progress, new_progress,
#                    old_badge, new_badge, old_module_label, new_module_label)
MOD2_CONFIG = {
    'lesson10_introduction_to_classes.html': {
        'hero_label': ('Lesson 01', 'Lesson 10'),
        'progress':   ('extrabold">2<span class="font-bold opacity-50">/8',
                       'extrabold">10<span class="font-bold opacity-50">/15'),
        'badge':      ('text-lg">2', 'text-lg">11'),
        'mod_label':  ('Module 2 · Lesson 2', 'Module 2 · Lesson 11'),
        # next-lesson points to lesson11 (was lesson02) — handled by href rename
    },
    'lesson11_attributes_methods.html': {
        'hero_label': ('Lesson 02', 'Lesson 11'),
        'progress':   ('extrabold">3<span class="font-bold opacity-50">/8',
                       'extrabold">11<span class="font-bold opacity-50">/15'),
        'badge':      ('text-lg">4', 'text-lg">12'),
        'mod_label':  ('Module 2 · Lesson 3', 'Module 2 · Lesson 12'),  # may or may not exist
    },
    'lesson12_refactoring_a_script_into_a_class.html': {
        'hero_label': ('Lesson 03', 'Lesson 12'),
        'progress':   ('extrabold">4<span class="font-bold opacity-50">/8',
                       'extrabold">12<span class="font-bold opacity-50">/15'),
        'badge':      ('text-lg">4', 'text-lg">13'),
        'mod_label':  ('Module 2 · Lesson 4', 'Module 2 · Lesson 13'),
    },
    'lesson13_modules_and_project_structure.html': {
        'hero_label': ('Lesson 04', 'Lesson 13'),
        'progress':   ('extrabold">6<span class="font-bold opacity-50">/8',
                       'extrabold">13<span class="font-bold opacity-50">/15'),
        'badge':      ('text-lg">5', 'text-lg">14'),
        'mod_label':  ('Module 2 · Lesson 5', 'Module 2 · Lesson 14'),
    },
    'lesson14_introduction_to_git_simple_workflow.html': {
        'hero_label': ('Lesson 05', 'Lesson 14'),
        'progress':   ('extrabold">7<span class="font-bold opacity-50">/8',
                       'extrabold">14<span class="font-bold opacity-50">/15'),
        'badge':      ('text-lg">6', 'text-lg">15'),
        'mod_label':  ('Module 2 · Lesson 6', 'Module 2 · Lesson 15'),
    },
    'lesson15_logging_basics.html': {
        'hero_label': ('Lesson 06', 'Lesson 15'),
        'progress':   ('extrabold">8<span class="font-bold opacity-50">/8',
                       'extrabold">15<span class="font-bold opacity-50">/15'),
        'badge':      None,   # last lesson — no next-lesson section
        'mod_label':  None,
    },
}

# href renaming pairs for mod_02 content (applied in order — be specific first)
MOD2_HREF_RENAMES = [
    # Fix existing bug: lesson04_refactoring should be lesson03_refactoring
    ('href="lesson04_refactoring_a_script_into_a_class.html"',
     'href="lesson12_refactoring_a_script_into_a_class.html"'),
    ('href="lesson01_introduction_to_classes.html"',
     'href="lesson10_introduction_to_classes.html"'),
    ('href="lesson02_attributes_methods.html"',
     'href="lesson11_attributes_methods.html"'),
    ('href="lesson03_refactoring_a_script_into_a_class.html"',
     'href="lesson12_refactoring_a_script_into_a_class.html"'),
    ('href="lesson04_modules_and_project_structure.html"',
     'href="lesson13_modules_and_project_structure.html"'),
    ('href="lesson05_introduction_to_git_simple_workflow.html"',
     'href="lesson14_introduction_to_git_simple_workflow.html"'),
    ('href="lesson06_logging_basics.html"',
     'href="lesson15_logging_basics.html"'),
]

# ── Previous-nav block to inject for lesson10 ────────────────────────────────
LESSON10_PREV_NAV = '''\
    <a href="lesson09_reading_understanding_errors.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Reading &amp; Understanding Errors</p>
      </div>
    </a>'''

# ── Main processing ───────────────────────────────────────────────────────────
results = []

for lesson_num, (new_fname, toc_label, src_dir) in enumerate(LESSONS, start=1):
    # Resolve source path
    if src_dir == OLD_M2:
        old_fname = MOD2_OLD_NAMES[new_fname]
    else:
        old_fname = new_fname
    src_path = os.path.join(src_dir, old_fname)
    dst_path = os.path.join(NEW_DIR, new_fname)

    if not os.path.exists(src_path):
        print(f'❌ MISSING: {src_path}')
        results.append((new_fname, False, 'source file not found'))
        continue

    with open(src_path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Replace TOC module-lessons block
    c = replace_toc_module_list(c, lesson_num)

    # 2. Lesson 09 — replace entire next-lesson + bottom-nav sections
    if new_fname == 'lesson09_reading_understanding_errors.html':
        old_section = re.search(
            r'<section id="next-lesson".*?</section>\s*\n\s*<section>\s*\n.*?</section>',
            c, re.DOTALL
        )
        if old_section:
            c = c[:old_section.start()] + LESSON09_NEXT_SECTION + c[old_section.end():]
            print(f'  ✅ lesson09: replaced next-lesson + bottom nav')
        else:
            print(f'  ⚠  lesson09: could not find next-lesson section to replace')

    # 3. Mod_01 files — update progress denominator /9 → /15
    if src_dir == OLD_M1:
        before = c
        c = c.replace('opacity-50">/9', 'opacity-50">/15')
        if c == before:
            print(f'  ⚠  {new_fname}: /9 not found in progress pill')

    # 4. Mod_02 files — rename hrefs, update labels, progress, badges
    if src_dir == OLD_M2:
        # 4a. Rename all internal lesson hrefs
        for old_href, new_href in MOD2_HREF_RENAMES:
            c = c.replace(old_href, new_href)

        cfg = MOD2_CONFIG[new_fname]

        # 4b. Hero lesson number label
        old_lbl, new_lbl = cfg['hero_label']
        old_lbl_html = f'<p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">{old_lbl}</p>'
        new_lbl_html = f'<p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">{new_lbl}</p>'
        if old_lbl_html in c:
            c = c.replace(old_lbl_html, new_lbl_html, 1)
        else:
            print(f'  ⚠  {new_fname}: hero label "{old_lbl}" not found')

        # 4c. Progress pill
        old_prog, new_prog = cfg['progress']
        if old_prog in c:
            c = c.replace(old_prog, new_prog, 1)
        else:
            print(f'  ⚠  {new_fname}: progress "{old_prog}" not found')

        # 4d. Next-lesson badge number
        if cfg['badge']:
            old_badge, new_badge = cfg['badge']
            if old_badge in c:
                c = c.replace(old_badge, new_badge, 1)
            else:
                print(f'  ⚠  {new_fname}: badge "{old_badge}" not found')

        # 4e. Next-lesson module label
        if cfg['mod_label']:
            old_ml, new_ml = cfg['mod_label']
            if old_ml in c:
                c = c.replace(old_ml, new_ml, 1)
            else:
                # not a fatal error — some files may not have this label
                pass  # silently skip

        # 4f. Remove "Module 2" hero badge pill (still fine — means Track 2)

        # 4g. lesson10: inject Previous nav, keeping lesson09 progress denominator
        if new_fname == 'lesson10_introduction_to_classes.html':
            # Update denominator /8 → /15 only after numerator fix (done in 4c)
            # Inject Previous nav link
            old_spacer = '    <div class="flex-1"></div>\n\n    <a href="../../../hub_home_page.html"'
            new_spacer = LESSON10_PREV_NAV + '\n\n    <a href="../../../hub_home_page.html"'
            if old_spacer in c:
                c = c.replace(old_spacer, new_spacer, 1)
                print(f'  ✅ lesson10: injected Previous nav link')
            else:
                print(f'  ⚠  lesson10: could not find spacer div to inject Previous nav')

    # Write output
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(c)
    results.append((new_fname, True, 'OK'))

# ── Summary ───────────────────────────────────────────────────────────────────
print('\n' + '='*60)
print(f'Output folder: {NEW_DIR}')
print(f'{"File":<55} {"Status"}')
print('-'*60)
for fname, ok, msg in results:
    icon = '✅' if ok else '❌'
    print(f'{icon} {fname:<53} {msg}')
print(f'\n{sum(1 for _,ok,_ in results if ok)}/{len(results)} files written successfully.')
