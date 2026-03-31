"""
Replace <section id="recap"> in lesson04.
4 recap cards mirroring the #objective section exactly:
  01 arrows-rotate — What Refactoring Means
  02 triangle-exclamation — Why Scripts Grow Messy
  03 code — Converting Scripts to Classes
  04 layer-group — Benefits of a Class Structure
Plus: completion banner.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="recap" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:list-check"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Recap</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The four things you learned in this lesson</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

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
              <p class="text-sm text-gray-700 font-medium leading-relaxed">Refactoring means reorganising the structure of your code without changing what the script actually does or the output it produces.</p>
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
              <p class="text-sm text-gray-700 font-medium leading-relaxed">Loose functions scattered without structure become harder to read, test, and update as a script grows longer — a class solves that by giving every step a clear home.</p>
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
              <p class="text-sm text-gray-700 font-medium leading-relaxed">Converting a script into a class means moving each function inside the <code class="font-mono text-xs">class</code> block and adding <code class="font-mono text-xs">self</code> as the first parameter — the function logic itself stays the same.</p>
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
              <p class="text-sm text-gray-700 font-medium leading-relaxed">A class with a <code class="font-mono text-xs">run()</code> method keeps all steps together in one place and reduces your calling code to just two lines — making the script easier to reuse, test, and maintain.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- Completion banner -->
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">✓</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You have covered 4 key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
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
        elif search[i:].startswith('</section>'):
            depth -= 1
            if depth == 0:
                end = start + i + len('</section>'); break
            i += len('</section>')
        else:
            i += 1
    if end == -1:
        print(f'❌ No closing </section> for #{section_id}'); return html, False
    old = html[start:end]
    print(f'  Old #{section_id}: {len(old):,} chars')
    print(f'  New #{section_id}: {len(new_html):,} chars')
    return html[:start] + new_html + html[end:], True

html = TARGET.read_text(encoding='utf-8')
html, ok = replace_section(html, 'recap', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
se_start = result.find('<section id="recap"')
nx_start = result.find('<section id="knowledge-check"')
s = result[se_start:nx_start] if se_start != -1 and nx_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon fa6-solid:list-check",           'data-icon="fa6-solid:list-check"'),
    ("Header: Lesson Recap",                ">Lesson Recap<"),
    ("4 recap cards (grid divs)",           4),
    ("Card 01 watermark",                   ">01<"),
    ("Card 02 watermark",                   ">02<"),
    ("Card 03 watermark",                   ">03<"),
    ("Card 04 watermark",                   ">04<"),
    ("Icon: arrows-rotate",                 'data-icon="fa6-solid:arrows-rotate"'),
    ("Icon: triangle-exclamation",          'data-icon="fa6-solid:triangle-exclamation"'),
    ("Icon: code",                          'data-icon="fa6-solid:code"'),
    ("Icon: layer-group",                   'data-icon="fa6-solid:layer-group"'),
    ("Card 01 text: Refactoring means",     "Refactoring means reorganising"),
    ("Card 02 text: Loose functions",       "Loose functions scattered"),
    ("Card 03 text: self as first param",   "self"),
    ("Card 04 text: run() method",          "run()"),
    ("Completion banner present",           "Lesson Complete!"),
    ("Trophy icon",                         'data-icon="fa6-solid:trophy"'),
    ("4 key concepts count",                "4 key concepts"),
    ("No ETL/ELT refs",                     True),
    ("No DataPipeline refs",                True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        label_map = {
            "No ETL/ELT refs": "ETL",
            "No DataPipeline refs": "DataPipeline",
        }
        term = label_map.get(label, "")
        ok2 = term not in s
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        # Count the recap card divs by their watermark pattern
        count = s.count('text-[5rem] font-black text-[#CB187D]/[0.04]')
        ok3 = count >= needle
        print(f'  {"✅" if ok3 else "❌"} {label} (found {count})')
        if ok3: passed += 1
        else: failed += 1
    elif needle in s:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
