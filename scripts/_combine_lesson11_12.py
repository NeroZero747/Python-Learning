"""
Combine lesson11 (CASE Statements) + lesson12 (NULL Handling) into a single
lesson11_case_statements.html, then renumber & delete merged file.

Steps performed:
  1. Augment lesson11 with NULL-handling content:
       - Update hero <h1> + subtitle
       - Update Examples / Exercises count pills (4 -> 5)
       - Add 1 tab + panel to #key-concepts (NULL & COALESCE)
       - Add 1 tab + panel to #code-examples (NULL handling with COALESCE)
       - Add 1 tab + panel to #practice (Replace NULLs)
       - Add 1 tab + panel to #mistakes (= NULL fails)
       - Update #next-lesson preview block to point at Query Optimization
       - Fix bottom-nav 'Next' link
  2. Delete lesson12_null_handling.html
  3. Rename lesson13_query_optimization.html        -> lesson12_query_optimization.html
  4. Rename lesson14_sql_for_analytics_workflows.html -> lesson13_sql_for_analytics_workflows.html
  5. Bulk-update module TOC sidebar in lessons 8-13: merge "7. CASE" + "8. NULL"
     into "7. CASE Statements & NULL Handling", shift 9->8, 10->9
  6. Bulk-update prev/next nav links across affected lessons
"""
from pathlib import Path
import re
import sys

DIR = Path(r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations')

FILES_BEFORE = {
    'l10':  DIR / 'lesson10_advanced_joins.html',
    'l11':  DIR / 'lesson11_case_statements.html',
    'l12':  DIR / 'lesson12_null_handling.html',
    'l13':  DIR / 'lesson13_query_optimization.html',
    'l14':  DIR / 'lesson14_sql_for_analytics_workflows.html',
}

# ---------------------------------------------------------------------------
# Step 1 — Augment lesson11
# ---------------------------------------------------------------------------
target = FILES_BEFORE['l11']
content = target.read_text(encoding='utf-8')
orig = len(content)

# 1a. Hero title
content = content.replace(
    '<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">CASE Statements</h1>',
    '<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">CASE Statements &amp; NULL Handling</h1>',
    1,
)

# 1b. Hero stat pills: bump Examples 4->5 and Exercises 4->5
def bump_pill(html, anchor_href, new_count):
    pattern = re.compile(
        r'(<a href="' + re.escape(anchor_href) + r'" class="hero-pill[^"]*"[^>]*>'
        r'<span class="iconify[^"]*"[^>]*></span>'
        r'<span class="font-extrabold">)\d+(</span>)'
    )
    return pattern.sub(lambda m: f'{m.group(1)}{new_count}{m.group(2)}', html, count=1)

content = bump_pill(content, '#code-examples', 5)
content = bump_pill(content, '#practice', 5)

# 1c. Hero subtitle — find subtitle text and replace
sub_old_re = re.compile(
    r'(class="hero-pill[^"]*"[^>]*>[\s\S]*?Subtitle[\s\S]*?</span>)',
    re.IGNORECASE,
)
# Actually the subtitle is inside the hero block — find the <p> after the <h1>
subtitle_pattern = re.compile(
    r'(<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-\[1\.15\] tracking-tight">CASE Statements &amp; NULL Handling</h1>\s*)<p class="[^"]*">([\s\S]*?)</p>',
    re.MULTILINE,
)
m = subtitle_pattern.search(content)
if m:
    new_subtitle = '<p class="text-base md:text-lg text-white/85 mb-7 leading-relaxed max-w-2xl">Combine SQL\'s if/then logic with safe NULL handling so you can categorize, transform, and clean messy data inside a single query \u2014 the foundation of every reporting layer.</p>'
    content = subtitle_pattern.sub(lambda mm: mm.group(1) + new_subtitle, content, count=1)

# 1d. Add NULL & COALESCE tab to #key-concepts (kc-tab index 4)
KC_NEW_BUTTON = '''<button onclick="switchKcTab(4)" class="kc-tab  group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:circle-question"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">NULL &amp; COALESCE</span>
</button>
'''

# Insert KC button right before the closing </div> of the tab-list column
kc_anchor = '''<button onclick="switchKcTab(3)" class="kc-tab  group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:cube"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Using CASE in Aggregations</span>
</button>
'''
if kc_anchor not in content:
    raise RuntimeError("KC anchor not found")
content = content.replace(kc_anchor, kc_anchor + KC_NEW_BUTTON, 1)

# 1e. KC panel — insert just before the section closes. We need a panel for tab 4.
KC_NEW_PANEL = '''<div class="kc-panel kc-panel-anim hidden" data-color="pink" role="tabpanel">
  <div class="rounded-2xl border border-pink-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
    <div class="bg-gradient-to-br from-pink-50/60 to-white p-5">
      <div class="mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">NULL &amp; COALESCE</h3>
        <span class="text-[10px] font-bold text-#CB187D uppercase tracking-widest">Definition</span>
      </div>
      <div class="space-y-3 mb-4">
        <p class="text-xs text-gray-600 leading-relaxed"><code class="text-[11px] font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">NULL</code> means &quot;unknown&quot; \u2014 it is not zero and not an empty string. Two NULLs are <strong>not</strong> equal to each other, so <code class="text-[11px] font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">x = NULL</code> never matches; you must use <code class="text-[11px] font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">IS NULL</code>.</p>
        <p class="text-xs text-gray-600 leading-relaxed"><code class="text-[11px] font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COALESCE(a, b, c)</code> returns the first non-NULL argument \u2014 perfect for substituting a default when a column is missing.</p>
      </div>
      <div class="space-y-3">
        <div class="rounded-xl overflow-hidden bg-code shadow-md">
          <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
            <div class="flex items-center gap-2">
              <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
              <span class="text-[11px] font-semibold text-gray-400">SQL</span>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <pre class="overflow-x-auto pre-reset"><code class="language-sql">-- IS NULL is the only way to test for NULL
SELECT name FROM customers WHERE phone IS NULL;

-- COALESCE returns the first non-NULL value
SELECT COALESCE(nickname, first_name, 'Friend') AS display_name
FROM users;</code></pre>
        </div>
      </div>
    </div>
  </div>
</div>
'''

# Insert KC panel: place right before the closing </div></div></section> of #key-concepts
kc_section_close_re = re.compile(
    r'(<section id="key-concepts">[\s\S]*?)(\n\s*</div>\s*</div>\s*</div>\s*</section>)',
    re.MULTILINE,
)
m = kc_section_close_re.search(content)
if not m:
    raise RuntimeError("KC section close not found")
# Find the LAST kc-panel block (current panel index 3) and append after it.
kc_section_text = m.group(1)
# Append our new panel right after the last </div> that closes the previous panel
# Easiest: insert just before the final closing pattern.
content = content[:m.end(1)] + '\n' + KC_NEW_PANEL + content[m.end(1):]

# 1f. Add Code Examples tab + panel
CE_TAB_NEW = '''<button onclick="switchCeTab(4)" class="ce-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
  <span class="ce-step-label text-xs font-bold">NULL Handling</span>
</button>
'''

ce_tab3_anchor_re = re.compile(
    r'(<button onclick="switchCeTab\(3\)" class="ce-step[^"]*"[^>]*>\s*<span class="iconify[^"]*"[^>]*></span>\s*<span class="ce-step-label[^"]*">[^<]+</span>\s*</button>)',
)
m = ce_tab3_anchor_re.search(content)
if not m:
    raise RuntimeError("CE tab(3) anchor not found")
content = content[:m.end()] + '\n' + CE_TAB_NEW + content[m.end():]

CE_PANEL_NEW = '''      <!-- Panel 5 - NULL Handling - hidden -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Replacing NULL with COALESCE</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Customers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">COALESCE</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">NULLIF</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">Reports look unprofessional when they show empty cells. <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">COALESCE</code> swaps a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">NULL</code> for a default value, and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">NULLIF</code> turns an unwanted value (like 0) into a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">NULL</code> so it does not skew averages.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">null_handling.sql</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT
    name,
    COALESCE(phone,    'No phone on file') AS phone,    -- swap NULL for default
    COALESCE(country,  'Unknown')          AS country,  -- safer reports
    NULLIF(discount, 0)                    AS discount  -- turn 0 into NULL
FROM customers;</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ psql -f null_handling.sql</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Alice | 555-1234        | USA     | NULL<br>Bob   | No phone on file | Unknown | 0.10</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">NULLIF</code> to protect against divide-by-zero: <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">total / NULLIF(quantity, 0)</code> returns NULL instead of throwing an error.</p>
            </div>
          </div>
        </div>
      </div>

    </div>'''

# Insert CE panel before the </div> that closes the panel-list inside #code-examples
# Find the end of #code-examples section content area, after the last existing panel
ce_section_re = re.compile(
    r'(<section id="code-examples">[\s\S]*?)(\n\s*</div>\s*</div>\s*</section>)',
)
m = ce_section_re.search(content)
if not m:
    raise RuntimeError("#code-examples section close not found")
# The panels live in a wrapper div. Look for the LAST </div> that closes the panel wrapper.
# Strategy: find the second-to-last </div> directly before </section> closes.
# Simpler: replace the </div>\n  </div>\n</section> footer pattern by injecting our panel.
# We'll insert just before the last `    </div>\n  </div>\n</section>` pattern in the section.
ce_section_full = m.group(1) + m.group(2)
# Find the last `</div>` that occurs in this section and insert before it.
# Use the inner closing pattern of the panel wrapper:
insertion_point = m.end(1)  # right at the start of the closing block
# Insert with proper indentation
content = content[:insertion_point] + '\n' + CE_PANEL_NEW + content[insertion_point:]

# 1g. Practice tab + panel
PE_TAB_NEW = '''<button onclick="switchPeTab(4)" class="pe-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
  <span class="pe-step-label text-xs font-bold">Replace NULL Phones</span>
</button>
'''

pe_tab3_re = re.compile(
    r'(<button onclick="switchPeTab\(3\)" class="pe-step[^"]*"[^>]*>\s*<span class="iconify[^"]*"[^>]*></span>\s*<span class="pe-step-label[^"]*">[^<]+</span>\s*</button>)',
)
m = pe_tab3_re.search(content)
if not m:
    raise RuntimeError("PE tab(3) anchor not found")
content = content[:m.end()] + '\n' + PE_TAB_NEW + content[m.end():]

PE_PANEL_NEW = '''      <!-- Panel 5 - Replace NULL Phones - hidden -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Replace NULL Phones</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Customers</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">COALESCE</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">The marketing team is exporting a customer list and does not want any blank phone-number cells. Write a query that returns every customer&apos;s name and phone number, but replace any <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">NULL</code> phone with the literal text <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">No phone on file</code>.</p>
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
                      <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:database" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">replace_null_phones.sql</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">SELECT
    name,
    COALESCE(phone, 'No phone on file') AS phone   -- swap NULL for default
FROM customers;</code></pre>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">For numeric columns, choose your default carefully \u2014 substituting <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">0</code> for a missing salary will pull the team average down.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>'''

pe_section_re = re.compile(
    r'(<section id="practice">[\s\S]*?)(\n\s*</div>\s*</div>\s*</section>)',
)
m = pe_section_re.search(content)
if not m:
    raise RuntimeError("#practice section close not found")
content = content[:m.end(1)] + '\n' + PE_PANEL_NEW + content[m.end(1):]

# 1h. Mistakes tab + panel — find max existing index
mk_indices = [int(x) for x in re.findall(r'switchMkTab\((\d+)\)', content)]
next_mk = max(mk_indices) + 1 if mk_indices else 0

MK_TAB_NEW = f'''<button onclick="switchMkTab({next_mk})" class="mk-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
  <span class="mk-step-label text-xs font-bold">= NULL Never Matches</span>
</button>
'''

mk_last_re = re.compile(
    r'(<button onclick="switchMkTab\(' + str(next_mk - 1) + r'\) class="mk-step[^"]*"[^>]*>\s*<span class="iconify[^"]*"[^>]*></span>\s*<span class="mk-step-label[^"]*">[^<]+</span>\s*</button>)',
)
# More tolerant pattern (the class might or might not have an extra space after mk-step):
mk_last_re = re.compile(
    r'(<button onclick="switchMkTab\(' + str(next_mk - 1) + r'\)"[^>]*>\s*<span class="iconify[^"]*"[^>]*></span>\s*<span class="mk-step-label[^"]*">[^<]+</span>\s*</button>)',
)
m = mk_last_re.search(content)
if not m:
    raise RuntimeError(f"MK tab({next_mk - 1}) anchor not found")
content = content[:m.end()] + '\n' + MK_TAB_NEW + content[m.end():]

MK_PANEL_NEW = '''      <!-- Mistake N - = NULL never matches - hidden -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">= NULL Never Matches \u2014 Use IS NULL</h4>
              <p class="text-xs text-gray-500 mt-0.5">SQL treats NULL as &quot;unknown&quot;, so any comparison with = silently returns no rows.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">In SQL, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">NULL</code> is not a value but the absence of a value. Comparing anything to NULL with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">=</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">!=</code> returns NULL (not TRUE), so the row is dropped from the result. Always use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">IS NULL</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">IS NOT NULL</code>.</p>
          </div>
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &#8212; returns 0 rows
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT name
FROM customers
WHERE phone = NULL;
-- always returns 0 rows
-- silently incorrect</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &#8212; use IS NULL
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT name
FROM customers
WHERE phone IS NULL;
-- returns every customer
-- with a missing phone</code></pre>
              </div>
            </div>
          </div>
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Same trap with <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">!= NULL</code> \u2014 use <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">IS NOT NULL</code>. When in doubt, ask: &quot;is the value missing?&quot; If yes, reach for IS / IS NOT.</p>
          </div>
        </div>
      </div>

    </div>'''

mk_section_re = re.compile(
    r'(<section id="mistakes">[\s\S]*?)(\n\s*</div>\s*</div>\s*</section>)',
)
m = mk_section_re.search(content)
if not m:
    raise RuntimeError("#mistakes section close not found")
content = content[:m.end(1)] + '\n' + MK_PANEL_NEW + content[m.end(1):]

# 1i. Update next-lesson preview block — was probably "NULL Handling", now "Query Optimization"
# Search broadly for next-lesson section content; safest: find the lesson title line.
content = re.sub(
    r'(<h3 class="text-base font-bold text-gray-800">)[^<]*NULL[^<]*(</h3>)',
    r'\g<1>Query Optimization\g<2>',
    content,
    count=1,
)
content = re.sub(
    r'(Module \d+ &middot; Lesson )\d+',
    lambda m: m.group(1) + '12',
    content,
    count=1,  # only the next-lesson badge label
)
# Also try plain · separator
content = re.sub(
    r'(Module \d+ \xb7 Lesson )\d+',
    lambda m: m.group(1) + '12',
    content,
    count=1,
)

# Replace lesson number badge (the big "12" block in next-lesson)
content = re.sub(
    r'(<span class="text-white font-bold text-lg">)\d+(</span>)',
    r'\g<1>12\g<2>',
    content,
    count=1,
)

# 1j. Update bottom nav next link in lesson11
content = content.replace(
    'href="lesson12_null_handling.html"',
    'href="lesson12_query_optimization.html"',
)
# Update the visible "Next" lesson title text in bottom nav (was "NULL Handling")
content = re.sub(
    r'(class="text-sm font-bold text-gray-700 group-hover:text-\[#CB187D\] transition-colors truncate">)NULL Handling(</p>)',
    r'\g<1>Query Optimization\g<2>',
    content,
)

target.write_text(content, encoding='utf-8')
print(f"[OK] Augmented lesson11_case_statements.html  ({orig} -> {len(target.read_text(encoding='utf-8'))} bytes)")

# ---------------------------------------------------------------------------
# Step 2-4 — Delete + rename files
# ---------------------------------------------------------------------------
# Delete lesson12_null_handling.html
if FILES_BEFORE['l12'].exists():
    FILES_BEFORE['l12'].unlink()
    print(f"[OK] Deleted {FILES_BEFORE['l12'].name}")

new_l12 = DIR / 'lesson12_query_optimization.html'
new_l13 = DIR / 'lesson13_sql_for_analytics_workflows.html'

if FILES_BEFORE['l13'].exists():
    FILES_BEFORE['l13'].rename(new_l12)
    print(f"[OK] Renamed lesson13_query_optimization.html -> {new_l12.name}")

if FILES_BEFORE['l14'].exists():
    FILES_BEFORE['l14'].rename(new_l13)
    print(f"[OK] Renamed lesson14_sql_for_analytics_workflows.html -> {new_l13.name}")

# ---------------------------------------------------------------------------
# Step 5 — Bulk update module TOC sidebars + nav links
# ---------------------------------------------------------------------------
# Process every lesson file currently in the directory
for f in sorted(DIR.glob('lesson*.html')):
    text = f.read_text(encoding='utf-8')
    before = text

    # 5a. Update module TOC sidebar entries (lessons 8-13 use the 1-10 numbering)
    # Merge "7. CASE Statements" + "8. NULL Handling" into "7. CASE Statements & NULL Handling"
    # and shift "9. Query Optimization" -> "8.", "10. SQL for Analytics Workflows" -> "9."

    # Replace the entire block of 4 entries (7,8,9,10) with the new 3 entries
    old_block_re = re.compile(
        r'<a href="lesson07_case_statements\.html"[\s\S]*?<span class="truncate">7\. CASE Statements</span>\s*</a>\s*'
        r'<a href="lesson08_null_handling\.html"[\s\S]*?<span class="truncate">8\. NULL Handling</span>\s*</a>\s*'
        r'<a href="lesson09_query_optimization\.html"[\s\S]*?<span class="truncate">9\. Query Optimization</span>\s*</a>\s*'
        r'<a href="lesson10_sql_for_analytics_workflows\.html"[\s\S]*?<span class="truncate">10\. SQL for Analytics Workflows</span>\s*</a>'
    )
    new_block = (
        '<a href="lesson11_case_statements.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
        '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
        '  <span class="truncate">7. CASE Statements &amp; NULL Handling</span>\n'
        '</a>\n'
        '<a href="lesson12_query_optimization.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
        '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
        '  <span class="truncate">8. Query Optimization</span>\n'
        '</a>\n'
        '<a href="lesson13_sql_for_analytics_workflows.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
        '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
        '  <span class="truncate">9. SQL for Analytics Workflows</span>\n'
        '</a>'
    )
    text = old_block_re.sub(new_block, text)

    # 5b. Update bottom-nav prev/next file references
    text = text.replace(
        'href="lesson12_null_handling.html"',
        'href="lesson12_query_optimization.html"',
    )
    text = text.replace(
        'href="lesson13_query_optimization.html"',
        'href="lesson12_query_optimization.html"',
    )
    text = text.replace(
        'href="lesson14_sql_for_analytics_workflows.html"',
        'href="lesson13_sql_for_analytics_workflows.html"',
    )

    # 5c. Bottom-nav visible "NULL Handling" label -> "Query Optimization"
    text = re.sub(
        r'(class="text-sm font-bold text-gray-700 group-hover:text-\[#CB187D\] transition-colors truncate">)NULL Handling(</p>)',
        r'\g<1>Query Optimization\g<2>',
        text,
    )

    if text != before:
        f.write_text(text, encoding='utf-8')
        print(f"[OK] Updated TOC/nav in {f.name}")

# ---------------------------------------------------------------------------
# 6. Mark current lesson active in module TOC sidebar (each lesson should highlight itself)
# ---------------------------------------------------------------------------
ACTIVE_CLASS = 'bg-[#fdf0f7] border-[#CB187D] text-[#CB187D]'
INACTIVE_CLASS = 'bg-white border-gray-100 text-gray-600 hover:border-gray-200'
ACTIVE_DOT = 'bg-[#CB187D]'
INACTIVE_DOT = 'bg-gray-300'

for f in sorted(DIR.glob('lesson*.html')):
    text = f.read_text(encoding='utf-8')
    before = text
    own_filename = f.name
    # First reset all entries to inactive
    text = text.replace(ACTIVE_CLASS, INACTIVE_CLASS)
    text = re.sub(
        r'(<a href="lesson\d+[^"]*\.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border )' + re.escape(INACTIVE_CLASS) + r'(" [^>]*>\s*<span class="w-2 h-2 rounded-full )' + re.escape(ACTIVE_DOT),
        r'\g<1>' + INACTIVE_CLASS + r'\g<2>' + INACTIVE_DOT,
        text,
    )
    # Then mark THIS lesson's <a> as active
    pattern = re.compile(
        r'(<a href="' + re.escape(own_filename) + r'" class="flex items-center gap-2 px-3 py-2 rounded-lg border )' +
        re.escape(INACTIVE_CLASS) +
        r'(" [^>]*>\s*<span class="w-2 h-2 rounded-full )' +
        re.escape(INACTIVE_DOT),
    )
    text2 = pattern.sub(
        r'\g<1>' + ACTIVE_CLASS + r'\g<2>' + ACTIVE_DOT,
        text,
    )
    if text2 != before:
        f.write_text(text2, encoding='utf-8')

print("\n[DONE] Lesson 11 + 12 combined; lessons 13->12, 14->13. TOCs updated.")

# Final listing
print("\nFinal directory contents:")
for p in sorted(DIR.glob('lesson*.html')):
    print(f"  {p.name}")
