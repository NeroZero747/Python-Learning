"""
Replace the #comparison section body in lesson01_creating_your_own_modules.html
following the lesson-comparison prompt rules.
"""
import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"

NEW_BODY = '''\
      <p class="text-sm text-gray-600 leading-relaxed">If you already use SQL stored procedures or Excel macros, you've been creating reusable logic for years. Python modules do exactly the same thing — they let you write a function once and call it from any script in your project.</p>

      <div class="grid grid-cols-3 gap-3">
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel
        </div>
      </div>

      <!-- Row 1 — reusable logic container -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:box-archive"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">reusable logic container</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">module (.py file)</code>
            <p class="text-xs text-gray-500 leading-relaxed">A plain Python file that holds functions any other script can import and use.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">stored procedure</code>
            <p class="text-xs text-gray-500 leading-relaxed">A saved block of SQL that you can run by name from any query without rewriting.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">macro (VBA module)</code>
            <p class="text-xs text-gray-500 leading-relaxed">A saved set of steps stored in a VBA module that any Excel workbook can run.</p>
          </div>
        </div>
      </div>

      <!-- Row 2 — single reusable unit -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:gear"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">single reusable unit</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">function</code>
            <p class="text-xs text-gray-500 leading-relaxed">A named block of code inside a module that takes inputs and returns a result.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">user-defined function</code>
            <p class="text-xs text-gray-500 leading-relaxed">A custom SQL function you write once and call inside any <code class="font-mono">SELECT</code>.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">custom formula / UDF</code>
            <p class="text-xs text-gray-500 leading-relaxed">A formula you build in VBA that works just like <code class="font-mono">=SUM()</code> in any cell.</p>
          </div>
        </div>
      </div>

      <!-- Row 3 — loading the logic -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:arrow-right-to-bracket"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">loading the logic</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">import module</code>
            <p class="text-xs text-gray-500 leading-relaxed">One line at the top of a script loads the whole module so you can call its functions.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">EXEC / CALL</code>
            <p class="text-xs text-gray-500 leading-relaxed">You run a stored procedure by name with <code class="font-mono">EXEC proc_name</code> — no copying needed.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">=MacroName() / Run</code>
            <p class="text-xs text-gray-500 leading-relaxed">You call a macro from any cell or button — Excel finds the code in the module automatically.</p>
          </div>
        </div>
      </div>

      <!-- Divider + side-by-side code blocks -->
      <div>
        <div class="flex items-center gap-3 mb-4">
          <span class="flex-1 h-px bg-gray-100"></span>
          <div class="flex items-center gap-2 shrink-0">
            <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
            </span>
            <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">Same discount calculation, three tools</p>
          </div>
          <span class="flex-1 h-px bg-gray-100"></span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 items-stretch">

          <!-- Python column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Python code</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify" data-icon="logos:python" data-width="16" data-height="16"></span>
                  <span class="text-xs font-semibold text-gray-400">Python</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-python">from shop_utils import apply_discount

sale_price = apply_discount(200, 10)
print(sale_price)</code></pre>
            </div>
          </div>

          <!-- SQL column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">SQL query</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-orange-400" data-icon="fa6-solid:database"></span>
                  <span class="text-xs font-semibold text-gray-400">SQL</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-sql">EXEC apply_discount
  @price    = 200,
  @percent  = 10;</code></pre>
            </div>
          </div>

          <!-- Excel column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Excel formula</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-green-400" data-icon="fa6-solid:table"></span>
                  <span class="text-xs font-semibold text-gray-400">Excel</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-text">=ApplyDiscount(B2, 10)
' calls a VBA function
' stored in a module</code></pre>
            </div>
          </div>

        </div>

        <p class="text-xs text-gray-400 mt-2">All three apply a 10% discount to a price of 200 — the same result, just written in a different tool.</p>
      </div>

      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">The idea of splitting logic into reusable, named units is the same across Python, SQL, and Excel. Python modules just give you a cleaner, more flexible way to organise that logic as your project grows.</p>
      </div>
'''

html = open(TARGET, encoding="utf-8").read()

# Match the body div between the section header and closing tags
pattern = re.compile(
    r'(<section id="comparison">.*?<div class="bg-white px-8 py-7 space-y-5">)'
    r'.*?'
    r'(</div>\s*</div>\s*</section>)',
    re.DOTALL
)

m = pattern.search(html)
if not m:
    print("❌  Could not find #comparison body")
    raise SystemExit(1)

old_len = len(m.group(0))
new_section = m.group(1) + '\n' + NEW_BODY + '\n    ' + m.group(2)
html_new = html[:m.start()] + new_section + html[m.end():]

open(TARGET, "w", encoding="utf-8").write(html_new)
print(f"✅  #comparison body replaced  ({old_len:,} chars → {len(new_section):,} chars)")
print(f"   File size: {len(html_new):,} chars")
