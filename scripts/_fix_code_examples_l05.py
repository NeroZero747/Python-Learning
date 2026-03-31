"""
Rewrites the #code-examples section body in lesson05_operators.html.
Three healthcare examples: Members (arithmetic) / Claims (comparison) / Providers (logical + assignment)
"""

import re

TARGET = (
    "/Users/graywolf/Documents/Project/Python-Learning/"
    "pages/track_01/mod_02_programming_foundations/lesson05_operators.html"
)

NEW_BODY = '''\
    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Calculate Member Cost</span>
        </button>

        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Check Claim Threshold</span>
        </button>

        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Provider Eligibility Check</span>
        </button>

      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 1 — Members · Calculate Member Cost     -->
      <!-- ══════════════════════════════════════════════ -->
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
                <h3 class="font-bold text-gray-800">Calculate Member Cost</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Members</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">*, -, /</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Arithmetic</span>
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
                <p class="text-sm text-gray-600">This script uses <strong class="text-gray-800">arithmetic operators</strong> to split a medical bill between the plan and the member — multiplying to find the plan&apos;s share, then subtracting to find what the member owes. Update the three values at the top and Python recalculates the rest automatically.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">member_cost.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">member_id = &quot;M-10042&quot;           # the member&apos;s unique ID
total_bill = 250                  # total amount billed for the visit
plan_covers_pct = 0.80            # the plan covers 80% of the bill

plan_pays = total_bill * plan_covers_pct    # multiply to get the plan&apos;s share = 200.0
member_owes = total_bill - plan_pays        # subtract to find the member&apos;s share = 50.0

print(&quot;Member ID:&quot;, member_id)              # display the member&apos;s ID
print(&quot;Total bill: $&quot;, total_bill)          # display the full billed amount
print(&quot;Plan pays: $&quot;, plan_pays)            # display what the plan covers
print(&quot;Member owes: $&quot;, member_owes)        # display the member&apos;s out-of-pocket cost</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python member_cost.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Member ID: M-10042<br>Total bill: $ 250<br>Plan pays: $ 200.0<br>Member owes: $ 50.0</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Change the number stored in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">total_bill</code> or <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">plan_covers_pct</code> at the top and Python recalculates every line below it automatically — no manual arithmetic needed.</p>
            </div>

          </div>
        </div>
      </div><!-- /panel 1 -->

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 2 — Claims · Check Claim Threshold      -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Check Claim Threshold</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Claims</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">&gt;=, &gt;, ==</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">True / False</span>
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
                <p class="text-sm text-gray-600">This script applies <strong class="text-gray-800">comparison operators</strong> to a claim amount and produces a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">True</code> or <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">False</code> answer for each test — checking whether the claim meets the deductible, exceeds a review threshold, or matches an exact amount.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">claim_threshold.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">claim_id = &quot;CLM-88291&quot;              # unique reference number for this claim
claim_amount = 340.00               # total amount submitted on the claim
deductible = 500.00                 # member&apos;s remaining annual deductible

deductible_met = claim_amount &gt;= deductible    # True if claim meets or exceeds deductible
above_threshold = claim_amount &gt; 200           # True if claim is over the review threshold
exact_amount = claim_amount == 340.00          # True if billed amount is exactly 340.00

print(&quot;Claim ID:&quot;, claim_id)                   # display the claim reference
print(&quot;Deductible met:&quot;, deductible_met)       # False — 340 is less than 500
print(&quot;Above threshold:&quot;, above_threshold)     # True — 340 is greater than 200
print(&quot;Exact amount:&quot;, exact_amount)           # True — 340.00 equals 340.00</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python claim_threshold.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Claim ID: CLM-88291<br>Deductible met: False<br>Above threshold: True<br>Exact amount: True</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Every comparison always produces either <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">True</code> or <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">False</code> — these Boolean results are what power every <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">if</code> statement you will write in the lessons ahead.</p>
            </div>

          </div>
        </div>
      </div><!-- /panel 2 -->

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 3 — Providers · Provider Eligibility    -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Provider Eligibility Check</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Providers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">and, or, not</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">+=, -=</span>
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
                <p class="text-sm text-gray-600">This script uses <strong class="text-gray-800">assignment shorthand</strong> (<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">+=</code>, <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">-=</code>) to adjust a provider&apos;s billed amount, then applies <strong class="text-gray-800">logical operators</strong> (<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">and</code>, <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">or</code>, <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">not</code>) to decide whether the provider is eligible for payment and whether the claim needs flagging.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">provider_eligibility.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">provider_name = &quot;Dr. Sarah Kim&quot;       # the rendering provider&apos;s name
is_in_network = True                  # whether the provider is in the plan&apos;s network
npi_verified = True                   # whether the NPI number has been confirmed
billed_amount = 1200.00               # initial amount billed for services rendered

billed_amount += 150.00               # add a late submission fee — total becomes 1350.00
billed_amount -= 50.00                # apply a negotiated credit — total becomes 1300.00

can_be_paid = is_in_network and npi_verified          # both must be True to authorise payment
flagged = billed_amount &gt; 1000 or not npi_verified    # flag if high-cost or NPI unverified

print(&quot;Provider:&quot;, provider_name)                     # display provider name
print(&quot;Adjusted bill: $&quot;, billed_amount)              # display the final adjusted amount
print(&quot;Eligible for payment:&quot;, can_be_paid)           # True — both conditions are met
print(&quot;Flagged for review:&quot;, flagged)                 # True — adjusted bill exceeds 1000</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python provider_eligibility.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Provider: Dr. Sarah Kim<br>Adjusted bill: $ 1300.0<br>Eligible for payment: True<br>Flagged for review: True</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">and</code> requires every condition to be true, so it is the right choice when all criteria must be satisfied — such as confirming a provider is both in-network <em>and</em> verified before authorising a payment.</p>
            </div>

          </div>
        </div>
      </div><!-- /panel 3 -->

    </div>
'''


def main():
    with open(TARGET, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace only the body div of #code-examples, stopping before </section>
    pattern = (
        r'(<section id="code-examples">.*?'
        r'<div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">.*?'
        r'</div>\s*</div>\s*</div>\s*)'  # header + body wrapper close
        r'(\s*</div>\s*</section>)'
    )

    # Simpler: locate section start and next section start
    sec_pattern = r'(<section id="code-examples">.*?<div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">)(.*?)(\s*</div>\s*</section>\s*\n\s*<section id="comparison">)'

    m = re.search(sec_pattern, html, flags=re.DOTALL)
    if not m:
        print("❌ Pattern not found. Trying fallback...")
        # Fallback: match section outer wrapper
        start_marker = '<section id="code-examples">'
        end_marker = '<section id="comparison">'
        idx_start = html.find(start_marker)
        idx_end = html.find(end_marker)
        if idx_start == -1 or idx_end == -1:
            print("❌ Could not locate #code-examples or #comparison sections.")
            return

        old_section = html[idx_start:idx_end]

        # Now find the body div inside the old section — replace only the body
        body_start = old_section.find('<div class="bg-white px-8 py-7 space-y-6">')
        if body_start == -1:
            # Try without space-y-6
            body_start = old_section.find('<div class="bg-white px-8 py-7')
        if body_start == -1:
            print("❌ Could not locate the body div inside #code-examples.")
            return

        # The body ends with three closing tags: </div>\n  </div>\n</section>
        header_part = old_section[:body_start]
        # Find the section header close — everything up to and including the header div close
        new_section = header_part + NEW_BODY + '  </div>\n</section>\n\n'
        new_html = html[:idx_start] + new_section + html[idx_end:]

        with open(TARGET, "w", encoding="utf-8") as f:
            f.write(new_html)
        print("✅ #code-examples body replaced (fallback path).")
        print("   3 panels: Members (arithmetic) / Claims (comparison) / Providers (logical + assignment)")
        return

    # Primary path: use the regex match
    group1 = m.group(1)  # section opening + outer card div start
    group3 = m.group(3)  # closing tags + next section

    # Find the body div start inside group1+group2
    full_match_start = m.start()
    new_html = html[:full_match_start] + group1 + NEW_BODY + '  </div>\n</section>\n\n' + '<section id="comparison">' + html[m.end():]

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("✅ #code-examples body replaced (regex path).")
    print("   3 panels: Members (arithmetic) / Claims (comparison) / Providers (logical + assignment)")


if __name__ == "__main__":
    main()
