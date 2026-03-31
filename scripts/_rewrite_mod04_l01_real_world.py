"""Rewrite the #real-world section body for lesson01_creating_your_own_modules.html."""

import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
)

NEW_BODY = """\
        <!-- Intro paragraph -->
        <p class="text-sm text-gray-600 leading-relaxed">Professional Python projects almost always split code across multiple files. A data team processing thousands of records each day cannot afford to duplicate calculation logic across every script. Modules give each script access to the same set of functions — write the function once, use it from any file in the project.</p>

        <!-- Three scenario cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

          <!-- Card 1 — violet -->
          <div class="relative rounded-2xl overflow-hidden border border-violet-100 bg-gradient-to-br from-violet-50 via-white to-purple-50 px-6 py-6 text-center">
            <div class="flex flex-col items-center gap-3">
              <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-lg shadow-violet-200">
                <span class="iconify text-white text-2xl" data-icon="fa6-solid:database"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-800 leading-snug">4 scripts,<br>one calculation</h3>
              <p class="text-xs text-gray-500 leading-relaxed">Your team has four scripts that all calculate a customer's total spend. You write <code class="font-mono text-violet-600">get_total()</code> once in <code class="font-mono text-violet-600">shop_utils.py</code>, and every script imports it rather than duplicating the formula.</p>
              <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-violet-100 border border-violet-200">
                <span class="iconify text-violet-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
                <span class="text-[11px] font-semibold text-violet-700">returns <code class="font-mono">order_total</code></span>
              </div>
            </div>
          </div>

          <!-- Card 2 — pink -->
          <div class="relative rounded-2xl overflow-hidden border border-pink-100 bg-gradient-to-br from-pink-50 via-white to-rose-50 px-6 py-6 text-center">
            <div class="flex flex-col items-center gap-3">
              <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-lg shadow-pink-200">
                <span class="iconify text-white text-2xl" data-icon="fa6-solid:tag"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-800 leading-snug">A 10% discount,<br>applied everywhere</h3>
              <p class="text-xs text-gray-500 leading-relaxed">The pricing rule changes from 10% to 15%. You update <code class="font-mono text-[#CB187D]">apply_discount()</code> in one file. Every script that imports it gets the new rate automatically.</p>
              <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-pink-100 border border-pink-200">
                <span class="iconify text-[#CB187D] text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
                <span class="text-[11px] font-semibold text-[#CB187D]">returns <code class="font-mono">sale_price</code></span>
              </div>
            </div>
          </div>

          <!-- Card 3 — emerald -->
          <div class="relative rounded-2xl overflow-hidden border border-emerald-100 bg-gradient-to-br from-emerald-50 via-white to-teal-50 px-6 py-6 text-center">
            <div class="flex flex-col items-center gap-3">
              <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-lg shadow-emerald-200">
                <span class="iconify text-white text-2xl" data-icon="fa6-solid:folder-tree"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-800 leading-snug">One project,<br>five focused files</h3>
              <p class="text-xs text-gray-500 leading-relaxed">Instead of a 500-line script, you split the project into <code class="font-mono text-emerald-700">data_cleaning.py</code>, <code class="font-mono text-emerald-700">calculations.py</code>, and <code class="font-mono text-emerald-700">export.py</code>. Each file handles one job, and your main script simply imports what it needs.</p>
              <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-emerald-100 border border-emerald-200">
                <span class="iconify text-emerald-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
                <span class="text-[11px] font-semibold text-emerald-700">returns <code class="font-mono">clean_data</code></span>
              </div>
            </div>
          </div>

        </div>

        <!-- Before / After comparison table -->
        <div class="rounded-xl border border-gray-100 overflow-hidden">
          <div class="grid grid-cols-2">

            <!-- Without column -->
            <div class="border-r border-gray-100">
              <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">
                <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>
                <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without modules</p>
              </div>
              <div class="px-4 py-4 space-y-3">
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                  <p class="text-xs text-gray-500 leading-relaxed">Each of the four scripts contains its own copy of the calculation — any formula change must be updated in four separate files.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                  <p class="text-xs text-gray-500 leading-relaxed">A discount rate change requires finding and editing every script individually, making inconsistencies almost certain.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                  <p class="text-xs text-gray-500 leading-relaxed">A single 500-line script handles everything — no team member can read or change one part without risking another.</p>
                </div>
              </div>
            </div>

            <!-- With column -->
            <div>
              <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">
                <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>
                <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With modules</p>
              </div>
              <div class="px-4 py-4 space-y-3">
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                  <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">get_total()</strong> lives in one file — update it once and every script that imports it automatically gets the new logic.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                  <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">apply_discount()</strong> holds the pricing rule — any change takes effect everywhere the function is called.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                  <p class="text-xs text-gray-500 leading-relaxed">Splitting into focused modules means every team member edits only the file they own, with no risk of breaking another part of the project.</p>
                </div>
              </div>
            </div>

          </div>
        </div>
"""

# ── Locate the #real-world section body and replace it ────────────────────────
html = TARGET.read_text(encoding="utf-8")

pattern = re.compile(
    r'(<section id="real-world">.*?<div class="bg-white px-8 py-7 space-y-[56]">)'
    r'(.*?)'
    r'(</div>\s*</div>\s*</section>)',
    re.DOTALL,
)

m = pattern.search(html)
if not m:
    print("❌  Pattern not found — aborting.")
else:
    before = len(m.group(2))
    new_html = html[: m.start(2)] + "\n" + NEW_BODY + "\n      " + html[m.start(3):]
    TARGET.write_text(new_html, encoding="utf-8")
    after = len(NEW_BODY)
    print(f"✅  #real-world body replaced  ({before:,} chars → {after:,} chars)")
    print(f"   File size: {len(new_html):,} chars")
