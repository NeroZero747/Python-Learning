"""Rewrite #real-world section in lesson04 per lesson-real-world.prompt.md."""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

# ── Header fixes ──────────────────────────────────────────────────────────────
OLD_HEADER_TITLE = '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Real-World Applications</h2>\n        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Where you will use this refactoring pattern in professional Python projects</p>'
NEW_HEADER_TITLE = '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Real-World Use</h2>\n        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How classes are used across real-world data workflows</p>'

# ── New body ──────────────────────────────────────────────────────────────────
NEW_BODY = '''

      <!-- Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Every data team has reports that need to run on a schedule — loading fresh data, cleaning it, and saving the output. Without a class, that workflow is a set of loose functions you have to call in the right order every time. A class bundles the whole pipeline into one object so you can trigger all the steps with a single clean call.</p>

      <!-- Three scenario cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

        <!-- Card 1 — violet -->
        <div class="relative rounded-2xl overflow-hidden border border-violet-100 bg-gradient-to-br from-violet-50 via-white to-purple-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-lg shadow-violet-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-solid:chart-line"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">Your team runs<br>30 reports a week</h3>
            <p class="text-xs text-gray-500 leading-relaxed">Each report needs the same three steps run in the same order every time. You write <code class="font-mono text-violet-700">ReportRunner</code> once, and every report runs cleanly without anyone needing to remember the sequence.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-violet-100 border border-violet-200">
              <span class="iconify text-violet-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-violet-700">returns <code class="font-mono">pipeline complete</code></span>
            </div>
          </div>
        </div>

        <!-- Card 2 — pink (brand) -->
        <div class="relative rounded-2xl overflow-hidden border border-pink-100 bg-gradient-to-br from-pink-50 via-white to-rose-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-lg shadow-pink-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-solid:user-plus"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">A new analyst joins<br>the team tomorrow</h3>
            <p class="text-xs text-gray-500 leading-relaxed">Without a class, they must read the whole script to learn which functions to call and in what order. They call <code class="font-mono text-[#CB187D]">report.run()</code> and the full pipeline completes — zero guesswork.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-pink-100 border border-pink-200">
              <span class="iconify text-[#CB187D] text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-[#CB187D]">returns <code class="font-mono">3 steps, 1 call</code></span>
            </div>
          </div>
        </div>

        <!-- Card 3 — emerald -->
        <div class="relative rounded-2xl overflow-hidden border border-emerald-100 bg-gradient-to-br from-emerald-50 via-white to-teal-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-lg shadow-emerald-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-solid:code-branch"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">Six pipelines share<br>the same logic</h3>
            <p class="text-xs text-gray-500 leading-relaxed">Six different reports all need loading, cleaning, and saving. You create six <code class="font-mono text-emerald-700">ReportRunner()</code> objects — each runs independently using the exact same class with no duplicate code.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-emerald-100 border border-emerald-200">
              <span class="iconify text-emerald-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-emerald-700">returns <code class="font-mono">6 objects, 1 class</code></span>
            </div>
          </div>
        </div>

      </div>

      <!-- Before / After comparison table -->
      <div class="rounded-xl border border-gray-100 overflow-hidden">
        <div class="grid grid-cols-2">

          <!-- Without column -->
          <div class="border-r border-gray-100">
            <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">
              <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>
              <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without a class</p>
            </div>
            <div class="px-4 py-4 space-y-3">
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500 leading-relaxed">Running 30 reports means calling three loose functions in the right order 30 separate times — one wrong call breaks the output.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500 leading-relaxed">A new analyst has to read the whole script to discover which functions exist, what order they go in, and what each one depends on.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500 leading-relaxed">Six similar pipelines mean six copies of the same load/clean/save logic — one bug fix must be made in six different places.</p>
              </div>
            </div>
          </div>

          <!-- With column -->
          <div>
            <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">
              <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>
              <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With a class</p>
            </div>
            <div class="px-4 py-4 space-y-3">
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">ReportRunner</strong> bundles all three steps — create one object per report and the sequence is always correct.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">report.run()</strong> is the only call a new analyst needs to make — the class handles the order and dependencies internally.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500 leading-relaxed">Fix the logic once inside <strong class="text-gray-700">ReportRunner</strong> and all six objects immediately use the corrected code.</p>
              </div>
            </div>
          </div>

        </div>
      </div>

    '''

# ── Apply changes ──────────────────────────────────────────────────────────────
html = TARGET.read_text(encoding='utf-8')

# 1. Fix section header title + subtitle
if OLD_HEADER_TITLE not in html:
    print('❌ Old header title not found'); sys.exit(1)
html = html.replace(OLD_HEADER_TITLE, NEW_HEADER_TITLE, 1)
print('  ✅ Header title + subtitle updated')

# 2. Find body div (space-y-6 in this section)
idx = html.find('id="real-world"')
BODY_OPEN_6 = '<div class="bg-white px-8 py-7 space-y-6">'
BODY_OPEN_5 = '<div class="bg-white px-8 py-7 space-y-5">'
body_start = html.find(BODY_OPEN_6, idx)
if body_start != -1 and body_start < idx + 2000:
    html = html[:body_start] + BODY_OPEN_5 + html[body_start + len(BODY_OPEN_6):]
    print('  ✅ space-y-6 → space-y-5')

# 3. Replace body
idx2 = html.find('id="real-world"')
body_start2 = html.find(BODY_OPEN_5, idx2)
if body_start2 == -1:
    print('❌ body div not found'); sys.exit(1)

content_start = body_start2 + len(BODY_OPEN_5)
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
    print('❌ Closing </div> not found'); sys.exit(1)

old = html[content_start:body_end]
print(f'  Old body: {len(old):,} chars')
print(f'  New body: {len(NEW_BODY):,} chars')

html = html[:content_start] + NEW_BODY + html[body_end:]
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# ── Verification ───────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding='utf-8')
idx3 = result.find('id="real-world"')
sec_s = result.rfind('<section', 0, idx3)
search2 = result[sec_s:]
depth2, sec_e, i = 0, -1, 0
while i < len(search2):
    if search2[i:].startswith('<section'): depth2 += 1; i += len('<section')
    elif search2[i:].startswith('</section>'):
        depth2 -= 1
        if depth2 == 0: sec_e = sec_s + i + len('</section>'); break
        i += len('</section>')
    else: i += 1
s = result[sec_s:sec_e]

checks = [
    # Shell preserved
    ('Shell: id="real-world"',                      'id="real-world"'),
    ('Shell: fa6-solid:briefcase icon',             'data-icon="fa6-solid:briefcase"'),
    ('Shell: Real-World Use title',                 '>Real-World Use<'),
    ('Shell: subtitle updated',                     'How classes are used across real-world data workflows'),
    ('Shell: old title gone',                       'Real-World Applications' not in s),
    # Body wrapper
    ('Body: space-y-5',                             'bg-white px-8 py-7 space-y-5'),
    ('Body: no space-y-6',                          'bg-white px-8 py-7 space-y-6' not in s),
    # Intro paragraph
    ('Intro: data team',                            'Every data team has reports'),
    ('Intro: no code block',                        '<pre' not in s),
    # Cards — three distinct colors
    ('Card 1: violet border',                       'border-violet-100'),
    ('Card 1: violet icon gradient',                'from-violet-500 to-purple-600'),
    ('Card 1: chart-line icon',                     'fa6-solid:chart-line'),
    ('Card 1: headline "30 reports"',               '30 reports a week'),
    ('Card 1: returns pill violet',                 'bg-violet-100'),
    ('Card 1: pipeline complete',                   'pipeline complete'),
    ('Card 2: pink border',                         'border-pink-100'),
    ('Card 2: brand gradient',                      'from-[#CB187D] to-[#e84aad]'),
    ('Card 2: user-plus icon',                      'fa6-solid:user-plus'),
    ('Card 2: headline "new analyst"',              'A new analyst joins'),
    ('Card 2: returns pill pink',                   'bg-pink-100'),
    ('Card 2: 3 steps 1 call',                      '3 steps, 1 call'),
    ('Card 3: emerald border',                      'border-emerald-100'),
    ('Card 3: emerald icon gradient',               'from-emerald-500 to-teal-600'),
    ('Card 3: code-branch icon',                    'fa6-solid:code-branch'),
    ('Card 3: headline "Six pipelines"',            'Six pipelines share'),
    ('Card 3: returns pill emerald',                'bg-emerald-100'),
    ('Card 3: 6 objects 1 class',                   '6 objects, 1 class'),
    # All cards: icon badge w-14 h-14
    ('Cards: w-14 h-14 × 3',                       s.count('w-14 h-14') == 3),
    # All cards: returns icon
    ('Cards: arrow-right-from-bracket × 3',        s.count('fa6-solid:arrow-right-from-bracket') == 3),
    # Before/After table
    ('Table: Without a class header',              '>Without a class<'),
    ('Table: With a class header',                 '>With a class<'),
    ('Table: bg-red-50 header',                    'bg-red-50'),
    ('Table: bg-[#fdf0f7] header',                 'bg-[#fdf0f7]'),
    ('Table: circle-xmark icon',                   'fa6-solid:circle-xmark'),
    ('Table: circle-check icon',                   'fa6-solid:circle-check'),
    ('Table: 3 × xmark rows',                      s.count('data-icon="fa6-solid:xmark"') == 3),
    ('Table: 3 × check rows',                      s.count('data-icon="fa6-solid:check"') == 3),
    # Without rows content
    ('Without row 1: 30 reports',                  '30 separate times'),
    ('Without row 2: new analyst',                 'A new analyst has to read the whole script'),
    ('Without row 3: six places',                  'six different places'),
    # With rows — bold function names
    ('With row 1: <strong>ReportRunner</strong>',  '<strong class="text-gray-700">ReportRunner</strong>'),
    ('With row 2: <strong>report.run()</strong>',  '<strong class="text-gray-700">report.run()</strong>'),
    ('With row 3: <strong>ReportRunner</strong> fix', 'Fix the logic once inside <strong class="text-gray-700">ReportRunner</strong>'),
    # No code blocks
    ('No <pre> blocks',                            '<pre' not in s),
    # Old content gone
    ('Old content gone: code-example class',       'code-example' not in s),
]

passed, failed = 0, 0
for label, check in checks:
    ok = check if isinstance(check, bool) else (check in s)
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
