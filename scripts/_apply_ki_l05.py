"""
1. Add the obj-card Key Takeaways hover CSS to lesson05.
2. Replace the #key-ideas section body with 3 new cards.
"""

TARGET = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson05_aggregations_count_sum_avg.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── 1. Add missing hover CSS ─────────────────────────────────────────────────
OLD_CSS = "    /* ── Card hover animations — Mistake, Flow, Recap, Overview cards  */"

NEW_CSS = """    /* ── Card hover animations — Key Takeaways cards ──────────── */
    .obj-card {
      transition: transform 0.22s cubic-bezier(.4,0,.2,1),
                  box-shadow 0.22s cubic-bezier(.4,0,.2,1),
                  border-color 0.22s ease, background-color 0.22s ease;
    }
    .obj-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 32px -6px rgba(203,24,125,0.18), 0 6px 12px -2px rgba(203,24,125,0.1);
      border-color: #CB187D;
      background-color: #fdf0f7;
    }
    .obj-card .obj-icon {
      transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease;
    }
    .obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
    .obj-card:hover .obj-icon .iconify { color: white !important; }
    .obj-card-kt:hover    { box-shadow: none; background-color: #ffffff; border-color: #CB187D; }
    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }
    .obj-card-blue:hover   { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }

    /* ── Card hover animations — Mistake, Flow, Recap, Overview cards  */"""

if OLD_CSS in content:
    content = content.replace(OLD_CSS, NEW_CSS, 1)
    print("✅ CSS hover block added")
else:
    print("❌ CSS anchor not found — check file")
    exit(1)

# ── 2. Replace #key-ideas body ───────────────────────────────────────────────
OLD_KI_START = '    <div class="bg-white px-8 py-7 space-y-4"><div class="obj-card flex flex-col md:flex-row rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">'

OLD_KI_END = '</div>\n  </div>\n</section>\n\n<section id="key-concepts">'

NEW_KI = '''    <div class="bg-white px-8 py-7 space-y-4">

<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:table"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Aggregates Process the Whole Column</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Every aggregate function scans the entire column automatically — you never copy cells into a formula or loop through rows one by one, even across a million-row table.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Whole Column</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">No Looping</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">One Query</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:circle-xmark"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">NULL Values Are Skipped Silently</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">SUM and AVG ignore any NULL (empty) cell when calculating, keeping your totals accurate even when some rows have missing data — though COUNT(*) still counts every row regardless.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">NULL Skipped</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">COUNT(*)</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Missing Data</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:tag"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Aliases Make Results Readable</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Without AS, SQL names your result column "SUM(revenue)" — awkward in a dashboard or report — so analysts always add an alias like "total_revenue" to produce a clean, professional column heading.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">AS Keyword</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Column Label</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Readable Output</span>
    </div>
  </div>
</div>

    </div>
  </div>
</section>

<section id="key-concepts">'''

start_idx = content.find(OLD_KI_START)
if start_idx == -1:
    print("❌ key-ideas body START anchor not found")
    exit(1)

end_idx = content.find(OLD_KI_END)
if end_idx == -1:
    print("❌ key-ideas body END anchor not found")
    exit(1)

end_idx += len(OLD_KI_END)

content = content[:start_idx] + NEW_KI + content[end_idx:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Key Takeaways section replaced successfully")
