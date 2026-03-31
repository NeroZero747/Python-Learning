#!/usr/bin/env python3
"""Replace #comparison section body in lesson04_lists_dictionaries.html."""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Locate section boundaries ─────────────────────────────────────────────────
SEC_START = 'id="comparison"'
NEXT_SEC  = 'id="practice"'

sec_idx  = content.index(SEC_START)
next_idx = content.index(NEXT_SEC, sec_idx)

# The body div we want to replace starts after the header block
BODY_OPEN  = '    <div class="bg-white px-8 py-7 space-y-5">'
body_start = content.index(BODY_OPEN, sec_idx)
body_end   = content.rindex('  </div>\n</section>', sec_idx, next_idx)

# Everything from body_start up to (not including) body_end is replaced
old_body = content[body_start:body_end]

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-5">

      <!-- 1 · Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">If you already work with SQL tables or Excel spreadsheets, you already know what lists and dictionaries are — Python just gives them different names. A list is a column of values; a dictionary is a single row where each field has a name.</p>

      <!-- 2 · Tool header cards -->
      <div class="grid grid-cols-3 gap-3">
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel
        </div>
      </div>

      <!-- 3 · Row 1 — ordered data -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:list"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">ordered data</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">list</code>
            <p class="text-xs text-gray-500 leading-relaxed">A Python list holds multiple values in a fixed order, just like a numbered column of cells.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">table column</code>
            <p class="text-xs text-gray-500 leading-relaxed">A SQL column holds one type of value for every row in a table, in the order the rows were inserted.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">spreadsheet column</code>
            <p class="text-xs text-gray-500 leading-relaxed">An Excel column (A, B, C…) stores a series of values you can reference by row number.</p>
          </div>
        </div>
      </div>

      <!-- 3 · Row 2 — named record -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:id-card"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">named record</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">dictionary</code>
            <p class="text-xs text-gray-500 leading-relaxed">A Python dictionary groups related values together under named keys, like <code class="font-mono">{"name": "Alice", "age": 30}</code>.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">table row</code>
            <p class="text-xs text-gray-500 leading-relaxed">A SQL row is one record in a table, where each column name acts as the field label for that record's values.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">spreadsheet row</code>
            <p class="text-xs text-gray-500 leading-relaxed">An Excel row groups related cells across columns, where the header row acts as the field names for every data row below it.</p>
          </div>
        </div>
      </div>

      <!-- 3 · Row 3 — read one item -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:hashtag"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">read one item by position</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">list[index]</code>
            <p class="text-xs text-gray-500 leading-relaxed">Write the list name followed by a number in square brackets, like <code class="font-mono">members[0]</code>, to read the item at that position.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">LIMIT / OFFSET</code>
            <p class="text-xs text-gray-500 leading-relaxed">SQL uses <code class="font-mono">LIMIT 1 OFFSET n</code> to skip to a specific row position and return just that one record.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">INDEX()</code>
            <p class="text-xs text-gray-500 leading-relaxed">The Excel <code class="font-mono">=INDEX(A:A, n)</code> function returns the value at row <code class="font-mono">n</code> in a column, just as a list index does.</p>
          </div>
        </div>
      </div>

      <!-- 3 · Row 4 — look up by name -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:magnifying-glass"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">look up by name</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">dict["key"]</code>
            <p class="text-xs text-gray-500 leading-relaxed">Write the dictionary name followed by a quoted key in square brackets, like <code class="font-mono">provider["name"]</code>, to read that field's value.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">WHERE column = value</code>
            <p class="text-xs text-gray-500 leading-relaxed">A SQL <code class="font-mono">WHERE</code> clause filters rows by matching a column value, letting you retrieve one specific record by name or ID.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">VLOOKUP()</code>
            <p class="text-xs text-gray-500 leading-relaxed">Excel's <code class="font-mono">=VLOOKUP()</code> searches the first column of a table for a name and returns the value from another column in that row.</p>
          </div>
        </div>
      </div>

      <!-- 4 · Centered divider + side-by-side code blocks -->
      <div>
        <div class="flex items-center gap-3 mb-4">
          <span class="flex-1 h-px bg-gray-100"></span>
          <div class="flex items-center gap-2 shrink-0">
            <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
            </span>
            <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">Same provider record, three tools</p>
          </div>
          <span class="flex-1 h-px bg-gray-100"></span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 items-stretch">

          <!-- Python column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Python code</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify" data-icon="logos:python" data-width="16" data-height="16"></span>
                  <span class="text-xs font-semibold text-gray-400">Python</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-python">provider = {
    "name": "Dr. Lee",
    "specialty": "Cardiology",
    "npi": "1234567890"
}
print(provider["name"])</code></pre>
            </div>
          </div>

          <!-- SQL column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">SQL query</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-orange-400" data-icon="fa6-solid:database"></span>
                  <span class="text-xs font-semibold text-gray-400">SQL</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-sql">SELECT name,
       specialty,
       npi
FROM providers
WHERE npi = &apos;1234567890&apos;;</code></pre>
            </div>
          </div>

          <!-- Excel column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Excel formula</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-green-400" data-icon="fa6-solid:table"></span>
                  <span class="text-xs font-semibold text-gray-400">Excel</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-text">=VLOOKUP(
  "1234567890",
  ProvidersTable,
  2,
  FALSE
)</code></pre>
            </div>
          </div>

        </div>

        <p class="text-xs text-gray-400 mt-2">All three retrieve a provider's name by matching on the NPI identifier — the same result, just written in a different tool.</p>
      </div>

      <!-- 5 · Closing amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Every time you work with a table in SQL or a sheet in Excel, you're already thinking in lists and dictionaries. Python just gives you the same structures as variables you can manipulate with code — once you know one, the other two feel immediately familiar.</p>
      </div>

'''

# Build the new content
new_content = content[:body_start] + NEW_BODY + content[body_end:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Wrote file.")

# ── Verification ──────────────────────────────────────────────────────────────
with open(TARGET, "r", encoding="utf-8") as f:
    result = f.read()

checks = [
    ("Intro 'If you already'",          "If you already work with SQL tables"),
    ("Tool header — Python",            'bg-indigo-600 text-white'),
    ("Tool header — SQL",               'bg-orange-600 text-white'),
    ("Tool header — Excel",             'bg-emerald-600 text-white'),
    ("Row 1 label — ordered data",      ">ordered data<"),
    ("Row 1 icon",                      'fa6-solid:list'),
    ("Row 1 PY chip — list",            '>list<'),
    ("Row 2 label — named record",      ">named record<"),
    ("Row 2 icon",                      'fa6-solid:id-card'),
    ("Row 2 PY chip — dictionary",      '>dictionary<'),
    ("Row 3 label — read one item",     ">read one item by position<"),
    ("Row 3 icon",                      'fa6-solid:hashtag'),
    ("Row 3 PY chip",                   '>list[index]<'),
    ("Row 3 SQL chip",                  '>LIMIT / OFFSET<'),
    ("Row 3 XL chip",                   '>INDEX()<'),
    ("Row 4 label — look up by name",   ">look up by name<"),
    ("Row 4 icon",                      'fa6-solid:magnifying-glass'),
    ("Row 4 PY chip",                   '>dict[&quot;key&quot;]<'),
    ("Row 4 SQL chip",                  '>WHERE column = value<'),
    ("Row 4 XL chip",                   '>VLOOKUP()<'),
    ("Divider label",                   "Same provider record, three tools"),
    ("No traffic-light dots",           'bg-red-400/80' not in result[result.index('id="comparison"'):result.index('id="practice"')]),
    ("PY code block language-python",   'class="language-python">provider = {'),
    ("SQL code block language-sql",     'class="language-sql">SELECT name,'),
    ("XL code block language-text",     'class="language-text">=VLOOKUP('),
    ("Caption 'All three'",             "All three retrieve a provider"),
    ("Closing amber tip",               "Every time you work with a table"),
    ("Practice section intact",         'id="practice"'),
]

all_ok = True
for label, check in checks:
    if isinstance(check, bool):
        ok = check
    else:
        ok = check in result
    status = "YES" if ok else "NO "
    if not ok:
        all_ok = False
    print(f"{status}: {label}")

if all_ok:
    print("\nAll checks passed!")
else:
    print("\nSome checks FAILED — review output above.")
