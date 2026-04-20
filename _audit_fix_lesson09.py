"""Audit fix script for lesson09 — adds comparison section, extra tabs, TOC link, hero pill updates."""
import re

FILE = "pages/mod_04_data_engineering/lesson09_data_warehouses_and_lakes.html"

html = open(FILE, encoding="utf-8").read()
changes = []

# ─────────────────────────────────────────────
# 1. Add comparison TOC link (after Practice Exercises, before Common Mistakes)
# ─────────────────────────────────────────────
old_toc = (
    '<a href="#practice" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">'
    '<span class="iconify text-brand shrink-0" data-icon="fa6-solid:dumbbell"></span> Practice Exercises</a>\n'
    '          <a href="#mistakes"'
)
new_toc = (
    '<a href="#practice" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">'
    '<span class="iconify text-brand shrink-0" data-icon="fa6-solid:dumbbell"></span> Practice Exercises</a>\n'
    '          <a href="#comparison" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">'
    '<span class="iconify text-brand shrink-0" data-icon="fa6-solid:scale-balanced"></span> Comparison</a>\n'
    '          <a href="#mistakes"'
)
if old_toc in html:
    html = html.replace(old_toc, new_toc)
    changes.append("✅ Added comparison TOC link")
else:
    changes.append("⚠️ Could not find TOC insertion point for comparison")

# ─────────────────────────────────────────────
# 2. Add comparison section (between Practice and Mistakes)
# ─────────────────────────────────────────────
COMPARISON_SECTION = '''
<!-- ═══ COMPARISON ═══ -->
<section id="comparison" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0"><span class="iconify text-white text-base" data-icon="fa6-solid:scale-balanced"></span></span>
      <div class="min-w-0"><h2 class="text-xl font-bold text-gray-900 leading-tight">SQL &amp; Excel Comparison</h2><p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How warehouse concepts map to tools you already know</p></div>
    </div>
    <div class="bg-white px-8 py-7 space-y-4">

      <!-- Row: Schema Enforcement -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:shield-halved"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Schema Enforcement</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Warehouse (SQL)</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">CREATE TABLE ... NOT NULL</code><p class="text-xs text-gray-500 leading-relaxed">Columns have fixed types and constraints. Bad rows are rejected at load time (schema-on-write).</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Data Lake</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">schema-on-read</code><p class="text-xs text-gray-500 leading-relaxed">Files land as-is. You apply a schema only when you query the data, so bad rows are caught late.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Data Validation</code><p class="text-xs text-gray-500 leading-relaxed">You can add cell validation rules, but nothing stops someone from pasting unvalidated data into the sheet.</p></div>
        </div>
      </div>

      <!-- Divider -->
      <div class="flex items-center gap-3"><span class="flex-1 h-px bg-gray-100"></span><span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0"><span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span></span><span class="flex-1 h-px bg-gray-100"></span></div>

      <!-- Row: Star Schema -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:star"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Star Schema / Dimensional Model</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Warehouse (SQL)</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">fact + dim tables + FK</code><p class="text-xs text-gray-500 leading-relaxed">Fact table holds numeric measures; dimension tables hold descriptive context. JOINs connect them via foreign keys.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Data Lake</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">folder partitions</code><p class="text-xs text-gray-500 leading-relaxed">Lakes use folder-based partitioning (e.g. year=2024/month=01/) instead of formal schemas. There are no foreign keys.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">VLOOKUP / Power Pivot</code><p class="text-xs text-gray-500 leading-relaxed">You reference lookup sheets with VLOOKUP or build a data model in Power Pivot &mdash; similar concept, much smaller scale.</p></div>
        </div>
      </div>

      <!-- Divider -->
      <div class="flex items-center gap-3"><span class="flex-1 h-px bg-gray-100"></span><span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0"><span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span></span><span class="flex-1 h-px bg-gray-100"></span></div>

      <!-- Row: Cloud Warehouse Scaling -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:cloud"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Scaling &amp; Performance</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Warehouse (SQL)</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">ALTER WAREHOUSE SET SIZE</code><p class="text-xs text-gray-500 leading-relaxed">Cloud warehouses scale compute independently. A single SQL command resizes processing power without touching your data.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Data Lake</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">Spark / distributed read</code><p class="text-xs text-gray-500 leading-relaxed">Lakes scale by adding parallel readers (Spark workers, DuckDB threads). Storage is already elastic by design.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">n/a &mdash; single machine</code><p class="text-xs text-gray-500 leading-relaxed">Excel runs on one computer. When the file exceeds ~1 million rows, it stops working. There is no built-in scale-out.</p></div>
        </div>
      </div>

      <!-- Divider -->
      <div class="flex items-center gap-3"><span class="flex-1 h-px bg-gray-100"></span><span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0"><span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span></span><span class="flex-1 h-px bg-gray-100"></span></div>

      <!-- Row: Cost Model -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:coins"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Cost Model</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Warehouse (SQL)</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">compute + storage</code><p class="text-xs text-gray-500 leading-relaxed">You pay for compute time (per second or per query) plus storage. Selecting fewer columns reduces scan cost on BigQuery.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Data Lake</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">~$0.02/GB/month (S3)</code><p class="text-xs text-gray-500 leading-relaxed">Object storage is extremely cheap. You only pay processing costs when you run a query engine on top of the files.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">license fee</code><p class="text-xs text-gray-500 leading-relaxed">You pay a flat Microsoft 365 subscription regardless of data size, but you hit a hard row limit at ~1 million.</p></div>
        </div>
      </div>

    </div>
  </div>
</section>
'''

anchor = '<!-- ═══ COMMON MISTAKES ═══ -->'
if anchor in html:
    html = html.replace(anchor, COMPARISON_SECTION.strip() + '\n\n' + anchor)
    changes.append("✅ Added comparison section before Common Mistakes")
else:
    changes.append("❌ Could not find COMMON MISTAKES anchor")

# ─────────────────────────────────────────────
# 3. Add Mistakes tabs 4 & 5
# ─────────────────────────────────────────────
# Add tab buttons
old_mk_tabs = '<span class="mk-step-label text-xs font-bold">SELECT *</span></button>\n      </div>'
new_mk_tabs = (
    '<span class="mk-step-label text-xs font-bold">SELECT *</span></button>\n'
    '        <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">'
    '<span class="iconify text-[13px]" data-icon="fa6-solid:link-slash"></span>'
    '<span class="mk-step-label text-xs font-bold">Missing FK</span></button>\n'
    '        <button onclick="switchMkTab(4)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">'
    '<span class="iconify text-[13px]" data-icon="fa6-solid:magnifying-glass-minus"></span>'
    '<span class="mk-step-label text-xs font-bold">Wrong Grain</span></button>\n'
    '      </div>'
)
if old_mk_tabs in html:
    html = html.replace(old_mk_tabs, new_mk_tabs)
    changes.append("✅ Added Mistakes tab buttons 4 & 5")

# Add tab panels (before closing of mistakes section body)
MK_PANELS_45 = '''
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="px-6 py-5 space-y-4">
            <h3 class="text-sm font-bold text-gray-800">Forgetting foreign key constraints on fact tables</h3>
            <p class="text-xs text-gray-600 leading-relaxed">Without foreign keys, nothing stops a fact row from referencing a customer_key that does not exist in dim_customer. Reports silently drop those rows from JOINs, and you get undercounted revenue with no error message.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div><p class="text-[10px] font-bold text-red-500 uppercase tracking-widest mb-1.5">&#10007; Wrong</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- No FK — orphan rows slip through
CREATE TABLE fact_sales (
    sale_id      BIGINT PRIMARY KEY,
    customer_key INT,  -- no REFERENCES
    amount       DECIMAL(12,2)
);</code></pre></div></div>
              <div><p class="text-[10px] font-bold text-emerald-500 uppercase tracking-widest mb-1.5">&#10003; Correct</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- FK catches invalid references
CREATE TABLE fact_sales (
    sale_id      BIGINT PRIMARY KEY,
    customer_key INT REFERENCES dim_customer(customer_key),
    amount       DECIMAL(12,2)
);</code></pre></div></div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"><span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span><p class="text-sm text-gray-600">Always add <code class="font-mono text-[11px]">REFERENCES dim_table(key)</code> to every foreign key column in your fact table. Some warehouses (like Snowflake) do not enforce FKs at runtime, but declaring them still helps the query optimizer and documents your intent.</p></div>
          </div>
        </div>
      </div>

      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="px-6 py-5 space-y-4">
            <h3 class="text-sm font-bold text-gray-800">Setting the wrong grain on a fact table</h3>
            <p class="text-xs text-gray-600 leading-relaxed">The grain defines what each row represents. If you mix daily totals and individual transactions in the same table, aggregations double-count and your numbers are silently wrong. Always document: "one row = one [event]."</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div><p class="text-[10px] font-bold text-red-500 uppercase tracking-widest mb-1.5">&#10007; Wrong</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- Mixes individual rows with daily totals
INSERT INTO fact_sales VALUES
  (1, 20240101, 101, 50.00),  -- single sale
  (2, 20240101, NULL, 3200);  -- daily total</code></pre></div></div>
              <div><p class="text-[10px] font-bold text-emerald-500 uppercase tracking-widest mb-1.5">&#10003; Correct</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- One row = one transaction (consistent grain)
INSERT INTO fact_sales VALUES
  (1, 20240101, 101, 50.00),
  (2, 20240101, 102, 75.00),
  (3, 20240101, 103, 30.00);</code></pre></div></div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"><span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span><p class="text-sm text-gray-600">Before loading data, write a one-sentence grain statement: &ldquo;One row in <code class="font-mono text-[11px]">fact_sales</code> represents one individual purchase transaction.&rdquo; If a row does not match that sentence, it belongs in a different table.</p></div>
          </div>
        </div>
      </div>
'''

# Insert before closing of mistakes section body
mk_close = '    </div>\n  </div>\n</section>\n\n<!-- ═══ RECAP ═══ -->'
mk_insert = MK_PANELS_45 + '\n    </div>\n  </div>\n</section>\n\n<!-- ═══ RECAP ═══ -->'
if mk_close in html:
    html = html.replace(mk_close, mk_insert, 1)
    changes.append("✅ Added Mistakes panels 4 & 5")
else:
    changes.append("❌ Could not find Mistakes section close anchor")

# ─────────────────────────────────────────────
# 4. Add CE tab 5 (BigQuery Analytics)
# ─────────────────────────────────────────────
old_ce_tabs = '<span class="ce-step-label text-xs font-bold">Snowflake SQL</span></button>\n      </div>'
new_ce_tabs = (
    '<span class="ce-step-label text-xs font-bold">Snowflake SQL</span></button>\n'
    '        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">'
    '<span class="iconify text-[13px]" data-icon="fa6-solid:cloud"></span>'
    '<span class="ce-step-label text-xs font-bold">BigQuery Query</span></button>\n'
    '      </div>'
)
if old_ce_tabs in html:
    html = html.replace(old_ce_tabs, new_ce_tabs)
    changes.append("✅ Added CE tab button 5")

CE_PANEL_5 = '''
      <!-- Panel 4 -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]"><div class="flex items-center gap-3"><div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5"><span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span><span class="text-[11px] font-semibold text-gray-400">bigquery_cost.sql</span></div></div><button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button></div>
          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-sql">-- BigQuery: only select the columns you need (pay per TB scanned)
SELECT
    d.year,                       -- dimension: time period
    p.category,                   -- dimension: product group
    SUM(f.amount) AS revenue,     -- measure: total sales
    COUNT(*)      AS order_count  -- measure: number of orders
FROM `project.warehouse.fact_sales` f          -- fully-qualified table
JOIN `project.warehouse.dim_date`    d ON f.date_key    = d.date_key
JOIN `project.warehouse.dim_product` p ON f.product_key = p.product_key
WHERE d.year = 2024                            -- partition pruning saves cost
GROUP BY d.year, p.category
ORDER BY revenue DESC;</code></pre></div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3"><div class="flex items-center gap-2 mb-1.5"><span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span><span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span></div><div class="font-mono text-xs text-emerald-400 leading-relaxed">+------+------------+-----------+------------+<br>| year | category   | revenue   | order_count|<br>+------+------------+-----------+------------+<br>| 2024 | Electronics| 4,120,300 |     12,890 |<br>| 2024 | Clothing   | 2,870,100 |     18,240 |<br>| 2024 | Home       | 1,540,800 |      6,310 |<br>+------+------------+-----------+------------+<br>Bytes processed: 42.8 MB (on-demand cost: $0.0002)</div></div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"><span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span><p class="text-sm text-gray-600">BigQuery charges per terabyte scanned. Naming only the columns you need (instead of <code class="font-mono text-[11px]">SELECT *</code>) and filtering on partitioned columns like <code class="font-mono text-[11px]">year</code> can cut your bill by 90% or more.</p></div>
      </div>
'''

# Insert before closing of CE section body
ce_close_anchor = '    </div>\n  </div>\n</section>\n\n<!-- ═══ PRACTICE ═══ -->'
ce_insert = CE_PANEL_5 + '\n    </div>\n  </div>\n</section>\n\n<!-- ═══ PRACTICE ═══ -->'
if ce_close_anchor in html:
    html = html.replace(ce_close_anchor, ce_insert, 1)
    changes.append("✅ Added CE panel 5 (BigQuery)")
else:
    changes.append("❌ Could not find CE section close anchor")

# ─────────────────────────────────────────────
# 5. Add Practice tabs 4 & 5
# ─────────────────────────────────────────────
old_pe_tabs = '<span class="pe-step-label text-xs font-bold">Analytics Query</span></button>\n      </div>'
new_pe_tabs = (
    '<span class="pe-step-label text-xs font-bold">Analytics Query</span></button>\n'
    '        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">'
    '<span class="iconify text-[13px]" data-icon="fa6-solid:snowflake"></span>'
    '<span class="pe-step-label text-xs font-bold">Platform Config</span></button>\n'
    '        <button onclick="switchPeTab(4)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">'
    '<span class="iconify text-[13px]" data-icon="fa6-solid:water"></span>'
    '<span class="pe-step-label text-xs font-bold">Lakehouse Query</span></button>\n'
    '      </div>'
)
if old_pe_tabs in html:
    html = html.replace(old_pe_tabs, new_pe_tabs)
    changes.append("✅ Added Practice tab buttons 4 & 5")

PE_PANELS_45 = '''
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl border border-gray-100 overflow-hidden">
          <div class="task-box px-5 py-4"><p class="text-sm font-semibold text-gray-800 mb-1">Exercise 4: Configure a Snowflake Warehouse</p><p class="text-xs text-gray-500">Write SQL to create a Snowflake virtual warehouse called <code class="font-mono text-[11px] bg-pink-50 text-[#CB187D] border border-pink-100 px-1 rounded">reporting_wh</code> with size SMALL, auto-suspend after 60 seconds, and auto-resume enabled. Then load data from a stage into <code class="font-mono text-[11px] bg-pink-50 text-[#CB187D] border border-pink-100 px-1 rounded">raw_events</code>.</p></div>
          <div class="px-5 py-4 space-y-3"><button class="accordion-toggle" onclick="toggleAccordion(this)"><span class="iconify text-[#CB187D]" data-icon="fa6-solid:lightbulb"></span> Show Solution<span class="iconify accordion-chevron" data-icon="fa6-solid:chevron-down"></span></button><div class="accordion-body"><div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3"><div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]"><div class="flex items-center gap-3"><div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5"><span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span><span class="text-[11px] font-semibold text-gray-400">exercise_4.sql</span></div></div><button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button></div><div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Create a small warehouse that pauses after 60s idle
CREATE WAREHOUSE reporting_wh
    WITH WAREHOUSE_SIZE = 'SMALL'
    AUTO_SUSPEND = 60            -- seconds of idle before pause
    AUTO_RESUME  = TRUE;         -- wake automatically on next query

-- Load CSV data from a stage
COPY INTO raw_events
    FROM @my_s3_stage/events/
    FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);</code></pre></div></div></div></div>
        </div>
      </div>

      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl border border-gray-100 overflow-hidden">
          <div class="task-box px-5 py-4"><p class="text-sm font-semibold text-gray-800 mb-1">Exercise 5: Query a Lakehouse with DuckDB</p><p class="text-xs text-gray-500">Write a Python script that uses DuckDB to query Parquet files directly from your silver layer. Return total revenue per region from <code class="font-mono text-[11px] bg-pink-50 text-[#CB187D] border border-pink-100 px-1 rounded">lake/silver/orders.parquet</code>.</p></div>
          <div class="px-5 py-4 space-y-3"><button class="accordion-toggle" onclick="toggleAccordion(this)"><span class="iconify text-[#CB187D]" data-icon="fa6-solid:lightbulb"></span> Show Solution<span class="iconify accordion-chevron" data-icon="fa6-solid:chevron-down"></span></button><div class="accordion-body"><div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3"><div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]"><div class="flex items-center gap-3"><div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5"><span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span><span class="text-[11px] font-semibold text-gray-400">exercise_5.py</span></div></div><button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button></div><div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import duckdb

# DuckDB reads Parquet directly — no loading step needed
result = duckdb.sql("""
    SELECT
        region,                          -- group by region
        SUM(amount)   AS total_revenue,  -- aggregate measure
        COUNT(*)      AS order_count     -- row count per group
    FROM 'lake/silver/orders.parquet'    -- query file in place
    GROUP BY region
    ORDER BY total_revenue DESC
""")
print(result.fetchdf())                  # returns a pandas DataFrame</code></pre></div></div></div></div>
        </div>
      </div>
'''

# Find the practice section close — it's before the comparison section now
pe_close = '    </div>\n  </div>\n</section>\n\n\n<!-- ═══ COMPARISON ═══ -->'
pe_insert = PE_PANELS_45 + '\n    </div>\n  </div>\n</section>\n\n\n<!-- ═══ COMPARISON ═══ -->'
if pe_close in html:
    html = html.replace(pe_close, pe_insert, 1)
    changes.append("✅ Added Practice panels 4 & 5")
else:
    # Try without double newline
    pe_close2 = '    </div>\n  </div>\n</section>\n\n<!-- ═══ COMPARISON ═══ -->'
    if pe_close2 in html:
        pe_insert2 = PE_PANELS_45 + '\n    </div>\n  </div>\n</section>\n\n<!-- ═══ COMPARISON ═══ -->'
        html = html.replace(pe_close2, pe_insert2, 1)
        changes.append("✅ Added Practice panels 4 & 5 (alt anchor)")
    else:
        changes.append("❌ Could not find Practice section close anchor")

# ─────────────────────────────────────────────
# 6. Add Quiz tabs 4 & 5
# ─────────────────────────────────────────────
old_qz_tabs = '<span class="qz-step-label text-xs font-bold">Question 3</span></button>\n      </div>'
new_qz_tabs = (
    '<span class="qz-step-label text-xs font-bold">Question 3</span></button>\n'
    '        <button onclick="switchQzTab(3)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">'
    '<span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>'
    '<span class="qz-step-label text-xs font-bold">Question 4</span></button>\n'
    '        <button onclick="switchQzTab(4)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">'
    '<span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>'
    '<span class="qz-step-label text-xs font-bold">Question 5</span></button>\n'
    '      </div>'
)
if old_qz_tabs in html:
    html = html.replace(old_qz_tabs, new_qz_tabs)
    changes.append("✅ Added Quiz tab buttons 4 & 5")

QZ_PANELS_45 = '''
      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden"><span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q4</span><div class="relative flex items-center gap-3"><span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:circle-question"></span></span><div><h3 class="font-bold text-gray-800">Multiple Choice</h3><p class="text-xs text-gray-500 mt-0.5">Select the best answer</p></div></div></div>
          <div class="px-6 py-5 space-y-4"><div class="quiz-question" data-qid="quiz-q3"><p class="text-sm font-semibold text-gray-800 mb-4">Your dashboard query joins fact_sales to dim_product and groups by category. Which storage design makes this query fastest?</p><div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">A. Normalized 3NF with product, category, and brand in separate tables</button>
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, true)">B. Star schema with a denormalized dim_product table</button>
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">C. Raw CSV files in a data lake bronze folder</button>
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">D. An Excel spreadsheet with all data in one tab</button>
          </div><p class="quiz-feedback mt-3 text-sm font-medium hidden"></p></div></div>
        </div>
      </div>

      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden"><span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q5</span><div class="relative flex items-center gap-3"><span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:circle-question"></span></span><div><h3 class="font-bold text-gray-800">Multiple Choice</h3><p class="text-xs text-gray-500 mt-0.5">Select the best answer</p></div></div></div>
          <div class="px-6 py-5 space-y-4"><div class="quiz-question" data-qid="quiz-q4"><p class="text-sm font-semibold text-gray-800 mb-4">Your team stores 20 TB of raw JSON logs. Analysts query them once a week. Which is the most cost-effective storage approach?</p><div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">A. Load all 20 TB into a Snowflake warehouse with an always-on XL cluster</button>
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, true)">B. Keep the files in S3 (data lake) and query with a serverless engine when needed</button>
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">C. Export the JSON to Excel and share via email</button>
            <button class="quiz-btn px-4 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">D. Store them in a normalized PostgreSQL database with strict schemas</button>
          </div><p class="quiz-feedback mt-3 text-sm font-medium hidden"></p></div></div>
        </div>
      </div>
'''

qz_close = '    </div>\n  </div>\n</section>\n\n<!-- ═══ NEXT LESSON ═══ -->'
qz_insert = QZ_PANELS_45 + '\n    </div>\n  </div>\n</section>\n\n<!-- ═══ NEXT LESSON ═══ -->'
if qz_close in html:
    html = html.replace(qz_close, qz_insert, 1)
    changes.append("✅ Added Quiz panels 4 & 5")
else:
    changes.append("❌ Could not find Quiz section close anchor")

# ─────────────────────────────────────────────
# 7. Update hero pills: Examples 4→5, Exercises 3→5
# ─────────────────────────────────────────────
html = html.replace(
    '<span class="font-extrabold">4</span><span class="font-semibold opacity-55">Examples</span>',
    '<span class="font-extrabold">5</span><span class="font-semibold opacity-55">Examples</span>'
)
html = html.replace(
    '<span class="font-extrabold">3</span><span class="font-semibold opacity-55">Exercises</span>',
    '<span class="font-extrabold">5</span><span class="font-semibold opacity-55">Exercises</span>'
)
changes.append("✅ Updated hero pills: 5 Examples, 5 Exercises")

# ─────────────────────────────────────────────
# Write
# ─────────────────────────────────────────────
open(FILE, "w", encoding="utf-8").write(html)
print(f"\n{'='*50}")
print(f"Wrote {len(html):,} chars to {FILE}")
print(f"{'='*50}")
for c in changes:
    print(c)
