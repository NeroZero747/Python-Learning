"""
Quality audit fixes for lesson01_what_is_sql.html — batch 2.

Changes applied:
  1. Remove traffic-light dots from all 4 Code Example code blocks.
  2. Add terminal output panes to Code Examples 1, 2, 4.
  3. Fix Code Example 3 task-box text (was "Example table:").
  4. Fix Code Example 3 amber tip (was "Query:").
  5. Add amber tips to Code Examples 1, 2, 4.
  6. Rewrite Practice Exercise task descriptions (were just tag labels).
  7. Rewrite Knowledge Check Q1-Q3 (questions were nonsensical).
  8. Fix Mistakes Panel 1: add ✗Wrong / ✓Correct split panel.
  9. Fix Mistakes Panel 1 amber tip (was just "Example:").
  10. Fix Mistakes Panel 3 amber tip (was just "Example:").
"""

from pathlib import Path
import re

TARGET = Path(__file__).parent.parent / "pages" / "mod_06a_sql_foundation" / "mod_05_sql_foundations" / "lesson01_what_is_sql.html"


def patch(html: str, old: str, new: str, label: str) -> str:
    if old in html:
        print(f"  ✅ {label}")
        return html.replace(old, new, 1)
    print(f"  ❌ NOT FOUND — {label}")
    return html


def run():
    html = TARGET.read_text(encoding="utf-8")

    # ── 1. Remove traffic-light dots from all 4 code-example blocks ──────────
    dots_block = (
        '      <div class="flex gap-1.5">\n'
        '        <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>\n'
        '        <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>\n'
        '        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>\n'
        '      </div>\n'
        '      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">'
    )
    no_dots = '      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">'

    count = html.count(dots_block)
    if count == 4:
        html = html.replace(dots_block, no_dots)
        print(f"  ✅ Traffic-light dots removed ({count} occurrences)")
    elif count > 0:
        html = html.replace(dots_block, no_dots)
        print(f"  ⚠️  Traffic-light dots removed (only {count}/4 found)")
    else:
        print("  ❌ NOT FOUND — traffic-light dots block")

    # ── 2. Example 1 — add terminal pane + amber tip ─────────────────────────
    CE1_OLD = (
        'FROM customers;</code></pre>\n'
        '  </div>\n'
        '</div>\n'
        '      \n'
        '      \n'
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        '<div class="ce-panel ce-panel-anim hidden" role="tabpanel">\n'
        '  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n'
        '    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
        '  <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>'
    )
    CE1_NEW = (
        'FROM customers;</code></pre>\n'
        '  </div>\n'
        '  <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">\n'
        '    <div class="flex items-center gap-2 mb-1.5">\n'
        '      <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>\n'
        '      <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>\n'
        '      <span class="text-[10px] text-gray-600 font-mono">$ psql -c "SELECT * FROM customers;"</span>\n'
        '    </div>\n'
        '    <div class="font-mono text-xs text-emerald-400 leading-relaxed whitespace-pre'
        '"> customer_id | name  | city\n'
        '-------------+-------+--------------\n'
        ' 101         | Maria | Los Angeles\n'
        ' 102         | James | Chicago\n'
        ' 103         | Sarah | New York\n'
        '(3 rows)</div>\n'
        '  </div>\n'
        '</div>\n'
        '      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        '        <p class="text-sm text-gray-600">The asterisk (<code class="font-mono text-[11px] bg-white px-1 py-0.5 rounded border border-gray-100">*</code>) is a wildcard that means "all columns." It\'s useful when exploring data for the first time, but on large tables with many columns, naming specific columns keeps queries faster and easier to maintain.</p>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        '<div class="ce-panel ce-panel-anim hidden" role="tabpanel">\n'
        '  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n'
        '    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
        '  <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>'
    )
    html = patch(html, CE1_OLD, CE1_NEW, "CE1 — terminal pane + amber tip")

    # ── 3. Example 2 — add terminal pane + amber tip ─────────────────────────
    CE2_OLD = (
        'FROM customers;</code></pre>\n'
        '  </div>\n'
        '</div>\n'
        '      \n'
        '      \n'
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        '<div class="ce-panel ce-panel-anim hidden" role="tabpanel">\n'
        '  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n'
        '    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
        '  <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>'
    )
    CE2_NEW = (
        'FROM customers;</code></pre>\n'
        '  </div>\n'
        '  <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">\n'
        '    <div class="flex items-center gap-2 mb-1.5">\n'
        '      <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>\n'
        '      <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>\n'
        '      <span class="text-[10px] text-gray-600 font-mono">$ psql -c "SELECT name, city FROM customers;"</span>\n'
        '    </div>\n'
        '    <div class="font-mono text-xs text-emerald-400 leading-relaxed whitespace-pre'
        '"> name  | city\n'
        '-------+--------------\n'
        ' Maria | Los Angeles\n'
        ' James | Chicago\n'
        ' Sarah | New York\n'
        '(3 rows)</div>\n'
        '  </div>\n'
        '</div>\n'
        '      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        '        <p class="text-sm text-gray-600">When you name columns explicitly, the order they appear in your SELECT list determines the column order in the results. The order of columns in the original table does not matter — only the order in your SELECT clause does.</p>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        '<div class="ce-panel ce-panel-anim hidden" role="tabpanel">\n'
        '  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n'
        '    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
        '  <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>'
    )
    html = patch(html, CE2_OLD, CE2_NEW, "CE2 — terminal pane + amber tip")

    # ── 4. Example 3 — fix task-box text and amber tip ───────────────────────
    CE3_TASK_OLD = (
        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>\n'
        '    <p class="text-sm text-gray-600">Example table:</p>'
    )
    CE3_TASK_NEW = (
        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>\n'
        '    <p class="text-sm text-gray-600">Selecting specific columns (<code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">product</code> and <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">price</code>) from the sales table returns only the fields relevant to pricing, ignoring <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">order_id</code> and any other columns you do not need.</p>'
    )
    html = patch(html, CE3_TASK_OLD, CE3_TASK_NEW, "CE3 — task-box text")

    CE3_TIP_OLD = '  <p class="text-sm text-gray-600">Query:</p>\n</div>'
    CE3_TIP_NEW = '  <p class="text-sm text-gray-600">Selecting only the columns you need is considered best practice in SQL. On tables with 50 or 100 columns, using <code class="font-mono text-[11px] bg-white px-1 py-0.5 rounded border border-gray-100">SELECT *</code> would transfer a large amount of data you do not actually need.</p>\n</div>'
    html = patch(html, CE3_TIP_OLD, CE3_TIP_NEW, "CE3 — amber tip")

    # ── 5. Example 4 — add terminal pane + amber tip ─────────────────────────
    CE4_OLD = (
        'FROM customers;</code></pre>\n'
        '  </div>\n'
        '</div>\n'
        '      \n'
        '      \n'
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        '\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )
    CE4_NEW = (
        'FROM customers;</code></pre>\n'
        '  </div>\n'
        '  <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">\n'
        '    <div class="flex items-center gap-2 mb-1.5">\n'
        '      <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>\n'
        '      <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>\n'
        '      <span class="text-[10px] text-gray-600 font-mono">$ psql -c "SELECT customer_id FROM customers;"</span>\n'
        '    </div>\n'
        '    <div class="font-mono text-xs text-emerald-400 leading-relaxed whitespace-pre'
        '"> customer_id\n'
        '-------------\n'
        ' 101\n'
        ' 102\n'
        ' 103\n'
        '(3 rows)</div>\n'
        '  </div>\n'
        '</div>\n'
        '      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        '        <p class="text-sm text-gray-600">SQL does not add a semicolon for you — you must end every statement with one yourself. A missing semicolon is one of the most common beginner syntax errors, and most database tools will simply wait for input rather than run the query.</p>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        '\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )
    html = patch(html, CE4_OLD, CE4_NEW, "CE4 — terminal pane + amber tip")

    # -- 6. Practice Exercise task descriptions + accordion solutions ---------

    # PE1 — "employees" in amber tip body identifies this block uniquely
    html = patch(
        html,
        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Tags: SELECT, SQL Queries</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">\n'
        '        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer\n'
        '        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        \n'
        '        <div class="mt-3"><div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        '  <p class="text-sm text-gray-600">Write a SQL query that retrieves all data from the table <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">employees</code>.</p>\n'
        '</div></div>\n'
        '      </div>',

        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Write a query that retrieves <strong>every row and every column</strong> from the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">employees</code> table. Use the wildcard shorthand instead of typing each column name individually.</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">\n'
        '        <span class="flex items-center gap-2"><span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span> Reveal Solution</span>\n'
        '        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">\n'
        '          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
        '            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
        '              <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>\n'
        '              <span class="text-[11px] font-semibold text-gray-400">solution_1.sql</span>\n'
        '            </div>\n'
        '            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        '          </div>\n'
        '          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT *\nFROM employees;</code></pre></div>\n'
        '        </div>\n'
        '      </div>',
        "PE1 — task + solution"
    )

    # PE2 — "name column from customers" identifies this block uniquely
    html = patch(
        html,
        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Tags: SELECT, SQL Queries</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">\n'
        '        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer\n'
        '        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        \n'
        '        <div class="mt-3"><div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        '  <p class="text-sm text-gray-600">Write a query that returns only the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">name</code> column from the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">customers</code> table.</p>\n'
        '</div></div>\n'
        '      </div>',

        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Write a query that retrieves <strong>only the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">name</code> column</strong> from the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">customers</code> table. Your result should show one column of names, not all columns.</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">\n'
        '        <span class="flex items-center gap-2"><span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span> Reveal Solution</span>\n'
        '        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">\n'
        '          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
        '            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
        '              <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>\n'
        '              <span class="text-[11px] font-semibold text-gray-400">solution_2.sql</span>\n'
        '            </div>\n'
        '            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        '          </div>\n'
        '          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT name\nFROM customers;</code></pre></div>\n'
        '        </div>\n'
        '      </div>',
        "PE2 — task + solution"
    )

    # PE3 — "product and price columns from sales" identifies this block uniquely
    html = patch(
        html,
        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Tags: SELECT, SQL Queries</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">\n'
        '        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer\n'
        '        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        \n'
        '        <div class="mt-3"><div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        '  <p class="text-sm text-gray-600">Write a query that returns the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">product</code> and <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">price</code> columns from a table called <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">sales</code>.</p>\n'
        '</div></div>\n'
        '      </div>',

        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Write a query that retrieves <strong>two columns</strong> \u2014 <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">product</code> and <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">price</code> \u2014 from the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">sales</code> table. Separate the column names with a comma in your SELECT clause.</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">\n'
        '        <span class="flex items-center gap-2"><span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span> Reveal Solution</span>\n'
        '        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">\n'
        '          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
        '            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
        '              <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>\n'
        '              <span class="text-[11px] font-semibold text-gray-400">solution_3.sql</span>\n'
        '            </div>\n'
        '            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        '          </div>\n'
        '          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT product, price\nFROM sales;</code></pre></div>\n'
        '        </div>\n'
        '      </div>',
        "PE3 — task + solution"
    )

    # PE4 — "Tags: SQL, Queries" + Customer records body identifies this block
    html = patch(
        html,
        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Tags: SQL, Queries</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">\n'
        '        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer\n'
        '        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        <div class="rounded-xl px-5 py-3 bg-gray-50 border border-gray-100"><pre class="font-mono text-sm text-gray-600 whitespace-pre-wrap">Customer records\nClaims data\nProduct catalogs</pre></div>\n'
        '        <div class="mt-3"><div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        '  <p class="text-sm text-gray-600">Consider what information might be stored in a table.</p>\n'
        '</div></div>\n'
        '      </div>',

        '    <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        '    <p class="text-sm text-gray-600">Write a query that retrieves the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">customer_id</code> and <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">city</code> columns from the <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">customers</code> table. Name the columns explicitly \u2014 do not use <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">*</code>.</p>\n'
        '  </div>\n'
        '</div>\n'
        '      <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">\n'
        '        <span class="flex items-center gap-2"><span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span> Reveal Solution</span>\n'
        '        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>\n'
        '      </button>\n'
        '      <div class="accordion-body">\n'
        '        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">\n'
        '          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
        '            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
        '              <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>\n'
        '              <span class="text-[11px] font-semibold text-gray-400">solution_4.sql</span>\n'
        '            </div>\n'
        '            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        '          </div>\n'
        '          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT customer_id, city\nFROM customers;</code></pre></div>\n'
        '        </div>\n'
        '      </div>',
        "PE4 — task + solution"
    )

    # -- 7. Knowledge Check Q1-Q3 -----------------------------------------------

    # Q1: fix question text
    html = patch(
        html,
        '        <p class="text-sm font-semibold text-gray-800 mb-4">what SQL stands for &#8212; True or False?</p>',
        '        <p class="text-sm font-semibold text-gray-800 mb-4">SQL stands for "Structured Query Language." &#8212; True or False?</p>',
        "KQ1 — fix question text"
    )

    # Q2: rewrite as multiple-choice — replace the whole question div
    html = patch(
        html,
        '        <p class="text-sm font-semibold text-gray-800 mb-4">how databases store structured data &#8212; True or False?</p>\n'
        '        <div class="flex gap-3">\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">\n'
        '            <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True\n'
        '          </button>\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">\n'
        '            <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False\n'
        '          </button>\n'
        '        </div>',

        '        <p class="text-sm font-semibold text-gray-800 mb-4">Which SQL keyword is used to retrieve data from a table?</p>\n'
        '        <div class="flex flex-wrap gap-3">\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">\n'
        '            FETCH\n'
        '          </button>\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">\n'
        '            SELECT\n'
        '          </button>\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">\n'
        '            CHOOSE\n'
        '          </button>\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">\n'
        '            GET\n'
        '          </button>\n'
        '        </div>',
        "KQ2 — rewrite as multiple-choice"
    )

    # Q3: rewrite question + flip True/False buttons
    html = patch(
        html,
        '        <p class="text-sm font-semibold text-gray-800 mb-4">what tables, rows, and columns represent &#8212; True or False?</p>\n'
        '        <div class="flex gap-3">\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">\n'
        '            <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True\n'
        '          </button>\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">\n'
        '            <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False\n'
        '          </button>\n'
        '        </div>',

        '        <p class="text-sm font-semibold text-gray-800 mb-4">A single database can only contain one table. &#8212; True or False?</p>\n'
        '        <div class="flex gap-3">\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">\n'
        '            <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True\n'
        '          </button>\n'
        '          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">\n'
        '            <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False\n'
        '          </button>\n'
        '        </div>',
        "KQ3 — rewrite as T/F about one-table myth"
    )

    # -- 8. Mistakes Panel 1 — add split panel + fix amber tip ------------------
    html = patch(
        html,
        '    <div class="px-6 py-5 space-y-3"><p class="text-sm text-gray-600 leading-relaxed">A <strong>database</strong> can contain many tables.</p>\n'
        '<p class="text-sm text-gray-600 leading-relaxed">Example:</p>\n'
        '<div class="rounded-xl px-5 py-3 bg-gray-50 border border-gray-100"><pre class="font-mono text-sm text-gray-600 whitespace-pre-wrap">Database\n'
        ' \u251c\u2500\u2500 customers\n'
        ' \u251c\u2500\u2500 orders\n'
        ' \u2514\u2500\u2500 products</pre></div></div>\n'
        '    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">\n'
        '  <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>\n'
        '  <p class="text-xs text-gray-600 leading-relaxed">Example:</p>\n'
        '</div>',

        '    <div class="px-6 py-5 space-y-4">\n'
        '      <p class="text-sm text-gray-600 leading-relaxed">When starting out with SQL, some learners try to query a database name where a table name is required. SQL treats the database and the table as two completely separate objects in a strict hierarchy \u2014 you connect to the <em>database</em> first, then you query a <em>table</em> inside it.</p>\n'
        '      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">\n'
        '        <div>\n'
        '          <p class="text-xs font-bold text-red-500 mb-1.5 flex items-center gap-1.5"><span class="iconify" data-icon="fa6-solid:xmark"></span> Wrong \u2014 treating the database as a table</p>\n'
        '          <div class="rounded-xl overflow-hidden bg-code">\n'
        '            <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- \u274c company_db is the database name,\n'
        '--    not a table you can query\n'
        'SELECT *\n'
        'FROM company_db;</code></pre>\n'
        '          </div>\n'
        '        </div>\n'
        '        <div>\n'
        '          <p class="text-xs font-bold text-emerald-600 mb-1.5 flex items-center gap-1.5"><span class="iconify" data-icon="fa6-solid:check"></span> Correct \u2014 query the table inside the database</p>\n'
        '          <div class="rounded-xl overflow-hidden bg-code">\n'
        '            <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">-- \u2705 Connect to company_db first,\n'
        '--    then SELECT from the employees table\n'
        'SELECT *\n'
        'FROM employees;</code></pre>\n'
        '          </div>\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">\n'
        '      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>\n'
        '      <p class="text-xs text-gray-600 leading-relaxed">Think of a database as the filing cabinet and tables as the individual drawers inside it. You open the cabinet first (connect to the database), then pull out a specific drawer (query a table). You cannot pull a drawer from a cabinet you have not opened.</p>\n'
        '    </div>',
        "MK1 — add split panel + fix amber tip"
    )

    # -- 9. Mistakes Panel 3 (Using Incorrect Column Names) amber tip -----------
    html = patch(
        html,
        '  <p class="text-xs text-gray-600 leading-relaxed">Example:</p>\n'
        '</div>\n'
        '  </div>\n'
        '</div>\n'
        '\n'
        '    </div>\n'
        '  </div>\n'
        '</section>\n'
        '\n'
        '\n'
        '<section id="recap">',

        '  <p class="text-xs text-gray-600 leading-relaxed">SQL column names are case-sensitive in most databases and must match the table definition exactly. If the column is called <code class="font-mono text-[10px] bg-white px-1 py-0.5 rounded border border-gray-100">customer_id</code>, you cannot write <code class="font-mono text-[10px] bg-white px-1 py-0.5 rounded border border-gray-100">customerid</code>, <code class="font-mono text-[10px] bg-white px-1 py-0.5 rounded border border-gray-100">CustomerId</code>, or <code class="font-mono text-[10px] bg-white px-1 py-0.5 rounded border border-gray-100">customer</code> \u2014 the database will return an error for each of those.</p>\n'
        '</div>\n'
        '  </div>\n'
        '</div>\n'
        '\n'
        '    </div>\n'
        '  </div>\n'
        '</section>\n'
        '\n'
        '\n'
        '<section id="recap">',
        "MK3 — fix amber tip placeholder"
    )

    TARGET.write_text(html, encoding="utf-8")
    print(f"\nDone -> {TARGET}")


if __name__ == "__main__":
    run()
