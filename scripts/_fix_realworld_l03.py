#!/usr/bin/env python3
"""Rewrite #real-world section body in lesson03 with proper healthcare content."""

FILE = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

SECTION_OPEN = '<section id="real-world">'
NEXT_SECTION  = '<section id="recap">'

sec_idx  = content.index(SECTION_OPEN)
next_idx = content.index(NEXT_SECTION, sec_idx)

# Locate the section body div
BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
body_open_pos      = content.index(BODY_OPEN, sec_idx)
body_content_start = body_open_pos + len(BODY_OPEN)

# End boundary: locate the outer </div></section> just before the next section
# The real-world section closes with: </div>\n  </div>\n</section>\n\n<section id="recap">
# We find the next section start (reliable), then walk back to find the body closing.
NEXT_SEC_POS  = content.index('\n\n' + NEXT_SECTION, sec_idx)
# body end = position of "\n    </div>" closest to NEXT_SEC_POS that is after body_content_start
# Simpler: find "  </div>\n</section>" just before the next section
OUTER_CLOSE = '  </div>\n</section>'
outer_close_pos = content.rindex(OUTER_CLOSE, sec_idx, NEXT_SEC_POS)
end_pos = outer_close_pos  # we keep "  </div>\n</section>\n\n" in the file, only replace body content

print(f"body_content_start = {body_content_start}")
print(f"end_pos (outer close before recap) = {end_pos}")

# Also fix the subtitle text in the section header
OLD_SUBTITLE = '<p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Practical applications in real-world workflows</p>'
NEW_SUBTITLE = '<p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How tuples, sets, and None are used across healthcare insurance workflows</p>'

NEW_BODY = """
      <!-- Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">In healthcare insurance, analysts work with data that is either <strong>fixed and ordered</strong> (a member's enrollment record), <strong>deduplicated</strong> (a list of unique diagnosis codes on a claim), or <strong>potentially absent</strong> (a provider's specialty that has not yet been supplied by the credentialing feed). Tuples, sets, and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">None</code> are the three Python structures that model each of those realities directly, making raw healthcare data safe to store, compare, and report on.</p>

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
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Enrollment record</strong> — the member's ID, plan type, and effective date are stored as a <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">tuple</code> so no field can be overwritten after enrollment is confirmed.</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-violet-400 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Missing contact details</strong> — a phone number not yet supplied by the member is stored as <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">None</code> so the system can distinguish "not provided" from an empty string.</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-violet-400 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Unique plan codes</strong> — a <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">set</code> built from a member's coverage history holds each plan code exactly once, making it easy to count how many distinct plans they have ever held.</span>
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
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Diagnosis code deduplication</strong> — a <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">set</code> converts the raw list of diagnosis codes on a batch of claims into a unique collection so each condition is counted once.</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-[#CB187D] mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Fixed service line record</strong> — the procedure code, service date, and billed amount for a line item are stored as a <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">tuple</code> to prevent accidental edits during processing.</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-[#CB187D] mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Missing adjudication reason</strong> — a claim that has not yet been reviewed stores its denial reason as <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">None</code>, allowing downstream code to skip it until a reason is assigned.</span>
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
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Credentialing record</strong> — the NPI number, tax ID, and license number are grouped in a <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">tuple</code> so the identifiers travel together and cannot be individually reassigned.</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-emerald-500 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Missing specialty</strong> — a provider whose specialty was not supplied by the credentialing feed stores that field as <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">None</code> until the data is received and verified.</span>
            </li>
            <li class="flex items-start gap-3 px-4 py-3">
              <span class="iconify text-emerald-500 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:check"></span>
              <span class="text-xs text-gray-600 leading-relaxed"><strong class="text-gray-800">Contracted network set</strong> — a <code class="font-mono bg-gray-100 px-0.5 rounded text-[10px]">set</code> holds the unique NPI numbers of all contracted in-network providers, making membership lookups instant with no duplicate entries.</span>
            </li>
          </ul>
        </div>

      </div>

      <!-- Workflow stepper -->
      <div class="rounded-xl border border-gray-100 overflow-hidden">
        <div class="px-4 py-2.5 bg-gray-50 border-b border-gray-100">
          <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">A typical claims data-cleaning workflow</p>
        </div>
        <div class="px-4 py-4">
          <div class="flex flex-wrap items-center gap-2">

            <!-- Step 1 — Import raw claim records (violet) -->
            <div class="flex items-center gap-2 rounded-lg border border-violet-100 bg-violet-50 px-3 py-2">
              <span class="iconify text-violet-500 text-sm shrink-0" data-icon="fa6-solid:database"></span>
              <div>
                <p class="text-[10px] font-bold text-violet-700">Import records</p>
                <p class="text-[10px] text-violet-500">Raw claim &amp; member data</p>
              </div>
            </div>
            <span class="iconify text-gray-300" data-icon="fa6-solid:arrow-right"></span>

            <!-- Step 2 — Fix values as tuples (pink) -->
            <div class="flex items-center gap-2 rounded-lg border border-pink-100 bg-pink-50 px-3 py-2">
              <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:lock"></span>
              <div>
                <p class="text-[10px] font-bold text-[#CB187D]">Lock fixed fields</p>
                <p class="text-[10px] text-pink-400">Store as tuples</p>
              </div>
            </div>
            <span class="iconify text-gray-300" data-icon="fa6-solid:arrow-right"></span>

            <!-- Step 3 — Deduplicate with sets, guard None (blue) -->
            <div class="flex items-center gap-2 rounded-lg border border-blue-100 bg-blue-50 px-3 py-2">
              <span class="iconify text-blue-500 text-sm shrink-0" data-icon="fa6-solid:filter"></span>
              <div>
                <p class="text-[10px] font-bold text-blue-700">Clean &amp; deduplicate</p>
                <p class="text-[10px] text-blue-500">Sets &amp; None guards</p>
              </div>
            </div>
            <span class="iconify text-gray-300" data-icon="fa6-solid:arrow-right"></span>

            <!-- Step 4 — Output clean report (emerald) -->
            <div class="flex items-center gap-2 rounded-lg border border-emerald-100 bg-emerald-50 px-3 py-2">
              <span class="iconify text-emerald-600 text-sm shrink-0" data-icon="fa6-solid:file-lines"></span>
              <div>
                <p class="text-[10px] font-bold text-emerald-700">Output clean report</p>
                <p class="text-[10px] text-emerald-500">Verified claim data</p>
              </div>
            </div>

          </div>
        </div>
      </div>

"""

# NEW_BODY replaces everything from body_content_start up to (not including)
# the outer div close "  </div>\n</section>".
# We must close the body div <div class="bg-white px-8 py-7 space-y-6"> ourselves.
new_content = content[:body_content_start] + NEW_BODY + "    </div>\n" + content[end_pos:]

# Fix the subtitle in the section header
new_content = new_content.replace(OLD_SUBTITLE, NEW_SUBTITLE, 1)

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done — real-world section rewritten successfully.")
