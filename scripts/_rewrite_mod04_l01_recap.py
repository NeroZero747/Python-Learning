"""Rewrite the #recap section body for lesson01_creating_your_own_modules.html."""

import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
)

NEW_BODY = """\
      <!-- 2x2 recap grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:cube"></span>
              </span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">A Python module is any <code class="font-mono bg-gray-100 px-1 rounded text-xs">.py</code> file that stores reusable functions — moving shared logic into a module means every script in your project can import it instead of repeating it.</p>
            </div>
          </div>
        </div>

        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:arrow-right-to-bracket"></span>
              </span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">The <code class="font-mono bg-gray-100 px-1 rounded text-xs">import</code> statement loads a module into your script, and you call its functions using the module name as a prefix — for example, <code class="font-mono bg-gray-100 px-1 rounded text-xs">shop_utils.get_total()</code>.</p>
            </div>
          </div>
        </div>

        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:filter"></span>
              </span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">The <code class="font-mono bg-gray-100 px-1 rounded text-xs">from module import function</code> syntax brings a single function directly into scope so you can call it without any prefix — useful when you only need one thing from a module.</p>
            </div>
          </div>
        </div>

        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:folder-tree"></span>
              </span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">Keep your module file in the same folder as your main script and give it a unique, task-based name — this prevents both <code class="font-mono bg-gray-100 px-1 rounded text-xs">ModuleNotFoundError</code> and the silent bug of shadowing a built-in library.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- Completion banner -->
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You've covered 4 key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
      </div>
"""

# ── Locate the #recap section body and replace it ─────────────────────────────
html = TARGET.read_text(encoding="utf-8")

pattern = re.compile(
    r'(<section id="recap">.*?<div class="bg-white px-8 py-7 space-y-6">)'
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
    print(f"✅  #recap body replaced  ({before:,} chars → {after:,} chars)")
    print(f"   File size: {len(new_html):,} chars")
