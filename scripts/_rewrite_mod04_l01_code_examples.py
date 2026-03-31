"""
Replace the #code-examples body in lesson01_creating_your_own_modules.html
with 3 clean examples following the lesson-code-examples prompt rules.
"""

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"

NEW_BODY = '''\
      <!-- ── Tab pill row ──────────────────────────────────────── -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Create a Module</span>
        </button>

        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Import a Module</span>
        </button>

        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Pick Specific Functions</span>
        </button>

      </div>

      <!-- ── Panel 1 — Create a Module ─────────────────────────── -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Create a Module</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Shop</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">.py file</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- What This Does -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This file saves two <strong class="text-gray-800">functions</strong> in a standalone Python file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">shop_utils.py</code>. Any script in the same folder can import this file and call either function without copying the code.</p>
              </div>
            </div>

            <!-- Code block -->
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">shop_utils.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python"># shop_utils.py — a reusable module for the shop project

def get_total(price, quantity):         # multiply price by number of items
    return price * quantity             # return the total cost

def apply_discount(total, percent):     # reduce a price by a percentage
    saving = total * (percent / 100)   # calculate the discount amount
    return total - saving              # return the discounted price

print(get_total(12, 4))                # quick test: 4 items at 12 each</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python shop_utils.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">48</div>
              </div>
            </div>

            <!-- Amber tip -->
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Save this file in your project folder — any script in that same folder can import it instantly.</p>
            </div>

          </div>
        </div>
      </div>

      <!-- ── Panel 2 — Import a Module ─────────────────────────── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Import a Module</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Shop</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">import</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">dot notation</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- What This Does -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script loads every function from <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">shop_utils.py</code> using <strong class="text-gray-800"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">import</code></strong>, then calls each function using dot notation — <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">shop_utils.function()</code>.</p>
              </div>
            </div>

            <!-- Code block -->
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">main_shop.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">import shop_utils                              # load every function from shop_utils.py

shirt_cost = shop_utils.get_total(25, 3)      # call get_total using dot notation
print(shirt_cost)                             # 3 shirts at 25 each → 75

sale_price = shop_utils.apply_discount(shirt_cost, 10)  # apply a 10% discount
print(sale_price)                             # 75 with 10% off → 67.5</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python main_shop.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">75<br>67.5</div>
              </div>
            </div>

            <!-- Amber tip -->
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">shop_utils.</code> prefix tells Python exactly which file a function comes from — helpful when you import several modules.</p>
            </div>

          </div>
        </div>
      </div>

      <!-- ── Panel 3 — Pick Specific Functions ─────────────────── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Pick Specific Functions</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Shop</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">from … import</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- What This Does -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script uses <strong class="text-gray-800"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">from … import</code></strong> to pull two functions directly into the current file. You call them by name alone — no module prefix needed.</p>
              </div>
            </div>

            <!-- Code block -->
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">daily_report.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">from shop_utils import get_total          # import get_total directly — no prefix needed
from shop_utils import apply_discount     # import apply_discount the same way

jacket_cost = get_total(80, 2)           # call directly: 2 jackets at 80 each
print(jacket_cost)                        # 2 × 80 → 160

discounted = apply_discount(jacket_cost, 15)  # apply a 15% discount
print(discounted)                             # 160 with 15% off → 136.0</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python daily_report.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">160<br>136.0</div>
              </div>
            </div>

            <!-- Amber tip -->
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">You can combine both imports on one line: <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">from shop_utils import get_total, apply_discount</code>.</p>
            </div>

          </div>
        </div>
      </div>
'''

# ── Find and replace the body div ─────────────────────────────────────
import re

html = open(TARGET, encoding="utf-8").read()

# Match from the opening of the body div to just before </div></div></section>
# The body div sits between the section header </div> and the outer </div></div></section>
pattern = re.compile(
    r'(<div class="bg-white px-8 py-7 space-y-6">)'  # opening tag
    r'.*?'                                             # old content
    r'(\s+</div>\s+</div>\s+</section>\s+<section id="comparison">)',  # closing
    re.DOTALL
)

m = pattern.search(html)
if not m:
    print("❌  Could not find the code-examples body div")
    raise SystemExit(1)

old_section = m.group(0)
new_section = (
    '<div class="bg-white px-8 py-7 space-y-6">\n'
    + NEW_BODY
    + '\n    </div>\n  </div>\n</section>\n\n<section id="comparison">'
)

old_len = len(old_section)
new_len = len(new_section)

html_new = html[:m.start()] + new_section + html[m.end():]
open(TARGET, "w", encoding="utf-8").write(html_new)

print(f"✅  #code-examples body replaced  ({old_len:,} chars → {new_len:,} chars)")
print(f"   File size: {len(html_new):,} chars")
