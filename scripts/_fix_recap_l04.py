"""
Rewrite the #recap section body in lesson04 to mirror the #objective cards.
"""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

OLD_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4"><div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="fa6-solid:check"></span>
      </span>
      <p class="text-sm text-gray-700 font-medium leading-relaxed">lists store ordered collections of values</p>
    </div>
  </div>
</div>
<div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="fa6-solid:check"></span>
      </span>
      <p class="text-sm text-gray-700 font-medium leading-relaxed">dictionaries store key-value pairs</p>
    </div>
  </div>
</div>
<div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="fa6-solid:check"></span>
      </span>
      <p class="text-sm text-gray-700 font-medium leading-relaxed">lists use indexes to access data</p>
    </div>
  </div>
</div>
<div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="fa6-solid:check"></span>
      </span>
      <p class="text-sm text-gray-700 font-medium leading-relaxed">dictionaries use keys to retrieve values</p>
    </div>
  </div>
</div>
</div>
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
    </div>
  </div>
</section>'''

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- Card 01 — Lists: ordered data collections -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:list"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Lists: ordered data collections</p>
                <p class="text-[11px] text-gray-600 leading-snug">Use <code class="font-mono">[]</code> to store claim amounts, member IDs, or procedure codes in a fixed order.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 02 — Dictionaries: key-value pairs -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:book-open"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Dictionaries: key-value pairs</p>
                <p class="text-[11px] text-gray-600 leading-snug">A <code class="font-mono">dict</code> holds a record's named fields — like a provider's NPI, specialty, and city.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 03 — Reading values by index or key -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:magnifying-glass"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Reading values by index or key</p>
                <p class="text-[11px] text-gray-600 leading-snug">Fetch the first item with <code class="font-mono">[0]</code>, or any named field with <code class="font-mono">["key"]</code>.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 04 — Link to SQL tables and Excel -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:table-columns"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Link to SQL tables and Excel</p>
                <p class="text-[11px] text-gray-600 leading-snug">Lists map to SQL columns; dictionaries map to table rows or spreadsheet records.</p>
              </div>
            </div>
          </div>
        </div>

      </div>
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
    </div>
  </div>
</section>'''

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

if OLD_BODY not in content:
    print("❌ OLD_BODY not found — check whitespace or content")
else:
    new_content = content.replace(OLD_BODY, NEW_BODY, 1)
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ #recap body replaced")

# --- Verify ---
with open(TARGET, 'r', encoding='utf-8') as f:
    c = f.read()

import re

sec_start = c.index('<section id="recap">')
sec_end   = c.index('<section id="knowledge-check">', sec_start)
section   = c[sec_start:sec_end]

checks = [
    ("Section header icon unchanged (list-check)",   'data-icon="fa6-solid:list-check"' in section),
    ("Header title unchanged (Lesson Recap)",         '>Lesson Recap<' in section),
    ("Card 01 watermark",                             '>01<' in section),
    ("Card 02 watermark",                             '>02<' in section),
    ("Card 03 watermark",                             '>03<' in section),
    ("Card 04 watermark",                             '>04<' in section),
    ("Card 01 icon matches objective (fa6-solid:list)",            'data-icon="fa6-solid:list"' in section),
    ("Card 02 icon matches objective (fa6-solid:book-open)",       'data-icon="fa6-solid:book-open"' in section),
    ("Card 03 icon matches objective (fa6-solid:magnifying-glass)",'data-icon="fa6-solid:magnifying-glass"' in section),
    ("Card 04 icon matches objective (fa6-solid:table-columns)",   'data-icon="fa6-solid:table-columns"' in section),
    ("Card 01 label text",   'Lists: ordered data collections' in section),
    ("Card 02 label text",   'Dictionaries: key-value pairs' in section),
    ("Card 03 label text",   'Reading values by index or key' in section),
    ("Card 04 label text",   'Link to SQL tables and Excel' in section),
    ("No generic fa6-solid:check icons in cards",    section.count('data-icon="fa6-solid:check"') == 0),
    ("Label class present (uppercase tracking-widest)", 'text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1' in section),
    ("Sentence class present (text-[11px])",         'text-[11px] text-gray-600 leading-snug' in section),
    ("Code tag for [] in card 1",                    '<code class="font-mono">[]</code>' in section),
    ("Code tag for dict in card 2",                  '<code class="font-mono">dict</code>' in section),
    ("Code tag for [0] in card 3",                   '<code class="font-mono">[0]</code>' in section),
    ("Code tag for [\"key\"] in card 3",             '<code class="font-mono">["key"]</code>' in section),
    ("Completion banner present",                    'Lesson Complete!' in section),
    ("Banner concept count = 4",                     'covered 4 key concepts' in section),
    ("Trophy icon present",                          'data-icon="fa6-solid:trophy"' in section),
]

all_pass = True
for label, result in checks:
    status = "YES" if result else "NO "
    if not result:
        all_pass = False
    print(f"  {status}: {label}")

print()
if all_pass:
    print("All checks passed!")
else:
    print("Some checks FAILED — review above.")
