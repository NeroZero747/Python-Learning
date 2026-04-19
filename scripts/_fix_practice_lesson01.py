"""
Replace the #practice section in lesson01 with 4 properly structured exercises:
  0 — Explore a Pipeline       (Data Pipeline objective)
  1 — Classify Data Roles      (DE vs DA vs DS objective)
  2 — Query Warehouse Data     (Data Warehouse objective)
  3 — Validate Data Quality    (Data Quality objective)

Fixes applied:
- Drop generic "Exercise 1/2/3" labels and traffic-light dots
- Add proper task-box with 2–4 numbered sub-tasks per panel
- "Show Solution" accordion with Style A code block (no terminal pane)
- "Why this matters" sentence after every solution
- Panel format consistent across all 4 tabs
- Icon updated from fa6-solid:dumbbell → fa6-solid:pencil (per spec)
- Reduce from 5 tabs → 4 tabs (1 per objective)
"""

import re
from pathlib import Path

TARGET = Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson01_what_is_data_engineering.html")

NEW_SECTION = r'''<section id="practice">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Guided exercises to reinforce your learning</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab buttons -->
      <div class="flex flex-wrap items-center gap-2 mb-6" role="tablist">
        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:diagram-project"></span>
          <span class="pe-step-label text-xs font-bold">Explore a Pipeline</span>
        </button>
        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:users"></span>
          <span class="pe-step-label text-xs font-bold">Classify Data Roles</span>
        </button>
        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:database"></span>
          <span class="pe-step-label text-xs font-bold">Query Warehouse Data</span>
        </button>
        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:vial"></span>
          <span class="pe-step-label text-xs font-bold">Validate Data Quality</span>
        </button>
      </div>

      <!-- Panel 0: Explore a Pipeline -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:diagram-project"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Explore a Pipeline</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="text-[10px] text-gray-400 font-medium">Data Pipeline</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div class="w-full">
                <p class="text-xs font-bold uppercase tracking-widest mb-3 text-brand">Your Tasks</p>
                <ol class="text-sm text-gray-700 space-y-2 list-decimal list-inside">
                  <li>Import pandas and load <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">students.csv</code> into a DataFrame called <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">df</code>.</li>
                  <li>Print the number of rows and columns using <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">df.shape</code>.</li>
                  <li>Preview the first three rows with <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">df.head(3)</code> to understand the data structure.</li>
                  <li>Print all column names using <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">df.columns.tolist()</code> so you know what fields the pipeline carries.</li>
                </ol>
              </div>
            </div>
            <div>
              <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
                <span class="flex items-center gap-2">
                  <span class="iconify text-[#CB187D] text-sm" data-icon="fa6-solid:lightbulb"></span>
                  Show Solution
                </span>
                <span class="iconify accordion-chevron text-[10px] text-gray-400" data-icon="fa6-solid:chevron-down"></span>
              </button>
              <div class="accordion-body mt-3">
                <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                    <div class="flex items-center gap-3">
                      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                        <span class="text-[11px] font-semibold text-gray-400">explore_pipeline.py</span>
                      </div>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

df = pd.read_csv("students.csv")     # load the source file into a DataFrame
print(df.shape)                      # (rows, columns) — how big is this dataset?
print(df.head(3))                    # first 3 rows — what does the data look like?
print(df.columns.tolist())           # field names — what does the pipeline carry?</code></pre>
                  </div>
                </div>
                <p class="mt-3 text-xs text-gray-500 italic">Why this matters: before you build or debug any pipeline, you need to inspect the data it carries — checking shape and columns is the first thing every data engineer does.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 1: Classify Data Roles -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:users"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Classify Data Roles</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="text-[10px] text-gray-400 font-medium">DE vs DA vs DS</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div class="w-full">
                <p class="text-xs font-bold uppercase tracking-widest mb-3 text-brand">Your Tasks</p>
                <ol class="text-sm text-gray-700 space-y-2 list-decimal list-inside">
                  <li>Read the five job tasks listed below.</li>
                  <li>Assign each task a role label: <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">"DE"</code> (Data Engineer), <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">"DA"</code> (Data Analyst), or <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">"DS"</code> (Data Scientist).</li>
                  <li>Store your answers in a dictionary and print each task with its role label.</li>
                </ol>
                <div class="mt-3 rounded-lg bg-white border border-gray-200 px-4 py-3">
                  <p class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-2">Tasks to Classify</p>
                  <ul class="text-xs text-gray-600 space-y-1.5 list-disc list-inside">
                    <li>Build a pipeline to move sales data from MySQL to a data warehouse</li>
                    <li>Create a bar chart showing revenue by product category</li>
                    <li>Train a model that predicts whether a customer will churn</li>
                    <li>Write SQL to clean duplicate rows in a raw transactions table</li>
                    <li>Visualize how customer age correlates with average spend</li>
                  </ul>
                </div>
              </div>
            </div>
            <div>
              <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
                <span class="flex items-center gap-2">
                  <span class="iconify text-[#CB187D] text-sm" data-icon="fa6-solid:lightbulb"></span>
                  Show Solution
                </span>
                <span class="iconify accordion-chevron text-[10px] text-gray-400" data-icon="fa6-solid:chevron-down"></span>
              </button>
              <div class="accordion-body mt-3">
                <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                    <div class="flex items-center gap-3">
                      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                        <span class="text-[11px] font-semibold text-gray-400">classify_roles.py</span>
                      </div>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python"># Assign each task to the most appropriate role
tasks = {
    "Build a pipeline to move sales data from MySQL to a warehouse": "DE",
    "Create a bar chart showing revenue by product category":        "DA",
    "Train a model that predicts whether a customer will churn":     "DS",
    "Write SQL to clean duplicate rows in a raw transactions table": "DE",
    "Visualize how customer age correlates with average spend":      "DA",
}

for task, role in tasks.items():
    print(f"[{role}]  {task}")</code></pre>
                  </div>
                </div>
                <p class="mt-3 text-xs text-gray-500 italic">Why this matters: knowing which role owns which responsibility prevents work being duplicated or falling through the gaps when your team grows.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 2: Query Warehouse Data -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:database"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Query Warehouse Data</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="text-[10px] text-gray-400 font-medium">Data Warehouse</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div class="w-full">
                <p class="text-xs font-bold uppercase tracking-widest mb-3 text-brand">Your Tasks</p>
                <ol class="text-sm text-gray-700 space-y-2 list-decimal list-inside">
                  <li>Load <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">inventory.csv</code> — it has columns: <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">product</code>, <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">category</code>, <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">stock</code>, <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">price</code>.</li>
                  <li>Filter to rows where <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">stock &lt; 10</code> (low-stock items only).</li>
                  <li>Add a <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">value</code> column (<code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">stock × price</code>) and print the total value at risk.</li>
                  <li>Print the low-stock items sorted by price, highest first.</li>
                </ol>
              </div>
            </div>
            <div>
              <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
                <span class="flex items-center gap-2">
                  <span class="iconify text-[#CB187D] text-sm" data-icon="fa6-solid:lightbulb"></span>
                  Show Solution
                </span>
                <span class="iconify accordion-chevron text-[10px] text-gray-400" data-icon="fa6-solid:chevron-down"></span>
              </button>
              <div class="accordion-body mt-3">
                <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                    <div class="flex items-center gap-3">
                      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                        <span class="text-[11px] font-semibold text-gray-400">query_warehouse.py</span>
                      </div>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

inv = pd.read_csv("inventory.csv")              # load warehouse inventory data
low_stock = inv[inv["stock"] &lt; 10].copy()       # filter: low-stock rows only
low_stock["value"] = low_stock["stock"] * low_stock["price"]  # calc at-risk value

total = low_stock["value"].sum()
print(f"Total at-risk inventory value: ${total:,.2f}")

# Sort by price so the most expensive low-stock items appear first
print(low_stock.sort_values("price", ascending=False))</code></pre>
                  </div>
                </div>
                <p class="mt-3 text-xs text-gray-500 italic">Why this matters: data warehouses are designed for exactly this kind of filter-and-aggregate query — running it in Python mirrors the SQL you would write against a real warehouse.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 3: Validate Data Quality -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:vial"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Validate Data Quality</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="text-[10px] text-gray-400 font-medium">Data Quality</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div class="w-full">
                <p class="text-xs font-bold uppercase tracking-widest mb-3 text-brand">Your Tasks</p>
                <ol class="text-sm text-gray-700 space-y-2 list-decimal list-inside">
                  <li>Load <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">sales.csv</code> with pandas and print its shape.</li>
                  <li>Check for null values using <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">.isnull().sum()</code> and print only the columns that contain nulls.</li>
                  <li>Check for duplicate rows using <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">.duplicated().sum()</code> and print the count.</li>
                  <li>Write an <code class="font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200">assert</code> statement that raises an error if the DataFrame has fewer than 100 rows.</li>
                </ol>
              </div>
            </div>
            <div>
              <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
                <span class="flex items-center gap-2">
                  <span class="iconify text-[#CB187D] text-sm" data-icon="fa6-solid:lightbulb"></span>
                  Show Solution
                </span>
                <span class="iconify accordion-chevron text-[10px] text-gray-400" data-icon="fa6-solid:chevron-down"></span>
              </button>
              <div class="accordion-body mt-3">
                <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                    <div class="flex items-center gap-3">
                      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                        <span class="text-[11px] font-semibold text-gray-400">validate_quality.py</span>
                      </div>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

sales = pd.read_csv("sales.csv")              # load the pipeline output file
print(f"Shape: {sales.shape}")                # rows x columns

# Check for nulls per column
nulls = sales.isnull().sum()
print(nulls[nulls &gt; 0])                      # show only columns that have nulls

# Check for duplicate rows
dupes = sales.duplicated().sum()
print(f"Duplicate rows: {dupes}")

# Fail loudly if the dataset is suspiciously small
assert len(sales) &gt;= 100, "Too few rows — check the source file"
print("&#x2713; All quality checks passed")</code></pre>
                  </div>
                </div>
                <p class="mt-3 text-xs text-gray-500 italic">Why this matters: catching data problems early prevents silent errors from cascading through every downstream report or model that depends on this data.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
'''

html = TARGET.read_text(encoding="utf-8")

# Find the section and replace it
pattern = re.compile(r'<section id="practice">.*?(?=<section id="mistakes">)', re.DOTALL)
match = pattern.search(html)
if not match:
    print("❌ Could not find <section id='practice'>")
    exit(1)

old = match.group(0)
new_html = html.replace(old, NEW_SECTION, 1)

if new_html == html:
    print("⚠️  No change made — replacement string may already be applied")
    exit(0)

TARGET.write_text(new_html, encoding="utf-8")
print(f"✅ Patched: {TARGET.name}")

# --- DIV balance check ---
import re as _re

def div_balance(text):
    opens  = len(_re.findall(r'<div\b', text))
    closes = len(_re.findall(r'</div>', text))
    return opens - closes

old_balance  = div_balance(old)
new_balance  = div_balance(NEW_SECTION)
full_balance = div_balance(new_html)

print(f"  old section  div diff : {old_balance:+d}")
print(f"  new section  div diff : {new_balance:+d}")
print(f"  full file    div diff : {full_balance:+d}  ({'OK ✅' if full_balance == 0 else 'UNBALANCED ❌'})")
