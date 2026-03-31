"""Rewrite the #recap section to mirror the #objective cards exactly.

Objective cards  →  Recap cards:
  1. "What a Module Is"         fa6-solid:cube
  2. "Splitting Code into Files" fa6-solid:file-code
  3. "Organizing Larger Projects" fa6-solid:folder-tree
  4. "Importing from a Module"  fa6-solid:arrow-right-to-bracket
"""

import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
)

NEW_BODY = """\
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- Card 01 — What a Module Is -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:cube"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">What a Module Is</p>
                <p class="text-[11px] text-gray-600 leading-snug">Any <code class="font-mono">.py</code> file that holds functions is a module your other scripts can share.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 02 — Splitting Code into Files -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:file-code"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Splitting Code into Files</p>
                <p class="text-[11px] text-gray-600 leading-snug">Move related functions into their own <code class="font-mono">.py</code> file so each task has one clear home.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 03 — Organizing Larger Projects -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:folder-tree"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Organizing Larger Projects</p>
                <p class="text-[11px] text-gray-600 leading-snug">Multiple focused module files keep any project readable and safe to update or extend.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 04 — Importing from a Module -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:arrow-right-to-bracket"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Importing from a Module</p>
                <p class="text-[11px] text-gray-600 leading-snug">Use <code class="font-mono">import</code> or <code class="font-mono">from … import</code> to load exactly the functions a script needs.</p>
              </div>
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
            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>
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
    print(f"✅  #recap body replaced  ({before:,} chars → {len(NEW_BODY):,} chars)")
    print(f"   File size: {len(new_html):,} chars")
