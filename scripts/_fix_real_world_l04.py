#!/usr/bin/env python3
"""Replace #real-world section body in lesson04_lists_dictionaries.html."""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Locate section boundaries ─────────────────────────────────────────────────
SEC_START = 'id="real-world"'
NEXT_SEC  = 'id="recap"'

sec_idx  = content.index(SEC_START)
next_idx = content.index(NEXT_SEC, sec_idx)

BODY_OPEN  = '    <div class="bg-white px-8 py-7 space-y-6">'
body_start = content.index(BODY_OPEN, sec_idx)
body_end   = content.rindex('  </div>\n</section>', sec_idx, next_idx)

# Also fix the subtitle in the section header
old_subtitle = '    <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Practical applications in real-world workflows</p>'
new_subtitle = '    <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How lists and dictionaries are used across healthcare insurance workflows</p>'

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">In healthcare insurance, lists and dictionaries are the two structures that hold almost every piece of data an analyst works with — a list represents a column of values (claim amounts, member IDs, procedure codes) while a dictionary represents a single record (one member's details, one provider's profile, one claim's fields). Understanding both structures lets you read, calculate, and route real healthcare data from the moment it arrives in your script.</p>

      <!-- Three-column domain card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">

        <!-- Members — violet -->
        <div class="rounded-xl border border-violet-100 overflow-hidden">
          <div class="flex items-center gap-2.5 px-4 py-3 bg-violet-50 border-b border-violet-100">
            <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:id-card"></span>
            <h3 class="text-sm font-bold text-gray-800">Members</h3>
          </div>
          <ul class="divide-y divide-violet-50">
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-violet-400 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Enrollment roster</strong> — a list of member names or IDs holds all enrolled members for a plan in a single, indexed sequence</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-violet-400 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Member profile</strong> — a dictionary stores one member's record with named fields like <code>"member_id"</code>, <code>"plan_type"</code>, and <code>"is_active"</code></span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-violet-400 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Premium history</strong> — a list of monthly premium amounts lets you compute totals, averages, and year-over-year comparisons with <code>sum()</code> and <code>len()</code></span>
            </li>
          </ul>
        </div>

        <!-- Claims — pink/brand -->
        <div class="rounded-xl border border-pink-100 overflow-hidden">
          <div class="flex items-center gap-2.5 px-4 py-3 bg-pink-50 border-b border-pink-100">
            <span class="iconify text-[#CB187D] text-base" data-icon="fa6-solid:file-invoice-dollar"></span>
            <h3 class="text-sm font-bold text-gray-800">Claims</h3>
          </div>
          <ul class="divide-y divide-pink-50">
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-[#CB187D] mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Claim amounts batch</strong> — a list of <code>float</code> values holds all submitted claim amounts so <code>sum()</code> calculates the total billed in one call</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-[#CB187D] mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Claim record</strong> — a dictionary maps field names like <code>"claim_id"</code>, <code>"billed_amount"</code>, and <code>"status"</code> to their values for a single claim</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-[#CB187D] mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Procedure code list</strong> — a list of billing codes submitted on one claim can be inspected by index to check the primary code at position <code>[0]</code></span>
            </li>
          </ul>
        </div>

        <!-- Providers — emerald -->
        <div class="rounded-xl border border-emerald-100 overflow-hidden">
          <div class="flex items-center gap-2.5 px-4 py-3 bg-emerald-50 border-b border-emerald-100">
            <span class="iconify text-emerald-600 text-base" data-icon="fa6-solid:user-doctor"></span>
            <h3 class="text-sm font-bold text-gray-800">Providers</h3>
          </div>
          <ul class="divide-y divide-emerald-50">
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-emerald-500 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Provider profile</strong> — a dictionary holds each doctor's record with keys like <code>"name"</code>, <code>"npi"</code>, <code>"specialty"</code>, and <code>"accepting_patients"</code></span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-emerald-500 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Network directory</strong> — a list of in-network NPI numbers lets the system check whether a provider is covered before processing the claim</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-emerald-500 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Billing totals</strong> — a list of amounts billed by one provider across multiple claims can be summed to compare against contracted fee schedules</span>
            </li>
          </ul>
        </div>

      </div>

      <!-- Workflow stepper -->
      <div class="rounded-xl border border-gray-100 overflow-hidden">
        <div class="px-4 py-2.5 bg-gray-50 border-b border-gray-100">
          <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">A typical healthcare claims data workflow</p>
        </div>
        <div class="px-4 py-4">
          <div class="flex flex-wrap items-center gap-2">

            <!-- Step 1 — Load records (violet) -->
            <div class="flex items-center gap-2 rounded-lg border border-violet-100 bg-violet-50 px-3 py-2">
              <span class="iconify text-violet-500 text-sm shrink-0" data-icon="fa6-solid:database"></span>
              <div>
                <p class="text-[10px] font-bold text-violet-700">Load records</p>
                <p class="text-[10px] text-violet-500">Member &amp; claim data</p>
              </div>
            </div>
            <span class="iconify text-gray-300" data-icon="fa6-solid:arrow-right"></span>

            <!-- Step 2 — Store in lists & dicts (pink/brand) -->
            <div class="flex items-center gap-2 rounded-lg border border-pink-100 bg-pink-50 px-3 py-2">
              <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:cubes"></span>
              <div>
                <p class="text-[10px] font-bold text-[#CB187D]">Organise data</p>
                <p class="text-[10px] text-pink-400">Lists &amp; dictionaries</p>
              </div>
            </div>
            <span class="iconify text-gray-300" data-icon="fa6-solid:arrow-right"></span>

            <!-- Step 3 — Read & calculate (blue) -->
            <div class="flex items-center gap-2 rounded-lg border border-blue-100 bg-blue-50 px-3 py-2">
              <span class="iconify text-blue-500 text-sm shrink-0" data-icon="fa6-solid:calculator"></span>
              <div>
                <p class="text-[10px] font-bold text-blue-700">Read &amp; calculate</p>
                <p class="text-[10px] text-blue-500">Totals, averages, lookups</p>
              </div>
            </div>
            <span class="iconify text-gray-300" data-icon="fa6-solid:arrow-right"></span>

            <!-- Step 4 — Output result (emerald) -->
            <div class="flex items-center gap-2 rounded-lg border border-emerald-100 bg-emerald-50 px-3 py-2">
              <span class="iconify text-emerald-600 text-sm shrink-0" data-icon="fa6-solid:file-lines"></span>
              <div>
                <p class="text-[10px] font-bold text-emerald-700">Output result</p>
                <p class="text-[10px] text-emerald-500">Report or dashboard</p>
              </div>
            </div>

          </div>
        </div>
      </div>

'''

# Apply the subtitle fix and body replacement
new_content = content.replace(old_subtitle, new_subtitle, 1)
# Re-read to get updated positions
sec_idx  = new_content.index('id="real-world"')
next_idx = new_content.index('id="recap"', sec_idx)
body_start = new_content.index(BODY_OPEN, sec_idx)
body_end   = new_content.rindex('  </div>\n</section>', sec_idx, next_idx)

new_content = new_content[:body_start] + NEW_BODY + new_content[body_end:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Wrote file.")

# ── Verification ──────────────────────────────────────────────────────────────
with open(TARGET, "r", encoding="utf-8") as f:
    result = f.read()

sec_idx  = result.index('id="real-world"')
next_idx = result.index('id="recap"', sec_idx)
section  = result[sec_idx:next_idx]

checks = [
    ("Intro starts with 'In healthcare insurance'",         "In healthcare insurance," in section),
    ("No code blocks in section",                           'class="language-python"' not in section),
    ("Members card (violet)",                               "border-violet-100" in section and "fa6-solid:id-card" in section),
    ("Claims card (pink/brand)",                            "border-pink-100" in section and "fa6-solid:file-invoice-dollar" in section),
    ("Providers card (emerald)",                            "border-emerald-100" in section and "fa6-solid:user-doctor" in section),
    ("Members — 3 bullets",                                 section.count("text-violet-400 mt-0.5") == 3),
    ("Claims — 3 bullets",                                  section.count('text-[#CB187D] mt-0.5') == 3),
    ("Providers — 3 bullets",                               section.count("text-emerald-500 mt-0.5") == 3),
    ("All 9 bullets present",                               section.count("fa6-solid:check") == 9),
    ("Enrollment roster bullet",                            "Enrollment roster" in section),
    ("Member profile bullet",                               "Member profile" in section),
    ("Claim amounts batch bullet",                          "Claim amounts batch" in section),
    ("Claim record bullet",                                 "Claim record" in section),
    ("Provider profile bullet",                             "Provider profile" in section),
    ("Network directory bullet",                            "Network directory" in section),
    ("Stepper label present",                               "A typical healthcare claims data workflow" in section),
    ("4 stepper steps",                                     section.count("rounded-lg border") == 4),
    ("3 gray arrow connectors",                             section.count('fa6-solid:arrow-right') == 3),
    ("Step 1 — Load records (violet)",                      "Load records" in section and "border-violet-100" in section),
    ("Step 2 — Organise data (pink)",                       "Organise data" in section),
    ("Step 3 — Read & calculate (blue)",                    "Read &amp; calculate" in section),
    ("Step 4 — Output result (emerald)",                    "Output result" in section),
    ("No & without &amp; in HTML content",                  "Member & claim" not in section and "Lists & dicts" not in section),
    ("Subtitle updated",                                    "How lists and dictionaries" in section),
    ("Recap section intact",                                'id="recap"' in result),
]

all_ok = True
for label, check in checks:
    status = "YES" if check else "NO "
    if not check:
        all_ok = False
    print(f"{status}: {label}")

if all_ok:
    print("\nAll checks passed!")
else:
    print("\nSome checks FAILED.")
