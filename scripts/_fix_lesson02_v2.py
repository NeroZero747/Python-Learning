"""
Apply remaining changes to lesson02_reading_files_csv_excel_json.html:
1. TOC module list (15 lessons, lesson02 active) — skip if already done
2. Key takeaways redesign (2-col grid, text-sm, no modifier classes) — skip if already done
3. Real-world section redesign (health insurance, file-reading pipeline)
"""
import re, sys

FILE = r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_03_python_for_data_analysts\lesson02_reading_files_csv_excel_json.html'

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

orig = content

# ─────────────────────────────────────────────────────────
# 1. TOC MODULE LIST — skip if already correct
# ─────────────────────────────────────────────────────────
INACTIVE = 'class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors"'
ACTIVE   = 'class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline mod-lesson-active transition-colors"'
DOT_INACTIVE = '<span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>'
DOT_ACTIVE   = '<span class="w-2 h-2 rounded-full bg-[#CB187D] lesson-dot shrink-0"></span>'

lessons = [
    ("lesson01_pandas_and_dataframes.html",          "1. Pandas &amp; DataFrames",              False),
    ("lesson02_reading_files_csv_excel_json.html",    "2. Reading Files (CSV, Excel &amp; JSON)", True),
    ("lesson03_selecting_and_filtering_data.html",    "3. Selecting &amp; Filtering Data",        False),
    ("lesson04_groupby_and_aggregation.html",         "4. GroupBy &amp; Aggregation",             False),
    ("lesson05_merging_and_joining_data.html",        "5. Merging &amp; Joining Data",            False),
    ("lesson06_cleaning_missing_data.html",           "6. Cleaning Missing Data",                 False),
    ("lesson07_string_operations.html",               "7. String Operations",                     False),
    ("lesson08_datetime_operations.html",             "8. Datetime Operations",                   False),
    ("lesson09_pivot_tables.html",                    "9. Pivot Tables",                          False),
    ("lesson10_applying_functions.html",              "10. Applying Functions",                   False),
    ("lesson11_multi_index_and_reshaping.html",       "11. Multi-Index &amp; Reshaping",          False),
    ("lesson12_duplicates_and_outliers.html",         "12. Duplicates &amp; Outliers",            False),
    ("lesson13_visualisation_basics.html",            "13. Visualisation Basics",                 False),
    ("lesson14_exporting_data.html",                  "14. Exporting Data",                       False),
    ("lesson15_end_to_end_project.html",              "15. End-to-End Project",                   False),
]

items = []
for href, label, active in lessons:
    dot  = DOT_ACTIVE if active else DOT_INACTIVE
    cls  = ACTIVE     if active else INACTIVE
    items.append(f'<a href="{href}" {cls}>\n  {dot}\n  <span class="truncate">{label}</span>\n</a>')

new_toc_block = (
    '<div class="space-y-1">'
    + '\n'
    + '\n'.join(items)
    + '\n</div>\n          </div>\n        </div>\n      </aside>'
)

old_toc_m = re.search(r'<div class="space-y-1">.*?</aside>', content, re.DOTALL)
if not old_toc_m:
    print('⚠️  TOC space-y-1 block not found — skipping')
elif 'lesson15_end_to_end_project.html' in old_toc_m.group():
    print('⚠️  TOC already has 15 lessons — skipping')
else:
    content = content[:old_toc_m.start()] + new_toc_block + content[old_toc_m.end():]
    print('✅ TOC module list replaced (15 lessons, lesson02 active)')


# ─────────────────────────────────────────────────────────
# 2. KEY TAKEAWAYS — skip if already 2-col
# ─────────────────────────────────────────────────────────
ki_section_start = content.find('<section id="key-ideas"')
ki_section_end   = content.find('</section>', ki_section_start) + len('</section>')
ki_region = content[ki_section_start:ki_section_end]

if 'sm:grid-cols-2 gap-4' in ki_region:
    print('⚠️  Key takeaways already 2-col — skipping')
else:
    ki_body_m = re.search(r'<div class="bg-white px-8 py-7 space-y-4">.*?</div>\s*</div>\s*</section>', ki_region, re.DOTALL)
    if not ki_body_m:
        print('❌ key-ideas body not found')
        sys.exit(1)

    old_ki_str = ki_body_m.group()
    if content.count(old_ki_str) != 1:
        print(f'❌ key-ideas body appears {content.count(old_ki_str)} times — not safe')
        sys.exit(1)

    NEW_KI_BODY = '''<div class="bg-white px-8 py-7">

<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

<div class="obj-card rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-5 py-5 space-y-3">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:gear"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Parameters Prevent Corrupted Loads</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Without specifying the separator and encoding, pandas guesses — and a wrong guess silently turns every accented character and currency symbol into a question mark or garbled text that breaks downstream calculations.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">sep=</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">encoding=</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Silent errors</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-5 py-5 space-y-3">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:magnifying-glass"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">head() Is Your First Quality Check</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Running <code class="text-[11px] bg-gray-100 px-1 rounded">df.head()</code> immediately after loading catches wrong separators, missing column names, and garbled text before any calculation produces a wrong result. It takes two seconds and saves hours of debugging.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">df.head()</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">First 5 rows</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Spot errors</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-5 py-5 space-y-3">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Object dtype Means Numbers Loaded as Text</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">When pandas shows <code class="text-[11px] bg-gray-100 px-1 rounded">dtype: object</code> for a column you expected to be numeric, it means every value is stored as a string. Arithmetic will fail and <code class="text-[11px] bg-gray-100 px-1 rounded">pd.to_numeric()</code> is needed to convert it correctly.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">dtype: object</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">pd.to_numeric()</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Type fix</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-emerald-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
  <div class="px-5 py-5 space-y-3">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:forward-fast"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">nrows Tests Large Files Cheaply</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Loading a million-row CSV to check its structure wastes time and memory. Passing <code class="text-[11px] bg-gray-100 px-1 rounded">nrows=100</code> loads just the first hundred rows — more than enough to verify columns, dtypes, and separators before committing to a full read.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">nrows=</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Quick preview</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Large files</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-amber-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-amber-500 to-orange-400"></div>
  <div class="px-5 py-5 space-y-3">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:calendar-check"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">parse_dates Converts on Load</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Date columns arrive as text strings unless you tell pandas otherwise. Passing <code class="text-[11px] bg-gray-100 px-1 rounded">parse_dates=["date_col"]</code> converts them to proper datetime objects at load time, so sorting, filtering by date range, and time-series calculations all work correctly from the start.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-600 border border-amber-100">parse_dates=</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-600 border border-amber-100">datetime</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-600 border border-amber-100">No conversion needed</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-teal-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-teal-500 to-cyan-400"></div>
  <div class="px-5 py-5 space-y-3">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:sitemap"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Nested JSON Must Be Flattened First</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">A JSON file where each record contains an object inside an object (for example, an address nested inside a provider record) cannot be queried as flat columns until you call <code class="text-[11px] bg-gray-100 px-1 rounded">json_normalize()</code> — which expands each nested key into its own column.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-teal-50 text-teal-600 border border-teal-100">json_normalize()</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-teal-50 text-teal-600 border border-teal-100">Nested</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-teal-50 text-teal-600 border border-teal-100">Flat columns</span>
    </div>
  </div>
</div>

</div>

</div>
  </div>
</section>'''

    content = content.replace(old_ki_str, NEW_KI_BODY, 1)
    print('✅ Key takeaways redesigned (2-col grid, text-sm, no modifier classes, 6 cards)')


# ─────────────────────────────────────────────────────────
# 3. REAL-WORLD SECTION REDESIGN — skip if already health insurance
# ─────────────────────────────────────────────────────────
if 'claims CSV' in content and 'provider_df' in content:
    print('⚠️  Real-world already health insurance — skipping')
else:
    rw_section_start = content.find('<section id="real-world"')
    rw_section_end   = content.find('</section>', rw_section_start) + len('</section>')
    rw_region = content[rw_section_start:rw_section_end]

    # Match any space-y-N body div
    rw_body_m = re.search(r'<div class="bg-white px-8 py-7 space-y-\d+">.*?</div>\s*</div>\s*</section>', rw_region, re.DOTALL)
    if not rw_body_m:
        print('❌ real-world body not found')
        sys.exit(1)

    old_rw_str = rw_body_m.group()
    if content.count(old_rw_str) != 1:
        print(f'❌ real-world body appears {content.count(old_rw_str)} times — not safe')
        sys.exit(1)

    NEW_RW_FULL = '''<div class="bg-white px-8 py-7 space-y-6">

  <!-- Intro paragraph -->
  <p class="text-sm text-gray-600 leading-relaxed">Every morning, the health insurance data team ingests three separate data sources: a pipe-delimited claims CSV extract from the Policy Administration System (PAS), a multi-sheet Excel benefits schedule issued by the HR department, and a JSON provider feed from the registration API. The team runs <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">pd.read_csv()</code>, <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">pd.read_excel()</code>, and <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">pd.read_json()</code> in sequence — then calls <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">df.head()</code> and <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">df.info()</code> before touching any of the data.</p>

  <!-- 4-step pipeline -->
  <div>
    <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">The 15-minute data ingestion pipeline — start to finish</p>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

      <!-- Step 1 — pink -->
      <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
        <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
        <div class="px-4 py-4">
          <div class="flex items-center justify-between mb-3">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0">
              <span class="iconify text-white text-xs" data-icon="fa6-solid:file-csv"></span>
            </span>
            <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">9:00 am</span>
          </div>
          <p class="text-xs font-bold text-gray-800 mb-1.5">Step 1 — Load claims CSV</p>
          <p class="text-xs text-gray-500 leading-relaxed mb-3">Reads 12 regional claims extracts using <code class="bg-gray-100 px-0.5 rounded">sep=&quot;|&quot;</code> and <code class="bg-gray-100 px-0.5 rounded">encoding=&quot;utf-8&quot;</code> to prevent garbled characters.</p>
          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-pink-50 text-[#CB187D] border border-pink-100">read_csv()</span>
        </div>
      </div>

      <!-- Step 2 — violet -->
      <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-violet-100 transition-all duration-300">
        <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
        <div class="px-4 py-4">
          <div class="flex items-center justify-between mb-3">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-violet-500 to-purple-600 shrink-0">
              <span class="iconify text-white text-xs" data-icon="fa6-solid:file-excel"></span>
            </span>
            <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">9:03 am</span>
          </div>
          <p class="text-xs font-bold text-gray-800 mb-1.5">Step 2 — Load Excel benefits</p>
          <p class="text-xs text-gray-500 leading-relaxed mb-3">Uses <code class="bg-gray-100 px-0.5 rounded">sheet_name=&quot;Q1&quot;</code> to target the correct quarter from the HR multi-tab benefits schedule.</p>
          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-violet-50 text-violet-600 border border-violet-100">read_excel(sheet_name=)</span>
        </div>
      </div>

      <!-- Step 3 — blue -->
      <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-blue-100 transition-all duration-300">
        <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
        <div class="px-4 py-4">
          <div class="flex items-center justify-between mb-3">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0">
              <span class="iconify text-white text-xs" data-icon="fa6-solid:code-branch"></span>
            </span>
            <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">9:07 am</span>
          </div>
          <p class="text-xs font-bold text-gray-800 mb-1.5">Step 3 — Parse provider JSON</p>
          <p class="text-xs text-gray-500 leading-relaxed mb-3">Calls <code class="bg-gray-100 px-0.5 rounded">read_json()</code> then <code class="bg-gray-100 px-0.5 rounded">json_normalize()</code> to flatten nested address and contact fields into separate columns.</p>
          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-50 text-blue-600 border border-blue-100">read_json() + json_normalize()</span>
        </div>
      </div>

      <!-- Step 4 — emerald -->
      <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-emerald-100 transition-all duration-300">
        <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
        <div class="px-4 py-4">
          <div class="flex items-center justify-between mb-3">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0">
              <span class="iconify text-white text-xs" data-icon="fa6-solid:magnifying-glass-chart"></span>
            </span>
            <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">9:15 am</span>
          </div>
          <p class="text-xs font-bold text-gray-800 mb-1.5">Step 4 — Inspect all DataFrames</p>
          <p class="text-xs text-gray-500 leading-relaxed mb-3">Runs <code class="bg-gray-100 px-0.5 rounded">df.head()</code> and <code class="bg-gray-100 px-0.5 rounded">df.info()</code> on each DataFrame to confirm row counts, column names, and dtypes before analysis begins.</p>
          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-600 border border-emerald-100">df.head() + df.info()</span>
        </div>
      </div>

    </div>
  </div>

  <!-- 3 role cards -->
  <div>
    <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">Health insurance analysts who read data every day</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

      <!-- Claims Data Analyst — violet -->
      <div class="rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm hover:shadow-md transition-all duration-300">
        <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
        <div class="px-5 py-5 space-y-3">
          <div class="flex items-center gap-3">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
              <span class="iconify text-white text-base" data-icon="fa6-solid:file-medical"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800">Claims Data Analyst</p>
              <p class="text-xs text-gray-400">Policy Administration System</p>
            </div>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed">Receives a daily pipe-delimited claims CSV extract from PAS. Loads it with <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">pd.read_csv(sep="|", encoding="utf-8")</code> to stack 12 regional files into a single DataFrame for trend analysis.</p>
          <div class="rounded-lg bg-gray-50 border border-gray-100 px-3 py-2">
            <p class="text-[10px] font-mono text-gray-500">returns <span class="text-violet-600 font-bold">claims_df</span></p>
          </div>
        </div>
      </div>

      <!-- Benefits Coordinator — pink -->
      <div class="rounded-2xl border border-[#f5c6e0] bg-white overflow-hidden shadow-sm hover:shadow-md transition-all duration-300">
        <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
        <div class="px-5 py-5 space-y-3">
          <div class="flex items-center gap-3">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
              <span class="iconify text-white text-base" data-icon="fa6-solid:file-excel"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800">Benefits Coordinator</p>
              <p class="text-xs text-gray-400">HR Benefits Department</p>
            </div>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed">Works with a quarterly benefits schedule delivered as a multi-tab Excel workbook. Uses <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">pd.read_excel(sheet_name="Q1")</code> to isolate the correct quarter without loading the entire workbook into memory.</p>
          <div class="rounded-lg bg-gray-50 border border-gray-100 px-3 py-2">
            <p class="text-[10px] font-mono text-gray-500">returns <span class="text-[#CB187D] font-bold">benefits_df</span></p>
          </div>
        </div>
      </div>

      <!-- Provider Data Analyst — emerald -->
      <div class="rounded-2xl border border-emerald-100 bg-white overflow-hidden shadow-sm hover:shadow-md transition-all duration-300">
        <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
        <div class="px-5 py-5 space-y-3">
          <div class="flex items-center gap-3">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
              <span class="iconify text-white text-base" data-icon="fa6-solid:hospital-user"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800">Provider Data Analyst</p>
              <p class="text-xs text-gray-400">Provider Registration API</p>
            </div>
          </div>
          <p class="text-xs text-gray-600 leading-relaxed">Consumes a live JSON feed from the provider registration API, where each record contains a nested address object. Calls <code class="text-[11px] bg-gray-100 px-1 rounded font-mono">json_normalize()</code> after loading to flatten nested fields into queryable columns.</p>
          <div class="rounded-lg bg-gray-50 border border-gray-100 px-3 py-2">
            <p class="text-[10px] font-mono text-gray-500">returns <span class="text-emerald-600 font-bold">provider_df</span></p>
          </div>
        </div>
      </div>

    </div>
  </div>

</div>
    </div>
  </div>
</section>'''

    content = content.replace(old_rw_str, NEW_RW_FULL, 1)
    print('✅ Real-world section redesigned (health insurance, file-reading pipeline + 3 role cards)')


# ─────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n✅ File saved. Total chars: {len(content):,} (delta: {len(content)-len(orig):+,})')
