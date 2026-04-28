"""
Replace the #mistakes section body in lesson04_filtering_data_with_where.html
3 mistakes:
  1. Quotes Around Text  — omitting single quotes around text values
  2. AND vs OR           — using AND when filtering the same column for two values
  3. WHERE Before FROM   — wrong clause order
SQL lesson — uses language-sql, Style B-lite panels.
"""

TARGET = (
    r"c:/Users/nightwolf/Projects/Python-Learning/pages/"
    r"mod_06a_sql_foundation/mod_05_sql_foundations/lesson04_filtering_data_with_where.html"
)

NEW_BODY = """      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Quotes Around Text</span>
        </button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">AND vs OR</span>
        </button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">WHERE Before FROM</span>
        </button>
      </div>

      <!-- ── Mistake 1: Quotes Around Text ──────────────────────────────── -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Omitting Single Quotes Around a Text Value</h4>
              <p class="text-xs text-gray-500 mt-0.5">SQL treats an unquoted word as a column name — this causes an error, not a match.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">WHERE city = Chicago</code> tells SQL to compare the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">city</code> column against another column called <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Chicago</code>. Because no such column exists, the database returns an error. Wrap text values in single quotes: <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">WHERE city = &apos;Chicago&apos;</code>.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — unquoted text value
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">WHERE city = Chicago</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — single quotes around text
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">WHERE city = &apos;Chicago&apos; -- match city to the text value</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Single quotes tell SQL "this is a piece of text to match against." Without them, SQL looks for a column with that name — just like Excel would if you typed a cell reference instead of a value in a formula.</p>
          </div>

        </div>
      </div>

      <!-- ── Mistake 2: AND vs OR ─────────────────────────────────────────── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Using AND When Filtering the Same Column for Two Values</h4>
              <p class="text-xs text-gray-500 mt-0.5">A single row can only hold one value per column — AND with two different values returns zero rows.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">WHERE city = &apos;Chicago&apos; AND city = &apos;New York&apos;</code> asks for rows where the city column equals both values at the same time. No single row can satisfy that, so the query always returns zero results. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">OR</code> to allow either value.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — AND returns no rows
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">WHERE city = &apos;Chicago&apos;
AND city = &apos;New York&apos;</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — OR returns both cities
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">WHERE city = &apos;Chicago&apos;  -- match Chicago
OR city = &apos;New York&apos;    -- or match New York</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of it this way: the <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">city</code> column holds one value per row — "Chicago" or "New York", never both at once. OR works like a checklist where passing any one box is enough; AND requires every box to pass at the same time.</p>
          </div>

        </div>
      </div>

      <!-- ── Mistake 3: WHERE Before FROM ────────────────────────────────── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Writing WHERE Before FROM in the Query</h4>
              <p class="text-xs text-gray-500 mt-0.5">SQL requires a fixed clause order — WHERE placed before FROM causes a syntax error.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">SQL reads clauses in a strict order: <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SELECT</code> first, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">FROM</code> second, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">WHERE</code> third. Placing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">WHERE</code> before <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">FROM</code> raises a syntax error because SQL cannot filter rows from a table it hasn't been told about yet. Always follow the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SELECT → FROM → WHERE</code> sequence.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — WHERE before FROM
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT *
WHERE city = &apos;Chicago&apos;
FROM customers;</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — SELECT → FROM → WHERE
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-sql">SELECT *                  -- choose columns first
FROM customers            -- then name the table
WHERE city = &apos;Chicago&apos;;  -- then apply the filter</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">A useful way to remember the order is <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">S → F → W</code>: Select what you want, From which table, Where the condition applies. Every SQL query you write will follow that same sequence.</p>
          </div>

        </div>
      </div>
"""

# ── Locate and replace the body div inside #mistakes ────────────────────────

SECTION_ANCHOR = '<section id="mistakes">'
BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
SECTION_CLOSE_AFTER = '\n    </div>\n  </div>\n</section>\n\n\n<section id="recap">'

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

mistakes_start = content.index(SECTION_ANCHOR)
body_open_pos = content.index(BODY_OPEN, mistakes_start)
body_content_start = body_open_pos + len(BODY_OPEN)

section_close_pos = content.index(SECTION_CLOSE_AFTER, body_content_start)

old_body = content[body_content_start:section_close_pos]
print(f"Old body: {len(old_body)} chars")
print(f"Old body preview: {repr(old_body[:100])}")

new_content = content[:body_content_start] + '\n' + NEW_BODY + '    ' + content[section_close_pos:]

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ #mistakes body replaced successfully.")

# Verify
with open(TARGET, 'r', encoding='utf-8') as f:
    verify = f.read()

checks = {
    'Quotes Around Text': verify.count('Quotes Around Text'),
    'AND vs OR': verify.count('AND vs OR'),
    'WHERE Before FROM': verify.count('WHERE Before FROM'),
    'Mistake 1 (old)': verify.count('>Mistake 1<'),
    'mk-panel count': verify.count('mk-panel mk-panel-anim'),
    'hidden panels': verify.count('mk-panel mk-panel-anim hidden'),
    'Explanation paras': verify.count('<div class="px-6 py-5">\n            <p class="text-sm text-gray-600'),
    'Amber tips (mistakes)': verify.count('bg-amber-50/40'),
}
print("\nVerification:")
for k, v in checks.items():
    print(f"  {k}: {v}")
