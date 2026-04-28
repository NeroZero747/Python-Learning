"""Replace #key-concepts body in lesson07 with 5-tab JOIN types layout."""

FILE = 'pages/mod_06a_sql_foundation/mod_05_sql_foundations/lesson07_joining_tables_join.html'

NEW_KC = '''<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, and CROSS JOIN.</p>
      </div>
    </div>

    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- Sidebar -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0: INNER JOIN — ACTIVE -->
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:link"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">INNER JOIN</span>
          </button>

          <!-- Tab 1: LEFT JOIN — inactive -->
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:code-compare"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">LEFT JOIN</span>
          </button>

          <!-- Tab 2: RIGHT JOIN — inactive -->
          <button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:arrow-right-to-bracket"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">RIGHT JOIN</span>
          </button>

          <!-- Tab 3: FULL OUTER JOIN — inactive -->
          <button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:circle-dot"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">FULL OUTER JOIN</span>
          </button>

          <!-- Tab 4: CROSS JOIN — inactive -->
          <button onclick="switchKcTab(4)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:xmark"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">CROSS JOIN</span>
          </button>

        </div><!-- /sidebar -->

        <!-- Panels -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ─── Panel 0: INNER JOIN (pink) — ACTIVE ─── -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:link"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">INNER JOIN</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Returns only rows that match in both tables</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> SQL Clause
                  </span>
                </div>

                <p class="text-xs text-gray-600 leading-relaxed">An <strong>INNER JOIN</strong> returns rows where the <code class="bg-pink-100 border border-pink-200 text-[#CB187D] px-1 rounded font-mono text-[11px]">ON</code> condition finds a match in both tables. Any row that has no match in the other table is left out of the result entirely.</p>

                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-[#CB187D]">INNER JOIN Behavior</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-pink-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-pink-100 text-[#CB187D] border border-pink-200 text-[10px] font-bold">INNER JOIN</span></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Rows returned</td>
                        <td class="py-2 px-3 text-gray-500">Matched rows only &mdash; both tables must have a value</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">No match?</td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">&#x2717;</span> <span class="text-gray-400">Row is excluded from the result</span></td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Produces NULLs?</td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">&#x2717;</span> <span class="text-gray-400">Never &mdash; only matched rows appear</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Use when</td>
                        <td class="py-2 px-3 text-gray-500">A match must exist in both tables</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT c.name, o.amount      -- columns from both tables
FROM orders AS o             -- first (left) table
INNER JOIN customers AS c    -- second (right) table
ON o.customer_id = c.customer_id; -- match on shared key</code></pre>
                </div>

                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600">Writing just <code class="bg-pink-200 border border-pink-300 text-[#CB187D] px-1 rounded font-mono text-[11px]">JOIN</code> without the word <code class="bg-pink-200 border border-pink-300 text-[#CB187D] px-1 rounded font-mono text-[11px]">INNER</code> works in every major database &mdash; they default to INNER JOIN.</p>
                </div>

              </div>
            </div>
          </div>

          <!-- ─── Panel 1: LEFT JOIN (violet) ─── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:code-compare"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">LEFT JOIN</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Keeps every row from the left table</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> SQL Clause
                  </span>
                </div>

                <p class="text-xs text-gray-600 leading-relaxed">A <strong>LEFT JOIN</strong> returns every row from the first (left) table. If a left-table row has no match in the right table, the right-table columns return <code class="bg-violet-100 border border-violet-200 text-violet-700 px-1 rounded font-mono text-[11px]">NULL</code> for that row.</p>

                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">LEFT JOIN vs INNER JOIN</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-violet-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-violet-100 text-violet-700 border border-violet-200 text-[10px] font-bold">LEFT JOIN</span></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-pink-100 text-[#CB187D] border border-pink-200 text-[10px] font-bold">INNER JOIN</span></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">No match?</td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">&#x2713;</span> <span class="text-gray-400">Row kept (NULLs)</span></td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">&#x2717;</span> <span class="text-gray-400">Row dropped</span></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Produces NULLs?</td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">&#x2713;</span> <span class="text-gray-400">Yes, for unmatched rows</span></td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">&#x2717;</span> <span class="text-gray-400">Never</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Use when</td>
                        <td class="py-2 px-3 text-gray-500">Gaps are expected (e.g. customers without orders)</td>
                        <td class="py-2 px-3 text-gray-500">Match must always exist</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT c.name, o.amount          -- NULL if customer has no order
FROM customers AS c              -- left table &mdash; keep ALL rows
LEFT JOIN orders AS o            -- right table &mdash; may return NULL
ON c.customer_id = o.customer_id; -- match on shared key</code></pre>
                </div>

                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Put the table you want ALL rows from on the LEFT side.</strong> Swapping the table order changes which rows are kept &mdash; <code class="bg-violet-200 border border-violet-300 text-violet-800 px-1 rounded font-mono text-[11px]">FROM orders LEFT JOIN customers</code> keeps all orders, not all customers.</p>
                </div>

              </div>
            </div>
          </div>

          <!-- ─── Panel 2: RIGHT JOIN (blue) ─── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:arrow-right-to-bracket"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">RIGHT JOIN</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Keeps every row from the right table</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> SQL Clause
                  </span>
                </div>

                <p class="text-xs text-gray-600 leading-relaxed">A <strong>RIGHT JOIN</strong> is the mirror image of a LEFT JOIN. It keeps every row from the second (right) table. If a right-table row has no match in the left table, the left-table columns return <code class="bg-blue-100 border border-blue-200 text-blue-700 px-1 rounded font-mono text-[11px]">NULL</code>.</p>

                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">RIGHT JOIN vs LEFT JOIN</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">RIGHT JOIN</span></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-violet-100 text-violet-700 border border-violet-200 text-[10px] font-bold">LEFT JOIN</span></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Keeps all rows from</td>
                        <td class="py-2 px-3 text-gray-500">Right (second) table</td>
                        <td class="py-2 px-3 text-gray-500">Left (first) table</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">No match?</td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">&#x2713;</span> <span class="text-gray-400">Right row kept (NULLs on left)</span></td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">&#x2713;</span> <span class="text-gray-400">Left row kept (NULLs on right)</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Avoid by</td>
                        <td class="py-2 px-3 text-gray-500">Swapping table order and using LEFT JOIN</td>
                        <td class="py-2 px-3 text-gray-500">No change needed</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT c.name, o.amount          -- NULL if order has no customer
FROM orders AS o                 -- left table &mdash; may return NULL
RIGHT JOIN customers AS c        -- right table &mdash; keep ALL rows
ON o.customer_id = c.customer_id; -- match on shared key</code></pre>
                </div>

                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600">Most developers <strong>avoid RIGHT JOIN</strong> by simply swapping the table order and writing a LEFT JOIN instead. The results are identical &mdash; <code class="bg-blue-200 border border-blue-300 text-blue-800 px-1 rounded font-mono text-[11px]">A RIGHT JOIN B</code> is the same as <code class="bg-blue-200 border border-blue-300 text-blue-800 px-1 rounded font-mono text-[11px]">B LEFT JOIN A</code>.</p>
                </div>

              </div>
            </div>
          </div>

          <!-- ─── Panel 3: FULL OUTER JOIN (emerald) ─── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:circle-dot"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">FULL OUTER JOIN</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Keeps every row from both tables</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> SQL Clause
                  </span>
                </div>

                <p class="text-xs text-gray-600 leading-relaxed">A <strong>FULL OUTER JOIN</strong> returns all rows from both tables. Where no match exists on either side, the unmatched columns return <code class="bg-emerald-100 border border-emerald-200 text-emerald-700 px-1 rounded font-mono text-[11px]">NULL</code>. It combines the results of a LEFT JOIN and a RIGHT JOIN.</p>

                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">What FULL OUTER JOIN Returns</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 w-1/2">Matched rows (both tables have a value)</td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">included</code> &#x2713;</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700">Left-only rows (no match in right table)</td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">included</code> &#x2713; &mdash; right columns = NULL</td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700">Right-only rows (no match in left table)</td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">included</code> &#x2713; &mdash; left columns = NULL</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT c.name, o.amount           -- NULLs on either side if no match
FROM customers AS c               -- keep ALL rows from customers
FULL OUTER JOIN orders AS o       -- keep ALL rows from orders too
ON c.customer_id = o.customer_id; -- NULL where no match exists</code></pre>
                </div>

                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>FULL OUTER JOIN is not supported in MySQL.</strong> PostgreSQL, SQL Server, Oracle, and SQLite all support it. If you use MySQL, you can simulate a FULL OUTER JOIN by combining a LEFT JOIN and a RIGHT JOIN with <code class="bg-emerald-200 border border-emerald-300 text-emerald-800 px-1 rounded font-mono text-[11px]">UNION</code>.</p>
                </div>

              </div>
            </div>
          </div>

          <!-- ─── Panel 4: CROSS JOIN (amber) ─── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="amber" role="tabpanel">
            <div class="rounded-2xl border border-amber-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-amber-500 via-orange-400 to-red-300"></div>
              <div class="bg-gradient-to-br from-amber-50/60 to-white p-5 space-y-4">

                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:xmark"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">CROSS JOIN</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Pairs every row from one table with every row from the other</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-amber-100 to-orange-100 text-amber-600 border border-amber-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> SQL Clause
                  </span>
                </div>

                <p class="text-xs text-gray-600 leading-relaxed">A <strong>CROSS JOIN</strong> returns every possible combination of rows from both tables &mdash; called a Cartesian product. It has <strong>no ON clause</strong>. If table A has 3 rows and table B has 4 rows, the result contains 3 &times; 4 = 12 rows.</p>

                <div class="rounded-xl overflow-hidden border border-amber-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-amber-50 to-orange-50 border-b border-amber-100">
                    <span class="iconify text-amber-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-amber-500">When to Use CROSS JOIN</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 w-1/2">Generate all size &times; color combinations</td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">good use</code> &#x2713;</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700">Joining related data from two tables</td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">wrong choice</code> &#x2717; &rarr; use INNER JOIN</td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700">Create a full schedule grid</td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">good use</code> &#x2713;</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT c.name, p.product_name   -- every customer + every product
FROM customers AS c             -- 3 rows
CROSS JOIN products AS p;       -- 4 rows &rarr; 12 rows in the result</code></pre>
                </div>

                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-amber-50 border border-amber-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-amber-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>CROSS JOIN on large tables produces enormous results.</strong> Two tables with 1,000 rows each returns 1,000,000 rows. Only use it when you intentionally need every possible combination.</p>
                </div>

              </div>
            </div>
          </div>

        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>'''

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

kc_start = content.find('<section id="key-concepts"')
kc_end = content.find('\n<section id="code-examples">')

if kc_start == -1 or kc_end == -1:
    print("ERROR: Could not find section boundaries")
    exit(1)

old_section = content[kc_start:kc_end]
print(f"Old section: {len(old_section)} chars, {old_section.count('kc-tab')} kc-tabs, {old_section.count('kc-panel')} kc-panels")

new_content = content[:kc_start] + NEW_KC + content[kc_end:]

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
with open(FILE, 'r', encoding='utf-8') as f:
    verify = f.read()

kc_chunk = verify[verify.find('<section id="key-concepts"'):verify.find('\n<section id="code-examples">')]

import re
tab_labels = re.findall(r'kc-tab-label[^>]+>([^<]+)', kc_chunk)
panels = kc_chunk.count('class="kc-panel kc-panel-anim')
hidden = kc_chunk.count('class="kc-panel kc-panel-anim hidden"')
lang_sql = kc_chunk.count('language-sql')
traffic = kc_chunk.count('w-2.5 h-2.5 rounded-full')

print(f"\n✅ Replaced key-concepts ({len(old_section)} chars -> {len(NEW_KC)} chars)")
print(f"   Tab labels: {tab_labels}")
print(f"   Panels: {panels} total, {hidden} hidden (should be 4 hidden)")
print(f"   language-sql blocks: {lang_sql} (should be 5)")
print(f"   Traffic-light dots: {traffic} (should be 0)")
