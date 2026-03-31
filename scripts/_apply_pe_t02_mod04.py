"""Rewrite #practice for every lesson in track_02 / mod_04."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_04_handling_large_data")
SECTION_RE = re.compile(
    r'(<section id="practice"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── HTML builder helpers (identical across all pe scripts) ───────

def pill_tabs(tabs):
    parts = []
    for i, label in enumerate(tabs):
        if i == 0:
            cls = ('pe-step pe-step-active flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
                   'text-white shadow-lg shadow-pink-200/50 transition-all duration-250')
        else:
            cls = ('pe-step flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gray-800 text-gray-400 transition-all duration-250')
        parts.append(
            f'<button onclick="switchPeTab({i})" class="{cls}" role="tab">\n'
            f'  <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>\n'
            f'  <span class="pe-step-label text-xs font-bold">{label}</span>\n'
            f'</button>'
        )
    return ('<div class="flex items-center gap-2 mb-6" role="tablist">\n'
            + '\n'.join(parts) + '\n</div>')


def badge_pill(text):
    return (f'<span class="flex items-center gap-1 text-[10px] px-2 py-0.5 '
            f'rounded-full bg-gray-100 text-gray-500 font-medium">{text}</span>')


def build_panel(idx, ex):
    hidden = ' hidden' if idx > 0 else ''
    watermark = f'{idx+1:02d}'
    extra = '\n            '.join(badge_pill(b) for b in ex['badges'])
    return f'''<div class="pe-panel pe-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{watermark}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{ex['title']}</h3>
          <div class="flex items-center gap-2 mt-1 flex-wrap">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            {badge_pill(ex['domain'])}
            {extra}
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
          <p class="text-sm text-gray-600">{ex['task']}</p>
        </div>
      </div>
      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">{ex['filename']}</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">{ex['code']}</code></pre>
          </div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">{ex['cmd']}</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">{ex['output']}</div>
          </div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">{ex['tip']}</p>
        </div>
      </div>
    </div>
  </div>
</div>'''


def make_section(exercises):
    tabs = [ex['tab'] for ex in exercises]
    pills_html = pill_tabs(tabs)
    panels_html = '\n'.join(build_panel(i, ex) for i, ex in enumerate(exercises))
    body = f'{pills_html}\n{panels_html}'
    return (
        '<section id="practice">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Guided exercises to reinforce your learning</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-6">\n'
        f'{body}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── lesson content ───────────────────────────────────────────────

def lesson02():
    """Memory Optimization"""
    return [
        {
            'tab': 'Audit Memory',
            'title': 'Audit Memory Usage',
            'domain': 'Vehicles',
            'badges': ['memory_usage()', 'deep=True'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">fleet.csv</code> and print the memory usage of every column in megabytes. Use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">deep=True</code> so string columns are measured accurately.',
            'filename': 'audit_memory.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;fleet.csv&quot;)  # load fleet data\n'
                '\n'
                'mem = df.memory_usage(deep=True) / 1_048_576  # bytes to MB\n'
                'print(mem.round(2))'
            ),
            'cmd': '$ python audit_memory.py',
            'output': 'Index        0.00<br>vehicle_id   0.76<br>make         1.12<br>year         0.08<br>dtype: float64',
            'tip': 'Always pass deep=True &#8212; without it, object columns report a tiny pointer size instead of their real memory footprint.',
        },
        {
            'tab': 'Shrink Integers',
            'title': 'Shrink Integer Columns',
            'domain': 'Weather',
            'badges': ['to_numeric()', 'downcast'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">readings.csv</code>. Downcast the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">temperature</code> column from int64 to the smallest integer type that fits. Print the dtype before and after.',
            'filename': 'shrink_ints.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;readings.csv&quot;)  # load weather data\n'
                'print(f&quot;Before: {df[&apos;temperature&apos;].dtype}&quot;)  # original\n'
                '\n'
                'df[&quot;temperature&quot;] = pd.to_numeric(df[&quot;temperature&quot;],\n'
                '                                    downcast=&quot;integer&quot;)  # shrink\n'
                'print(f&quot;After:  {df[&apos;temperature&apos;].dtype}&quot;)'
            ),
            'cmd': '$ python shrink_ints.py',
            'output': 'Before: int64<br>After:  int8',
            'tip': 'Downcasting from int64 to int8 uses 8&#215; less memory per value &#8212; that adds up quickly on millions of rows.',
        },
        {
            'tab': 'Use Category Type',
            'title': 'Convert to Category',
            'domain': 'Retail',
            'badges': ['astype()', 'category'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">transactions.csv</code>. Convert the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">payment_method</code> column to the category dtype and print memory usage before and after the conversion.',
            'filename': 'to_category.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;transactions.csv&quot;)\n'
                'before = df[&quot;payment_method&quot;].memory_usage(deep=True)\n'
                '\n'
                'df[&quot;payment_method&quot;] = df[&quot;payment_method&quot;].astype(&quot;category&quot;)\n'
                'after = df[&quot;payment_method&quot;].memory_usage(deep=True)\n'
                '\n'
                'print(f&quot;Before: {before:,} bytes  After: {after:,} bytes&quot;)'
            ),
            'cmd': '$ python to_category.py',
            'output': 'Before: 1,920,128 bytes  After: 250,346 bytes',
            'tip': 'Category dtype stores each unique value once and uses integer codes per row &#8212; ideal when a column has only a handful of distinct values.',
        },
    ]


def lesson03():
    """Chunk Processing"""
    return [
        {
            'tab': 'Count in Chunks',
            'title': 'Count in Chunks',
            'domain': 'Clickstream',
            'badges': ['chunksize', 'iteration'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">clicks.csv</code> in chunks of 50,000 rows. Count the total number of rows without loading the entire file into memory at once.',
            'filename': 'count_chunks.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'total_rows = 0  # running counter\n'
                '\n'
                'for chunk in pd.read_csv(&quot;clicks.csv&quot;, chunksize=50_000):\n'
                '    total_rows += len(chunk)  # add rows in this chunk\n'
                '\n'
                'print(f&quot;Total rows: {total_rows:,}&quot;)'
            ),
            'cmd': '$ python count_chunks.py',
            'output': 'Total rows: 1,250,000',
            'tip': 'Each chunk is a regular DataFrame that gets garbage-collected after the loop moves on &#8212; memory stays flat no matter how large the file is.',
        },
        {
            'tab': 'Filter a Large File',
            'title': 'Filter a Large File',
            'domain': 'Payments',
            'badges': ['chunk + filter', 'concat'],
            'task': 'Read <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">payments.csv</code> in 100,000-row chunks. Keep only rows where <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">status == &quot;failed&quot;</code>. Combine the results and print the count.',
            'filename': 'filter_chunks.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'parts = []  # collect matching chunks\n'
                '\n'
                'for chunk in pd.read_csv(&quot;payments.csv&quot;, chunksize=100_000):\n'
                '    failed = chunk[chunk[&quot;status&quot;] == &quot;failed&quot;]  # filter\n'
                '    parts.append(failed)                           # keep\n'
                '\n'
                'result = pd.concat(parts, ignore_index=True)      # combine\n'
                'print(f&quot;Failed payments: {len(result):,}&quot;)'
            ),
            'cmd': '$ python filter_chunks.py',
            'output': 'Failed payments: 3,412',
            'tip': 'Filter inside the loop so you only keep the tiny subset you need &#8212; the full file never sits in memory.',
        },
        {
            'tab': 'Sum in Chunks',
            'title': 'Sum in Chunks',
            'domain': 'Deliveries',
            'badges': ['running total', 'chunksize'],
            'task': 'Read <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">deliveries.csv</code> in 50,000-row chunks. Calculate the total weight shipped by summing the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">weight_kg</code> column across all chunks.',
            'filename': 'sum_chunks.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'total_weight = 0.0  # running total\n'
                '\n'
                'for chunk in pd.read_csv(&quot;deliveries.csv&quot;, chunksize=50_000):\n'
                '    total_weight += chunk[&quot;weight_kg&quot;].sum()  # add chunk sum\n'
                '\n'
                'print(f&quot;Total shipped: {total_weight:,.1f} kg&quot;)'
            ),
            'cmd': '$ python sum_chunks.py',
            'output': 'Total shipped: 487,320.5 kg',
            'tip': 'For simple aggregations (sum, count, min, max) you only need a single running variable &#8212; no need to keep any chunks in memory.',
        },
    ]


def lesson04():
    """Processing Millions of Rows"""
    return [
        {
            'tab': 'Column Arithmetic',
            'title': 'Column Arithmetic',
            'domain': 'Tickets',
            'badges': ['vectorised', 'no loops'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">event_tickets.csv</code>. Create a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">revenue</code> column by multiplying <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">quantity</code> &#215; <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">price</code>. Print total revenue.',
            'filename': 'ticket_revenue.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;event_tickets.csv&quot;)  # load ticket data\n'
                '\n'
                'df[&quot;revenue&quot;] = df[&quot;quantity&quot;] * df[&quot;price&quot;]  # vectorised\n'
                'print(f&quot;Total revenue: ${df[&apos;revenue&apos;].sum():,.2f}&quot;)'
            ),
            'cmd': '$ python ticket_revenue.py',
            'output': 'Total revenue: $2,145,600.00',
            'tip': 'Column arithmetic runs in compiled C under the hood &#8212; it processes millions of rows in milliseconds without a Python loop.',
        },
        {
            'tab': 'Conditional Labels',
            'title': 'Conditional Labels',
            'domain': 'Shipments',
            'badges': ['np.where()', 'vectorised'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">shipments.csv</code>. Add a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">size_label</code> column: rows where <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">weight_kg &gt;= 50</code> get "Heavy", the rest get "Light". Print the count of each label.',
            'filename': 'label_shipments.py',
            'code': (
                'import pandas as pd\n'
                'import numpy as np\n'
                '\n'
                'df = pd.read_csv(&quot;shipments.csv&quot;)  # load shipments\n'
                '\n'
                'df[&quot;size_label&quot;] = np.where(\n'
                '    df[&quot;weight_kg&quot;] &gt;= 50, &quot;Heavy&quot;, &quot;Light&quot;)  # label\n'
                'print(df[&quot;size_label&quot;].value_counts())'
            ),
            'cmd': '$ python label_shipments.py',
            'output': 'size_label<br>Light    784320<br>Heavy    215680<br>Name: count, dtype: int64',
            'tip': 'np.where() runs at C speed. A Python for-loop doing the same thing on a million rows would take minutes.',
        },
        {
            'tab': 'Benchmark a Groupby',
            'title': 'Benchmark a Groupby',
            'domain': 'Metrics',
            'badges': ['time', 'performance'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">metrics.csv</code> (1 million+ rows). Time how long a groupby-mean operation takes on the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">value</code> column grouped by <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">region</code>. Print the elapsed time.',
            'filename': 'bench_groupby.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'df = pd.read_csv(&quot;metrics.csv&quot;)  # large dataset\n'
                '\n'
                'start = time.time()                               # begin\n'
                'result = df.groupby(&quot;region&quot;)[&quot;value&quot;].mean()     # groupby\n'
                'elapsed = time.time() - start                     # end\n'
                '\n'
                'print(f&quot;Groupby took {elapsed:.4f}s&quot;)\n'
                'print(result)'
            ),
            'cmd': '$ python bench_groupby.py',
            'output': 'Groupby took 0.0312s<br>region<br>APAC     47.23<br>EMEA     52.11<br>LATAM    48.67<br>NAM      55.40<br>Name: value, dtype: float64',
            'tip': 'Always time operations on real-sized data &#8212; a function that feels fast on 100 rows may be slow on 10 million.',
        },
    ]


def lesson05():
    """Columnar Storage Formats"""
    return [
        {
            'tab': 'Save as Parquet',
            'title': 'Save as Parquet',
            'domain': 'Surveys',
            'badges': ['to_parquet()', 'file size'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">survey_results.csv</code> and save it as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">survey_results.parquet</code>. Print the file sizes of both to compare.',
            'filename': 'save_parquet.py',
            'code': (
                'import pandas as pd\n'
                'from pathlib import Path\n'
                '\n'
                'df = pd.read_csv(&quot;survey_results.csv&quot;)         # load CSV\n'
                'df.to_parquet(&quot;survey_results.parquet&quot;)         # save parquet\n'
                '\n'
                'csv_mb = Path(&quot;survey_results.csv&quot;).stat().st_size / 1_048_576\n'
                'pq_mb = Path(&quot;survey_results.parquet&quot;).stat().st_size / 1_048_576\n'
                'print(f&quot;CSV: {csv_mb:.1f} MB  Parquet: {pq_mb:.1f} MB&quot;)'
            ),
            'cmd': '$ python save_parquet.py',
            'output': 'CSV: 24.3 MB  Parquet: 4.8 MB',
            'tip': 'Parquet applies column-level compression automatically &#8212; typical CSV files shrink 3&#8211;10&#215; with no extra code.',
        },
        {
            'tab': 'Load Two Columns',
            'title': 'Load Selected Columns',
            'domain': 'Stock',
            'badges': ['columns=[]', 'selective read'],
            'task': 'Load only the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">symbol</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">close_price</code> columns from <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">stocks.parquet</code>. Print the DataFrame shape and memory usage.',
            'filename': 'load_columns.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_parquet(&quot;stocks.parquet&quot;,\n'
                '                     columns=[&quot;symbol&quot;, &quot;close_price&quot;])  # 2 cols only\n'
                '\n'
                'mem_mb = df.memory_usage(deep=True).sum() / 1_048_576\n'
                'print(f&quot;Shape: {df.shape}  Memory: {mem_mb:.1f} MB&quot;)'
            ),
            'cmd': '$ python load_columns.py',
            'output': 'Shape: (500000, 2)  Memory: 8.6 MB',
            'tip': 'Columnar formats like Parquet skip columns you did not ask for &#8212; CSV must read every column even if you only need two.',
        },
        {
            'tab': 'Time the Load',
            'title': 'Time CSV vs Parquet',
            'domain': 'Events',
            'badges': ['time', 'comparison'],
            'task': 'Time how long it takes to load the same dataset from <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">events.csv</code> versus <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">events.parquet</code>. Print both times side by side.',
            'filename': 'time_load.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'start = time.time()\n'
                'pd.read_csv(&quot;events.csv&quot;)                        # load CSV\n'
                'csv_time = time.time() - start\n'
                '\n'
                'start = time.time()\n'
                'pd.read_parquet(&quot;events.parquet&quot;)                 # load Parquet\n'
                'pq_time = time.time() - start\n'
                '\n'
                'print(f&quot;CSV: {csv_time:.3f}s  Parquet: {pq_time:.3f}s&quot;)'
            ),
            'cmd': '$ python time_load.py',
            'output': 'CSV: 1.247s  Parquet: 0.183s',
            'tip': 'Parquet is faster to read because the file stores metadata about column types &#8212; pandas does not need to guess them row by row.',
        },
    ]


def lesson06():
    """Parquet Files — Deeper Dive"""
    return [
        {
            'tab': 'Convert a CSV',
            'title': 'Convert CSV to Parquet',
            'domain': 'Archives',
            'badges': ['to_parquet()', 'workflow'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">archive_logs.csv</code> and save it as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">archive_logs.parquet</code>. Print the row count and confirm the output file exists.',
            'filename': 'convert_csv.py',
            'code': (
                'import pandas as pd\n'
                'from pathlib import Path\n'
                '\n'
                'df = pd.read_csv(&quot;archive_logs.csv&quot;)             # load\n'
                'df.to_parquet(&quot;archive_logs.parquet&quot;)             # convert\n'
                '\n'
                'exists = Path(&quot;archive_logs.parquet&quot;).exists()   # verify\n'
                'print(f&quot;{len(df):,} rows saved. File exists: {exists}&quot;)'
            ),
            'cmd': '$ python convert_csv.py',
            'output': '450,000 rows saved. File exists: True',
            'tip': 'Converting archival CSV files to Parquet once saves time on every future read &#8212; a one-time cost for a permanent speed-up.',
        },
        {
            'tab': 'Verify Column Types',
            'title': 'Verify Column Types',
            'domain': 'Payroll',
            'badges': ['dtypes', 'round-trip'],
            'task': 'Save <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">payroll.csv</code> as Parquet, then reload it. Compare the dtypes of the original and the reloaded DataFrame to confirm nothing changed.',
            'filename': 'verify_types.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'original = pd.read_csv(&quot;payroll.csv&quot;)             # load CSV\n'
                'original.to_parquet(&quot;payroll.parquet&quot;)             # save\n'
                'reloaded = pd.read_parquet(&quot;payroll.parquet&quot;)      # reload\n'
                '\n'
                'print(&quot;Original dtypes:&quot;, original.dtypes.tolist())\n'
                'print(&quot;Reloaded dtypes:&quot;, reloaded.dtypes.tolist())'
            ),
            'cmd': '$ python verify_types.py',
            'output': "Original dtypes: [dtype('O'), dtype('float64'), dtype('int64')]<br>Reloaded dtypes: [dtype('O'), dtype('float64'), dtype('int64')]",
            'tip': 'Parquet preserves column types exactly. CSV does not &#8212; re-loading a CSV often turns integers into floats or dates into strings.',
        },
        {
            'tab': 'Measure Compression',
            'title': 'Measure Compression',
            'domain': 'Telemetry',
            'badges': ['file size', 'ratio'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">telemetry.csv</code> and save it as Parquet with <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">snappy</code> compression. Print both file sizes and the compression ratio.',
            'filename': 'compression.py',
            'code': (
                'import pandas as pd\n'
                'from pathlib import Path\n'
                '\n'
                'df = pd.read_csv(&quot;telemetry.csv&quot;)                # load\n'
                'df.to_parquet(&quot;telemetry.parquet&quot;, compression=&quot;snappy&quot;)\n'
                '\n'
                'csv_b = Path(&quot;telemetry.csv&quot;).stat().st_size\n'
                'pq_b = Path(&quot;telemetry.parquet&quot;).stat().st_size\n'
                'ratio = csv_b / pq_b  # compression ratio\n'
                'print(f&quot;CSV: {csv_b:,}B  Parquet: {pq_b:,}B  Ratio: {ratio:.1f}x&quot;)'
            ),
            'cmd': '$ python compression.py',
            'output': 'CSV: 36,700,160B  Parquet: 5,242,880B  Ratio: 7.0x',
            'tip': 'Snappy is the default Parquet compression &#8212; it balances speed and size well. Use gzip for smaller files at the cost of slower writes.',
        },
    ]


def lesson13():
    """Performance Profiling"""
    return [
        {
            'tab': 'Time a Load Step',
            'title': 'Time a Load Step',
            'domain': 'Dashboards',
            'badges': ['time', 'bottleneck'],
            'task': 'Write a script that loads <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">dashboard_data.csv</code> and prints how many seconds the load took. This helps identify whether the file read is the bottleneck.',
            'filename': 'time_load_step.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'start = time.time()                                # begin\n'
                'df = pd.read_csv(&quot;dashboard_data.csv&quot;)             # load\n'
                'elapsed = time.time() - start                      # end\n'
                '\n'
                'print(f&quot;Loaded {len(df):,} rows in {elapsed:.3f}s&quot;)'
            ),
            'cmd': '$ python time_load_step.py',
            'output': 'Loaded 800,000 rows in 1.342s',
            'tip': 'If the load step is slow, consider switching to Parquet or reading only the columns you need.',
        },
        {
            'tab': 'Profile a Function',
            'title': 'Profile a Function',
            'domain': 'ETL',
            'badges': ['cProfile', 'run()'],
            'task': 'Write a function called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">transform</code> that loads a CSV and groups by category. Use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">cProfile</code> to profile the function and print the top results.',
            'filename': 'profile_etl.py',
            'code': (
                'import pandas as pd\n'
                'import cProfile\n'
                '\n'
                'def transform():                                   # function\n'
                '    df = pd.read_csv(&quot;etl_input.csv&quot;)\n'
                '    return df.groupby(&quot;category&quot;)[&quot;value&quot;].sum()\n'
                '\n'
                'cProfile.run(&quot;transform()&quot;, sort=&quot;cumulative&quot;)'
            ),
            'cmd': '$ python profile_etl.py',
            'output': '         38 function calls in 0.842 seconds<br><br>   Ordered by: cumulative time<br>   ...',
            'tip': 'cProfile shows exactly how much time each function call took &#8212; focus your optimisation on the slowest lines first.',
        },
        {
            'tab': 'Compare Approaches',
            'title': 'Compare Two Approaches',
            'domain': 'Queries',
            'badges': ['before/after', 'time'],
            'task': 'Time two ways to filter rows in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">queries.csv</code>: first using a Python loop, then using vectorised boolean indexing. Print both times to show the speed difference.',
            'filename': 'compare_filter.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'df = pd.read_csv(&quot;queries.csv&quot;)\n'
                '\n'
                'start = time.time()\n'
                'slow = [r for _, r in df.iterrows() if r[&quot;ms&quot;] &gt; 100]  # loop\n'
                'loop_t = time.time() - start\n'
                '\n'
                'start = time.time()\n'
                'fast = df[df[&quot;ms&quot;] &gt; 100]                              # vectorised\n'
                'vec_t = time.time() - start\n'
                '\n'
                'print(f&quot;Loop: {loop_t:.3f}s  Vectorised: {vec_t:.4f}s&quot;)'
            ),
            'cmd': '$ python compare_filter.py',
            'output': 'Loop: 4.217s  Vectorised: 0.0085s',
            'tip': 'Vectorised operations are often 100&#8211;1,000&#215; faster than iterrows(). Avoid Python loops on DataFrames whenever possible.',
        },
    ]


REGISTRY = {
    "lesson02_memory_optimization.html": lesson02,
    "lesson03_chunk_processing.html": lesson03,
    "lesson04_processing_millions_of_rows.html": lesson04,
    "lesson05_columnar_storage.html": lesson05,
    "lesson06_parquet_files.html": lesson06,
    "lesson13_performance_profiling.html": lesson13,
}


def main():
    for fname, fn in REGISTRY.items():
        fpath = ROOT / fname
        if not fpath.exists():
            print(f"  SKIP  {fname} (not found)")
            continue
        html = fpath.read_text(encoding="utf-8")
        exercises = fn()
        new_section = make_section(exercises)
        new_html, count = SECTION_RE.subn(new_section, html)
        if count == 0:
            print(f"  WARN  {fname} (no #practice section)")
            continue
        fpath.write_text(new_html, encoding="utf-8")
        print(f"  OK    {fname} ({len(exercises)} exercises)")
    print("\nDone.")


if __name__ == "__main__":
    main()
