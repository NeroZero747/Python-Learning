"""Merge lesson09 (CTEs) into lesson08 (Subqueries) and renumber/rename lessons 10-17 -> 9-16."""

import os
import re

DIR = 'pages/mod_06a_sql_foundation/mod_05_sql_foundations'
L08 = os.path.join(DIR, 'lesson08_subqueries.html')
L09_OLD = os.path.join(DIR, 'lesson09_common_table_expressions_ctes.html')
L07 = os.path.join(DIR, 'lesson07_joining_tables_join.html')

# ─── PART 1: Build the new CTE section ────────────────────────────────────────
CTE_SECTION = '''
<!-- ─── Common Table Expressions (CTEs) — merged from former lesson 09 ─── -->
<section id="ctes" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:layer-group"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Table Expressions (CTEs)</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A cleaner way to write subqueries — name the temporary result and reuse it.</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Hook -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">CTE</span>
        <div class="relative flex items-start gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">A <strong>Common Table Expression</strong> is a named, temporary result set defined with <code class="bg-pink-100 border border-pink-200 text-[#CB187D] px-1 rounded font-mono text-[12px]">WITH</code> that you can reference later in the query — like a subquery you give a name and read top-to-bottom.</p>
        </div>
      </div>

      <!-- 3-card grid: Basic | Multiple | vs Subquery -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">

        <!-- Basic CTE -->
        <div class="rounded-2xl border border-pink-100 overflow-hidden bg-white shadow-sm">
          <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
          <div class="p-5 space-y-3 bg-gradient-to-br from-pink-50/40 to-white">
            <div class="flex items-center gap-2.5">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                <span class="iconify text-white text-xs" data-icon="fa6-solid:code"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Basic CTE Structure</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">Every CTE starts with <code class="bg-pink-100 border border-pink-200 text-[#CB187D] px-1 rounded font-mono text-[11px]">WITH</code>, names the temporary result, defines the inner query in parentheses, and then runs the outer query against that name.</p>
            <div class="rounded-xl overflow-hidden bg-code shadow-md">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                  <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto pre-reset"><code class="language-sql">WITH cte_name AS (   -- name the temporary result
    SELECT columns   -- inner query
    FROM table
)
SELECT *             -- outer query reads the CTE
FROM cte_name;</code></pre>
            </div>
          </div>
        </div>

        <!-- Multiple CTEs -->
        <div class="rounded-2xl border border-violet-100 overflow-hidden bg-white shadow-sm">
          <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
          <div class="p-5 space-y-3 bg-gradient-to-br from-violet-50/40 to-white">
            <div class="flex items-center gap-2.5">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                <span class="iconify text-white text-xs" data-icon="fa6-solid:file-code"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Multiple CTEs</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">Chain several CTEs by separating them with commas. Each step builds on the previous one, so complex logic reads as a clear top-to-bottom story.</p>
            <div class="rounded-xl overflow-hidden bg-code shadow-md">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                  <span class="text-[11px] font-semibold text-gray-400">SQL</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto pre-reset"><code class="language-sql">WITH sales_by_region AS (        -- Step 1
    SELECT region, SUM(revenue) AS revenue
    FROM sales
    GROUP BY region
),
high_performing AS (             -- Step 2 (uses Step 1)
    SELECT *
    FROM sales_by_region
    WHERE revenue &gt; 10000
)
SELECT *                         -- Step 3 (final)
FROM high_performing;</code></pre>
            </div>
          </div>
        </div>

        <!-- CTE vs Subquery -->
        <div class="rounded-2xl border border-blue-100 overflow-hidden bg-white shadow-sm">
          <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
          <div class="p-5 space-y-3 bg-gradient-to-br from-blue-50/40 to-white">
            <div class="flex items-center gap-2.5">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                <span class="iconify text-white text-xs" data-icon="fa6-solid:puzzle-piece"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">CTE vs Subquery</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">Both produce the same result. CTEs are usually easier to read because each step has a name and the logic flows top-to-bottom instead of inside-out.</p>
            <div class="rounded-xl overflow-hidden bg-code shadow-md">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-gray-400" data-icon="fa6-solid:database" data-width="14" data-height="14"></span>
                  <span class="text-[11px] font-semibold text-gray-400">SQL &mdash; CTE</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto pre-reset"><code class="language-sql">WITH regional_sales AS (
    SELECT region, SUM(revenue) AS revenue
    FROM sales
    GROUP BY region
)
SELECT *
FROM regional_sales;</code></pre>
            </div>
          </div>
        </div>

      </div>

      <!-- Closing tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Reach for a <strong>CTE</strong> when your logic has multiple stages or when a subquery would be repeated. Reach for a <strong>subquery</strong> when the inner query is short and used once.</p>
      </div>

    </div>
  </div>
</section>
'''


# ─── PART 2: Update lesson08 (combine + renumber outgoing) ────────────────────
print("─── PART 2: Updating lesson08 ───")
with open(L08, 'r', encoding='utf-8') as f:
    l08 = f.read()

# 2a. Title in <h1>
l08 = l08.replace(
    '<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">Subqueries</h1>',
    '<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">Subqueries and CTEs</h1>'
)

# 2b. Progress pill: "1/10" → "1/9"
l08 = re.sub(
    r'<span class="font-extrabold">1<span class="font-bold opacity-50">/10</span></span>',
    '<span class="font-extrabold">1<span class="font-bold opacity-50">/9</span></span>',
    l08
)

# 2c. Add "CTEs" entry to in-page TOC sidebar (insert after Key Concepts entry)
toc_old = '''<a href="#key-concepts" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:book-open"></span> Key Concepts
</a>'''
toc_new = toc_old + '''
<a href="#ctes" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:layer-group"></span> CTEs
</a>'''
if toc_old in l08:
    l08 = l08.replace(toc_old, toc_new, 1)
    print("  ✅ TOC entry added for CTEs")
else:
    print("  ⚠️  TOC entry pattern not found")

# 2d. Insert CTE section right before #code-examples
ce_marker = '<section id="code-examples">'
idx = l08.find(ce_marker)
if idx == -1:
    print("  ❌ Could not find #code-examples marker")
else:
    l08 = l08[:idx] + CTE_SECTION + '\n' + l08[idx:]
    print("  ✅ CTE section inserted before #code-examples")

# 2e. Fix next-lesson preview: "Common Table Expressions (CTEs)" → "Window Functions (PARTITION BY)"
# Replace title in next-lesson preview
l08 = l08.replace(
    '<h3 class="text-base font-bold text-gray-800">Common Table Expressions (CTEs)</h3>',
    '<h3 class="text-base font-bold text-gray-800">Window Functions (PARTITION BY)</h3>'
)
# Replace preview card 1 title
l08 = l08.replace(
    '<p class="text-sm font-semibold text-gray-700">Common Table Expressions (CTEs)</p>',
    '<p class="text-sm font-semibold text-gray-700">Window Functions Basics</p>',
    1
)
# Replace preview card 2 title
l08 = l08.replace(
    '<p class="text-sm font-semibold text-gray-700">CTEs vs Subqueries</p>',
    '<p class="text-sm font-semibold text-gray-700">PARTITION BY Explained</p>',
    1
)

# 2f. Fix bottom-nav links
# Previous → fix to lesson07_joining_tables_join.html
l08 = l08.replace(
    'href="../mod_05_sql_foundations/lesson09_joining_tables_join.html"',
    'href="lesson07_joining_tables_join.html"'
)
# Next link in nice nav → window functions
l08 = l08.replace(
    'href="lesson02_common_table_expressions_ctes.html"',
    'href="lesson09_window_functions_partition_by.html"'
)
# Next link label
l08 = l08.replace(
    '<p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Common Table Expressions (CTEs)</p>',
    '<p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Window Functions (PARTITION BY)</p>'
)
# Old-style duplicate nav block also has the title text
l08 = l08.replace(
    '<p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">Common Table Expressions (CTEs)</p>',
    '<p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">Window Functions (PARTITION BY)</p>'
)

# Also fix the old-style nav prev label "Joining Tables" was probably wrong - leave it
with open(L08, 'w', encoding='utf-8') as f:
    f.write(l08)
print("  ✅ lesson08 written")


# ─── PART 3: Delete lesson09 (old CTE file) ───────────────────────────────────
print("\n─── PART 3: Delete lesson09 (CTE) ───")
if os.path.exists(L09_OLD):
    os.remove(L09_OLD)
    print(f"  ✅ Deleted {L09_OLD}")
else:
    print(f"  ⚠️  {L09_OLD} already gone")


# ─── PART 4: Rename lessons 10-17 → 9-16 ──────────────────────────────────────
print("\n─── PART 4: Rename lesson10..17 → lesson09..16 ───")
RENAMES = []  # (old_name, new_name)
for old_n in range(10, 18):
    new_n = old_n - 1
    pat = re.compile(rf'^lesson{old_n}_(.+\.html)$')
    for fn in os.listdir(DIR):
        m = pat.match(fn)
        if m:
            new_fn = f'lesson{new_n:02d}_{m.group(1)}'
            old_p = os.path.join(DIR, fn)
            new_p = os.path.join(DIR, new_fn)
            os.rename(old_p, new_p)
            RENAMES.append((fn, new_fn))
            print(f"  {fn} → {new_fn}")


# ─── PART 5: Update each renamed file's hero / next-preview / bottom-nav ──────
print("\n─── PART 5: Updating renamed files' internal numbering ───")
# Build new hero "Lesson NN" labels.
# After merge: lesson08 = Module 6 / Lesson 01.  lesson09 (formerly lesson10) = Lesson 02. etc.
# The OLD file lesson10 had hero "Lesson 03" → new "Lesson 02"
# Generic rule: file lesson{NN} (after rename) has hero "Lesson {NN-7:02d}" (because lesson08 = Lesson 01, lesson09 = Lesson 02, …)

for old_fn, new_fn in RENAMES:
    path = os.path.join(DIR, new_fn)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # File numbers:
    new_file_n = int(new_fn[6:8])           # e.g. 9 for lesson09
    old_file_n = int(old_fn[6:8])           # e.g. 10
    # Hero "Lesson NN" — old had file_n - 7 padded. But we observed lesson10 → "Lesson 03".
    # That fits: 10 - 7 = 3. After rename to lesson09 → "Lesson 02" = 9 - 7.
    new_hero_n = new_file_n - 7
    old_hero_n = old_file_n - 7
    # next-preview "Module 6 · Lesson N" — old had hero_n + 1 (the next lesson number)
    new_next_n = new_hero_n + 1
    old_next_n = old_hero_n + 1
    # progress pill "N/10" — N == old_hero_n.  Becomes (new_hero_n)/9
    # Hero badge replace
    c = c.replace(
        f'>Lesson {old_hero_n:02d}</p>',
        f'>Lesson {new_hero_n:02d}</p>'
    )
    # next-lesson preview (label uses non-padded number after middot)
    c = c.replace(
        f'Module 6 &middot; Lesson {old_next_n}</p>',
        f'Module 6 &middot; Lesson {new_next_n}</p>'
    )
    # Also handle the badge number circle (large number in next-lesson box: "N")
    # Format: <span class="text-white font-bold text-lg">N</span>
    c = re.sub(
        rf'(text-white font-bold text-lg">){old_next_n}(</span>)',
        rf'\g<1>{new_next_n}\g<2>',
        c
    )
    # Progress pill "N/10" → "(N)/9" (use new_hero_n / 9)
    c = re.sub(
        r'<span class="font-extrabold">(\d+)<span class="font-bold opacity-50">/10</span></span>',
        f'<span class="font-extrabold">{new_hero_n}<span class="font-bold opacity-50">/9</span></span>',
        c
    )

    # Bottom-nav prev link: old prev pointed to file (old_file_n - 1)... after rename, prev points to (new_file_n - 1).
    # Find the old prev filename pattern in nav links and shift.
    # Easier: scan for any href="lessonXX_..." where XX in (old_file_n - 1, old_file_n + 1) and shift to new numbering.
    def shift_href(match):
        full = match.group(0)
        href = match.group(1)
        nn = int(match.group(2))
        rest = match.group(3)
        if nn >= 10:  # only shift 10..17 → 9..16
            new_nn = nn - 1
            return f'href="lesson{new_nn:02d}_{rest}"'
        return full
    c = re.sub(r'href="(lesson)(\d{2})_([^"]+)"', shift_href, c)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"  ✅ {new_fn}: hero Lesson {old_hero_n:02d}→{new_hero_n:02d}, next-preview Lesson {old_next_n}→{new_next_n}, progress /10→/9, hrefs shifted")


# ─── PART 6: Update lesson07's next-preview title ─────────────────────────────
print("\n─── PART 6: Updating lesson07 next-preview title ───")
with open(L07, 'r', encoding='utf-8') as f:
    l07 = f.read()
old_count = l07.count('Subqueries')
l07 = l07.replace(
    '<h3 class="text-base font-bold text-gray-800">Subqueries</h3>',
    '<h3 class="text-base font-bold text-gray-800">Subqueries and CTEs</h3>'
)
l07 = l07.replace(
    '<p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Subqueries</p>',
    '<p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Subqueries and CTEs</p>'
)
with open(L07, 'w', encoding='utf-8') as f:
    f.write(l07)
print(f"  ✅ lesson07 updated (Subqueries → Subqueries and CTEs in next-preview)")


# ─── PART 7: Verify ───────────────────────────────────────────────────────────
print("\n─── PART 7: Verification ───")
files = sorted(os.listdir(DIR))
lessons = [f for f in files if f.startswith('lesson') and f.endswith('.html')]
print(f"  Module now has {len(lessons)} lesson files:")
for f in lessons:
    print(f"    {f}")
