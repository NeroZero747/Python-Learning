#!/usr/bin/env python3
"""Rewrite #recap section body in lesson03, mirroring the #objective card labels and icons."""

FILE = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

SECTION_OPEN = '<section id="recap">'
NEXT_SECTION  = '<section id="knowledge-check">'

sec_idx  = content.index(SECTION_OPEN)
next_idx = content.index(NEXT_SECTION, sec_idx)

BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
body_open_pos      = content.index(BODY_OPEN, sec_idx)
body_content_start = body_open_pos + len(BODY_OPEN)

# The section closes with "  </div>\n</section>" just before the next section
OUTER_CLOSE = '  </div>\n</section>'
outer_close_pos = content.rindex(OUTER_CLOSE, sec_idx, next_idx)
end_pos = outer_close_pos

print(f"body_content_start = {body_content_start}")
print(f"end_pos            = {end_pos}")

NEW_BODY = """
      <!-- 2×2 recap card grid — labels and icons mirror the #objective section -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- Card 01 — Tuples: locked, ordered sequences (fa6-solid:lock) -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:lock"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Tuples: locked, ordered sequences</p>
                <p class="text-[11px] text-gray-600 leading-snug">Store a member record as a <code class="font-mono">tuple</code> — its fields stay fixed after enrollment.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 02 — Sets: collections without duplicates (fa6-solid:filter) -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:filter"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Sets: collections without duplicates</p>
                <p class="text-[11px] text-gray-600 leading-snug">Convert a list of diagnosis codes to a <code class="font-mono">set</code> to remove duplicates in one step.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 03 — None: representing missing data (fa6-solid:ban) -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:ban"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">None: representing missing data</p>
                <p class="text-[11px] text-gray-600 leading-snug">Use <code class="font-mono">is None</code> to check whether a field like provider specialty is absent.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 04 — Choosing the right data type (fa6-solid:code-branch) -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:code-branch"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Choosing the right data type</p>
                <p class="text-[11px] text-gray-600 leading-snug"><code class="font-mono">tuple</code> for fixed data, <code class="font-mono">set</code> for unique values, <code class="font-mono">None</code> for absent fields.</p>
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

new_content = content[:body_content_start] + NEW_BODY + "    </div>\n" + content[end_pos:]

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done — recap section rewritten successfully.")
