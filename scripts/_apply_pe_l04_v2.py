#!/usr/bin/env python3
"""Rebuild the #practice section for lesson02_etl_elt_pipeline_thinking.html.

Changes:
- Expands from 3 to 4 tabs (adds Exercise 4 — Batch vs Streaming)
- Adds numbered sub-task lists to every task-box (2–4 tasks per exercise)
- Adds Show Solution accordion with Style A code block to every panel
- Adds "Why this matters" sentence inside each accordion
- Removes Exercise 2's immediate answer reveal (moves it behind Show Solution)
"""

import re

TARGET = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson02_etl_elt_pipeline_thinking.html"

NEW_SECTION = """\
<section id="practice">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Hands-on tasks to reinforce the concepts</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

<div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
  <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
    <span class="pe-step-label text-xs font-bold">Exercise 1</span>
  </button>
  <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
    <span class="pe-step-label text-xs font-bold">Exercise 2</span>
  </button>
  <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
    <span class="pe-step-label text-xs font-bold">Exercise 3</span>
  </button>
  <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
    <span class="pe-step-label text-xs font-bold">Exercise 4</span>
  </button>
</div>

<!-- ── Exercise 1 — Modular ETL Pipeline ─────────────────────────────── -->
<div class="pe-panel pe-panel-anim" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Exercise 1 &mdash; Write a Modular ETL Pipeline</h3>
          <p class="text-xs text-gray-400 mt-0.5">Objective: Write modular, reusable pipeline functions</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="flex-1">
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Your Tasks</p>
          <ol class="space-y-1.5 text-sm text-gray-600 list-decimal pl-4">
            <li>Write an <code>extract(filepath)</code> function that reads <code>orders.csv</code> and prints how many rows were loaded.</li>
            <li>Complete the <code>transform(df)</code> function in the starter code: drop nulls in <code>customer_id</code> and <code>total</code>, parse <code>order_date</code> as datetime, remove rows where <code>total &lt; 0</code>, and add a <code>tax</code> column equal to <code>total * 0.1</code>.</li>
            <li>Write a <code>load(df, engine, table)</code> function that writes to SQLite using <code>if_exists='replace'</code> and logs the row count after loading.</li>
            <li>Wire all three in a <code>run()</code> function and call it to verify the pipeline completes end-to-end.</li>
          </ol>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">exercise_01_starter.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd
from sqlalchemy import create_engine

def extract(filepath):
    pass  # TODO: read CSV and return DataFrame, print row count

def transform(df):
    # TODO: drop nulls in &#x27;customer_id&#x27; and &#x27;total&#x27;
    # TODO: parse &#x27;order_date&#x27; as datetime
    # TODO: remove rows where total &lt; 0
    # TODO: add &#x27;tax&#x27; column = total * 0.1
    return df

def load(df, engine, table):
    pass  # TODO: write to SQLite with if_exists=&#x27;replace&#x27;, log row count

def run():
    engine = create_engine(&quot;sqlite:///orders.db&quot;)
    # TODO: call extract, transform, and load in sequence
    pass

run()</code></pre>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <div class="flex items-center gap-2">
          <span class="iconify text-brand" data-icon="fa6-solid:eye"></span>
          Show Solution
        </div>
        <span class="iconify accordion-chevron text-gray-400 text-xs" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">exercise_01_solution.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd
from sqlalchemy import create_engine

def extract(filepath):
    df = pd.read_csv(filepath)              # read the source CSV from disk
    print(f&quot;Extracted {len(df):,} rows&quot;)   # log the raw row count immediately
    return df

def transform(df):
    df = df.dropna(subset=[&quot;customer_id&quot;, &quot;total&quot;])   # remove rows missing critical fields
    df[&quot;order_date&quot;] = pd.to_datetime(df[&quot;order_date&quot;])  # parse date strings to Timestamp
    df = df[df[&quot;total&quot;] &gt;= 0]              # discard refund or data-error rows
    df[&quot;tax&quot;] = df[&quot;total&quot;] * 0.1          # derive a 10% tax column from total
    print(f&quot;Transformed: {len(df):,} rows remain&quot;)
    return df

def load(df, engine, table):
    df.to_sql(table, engine, if_exists=&quot;replace&quot;, index=False)  # full refresh — idempotent
    print(f&quot;Loaded {len(df):,} rows into &#x27;{table}&#x27;&quot;)

def run():
    engine = create_engine(&quot;sqlite:///orders.db&quot;)
    raw    = extract(&quot;orders.csv&quot;)           # step 1 — read source file
    clean  = transform(raw)                   # step 2 — clean and enrich
    load(clean, engine, &quot;orders&quot;)             # step 3 — write to warehouse
    print(&quot;Pipeline complete&quot;)

run()</code></pre>
          </div>
        </div>
        <p class="text-xs text-gray-500 mt-3 italic">Why this matters: splitting extract, transform, and load into separate functions means that if the load step fails at midnight, you fix and rerun only that one function without re-downloading or re-cleaning all the data — critical when your source is a slow API or a multi-gigabyte CSV file.</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Exercise 2 — ETL vs ELT Pattern Annotation ────────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Exercise 2 &mdash; Annotate ETL and ELT Pipelines</h3>
          <p class="text-xs text-gray-400 mt-0.5">Objective: Contrast ETL and ELT pipeline patterns</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="flex-1">
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Your Tasks</p>
          <ol class="space-y-1.5 text-sm text-gray-600 list-decimal pl-4">
            <li>For each pipeline script below, add a comment at the top labelling it as either <code>ETL</code> or <code>ELT</code>.</li>
            <li>On the line that performs (or skips) the transformation, add a comment stating <em>where</em> the transform runs &mdash; in Python or inside the warehouse.</li>
            <li>Rewrite Script A as ELT: remove the Python transform, load the raw DataFrame directly, and add a SQL comment showing what the equivalent warehouse query would look like.</li>
          </ol>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">exercise_02_starter.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd
from sqlalchemy import create_engine

# ── Script A ────────────────────────────────────────────
# Pattern: ???
engine_a = create_engine(&quot;sqlite:///warehouse.db&quot;)
df = pd.read_csv(&quot;events.csv&quot;)
df[&quot;revenue&quot;] = df[&quot;quantity&quot;] * df[&quot;unit_price&quot;]  # transform: ???
df.to_sql(&quot;events_summary&quot;, engine_a, if_exists=&quot;replace&quot;, index=False)

# ── Script B ────────────────────────────────────────────
# Pattern: ???
engine_b = create_engine(&quot;sqlite:///warehouse.db&quot;)
raw = pd.read_csv(&quot;events.csv&quot;)
raw.to_sql(&quot;events_raw&quot;, engine_b, if_exists=&quot;replace&quot;, index=False)
# A dbt model or SQL query runs here afterward — transform: ???</code></pre>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <div class="flex items-center gap-2">
          <span class="iconify text-brand" data-icon="fa6-solid:eye"></span>
          Show Solution
        </div>
        <span class="iconify accordion-chevron text-gray-400 text-xs" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">exercise_02_solution.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd
from sqlalchemy import create_engine

# ── Script A — ETL ──────────────────────────────────────
# Pattern: ETL — transform happens in Python before loading
engine_a = create_engine(&quot;sqlite:///warehouse.db&quot;)
df = pd.read_csv(&quot;events.csv&quot;)
df[&quot;revenue&quot;] = df[&quot;quantity&quot;] * df[&quot;unit_price&quot;]  # transform runs in Python (ETL)
df.to_sql(&quot;events_summary&quot;, engine_a, if_exists=&quot;replace&quot;, index=False)

# ── Script A rewritten as ELT ───────────────────────────
# Pattern: ELT — load raw first, transform inside the warehouse
engine_a2 = create_engine(&quot;sqlite:///warehouse.db&quot;)
raw = pd.read_csv(&quot;events.csv&quot;)                      # extract only — no Python transform
raw.to_sql(&quot;events_raw&quot;, engine_a2, if_exists=&quot;replace&quot;, index=False)  # load raw to warehouse
# SQL transform runs inside the warehouse (ELT):
# SELECT quantity * unit_price AS revenue FROM events_raw

# ── Script B — ELT ──────────────────────────────────────
# Pattern: ELT — raw data loaded first, transform happens inside the warehouse
engine_b = create_engine(&quot;sqlite:///warehouse.db&quot;)
raw = pd.read_csv(&quot;events.csv&quot;)
raw.to_sql(&quot;events_raw&quot;, engine_b, if_exists=&quot;replace&quot;, index=False)  # load raw — transform: SQL
# SELECT quantity * unit_price AS revenue FROM events_raw  &larr; warehouse runs this (ELT)</code></pre>
          </div>
        </div>
        <p class="text-xs text-gray-500 mt-3 italic">Why this matters: knowing which pattern a pipeline uses tells you immediately where to look when the output is wrong &mdash; if it is ETL and the numbers are off, the bug is in your Python transform; if it is ELT and the numbers are off, the bug is in your SQL model or dbt macro.</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Exercise 3 — Fix the Idempotency Bug ──────────────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Exercise 3 &mdash; Fix the Idempotency Bug</h3>
          <p class="text-xs text-gray-400 mt-0.5">Objective: Apply pipeline design principles &mdash; idempotency and validation</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="flex-1">
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Your Tasks</p>
          <ol class="space-y-1.5 text-sm text-gray-600 list-decimal pl-4">
            <li>Read the pipeline below. Trace what happens to the <code>sales</code> table if you call <code>run()</code> three times in a row, then write one comment in the code explaining the problem.</li>
            <li>Fix the <code>load()</code> function so the pipeline is idempotent &mdash; running it any number of times must produce exactly the same result in the database.</li>
            <li>Add a row-count guard in <code>transform()</code>: if more than 20% of input rows are dropped, raise a <code>ValueError</code> that states how many rows were lost and what percentage that represents.</li>
          </ol>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">exercise_03_starter.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd
from sqlalchemy import create_engine

def extract(filepath):
    return pd.read_csv(filepath)

def transform(df):
    df = df.dropna(subset=[&quot;order_id&quot;, &quot;total&quot;])  # remove incomplete rows
    df[&quot;total&quot;] = df[&quot;total&quot;].abs()               # convert negatives to positive
    return df

def load(df, engine):
    df.to_sql(&quot;sales&quot;, engine, if_exists=&quot;append&quot;, index=False)  # BUG: doubles rows on re-run

def run():
    engine = create_engine(&quot;sqlite:///sales.db&quot;)
    raw    = extract(&quot;orders.csv&quot;)
    clean  = transform(raw)
    load(clean, engine)

run()</code></pre>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <div class="flex items-center gap-2">
          <span class="iconify text-brand" data-icon="fa6-solid:eye"></span>
          Show Solution
        </div>
        <span class="iconify accordion-chevron text-gray-400 text-xs" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">exercise_03_solution.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd
from sqlalchemy import create_engine

def extract(filepath):
    return pd.read_csv(filepath)

def transform(df):
    raw_count = len(df)                                  # record starting row count before drops
    df = df.dropna(subset=[&quot;order_id&quot;, &quot;total&quot;])      # remove incomplete rows
    df[&quot;total&quot;] = df[&quot;total&quot;].abs()                    # convert negatives to positive
    dropped = raw_count - len(df)                        # calculate how many rows were removed
    if dropped / raw_count &gt; 0.20:                      # guard: &gt;20% row loss is suspicious
        raise ValueError(
            f&quot;Transform dropped {dropped:,} rows &quot;
            f&quot;({dropped / raw_count:.0%} of {raw_count:,}). Aborting load.&quot;
        )
    return df

def load(df, engine):
    df.to_sql(&quot;sales&quot;, engine, if_exists=&quot;replace&quot;, index=False)  # FIXED: replace not append
    print(f&quot;Loaded {len(df):,} rows into &#x27;sales&#x27;&quot;)

def run():
    engine = create_engine(&quot;sqlite:///sales.db&quot;)
    raw    = extract(&quot;orders.csv&quot;)
    clean  = transform(raw)
    print(f&quot;Passing {len(clean):,} clean rows to load&quot;)  # confirm count before write
    load(clean, engine)
    print(&quot;Done — pipeline is idempotent&quot;)

run()</code></pre>
          </div>
        </div>
        <p class="text-xs text-gray-500 mt-3 italic">Why this matters: a pipeline that silently appends duplicate rows on every re-run raises no error and produces plausible-looking totals until someone audits the data days later; the 20% guard makes suspicious data loss loud and immediate, so failures are caught in seconds rather than discovered in a board report.</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Exercise 4 — Batch vs Streaming Patterns ──────────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Exercise 4 &mdash; Simulate a Streaming Pipeline</h3>
          <p class="text-xs text-gray-400 mt-0.5">Objective: Recognize batch vs streaming patterns and write a generator</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="flex-1">
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Your Tasks</p>
          <ol class="space-y-1.5 text-sm text-gray-600 list-decimal pl-4">
            <li>Read the batch pipeline in the starter code. Identify the single line that makes it batch rather than streaming, and add a comment on that line explaining why.</li>
            <li>Write a <code>simulate_stream(filepath)</code> generator function that reads the CSV once but <code>yield</code>s one row as a <code>dict</code> at a time, simulating a Kafka or Pub/Sub message stream.</li>
            <li>Write a <code>process_stream(generator)</code> function that iterates the generator, skips rows where <code>total</code> is <code>None</code>, adds a <code>tax</code> field equal to <code>total * 0.1</code>, and prints each processed record.</li>
          </ol>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text="gray-400">exercise_04_starter.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

# ── Batch pipeline (runs once per hour from a scheduler) ────
def extract_batch(filepath):
    return pd.read_csv(filepath)           # reads ALL rows into memory at once

def transform_batch(df):
    df = df.dropna(subset=[&quot;total&quot;])
    df[&quot;tax&quot;] = df[&quot;total&quot;] * 0.1
    return df

def run_batch():
    df = extract_batch(&quot;orders.csv&quot;)
    df = transform_batch(df)
    print(f&quot;Batch processed {len(df):,} rows&quot;)

run_batch()

# ── Streaming pipeline (your code goes here) ────────────────
def simulate_stream(filepath):
    pass  # TODO: read CSV, yield one row dict at a time

def process_stream(generator):
    pass  # TODO: iterate, skip None totals, add tax, print each record

process_stream(simulate_stream(&quot;orders.csv&quot;))</code></pre>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <div class="flex items-center gap-2">
          <span class="iconify text-brand" data-icon="fa6-solid:eye"></span>
          Show Solution
        </div>
        <span class="iconify accordion-chevron text-gray-400 text-xs" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">exercise_04_solution.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

# ── Batch pipeline (unchanged reference) ────────────────────
def extract_batch(filepath):
    return pd.read_csv(filepath)  # BATCH: this line loads ALL rows into memory at once

def transform_batch(df):
    df = df.dropna(subset=[&quot;total&quot;])   # remove rows with no total
    df[&quot;tax&quot;] = df[&quot;total&quot;] * 0.1     # add derived column
    return df

def run_batch():
    df = extract_batch(&quot;orders.csv&quot;)
    df = transform_batch(df)
    print(f&quot;Batch processed {len(df):,} rows&quot;)

# ── Streaming simulation ─────────────────────────────────────
def simulate_stream(filepath):
    &quot;&quot;&quot;Generator that yields one order dict at a time — simulates a Kafka message stream.&quot;&quot;&quot;
    df = pd.read_csv(filepath)          # read source (in production: use a Kafka consumer)
    for _, row in df.iterrows():        # iterate one row at a time — not all in memory at once
        yield row.to_dict()             # yield a single record as a plain dict

def process_stream(generator):
    &quot;&quot;&quot;Processes each incoming record individually as it arrives from the stream.&quot;&quot;&quot;
    for record in generator:                    # iterate until the stream ends
        if record.get(&quot;total&quot;) is None:         # guard: skip records missing a total value
            continue
        record[&quot;tax&quot;] = record[&quot;total&quot;] * 0.1  # apply per-record transform in place
        print(
            f&quot;order {record.get(&#x27;order_id&#x27;, &#x27;?&#x27;)}: &quot;
            f&quot;total={record[&#x27;total&#x27;]:.2f}, tax={record[&#x27;tax&#x27;]:.2f}&quot;
        )

process_stream(simulate_stream(&quot;orders.csv&quot;))</code></pre>
          </div>
        </div>
        <p class="text-xs text-gray-500 mt-3 italic">Why this matters: real streaming pipelines (Kafka, Pub/Sub, Kinesis) deliver one event at a time and never give you a complete batch to load into a DataFrame &mdash; understanding Python generators prepares you to handle live data sources where you must process each record immediately rather than accumulating everything before acting.</p>
      </div>
    </div>
  </div>
</div>

    </div>
  </div>
</section>"""

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# Find and replace the practice section
old_match = re.search(r'<section id="practice">.*?</section>', content, re.DOTALL)
if old_match:
    content = content[: old_match.start()] + NEW_SECTION + content[old_match.end():]
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Practice section rebuilt: 4 tabs, numbered tasks, Show Solution accordions")
else:
    print("❌ Could not find <section id=\"practice\">")
