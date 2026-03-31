"""
Rewrites the #key-concepts section in lesson05_operators.html with a
4-tab vertical sidebar layout: Arithmetic / Comparison / Logical / Assignment.
"""

import re

TARGET = (
    "/Users/graywolf/Documents/Project/Python-Learning/"
    "pages/track_01/mod_02_programming_foundations/lesson05_operators.html"
)

NEW_SECTION = '''\
<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Arithmetic, comparison, logical, and assignment operators — with examples for each.</p>
      </div>
    </div>

    <!-- Two-column layout: sidebar left, panel right -->
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar tabs ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <!-- Active indicator bar (desktop only) — height syncs to active tab via JS -->
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — Arithmetic (pink, active) -->
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:calculator"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Arithmetic</span>
          </button>

          <!-- Tab 1 — Comparison (violet) -->
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:scale-balanced"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Comparison</span>
          </button>

          <!-- Tab 2 — Logical (blue) -->
          <button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:diagram-project"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Logical</span>
          </button>

          <!-- Tab 3 — Assignment (emerald) -->
          <button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:floppy-disk"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Assignment</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Content panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ════════════════════════════════════════════════════════ -->
          <!-- Panel 0 — pink · Arithmetic Operators (ACTIVE)          -->
          <!-- ════════════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:calculator"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Arithmetic Operators</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Mathematical calculations on numbers</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:plus-minus"></span> math ops
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">Arithmetic operators are <strong>symbols that perform calculations on numbers</strong>, just like the keys on a calculator. Python supports addition, subtraction, multiplication, division, floor division, and the modulo remainder.</p>

                <!-- Widget: operators-table (pink) -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:calculator"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">Arithmetic Operators</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-pink-50">
                        <th class="py-2 px-3 text-left font-bold text-pink-600 w-12">Op</th>
                        <th class="py-2 px-3 text-left font-bold text-pink-600">Meaning</th>
                        <th class="py-2 px-3 text-left font-bold text-pink-600">Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">+</code></td>
                        <td class="py-2 px-3 text-gray-500">Add</td>
                        <td class="py-2 px-3"><code class="font-mono bg-pink-50 text-pink-700 border border-pink-200 px-1.5 py-0.5 rounded text-[10px]">3 + 4 → 7</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">-</code></td>
                        <td class="py-2 px-3 text-gray-500">Subtract</td>
                        <td class="py-2 px-3"><code class="font-mono bg-pink-50 text-pink-700 border border-pink-200 px-1.5 py-0.5 rounded text-[10px]">10 - 6 → 4</code></td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">*</code></td>
                        <td class="py-2 px-3 text-gray-500">Multiply</td>
                        <td class="py-2 px-3"><code class="font-mono bg-pink-50 text-pink-700 border border-pink-200 px-1.5 py-0.5 rounded text-[10px]">5 * 3 → 15</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">/</code></td>
                        <td class="py-2 px-3 text-gray-500">Divide</td>
                        <td class="py-2 px-3"><code class="font-mono bg-pink-50 text-pink-700 border border-pink-200 px-1.5 py-0.5 rounded text-[10px]">10 / 4 → 2.5</code></td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">//</code></td>
                        <td class="py-2 px-3 text-gray-500">Floor divide</td>
                        <td class="py-2 px-3"><code class="font-mono bg-pink-50 text-pink-700 border border-pink-200 px-1.5 py-0.5 rounded text-[10px]">7 // 2 → 3</code></td>
                      </tr>
                      <tr class="bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">%</code></td>
                        <td class="py-2 px-3 text-gray-500">Remainder</td>
                        <td class="py-2 px-3"><code class="font-mono bg-pink-50 text-pink-700 border border-pink-200 px-1.5 py-0.5 rounded text-[10px]">7 % 2 → 1</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">price = 49.99        # a decimal number (the unit price)
quantity = 3         # a whole number (items in the order)

total = price * quantity   # multiply to get the gross total = 149.97
discount = total * 0.1     # calculate 10% discount = 14.997
final = total - discount   # subtract discount from total = 134.973
print(round(final, 2))     # prints 134.97 (rounded to 2 decimal places)</code></pre>
                </div>

                <!-- Tip callout — pink -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Use <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">//</code> for whole-number division:</strong> <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">7 // 2</code> gives <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">3</code>, not <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">3.5</code> — it drops the decimal, which is useful when counting items that cannot be split, such as seats or tickets.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ════════════════════════════════════════════════════════ -->
          <!-- Panel 1 — violet · Comparison Operators (hidden)        -->
          <!-- ════════════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:scale-balanced"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Comparison Operators</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Test relationships between values</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:toggle-on"></span> bool result
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">Comparison operators <strong>test the relationship between two values</strong> and always return a Boolean result — either <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">True</code> or <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">False</code>. They are the building blocks of every decision in Python.</p>

                <!-- Widget: operators-table (violet) -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Comparison Operators</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-violet-50">
                        <th class="py-2 px-3 text-left font-bold text-violet-600 w-12">Op</th>
                        <th class="py-2 px-3 text-left font-bold text-violet-600">Meaning</th>
                        <th class="py-2 px-3 text-left font-bold text-violet-600">Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">==</code></td>
                        <td class="py-2 px-3 text-gray-500">Equal to</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">5 == 5 → True</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">!=</code></td>
                        <td class="py-2 px-3 text-gray-500">Not equal to</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">5 != 3 → True</code></td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">&gt;</code></td>
                        <td class="py-2 px-3 text-gray-500">Greater than</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">10 &gt; 5 → True</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">&lt;</code></td>
                        <td class="py-2 px-3 text-gray-500">Less than</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">3 &lt; 8 → True</code></td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">&gt;=</code></td>
                        <td class="py-2 px-3 text-gray-500">Greater or equal</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">5 &gt;= 5 → True</code></td>
                      </tr>
                      <tr class="bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">&lt;=</code></td>
                        <td class="py-2 px-3 text-gray-500">Less or equal</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">4 &lt;= 7 → True</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">sales = 120              # today\'s sales figure

print(sales > 100)       # True — sales exceeded the target
print(sales == 120)      # True — exact match confirmed
print(sales >= 100)      # True — met or exceeded the target
print(sales != 50)       # True — sales are definitely not 50
print(sales < 200)       # True — still under the ceiling limit</code></pre>
                </div>

                <!-- Tip callout — violet -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong><code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">==</code> compares, <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">=</code> assigns:</strong> writing <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">sales = 100</code> stores 100 in the variable, but <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">sales == 100</code> tests whether it equals 100 — confusing the two is one of the most common beginner mistakes in Python.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ════════════════════════════════════════════════════════ -->
          <!-- Panel 2 — blue · Logical Operators (hidden)             -->
          <!-- ════════════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:diagram-project"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Logical Operators</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Combine conditions with and / or / not</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:circle-half-stroke"></span> bool ops
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">Logical operators — <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">and</code>, <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">or</code>, and <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">not</code> — <strong>combine or reverse Boolean conditions</strong> so Python can evaluate two or more tests at once. They are essential for writing <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">if</code> statements that check multiple criteria.</p>

                <!-- Widget: operators-table (blue) -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:diagram-project"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">Logical Operators</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-blue-600 w-14">Op</th>
                        <th class="py-2 px-3 text-left font-bold text-blue-600">Meaning</th>
                        <th class="py-2 px-3 text-left font-bold text-blue-600">Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">and</code></td>
                        <td class="py-2 px-3 text-gray-500">Both must be True</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">True and True → True</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">or</code></td>
                        <td class="py-2 px-3 text-gray-500">Either can be True</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">False or True → True</code></td>
                      </tr>
                      <tr class="bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">not</code></td>
                        <td class="py-2 px-3 text-gray-500">Flip True ↔ False</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">not False → True</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">age = 28                              # user\'s age
has_account = True                    # whether the user is registered

is_eligible = age >= 18 and has_account   # both conditions must be True
is_guest    = not has_account             # flip: True becomes False
can_access  = age >= 18 or has_account    # either condition is enough

print(is_eligible)                        # True
print(is_guest)                           # False</code></pre>
                </div>

                <!-- Tip callout — blue -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong><code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">and</code> is stricter than <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">or</code>:</strong> <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">A and B</code> returns <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">False</code> the moment either side is <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">False</code>, while <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">A or B</code> only returns <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">False</code> when both sides are <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">False</code>.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ════════════════════════════════════════════════════════ -->
          <!-- Panel 3 — emerald · Assignment Operators (hidden)       -->
          <!-- ════════════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:floppy-disk"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Assignment Operators</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Store and update values in memory</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:equals"></span> assign ops
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">Assignment operators <strong>store a value in a variable</strong>. The basic operator <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">=</code> saves a value for the first time, while shorthand operators like <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">+=</code> and <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">-=</code> update an existing value without rewriting the full expression.</p>

                <!-- Widget: operators-table (emerald) -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:floppy-disk"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">Assignment Operators</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-emerald-50">
                        <th class="py-2 px-3 text-left font-bold text-emerald-600 w-12">Op</th>
                        <th class="py-2 px-3 text-left font-bold text-emerald-600">Meaning</th>
                        <th class="py-2 px-3 text-left font-bold text-emerald-600">Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">=</code></td>
                        <td class="py-2 px-3 text-gray-500">Assign a value</td>
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.5 rounded text-[10px]">score = 0</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">+=</code></td>
                        <td class="py-2 px-3 text-gray-500">Add and update</td>
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.5 rounded text-[10px]">score += 10 → 10</code></td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">-=</code></td>
                        <td class="py-2 px-3 text-gray-500">Subtract and update</td>
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.5 rounded text-[10px]">score -= 3 → 7</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">*=</code></td>
                        <td class="py-2 px-3 text-gray-500">Multiply and update</td>
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.5 rounded text-[10px]">score *= 2 → 14</code></td>
                      </tr>
                      <tr class="bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">/=</code></td>
                        <td class="py-2 px-3 text-gray-500">Divide and update</td>
                        <td class="py-2 px-3"><code class="font-mono bg-emerald-50 text-emerald-700 border border-emerald-200 px-1.5 py-0.5 rounded text-[10px]">score /= 2 → 7.0</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">score = 0            # basic assignment: start the score at zero

score += 10          # same as: score = score + 10  →  10
score += 5           # same as: score = score + 5   →  15
score -= 3           # same as: score = score - 3   →  12
score *= 2           # same as: score = score * 2   →  24

print(score)         # prints 24</code></pre>
                </div>

                <!-- Tip callout — emerald -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong><code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">+=</code> is the go-to shorthand for running totals:</strong> instead of writing <code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">total = total + sale_amount</code> every time, write <code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">total += sale_amount</code> — it\'s shorter, cleaner, and exactly what you will use in loops to accumulate values.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->

      </div><!-- /flex row -->
    </div><!-- /section body -->

  </div>
</section>'''


def main():
    with open(TARGET, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace from <section id="key-concepts"> up to (but not including) <section id="decision-flow">
    pattern = r'<section id="key-concepts">.*?(?=<section id="decision-flow">)'
    new_html, count = re.subn(pattern, NEW_SECTION + "\n\n", html, flags=re.DOTALL)

    if count == 0:
        print("❌ Pattern not found — section may have already been updated or ID changed.")
        return

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"✅ #key-concepts section replaced ({count} substitution).")
    print(f"   4 tabs: Arithmetic (pink) / Comparison (violet) / Logical (blue) / Assignment (emerald)")


if __name__ == "__main__":
    main()
