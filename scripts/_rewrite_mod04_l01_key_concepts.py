TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"

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
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Creating, importing, and selectively pulling functions from module files.</p>
      </div>
    </div>

    <!-- Two-column layout: sidebar left, panel right -->
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar tabs ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — active (pink) -->
          <button onclick="switchKcTab(0)"
            class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:file-code"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Creating a Module</span>
          </button>

          <!-- Tab 1 — inactive (violet) -->
          <button onclick="switchKcTab(1)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:arrow-right-to-bracket"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Importing a Module</span>
          </button>

          <!-- Tab 2 — inactive (blue) -->
          <button onclick="switchKcTab(2)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:filter"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Specific Imports</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Content panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ═══════════════════════════ -->
          <!-- Panel 0 — pink (ACTIVE)    -->
          <!-- ═══════════════════════════ -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:file-code"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Creating a Module</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">A reusable Python file</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> .py file
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>module is a plain Python file that holds functions</strong> your other scripts can borrow. Give the file a descriptive name and save it with a <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">.py</code> extension — that is all Python needs to recognise it as a module.</p>

                <!-- Widget: rules-table — module file naming rules -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-[#CB187D]">Module File Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Ends with <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">.py</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">utils.py</code>
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">sales_utils.py</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Lowercase + underscores</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">SalesUtils.py</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">sales_utils.py</code>
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">One theme per file</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">calculations.py</code> over
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">misc.py</code>
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
                      <span class="text-[11px] font-semibold text-gray-400">Python — sales_utils.py</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># sales_utils.py — a module file that holds sales functions
def calculate_total(price, quantity):  # a reusable function
    return price * quantity            # multiplies the two arguments

def apply_discount(total, rate):       # a second reusable function
    return total * (1 - rate)          # subtracts the discount percentage</code></pre>
                </div>

                <!-- Tip callout — pink -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Keep one theme per module file.</strong> A file called <code class="font-mono bg-pink-200 text-[#CB187D] border border-pink-300 px-1 rounded">sales_utils.py</code> should only hold sales-related functions — mixing unrelated logic makes the module harder to search and update later.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ═══════════════════════════════════ -->
          <!-- Panel 1 — violet (INACTIVE)        -->
          <!-- ═══════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:arrow-right-to-bracket"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Importing a Module</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Use the whole module at once</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> import
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <strong><code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">import</code> statement loads your module</strong> into the current script. You then access any function inside it by writing the module name, a dot, and the function name.</p>

                <!-- Widget: comparison-strip — import syntax -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:code"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Import Syntax</p>
                  </div>
                  <div class="flex gap-0 bg-white">
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-violet-50">
                      <code class="text-sm font-mono font-bold text-violet-700 bg-violet-100 border border-violet-200 px-2 py-0.5 rounded mb-1">import sales_utils</code>
                      <span class="text-[10px] font-semibold text-violet-600 bg-violet-100 border border-violet-200 px-2 py-0.5 rounded-full">Load the module</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-violet-300 text-base font-black">→</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-violet-50">
                      <code class="text-sm font-mono font-bold text-violet-700 bg-violet-100 border border-violet-200 px-2 py-0.5 rounded mb-1">sales_utils.calculate_total()</code>
                      <span class="text-[10px] font-semibold text-violet-600 bg-violet-100 border border-violet-200 px-2 py-0.5 rounded-full">Call the function</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-violet-300 text-base font-black">→</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3">
                      <span class="iconify text-xl text-green-500 mb-1" data-icon="fa6-solid:circle-check"></span>
                      <span class="text-[10px] font-bold text-green-700 bg-green-100 border border-green-200 px-2 py-0.5 rounded-full">Result returned</span>
                    </div>
                  </div>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python — main.py</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import sales_utils              # load the entire sales_utils module

total = sales_utils.calculate_total(10, 5)   # call a function from it
print(total)                   # prints: 50

discounted = sales_utils.apply_discount(50, 0.1)  # call a second function
print(discounted)              # prints: 45.0</code></pre>
                </div>

                <!-- Tip callout — violet -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>The module file must be in the same folder</strong> as your main script. If Python cannot find <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">sales_utils.py</code> next to your script, it will raise a <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">ModuleNotFoundError</code>.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ═══════════════════════════════════ -->
          <!-- Panel 2 — blue (INACTIVE)          -->
          <!-- ═══════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:filter"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Specific Imports</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Pick only what you need</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> from … import
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <strong><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">from … import</code> syntax pulls one function directly</strong> into your script. You can then call it by name alone — no module prefix needed.</p>

                <!-- Widget: comparison-table — import vs from…import -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">import vs from … import</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-violet-100 text-violet-700 border border-violet-200 text-[10px] font-bold">import module</span>
                        </th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">from module import fn</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Call style</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">module.func()</code></td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">func()</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Loads whole module</td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">✓</span> <span class="text-gray-400">Yes</span></td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">✗</span> <span class="text-gray-400">Just the function</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Best when</td>
                        <td class="py-2 px-3 text-gray-500">Using many functions</td>
                        <td class="py-2 px-3 text-gray-500">Using one or two</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python — main.py</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">from sales_utils import calculate_total    # import just this one function

total = calculate_total(10, 5)  # call it directly — no module prefix needed
print(total)                    # prints: 50

# You can also import multiple functions in one line
from sales_utils import calculate_total, apply_discount  # two at once</code></pre>
                </div>

                <!-- Tip callout — blue -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Use <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">from … import</code> when you only need one or two functions</strong> from a large module — it keeps your script shorter and makes it obvious which functions you are borrowing.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

        </div><!-- /panels -->
      </div><!-- /flex row -->
    </div><!-- /section body -->

  </div>
</section>'''

html = open(TARGET).read()

# Find <section id="key-concepts"> … </section>
sec_open  = '<section id="key-concepts">'
if sec_open not in html:
    # try without scroll-mt-24
    sec_open = '<section id="key-concepts"'
    sec_start = html.index(sec_open)
    # find the first > to get end of opening tag
else:
    sec_start = html.index(sec_open)

# Depth-count <section>…</section> to find closing tag
pos   = sec_start + 1
depth = 1
sec_end = None
i = sec_start
while i < len(html):
    next_open  = html.find('<section', i + 1)
    next_close = html.find('</section>', i + 1)
    if next_close == -1:
        break
    if next_open != -1 and next_open < next_close:
        depth += 1
        i = next_open
    else:
        depth -= 1
        if depth == 0:
            sec_end = next_close + len('</section>')
            break
        i = next_close

if sec_end is None:
    print('❌ Could not find closing </section> for #key-concepts')
    exit(1)

old_sec = html[sec_start:sec_end]
new_html = html[:sec_start] + NEW_SECTION + html[sec_end:]
open(TARGET, 'w').write(new_html)
print(f'✅ #key-concepts replaced  ({len(old_sec):,} chars → {len(NEW_SECTION):,} chars)')
print(f'   File size: {len(new_html):,} chars')
