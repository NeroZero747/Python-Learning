"""
Replace the #key-concepts section in lesson03_attributes_methods.html
with a full 4-tab vertical sidebar layout:
  Tab 0 (pink)    — Attribute
  Tab 1 (violet)  — Method
  Tab 2 (blue)    — self
  Tab 3 (emerald) — __init__
"""

import re

TARGET = (
    "pages/track_01_python_foundation/"
    "mod_03_object_oriented_programming/"
    "lesson03_attributes_methods.html"
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
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Attributes, methods, self, and __init__ — the four building blocks of every class.</p>
      </div>
    </div>

    <!-- Two-column layout: sidebar left, panels right -->
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar tabs ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <!-- Active indicator bar (desktop only) -->
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — Attribute (pink, active) -->
          <button onclick="switchKcTab(0)"
            class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:database"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Attribute</span>
          </button>

          <!-- Tab 1 — Method (violet, inactive) -->
          <button onclick="switchKcTab(1)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:wrench"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Method</span>
          </button>

          <!-- Tab 2 — self (blue, inactive) -->
          <button onclick="switchKcTab(2)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:arrow-right-to-bracket"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">self</span>
          </button>

          <!-- Tab 3 — __init__ (emerald, inactive) -->
          <button onclick="switchKcTab(3)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:sliders"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">__init__</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Content panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ════════════════════════════════════ -->
          <!-- Panel 0 — Attribute (pink, active)  -->
          <!-- ════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:database"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Attribute</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">A named value stored inside every object</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:tag"></span> self.x
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">An attribute is a <strong>named value stored inside an object</strong>. You create one with <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">self.name = value</code> inside the class, and Python keeps a separate copy for every object you create.</p>

                <!-- Widget: rules-table (Attribute Rules) -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">Attribute Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Always prefix with <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">self.</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">self.member_id</code> ✓
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">member_id</code> ✗
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Lowercase + underscores</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">plan_type</code> ✓
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">PlanType</code> avoid
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Define in <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">__init__</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">self.age = 0</code> inside the constructor ✓
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class HealthRecord:
    def __init__(self):
        self.member_id = "M001"   # stores a text value on this object
        self.plan_type = "Gold"   # each object gets its own separate copy
        self.is_active = True     # attributes can hold any data type</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Each object keeps its own copy:</strong> changing <code class="font-mono bg-pink-200 text-[#CB187D] border border-pink-300 px-1 rounded">record1.member_id</code> never affects <code class="font-mono bg-pink-200 text-[#CB187D] border border-pink-300 px-1 rounded">record2.member_id</code> — they are completely independent.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ══════════════════════════════════════ -->
          <!-- Panel 1 — Method (violet, hidden)     -->
          <!-- ══════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:wrench"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Method</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">A function that belongs to the class</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> def method()
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A method is a <strong>function defined inside a class</strong>. It always takes <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">self</code> as its first parameter so it can read and update the object's own attributes.</p>

                <!-- Widget: rules-table (Method Rules) -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Method Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Start with the <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">def</code> keyword</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">def check(self):</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">First parameter is <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">self</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">def check(self):</code> ✓
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">def check():</code> ✗
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Indent the body 8 spaces inside the class</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">return "value"</code> inside the method ✓
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class HealthRecord:
    def __init__(self):
        self.is_active = True       # attribute to track membership status

    def check_eligibility(self):    # define a method — self is first parameter
        if self.is_active:          # read own attribute via self
            return "Eligible"       # return a result to the caller
        return "Not eligible"       # alternative if the condition is false</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Call a method on the object:</strong> write <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">record.check_eligibility()</code> — Python passes the object as <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">self</code> automatically, so you never type <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">self</code> when calling.</p>
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
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">The object's own reference to itself</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:link"></span> self
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">self</code> is <strong>the object that called the method</strong>. Python passes it automatically — you list it as the first parameter and use it to reach any attribute or method on the same object.</p>

                <!-- Widget: comparison-table (Inside the class vs Your script) -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">self vs the variable name</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">Inside the class</span>
                        </th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-700 border border-indigo-200 text-[10px] font-bold">Your script</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Access attribute</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">self.member_id</code></td>
                        <td class="py-2 px-3"><code class="font-mono bg-indigo-100 text-indigo-700 border border-indigo-200 px-1 rounded">record.member_id</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Call method</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">self.show_id()</code></td>
                        <td class="py-2 px-3"><code class="font-mono bg-indigo-100 text-indigo-700 border border-indigo-200 px-1 rounded">record.show_id()</code></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Meaning</td>
                        <td class="py-2 px-3 text-gray-500">"this object"</td>
                        <td class="py-2 px-3 text-gray-500">"the record variable"</td>
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class HealthRecord:
    def __init__(self, member_id):
        self.member_id = member_id   # self stores the value on this object

    def show_id(self):
        print(self.member_id)        # self reads the value back

record = HealthRecord("M001")        # Python sets self = record automatically
record.show_id()                     # prints: M001</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Never forget <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">self</code> in the parameter list:</strong> writing <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">def show_id():</code> instead of <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">def show_id(self):</code> causes a TypeError when you call the method — Python cannot pass the object without it.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ════════════════════════════════════ -->
          <!-- Panel 3 — __init__ (emerald, hidden) -->
          <!-- ════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:sliders"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">__init__</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Runs automatically when an object is created</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:bolt"></span> constructor
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">__init__</code> is the <strong>constructor method that runs the moment you create an object</strong>. Use it to set every attribute your object needs — think of it as filling in the columns of a new database row.</p>

                <!-- Widget: rules-table (__init__ Rules) -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">__init__ Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Name must be exactly <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">__init__</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">__init__</code> ✓
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">init</code> ✗
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">_init_</code> ✗
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">First parameter is <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">self</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">def __init__(self):</code> ✓
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Set all attributes here, not later</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">self.age = 0</code> in <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">__init__</code> ✓
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class HealthRecord:
    def __init__(self, member_id, plan_type):  # constructor — runs on creation
        self.member_id = member_id   # set attribute from the argument
        self.plan_type = plan_type   # set second attribute from argument
        self.is_active = True        # default value — no argument needed

record = HealthRecord("M001", "Gold")          # __init__ runs automatically
print(record.plan_type)                        # Gold</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Think of <code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">__init__</code> like a database INSERT:</strong> every parameter you pass becomes an attribute — similar to supplying values for each column when inserting a new record into a table.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->

      </div><!-- /flex row -->
    </div><!-- /section body -->

  </div>
</section>'''

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

# Match from <section id="key-concepts"> to the closing </section>
# then stop before <section id="decision-flow">
pattern = r'<section id="key-concepts">.*?</section>(?=\s*\n\s*<section id="decision-flow">)'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("❌ Could not find <section id=\"key-concepts\"> block — check the file.")
else:
    new_content = content[:match.start()] + NEW_SECTION + content[match.end():]
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Replaced #key-concepts section ({match.end() - match.start()} chars → {len(NEW_SECTION)} chars)")
