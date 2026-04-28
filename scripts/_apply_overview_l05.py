"""
Replace the #overview section body in lesson05_aggregations_count_sum_avg.html
with the correct 4-part structure per lesson-overview.prompt.md.
"""

TARGET = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson05_aggregations_count_sum_avg.html"

# ── Anchor markers ────────────────────────────────────────────────────────────
# Start: the opening of the section body div (unique in the file at this location)
OLD_START = '    <div class="bg-white px-8 py-7 space-y-5"><div class="relative rounded-2xl border border-[#f5c6e0]'

# End: the closing of the old overview body
OLD_END = 'Aggregation functions summarize data across <strong>multiple rows</strong>.</p></div>\n  </div>\n</section>'

# ── New content ───────────────────────────────────────────────────────────────
NEW_CONTENT = '''    <div class="bg-white px-8 py-7 space-y-5">

<!-- Part 1 — Hook quote banner -->
<div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
  <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
      <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
    </span>
    <p class="text-base text-gray-800 leading-relaxed font-medium">Aggregate functions summarize an entire column of data — turning thousands of rows into a single meaningful number.</p>
  </div>
</div>

<!-- Part 2 — Analogy intro paragraph -->
<p class="text-sm text-gray-600 leading-relaxed">Think of your bank statement as a database table: every row is one transaction, and aggregate functions are the summary row at the bottom that does all the arithmetic for you.</p>

<!-- Part 3 — Analogy card grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

  <!-- Card 1 — COUNT — pink accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-base" data-icon="fa6-solid:hashtag"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">COUNT</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The transaction counter — how many rows exist</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">The tally at the bottom of the statement.</p>
  </div>

  <!-- Card 2 — SUM — violet accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
        <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:plus"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">SUM</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The running total — adds every amount together</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">The "Total Spent" figure at the end of the month.</p>
  </div>

  <!-- Card 3 — AVG — blue accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
        <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:divide"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">AVG</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The typical amount — middle ground of all values</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">The average transaction value across all rows.</p>
  </div>

  <!-- Card 4 — Column Aliases (AS) — emerald accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
        <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:tag"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Column Aliases (AS)</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The column label — names your result clearly</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">The heading at the top of each summary column.</p>
  </div>

</div>

<!-- Part 4 — Amber tip -->
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">If you already use SUM and AVERAGE in Excel, you already know what these functions do — SQL just applies them to millions of rows in milliseconds.</p>
</div>

    </div>
  </div>
</section>'''

# ── Apply ─────────────────────────────────────────────────────────────────────
with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# Find the start of the body div up to and including the closing section tag
start_idx = content.find(OLD_START)
if start_idx == -1:
    print("❌ START anchor not found")
    exit(1)

end_idx = content.find(OLD_END)
if end_idx == -1:
    print("❌ END anchor not found")
    exit(1)

end_idx += len(OLD_END)

old_block = content[start_idx:end_idx]
new_content = content[:start_idx] + NEW_CONTENT + content[end_idx:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ Overview section replaced successfully")
print(f"   Removed {len(old_block)} chars, inserted {len(NEW_CONTENT)} chars")
