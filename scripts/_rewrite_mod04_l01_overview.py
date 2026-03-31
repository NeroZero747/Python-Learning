TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"

NEW_BODY = '''\
    <div class="bg-white px-8 py-7 space-y-5">

      <!-- Part 1 — Hook quote banner -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">A Python module is a separate file where you store functions that any script in your project can share.</p>
        </div>
      </div>

      <!-- Part 2 — Analogy intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Think of your Python project as a workshop where every script shares the same toolbox. Instead of copying the same tool onto every workbench, you store it once and pick it up whenever you need it. A <strong>module</strong> is that toolbox, and Python is the language you use to fill it.</p>

      <!-- Part 3 — Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 — pink accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:toolbox"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">The Module File</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The toolbox — one shared box for the whole workshop</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">One file on the shelf, ready for any script to reach into.</p>
        </div>

        <!-- Card 2 — violet accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
              <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:arrow-right-from-bracket"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Moving Functions Out</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Packing the box — tools off your workbench</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Move shared tools into the box so your main workbench stays clear.</p>
        </div>

        <!-- Card 3 — blue accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
              <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:layer-group"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Organizing Your Project</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The workshop — each toolbox in its own corner</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Each toolbox covers one task, so the whole workshop stays tidy.</p>
        </div>

        <!-- Card 4 — emerald accent -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
              <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:arrow-right-to-bracket"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">The import Statement</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Grabbing a tool — bring it straight to your bench</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Reach into the toolbox and pull exactly the tool your script needs.</p>
        </div>

      </div>

      <!-- Part 4 — Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">If you already use separate spreadsheet tabs to keep different types of data apart, you are following the same idea — modules do the same thing for your Python functions.</p>
      </div>

    </div>'''

html = open(TARGET).read()

# Find the overview section boundaries
sec_start = html.index('<section id="overview">')
sec_end   = html.index('</section>', sec_start) + len('</section>')
section   = html[sec_start:sec_end]

# Find the body div within the section
body_open  = section.index('<div class="bg-white px-8 py-7 space-y-5">')
body_start = sec_start + body_open
body_tag   = '<div class="bg-white px-8 py-7 space-y-5">'

# Depth-count to find the matching closing </div>
pos   = body_start + len(body_tag)
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
new_html = html[:body_start] + NEW_BODY + html[body_end:]

open(TARGET, 'w').write(new_html)
print(f'✅ Written — {len(new_html):,} chars')
print(f'   Old body: {len(old_body):,} chars  →  New body: {len(NEW_BODY):,} chars')
