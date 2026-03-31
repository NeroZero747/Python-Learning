"""
Replace <section id="overview"> in lesson04.
4-part structure: hook quote | analogy paragraph | 2x2 card grid | amber tip.
Analogy domain: sticky notes / labelled folder.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="overview" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:binoculars"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Overview</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">What refactoring is and why it matters</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-5">

      <!-- Part 1 — Hook quote card -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">Refactoring means improving the shape of your code without changing what it does — like reorganising a filing cabinet without changing the documents inside.</p>
        </div>
      </div>

      <!-- Part 2 — Analogy intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Think of your Python script like a stack of loose sticky notes left on your desk — each note has one task written on it, but there is no label, no order, and no clear way to know which note belongs with which job. Refactoring into a class is like gathering all those notes into a neatly labelled folder, with every task sorted into the right section and ready to run in the correct sequence.</p>

      <!-- Part 3 — Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:file-lines"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">The Loose Script</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Sticky notes scattered across the desk</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">When you write functions one after another with no grouping, the script works — but it becomes harder to navigate and update as it grows longer and more complex.</p>
        </div>

        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:folder-open"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">The Class</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">A labelled folder with everything sorted</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">A class groups all the related functions under one shared name, so you know exactly where each step lives and can call them in a predictable order.</p>
        </div>

        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:note-sticky"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">A Method</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">One note filed in the right folder section</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">A method is a function that has been moved inside a class. It gains the <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">self</code> keyword so Python knows which object it belongs to.</p>
        </div>

        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:play"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Calling run()</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Flipping the folder from start to finish</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">A <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">run()</code> method calls all the other steps in the right order — so the rest of your code only needs one line to trigger everything.</p>
        </div>

      </div>

      <!-- Part 4 — Closing amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Once you learn to refactor, you can revisit a script months later and understand exactly what it does — because the shape of the code tells the story for you.</p>
      </div>

    </div>
  </div>
</section>'''

def replace_section(html, section_id, new_html):
    marker = f'<section id="{section_id}"'
    start = html.find(marker)
    if start == -1:
        print(f'❌ Could not find <section id="{section_id}">'); return html, False
    search = html[start:]
    depth, end, i = 0, -1, 0
    while i < len(search):
        if search[i:].startswith('<section'):
            depth += 1; i += len('<section')
        elif search[i:].startswith('</section'):
            depth -= 1
            if depth == 0:
                end = start + i + len('</section>'); break
            i += len('</section')
        else:
            i += 1
    if end == -1:
        print(f'❌ No closing </section> for #{section_id}'); return html, False
    old = html[start:end]
    print(f'  Old #{section_id}: {len(old):,} chars')
    print(f'  New #{section_id}: {len(new_html):,} chars')
    return html[:start] + new_html + html[end:], True

html = TARGET.read_text(encoding='utf-8')
html, ok = replace_section(html, 'overview', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
ov_start = result.find('<section id="overview"')
ki_start = result.find('<section id="key-ideas"')
slice_   = result[ov_start:ki_start] if ov_start != -1 and ki_start != -1 else result

checks = [
    ("scroll-mt-24 on section",             'class="scroll-mt-24"'),
    ("Section icon binoculars",             'data-icon="fa6-solid:binoculars"'),
    ("Header title Overview",               ">Overview<"),
    ("Part 1: items-center on flex",        "flex items-center gap-4"),
    ("Part 1: quote-left icon",             'data-icon="fa6-solid:quote-left"'),
    ("Part 1: hook quote text",             "improving the shape of your code"),
    ("Part 2: Think of analogy",            "Think of your Python script like"),
    ("Part 2: sticky notes",                "sticky notes"),
    ("Part 2: labelled folder",             "labelled folder"),
    ("Card 1: Loose Script",                "The Loose Script"),
    ("Card 1: file-lines icon",             'data-icon="fa6-solid:file-lines"'),
    ("Card 1: analogy subtitle",            "Sticky notes scattered"),
    ("Card 2: The Class",                   "The Class"),
    ("Card 2: folder-open icon",            'data-icon="fa6-solid:folder-open"'),
    ("Card 2: analogy subtitle folder",     "labelled folder with everything sorted"),
    ("Card 3: A Method",                    "A Method"),
    ("Card 3: note-sticky icon",            'data-icon="fa6-solid:note-sticky"'),
    ("Card 3: self code tag",               '<code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">self</code>'),
    ("Card 4: Calling run()",               "Calling run()"),
    ("Card 4: play icon",                   'data-icon="fa6-solid:play"'),
    ("Card 4: run() code tag",              '<code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">run()</code>'),
    ("Amber tip: revisit a script",         "revisit a script months later"),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle in slice_:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
