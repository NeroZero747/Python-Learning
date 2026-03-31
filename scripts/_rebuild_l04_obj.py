"""
Replace <section id="objective"> in lesson04 with clean, properly-structured content.
Domain: ReportRunner (neutral workflow class, no DataPipeline/ClaimsPipeline).
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="objective" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Learning Objectives</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">What you will be able to do after this lesson</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:arrows-rotate"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">What Refactoring Means</p>
            <p class="text-xs text-gray-500 mt-0.5">Reorganising code structure without changing what the script actually does or produces.</p>
          </div>
        </div>

        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:triangle-exclamation"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Why Scripts Grow Messy</p>
            <p class="text-xs text-gray-500 mt-0.5">Loose functions scattered without structure become harder to read, test, and update as a script grows longer.</p>
          </div>
        </div>

        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:code"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Converting Scripts to Classes</p>
            <p class="text-xs text-gray-500 mt-0.5">Moving related functions into a class gives every step a clear home and a consistent calling pattern.</p>
          </div>
        </div>

        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:layer-group"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Benefits of a Class Structure</p>
            <p class="text-xs text-gray-500 mt-0.5">A class keeps all related steps together, making code easier to reuse and maintain as your project grows.</p>
          </div>
        </div>

      </div>

      <div class="mt-5 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">This lesson shows you how to take messy, growing scripts and turn them into clean, professional Python code.</p>
      </div>
    </div>

  </div>
</section>'''

def replace_section(html, section_id, new_html):
    marker = f'<section id="{section_id}"'
    start = html.find(marker)
    if start == -1:
        marker2 = f'<section id="{section_id} '
        start = html.find(marker2)
    if start == -1:
        print(f'❌ Could not find <section id="{section_id}">')
        return html, False
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
html, ok = replace_section(html, 'objective', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
ov_start = result.find('<section id="objective"')
ov_end   = result.find('<section id="overview"')
slice_   = result[ov_start:ov_end] if ov_start != -1 and ov_end != -1 else result

checks = [
    ("scroll-mt-24 on section",          'class="scroll-mt-24"'),
    ("Section icon bullseye",            'data-icon="fa6-solid:bullseye"'),
    ("Header title Learning Objectives", "Learning Objectives"),
    ("Card 1 icon arrows-rotate",        'data-icon="fa6-solid:arrows-rotate"'),
    ("Card 1 title What Refactoring",    "What Refactoring Means"),
    ("Card 1 description reorganising",  "Reorganising code structure"),
    ("Card 2 icon triangle-excl",        'data-icon="fa6-solid:triangle-exclamation"'),
    ("Card 2 title Why Scripts Grow",    "Why Scripts Grow Messy"),
    ("Card 2 description loose fns",     "Loose functions scattered"),
    ("Card 3 icon code",                 'data-icon="fa6-solid:code"'),
    ("Card 3 title Converting Scripts",  "Converting Scripts to Classes"),
    ("Card 3 description clear home",    "clear home"),
    ("Card 4 icon layer-group",          'data-icon="fa6-solid:layer-group"'),
    ("Card 4 title Benefits",            "Benefits of a Class Structure"),
    ("Card 4 description reuse",         "easier to reuse"),
    ("Amber tip text",                   "turn them into clean, professional Python code"),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle in slice_:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
