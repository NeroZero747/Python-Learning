"""
Add two missing Code Examples tabs to lesson01:
  Tab 4 — "Data Roles in Action"  (DE vs DA vs DS objective)
  Tab 5 — "Write to a Warehouse"  (Data Warehouse objective)

Inserts:
  - Two new <button> tab elements in the tablist
  - Two new <div class="ce-panel ..."> panel blocks
"""

from pathlib import Path
import re

TARGET = Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson01_what_is_data_engineering.html")

# ── New tab buttons ────────────────────────────────────────────────────────────
NEW_BUTTONS = """
        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:users"></span>
          <span class="ce-step-label text-xs font-bold">Data Roles in Action</span>
        </button>

        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:database"></span>
          <span class="ce-step-label text-xs font-bold">Write to a Warehouse</span>
        </button>

      </div>"""

# ── New panels ─────────────────────────────────────────────────────────────────
NEW_PANELS = """
      <!-- Panel 4: Data Roles in Action -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:users"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Data Roles in Action</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Sales</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">DE / DA / DS</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script shows how the <strong class="text-gray-800">same sales data</strong> travels through three different roles — a Data Engineer prepares it, a Data Analyst summarizes it, and a Data Scientist engineers a feature from it.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">data_roles.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

# ── Data Engineer: clean and deliver the data ──────────────────────────
sales = pd.read_csv("sales.csv")                   # load raw source data
sales = sales.dropna(subset=["amount"])            # remove rows with no sale amount
sales["date"] = pd.to_datetime(sales["date"])      # convert text dates to datetime type
sales.to_csv("clean_sales.csv", index=False)       # deliver clean data downstream
print("DE: clean_sales.csv is ready\n")

# ── Data Analyst: answer a business question using the clean data ──────
monthly = sales.groupby(sales["date"].dt.month)["amount"].sum()
print("DA: total revenue per month")
print(monthly, "\n")                               # totals grouped by month number

# ── Data Scientist: engineer a feature for a predictive model ──────────
sales["sqrt_amount"] = sales["amount"] ** 0.5     # scale large values for ML
print("DS: feature engineering done — sqrt_amount column added")</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python data_roles.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">DE: clean_sales.csv is ready<br><br>DA: total revenue per month<br>date<br>1    48200.50<br>2    39100.00<br>3    55800.75<br><br>DS: feature engineering done — sqrt_amount column added</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Notice that the DE section runs first — analysts and scientists depend on clean data that engineers have already prepared and delivered.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 5: Write to a Warehouse -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:database"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Write to a Warehouse</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Orders</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">SQLite</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">to_sql()</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script loads a CSV, cleans it, then writes the result into a <strong class="text-gray-800">SQLite database</strong> — the same ETL pattern used with real data warehouses like BigQuery or Snowflake, just with a local file instead of a cloud server.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">write_warehouse.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd
import sqlite3

# Extract: load the raw source file
orders = pd.read_csv("orders.csv")
print(f"Loaded {len(orders)} orders from CSV")

# Transform: drop rows that are missing critical data
orders = orders.dropna(subset=["order_id", "amount"])

# Load: write the clean data into a SQLite database (our local "warehouse")
conn = sqlite3.connect("warehouse.db")             # create/open the database file
orders.to_sql("orders", conn,                      # table name in the warehouse
              if_exists="replace",                 # overwrite the table each run
              index=False)                         # do not store the DataFrame index

# Verify: query the warehouse to confirm the rows arrived
result = pd.read_sql("SELECT COUNT(*) AS total_rows FROM orders", conn)
print(result)                                      # should match the CSV row count
conn.close()                                       # always close the connection</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python write_warehouse.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Loaded 1248 orders from CSV<br>   total_rows<br>0        1241</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">The 7-row difference between the CSV count (1248) and the warehouse count (1241) shows that 7 rows were dropped during the transform step — always verify your load count matches expectations.</p>
            </div>
          </div>
        </div>
      </div>
"""

# ── Apply changes ──────────────────────────────────────────────────────────────
html = TARGET.read_text(encoding="utf-8")

# 1. Insert two new tab buttons before the closing </div> of the tablist
OLD_TABLIST_END = '''        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Run a Pipeline</span>
        </button>

      </div>'''

NEW_TABLIST_END = '''        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Run a Pipeline</span>
        </button>''' + NEW_BUTTONS

if OLD_TABLIST_END not in html:
    print("❌  Could not find tablist end — abort")
    exit(1)

html = html.replace(OLD_TABLIST_END, NEW_TABLIST_END, 1)
print("✅ Tab buttons inserted")

# 2. Insert two new panels before the </div></div></section> closing of #code-examples
# The section body closes with: </div>\n    </div>\n  </div>\n</section>\n\n<section id="practice">
OLD_SECTION_END = '''    </div>
  </div>
</section>

<section id="practice">'''

NEW_SECTION_END = NEW_PANELS + '''    </div>
  </div>
</section>

<section id="practice">'''

if OLD_SECTION_END not in html:
    print("❌  Could not find section end — abort")
    exit(1)

html = html.replace(OLD_SECTION_END, NEW_SECTION_END, 1)
print("✅ Panel content inserted")

TARGET.write_text(html, encoding="utf-8")
print(f"✅ Saved: {TARGET.name}")

# ── DIV balance check ──────────────────────────────────────────────────────────
def div_balance(text):
    return len(re.findall(r'<div\b', text)) - len(re.findall(r'</div>', text))

full_balance = div_balance(html)
print(f"\n  Full file div diff : {full_balance:+d}  ({'OK ✅' if full_balance == 0 else 'UNBALANCED ❌'})")

# Also check just the code-examples section
section_match = re.search(r'<section id="code-examples">.*?</section>', html, re.DOTALL)
if section_match:
    sec_balance = div_balance(section_match.group(0))
    print(f"  #code-examples div diff : {sec_balance:+d}  ({'OK ✅' if sec_balance == 0 else 'UNBALANCED ❌'})")
