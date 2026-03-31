"""
Replace <section id="comparison"> in lesson04.
3 columns: Python class | SQL stored procedure | Excel macro
Clean up the redundant amber tips — consolidate into one.
No DataPipeline refs.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="comparison" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:scale-balanced"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Comparison</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Python class vs. SQL stored procedure vs. Excel macro</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <p class="text-sm text-gray-600 leading-relaxed">The idea of grouping related steps into one callable unit is not unique to Python. SQL and Excel both have their own equivalent structures. Understanding the parallel helps you recognise you already know the concept — you are just learning a new syntax for it.</p>

      <!-- Comparison grid header -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

        <!-- Column headers -->
        <div class="grid grid-cols-3 gap-0 border-b border-gray-100">

          <div class="flex flex-col items-center justify-center gap-2 px-4 py-4 bg-gradient-to-br from-[#fdf0f7] to-white border-r border-gray-100">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="logos:python"></span>
            </span>
            <p class="text-sm font-bold text-gray-800">Python Class</p>
          </div>

          <div class="flex flex-col items-center justify-center gap-2 px-4 py-4 bg-gradient-to-br from-blue-50 to-white border-r border-gray-100">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-blue-600 shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:database"></span>
            </span>
            <p class="text-sm font-bold text-gray-800">SQL Procedure</p>
          </div>

          <div class="flex flex-col items-center justify-center gap-2 px-4 py-4 bg-gradient-to-br from-emerald-50 to-white">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-emerald-600 shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:file-excel"></span>
            </span>
            <p class="text-sm font-bold text-gray-800">Excel Macro</p>
          </div>

        </div>

        <!-- Row 1 — Container keyword -->
        <div class="grid grid-cols-3 gap-0 border-b border-gray-100">
          <div class="px-5 py-4 border-r border-gray-100 bg-[#fdf0f7]/30">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Container</p>
            <code class="text-sm font-mono font-bold text-[#CB187D]">class ReportRunner:</code>
          </div>
          <div class="px-5 py-4 border-r border-gray-100">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Container</p>
            <code class="text-sm font-mono font-bold text-blue-600">CREATE PROCEDURE</code>
          </div>
          <div class="px-5 py-4">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Container</p>
            <code class="text-sm font-mono font-bold text-emerald-600">Sub MacroName()</code>
          </div>
        </div>

        <!-- Row 2 — Steps keyword -->
        <div class="grid grid-cols-3 gap-0 border-b border-gray-100">
          <div class="px-5 py-4 border-r border-gray-100 bg-[#fdf0f7]/30">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Steps</p>
            <code class="text-sm font-mono font-bold text-[#CB187D]">def load_data(self): …</code>
          </div>
          <div class="px-5 py-4 border-r border-gray-100">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Steps</p>
            <code class="text-sm font-mono font-bold text-blue-600">SELECT … / INSERT …</code>
          </div>
          <div class="px-5 py-4">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Steps</p>
            <code class="text-sm font-mono font-bold text-emerald-600">macro steps (VBA lines)</code>
          </div>
        </div>

        <!-- Row 3 — Run keyword -->
        <div class="grid grid-cols-3 gap-0 border-b border-gray-100">
          <div class="px-5 py-4 border-r border-gray-100 bg-[#fdf0f7]/30">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Run it</p>
            <code class="text-sm font-mono font-bold text-[#CB187D]">report.run()</code>
          </div>
          <div class="px-5 py-4 border-r border-gray-100">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Run it</p>
            <code class="text-sm font-mono font-bold text-blue-600">EXEC process_sales</code>
          </div>
          <div class="px-5 py-4">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Run it</p>
            <code class="text-sm font-mono font-bold text-emerald-600">Run Macro button</code>
          </div>
        </div>

        <!-- Row 4 — Reusable? -->
        <div class="grid grid-cols-3 gap-0">
          <div class="px-5 py-4 border-r border-gray-100 bg-[#fdf0f7]/30">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Reusable?</p>
            <p class="text-sm text-gray-700 leading-snug">Yes — create a new object any time</p>
          </div>
          <div class="px-5 py-4 border-r border-gray-100">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Reusable?</p>
            <p class="text-sm text-gray-700 leading-snug">Yes — call the procedure from any query</p>
          </div>
          <div class="px-5 py-4">
            <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 mb-1.5">Reusable?</p>
            <p class="text-sm text-gray-700 leading-snug">Yes — but only within the same workbook</p>
          </div>
        </div>

      </div>

      <!-- SQL code example -->
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
            </div>
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-blue-400 text-xs" data-icon="fa6-solid:database"></span>
              <span class="text-[11px] font-semibold text-gray-400">SQL — equivalent to a Python class method</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- A stored procedure groups multiple SQL steps into one callable unit
CREATE PROCEDURE process_sales AS
BEGIN
    -- step 1: load raw data
    SELECT * FROM raw_sales INTO #staging;

    -- step 2: clean it
    DELETE FROM #staging WHERE amount IS NULL;

    -- step 3: save the result
    INSERT INTO sales_report SELECT * FROM #staging;
END;

-- run it with one call — same idea as report.run() in Python
EXEC process_sales;</code></pre>
        </div>
      </div>

      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">If you have ever written a SQL stored procedure or recorded an Excel macro, you have already been using the same pattern this lesson teaches. A Python class is just the Python way of saying "group these steps together and give the whole thing a name you can call later."</p>
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
html, ok = replace_section(html, 'comparison', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
se_start = result.find('<section id="comparison"')
nx_start = result.find('<section id="practice"')
if nx_start == -1:
    nx_start = result.find('<section id="mistakes"')
s = result[se_start:nx_start] if se_start != -1 and nx_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon fa6-solid:scale-balanced",       'data-icon="fa6-solid:scale-balanced"'),
    ("Header title Comparison",             ">Comparison<"),
    ("Python column header",                ">Python Class<"),
    ("SQL column header",                   ">SQL Procedure<"),
    ("Excel column header",                 ">Excel Macro<"),
    ("class ReportRunner: in row",          "class ReportRunner:"),
    ("CREATE PROCEDURE in row",             "CREATE PROCEDURE"),
    ("Sub MacroName() in row",              "Sub MacroName()"),
    ("report.run() in row",                 "report.run()"),
    ("EXEC process_sales in row",           "EXEC process_sales"),
    ("SQL code block present",             "EXEC process_sales;"),
    ("Row: Reusable? label",               "Reusable?"),
    ("Single amber tip",                    1),
    ("No DataPipeline refs",                True),
    ("def load_data(self): in row",         "def load_data(self):"),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        ok2 = "DataPipeline" not in s
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        count = s.count("bg-amber-tip")
        ok3 = count >= needle
        print(f'  {"✅" if ok3 else "❌"} {label} (found {count})')
        if ok3: passed += 1
        else: failed += 1
    elif needle in s:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
