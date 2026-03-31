TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"

# ── CSS to inject (after .obj-card:hover .obj-icon .iconify line) ──────────────
OLD_CSS = "    .obj-card:hover .obj-icon .iconify { color: white !important; }"
NEW_CSS = """\
    .obj-card:hover .obj-icon .iconify { color: white !important; }
    .obj-card-kt:hover     { box-shadow: none; background-color: #ffffff; border-color: #CB187D; }
    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }
    .obj-card-blue:hover   { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }"""

# ── New #key-ideas body ────────────────────────────────────────────────────────
NEW_BODY = '''\
    <div class="bg-white px-8 py-7 space-y-4">

      <div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
        <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
        <div class="px-6 py-5">
          <div class="flex items-center gap-3 mb-3">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:wrench"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-900">One Fix Updates Every Script</h3>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed mb-4">When you correct a mistake inside a module function, every script that imports it picks up the fix automatically — no hunting through copies pasted into separate files.</p>
          <div class="flex flex-wrap gap-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">no duplication</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">single source</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">easy fixes</span>
          </div>
        </div>
      </div>

      <div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
        <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
        <div class="px-6 py-5">
          <div class="flex items-center gap-3 mb-3">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:table-cells"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-900">Modules Work Like Shared Formulas</h3>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed mb-4">Just as you build a formula once in Excel and reference it across multiple sheets, you write a Python function once in a module and call it from any script that needs it.</p>
          <div class="flex flex-wrap gap-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">reusable</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">write once</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">like Excel</span>
          </div>
        </div>
      </div>

      <div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
        <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
        <div class="px-6 py-5">
          <div class="flex items-center gap-3 mb-3">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:list-check"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-900">Split by Task, Not by Length</h3>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed mb-4">Decide what goes in each module by asking what job the code does — one file for cleaning, one for calculating, one for exporting makes every file easy to find and update.</p>
          <div class="flex flex-wrap gap-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">task-focused</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">structure</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">project layout</span>
          </div>
        </div>
      </div>

    </div>'''

# ── Apply changes ──────────────────────────────────────────────────────────────
html = open(TARGET).read()

# 1. Inject CSS variants
if '.obj-card-kt:hover' in html:
    print('⚠️  CSS variants already present — skipping CSS patch')
else:
    if OLD_CSS not in html:
        print('❌ CSS anchor not found')
        exit(1)
    html = html.replace(OLD_CSS, NEW_CSS, 1)
    print('✅ CSS hover variants added')

# 2. Replace #key-ideas body
sec_start = html.index('<section id="key-ideas">')
sec_end   = html.index('</section>', sec_start) + len('</section>')
section   = html[sec_start:sec_end]

BODY_TAG = '<div class="bg-white px-8 py-7 space-y-4">'
if BODY_TAG not in section:
    print('❌ Body tag not found in #key-ideas section')
    exit(1)

body_rel   = section.index(BODY_TAG)
body_start = sec_start + body_rel

# Depth-count to find matching </div>
pos   = body_start + len(BODY_TAG)
depth = 1
body_end = None
while depth > 0 and pos < len(html):
    next_open  = html.find('<div', pos)
    next_close = html.find('</div>', pos)
    if next_close == -1:
        break
    if next_open != -1 and next_open < next_close:
        depth += 1
        pos = next_open + 4
    else:
        depth -= 1
        if depth == 0:
            body_end = next_close + len('</div>')
        pos = next_close + 6

if body_end is None:
    print('❌ Could not find closing </div> for body')
    exit(1)

old_body = html[body_start:body_end]
html = html[:body_start] + NEW_BODY + html[body_end:]

open(TARGET, 'w').write(html)
print(f'✅ #key-ideas body replaced — {len(old_body):,} chars → {len(NEW_BODY):,} chars')
print(f'   File size: {len(html):,} chars')
