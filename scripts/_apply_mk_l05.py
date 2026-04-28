"""
Replace the #mistakes body in lesson05_aggregations_count_sum_avg.html.
3 SQL mistakes — language-sql, Style B-lite split panels, no Mistake N labels.
"""

TARGET = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson05_aggregations_count_sum_avg.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Anchors ────────────────────────────────────────────────────────────────
OLD_START = '    <div class="bg-white px-8 py-7 space-y-6">\n      <div class="flex items-center gap-2 mb-6" role="tablist"><button onclick="switchMkTab(0)"'

OLD_END = '    </div>\n  </div>\n</section>\n\n\n<section id="recap">'

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row -->
      <div class="flex items-center gap-2 flex-wrap mb-6" role="tablist">

        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">SUM on Text</span>
        </button>

        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Counting NULLs</span>
        </button>

        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">No Column Alias</span>
        </button>

      </div>

      <!-- ── Mistake 1 — SUM on Text ── -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Using SUM or AVG on a Text Column</h4>
              <p class="text-xs text-gray-500 mt-0.5"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SUM</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">AVG</code> only work on numeric columns — pointing either at a text column raises a database error.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SUM(product_name)</code> asks the database to add up words — it cannot do that and returns an error. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SUM</code> only on numeric columns like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">price</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">quantity</code>, or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">amount</code>.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — text column
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- ERROR: cannot sum a text column
SELECT SUM(product_name)
FROM products;</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — numeric column
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- SUM a numeric column instead
SELECT SUM(price) AS total_value
FROM products;</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">SUM</code> like a calculator — you can only press the total button on columns that contain numbers, not labels or names.</p>
          </div>

        </div>
      </div>

      <!-- ── Mistake 2 — Counting NULLs ── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Expecting COUNT(*) and COUNT(column) to Always Match</h4>
              <p class="text-xs text-gray-500 mt-0.5"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">COUNT(*)</code> counts every row; <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">COUNT(column)</code> silently skips rows where that column is NULL.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">COUNT(email)</code> when you want the total number of customers will give a lower number than the table actually contains, because rows with a NULL email are excluded. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">COUNT(*)</code> to count every row regardless of NULL values in any column.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — NULLs excluded
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- Skips customers with no email
SELECT COUNT(email) AS total
FROM customers;</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — all rows counted
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- Counts every customer row
SELECT COUNT(*) AS all_customers
FROM customers;</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Use <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">COUNT(*)</code> to find the size of a table, and <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">COUNT(column)</code> only when you specifically want to know how many rows have a value in that column.</p>
          </div>

        </div>
      </div>

      <!-- ── Mistake 3 — No Column Alias ── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Leaving Aggregate Results Without an Alias</h4>
              <p class="text-xs text-gray-500 mt-0.5">Without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">AS</code>, the result column is labelled with the raw SQL expression, which breaks dashboard tools and Python scripts that reference column names.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">When you write <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SELECT COUNT(*) FROM orders</code>, the result column is named <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">COUNT(*)</code> — a name that contains punctuation and spaces, making it unreliable to reference in code. Adding <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">AS order_count</code> gives the column a clean, predictable name.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — no alias
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- Column heading becomes "COUNT(*)"
SELECT COUNT(*)
FROM orders;</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — named alias
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- Column heading becomes "order_count"
SELECT COUNT(*) AS order_count
FROM orders;</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Make it a habit to add <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">AS alias_name</code> after every aggregate — when you later load the results into Python or a dashboard, the tool uses the column name to find your data.</p>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>


<section id="recap">'''

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

print("✅ Common Mistakes section replaced (3 SQL mistakes)")
