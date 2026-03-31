#!/usr/bin/env python3
"""Rewrite #practice section body in lesson03 with 3 healthcare exercises."""

FILE = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

# --- 1. Fix section header icon (dumbbell → pencil) within practice section ---
prac_idx = content.index('<section id="practice">')
next_sec = '<section id="mistakes">'
next_sec_pos = content.index(next_sec, prac_idx)

practice_chunk = content[prac_idx:next_sec_pos]
if 'data-icon="fa6-solid:dumbbell"' in practice_chunk:
    new_practice_chunk = practice_chunk.replace(
        'data-icon="fa6-solid:dumbbell"',
        'data-icon="fa6-solid:pencil"',
        1
    )
    content = content[:prac_idx] + new_practice_chunk + content[next_sec_pos:]
    print("Icon fixed: dumbbell → pencil")
    # Recalculate positions after replacement
    prac_idx = content.index('<section id="practice">')
    next_sec_pos = content.index(next_sec, prac_idx)
else:
    print("Icon already correct or dumbbell not found in practice section")

# --- 2. Locate body div boundaries ---
BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
body_open_pos = content.index(BODY_OPEN, prac_idx)
body_content_start = body_open_pos + len(BODY_OPEN)

END_MARKER = '    </div>\n  </div>\n</section>\n\n<section id="mistakes">'
end_pos = content.index(END_MARKER, prac_idx)

print(f"Body content start index: {body_content_start}")
print(f"Body content end   index: {end_pos}")

# --- 3. New body HTML ---
NEW_BODY = """
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Build a Member Record</span>
        </button>

        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Count Unique Codes</span>
        </button>

        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Handle Missing Specialty</span>
        </button>

      </div>

      <!-- ── Exercise 1 — Members — Build a Member Record ───────────────── -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Build a Member Record</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Members</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">tuple</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">indexing</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">Your benefits system stores each member&apos;s key details as a tuple so the values cannot be changed after enrollment. Create a tuple called <code>member_record</code> that holds three values: the member&apos;s full name, their plan type, and their member ID. Then print each value separately by accessing the tuple at its position index — <code>[0]</code>, <code>[1]</code>, and <code>[2]</code>.</p>
              </div>
            </div>

            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">member_record.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">member_record = ("Diana Torres", "Gold PPO", "MBR-40291")  # store name, plan, and ID as a fixed tuple
member_name   = member_record[0]                            # get the member name at index 0
member_plan   = member_record[1]                            # get the plan type at index 1
member_id     = member_record[2]                            # get the member ID at index 2

print("Name:", member_name)                                 # print the member&apos;s full name
print("Plan:", member_plan)                                 # print the health plan type
print("ID:  ", member_id)                                   # print the member ID number</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python member_record.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Name: Diana Torres<br>Plan: Gold PPO<br>ID:   MBR-40291</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Storing member details in a tuple prevents accidental changes — once a member is enrolled, their ID and plan type should not be overwritten by a coding mistake. Tuples enforce that protection at the language level, with no extra code required.</p>
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- ── Exercise 2 — Claims — Count Unique Diagnosis Codes ──────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Count Unique Codes</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Claims</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">set</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">len()</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">A batch of eight claims was submitted with the following diagnosis codes — some appear more than once: <code>"J45.909"</code>, <code>"I10"</code>, <code>"E11.9"</code>, <code>"J45.909"</code>, <code>"I10"</code>, <code>"Z00.00"</code>, <code>"E11.9"</code>, <code>"M54.5"</code>. Convert the list to a set to remove duplicates, then print the deduplicated set and the total count of unique codes using <code>len()</code>.</p>
              </div>
            </div>

            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">unique_diagnosis_codes.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">diagnosis_codes = ["J45.909", "I10", "E11.9", "J45.909", "I10", "Z00.00", "E11.9", "M54.5"]  # raw codes, some duplicated

unique_codes = set(diagnosis_codes)        # convert list to set — removes all duplicates automatically
unique_count = len(unique_codes)           # count how many distinct codes remain

print("Unique codes:", unique_codes)       # print the deduplicated set (display order may vary each run)
print("Total distinct:", unique_count)     # print the count — always reliable</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python unique_diagnosis_codes.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Unique codes: {&apos;I10&apos;, &apos;Z00.00&apos;, &apos;J45.909&apos;, &apos;E11.9&apos;, &apos;M54.5&apos;}<br>Total distinct: 5</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">In claims processing, duplicate diagnosis codes can inflate condition counts and skew risk scores. Converting a raw list to a set is a fast, one-line way to guarantee each code is counted exactly once — the display order of the set may vary between runs, but <code>len()</code> always returns the correct count.</p>
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- ── Exercise 3 — Providers — Handle Missing Provider Specialty ───── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Handle Missing Specialty</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Providers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">None</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">is None</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">A new provider record was imported from a credentialing data feed, but the specialty field did not arrive — your system stored it as <code>None</code>. Write a program that checks whether the specialty value is <code>None</code> using <code>is None</code>, and if it is, assigns the placeholder text <code>&quot;Not on file&quot;</code> before printing the full provider summary.</p>
              </div>
            </div>

            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">provider_specialty.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">provider_name      = "Dr. Amara Osei"  # provider full name from the import feed
provider_specialty = None               # specialty field is missing — stored as None

if provider_specialty is None:          # check whether the value is truly absent
    provider_specialty = "Not on file"  # assign a safe placeholder so the field is never blank

print("Provider:", provider_name)       # print the provider&apos;s full name
print("Specialty:", provider_specialty) # print specialty — now guaranteed to be a string</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python provider_specialty.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Provider: Dr. Amara Osei<br>Specialty: Not on file</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Healthcare provider directories often receive incomplete data from credentialing feeds. Checking for <code>None</code> before displaying a field prevents your reports from showing a raw "None" label to end users — replacing it with a clear placeholder keeps provider records readable and professional.</p>
              </div>
            </div>

          </div>
        </div>
      </div>

"""

new_content = content[:body_content_start] + NEW_BODY + content[end_pos:]

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done — practice section rewritten successfully.")
