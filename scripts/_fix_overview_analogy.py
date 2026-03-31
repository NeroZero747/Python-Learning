"""Replace the #overview section body in lesson01_what_is_programming.html
with a 4-part structured layout:
  Part 1 — Hook quote (kept as-is)
  Part 2 — Analogy intro paragraph
  Part 3 — 2-column analogy card grid
  Part 4 — Amber tip box
"""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson01_what_is_programming.html"

# ── Marker strings ────────────────────────────────────────────────────────────
# Everything from the first paragraph after the quote banner through the body
# div closing tag will be replaced.  We anchor on text that only appears once.
OLD_START = '  </div>\n</div>\n<p class="text-sm text-gray-600 leading-relaxed">These instructions are written'
OLD_END   = 'run without manual effort.</p></div>'

NEW_CONTENT = '''  </div>
</div>

<!-- Part 2 — Analogy intro paragraph -->
<p class="text-sm text-gray-600 leading-relaxed">Think of a computer like a very precise chef\'s assistant: it will follow your recipe step by step, in exact order, without skipping or improvising — but only if you write out every instruction clearly. A <strong>program</strong> is that recipe, and Python is the language you use to write it.</p>

<!-- Part 3 — Analogy card grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

  <!-- Card 1: Recipe = Program -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-base" data-icon="fa6-solid:scroll"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">The program</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The recipe — your complete list of steps</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">A program is a written sequence of instructions you prepare in advance. The computer reads from the first line and works through every step in order.</p>
  </div>

  <!-- Card 2: Chef's assistant = Computer -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
        <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:robot"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">The computer</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The assistant — follows steps without improvising</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">Your computer executes each instruction exactly as written — never skipping, reordering, or making assumptions. Clear and precise instructions are essential.</p>
  </div>

  <!-- Card 3: Batch prep = Automation -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
        <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:arrows-rotate"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Automation</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">Batch prep — repeat the same steps on any scale</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">Once your recipe is written, Python can run it on 10 rows of data or 10 million rows with no extra effort from you.</p>
  </div>

  <!-- Card 4: Recipe language = Python -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
        <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:code"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Python</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The language — how you write the recipe</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">Python is one specific programming language. It\'s popular among data professionals because its syntax reads almost like plain English.</p>
  </div>

</div>

<!-- Part 4 — Amber tip -->
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">You already use tools that run step-by-step instructions — every Excel formula and SQL query is a form of programming. Python gives you a more powerful and flexible way to do the same thing.</p>
</div>
</div>'''

# ── Run ───────────────────────────────────────────────────────────────────────
with open(TARGET, "r", encoding="utf-8") as f:
    src = f.read()

start_idx = src.find(OLD_START)
if start_idx == -1:
    print("❌ OLD_START marker not found — no changes made")
    raise SystemExit(1)

end_idx = src.find(OLD_END, start_idx)
if end_idx == -1:
    print("❌ OLD_END marker not found — no changes made")
    raise SystemExit(1)

end_idx += len(OLD_END)   # include the marker itself
old_block = src[start_idx:end_idx]

result = src[:start_idx] + NEW_CONTENT + src[end_idx:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(result)

print(f"✅ Overview section replaced ({len(old_block)} chars → {len(NEW_CONTENT)} chars)")
