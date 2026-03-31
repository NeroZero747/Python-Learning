#!/usr/bin/env python3
"""Replace #mistakes section body in lesson04_lists_dictionaries.html."""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ── Locate section boundaries ─────────────────────────────────────────────────
SEC_START = 'id="mistakes"'
NEXT_SEC  = 'id="real-world"'

sec_idx  = content.index(SEC_START)
next_idx = content.index(NEXT_SEC, sec_idx)

BODY_OPEN  = '    <div class="bg-white px-8 py-7 space-y-6">'
body_start = content.index(BODY_OPEN, sec_idx)
body_end   = content.rindex('  </div>\n</section>', sec_idx, next_idx)

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Parentheses vs Brackets</span>
        </button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Off-by-One Index</span>
        </button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Missing Key Error</span>
        </button>
      </div>

      <!-- Mistake 1 — Parentheses vs Brackets -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Using Parentheses Instead of Square Brackets Creates a Tuple, Not a List</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python uses <code class="font-mono">( )</code> for tuples and <code class="font-mono">[ ]</code> for lists — they behave differently and are not interchangeable.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">enrolled_members = ("Alice", "Carlos")</code> creates a tuple — a permanently sealed sequence you cannot add to or change later. Use square brackets <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">[ ]</code> to create a list that can grow as new members enrol.</p>
          </div>

          <!-- Split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — parentheses → creates a tuple
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">enrolled_members = (&quot;Alice Nguyen&quot;, &quot;Carlos Rivera&quot;)
# this is a tuple, not a list — items cannot be added later</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — square brackets → creates a list
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">enrolled_members = [&quot;Alice Nguyen&quot;, &quot;Carlos Rivera&quot;]
# square brackets create a list — members can be added later</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of square brackets as an open binder that you can add pages to — parentheses make a sealed envelope. A member roster needs to grow as people enrol, so always use a list <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">[ ]</code> unless you have a specific reason to use an immutable tuple.</p>
          </div>

        </div>
      </div>

      <!-- Mistake 2 — Off-by-One Index -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Using Index 1 to Read the First Item Returns the Second Item Instead</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python counts list positions starting at 0, so the first item is always at <code class="font-mono">[0]</code>, not <code class="font-mono">[1]</code>.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">enrolled_members[1]</code> to get the first member silently returns the <em>second</em> member — Python's zero-based indexing means the first item lives at position <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">[0]</code>. Always use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">[0]</code> for the first item and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">[-1]</code> for the last.</p>
          </div>

          <!-- Split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — index 1 returns the second item
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">enrolled_members = [&quot;Alice Nguyen&quot;, &quot;Carlos Rivera&quot;, &quot;Maria Santos&quot;]
print(enrolled_members[1])
# prints &quot;Carlos Rivera&quot;, not &quot;Alice Nguyen&quot;</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — index 0 returns the first item
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">enrolled_members = [&quot;Alice Nguyen&quot;, &quot;Carlos Rivera&quot;, &quot;Maria Santos&quot;]
print(enrolled_members[0])  # index 0 → first member: &quot;Alice Nguyen&quot;
print(enrolled_members[-1]) # index -1 → last member: &quot;Maria Santos&quot;</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">A useful mental model: each item's index equals the number of items <em>before</em> it — Alice has zero items before her, so she sits at <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">[0]</code>. This is also how Python reads the first row of a SQL result set, so getting comfortable with zero-based counting pays off immediately.</p>
          </div>

        </div>
      </div>

      <!-- Mistake 3 — Missing Key Error -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Accessing a Dictionary Key That Doesn't Exist Raises a KeyError</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python stops immediately with <code class="font-mono">KeyError</code> if the key is not in the dictionary — it does not return <code class="font-mono">None</code> by default.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">provider["email"]</code> when <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"email"</code> is not a key raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">KeyError: 'email'</code> and stops the program. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">provider.get("email")</code> to return <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">None</code> safely when the key is absent, or pass a default value as the second argument: <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">provider.get("email", "Not on file")</code>.</p>
          </div>

          <!-- Split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — key not found → KeyError
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">provider = {&quot;name&quot;: &quot;Dr. Lee&quot;, &quot;specialty&quot;: &quot;Cardiology&quot;}
print(provider[&quot;email&quot;])
# KeyError: &apos;email&apos; — program crashes</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — use .get() → returns None safely
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">provider = {&quot;name&quot;: &quot;Dr. Lee&quot;, &quot;specialty&quot;: &quot;Cardiology&quot;}
print(provider.get(&quot;email&quot;))                  # returns None — no crash
print(provider.get(&quot;email&quot;, &quot;Not on file&quot;))  # returns &quot;Not on file&quot;</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">In healthcare data, not every provider record has every field — a provider may have a phone number but no fax number on file. Using <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">.get()</code> keeps your script running even when a field is missing, which is essential when processing real-world records that arrive with gaps.</p>
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

sec_idx  = result.index('id="mistakes"')
next_idx = result.index('id="real-world"', sec_idx)
section  = result[sec_idx:next_idx]

checks = [
    ("3 mk-step pills",                     section.count('class="mk-step') == 3),
    ("No 'Mistake N' labels",               "Mistake 1" not in section and "Mistake 2" not in section),
    ("Tab 1 — Parentheses vs Brackets",     "Parentheses vs Brackets" in section),
    ("Tab 2 — Off-by-One Index",            "Off-by-One Index" in section),
    ("Tab 3 — Missing Key Error",           "Missing Key Error" in section),
    ("3 mk-panels",                         section.count('class="mk-panel') == 3),
    ("Panel 1 active (no hidden)",          'mk-panel mk-panel-anim"' in section or 'mk-panel mk-panel-anim" role' in section),
    ("Panels 2+3 hidden",                   section.count('mk-panel mk-panel-anim hidden') == 2),
    ("3 mistake-card divs",                 section.count('class="mistake-card') == 3),
    ("3 card headers (bug icon)",           section.count('fa6-solid:bug') >= 6),  # 3 in tabs + 3 in cards
    ("Explanation paras (x3)",              section.count('<div class="px-6 py-5">') == 3),
    ("3 split panels (red/green)",          section.count('bg-red-50/30') == 3),
    ("3 green panels",                      section.count('bg-emerald-50/30') == 3),
    ("3 arrow dividers",                    section.count('fa6-solid:arrow-right') == 3),
    ("3 amber tip footers",                 section.count('bg-amber-50/40') == 3),
    ("No 'Mistake N' in any label",         "Mistake 1" not in section),
    ("enrolled_members in wrong code 1",    "enrolled_members" in section),
    ("provider dict in wrong code 3",       'provider = {' in section),
    ("KeyError reference",                  "KeyError" in section),
    ("get() reference",                     ".get(" in section),
    ("Off-by-one: index 0 vs 1",            "enrolled_members[0]" in section and "enrolled_members[1]" in section),
    ("real-world section intact",           'id="real-world"' in result),
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
