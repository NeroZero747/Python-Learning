"""
Replace <section id="key-concepts"> in lesson04.
4 tabs: Refactoring | class keyword | self | run() method
Domain: ReportRunner class (load_data/clean_data/save_report)
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Refactoring, classes, self, and run() — the four ideas behind moving a script into a class.</p>
      </div>
    </div>

    <!-- Two-column layout: sidebar left, panels right -->
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar tabs ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <!-- Active indicator bar (desktop only) -->
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — Refactoring (pink, active) -->
          <button onclick="switchKcTab(0)"
            class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:arrows-rotate"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Refactoring</span>
          </button>

          <!-- Tab 1 — class keyword (violet, inactive) -->
          <button onclick="switchKcTab(1)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:cube"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">class keyword</span>
          </button>

          <!-- Tab 2 — self (blue, inactive) -->
          <button onclick="switchKcTab(2)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:arrow-right-to-bracket"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">self</span>
          </button>

          <!-- Tab 3 — run() method (emerald, inactive) -->
          <button onclick="switchKcTab(3)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:play"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">run() method</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Content panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ════════════════════════════════════ -->
          <!-- Panel 0 — Refactoring (pink, active) -->
          <!-- ════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:arrows-rotate"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Refactoring</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Improving code shape without changing its output</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code-branch"></span> structure
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">Refactoring means <strong>rewriting the structure of your code without changing what it does</strong>. You take the same logic that already works and reorganise it into a cleaner layout — usually by moving loose functions into a class.</p>

                <!-- Rules table -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">When to refactor</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Script has 3 or more related functions</td>
                        <td class="py-2 px-3 text-gray-500">Group them into a single class</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">You catch yourself scrolling to find functions</td>
                        <td class="py-2 px-3 text-gray-500">Methods are easier to navigate inside a class</td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Same script runs in multiple workflows</td>
                        <td class="py-2 px-3 text-gray-500">A class lets you create a fresh object each time</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">before_refactor.py</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># Before — loose functions, no grouping
def load_data():
    print("Loading data...")

def clean_data():
    print("Cleaning data...")

def save_report():
    print("Report saved!")

# You must remember to call them in the right order every time
load_data()
clean_data()
save_report()</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Nothing changes for the user:</strong> refactoring is invisible to anyone running your script — the output stays the same, only the internal organisation improves.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ════════════════════════════════════ -->
          <!-- Panel 1 — class keyword (violet)    -->
          <!-- ════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:cube"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">class keyword</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">The container that holds all your methods</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> class Name:
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">class</code> keyword creates a <strong>named container for all your related functions</strong>. Once you define a class, every function you put inside it becomes a method — and all those methods share the same name, so you always know where they live.</p>

                <!-- Rules table -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">class naming rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Start with a capital letter</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">ReportRunner</code> ✓
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">reportRunner</code> ✗
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Use PascalCase (no underscores)</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">OrderProcessor</code> ✓
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">order_processor</code> avoid
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">End the header line with a colon</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">class ReportRunner:</code> ✓
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
                      <span class="text-[11px] font-semibold text-gray-400">report_runner.py</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:                  # capital R — the class header
    def load_data(self):             # method 1 — indented inside the class
        print("Loading data...")

    def clean_data(self):            # method 2 — same indent level
        print("Cleaning data...")

    def save_report(self):           # method 3 — every function is now a method
        print("Report saved!")</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Indentation is the container:</strong> Python knows a method belongs to a class because it is indented one level inside the class body — if you forget to indent, the function stays outside the class and loses its connection.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ════════════════════════════════════ -->
          <!-- Panel 2 — self (blue, hidden)       -->
          <!-- ════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:arrow-right-to-bracket"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">self</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Each method's link to its own object</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:link"></span> self
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">When you move a function into a class, you must add <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">self</code> as the <strong>first parameter of every method</strong>. This tells Python "this method belongs to an object" — without it, Python cannot connect the method call to the right object.</p>

                <!-- Rules table -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">self rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Always first, inside the class</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">def load_data(self):</code> ✓
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">def load_data():</code> ✗
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Never pass it when calling</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">report.load_data()</code> ✓
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">report.load_data(self)</code> ✗
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Python fills it in automatically</td>
                        <td class="py-2 px-3 text-gray-500">Python passes the object as <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">self</code> for you</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">report_runner.py</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:
    def load_data(self):             # self is required — do not skip it
        print("Loading data...")

    def clean_data(self):            # same pattern for every method
        print("Cleaning data...")

report = ReportRunner()              # create the object
report.load_data()                   # Python passes report as self — automatically</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-600 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>The most common refactoring mistake</strong> is copying a function into a class but forgetting to add <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">self</code> — Python will raise a <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">TypeError</code> the first time you call the method.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ════════════════════════════════════ -->
          <!-- Panel 3 — run() method (emerald)    -->
          <!-- ════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:play"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">run() method</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">The single-line trigger that runs all the steps</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-700 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:circle-play"></span> run()
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">run()</code> method is a <strong>single method that calls all the other steps in the correct order</strong>. Instead of listing every step in your main script, you call just <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">run()</code> and the class handles the sequence for you.</p>

                <!-- Rules table -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-600">run() patterns</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Calls other methods via self</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">self.load_data()</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Steps in the right order</td>
                        <td class="py-2 px-3 text-gray-500">load → clean → save</td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Called once to trigger everything</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">report.run()</code> ✓
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
                      <span class="text-[11px] font-semibold text-gray-400">report_runner.py</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:
    def load_data(self):
        print("Loading data...")

    def clean_data(self):
        print("Cleaning data...")

    def save_report(self):
        print("Report saved!")

    def run(self):                   # chains all steps in the right order
        self.load_data()             # step 1
        self.clean_data()            # step 2
        self.save_report()           # step 3

report = ReportRunner()
report.run()                         # all three steps run with one call</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-600 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Your main script stays clean:</strong> by putting the sequence logic inside <code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">run()</code>, you reduce the main script to two lines — creating the object and calling run — making it trivial to hand off to a colleague.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->
      </div>
    </div>

  </div>
</section>'''

def replace_section(html, section_id, new_html):
    marker = f'<section id="{section_id}"'
    start = html.find(marker)
    if start == -1:
        print(f'❌ Could not find <section id="{section_id}">'); return html, False
    search = html[start:]
    depth, end, i = 0, -1, 0
    while i < len(search):
        if search[i:].startswith('<section'):
            depth += 1; i += len('<section')
        elif search[i:].startswith('</section'):
            depth -= 1
            if depth == 0:
                end = start + i + len('</section>'); break
            i += len('</section')
        else:
            i += 1
    if end == -1:
        print(f'❌ No closing </section> for #{section_id}'); return html, False
    old = html[start:end]
    print(f'  Old #{section_id}: {len(old):,} chars')
    print(f'  New #{section_id}: {len(new_html):,} chars')
    return html[:start] + new_html + html[end:], True

html = TARGET.read_text(encoding='utf-8')
html, ok = replace_section(html, 'key-concepts', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
kc_start = result.find('<section id="key-concepts"')
df_start = result.find('<section id="decision-flow"')
slice_   = result[kc_start:df_start] if kc_start != -1 and df_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon book-open",                      'data-icon="fa6-solid:book-open"'),
    ("Header title Key Concepts",           ">Key Concepts<"),
    ("4 kc-tab buttons",                    4),
    ("Tab 0 active",                        "kc-tab-active"),
    ("Tab 0: Refactoring",                  ">Refactoring<"),
    ("Tab 1: class keyword",                ">class keyword<"),
    ("Tab 2: self",                         ">self<"),
    ("Tab 3: run() method",                 ">run() method<"),
    ("4 kc-panel divs",                     4),
    ("Panel 0: before_refactor.py",         "before_refactor.py"),
    ("Panel 0: load_data function no self", "def load_data():"),
    ("Panel 1: ReportRunner class",         "class ReportRunner:"),
    ("Panel 1: PascalCase rule",            "PascalCase"),
    ("Panel 2: self rules table",           "self rules"),
    ("Panel 2: self is required",           "self is required"),
    ("Panel 3: run() definition",           "chains all steps in the right order"),
    ("Panel 3: self.load_data()",           "self.load_data()"),
    ("Panel 3: report.run()",              "report.run()"),
    ("No DataPipeline refs",                True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        ok2 = "DataPipeline" not in slice_
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        count = slice_.count(f'class="kc-tab ') + slice_.count('class="kc-tab kc-tab-active')
        if label.startswith("4 kc-tab"):
            count = slice_.count('<button onclick="switchKcTab(')
        elif label.startswith("4 kc-panel"):
            count = slice_.count('class="kc-panel')
        ok3 = count >= needle
        print(f'  {"✅" if ok3 else "❌"} {label} (found {count})')
        if ok3: passed += 1
        else: failed += 1
    elif needle in slice_:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
