"""
Replace the #code-examples body in lesson05_aggregations_count_sum_avg.html.
5 SQL examples — each in a different domain, progressively complex.
No traffic-light dots. Result pane (not Terminal) for SQL.
"""

TARGET = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson05_aggregations_count_sum_avg.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Anchors ───────────────────────────────────────────────────────────────────
OLD_START = '    <div class="bg-white px-8 py-7 space-y-6">\n      <div class="flex items-center gap-2 mb-6" role="tablist"><button onclick="switchCeTab(0)"'

OLD_END = '    </div>\n  </div>\n</section>\n\n\n<section id="practice">'

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row -->
      <div class="flex items-center gap-2 flex-wrap mb-6" role="tablist">

        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Count All Customers</span>
        </button>

        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Sum Product Revenue</span>
        </button>

        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Average Book Rating</span>
        </button>

        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Name Your Results</span>
        </button>

        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Three Aggregates Together</span>
        </button>

      </div>

      <!-- ── Panel 1 — Count All Customers ── -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Count All Customers</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Customers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">COUNT(*)</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This query counts every row in the customers table using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COUNT(*)</code>. It returns one number — the total size of the table.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">count_customers.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Count every customer row in the table
SELECT COUNT(*) AS customer_count
FROM customers;</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                  <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">customer_count: 847</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">You can use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COUNT(*)</code> on any table — it's the quickest way to check exactly how many rows a table holds.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 2 — Sum Product Revenue ── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Sum Product Revenue</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Products</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">SUM</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This query adds up every value in the price column using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">SUM</code>. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">AS total_value</code> alias gives the result a clean column name.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">sum_revenue.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Add all price values to find total stock value
SELECT SUM(price) AS total_value
FROM products;</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                  <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">total_value: 12480.50</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">SUM</code> only works on numeric columns — pointing it at a text column like <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">product_name</code> will cause an error.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 3 — Average Book Rating ── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Average Book Rating</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Books</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">AVG, ROUND</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This query calculates the mean rating across all books using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">AVG</code>. Wrapping it in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">ROUND</code> limits the result to two decimal places.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">avg_rating.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Find the average star rating, rounded to 2 places
SELECT ROUND(AVG(rating), 2) AS avg_rating
FROM books;</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                  <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">avg_rating: 4.23</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">AVG</code> ignores NULL rows automatically, so missing ratings won't pull your average down.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 4 — Name Your Results ── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Name Your Results</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Employees</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">AS Alias</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This query shows the same count twice — once without an alias and once with one. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">AS</code> keyword replaces the raw expression name with a readable column heading.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">alias_example.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Without alias: column heading is "COUNT(*)"
SELECT COUNT(*) FROM employees;

-- With alias: column heading is "headcount"
SELECT COUNT(*) AS headcount
FROM employees;</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                  <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">COUNT(*): 53<br>headcount: 53</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Always add an <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">AS</code> alias to every aggregate column — dashboard tools and Python scripts rely on clean column names to work correctly.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 5 — Three Aggregates Together ── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Three Aggregates Together</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Orders</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">COUNT + SUM + AVG</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This query runs all three aggregate functions in a single <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">SELECT</code>, returning the order count, total amount, and average amount in one row.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">order_summary.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Full summary of the orders table in one query
SELECT COUNT(*)               AS order_count,
       SUM(amount)            AS total_amount,
       ROUND(AVG(amount), 2)  AS avg_amount
FROM orders;</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                  <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">order_count: 312 | total_amount: 24650.00 | avg_amount: 79.01</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Once this summary query works, add a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">WHERE</code> clause to filter by date, region, or any other condition without rewriting the aggregates.</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>


<section id="practice">'''

start_idx = content.find(OLD_START)
if start_idx == -1:
    print("❌ START anchor not found")
    exit(1)

end_idx = content.find(OLD_END)
if end_idx == -1:
    print("❌ END anchor not found")
    exit(1)
end_idx += len(OLD_END)

content = content[:start_idx] + NEW_BODY + content[end_idx:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Code Examples section replaced (5 SQL examples)")
