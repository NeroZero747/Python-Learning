"""
Replace the #practice section body in lesson04_filtering_data_with_where.html
4 exercises: Filter by Text | Filter by Number | Combine with AND | Expand with OR
SQL lesson — uses database icon, language-sql, .sql filenames, Result pane (not Terminal).
"""

TARGET = (
    r"c:/Users/nightwolf/Projects/Python-Learning/pages/"
    r"mod_06a_sql_foundation/mod_05_sql_foundations/lesson04_filtering_data_with_where.html"
)

# ── New body content (replaces everything inside the bg-white px-8 py-7 div) ────

NEW_BODY = """      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Filter by Text</span>
        </button>
        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Filter by Number</span>
        </button>
        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Combine with AND</span>
        </button>
        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Expand with OR</span>
        </button>
      </div>

      <!-- ── Panel 1: Filter by Text ─────────────────────────────────────── -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Filter by Text</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Customers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">WHERE</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Text Values</span>
                </div>
              </div>
            </div>
          </div>
          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You have a <code>customers</code> table with columns <code>customer_id</code>, <code>name</code>, and <code>city</code>. Write a query that returns only customers who live in Seattle. Every row in your result should have <code>city = &apos;Seattle&apos;</code>.</p>
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
                      <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">filter_by_text.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT *                -- retrieve every column from the table
FROM customers          -- the table containing customer records
WHERE city = &apos;Seattle&apos;; -- only rows where city equals Seattle</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">filter_by_text.sql</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">3 rows returned — customer_id, name, city (city = &apos;Seattle&apos; for all rows)</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Text values in a WHERE clause always need single quotes around them. Without the quotes, SQL treats the word as a column name and returns an error instead of matching a value.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ── Panel 2: Filter by Number ──────────────────────────────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Filter by Number</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Products</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">WHERE</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Numeric Values</span>
                </div>
              </div>
            </div>
          </div>
          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You have a <code>products</code> table with columns <code>product_id</code>, <code>product_name</code>, and <code>price</code>. Write a query that returns only products priced above $50. Every row in your result should have a <code>price</code> value greater than 50.</p>
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
                      <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">filter_by_number.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT *          -- retrieve every column from the table
FROM products     -- the table containing product records
WHERE price &gt; 50; -- only rows where price is greater than 50</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">filter_by_number.sql</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">4 rows returned — product_id, product_name, price (all prices above 50)</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Numeric values in a WHERE clause never use single quotes. Writing <code>WHERE price &gt; &apos;50&apos;</code> causes a data-type error in most databases — always write numbers without quotes.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ── Panel 3: Combine with AND ──────────────────────────────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Combine with AND</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Orders</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">WHERE</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">AND</span>
                </div>
              </div>
            </div>
          </div>
          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You have an <code>orders</code> table with columns <code>order_id</code>, <code>status</code>, and <code>total</code>. Write a query that returns only orders with a status of &apos;Shipped&apos; AND a total greater than 100. Both conditions must be true for a row to appear.</p>
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
                      <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">filter_with_and.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT *                   -- retrieve every column from the table
FROM orders                -- the table containing order records
WHERE status = &apos;Shipped&apos;   -- first condition: status must equal Shipped
AND total &gt; 100;           -- second condition: total must be above 100</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">filter_with_and.sql</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">2 rows returned — order_id, status, total (Shipped and total &gt; 100 for all rows)</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">AND narrows your results because both conditions must pass at the same time. Removing the AND line would return every shipped order regardless of total — AND keeps only the rows that meet all your requirements.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ── Panel 4: Expand with OR ─────────────────────────────────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Expand with OR</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Employees</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">WHERE</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">OR</span>
                </div>
              </div>
            </div>
          </div>
          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You have an <code>employees</code> table with columns <code>employee_id</code>, <code>name</code>, and <code>department</code>. Write a query that returns employees from either the &apos;Sales&apos; department OR the &apos;Marketing&apos; department. A row appears if it matches at least one of the two conditions.</p>
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
                      <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">filter_with_or.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT *                       -- retrieve every column from the table
FROM employees                 -- the table containing employee records
WHERE department = &apos;Sales&apos;     -- first condition: Sales department
OR department = &apos;Marketing&apos;;   -- second condition: Marketing department</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:table"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Result</span>
                    <span class="text-[10px] text-gray-600 font-mono">filter_with_or.sql</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">5 rows returned — Sales (3 rows), Marketing (2 rows)</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">OR widens your results because only one condition needs to be true. Adding more OR conditions always brings in more rows — it's the opposite of AND, which removes rows that don't meet every condition.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
"""

# ── Locate and replace the body div ─────────────────────────────────────────

BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
SECTION_CLOSE = '\n    </div>\n  </div>\n</section>\n\n<section id="mistakes">'

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the practice section
practice_start = content.index('<section id="practice">')
practice_body_open = content.index(BODY_OPEN, practice_start)
body_open_end = practice_body_open + len(BODY_OPEN)

# Find where the body div closes — look for the section close pattern after the body open
section_close_pos = content.index(SECTION_CLOSE, body_open_end)
body_close = section_close_pos  # everything from body_open_end to here is replaced

old_body_content = content[body_open_end:body_close]
print(f"Old body content: {len(old_body_content)} chars")
print(f"Old body preview (first 80): {repr(old_body_content[:80])}")

new_content = content[:body_open_end] + '\n' + NEW_BODY + '    ' + content[body_close:]

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ #practice body replaced successfully.")
print(f"New body content: {len(NEW_BODY)} chars")

# Verify
with open(TARGET, 'r', encoding='utf-8') as f:
    verify = f.read()
tabs = ['Filter by Text', 'Filter by Number', 'Combine with AND', 'Expand with OR']
print("\nVerification:")
for tab in tabs:
    count = verify.count(tab)
    print(f"  '{tab}': {count} occurrence(s)")
print(f"  'Exercise 1' (old): {verify.count('Exercise 1')} occurrence(s)")
print(f"  pe-panel count: {verify.count('pe-panel pe-panel-anim')}")
print(f"  hidden panels: {verify.count('pe-panel pe-panel-anim hidden')}")
