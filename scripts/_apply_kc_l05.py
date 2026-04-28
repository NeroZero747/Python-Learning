"""
Replace <section id="key-concepts"> in lesson05_aggregations_count_sum_avg.html
with 4-tab version: COUNT (pink), SUM (violet), AVG (blue), Column Aliases/AS (emerald).
CSS and JS already present — no additions needed.
"""

TARGET = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson05_aggregations_count_sum_avg.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Anchors ───────────────────────────────────────────────────────────────────
OLD_START = '<section id="key-concepts">'
OLD_END   = '</section>\n\n\n<section id="code-examples">'

NEW_SECTION = '''<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">COUNT, SUM, AVG, and column aliases with AS.</p>
      </div>
    </div>

    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — COUNT (active) -->
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:hashtag"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">COUNT</span>
          </button>

          <!-- Tab 1 — SUM (inactive) -->
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:plus"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">SUM</span>
          </button>

          <!-- Tab 2 — AVG (inactive) -->
          <button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:divide"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">AVG</span>
          </button>

          <!-- Tab 3 — Column Aliases (inactive) -->
          <button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:tag"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">AS (Alias)</span>
          </button>
        </div><!-- /sidebar -->

        <!-- ── Panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ── Panel 0 — COUNT (pink, active) ── -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:hashtag"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">COUNT</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Counts rows in a table or column</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> Syntax
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><code class="bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded font-mono">COUNT</code> tells you how many rows a query matches. Use <code class="bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded font-mono">COUNT(*)</code> to count every row. Use <code class="bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded font-mono">COUNT(column_name)</code> to count only rows where that column has a value.</p>

                <!-- Widget — operators-table: COUNT forms -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:calculator"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-[#CB187D]">COUNT Forms</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-pink-50">
                        <th class="py-2 px-3 text-left font-bold text-[#CB187D] w-[40%]">Syntax</th>
                        <th class="py-2 px-3 text-left font-bold text-[#CB187D]">What It Counts</th>
                        <th class="py-2 px-3 text-left font-bold text-[#CB187D]">NULLs?</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">COUNT(*)</code></td>
                        <td class="py-2 px-3 text-gray-500">Every row</td>
                        <td class="py-2 px-3 text-gray-500"><span class="text-green-500 font-bold">✓</span> Included</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">COUNT(col)</code></td>
                        <td class="py-2 px-3 text-gray-500">Rows with a value</td>
                        <td class="py-2 px-3 text-gray-500"><span class="text-red-400 font-bold">✗</span> Skipped</td>
                      </tr>
                      <tr class="bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">COUNT(DISTINCT col)</code></td>
                        <td class="py-2 px-3 text-gray-500">Unique values only</td>
                        <td class="py-2 px-3 text-gray-500"><span class="text-red-400 font-bold">✗</span> Skipped</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block — Style B, SQL -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Count every row (including NULLs)
SELECT COUNT(*) AS total_orders
FROM orders;

-- Count only rows where email is not empty
SELECT COUNT(email) AS customers_with_email
FROM customers;</code></pre>
                </div>

                <!-- Tip callout — pink -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Use <code class="bg-pink-200 text-[#CB187D] border border-pink-300 px-1 rounded font-mono">COUNT(*)</code> for totals.</strong> Only switch to <code class="bg-pink-200 text-[#CB187D] border border-pink-300 px-1 rounded font-mono">COUNT(column)</code> when you specifically want to exclude rows where that column is empty.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ── Panel 1 — SUM (violet, hidden) ── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:plus"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">SUM</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Adds up values in a numeric column</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> Syntax
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><code class="bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded font-mono">SUM</code> adds every value in a numeric column and returns one total. You point it at the column name and SQL does all the arithmetic for you.</p>

                <!-- Widget — rules-table: SUM syntax rules -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">SUM Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Column must be numeric</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">SUM(revenue)</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Cannot sum text columns</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">SUM(name)</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">COUNT(name)</code>
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">NULL rows are skipped</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">safe</code> — total stays accurate
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block — Style B, SQL -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Total revenue across the whole table
SELECT SUM(revenue) AS total_revenue
FROM sales;

-- Total revenue for one region only
SELECT SUM(amount) AS region_total
FROM orders
WHERE region = 'North';</code></pre>
                </div>

                <!-- Tip callout — violet -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>SUM only works on numbers.</strong> If you accidentally point it at a text column — like <code class="bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded font-mono">product_name</code> — the database will return an error.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ── Panel 2 — AVG (blue, hidden) ── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:divide"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">AVG</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Calculates the average of a numeric column</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> Syntax
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><code class="bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded font-mono">AVG</code> calculates the mean of a column. It adds all non-NULL values together, then divides by the count of those values. NULL rows are excluded from both steps.</p>

                <!-- Widget — comparison-table: AVG vs manual calculation -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">AVG vs Manual Mean</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">AVG(col)</span></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-700 border border-indigo-200 text-[10px] font-bold">SUM / COUNT</span></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Handles NULLs</td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">✓</span> <span class="text-gray-400">Auto-skipped</span></td>
                        <td class="py-2 px-3"><span class="text-amber-500 font-bold">!</span> <span class="text-gray-400">Depends on form</span></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Lines of SQL</td>
                        <td class="py-2 px-3 text-gray-500">1 line</td>
                        <td class="py-2 px-3 text-gray-500">1 line (longer)</td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Use for</td>
                        <td class="py-2 px-3 text-gray-500">Everyday averages</td>
                        <td class="py-2 px-3 text-gray-500">Custom NULL logic</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block — Style B, SQL -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Average order value (NULLs excluded automatically)
SELECT AVG(order_total) AS avg_order_value
FROM orders;

-- Round to 2 decimal places for cleaner output
SELECT ROUND(AVG(order_total), 2) AS avg_order_value
FROM orders;</code></pre>
                </div>

                <!-- Tip callout — blue -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong><code class="bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded font-mono">AVG</code> and <code class="bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded font-mono">SUM / COUNT(*)</code> can give different results</strong> when some rows have NULL. <code class="bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded font-mono">AVG</code> divides by non-NULL count only; <code class="bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded font-mono">COUNT(*)</code> includes every row.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ── Panel 3 — AS / Column Aliases (emerald, hidden) ── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:tag"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">AS (Column Alias)</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Names your result column clearly</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> Syntax
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">An <strong>alias</strong> is a custom name for a result column. You write <code class="bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded font-mono">AS alias_name</code> directly after any aggregate function. Without it, SQL names the column using the raw expression — like <code class="bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded font-mono">COUNT(*)</code> — which looks messy in a report.</p>

                <!-- Widget — rules-table: alias naming rules -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">Alias Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Use underscores, not spaces</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">total revenue</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">total_revenue</code>
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Lowercase is conventional</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">avg_price</code> ✓ preferred over
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">AVG_PRICE</code>
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Descriptive, not cryptic</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">order_count</code> ✓ over
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">cnt</code>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block — Style B, SQL -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Without alias: column heading is "COUNT(*)"
SELECT COUNT(*) FROM orders;

-- With alias: column heading is "order_count"
SELECT COUNT(*) AS order_count FROM orders;

-- Multiple aliases in one query
SELECT COUNT(*) AS order_count,
       SUM(amount) AS total_revenue,
       AVG(amount) AS avg_order_value
FROM orders;</code></pre>
                </div>

                <!-- Tip callout — emerald -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Always add an alias to aggregate columns.</strong> The raw expression name — like <code class="bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded font-mono">SUM(revenue)</code> — is confusing in dashboards and will break tools that expect a clean column name.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>'''

start_idx = content.find(OLD_START)
if start_idx == -1:
    print("❌ START anchor not found")
    exit(1)

end_idx = content.find(OLD_END)
if end_idx == -1:
    # Try alternate: section ends followed by two newlines + next section
    OLD_END_ALT = '</section>\n\n<section id="code-examples">'
    end_idx = content.find(OLD_END_ALT)
    if end_idx == -1:
        print("❌ END anchor not found")
        exit(1)
    end_idx += len(OLD_END_ALT)
    NEW_SECTION += '\n\n<section id="code-examples">'
else:
    end_idx += len(OLD_END)
    NEW_SECTION += '\n\n\n<section id="code-examples">'

content = content[:start_idx] + NEW_SECTION + content[end_idx:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Key Concepts section replaced (4 tabs: COUNT / SUM / AVG / AS Alias)")
