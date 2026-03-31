#!/usr/bin/env python3
"""Rewrite #mistakes section body in lesson03 with 3 healthcare common-mistakes."""

FILE = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

SECTION_OPEN = '<section id="mistakes">'
NEXT_SECTION  = '<section id="real-world">'

sec_idx  = content.index(SECTION_OPEN)
next_idx = content.index(NEXT_SECTION, sec_idx)

# Body div is the first occurrence of this class string after the section header
BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
body_open_pos    = content.index(BODY_OPEN, sec_idx)
body_content_start = body_open_pos + len(BODY_OPEN)

# End boundary: the closing shell before the next section
END_MARKER = '    </div>\n  </div>\n</section>\n\n' + NEXT_SECTION
end_pos = content.index(END_MARKER, sec_idx)

print(f"body_content_start = {body_content_start}")
print(f"end_pos            = {end_pos}")

NEW_BODY = """
      <!-- ── Tab pill row ────────────────────────────────────────────── -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Modifying a Tuple</span>
        </button>

        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Comparing None Wrong</span>
        </button>

        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Relying on Set Order</span>
        </button>

      </div>

      <!-- ── Mistake 1 — Modifying a Tuple ────────────────────────────── -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Trying to Change a Value Inside a Tuple</h4>
              <p class="text-xs text-gray-500 mt-0.5">Tuples are immutable — assigning to an index raises a TypeError immediately.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Tuples are read-only: once created, their values cannot be changed. Attempting <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">member_record[0] = "Diana Ramos"</code> raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TypeError: 'tuple' object does not support item assignment</code>. To update a field, reassign the entire variable to a new tuple containing the corrected values.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — index assignment
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">member_record = ("Diana Torres", "Gold PPO", "MBR-40291")
member_record[0] = "Diana Ramos"  # TypeError: tuples do not support item assignment</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — reassign the whole tuple
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">member_record = ("Diana Torres", "Gold PPO", "MBR-40291")  # original enrolled record
member_record = ("Diana Ramos", "Gold PPO", "MBR-40291")   # replace with corrected tuple
print(member_record[0])                                    # prints: Diana Ramos</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of a tuple as a sealed enrollment form — individual fields cannot be crossed out after submission. If a name correction is needed, the whole record is reissued as a new tuple with the updated values.</p>
          </div>

        </div>
      </div>

      <!-- ── Mistake 2 — Checking None with == ─────────────────────────── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Using == Instead of is to Check for None</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python's style guide requires <code class="font-mono text-[10px]">is None</code> — using <code class="font-mono text-[10px]">== None</code> can silently misbehave and triggers a linting warning in every professional codebase.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Python defines <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">None</code> as a singleton — there is exactly one <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">None</code> object in memory, so the correct check is <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">is None</code> (identity test). Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">== None</code> works most of the time but can return unexpected results if a class overrides <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">__eq__</code>, and it triggers a PEP 8 E711 linting warning in every professional codebase.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — equality check
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">provider_specialty = None

if provider_specialty == None:      # non-Pythonic — triggers PEP 8 E711
    provider_specialty = "Not on file"</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — identity check
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">provider_specialty = None

if provider_specialty is None:          # correct — tests object identity, not equality
    provider_specialty = "Not on file"  # safe placeholder for any absent specialty

print("Specialty:", provider_specialty) # prints: Specialty: Not on file</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed"><code class="font-mono bg-amber-100 px-1 rounded text-[11px]">None</code> is a singleton — like a "vacant" badge in a staff office, there is only one in the building. <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">is None</code> checks whether you are holding that exact badge; <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">== None</code> only checks whether something merely looks like it.</p>
          </div>

        </div>
      </div>

      <!-- ── Mistake 3 — Relying on Set Order ──────────────────────────── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Assuming a Set Preserves the Order Items Were Added</h4>
              <p class="text-xs text-gray-500 mt-0.5">Sets are unordered — iterating a set produces different output sequences each run.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Unlike a list, a set stores items in an internal hash order that bears no relation to insertion order — so even <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">for code in diagnosis_codes</code> may print codes in a different sequence every time Python starts. When display order matters, wrap the set in <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">sorted()</code> to produce a consistent alphabetical sequence.</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — assuming insertion order
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">diagnosis_codes = {"I10", "E11.9", "J45.909", "Z00.00"}
for code in diagnosis_codes:
    print(code)  # order varies between runs — not "I10" first</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — sort when order matters
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">diagnosis_codes = {"I10", "E11.9", "J45.909", "Z00.00"}  # set ensures uniqueness
for code in sorted(diagnosis_codes):                       # sorted() gives consistent alphabetical order
    print(code)                                            # output is the same every run</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Use a set when all you need is uniqueness — deduplicating claim codes, for example. The moment display order matters (for a printed report or a provider summary), wrap the set in <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">sorted()</code> to convert it to a predictable sequence.</p>
          </div>

        </div>
      </div>

"""

new_content = content[:body_content_start] + NEW_BODY + content[end_pos:]

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done — mistakes section rewritten successfully.")
