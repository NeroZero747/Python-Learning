"""
Rewrites the #overview section body in lesson04_logging_basics.html
following the 4-part structure from lesson-overview.prompt.md.
"""

TARGET = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

# ── Content values ────────────────────────────────────────────────────────────
HOOK_SENTENCE = (
    "Logging is Python\u2019s built-in system for recording what your program "
    "does \u2014 automatically, while it runs."
)

ANALOGY_INTRO = (
    "Think of Python logging like a security guard\u2019s logbook at a building "
    "entrance \u2014 every significant event gets written down with the time it "
    "happened and a note on how serious it was. "
    "A <strong>logging setup</strong> is that logbook, and Python\u2019s "
    "<strong>logging module</strong> is the system that writes in it for you."
)

AMBER_TIP = (
    "If you already track issues in an Excel sheet with a date column and a "
    "severity column, you\u2019ll recognise the pattern \u2014 logging does "
    "the same job automatically, so your scripts document themselves as they run."
)

# ── New body HTML ─────────────────────────────────────────────────────────────
NEW_BODY = f"""<div class="bg-white px-8 py-7 space-y-5">

      <!-- Part 1 — Hook quote banner -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">{HOOK_SENTENCE}</p>
        </div>
      </div>

      <!-- Part 2 — Analogy intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">{ANALOGY_INTRO}</p>

      <!-- Part 3 — Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 — pink accent: Log severity levels -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:layer-group"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Log severity levels</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The urgency stamp \u2014 INFO note or CRITICAL alarm</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Filters which entries are important enough to write down.</p>
        </div>

        <!-- Card 2 — violet accent: The Logger -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
              <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:user-shield"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">The Logger</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The guard \u2014 watches one wing of the building</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Passes each approved entry to the right handler for filing.</p>
        </div>

        <!-- Card 3 — blue accent: Log handlers -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
              <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:folder-open"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Log handlers</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The destination \u2014 logbook, email, or both</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Files each entry into the logbook or sends an alert.</p>
        </div>

        <!-- Card 4 — emerald accent: Log formatters -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
              <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:table-list"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Log formatters</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The template \u2014 timestamp, level, and message</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Sets the exact layout every entry in the logbook must follow.</p>
        </div>

      </div>

      <!-- Part 4 — Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">{AMBER_TIP}</p>
      </div>

    </div>"""

# ── Read file ─────────────────────────────────────────────────────────────────
with open(TARGET, encoding='utf-8') as fh:
    content = fh.read()

# ── Locate the overview section ───────────────────────────────────────────────
sec_start = content.find('<section id="overview">')
if sec_start == -1:
    print('ERROR: <section id="overview"> not found'); exit(1)

# Find the body div opening (within the overview section)
BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-5">'
body_start = content.find(BODY_OPEN, sec_start)
if body_start == -1:
    print(f'ERROR: body div not found in overview section'); exit(1)

# The body div closes just before the rounded-2xl and section closing tags
CLOSING_SEQ = '</div>\n  </div>\n</section>'
closing_pos = content.find(CLOSING_SEQ, body_start)
if closing_pos == -1:
    print('ERROR: closing sequence not found after overview body'); exit(1)

# body_end is right after the body div's </div>
body_end = closing_pos + len('</div>')

OLD_BODY = content[body_start:body_end]

# ── Replace ───────────────────────────────────────────────────────────────────
new_content = content[:body_start] + NEW_BODY + content[body_end:]

with open(TARGET, 'w', encoding='utf-8') as fh:
    fh.write(new_content)

print('Written successfully.')

# ── Verify ────────────────────────────────────────────────────────────────────
with open(TARGET, encoding='utf-8') as fh:
    result = fh.read()

s = result.find('<section id="overview">')
e = result.find('</section>', s) + len('</section>')
section = result[s:e]

checks = [
    ('Hook banner present',          'fa6-solid:quote-left' in section),
    ('items-center on flex row',     'flex items-center gap-4' in section),
    ('No items-start on hook row',   'flex items-start gap-4' not in section),
    ('No mt-0.5 on icon span',       'shadow-md shrink-0">' in section),  # no mt-0.5 between shrink-0 and >
    ('Hook sentence correct',        'Python\u2019s built-in system' in section),
    ('Analogy intro (Think of)',      'Think of Python logging' in section),
    ('4 analogy cards',              section.count('text-xs text-gray-500 leading-relaxed') == 4),
    ('Pink card — fa6-solid:layer-group',   'fa6-solid:layer-group' in section),
    ('Violet card — fa6-solid:user-shield', 'fa6-solid:user-shield' in section),
    ('Blue card — fa6-solid:folder-open',   'fa6-solid:folder-open' in section),
    ('Emerald card — fa6-solid:table-list', 'fa6-solid:table-list' in section),
    ('Amber tip present',            'bg-amber-tip' in section),
    ('Amber tip text correct',       'Excel sheet' in section),
    ('No old code block in overview','bg-[#181825]' not in section),
    ('No old print() text in overview', 'print(' not in section),
    ('space-y-5 class preserved',    'space-y-5' in section),
]

print()
all_ok = True
for label, ok in checks:
    print(f'  {"OK  " if ok else "FAIL"}: {label}')
    if not ok:
        all_ok = False

print()
print('All checks passed.' if all_ok else 'Some checks FAILED — review output above.')
