"""
Extend lesson10_advanced_joins.html:
  - Add 2 code-examples tabs (RIGHT JOIN, CROSS JOIN) -> panels 04, 05
  - Add 2 practice tabs (Orphaned Orders, Size x Color)  -> panels 04, 05
  - Add 2 mistakes tabs (WHERE on OUTER JOIN, Self-Join wrong column) -> mistakes 4, 5
"""
from pathlib import Path

TARGET = Path(r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson10_advanced_joins.html')

# ---------------------------------------------------------------------------
# CODE EXAMPLES
# ---------------------------------------------------------------------------

CE_NEW_TABS = '''        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">RIGHT JOIN</span>
        </button>
        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">CROSS JOIN</span>
        </button>
      </div>'''

CE_NEW_PANELS = '''      <!-- Panel 4 \u2014 RIGHT JOIN \u2014 hidden -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">RIGHT JOIN \u2014 Every Order Survives</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Orders</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Orphaned rows</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Outer join</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">A <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">RIGHT JOIN</code> is the mirror image of <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">LEFT JOIN</code> \u2014 it keeps every row from the <strong class="text-gray-800">right</strong> table, even when no customer matches. This surfaces orders linked to deleted customer records.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">right_join_orders.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT
    c.name      AS customer,    -- NULL when customer was deleted
    o.order_id                  -- always shown (right table)
FROM customers c
RIGHT JOIN orders o             -- keep every order row
ON c.id = o.customer_id;        -- join on the shared key</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ psql -f right_join_orders.sql</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Alice | 1001<br>NULL  | 1002</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Most analysts prefer to write <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">LEFT JOIN</code> and swap the table order, since it reads more naturally \u2014 but <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">RIGHT JOIN</code> can save a refactor when the right-hand table is the one you really want to preserve.</p>
            </div>

          </div>
        </div>
      </div>

      <!-- Panel 5 \u2014 CROSS JOIN \u2014 hidden -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">CROSS JOIN \u2014 All Combinations</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-amber-50 text-amber-600 border border-amber-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:fire"></span> Intermediate
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Stores &amp; Dates</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Cartesian product</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Calendar</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">A <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">CROSS JOIN</code> with no <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">ON</code> clause pairs every row from one table with every row from another. Here it builds a full grid of <strong class="text-gray-800">store \u00d7 date</strong> combinations \u2014 useful for spotting days when a store reported no sales at all.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">cross_join_calendar.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT
    s.name AS store,        -- 3 stores
    d.day  AS report_date   -- 7 days in the week
FROM stores s
CROSS JOIN days d           -- pair every store with every day
ORDER BY s.name, d.day;     -- result: 3 \u00d7 7 = 21 rows</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ psql -f cross_join_calendar.sql</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Downtown | 2026-04-20<br>Downtown | 2026-04-21<br>Uptown   | 2026-04-20</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Always check row counts before a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">CROSS JOIN</code> \u2014 a 5,000-row table joined with a 1,000-row table produces 5&nbsp;million rows.</p>
            </div>

          </div>
        </div>
      </div>

    </div>'''

# ---------------------------------------------------------------------------
# PRACTICE
# ---------------------------------------------------------------------------

PE_NEW_TABS = '''        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Orphaned Orders</span>
        </button>
        <button onclick="switchPeTab(4)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Size \u00d7 Color Grid</span>
        </button>
      </div>'''

PE_NEW_PANELS = '''      <!-- Panel 4 \u2014 Orphaned Orders \u2014 hidden -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Orphaned Orders</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Orders</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">RIGHT JOIN</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">IS NULL</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">Some <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">orders</code> rows reference a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">customer_id</code> that no longer exists in the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">customers</code> table \u2014 these are called orphaned rows. Write a RIGHT JOIN query that returns every order alongside the customer name, then filter to keep only orders with a missing customer.</p>
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
                      <span class="text-[11px] font-semibold text-gray-400">orphaned_orders.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT
    o.order_id,
    c.name AS customer        -- NULL when customer was deleted
FROM customers c
RIGHT JOIN orders o           -- keep every order row
ON c.id = o.customer_id
WHERE c.id IS NULL;           -- only orders with no customer</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ psql -f orphaned_orders.sql</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">1002 | NULL<br>1007 | NULL</div>
                </div>
              </div>

              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Orphaned rows usually mean a foreign key constraint is missing. Many teams run this query nightly to flag broken references before they corrupt downstream reports.</p>
              </div>

            </div>
          </div>
        </div>
      </div>

      <!-- Panel 5 \u2014 Size x Color Grid \u2014 hidden -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Size \u00d7 Color Grid</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-amber-50 text-amber-600 border border-amber-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:fire"></span> Intermediate
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Sizes &amp; Colors</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">CROSS JOIN</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">ORDER BY</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">A T-shirt vendor needs every possible <strong class="text-gray-800">size</strong>-and-<strong class="text-gray-800">color</strong> combination to seed an inventory table. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">sizes</code> table has 4 rows (S, M, L, XL) and the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">colors</code> table has 5 rows. Write a CROSS JOIN that returns all 20 combinations, sorted by size then color.</p>
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
                      <span class="text-[11px] font-semibold text-gray-400">size_color_grid.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT
    s.label AS size,        -- S, M, L, XL
    c.name  AS color        -- Red, Blue, Green, Black, White
FROM sizes s
CROSS JOIN colors c         -- pair every size with every color
ORDER BY s.label, c.name;   -- 4 \u00d7 5 = 20 rows</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ psql -f size_color_grid.sql</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">L  | Black<br>L  | Blue<br>L  | Green<br>...</div>
                </div>
              </div>

              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">CROSS JOIN is a fast way to seed lookup tables, build forecast scaffolds, or fill in missing time-series rows \u2014 anywhere you need every combination of two small dimensions.</p>
              </div>

            </div>
          </div>
        </div>
      </div>

    </div>'''

# ---------------------------------------------------------------------------
# MISTAKES
# ---------------------------------------------------------------------------

MK_NEW_TABS = '''        <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">WHERE Kills LEFT JOIN</span>
        </button>
        <button onclick="switchMkTab(4)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Wrong Self-Join Column</span>
        </button>
      </div>'''

MK_NEW_PANELS = '''      <!-- Mistake 4 \u2014 WHERE on right table turns LEFT JOIN into INNER JOIN \u2014 hidden -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Filtering the Right Table in WHERE Kills the LEFT JOIN</h4>
              <p class="text-xs text-gray-500 mt-0.5">A WHERE condition on the right table&apos;s columns silently turns a LEFT JOIN back into an INNER JOIN.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">When you put a condition on the <strong>right</strong> table&apos;s columns in the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">WHERE</code> clause, it filters out the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">NULL</code> rows that the LEFT JOIN just preserved \u2014 effectively turning your LEFT JOIN back into an INNER JOIN. Move the condition into the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ON</code> clause to filter <em>during</em> the join instead of after it.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &#8212; WHERE drops NULL rows
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT c.name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
WHERE o.status = &apos;shipped&apos;;
-- silently filters out NULL rows
-- behaves like an INNER JOIN</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &#8212; filter inside ON clause
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT c.name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
AND o.status = &apos;shipped&apos;;
-- filter happens during the join
-- unmatched customers still appear</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Rule of thumb: conditions on the <strong>left</strong> table belong in <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">WHERE</code>; conditions on the <strong>right</strong> table belong in <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">ON</code> when you want to keep unmatched rows.</p>
          </div>

        </div>
      </div>

      <!-- Mistake 5 \u2014 Self-join wrong column \u2014 hidden -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Joining a Self Join on the Wrong Column</h4>
              <p class="text-xs text-gray-500 mt-0.5">Joining e.id = m.id pairs every employee with themselves instead of with their manager.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">In a self join, you must connect the <strong>foreign key</strong> on one alias to the <strong>primary key</strong> on the other. Joining <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">e.id = m.id</code> just pairs every row with itself, which looks fine at a glance but is meaningless. The correct join is <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">e.manager_id = m.id</code>.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &#8212; pairs each row with itself
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT e.name AS employee,
       m.name AS manager
FROM employees e
JOIN employees m
ON e.id = m.id;
-- each row paired with itself
-- &quot;manager&quot; is always the employee</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &#8212; foreign key to primary key
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT e.name AS employee,
       m.name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.id;
-- each employee paired with their actual manager</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Before writing a self join, draw the relationship: which column on alias <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">e</code> <em>points to</em> a row on alias <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">m</code>? That column is your join key.</p>
          </div>

        </div>
      </div>

    </div>'''

# ---------------------------------------------------------------------------
# Apply edits
# ---------------------------------------------------------------------------

content = TARGET.read_text(encoding='utf-8')
original_size = len(content)

def replace_first_in_section(text, section_id, old_substring, new_substring):
    """Replace the first occurrence of old_substring within the bounds of <section id="section_id">...</section>."""
    sec_start = text.find(f'<section id="{section_id}">')
    if sec_start == -1:
        raise RuntimeError(f"Cannot find section {section_id}")
    # Find the matching </section>
    sec_end_marker = '</section>'
    sec_end = text.find(sec_end_marker, sec_start) + len(sec_end_marker)
    section_text = text[sec_start:sec_end]
    if old_substring not in section_text:
        raise RuntimeError(f"Substring not found in section {section_id}: {old_substring[:80]!r}")
    new_section = section_text.replace(old_substring, new_substring, 1)
    return text[:sec_start] + new_section + text[sec_end:]

# 1) #code-examples: insert new tabs before tab-row close, and new panels before final </div>
ce_tab_close_old = '''        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">FULL OUTER JOIN</span>
        </button>
      </div>'''
ce_tab_close_new = '''        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">FULL OUTER JOIN</span>
        </button>
''' + CE_NEW_TABS

content = replace_first_in_section(content, "code-examples", ce_tab_close_old, ce_tab_close_new)

# Insert panels at the end of #code-examples body. Find the unique closing pattern of FULL OUTER JOIN tip + close.
ce_panel_close_old = '''              <p class="text-sm text-gray-600">Filter with <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">WHERE c.name IS NULL OR o.status IS NULL</code> to isolate only the rows that had no match on either side.</p>
            </div>

          </div>
        </div>
      </div>

    </div>'''
ce_panel_close_new = '''              <p class="text-sm text-gray-600">Filter with <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">WHERE c.name IS NULL OR o.status IS NULL</code> to isolate only the rows that had no match on either side.</p>
            </div>

          </div>
        </div>
      </div>

''' + CE_NEW_PANELS

content = replace_first_in_section(content, "code-examples", ce_panel_close_old, ce_panel_close_new)

# 2) #practice
pe_tab_close_old = '''        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Full Audit</span>
        </button>
      </div>'''
pe_tab_close_new = '''        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Full Audit</span>
        </button>
''' + PE_NEW_TABS

content = replace_first_in_section(content, "practice", pe_tab_close_old, pe_tab_close_new)

pe_panel_close_old = '''                <p class="text-sm text-gray-600">Add <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">WHERE p.name IS NULL OR s.revenue IS NULL</code> to isolate only the mismatched rows &#8212; a quick way to spot data quality issues before building a report.</p>
              </div>

            </div>
          </div>
        </div>
      </div>

    </div>'''
pe_panel_close_new = '''                <p class="text-sm text-gray-600">Add <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">WHERE p.name IS NULL OR s.revenue IS NULL</code> to isolate only the mismatched rows &#8212; a quick way to spot data quality issues before building a report.</p>
              </div>

            </div>
          </div>
        </div>
      </div>

''' + PE_NEW_PANELS

content = replace_first_in_section(content, "practice", pe_panel_close_old, pe_panel_close_new)

# 3) #mistakes
mk_tab_close_old = '''        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">CROSS JOIN Explosion</span>
        </button>
      </div>'''
mk_tab_close_new = '''        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">CROSS JOIN Explosion</span>
        </button>
''' + MK_NEW_TABS

content = replace_first_in_section(content, "mistakes", mk_tab_close_old, mk_tab_close_new)

# Mistake 3 ends with this exact tip text — append new panels right after
mk_panel_close_old = '''            <p class="text-xs text-gray-600 leading-relaxed">Before running a <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">CROSS JOIN</code>, check how many rows each table has &#8212; multiply those two numbers to see how large your result set will be, and always add a filter if the answer is in the millions.</p>
          </div>

        </div>
      </div>

    </div>'''
mk_panel_close_new = '''            <p class="text-xs text-gray-600 leading-relaxed">Before running a <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">CROSS JOIN</code>, check how many rows each table has &#8212; multiply those two numbers to see how large your result set will be, and always add a filter if the answer is in the millions.</p>
          </div>

        </div>
      </div>

''' + MK_NEW_PANELS

content = replace_first_in_section(content, "mistakes", mk_panel_close_old, mk_panel_close_new)

# Write & validate
TARGET.write_text(content, encoding='utf-8')
print(f"OK  Original size: {original_size} bytes")
print(f"OK  New size:      {len(content)} bytes  (+{len(content) - original_size})")

# Validate div balance per section
sections = [
    ('code-examples',   '<section id="code-examples">', '<section id="practice">'),
    ('practice',        '<section id="practice">',      '<section id="mistakes">'),
    ('mistakes',        '<section id="mistakes">',      '<section id="recap">'),
]
for name, s1, s2 in sections:
    snippet = content[content.find(s1):content.find(s2)]
    opens = snippet.count('<div')
    closes = snippet.count('</div>')
    sym = 'OK' if opens == closes else 'FAIL'
    print(f"{sym:4s}  {name}: {opens} open / {closes} close")

# Count tabs/panels
for name, prefix in [('ce', 'code-examples'), ('pe', 'practice'), ('mk', 'mistakes')]:
    sec_start = content.find(f'<section id="{prefix}">')
    sec_end = content.find('</section>', sec_start) + 10
    sec = content[sec_start:sec_end]
    tabs = sec.count(f'switch{name.title()}Tab(')
    panels = sec.count(f'{name}-panel {name}-panel-anim')
    print(f"{prefix}: {tabs} tab buttons / {panels} panels (expect 5/5)")
