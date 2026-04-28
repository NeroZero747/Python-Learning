"""
Replace the #practice body in lesson05_aggregations_count_sum_avg.html.
5 SQL practice exercises — SQL file icon, language-sql, Result pane (not Terminal).
Domains: Students, Invoices, Scores, Members, Orders.
"""

TARGET = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson05_aggregations_count_sum_avg.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Anchors ───────────────────────────────────────────────────────────────────
# Start = opening of the body div inside #practice
OLD_START = '    <div class="bg-white px-8 py-7 space-y-6">\n      <div class="flex items-center gap-2 mb-6" role="tablist"><button onclick="switchPeTab(0)"'

# End = closing of the section, right before #mistakes
OLD_END = '    </div>\n  </div>\n</section>\n\n<section id="mistakes">'

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row — 5 exercises -->
      <div class="flex items-center gap-2 flex-wrap mb-6" role="tablist">

        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Count Students</span>
        </button>

        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Sum Invoices</span>
        </button>

        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Average Scores</span>
        </button>

        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Count Non-NULL</span>
        </button>

        <button onclick="switchPeTab(4)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Full Summary</span>
        </button>

      </div>

      <!-- ── Panel 1 — Count Students ── -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Count Students</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Students</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">COUNT(*)</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">The students table holds one row per enrolled student. Write a query that counts every row in the table. Give the result the alias <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">enrolled_count</code> so the output column has a clear name.</p>
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
                      <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">count_students.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- COUNT(*) counts every row, including rows with NULL values
SELECT COUNT(*) AS enrolled_count
FROM students;</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">enrolled_count: 342</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COUNT(*)</code> counts every row including those with NULL values in other columns — it's the most reliable way to check the total size of a table.</p>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 2 — Sum Invoices ── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Sum Invoices</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Invoices</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">SUM, AS</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">The invoices table has an <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">amount</code> column that stores the value of each invoice. Write a query that adds up all values in that column. Name the result <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">total_invoiced</code>.</p>
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
                      <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">sum_invoices.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Add up every invoice amount to get the running total
SELECT SUM(amount) AS total_invoiced
FROM invoices;</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">total_invoiced: 58420.75</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">SUM</code> silently skips NULL values, so any invoice rows with a missing amount won't affect your total.</p>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 3 — Average Scores ── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Average Scores</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Scores</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">AVG, ROUND</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">The test_results table stores a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">score</code> for each exam attempt. Write a query that finds the average score across all rows, rounded to one decimal place. Name the result <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">avg_score</code>.</p>
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
                      <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">avg_scores.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- ROUND limits the decimal places to 1 for a cleaner result
SELECT ROUND(AVG(score), 1) AS avg_score
FROM test_results;</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">avg_score: 72.4</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Always wrap <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">AVG</code> in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">ROUND</code> before displaying averages — a raw result like 72.3571428 is harder to read in a report than 72.4.</p>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 4 — Count Non-NULL ── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Count Non-NULL</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Members</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">COUNT(column)</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">NULL</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">The members table has an <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">email</code> column, but not every member has provided one — some values are NULL. Write two queries side by side: one that counts all rows with <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COUNT(*)</code>, and one that counts only rows where email is not NULL using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COUNT(email)</code>.</p>
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
                      <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">count_non_null.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- COUNT(*) includes every row, even those missing an email
SELECT COUNT(*) AS all_members FROM members;

-- COUNT(email) skips rows where email is NULL
SELECT COUNT(email) AS with_email FROM members;</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">1 row each</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">all_members: 500<br>with_email: 412</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">When the two counts differ, it means your column has NULL values — use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COUNT(column)</code> whenever you specifically want to exclude incomplete rows.</p>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 5 — Full Summary ── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Full Summary</h3>
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
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">The orders table records every purchase with a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">total</code> column for the order value. Write a single query that returns the total order count as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">order_count</code>, the sum of all totals as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">revenue</code>, and the average total rounded to two decimal places as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">avg_order</code>.</p>
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
                      <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">order_summary.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- Three aggregates in one SELECT — the database reads the table once
SELECT COUNT(*)              AS order_count,
       SUM(total)            AS revenue,
       ROUND(AVG(total), 2)  AS avg_order
FROM orders;</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">1 row returned</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">order_count: 1250 | revenue: 98400.00 | avg_order: 78.72</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Combining all three aggregates into one query is more efficient than running them separately — the database only has to scan the table once to produce all three numbers.</p>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>

<section id="mistakes">'''

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

print("✅ Practice section replaced (5 SQL exercises)")
