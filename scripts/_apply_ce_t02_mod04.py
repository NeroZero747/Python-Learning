"""Rewrite #code-examples for every lesson in track_02 / mod_04."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_04_handling_large_data")
SECTION_RE = re.compile(
    r'(<section id="code-examples"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── HTML builder helpers ─────────────────────────────────────────

def pill_tabs(tabs):
    parts = []
    for i, t in enumerate(tabs):
        label = t[0]
        if i == 0:
            cls = ('ce-step ce-step-active flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
                   'text-white shadow-lg shadow-pink-200/50 transition-all duration-250')
        else:
            cls = ('ce-step flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gray-800 text-gray-400 transition-all duration-250')
        parts.append(
            f'<button onclick="switchCeTab({i})" class="{cls}" role="tab">\n'
            f'  <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>\n'
            f'  <span class="ce-step-label text-xs font-bold">{label}</span>\n'
            f'</button>'
        )
    return ('<div class="flex items-center gap-2 mb-6" role="tablist">\n'
            + '\n'.join(parts) + '\n</div>')


def keyword_pill(text):
    return (f'<span class="flex items-center gap-1 text-[10px] px-2 py-0.5 '
            f'rounded-full bg-gray-100 text-gray-500 font-medium">{text}</span>')


def build_panel(idx, ex):
    hidden = ' hidden' if idx > 0 else ''
    watermark = f'{idx+1:02d}'
    extra_pills = '\n            '.join(keyword_pill(p) for p in ex['pills'])
    return f'''<div class="ce-panel ce-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{watermark}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{ex['title']}</h3>
          <div class="flex items-center gap-2 mt-1 flex-wrap">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            {keyword_pill(ex['domain'])}
            {extra_pills}
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">{ex['desc']}</p>
        </div>
      </div>
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
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">{ex['tip']}</p>
      </div>
    </div>
  </div>
</div>'''


def make_section(examples):
    tabs = [(ex['tab'],) for ex in examples]
    pills_html = pill_tabs(tabs)
    panels_html = '\n'.join(build_panel(i, ex) for i, ex in enumerate(examples))
    body = f'{pills_html}\n{panels_html}'
    return (
        '<section id="code-examples">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:code"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Code Examples</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Hands-on code snippets to explore the concepts</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-6">\n'
        f'{body}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── lesson content ───────────────────────────────────────────────

def lesson02_examples():
    """Memory Optimization"""
    return [
        {
            'tab': 'Check Memory Usage',
            'domain': 'Sales',
            'title': 'Check Memory Usage',
            'pills': ['memory_usage()', 'deep=True'],
            'desc': 'This script loads a CSV and prints how many megabytes each column uses. You can spot oversized columns before deciding where to optimise.',
            'filename': 'check_memory.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;sales.csv&quot;)  # load sales data\n'
                '\n'
                'mem = df.memory_usage(deep=True)   # bytes per column\n'
                'mem_mb = mem / 1_048_576            # convert to megabytes\n'
                'print(mem_mb.round(2))'
            ),
            'cmd': '$ python check_memory.py',
            'output': 'Index       0.00<br>order_id    0.76<br>product     3.81<br>revenue     0.76<br>dtype: float64',
            'tip': 'Always pass deep=True when checking memory &#8212; without it, string columns report a misleadingly small number.',
        },
        {
            'tab': 'Downcast Numbers',
            'domain': 'Sensors',
            'title': 'Downcast Numbers',
            'pills': ['pd.to_numeric()', 'downcast'],
            'desc': 'This script converts a 64-bit integer column to the smallest type that can hold its values, cutting memory in half or more.',
            'filename': 'downcast_int.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;sensors.csv&quot;)  # load sensor data\n'
                '\n'
                'before = df[&quot;reading&quot;].memory_usage(deep=True)  # before\n'
                'df[&quot;reading&quot;] = pd.to_numeric(df[&quot;reading&quot;], downcast=&quot;integer&quot;)\n'
                'after = df[&quot;reading&quot;].memory_usage(deep=True)   # after\n'
                'print(f&quot;Before: {before:,} bytes  After: {after:,} bytes&quot;)'
            ),
            'cmd': '$ python downcast_int.py',
            'output': 'Before: 800,128 bytes  After: 200,128 bytes',
            'tip': 'Downcasting works best on integer columns with a narrow range &#8212; check the min and max values first to make sure nothing overflows.',
        },
        {
            'tab': 'Use Category Type',
            'domain': 'Customers',
            'title': 'Use Category Type',
            'pills': ['astype(&quot;category&quot;)', 'strings'],
            'desc': 'This script converts a string column with many repeated values to the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">category</code> type. Pandas stores each unique value once instead of once per row.',
            'filename': 'use_category.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;customers.csv&quot;)  # load customer data\n'
                '\n'
                'before = df[&quot;region&quot;].memory_usage(deep=True)\n'
                'df[&quot;region&quot;] = df[&quot;region&quot;].astype(&quot;category&quot;)  # convert\n'
                'after = df[&quot;region&quot;].memory_usage(deep=True)\n'
                'print(f&quot;Saved {(before - after):,} bytes&quot;)'
            ),
            'cmd': '$ python use_category.py',
            'output': 'Saved 5,600,000 bytes',
            'tip': 'Category type shines when a column has fewer than ~10,000 unique values out of millions of rows &#8212; the more repetition, the bigger the saving.',
        },
    ]


def lesson03_examples():
    """Chunk Processing"""
    return [
        {
            'tab': 'Read in Chunks',
            'domain': 'Logs',
            'title': 'Read in Chunks',
            'pills': ['chunksize', 'iterator'],
            'desc': 'This script reads a large CSV in 10,000-row chunks instead of loading the entire file at once. Each chunk is a normal DataFrame.',
            'filename': 'read_chunks.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'chunks = pd.read_csv(&quot;logs.csv&quot;, chunksize=10_000)  # iterator\n'
                '\n'
                'for i, chunk in enumerate(chunks):       # loop over chunks\n'
                '    rows = len(chunk)                     # rows in this chunk\n'
                '    print(f&quot;Chunk {i}: {rows} rows&quot;)    # progress report'
            ),
            'cmd': '$ python read_chunks.py',
            'output': 'Chunk 0: 10000 rows<br>Chunk 1: 10000 rows<br>Chunk 2: 4500 rows',
            'tip': 'Start with chunksize=10_000 and increase it until memory use is comfortable &#8212; larger chunks process faster but use more RAM.',
        },
        {
            'tab': 'Filter Each Chunk',
            'domain': 'Transactions',
            'title': 'Filter Each Chunk',
            'pills': ['filter', 'append results'],
            'desc': 'This script filters each chunk for rows that match a condition and collects only the matching rows. The full file never sits in memory at once.',
            'filename': 'filter_chunks.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'results = []  # collect matching rows\n'
                '\n'
                'for chunk in pd.read_csv(&quot;txns.csv&quot;, chunksize=50_000):\n'
                '    high = chunk[chunk[&quot;amount&quot;] &gt; 1000]  # filter this chunk\n'
                '    results.append(high)                    # keep matches\n'
                '\n'
                'df = pd.concat(results, ignore_index=True)  # combine\n'
                'print(f&quot;Found {len(df)} high-value transactions&quot;)'
            ),
            'cmd': '$ python filter_chunks.py',
            'output': 'Found 2,347 high-value transactions',
            'tip': 'Filtering inside the loop keeps only the rows you need &#8212; the rest are discarded before the next chunk arrives.',
        },
        {
            'tab': 'Aggregate Chunks',
            'domain': 'Sales',
            'title': 'Aggregate Chunks',
            'pills': ['running total', 'sum()'],
            'desc': 'This script calculates a running total across chunks. Each chunk adds its sum to a counter, so you get the grand total without loading everything.',
            'filename': 'agg_chunks.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'total = 0  # running total\n'
                '\n'
                'for chunk in pd.read_csv(&quot;sales.csv&quot;, chunksize=25_000):\n'
                '    total += chunk[&quot;revenue&quot;].sum()  # add this chunk&apos;s total\n'
                '\n'
                'print(f&quot;Grand total: ${total:,.2f}&quot;)'
            ),
            'cmd': '$ python agg_chunks.py',
            'output': 'Grand total: $4,872,350.00',
            'tip': 'For simple aggregations like sum, mean, or count, accumulate a running result &#8212; there is no need to keep any rows after each chunk.',
        },
    ]


def lesson04_examples():
    """Processing Millions of Rows"""
    return [
        {
            'tab': 'Vectorised Calculation',
            'domain': 'Orders',
            'title': 'Vectorised Calculation',
            'pills': ['column math', 'no loops'],
            'desc': 'This script calculates total price by multiplying two columns directly. Pandas runs the operation in compiled C code, processing millions of rows in milliseconds.',
            'filename': 'vectorised.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;orders.csv&quot;)  # load order data\n'
                '\n'
                'df[&quot;total&quot;] = df[&quot;qty&quot;] * df[&quot;price&quot;]  # multiply columns directly\n'
                '\n'
                'print(f&quot;Calculated {len(df):,} rows&quot;)\n'
                'print(df[[&quot;qty&quot;, &quot;price&quot;, &quot;total&quot;]].head())'
            ),
            'cmd': '$ python vectorised.py',
            'output': 'Calculated 2,000,000 rows<br>   qty  price    total<br>0    3  29.99    89.97<br>1    1  49.99    49.99',
            'tip': 'Vectorised column math is 50&#8211;100x faster than a Python for-loop &#8212; always reach for it before writing a loop.',
        },
        {
            'tab': 'Replace a For-Loop',
            'domain': 'Products',
            'title': 'Replace a For-Loop',
            'pills': ['np.where()', 'conditional'],
            'desc': 'This script replaces a slow row-by-row loop with a single <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">np.where()</code> call. The conditional logic runs across the entire column at once.',
            'filename': 'replace_loop.py',
            'code': (
                'import pandas as pd\n'
                'import numpy as np\n'
                '\n'
                'df = pd.read_csv(&quot;products.csv&quot;)  # load product data\n'
                '\n'
                'df[&quot;label&quot;] = np.where(\n'
                '    df[&quot;price&quot;] &gt; 100,  # condition\n'
                '    &quot;premium&quot;,            # value if true\n'
                '    &quot;standard&quot;            # value if false\n'
                ')\n'
                'print(df[[&quot;product&quot;, &quot;price&quot;, &quot;label&quot;]].head())'
            ),
            'cmd': '$ python replace_loop.py',
            'output': '    product  price     label<br>0    Laptop  999.0   premium<br>1     Mouse   25.0  standard',
            'tip': 'Use np.where() for simple if/else logic and np.select() when you need more than two categories.',
        },
        {
            'tab': 'Time Your Code',
            'domain': 'Benchmarks',
            'title': 'Time Your Code',
            'pills': ['time module', 'profiling'],
            'desc': 'This script measures how long a pandas operation takes. Timing each step reveals which part of your pipeline is the bottleneck.',
            'filename': 'time_code.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'df = pd.read_csv(&quot;big_data.csv&quot;)  # load data\n'
                '\n'
                'start = time.time()                            # start timer\n'
                'result = df.groupby(&quot;region&quot;)[&quot;revenue&quot;].sum()  # operation\n'
                'elapsed = time.time() - start                  # stop timer\n'
                'print(f&quot;Groupby took {elapsed:.3f} seconds&quot;)'
            ),
            'cmd': '$ python time_code.py',
            'output': 'Groupby took 0.142 seconds',
            'tip': 'Always time operations on your actual data size &#8212; a function that is fast on 1,000 rows may be slow on 10 million.',
        },
    ]


def lesson05_examples():
    """Columnar Storage"""
    return [
        {
            'tab': 'Compare File Sizes',
            'domain': 'Analytics',
            'title': 'Compare File Sizes',
            'pills': ['os.path.getsize()', 'CSV vs Parquet'],
            'desc': 'This script saves the same DataFrame as CSV and Parquet, then compares the file sizes. Columnar formats compress data far more efficiently.',
            'filename': 'compare_sizes.py',
            'code': (
                'import pandas as pd\n'
                'import os\n'
                '\n'
                'df = pd.read_csv(&quot;analytics.csv&quot;)              # load data\n'
                'df.to_csv(&quot;output.csv&quot;, index=False)            # save as CSV\n'
                'df.to_parquet(&quot;output.parquet&quot;, index=False)    # save as Parquet\n'
                '\n'
                'csv_mb = os.path.getsize(&quot;output.csv&quot;) / 1_048_576\n'
                'pq_mb = os.path.getsize(&quot;output.parquet&quot;) / 1_048_576\n'
                'print(f&quot;CSV: {csv_mb:.1f} MB  Parquet: {pq_mb:.1f} MB&quot;)'
            ),
            'cmd': '$ python compare_sizes.py',
            'output': 'CSV: 48.2 MB  Parquet: 8.7 MB',
            'tip': 'Parquet files are typically 3&#8211;5x smaller than CSV for the same data because they compress each column independently.',
        },
        {
            'tab': 'Read Selected Columns',
            'domain': 'Warehouse',
            'title': 'Read Selected Columns',
            'pills': ['columns=[]', 'skip unneeded data'],
            'desc': 'This script reads only two columns from a Parquet file. The columnar format skips all other columns on disk, making the load much faster.',
            'filename': 'read_columns.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_parquet(\n'
                '    &quot;warehouse.parquet&quot;,\n'
                '    columns=[&quot;product&quot;, &quot;qty&quot;]  # read only these columns\n'
                ')\n'
                '\n'
                'print(f&quot;Loaded {len(df):,} rows, {len(df.columns)} columns&quot;)\n'
                'print(df.head())'
            ),
            'cmd': '$ python read_columns.py',
            'output': 'Loaded 500,000 rows, 2 columns<br>   product  qty<br>0   Widget   12<br>1   Gadget    5',
            'tip': 'Always specify the columns you need &#8212; reading two columns from a 50-column Parquet file is 25x less data from disk.',
        },
        {
            'tab': 'Row vs Column Layout',
            'domain': 'Benchmarks',
            'title': 'Row vs Column Layout',
            'pills': ['read_csv() vs read_parquet()', 'timing'],
            'desc': 'This script times loading the same data from CSV versus Parquet, showing the speed advantage of columnar storage for analytical queries.',
            'filename': 'row_vs_col.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'start = time.time()\n'
                'csv_df = pd.read_csv(&quot;data.csv&quot;, usecols=[&quot;revenue&quot;])\n'
                'csv_time = time.time() - start\n'
                '\n'
                'start = time.time()\n'
                'pq_df = pd.read_parquet(&quot;data.parquet&quot;, columns=[&quot;revenue&quot;])\n'
                'pq_time = time.time() - start\n'
                'print(f&quot;CSV: {csv_time:.3f}s  Parquet: {pq_time:.3f}s&quot;)'
            ),
            'cmd': '$ python row_vs_col.py',
            'output': 'CSV: 1.240s  Parquet: 0.085s',
            'tip': 'Parquet reads only the requested column bytes from disk while CSV must scan through every row &#8212; the gap widens as columns increase.',
        },
    ]


def lesson06_examples():
    """Parquet Files"""
    return [
        {
            'tab': 'Write to Parquet',
            'domain': 'Reports',
            'title': 'Write to Parquet',
            'pills': ['to_parquet()', 'binary format'],
            'desc': 'This script saves a DataFrame as a Parquet file. Column types are embedded automatically, so you do not need to specify them when reading later.',
            'filename': 'write_parquet.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;report.csv&quot;)  # load CSV data\n'
                '\n'
                'df.to_parquet(&quot;report.parquet&quot;, index=False)  # save as Parquet\n'
                '\n'
                'print(f&quot;Saved {len(df):,} rows to report.parquet&quot;)'
            ),
            'cmd': '$ python write_parquet.py',
            'output': 'Saved 150,000 rows to report.parquet',
            'tip': 'Parquet preserves column types &#8212; unlike CSV, you will not lose date or integer types when you reload the file.',
        },
        {
            'tab': 'Round-Trip Check',
            'domain': 'Quality',
            'title': 'Round-Trip Check',
            'pills': ['read_parquet()', 'dtypes'],
            'desc': 'This script saves to Parquet and reads it back, then compares the column types. A round-trip check confirms nothing changed during the save.',
            'filename': 'round_trip.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;data.csv&quot;, parse_dates=[&quot;date&quot;])\n'
                'df.to_parquet(&quot;data.parquet&quot;, index=False)  # save\n'
                '\n'
                'df2 = pd.read_parquet(&quot;data.parquet&quot;)        # reload\n'
                'print(&quot;Types match:&quot;, df.dtypes.equals(df2.dtypes))\n'
                'print(df2.dtypes)'
            ),
            'cmd': '$ python round_trip.py',
            'output': 'Types match: True<br>date       datetime64[ns]<br>amount            float64<br>region             object<br>dtype: object',
            'tip': 'CSV loses date types on save and reload &#8212; Parquet keeps them intact, so you never need to re-parse dates.',
        },
        {
            'tab': 'Parquet vs CSV Size',
            'domain': 'Storage',
            'title': 'Parquet vs CSV Size',
            'pills': ['compression', 'snappy'],
            'desc': 'This script saves the same data with and without compression, showing how much space Parquet saves compared to CSV.',
            'filename': 'parquet_size.py',
            'code': (
                'import pandas as pd\n'
                'import os\n'
                '\n'
                'df = pd.read_csv(&quot;big_table.csv&quot;)  # load data\n'
                '\n'
                'df.to_parquet(&quot;default.parquet&quot;)  # snappy compression (default)\n'
                'df.to_csv(&quot;output.csv&quot;, index=False)\n'
                '\n'
                'pq = os.path.getsize(&quot;default.parquet&quot;) / 1_048_576\n'
                'csv_s = os.path.getsize(&quot;output.csv&quot;) / 1_048_576\n'
                'print(f&quot;CSV: {csv_s:.1f} MB  Parquet: {pq:.1f} MB&quot;)'
            ),
            'cmd': '$ python parquet_size.py',
            'output': 'CSV: 62.4 MB  Parquet: 11.8 MB',
            'tip': 'Parquet uses Snappy compression by default &#8212; switch to compression=&quot;gzip&quot; for even smaller files at the cost of slower writes.',
        },
    ]


def lesson13_examples():
    """Performance Profiling"""
    return [
        {
            'tab': 'Time Each Step',
            'domain': 'Pipeline',
            'title': 'Time Each Step',
            'pills': ['time module', 'elapsed'],
            'desc': 'This script measures how long each step of a data pipeline takes. You can immediately see which step is the bottleneck.',
            'filename': 'time_steps.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'start = time.time()\n'
                'df = pd.read_csv(&quot;data.csv&quot;)                   # step 1\n'
                'print(f&quot;Load: {time.time() - start:.3f}s&quot;)\n'
                '\n'
                'start = time.time()\n'
                'result = df.groupby(&quot;region&quot;)[&quot;revenue&quot;].sum()  # step 2\n'
                'print(f&quot;Group: {time.time() - start:.3f}s&quot;)'
            ),
            'cmd': '$ python time_steps.py',
            'output': 'Load: 1.450s<br>Group: 0.032s',
            'tip': 'If loading is the slowest step, switch to Parquet &#8212; if grouping is slow, check whether the column types are correct.',
        },
        {
            'tab': 'Profile with cProfile',
            'domain': 'Functions',
            'title': 'Profile with cProfile',
            'pills': ['cProfile', 'cumulative time'],
            'desc': 'This script uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">cProfile</code> to measure the total time spent in each function call. The output ranks functions by cumulative time.',
            'filename': 'profile_code.py',
            'code': (
                'import pandas as pd\n'
                'import cProfile\n'
                '\n'
                'def pipeline():\n'
                '    df = pd.read_csv(&quot;data.csv&quot;)                   # load\n'
                '    summary = df.groupby(&quot;region&quot;)[&quot;revenue&quot;].sum()  # group\n'
                '    summary.to_csv(&quot;summary.csv&quot;)                  # save\n'
                '\n'
                'cProfile.run(&quot;pipeline()&quot;, sort=&quot;cumulative&quot;)'
            ),
            'cmd': '$ python profile_code.py',
            'output': '   ncalls  tottime  cumtime  filename:lineno(function)<br>        1    0.000    1.520  profile_code.py:4(pipeline)<br>        1    1.200    1.200  {read_csv}',
            'tip': 'Sort by cumulative time to see which function call uses the most time &#8212; that is the first place to optimise.',
        },
        {
            'tab': 'Before and After',
            'domain': 'Optimisation',
            'title': 'Before and After',
            'pills': ['baseline', 'comparison'],
            'desc': 'This script records baseline timing, applies an optimisation, and compares the results. Documenting both numbers proves the improvement.',
            'filename': 'before_after.py',
            'code': (
                'import pandas as pd\n'
                'import time\n'
                '\n'
                'start = time.time()\n'
                'df_csv = pd.read_csv(&quot;data.csv&quot;, usecols=[&quot;revenue&quot;])\n'
                'csv_time = time.time() - start  # baseline: CSV\n'
                '\n'
                'start = time.time()\n'
                'df_pq = pd.read_parquet(&quot;data.parquet&quot;, columns=[&quot;revenue&quot;])\n'
                'pq_time = time.time() - start   # optimised: Parquet\n'
                'print(f&quot;CSV: {csv_time:.3f}s  Parquet: {pq_time:.3f}s&quot;)'
            ),
            'cmd': '$ python before_after.py',
            'output': 'CSV: 1.350s  Parquet: 0.072s',
            'tip': 'Always record the baseline time before optimising &#8212; without it, you cannot prove the change was worth the effort.',
        },
    ]


REGISTRY = {
    "lesson02_memory_optimization.html": lesson02_examples,
    "lesson03_chunk_processing.html": lesson03_examples,
    "lesson04_processing_millions_of_rows.html": lesson04_examples,
    "lesson05_columnar_storage.html": lesson05_examples,
    "lesson06_parquet_files.html": lesson06_examples,
    "lesson13_performance_profiling.html": lesson13_examples,
}


def main():
    for fname, fn in REGISTRY.items():
        fpath = ROOT / fname
        if not fpath.exists():
            print(f"  SKIP  {fname} (not found)")
            continue
        html = fpath.read_text(encoding="utf-8")
        examples = fn()
        new_section = make_section(examples)
        new_html, count = SECTION_RE.subn(new_section, html)
        if count == 0:
            print(f"  WARN  {fname} (no #code-examples section)")
            continue
        fpath.write_text(new_html, encoding="utf-8")
        print(f"  OK    {fname} ({len(examples)} examples)")
    print("\nDone.")


if __name__ == "__main__":
    main()
