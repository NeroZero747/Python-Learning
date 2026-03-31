"""Replace the #code-examples section body in lesson04 with 3 healthcare examples."""

TARGET = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html'

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate boundaries
ce_start = content.index('<section id="code-examples">')
comp_start = content.index('<section id="comparison">', ce_start)

# Find the body div start (after section header closing div)
body_marker = '<div class="bg-white px-8 py-7 space-y-6">'
body_start = content.index(body_marker, ce_start)

# The section closes just before #comparison
section_end = content.rindex('</section>', ce_start, comp_start) + len('</section>')
body_end = content.rindex('</div>\n</section>', ce_start, comp_start) + len('</div>\n</section>')

NEW_BODY = '''<div class="bg-white px-8 py-7 space-y-6">

  <!-- ── Tab pill row ── -->
  <div class="flex items-center gap-2 mb-6" role="tablist">

    <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
      <span class="ce-step-label text-xs font-bold">Member Roster</span>
    </button>

    <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
      <span class="ce-step-label text-xs font-bold">Claim Totals</span>
    </button>

    <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
      <span class="ce-step-label text-xs font-bold">Provider Record</span>
    </button>

  </div>

  <!-- ══════════════════════════════════════════════════════════════════ -->
  <!-- Panel 1 — Member Roster (Members / list + index)  ACTIVE         -->
  <!-- ══════════════════════════════════════════════════════════════════ -->
  <div class="ce-panel ce-panel-anim" role="tabpanel">
    <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

      <!-- Panel header -->
      <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
        <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
        <div class="relative flex items-center gap-3">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
            <span class="iconify text-base" data-icon="fa6-solid:code"></span>
          </span>
          <div>
            <h3 class="font-bold text-gray-800">Member Roster</h3>
            <div class="flex items-center gap-2 mt-1">
              <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
              </span>
              <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Members</span>
              <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">list</span>
              <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">index</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel body -->
      <div class="px-6 py-5 space-y-4">

        <div class="flex items-start gap-3 rounded-xl p-4 task-box">
          <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
          <div>
            <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
            <p class="text-sm text-gray-600">This script stores three member names in a <strong class="text-gray-800">list</strong>, then uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">index</code> positions to read the first and last name without knowing them in advance.</p>
          </div>
        </div>

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
            <pre class="overflow-x-auto pre-reset"><code class="language-python">enrolled_members = [&quot;Alice Chen&quot;, &quot;Bernard Lopez&quot;, &quot;Diana Park&quot;]  # list of member names

first_member = enrolled_members[0]    # index 0 = first item
last_member  = enrolled_members[-1]   # index -1 = last item, any list length

print(&quot;First enrolled:&quot;, first_member)        # prints Alice Chen
print(&quot;Last enrolled:&quot;, last_member)          # prints Diana Park
print(&quot;Total members:&quot;, len(enrolled_members)) # len() counts items → 3</code></pre>
          </div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ python member_roster.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">First enrolled: Alice Chen<br>Last enrolled: Diana Park<br>Total members: 3</div>
          </div>
        </div>

        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">Using index <code class="text-xs font-mono px-1 rounded bg-orange-100 text-orange-800">-1</code> always gives you the last item — even if the roster grows from 3 members to 300,000.</p>
        </div>

      </div>
    </div>
  </div><!-- /panel 1 -->

  <!-- ══════════════════════════════════════════════════════════════════ -->
  <!-- Panel 2 — Claim Totals (Claims / list + sum + len)  INACTIVE      -->
  <!-- ══════════════════════════════════════════════════════════════════ -->
  <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
    <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

      <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
        <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
        <div class="relative flex items-center gap-3">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
            <span class="iconify text-base" data-icon="fa6-solid:code"></span>
          </span>
          <div>
            <h3 class="font-bold text-gray-800">Claim Totals</h3>
            <div class="flex items-center gap-2 mt-1">
              <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
              </span>
              <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Claims</span>
              <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">sum()</span>
              <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">len()</span>
            </div>
          </div>
        </div>
      </div>

      <div class="px-6 py-5 space-y-4">

        <div class="flex items-start gap-3 rounded-xl p-4 task-box">
          <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
          <div>
            <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
            <p class="text-sm text-gray-600">This script stores four claim amounts in a <strong class="text-gray-800">list</strong>, then uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">sum()</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">len()</code> to calculate a total and an average in two lines.</p>
          </div>
        </div>

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
            <pre class="overflow-x-auto pre-reset"><code class="language-python">claim_amounts = [1200.00, 850.50, 3400.75, 520.00]  # approved claim amounts in dollars

total_billed   = sum(claim_amounts)            # sum() adds every number in the list
claim_count    = len(claim_amounts)            # len() counts how many claims there are
average_claim  = total_billed / claim_count    # divide total by count for the average

print(&quot;Claims processed:&quot;, claim_count)   # → 4
print(&quot;Total billed:    &quot;, total_billed)   # → 5971.25
print(&quot;Average claim:   &quot;, average_claim)  # → 1492.8125</code></pre>
          </div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ python claim_totals.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">Claims processed: 4<br>Total billed:     5971.25<br>Average claim:    1492.8125</div>
          </div>
        </div>

        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">Add a new claim amount to the list and Python recalculates the total, count, and average automatically — no formula editing needed.</p>
        </div>

      </div>
    </div>
  </div><!-- /panel 2 -->

  <!-- ══════════════════════════════════════════════════════════════════ -->
  <!-- Panel 3 — Provider Record (Providers / dictionary)  INACTIVE      -->
  <!-- ══════════════════════════════════════════════════════════════════ -->
  <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
    <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

      <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
        <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
        <div class="relative flex items-center gap-3">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
            <span class="iconify text-base" data-icon="fa6-solid:code"></span>
          </span>
          <div>
            <h3 class="font-bold text-gray-800">Provider Record</h3>
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

      <div class="px-6 py-5 space-y-4">

        <div class="flex items-start gap-3 rounded-xl p-4 task-box">
          <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
          <div>
            <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
            <p class="text-sm text-gray-600">This script stores five provider fields in a <strong class="text-gray-800">dictionary</strong>, then retrieves each value by its <strong class="text-gray-800">key name</strong> — the same way a database row is accessed by column name.</p>
          </div>
        </div>

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
            <pre class="overflow-x-auto pre-reset"><code class="language-python">provider = {
    &quot;name&quot;:      &quot;Dr. Sandra Okafor&quot;,  # provider full name
    &quot;npi&quot;:       &quot;1234567890&quot;,          # National Provider Identifier
    &quot;specialty&quot;: &quot;Cardiology&quot;,          # clinical specialty
    &quot;network&quot;:   &quot;In-Network&quot;,          # contracted status
    &quot;ytd_claims&quot;: 47,                   # claims processed year-to-date
}

print(&quot;Provider:  &quot;, provider[&quot;name&quot;])        # look up by key &quot;name&quot;
print(&quot;Specialty: &quot;, provider[&quot;specialty&quot;])   # look up by key &quot;specialty&quot;
print(&quot;Status:    &quot;, provider[&quot;network&quot;])      # look up by key &quot;network&quot;
print(&quot;YTD Claims:&quot;, provider[&quot;ytd_claims&quot;])  # look up by key &quot;ytd_claims&quot;</code></pre>
          </div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ python provider_record.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">Provider:   Dr. Sandra Okafor<br>Specialty:  Cardiology<br>Status:     In-Network<br>YTD Claims: 47</div>
          </div>
        </div>

        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">A dictionary is the natural shape of one provider record — each field name becomes a key, so you retrieve data by name rather than by remembering which column position holds which value.</p>
        </div>

      </div>
    </div>
  </div><!-- /panel 3 -->

</div>'''

# Build result: keep everything up to the body div start, inject new body, then the closing section tag
result = content[:body_start] + NEW_BODY + '\n  </div>\n</section>\n\n' + content[comp_start:]

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(result)

print('Wrote file.')

# Verify
with open(TARGET, 'r', encoding='utf-8') as f:
    check = f.read()

ce_s = check.index('id="code-examples"')
comp_s = check.index('id="comparison"', ce_s)
section = check[ce_s:comp_s]

tests = [
    ('3 tab pills',                   section.count('<button onclick="switchCeTab(') == 3),
    ('No Example 1/2/3 labels',       'Example 1' not in section and 'Example 2' not in section),
    ('Tab — Member Roster',           'Member Roster' in section),
    ('Tab — Claim Totals',            'Claim Totals' in section),
    ('Tab — Provider Record',         'Provider Record' in section),
    ('3 ce-panels',                   section.count('class="ce-panel ce-panel-anim"') + section.count('class="ce-panel ce-panel-anim hidden"') == 3),
    ('Panel 1 active (no hidden)',    section.count('class="ce-panel ce-panel-anim"') == 1),
    ('Panels 2-3 hidden',             section.count('class="ce-panel ce-panel-anim hidden"') == 2),
    ('Watermarks 01 02 03',           '">01<' in section and '">02<' in section and '">03<' in section),
    ('No traffic-light dots',         'bg-red-400/80' not in section),
    ('Terminal panes present',        section.count('bg-[#11111b]') == 3),
    ('Amber tips present',            section.count('bg-amber-tip') == 3),
    ('member_roster.py',              'member_roster.py' in section),
    ('claim_totals.py',               'claim_totals.py' in section),
    ('provider_record.py',            'provider_record.py' in section),
    ('Members domain pill',           'Members' in section),
    ('Claims domain pill',            'Claims' in section),
    ('Providers domain pill',         'Providers' in section),
    ('comparison section intact',     check.count('id="comparison"') >= 1),
]

all_ok = True
for label, passed in tests:
    mark = 'YES' if passed else 'NO '
    if not passed:
        all_ok = False
    print(f'{mark}: {label}')

print()
print('All checks passed!' if all_ok else 'Some checks FAILED.')
