#!/usr/bin/env python3
"""Rewrite #overview section body in lesson04_lists_dictionaries.html."""

FILE = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

with open(FILE, encoding="utf-8") as f:
    content = f.read()

# ── Anchor markers ──────────────────────────────────────────────────────────
# The section body opens with `<div class="bg-white px-8 py-7 space-y-5">`
# Inside it, the hook banner:
HOOK_OLD_OPEN = '<div class="relative flex items-start gap-4">'
HOOK_OLD_ICON = '<span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">'

# We replace the whole section body (everything between the body open div and
# the two closing divs+section that end the overview).
SECTION_OPEN_ID = '<section id="overview">'
NEXT_SECTION_ID = '<section id="key-ideas">'

sec_start = content.index(SECTION_OPEN_ID)
next_sec   = content.index(NEXT_SECTION_ID, sec_start)

BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-5">'
body_open_pos      = content.index(BODY_OPEN, sec_start)
body_content_start = body_open_pos + len(BODY_OPEN)

# Find `</div>\n  </div>\n</section>` just before the next section
OUTER_CLOSE = '  </div>\n</section>'
outer_close_pos = content.rindex(OUTER_CLOSE, sec_start, next_sec)

# ── New body content ─────────────────────────────────────────────────────────
NEW_BODY = """
      <!-- Part 1 — Hook quote banner -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">A list keeps multiple values together in a fixed order; a dictionary links each value to a name so you can find it instantly.</p>
        </div>
      </div>

      <!-- Part 2 — Analogy intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Think of a <strong>filing cabinet</strong> in a busy office: one cabinet stores your lists (numbered folders filed in order, one slot per item), while another stores your dictionaries (labelled dividers that let you jump straight to the right folder by name). A <strong>list</strong> is the numbered drawer, and a <strong>dictionary</strong> is the labelled tab — Python is the office manager that lets you create, search, and update both.</p>

      <!-- Part 3 — Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 — pink accent: List -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:list"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">List</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The numbered drawer — items filed in strict order</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">The numbered slots in a drawer, one value per slot, in exact order.</p>
        </div>

        <!-- Card 2 — violet accent: Index -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
              <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:hand-pointer"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Index</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The slot number — pulls out exactly the right item</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">The position number that tells Python which slot to reach into.</p>
        </div>

        <!-- Card 3 — blue accent: Dictionary -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
              <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:book-open"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Dictionary</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The labelled divider — jump straight to the right folder</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">The tabbed divider that maps a name directly to the value behind it.</p>
        </div>

        <!-- Card 4 — emerald accent: Key -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
              <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:tag"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Key</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The tab label — the name written on the divider</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">The unique label you write on a divider to find its folder instantly.</p>
        </div>

      </div>

      <!-- Part 4 — Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">If you have ever used a VLOOKUP in Excel or a JOIN in SQL, you already understand the core idea behind a dictionary — and lists are simply the columns of data you were already pulling values from.</p>
      </div>

"""

new_content = content[:body_content_start] + NEW_BODY + "    </div>\n" + content[outer_close_pos:]

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

# ── Verify ───────────────────────────────────────────────────────────────────
final = open(FILE, encoding="utf-8").read()
checks = [
    ("Hook banner updated", "A list keeps multiple values together in a fixed order"),
    ("items-center on hook flex row", 'flex items-center gap-4'),
    ("Analogy intro Think of", "Think of a <strong>filing cabinet</strong>"),
    ("Card 1 — List pink", "fa6-solid:list"),
    ("Card 2 — Index violet", "fa6-solid:hand-pointer"),
    ("Card 3 — Dictionary blue", "fa6-solid:book-open"),
    ("Card 4 — Key emerald", "fa6-solid:tag"),
    ("Amber tip — Excel/SQL reference", "VLOOKUP in Excel"),
    ("Old table structure removed", "<table"),
    ("Old pill tags removed", "Sales numbers"),
]
print("=== Verification ===")
for label, needle in checks:
    if label.startswith("Old"):
        ok = needle not in final
        print(f"{'✅' if ok else '❌'} — {label} (expected absent)")
    else:
        ok = needle in final
        print(f"{'✅' if ok else '❌'} — {label}")
