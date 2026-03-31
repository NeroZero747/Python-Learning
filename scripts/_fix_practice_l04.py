#!/usr/bin/env python3
"""Replace #practice section body in lesson04_lists_dictionaries.html."""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Locate section boundaries ─────────────────────────────────────────────────
SEC_START = 'id="practice"'
NEXT_SEC  = 'id="mistakes"'

sec_idx  = content.index(SEC_START)
next_idx = content.index(NEXT_SEC, sec_idx)

BODY_OPEN  = '    <div class="bg-white px-8 py-7 space-y-6">'
body_start = content.index(BODY_OPEN, sec_idx)
body_end   = content.rindex('  </div>\n</section>', sec_idx, next_idx)

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- 1 · Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Build a Roster</span>
        </button>

        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Total Claims</span>
        </button>

        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Read a Record</span>
        </button>

      </div>

      <!-- 2 · Exercise 1 — Build a Roster (Members) -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Build a Roster</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Members</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">list</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">len()</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">A health plan has three enrolled members: "Alice Nguyen", "Carlos Rivera", and "Maria Santos". Create a list called <code class="font-mono">enrolled_members</code> that holds all three names in this order. Then print the first member using index <code class="font-mono">[0]</code>, the last member using index <code class="font-mono">[-1]</code>, and the total count using <code class="font-mono">len()</code> — your output should show three separate lines.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">member_roster.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">enrolled_members = ["Alice Nguyen", "Carlos Rivera", "Maria Santos"]  # list of enrolled members
print(enrolled_members[0])   # print the first member (index 0)
print(enrolled_members[-1])  # print the last member (index -1)
print(len(enrolled_members)) # print the total number of members</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python member_roster.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Alice Nguyen<br>Maria Santos<br>3</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Using <code class="font-mono">len()</code> on a member list gives you the current enrollment count without counting manually — a real member portal might call this every time the roster is displayed to show how many active members a plan currently has.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- 2 · Exercise 2 — Total Claims (Claims) -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Total Claims</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Claims</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">list</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">sum()</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">A provider submitted four claims this week with amounts of $120, $350, $85, and $240. Create a list called <code class="font-mono">claim_amounts</code> that holds all four values. Then use <code class="font-mono">sum()</code> to calculate the total billed and <code class="font-mono">len()</code> to count the claims, and print both results — your output should show two separate lines.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">claim_totals.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">claim_amounts = [120, 350, 85, 240]     # list of claim amounts submitted this week
total_billed = sum(claim_amounts)        # add all claim amounts together
claim_count = len(claim_amounts)         # count how many claims were submitted
print("Total billed:", total_billed)     # display the total amount billed
print("Number of claims:", claim_count)  # display the claim count</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python claim_totals.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Total billed: 795<br>Number of claims: 4</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Storing claim amounts in a list and using <code class="font-mono">sum()</code> means you can add a new claim simply by appending another number to the list — the total recalculates automatically, which is exactly how a claims processing system keeps a running balance without rewriting the calculation logic.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- 2 · Exercise 3 — Read a Record (Providers) -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Read a Record</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Providers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">dict</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">key lookup</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">A provider directory stores each doctor's information as a dictionary. Create a dictionary called <code class="font-mono">provider</code> with four fields: <code class="font-mono">"name"</code> set to <code class="font-mono">"Dr. Lee"</code>, <code class="font-mono">"specialty"</code> set to <code class="font-mono">"Cardiology"</code>, <code class="font-mono">"npi"</code> set to <code class="font-mono">"1234567890"</code>, and <code class="font-mono">"accepting_patients"</code> set to <code class="font-mono">True</code>. Then print the provider's name and specialty by looking them up using their key names — your output should show two lines.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">provider_record.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">provider = {                             # create a provider record as a dictionary
    &quot;name&quot;: &quot;Dr. Lee&quot;,                 # provider&apos;s full name
    &quot;specialty&quot;: &quot;Cardiology&quot;,          # medical specialty
    &quot;npi&quot;: &quot;1234567890&quot;,               # national provider identifier
    &quot;accepting_patients&quot;: True          # whether the provider is accepting new patients
}
print(provider[&quot;name&quot;])                # look up and print the provider&apos;s name
print(provider[&quot;specialty&quot;])           # look up and print the medical specialty</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python provider_record.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Dr. Lee<br>Cardiology</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Dictionaries are the natural format for provider records because every field has a meaningful name — when your code reads <code class="font-mono">provider["npi"]</code> instead of <code class="font-mono">provider[2]</code>, anyone reading the script immediately understands what data is being accessed, which matters when a team of analysts is sharing the same codebase.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

'''

new_content = content[:body_start] + NEW_BODY + content[body_end:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Wrote file.")

# ── Verification ──────────────────────────────────────────────────────────────
with open(TARGET, "r", encoding="utf-8") as f:
    result = f.read()

sec_idx  = result.index('id="practice"')
next_idx = result.index('id="mistakes"', sec_idx)
section  = result[sec_idx:next_idx]

checks = [
    ("3 tab pills",                         section.count('class="pe-step') == 3),
    ("No 'Exercise N' tab labels",          "Exercise 1" not in section and "Exercise 2" not in section),
    ("Tab 1 — Build a Roster",              "Build a Roster" in section),
    ("Tab 2 — Total Claims",                "Total Claims" in section),
    ("Tab 3 — Read a Record",               "Read a Record" in section),
    ("3 pe-panels",                         section.count('class="pe-panel') == 3),
    ("Panel 1 active (no hidden)",          'pe-panel pe-panel-anim"' in section or 'pe-panel pe-panel-anim" role' in section),
    ("Panels 2+3 hidden",                   section.count('pe-panel pe-panel-anim hidden') == 2),
    ("Watermarks 01 02 03",                 "01</span>" in section and "02</span>" in section and "03</span>" in section),
    ("No traffic-light dots",              'bg-red-400/80' not in section),
    ("Domain — Members",                    ">Members<" in section),
    ("Domain — Claims",                     ">Claims<" in section),
    ("Domain — Providers",                  ">Providers<" in section),
    ("member_roster.py filename",           "member_roster.py" in section),
    ("claim_totals.py filename",            "claim_totals.py" in section),
    ("provider_record.py filename",         "provider_record.py" in section),
    ("Terminal panes present (x3)",         section.count('fa6-solid:terminal') == 3),
    ("Amber tips present (x3)",             section.count('bg-amber-tip') == 3),
    ("Task boxes present (x3)",             section.count('fa6-solid:clipboard-list') == 3),
    ("Accordion toggles present (x3)",      section.count('toggleAccordion') == 3),
    ("Code: enrolled_members list",         "enrolled_members" in section),
    ("Code: claim_amounts list",            "claim_amounts" in section),
    ("Code: provider dict",                 'provider = {' in section),
    ("Output: Alice Nguyen",                "Alice Nguyen" in section),
    ("Output: Total billed: 795",           "Total billed: 795" in section),
    ("Output: Dr. Lee",                     "Dr. Lee" in section),
    ("Mistakes section intact",             'id="mistakes"' in result),
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
