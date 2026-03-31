"""Rewrite the #mistakes section body for lesson01_creating_your_own_modules.html."""

import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
)

NEW_BODY = """\
      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Shadowing a Library</span>
        </button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Dropping the Prefix</span>
        </button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Wrong File Location</span>
        </button>
      </div>

      <!-- Panel 1 — Shadowing a Library -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Naming Your Module File the Same as a Python Library</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python loads your file instead of the real library, and calls to the library then fail.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">When you save a file as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">math.py</code>, Python finds it before the built-in <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">math</code> library — so <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">import math</code> loads your file instead. Any call to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">math.sqrt()</code> then raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">AttributeError</code>. Rename your file to something specific to your project, such as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">shop_utils.py</code>.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span>
                Wrong &mdash; shadows built-in math
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># math.py  -- conflicts with Python's built-in library
def add_items(a, b):
    return a + b

# main.py
import math               # loads math.py, not the built-in
result = math.sqrt(4)     # AttributeError: no attribute 'sqrt'</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span>
                Correct &mdash; project-specific filename
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># shop_utils.py  -- unique name, no conflict
def add_items(a, b):
    return a + b           # custom function works fine

# main.py
import shop_utils          # loads shop_utils.py as intended
import math                # now loads the real built-in library
result = math.sqrt(4)      # 2.0 -- works correctly</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Name modules after the task they perform — <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">shop_utils.py</code>, <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">grade_utils.py</code>, <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">data_cleaning.py</code>. Built-in names like <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">math</code>, <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">os</code>, and <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">random</code> are reserved by Python — reusing them as filenames silently swaps out the library.</p>
          </div>

        </div>
      </div>

      <!-- Panel 2 — Dropping the Prefix -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Calling a Function Without Its Module Name</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python raises NameError because the bare function name is not in scope after a plain import.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">import shop_utils</code> puts the module into scope — not its individual functions. Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">get_total(10, 3)</code> without the prefix raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">NameError: name 'get_total' is not defined</code>. Either add the module prefix — <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">shop_utils.get_total(10, 3)</code> — or switch to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">from shop_utils import get_total</code> to bring the function directly into scope.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span>
                Wrong &mdash; bare function name fails
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">import shop_utils

total = get_total(10, 3)   # NameError: 'get_total' not defined</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span>
                Correct &mdash; use the module prefix
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">import shop_utils

# prefix tells Python where to look
total = shop_utils.get_total(10, 3)
print(total)                          # 30</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of the module name like a workbook name in Excel. Writing <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">get_total()</code> is like a formula with no sheet reference — Python has no idea where to look. You need <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">shop_utils.get_total()</code>, or bring the function across with <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">from shop_utils import get_total</code>.</p>
          </div>

        </div>
      </div>

      <!-- Panel 3 — Wrong File Location -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Placing the Module in a Different Folder from Your Script</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python raises ModuleNotFoundError because it only searches the folder where your script lives.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Python searches the same directory as the running script when resolving <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">import</code> statements. If <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">shop_utils.py</code> is in a subfolder while <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">main.py</code> is at the top level — or the reverse — Python raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ModuleNotFoundError: No module named 'shop_utils'</code>. Keep both files in the same directory until you learn about Python packages.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span>
                Wrong &mdash; module in wrong directory
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># project/
#   main.py              -- script runs from here
#   utils/
#     shop_utils.py      -- module is one level down

import shop_utils  # ModuleNotFoundError: No module named 'shop_utils'</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span>
                Correct &mdash; both files in same folder
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># project/
#   main.py              -- script
#   shop_utils.py        -- module at the same level

import shop_utils         # found -- Python looks in the same folder
total = shop_utils.get_total(10, 3)  # works correctly</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">While you are learning, always keep your module file in the same folder as your main script. Open your file manager and confirm that <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">main.py</code> and <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">shop_utils.py</code> sit side-by-side before you run the script.</p>
          </div>

        </div>
      </div>
"""

# ── Locate the #mistakes section body and replace it ──────────────────────────
html = TARGET.read_text(encoding="utf-8")

pattern = re.compile(
    r'(<section id="mistakes">.*?<div class="bg-white px-8 py-7 space-y-6">)'
    r'(.*?)'
    r'(</div>\s*</div>\s*</section>)',
    re.DOTALL,
)

m = pattern.search(html)
if not m:
    print("❌  Pattern not found — aborting.")
else:
    before = len(m.group(2))
    new_html = html[: m.start(2)] + "\n" + NEW_BODY + "\n    " + html[m.start(3):]
    TARGET.write_text(new_html, encoding="utf-8")
    after = len(NEW_BODY)
    print(f"✅  #mistakes body replaced  ({before:,} chars → {after:,} chars)")
    print(f"   File size: {len(new_html):,} chars")
