"""Rewrite #recap section in lesson04 per lesson-recap.prompt.md.

Objective card values (read from #objective section):
  Card 1: icon=fa6-solid:arrows-rotate       label="What Refactoring Means"
  Card 2: icon=fa6-solid:triangle-exclamation label="Why Scripts Grow Messy"
  Card 3: icon=fa6-solid:code               label="Converting Scripts to Classes"
  Card 4: icon=fa6-solid:layer-group         label="Benefits of a Class Structure"
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_BODY = '''

      <!-- 2×2 recap grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- Card 01 — What Refactoring Means -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:arrows-rotate"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">What Refactoring Means</p>
                <p class="text-[11px] text-gray-600 leading-snug">Refactoring reorganises code structure without changing what the script produces.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 02 — Why Scripts Grow Messy -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Why Scripts Grow Messy</p>
                <p class="text-[11px] text-gray-600 leading-snug">Loose functions without a class get harder to read, test, and update as a script grows.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 03 — Converting Scripts to Classes -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Converting Scripts to Classes</p>
                <p class="text-[11px] text-gray-600 leading-snug">Each function moves inside the <code class="font-mono">class</code> block with <code class="font-mono">self</code> added — no logic changes.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 04 — Benefits of a Class Structure -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:layer-group"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Benefits of a Class Structure</p>
                <p class="text-[11px] text-gray-600 leading-snug">A <code class="font-mono">run()</code> method calls all steps in order — the whole pipeline fires with one call.</p>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Completion banner -->
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
      </div>

    '''

# ── Replace body ───────────────────────────────────────────────────────────────
html = TARGET.read_text(encoding='utf-8')

idx = html.find('id="recap"')
BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-6">'
body_start = html.find(BODY_OPEN, idx)
if body_start == -1:
    print('❌ Body div not found'); sys.exit(1)

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
    print('❌ Closing </div> not found'); sys.exit(1)

old = html[content_start:body_end]
print(f'  Old body: {len(old):,} chars')
print(f'  New body: {len(NEW_BODY):,} chars')

html = html[:content_start] + NEW_BODY + html[body_end:]
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# ── Verification ───────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding='utf-8')
idx2 = result.find('id="recap"')
sec_s = result.rfind('<section', 0, idx2)
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
    ('Shell: id="recap"',                          'id="recap"'),
    ('Shell: fa6-solid:list-check icon',           'data-icon="fa6-solid:list-check"'),
    ('Shell: Lesson Recap title',                  '>Lesson Recap<'),
    ('Shell: subtitle preserved',                  'A quick summary of what you learned'),
    # Card structure — label + sentence divs (4 labels)
    ('Cards: uppercase pink label ×4',             s.count('text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1') == 4),
    ('Cards: text-[11px] sentence ×4',             s.count('text-[11px] text-gray-600 leading-snug') == 4),
    ('Cards: two-part div structure ×4',           s.count('class="relative flex items-start gap-3"') >= 4),
    # Watermarks
    ('Watermark 01',                               '>01<'),
    ('Watermark 02',                               '>02<'),
    ('Watermark 03',                               '>03<'),
    ('Watermark 04',                               '>04<'),
    # Icons — match objectives exactly
    ('Card 1 icon: fa6-solid:arrows-rotate',       'data-icon="fa6-solid:arrows-rotate"'),
    ('Card 2 icon: fa6-solid:triangle-exclamation','data-icon="fa6-solid:triangle-exclamation"'),
    ('Card 3 icon: fa6-solid:code',                s.count('data-icon="fa6-solid:code"') >= 1),
    ('Card 4 icon: fa6-solid:layer-group',         'data-icon="fa6-solid:layer-group"'),
    # Labels — exact match to objectives
    ('Label 1: What Refactoring Means',            '>What Refactoring Means<'),
    ('Label 2: Why Scripts Grow Messy',            '>Why Scripts Grow Messy<'),
    ('Label 3: Converting Scripts to Classes',     '>Converting Scripts to Classes<'),
    ('Label 4: Benefits of a Class Structure',     '>Benefits of a Class Structure<'),
    # Sentences — no label repeated verbatim as opening
    ('Sentence 1 starts with Refactoring',         'Refactoring reorganises code structure'),
    ('Sentence 2: harder to read, test, and update','harder to read, test, and update'),
    ('Sentence 3: class block + self',             'inside the'),
    ('Sentence 4: run() calls all steps',          'calls all steps in order'),
    # Inline code in sentences
    ('Inline code: class',                         '<code class="font-mono">class</code>'),
    ('Inline code: self',                          '<code class="font-mono">self</code>'),
    ('Inline code: run()',                         '<code class="font-mono">run()</code>'),
    # No old paragraph structure
    ('Old text-sm text-gray-700 gone',             'text-sm text-gray-700 font-medium leading-relaxed' not in s),
    # Completion banner
    ('Banner: trophy icon',                        'fa6-solid:trophy'),
    ('Banner: Lesson Complete!',                   '>Lesson Complete!<'),
    ("Banner: You've covered 4",                   "You&#39;ve covered 4 key concepts"),
    ('Banner: &#10003; checkmark',                 '&#10003;'),
    ('Banner: bg-gradient-to-r from-[#CB187D]',   'bg-gradient-to-r from-[#CB187D] to-[#e84aad]'),
    # Card hover styles preserved
    ('Cards: hover:border-[#f5c6e0] ×4',          s.count('hover:border-[#f5c6e0]') == 4),
    # Icon badge gradient ×4
    ('Icon badge: from-[#CB187D] to-[#e84aad] ×4', s.count('from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5') == 4),
]

passed, failed = 0, 0
for label, check in checks:
    ok = check if isinstance(check, bool) else (check in s)
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
