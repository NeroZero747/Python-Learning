"""Replace the #key-concepts section in lesson04 with the full 4-tab template."""

TARGET = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html'

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

# ── Locate section boundaries ──────────────────────────────────────────────────
kc_start = content.index('<section id="key-concepts">')
decision_start = content.index('<section id="decision-flow">', kc_start)
kc_end = content.rindex('</section>', kc_start, decision_start) + len('</section>')

# ── New section HTML ──────────────────────────────────────────────────────────
NEW_SECTION = '''<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Lists, indexes, dictionaries, and key-value pairs — with examples for each.</p>
      </div>
    </div>

    <!-- Two-column layout: sidebar left, panels right -->
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar tabs ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <!-- Active indicator bar (desktop only) -->
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — List (pink, active) -->
          <button onclick="switchKcTab(0)"
            class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:list"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">List</span>
          </button>

          <!-- Tab 1 — Index (violet) -->
          <button onclick="switchKcTab(1)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:hashtag"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Index</span>
          </button>

          <!-- Tab 2 — Dictionary (blue) -->
          <button onclick="switchKcTab(2)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:book-open"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Dictionary</span>
          </button>

          <!-- Tab 3 — Key-Value Pair (emerald) -->
          <button onclick="switchKcTab(3)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:link"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Key-Value Pair</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Content panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ═══════════════════════════════════════════════════ -->
          <!-- Panel 0 — List (pink) ACTIVE                       -->
          <!-- ═══════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">

              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>

              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:list"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">List</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Ordered sequence of values</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> list
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A list is an <strong>ordered, changeable sequence of values</strong> written inside square brackets <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">[ ]</code>. Python tracks the position of every item so you can read, add, or remove values at any time.</p>

                <!-- Widget: rules-table — List Syntax Rules -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">List Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Wrap items in <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">[ ]</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">[1, 2, 3]</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Separate items with <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">,</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">[1 2 3]</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">[1, 2, 3]</code>
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Any type is allowed</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">[42, &quot;text&quot;, True]</code> ✓
                        </td>
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">sales = [120, 150, 200]      # three integers in a list
names = [&quot;Ana&quot;, &quot;Ben&quot;]       # strings also work
first = sales[0]             # index 0 = first item → 120
last  = sales[-1]            # index -1 = last item → 200
print(len(sales))            # len() counts items → 3</code></pre>
                </div>

                <!-- Tip callout -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Indexing starts at 0, not 1:</strong> the first item in any list is at <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">sales[0]</code>, so a list of 3 items has valid indexes 0, 1, and 2 — accessing <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">sales[3]</code> causes an error.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ═══════════════════════════════════════════════════ -->
          <!-- Panel 1 — Index (violet) INACTIVE                  -->
          <!-- ═══════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">

              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>

              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:hashtag"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Index</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Position number for any item</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:arrow-down-1-9"></span> int
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">An <strong>index is an integer position</strong> that identifies where an item sits inside a list. Python numbers positions from 0, so the first item is index 0, the second is index 1, and negative indexes count backwards from the end.</p>

                <!-- Widget: rules-table — Index Quick Reference -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:arrow-down-1-9"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Index Quick Reference</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 w-1/2"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">scores[0]</code></td>
                        <td class="py-2 px-3 text-gray-500">First item (leftmost)</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">scores[1]</code></td>
                        <td class="py-2 px-3 text-gray-500">Second item</td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">scores[-1]</code></td>
                        <td class="py-2 px-3 text-gray-500">Last item (any length)</td>
                      </tr>
                      <tr class="bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">scores[-2]</code></td>
                        <td class="py-2 px-3 text-gray-500">Second-to-last item</td>
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">scores = [85, 90, 78, 95]   # list with four numbers
print(scores[0])             # first item → 85
print(scores[2])             # third item → 78
print(scores[-1])            # last item → 95</code></pre>
                </div>

                <!-- Tip callout -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Accessing a position that does not exist raises an IndexError:</strong> válid indexes for a 4-item list run from <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">0</code> to <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">3</code> — use <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">-1</code> to safely grab the last item regardless of length.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ═══════════════════════════════════════════════════ -->
          <!-- Panel 2 — Dictionary (blue) INACTIVE               -->
          <!-- ═══════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">

              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>

              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:book-open"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Dictionary</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Key-value data lookup by name</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:key"></span> dict
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A dictionary is a <strong>collection of key-value pairs</strong> enclosed in curly braces <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">{ }</code>. Each entry maps a unique string key to its value, letting you retrieve data by name rather than by position.</p>

                <!-- Widget: comparison-table — list vs dict -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">List vs Dictionary</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">list</span>
                        </th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-700 border border-indigo-200 text-[10px] font-bold">dict</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Create</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">[120, 150]</code></td>
                        <td class="py-2 px-3"><code class="font-mono bg-indigo-100 text-indigo-700 border border-indigo-200 px-1 rounded">{&quot;jan&quot;: 120}</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Access</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">sales[0]</code></td>
                        <td class="py-2 px-3"><code class="font-mono bg-indigo-100 text-indigo-700 border border-indigo-200 px-1 rounded">sales[&quot;jan&quot;]</code></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Best for</td>
                        <td class="py-2 px-3 text-gray-500">Ordered items</td>
                        <td class="py-2 px-3 text-gray-500">Named fields</td>
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">employee = {
    &quot;name&quot;: &quot;Maria&quot;,          # string key → string value
    &quot;age&quot;: 34,                 # string key → integer value
    &quot;active&quot;: True,           # string key → boolean value
}
print(employee[&quot;name&quot;])       # look up by key → &quot;Maria&quot;</code></pre>
                </div>

                <!-- Tip callout -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Dictionary keys must be unique:</strong> if you write the same key twice, Python silently keeps only the second value — check for typos when a value seems to disappear from your dictionary.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ═══════════════════════════════════════════════════ -->
          <!-- Panel 3 — Key-Value Pair (emerald) INACTIVE        -->
          <!-- ═══════════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">

              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>

              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:link"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Key-Value Pair</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">The building block of every dictionary</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> key: value
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>key-value pair is a single entry</strong> inside a dictionary — a string label on the left of a colon and its associated data on the right. Keys must be unique within one dictionary, but values can hold any Python type.</p>

                <!-- Widget: comparison-strip — anatomy of a pair -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:link"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">Anatomy of a Pair</p>
                  </div>
                  <div class="flex gap-0 bg-white">
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-emerald-50">
                      <code class="text-sm font-mono font-bold text-emerald-700 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded mb-1">&quot;name&quot;</code>
                      <span class="text-[10px] font-semibold text-emerald-600 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded-full">Key</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-emerald-300 text-base font-black">:</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-emerald-50">
                      <code class="text-sm font-mono font-bold text-emerald-700 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded mb-1">&quot;Alice&quot;</code>
                      <span class="text-[10px] font-semibold text-emerald-600 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded-full">Value</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-emerald-300 text-base font-black">→</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3">
                      <span class="iconify text-xl text-green-500 mb-1" data-icon="fa6-solid:circle-check"></span>
                      <span class="text-[10px] font-bold text-green-700 bg-green-100 border border-green-200 px-2 py-0.5 rounded-full">Linked!</span>
                    </div>
                  </div>
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">person = {&quot;name&quot;: &quot;Alice&quot;}    # one key-value pair
person[&quot;city&quot;] = &quot;London&quot;     # add a new key-value pair
person[&quot;name&quot;] = &quot;Bob&quot;        # update an existing key's value
del person[&quot;city&quot;]            # remove a key-value pair entirely</code></pre>
                </div>

                <!-- Tip callout -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>You can add a new key at any time:</strong> assign to it like a variable — <code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">person[&quot;email&quot;] = &quot;a@b.com&quot;</code> creates the key if it does not already exist in the dictionary.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->

      </div><!-- /flex row -->
    </div><!-- /section body -->

  </div>
</section>'''

result = content[:kc_start] + NEW_SECTION + '\n\n' + content[kc_end:].lstrip('\n')

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(result)

print('✅ Replaced #key-concepts section')

# ── Verify ────────────────────────────────────────────────────────────────────
with open(TARGET, 'r', encoding='utf-8') as f:
    check = f.read()

kc_s = check.index('<section id="key-concepts">')
kc_e = check.index('<section id="decision-flow">', kc_s)
section = check[kc_s:kc_e]

tests = [
    ('4 sidebar tabs',              section.count('<button onclick="switchKcTab(') == 4),
    ('Tab 0 — List active',         'kc-tab kc-tab-active' in section and 'fa6-solid:list' in section),
    ('Tab 1 — Index',               'fa6-solid:hashtag' in section),
    ('Tab 2 — Dictionary',          'kc-tab group' in section and 'fa6-solid:book-open' in section),
    ('Tab 3 — Key-Value Pair',      'fa6-solid:link' in section),
    ('4 kc-panels',                 section.count('class="kc-panel kc-panel-anim') == 4),
    ('Pink panel (panel 0)',        'border-pink-100' in section and 'data-color="pink"' in section),
    ('Violet panel (panel 1)',      'data-color="violet"' in section),
    ('Blue panel (panel 2)',        'data-color="blue"' in section),
    ('Emerald panel (panel 3)',     'data-color="emerald"' in section),
    ('Panel 0 active (no hidden)', 'class="kc-panel kc-panel-anim"' in section),
    ('Panels 1-3 hidden',          section.count('class="kc-panel kc-panel-anim hidden"') == 3),
    ('List Rules widget',          'List Rules' in section),
    ('Index Quick Reference',      'Index Quick Reference' in section),
    ('List vs Dictionary table',   'List vs Dictionary' in section),
    ('Anatomy of a Pair strip',    'Anatomy of a Pair' in section),
    ('Type badge — list',          '> list' in section),
    ('Type badge — dict',          '> dict' in section),
    ('Inline styles on kc-tab-num','style="background:#CB187D' in section),
    ('decision-flow still intact', '<section id="decision-flow">' in check),
    ('code-examples still intact', '<section id="code-examples">' in check),
]

all_ok = True
for label, passed in tests:
    mark = '✅' if passed else '❌'
    if not passed:
        all_ok = False
    print(f'{mark} {label}')

print()
print('✅ All checks passed!' if all_ok else '❌ Some checks failed — review above.')
