"""Rewrite #overview section body in lesson04 per lesson-overview.prompt.md rules."""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

# ── New body content (inside <div class="bg-white px-8 py-7 space-y-5">) ─────
NEW_BODY = '''\n\n      <!-- Part 1 — Hook quote card -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">Refactoring is the process of reorganising your code to make it cleaner and easier to manage, without changing what the code actually does.</p>
        </div>
      </div>

      <!-- Part 2 — Analogy intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Think of your Python script like a chef&#39;s stack of paper notes — each step written somewhere, but nothing labelled, nothing filed, and nothing a colleague could pick up and follow. A <strong>class</strong> is that recipe book, and Python is the language you use to write it.</p>

      <!-- Part 3 — Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 — pink accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:file-lines"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">The Loose Script</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Loose notes — scattered, unlabelled, unfiled</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Every step scattered across the countertop with no clear structure.</p>
        </div>

        <!-- Card 2 — violet accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
              <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:book-open"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">A Class</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The recipe book — one cover, every step</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Gathers all your loose steps under one named cover.</p>
        </div>

        <!-- Card 3 — blue accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
              <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:bookmark"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">A Method</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">One recipe — filed in the right chapter</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">One named page in the book, ready to call when needed.</p>
        </div>

        <!-- Card 4 — emerald accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
              <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:play"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">The run() Method</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Cook the full meal — start to finish</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">The page that calls every other recipe in the right order.</p>
        </div>

      </div>

      <!-- Part 4 — Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">If you have ever used an Excel macro or a SQL stored procedure that runs steps in a fixed order, you already understand what a class does — it is the same idea applied to your Python scripts.</p>
      </div>

    '''

html = TARGET.read_text(encoding='utf-8')

# ── Locate the overview section body div ──────────────────────────────────────
# Find the whole overview section first
ov_start = html.find('id="overview"')
if ov_start == -1:
    print('❌ id="overview" not found'); sys.exit(1)

# body div marker (unique inside overview)
BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-5">'
body_start = html.find(BODY_OPEN, ov_start)
if body_start == -1:
    print('❌ body div not found'); sys.exit(1)

# Find the matching closing </div> of the body div using depth counting
content_start = body_start + len(BODY_OPEN)
search = html[content_start:]
depth, body_end, i = 1, -1, 0
while i < len(search):
    if search[i:].startswith('<div'):
        depth += 1; i += 4
    elif search[i:].startswith('</div>'):
        depth -= 1
        if depth == 0:
            body_end = content_start + i; break
        i += 6
    else:
        i += 1

if body_end == -1:
    print('❌ Closing </div> of body not found'); sys.exit(1)

old_body = html[content_start:body_end]
print(f'  Old body: {len(old_body):,} chars')
print(f'  New body: {len(NEW_BODY):,} chars')

html = html[:content_start] + NEW_BODY + html[body_end:]
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# ── Verification ──────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding='utf-8')
ov_start = result.find('id="overview"')
sec_start = result.rfind('<section', 0, ov_start)
search2 = result[sec_start:]
depth2, sec_end, i = 0, -1, 0
while i < len(search2):
    if search2[i:].startswith('<section'):
        depth2 += 1; i += len('<section')
    elif search2[i:].startswith('</section>'):
        depth2 -= 1
        if depth2 == 0:
            sec_end = sec_start + i + len('</section>'); break
        i += len('</section>')
    else:
        i += 1
s = result[sec_start:sec_end]

checks = [
    # Part 1 — hook (no analogy, items-center)
    ('Hook: items-center (not items-start)',   'flex items-center gap-4'),
    ('Hook: quote-left icon',                  'fa6-solid:quote-left'),
    ('Hook: no analogy in sentence',           'filing cabinet'),    # must be ABSENT
    ('Hook: plain definition',                 'reorganising your code to make it cleaner'),
    # Part 2 — analogy intro
    ('Analogy: starts with Think of',          'Think of your Python script like'),
    ('Analogy: recipe book domain',            'recipe book'),
    ('Analogy: ends with Python sentence',     'Python is the language you use to write it'),
    # Part 3 — card accents
    ('Card 1 pink: bg-[#fdf0f7]',             'bg-[#fdf0f7] shrink-0'),
    ('Card 2 violet: bg-violet-50',            'bg-violet-50 shrink-0'),
    ('Card 3 blue: bg-blue-50',               'bg-blue-50 shrink-0'),
    ('Card 4 emerald: bg-emerald-50',          'bg-emerald-50 shrink-0'),
    # Card icons
    ('Card 1 icon: file-lines',               'fa6-solid:file-lines'),
    ('Card 2 icon: book-open',                'fa6-solid:book-open'),
    ('Card 3 icon: bookmark',                 'fa6-solid:bookmark'),
    ('Card 4 icon: play',                     'fa6-solid:play'),
    # Card titles
    ('Card 1 title: The Loose Script',        '>The Loose Script<'),
    ('Card 2 title: A Class',                 '>A Class<'),
    ('Card 3 title: A Method',                '>A Method<'),
    ('Card 4 title: The run() Method',        '>The run() Method<'),
    # No <code> in descriptions
    ('No <code> in card descriptions',         '</p>\n          <p class="text-xs text-gray-500'),  # after subtitle
    # Part 4 — amber tip
    ('Amber: circle-info icon',               'fa6-solid:circle-info'),
    ('Amber: Excel/SQL bridge',               'Excel macro'),
    ('Amber: no repeat of analogy',           'recipe book'),  # must be ABSENT from amber only
    # Structure unchanged
    ('space-y-5 preserved',                   'space-y-5'),
    ('Section header unchanged',              'fa6-solid:binoculars'),
]

# Some checks are "must NOT contain" — flag them
must_absent = {
    'Hook: no analogy in sentence',
    'No <code> in card descriptions',
    'Amber: no repeat of analogy',
}

passed, failed = 0, 0
for label, needle in checks:
    if label in must_absent:
        ok = needle not in s
        symbol = '✅' if ok else '❌'
        note = ' (absent ✓)' if ok else ' (FOUND — should be absent)'
    else:
        ok = needle in s
        symbol = '✅' if ok else '❌'
        note = ''
    print(f'  {symbol} {label}{note}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
