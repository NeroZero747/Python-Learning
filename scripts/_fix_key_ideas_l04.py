"""Replace the #key-ideas section body in lesson04 with the correct 3-card Key Takeaways template."""

TARGET = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html'

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the key-ideas section boundaries
ki_start = content.index('id="key-ideas"')
kc_start = content.index('id="key-concepts"', ki_start)

# Locate the section body div start
body_marker = '<div class="bg-white px-8 py-7 space-y-4">'
body_start = content.index(body_marker, ki_start)

# Locate the section body div end — it closes with \n  </div>\n</section> (the wrapper + section)
closing = '\n  </div>\n</section>'
closing_pos = content.rindex(closing, ki_start, kc_start)

NEW_BODY = '''<div class="bg-white px-8 py-7 space-y-4">

<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:hashtag"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Indexes Start at Zero</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Python counts list positions from 0, so the first item in any list is at index 0 and the last item sits at index length-minus-one.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Zero-based</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">First is [0]</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Last is [n-1]</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:scale-balanced"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Choose List or Dictionary Wisely</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Use a list when order matters, like a column of monthly figures; use a dictionary when each value needs a label, like a named column in a SQL table.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Ordered sequence</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Named lookup</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Data structure</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:database"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Real Data Arrives in Both Forms</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Every API response, database query result, and Excel import you process in Python arrives as a list, a dictionary, or a combination of both structures.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">API responses</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">SQL rows</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">JSON data</span>
    </div>
  </div>
</div>

</div>'''

result = content[:body_start] + NEW_BODY + content[closing_pos:]

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(result)

print('✅ Replaced #key-ideas body')

# Verify
with open(TARGET, 'r', encoding='utf-8') as f:
    check = f.read()

tests = [
    ('Pink card present',       'obj-card-kt rounded-2xl border border-gray-100' in check),
    ('Violet card present',     'obj-card-violet rounded-2xl border border-violet-100' in check),
    ('Blue card present',       'obj-card-blue rounded-2xl border border-blue-100' in check),
    ('Title 1 — Indexes start', 'Indexes Start at Zero' in check),
    ('Title 2 — Choose wisely', 'Choose List or Dictionary Wisely' in check),
    ('Title 3 — Real data',     'Real Data Arrives in Both Forms' in check),
    ('Icon 1 — hashtag',        'fa6-solid:hashtag' in check),
    ('Icon 2 — scale',          'fa6-solid:scale-balanced' in check),
    ('Icon 3 — database',       'fa6-solid:database' in check),
    ('Pills — Zero-based',      'Zero-based' in check),
    ('Pills — API responses',   'API responses' in check),
    ('Old md:flex-row gone',    'md:flex-row' not in check[ki_start:check.index('id="key-concepts"', ki_start)]),
]

for label, passed in tests:
    print(f'{"✅" if passed else "❌"} {label}')
