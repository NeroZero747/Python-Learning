#!/usr/bin/env python3
"""Replace the three placeholder code-example panels in lesson02 with healthcare examples."""

filepath = "pages/track_01/mod_02_programming_foundations/lesson02_variables_data_types.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Old block: from panel 1 open tag through end of panels (before closing body div + </section>)
OLD_START = '      <div class="ce-panel ce-panel-anim " role="tabpanel">'
OLD_END   = '\n    </div>\n  </div>\n</section>\n\n<section id="comparison">'

si = content.find(OLD_START)
ei = content.find(OLD_END, si)

if si == -1 or ei == -1:
    print(f"ERROR: markers not found (si={si}, ei={ei})")
    exit(1)

NEW_PANELS = '''\
      <!-- Panel 1: Member Profile -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Member Profile</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Members</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">str, int, float, bool</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">print()</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">When a member calls the helpline, the service representative&apos;s screen populates with key details pulled from the system. This script creates four <strong class="text-gray-800">variables</strong> &mdash; one for each of the four core data types &mdash; and prints them to the console, exactly as a script would do before displaying them on screen. Notice that Python preserves the exact type of each value: the name stays text, the ID stays a whole number, the premium stays a decimal, and the enrolment status stays a true/false flag.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">member_profile.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">member_name  = &quot;Alice Carter&quot;  # str  &mdash; the member&apos;s full name
member_id    = 100452           # int  &mdash; a whole-number identifier
plan_premium = 312.75           # float &mdash; monthly premium with cents
is_active    = True             # bool &mdash; whether enrolment is current

print(member_name)   # displays the name exactly as stored
print(member_id)     # displays the integer ID
print(plan_premium)  # displays the decimal premium amount
print(is_active)     # displays True or False</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python member_profile.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Alice Carter<br>100452<br>312.75<br>True</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Every field on a member record in a health plan system is stored as a specific data type &mdash; names and plan codes as strings, IDs and ages as integers, premium amounts as floats, and eligibility flags as booleans. Getting the type right at the point of storage makes every downstream calculation and comparison reliable.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 2: Claim Cost Split -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Claim Cost Split</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Claims</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">float arithmetic</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">derived variable</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">When a claim arrives, the adjudication system must calculate how much of the billed amount the member owes and how much the plan covers. This script stores the claim amount and the member&apos;s remaining <strong class="text-gray-800">deductible</strong> as <strong class="text-gray-800">float</strong> variables, then creates a third variable by subtracting one from the other &mdash; demonstrating that variables can hold the result of a <strong class="text-gray-800">calculation</strong>, not just a fixed value. Notice how the two derived variables are computed from the first two, so changing a single number at the top automatically updates the entire cost split.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">claim_cost_split.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">claim_amount         = 850.00  # total billed for the procedure
deductible_remaining = 200.00  # amount still owed on the member&apos;s deductible

member_owes = deductible_remaining        # member pays the deductible balance first
plan_covers = claim_amount - member_owes  # plan pays everything above the deductible

print(&quot;Total claim:&quot;, claim_amount)  # show the full billed amount
print(&quot;Member owes:&quot;, member_owes)    # show the member&apos;s share
print(&quot;Plan covers:&quot;, plan_covers)    # show the plan&apos;s share</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python claim_cost_split.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Total claim: 850.0<br>Member owes: 200.0<br>Plan covers: 650.0</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">A claims analyst could update the two input variables at the top of this script for any incoming claim and immediately see the correct cost split &mdash; no spreadsheet formula required. Storing calculated results in named variables also makes the intention of each number obvious to anyone reading the script later.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Panel 3: Provider Billing Check -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Provider Billing Check</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Providers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">type()</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">data validation</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">Before a provider payment is processed, a validation step confirms that each field in the provider record holds the correct data type &mdash; a name should be a string, a billed amount should be a float, and an NPI should be an integer. This script stores four provider fields spanning all four types, prints a summary, and then uses Python&apos;s built-in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">type()</code> function to confirm the type of the two most critical fields before any payment logic runs. Notice that <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">type()</code> always returns the class name wrapped in angle brackets.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">provider_billing_check.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">provider_name  = &quot;Dr. Maria Santos&quot;  # str  &mdash; provider&apos;s full name
provider_npi   = 1234567890           # int  &mdash; national provider identifier
billed_amount  = 1250.00              # float &mdash; total amount submitted for payment
in_network     = True                 # bool &mdash; whether the provider is contracted

print(provider_name, &quot;|&quot;, provider_npi)   # show the provider&apos;s identity
print(&quot;Billed:&quot;, billed_amount)            # show the amount to be paid
print(&quot;In-network:&quot;, in_network)           # show the network status

print(type(provider_name))   # confirm the name is stored as a string
print(type(billed_amount))   # confirm the amount is stored as a float</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python provider_billing_check.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Dr. Maria Santos | 1234567890<br>Billed: 1250.0<br>In-network: True<br>&lt;class &apos;str&apos;&gt;<br>&lt;class &apos;float&apos;&gt;</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">If <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">type(billed_amount)</code> returned <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">&lt;class &apos;str&apos;&gt;</code> instead of <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">&lt;class &apos;float&apos;&gt;</code>, any arithmetic on that field &mdash; such as summing all claims for the provider &mdash; would raise a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">TypeError</code>. Checking types early prevents payment errors that are difficult to trace once data has moved through multiple processing steps.</p>
            </div>
          </div>
        </div>
      </div>'''

new_content = content[:si] + NEW_PANELS + content[ei:]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

# Verify
with open(filepath, "r", encoding="utf-8") as f:
    verify = f.read()

checks = [
    ("member_profile.py", "member_profile.py" in verify),
    ("claim_cost_split.py", "claim_cost_split.py" in verify),
    ("provider_billing_check.py", "provider_billing_check.py" in verify),
    ("Example 1 -- Creating", "Example 1 &mdash; Creating" not in verify and "Example 1 — Creating" not in verify),
    ("traffic-light dots gone", "bg-red-400/80" not in verify),
]

for label, ok in checks:
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
