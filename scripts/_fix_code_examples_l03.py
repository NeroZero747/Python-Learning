path = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"
with open(path) as f:
    content = f.read()

CE_OPEN   = '<section id="code-examples">'
COMP_OPEN = '<section id="comparison">'

ce_idx   = content.index(CE_OPEN)
comp_idx = content.index(COMP_OPEN)

header_end_marker = '\n    <div class="bg-white px-8 py-7 space-y-6">'
body_start = content.index(header_end_marker, ce_idx)
section_end_marker = '\n\n' + COMP_OPEN
section_end = content.index(section_end_marker, ce_idx)

print("body_start line ~", content[:body_start].count('\n') + 1)
print("section_end line ~", content[:section_end].count('\n') + 1)

new_body = """
    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Member Record</span>
        </button>

        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Unique Diagnosis Codes</span>
        </button>

        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Missing Provider Specialty</span>
        </button>

      </div>

      <!-- Panel 1: Member Record (Tuple) -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Member Record</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Members</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">tuple, indexing</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script stores four pieces of member information in a <strong class="text-gray-800">tuple</strong> and then prints each value by its position. Tuples are ideal for fixed records where the order of fields always stays the same.</p>
              </div>
            </div>
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
                <pre class="overflow-x-auto pre-reset"><code class="language-python">member_record = (&quot;M10042&quot;, &quot;Aisha Patel&quot;, &quot;Gold Plan&quot;, True)  # tuple: member ID, name, plan, active status
print(member_record[0])   # index 0 → member ID
print(member_record[1])   # index 1 → full name
print(member_record[2])   # index 2 → plan type
print(member_record[3])   # index 3 → active status (True or False)</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python member_record.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">M10042<br>Aisha Patel<br>Gold Plan<br>True</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Because tuples cannot be changed after they are created, they protect reference data — like a member's ID or plan type — from being accidentally overwritten later in your script.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 2: Unique Diagnosis Codes (Set) -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Unique Diagnosis Codes</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Claims</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">set, len(), deduplication</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script converts a list of submitted diagnosis codes into a <strong class="text-gray-800">set</strong>, which automatically removes any duplicates. It then uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">len()</code> to compare how many codes were submitted versus how many were unique.</p>
              </div>
            </div>
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
                <pre class="overflow-x-auto pre-reset"><code class="language-python">submitted_codes = [&quot;Z00.00&quot;, &quot;I10&quot;, &quot;Z00.00&quot;, &quot;E11.9&quot;, &quot;I10&quot;, &quot;Z00.00&quot;]  # list with repeats
unique_codes = set(submitted_codes)                                           # set removes duplicates automatically
print(&quot;Total submitted:&quot;, len(submitted_codes))                               # count before deduplication
print(&quot;Unique codes:&quot;, unique_codes)                                          # deduplicated result
print(&quot;Duplicates removed:&quot;, len(submitted_codes) - len(unique_codes))        # how many extras were dropped</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python unique_diagnosis_codes.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Total submitted: 6<br>Unique codes: {'Z00.00', 'I10', 'E11.9'}<br>Duplicates removed: 3</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Sets do not maintain the order of your values, so if you need to display codes in a consistent order, wrap the set in <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">sorted()</code> before printing.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 3: Missing Provider Specialty (None) -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Missing Provider Specialty</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Providers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">None, is None, tuple</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script starts with a provider's specialty set to <strong class="text-gray-800"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">None</code></strong> — meaning it has not been loaded yet — then uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">is None</code> to detect that and fill in a safe default before bundling all three fields into a tuple.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">missing_provider_specialty.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">provider_name = &quot;Dr. Carlos Ruiz&quot;     # provider full name
provider_npi = &quot;1234567890&quot;           # NPI: unique national provider identifier
provider_specialty = None              # None: specialty not yet received from the system

if provider_specialty is None:                           # check whether specialty is missing
    provider_specialty = &quot;Not on file&quot;                   # replace None with a safe default

provider_record = (provider_name, provider_npi, provider_specialty)  # bundle all three into a tuple
print(&quot;Provider:&quot;, provider_record[0])                  # index 0 → name
print(&quot;NPI:&quot;, provider_record[1])                       # index 1 → NPI
print(&quot;Specialty:&quot;, provider_record[2])                 # index 2 → specialty</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python missing_provider_specialty.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Provider: Dr. Carlos Ruiz<br>NPI: 1234567890<br>Specialty: Not on file</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Always use <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">is None</code> to test for a missing value — never <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">== None</code> — because <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">is</code> checks that the variable truly points to nothing, which is the safest and clearest way to express that intent.</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

content = content[:body_start] + new_body + content[section_end:]

with open(path, "w") as f:
    f.write(content)

print("Done — code-examples section rewritten successfully")
