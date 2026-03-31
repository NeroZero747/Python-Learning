"""
Replace <section id="key-ideas"> in lesson04.
3 coloured cards (pink/violet/blue) with keyword pills.
No DataPipeline/ClaimsPipeline references.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="key-ideas" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:lightbulb"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Takeaways</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The most important ideas to remember from this lesson</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-4">

      <!-- Card 1 — Pink: Refactoring Keeps the Same Result -->
      <div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
        <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
        <div class="px-6 py-5">
          <div class="flex items-center gap-3 mb-3">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:arrows-rotate"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-900">Refactoring Keeps the Same Result</h3>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed mb-4">When you refactor a script, the output stays exactly the same — only the organisation changes, which means your improvement is completely invisible to anyone who runs your code.</p>
          <div class="flex flex-wrap gap-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Same output</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Safer changes</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">No new bugs</span>
          </div>
        </div>
      </div>

      <!-- Card 2 — Violet: Classes Remove Call-Order Guesswork -->
      <div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
        <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
        <div class="px-6 py-5">
          <div class="flex items-center gap-3 mb-3">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:sitemap"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-900">Classes Remove Call-Order Guesswork</h3>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed mb-4">A loose script forces you to call functions in exactly the right sequence every time — a class with a <code class="font-mono">run()</code> method handles that sequence automatically, so you never have to remember which step comes first.</p>
          <div class="flex flex-wrap gap-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">run() method</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Step order</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Automatic</span>
          </div>
        </div>
      </div>

      <!-- Card 3 — Blue: One Object Replaces Many Calls -->
      <div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
        <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
        <div class="px-6 py-5">
          <div class="flex items-center gap-3 mb-3">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:layer-group"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-900">One Object Replaces Many Calls</h3>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed mb-4">Instead of calling five separate functions scattered across a script, you create one object and call <code class="font-mono">run()</code> once — keeping your main code short, clean, and easy to hand to a colleague.</p>
          <div class="flex flex-wrap gap-2">
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Single object</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Cleaner code</span>
            <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Reusable</span>
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
html, ok = replace_section(html, 'key-ideas', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
ki_start = result.find('<section id="key-ideas"')
kc_start = result.find('<section id="key-concepts"')
slice_   = result[ki_start:kc_start] if ki_start != -1 and kc_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon lightbulb",                      'data-icon="fa6-solid:lightbulb"'),
    ("Header title Key Takeaways",          ">Key Takeaways<"),
    ("Card 1: obj-card-kt",                 "obj-card-kt"),
    ("Card 1: pink gradient top bar",       "from-[#CB187D] to-[#e84aad]"),
    ("Card 1: arrows-rotate icon",          'data-icon="fa6-solid:arrows-rotate"'),
    ("Card 1: title",                       "Refactoring Keeps the Same Result"),
    ("Card 1: description output",          "output stays exactly the same"),
    ("Card 1: pill Same output",            "Same output"),
    ("Card 1: pill Safer changes",          "Safer changes"),
    ("Card 1: pill No new bugs",            "No new bugs"),
    ("Card 2: obj-card-violet",             "obj-card-violet"),
    ("Card 2: violet gradient top bar",     "from-violet-500 to-purple-400"),
    ("Card 2: sitemap icon",                'data-icon="fa6-solid:sitemap"'),
    ("Card 2: title",                       "Classes Remove Call-Order Guesswork"),
    ("Card 2: description sequence",        "handles that sequence automatically"),
    ("Card 2: pill run() method",           "run() method"),
    ("Card 2: pill Step order",             "Step order"),
    ("Card 3: obj-card-blue",               "obj-card-blue"),
    ("Card 3: blue gradient top bar",       "from-blue-500 to-indigo-400"),
    ("Card 3: layer-group icon",            'data-icon="fa6-solid:layer-group"'),
    ("Card 3: title",                       "One Object Replaces Many Calls"),
    ("Card 3: description one object",      "create one object"),
    ("Card 3: pill Single object",          "Single object"),
    ("Card 3: pill Reusable",               "Reusable"),
    ("No DataPipeline refs",                True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        found = "DataPipeline" not in slice_
        print(f'  {"✅" if found else "❌"} {label}')
        (passed if found else failed).__class__  # just increment
        if found: passed += 1
        else: failed += 1
    elif needle in slice_:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
