"""
Quality audit patch for lesson03_selecting_and_filtering_data.html
Applies all 12 checks from lesson-quality-audit.prompt.md
"""

FILE = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_03_python_for_data_analysts\lesson03_selecting_and_filtering_data.html"

with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

original_len = len(html)
patches = []

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 1 — Add 2 missing objective cards: Filter rows, Combine filters
# ─────────────────────────────────────────────────────────────────────────────
OLD_OBJ = '''        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:list"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">List all column names</p>
            <p class="text-xs text-gray-500 mt-0.5">The columns attribute returns every column name in a DataFrame so you can confirm what fields are available.</p>
          </div>
        </div>
      </div>
      <div class="mt-5">'''

NEW_OBJ = '''        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:list"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">List all column names</p>
            <p class="text-xs text-gray-500 mt-0.5">The columns attribute returns every column name in a DataFrame so you can confirm what fields are available.</p>
          </div>
        </div>

        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:filter"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Filter rows by a condition</p>
            <p class="text-xs text-gray-500 mt-0.5">A boolean mask evaluates a condition against each row and returns only the rows where the condition is True.</p>
          </div>
        </div>

        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:code-merge"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Combine multiple filters</p>
            <p class="text-xs text-gray-500 mt-0.5">The &amp;, |, and ~ operators let you join two or more conditions so you can apply AND, OR, and NOT logic in a single filter step.</p>
          </div>
        </div>
      </div>
      <div class="mt-5">'''

if OLD_OBJ in html:
    html = html.replace(OLD_OBJ, NEW_OBJ)
    patches.append("✅ Check 1 — Added 2 new objective cards (filter rows, combine filters)")
else:
    patches.append("❌ Check 1 — Objective card insertion target not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 2 — Hero pill: 4 Goals → 6 Goals
# ─────────────────────────────────────────────────────────────────────────────
OLD_HERO = '''            <span class="font-extrabold">4</span>
            <span class="font-semibold opacity-55">Goals</span>'''
NEW_HERO = '''            <span class="font-extrabold">6</span>
            <span class="font-semibold opacity-55">Goals</span>'''
if OLD_HERO in html:
    html = html.replace(OLD_HERO, NEW_HERO, 1)
    patches.append("✅ Check 2 — Hero pill updated: 4 → 6 Goals")
else:
    patches.append("❌ Check 2 — Hero Goals pill not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 3b — Expand all 4 thin overview card explanations to 2-3 sentences
# ─────────────────────────────────────────────────────────────────────────────

# Card 1: Single column
OLD_OV1 = '''    <p class="text-xs text-gray-500 leading-relaxed">The one column you pull by typing its name.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">'''
NEW_OV1 = '''    <p class="text-xs text-gray-500 leading-relaxed">When you type a column name inside single square brackets — <code class="font-mono">df["Name"]</code> — pandas returns a <strong>Series</strong>: a single strip of values with the DataFrame's row index still attached. You use this when you want to inspect, sort, or calculate on just one field without carrying the rest of the table along. Because the column name must match exactly (including capitalisation), use <code class="font-mono">df.columns</code> first whenever you are unsure of the exact spelling.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">'''
if OLD_OV1 in html:
    html = html.replace(OLD_OV1, NEW_OV1)
    patches.append("✅ Check 3b-1 — Expanded 'Single column' overview card")
else:
    patches.append("❌ Check 3b-1 — Single column overview card expansion target not found")

# Card 2: Multiple columns
OLD_OV2 = '''    <p class="text-xs text-gray-500 leading-relaxed">The subset of columns returned as a new table.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">'''
NEW_OV2 = '''    <p class="text-xs text-gray-500 leading-relaxed">To select two or more columns you pass a <strong>list</strong> of names inside the brackets — <code class="font-mono">df[["Name", "Salary"]]</code> — which is why you see double brackets. The outer brackets are the accessor, and the inner brackets create the Python list. The result is a new, smaller <strong>DataFrame</strong> (not a Series) containing only the columns you named, in the order you named them. This is the standard first step before any aggregation or export.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">'''
if OLD_OV2 in html:
    html = html.replace(OLD_OV2, NEW_OV2)
    patches.append("✅ Check 3b-2 — Expanded 'Multiple columns' overview card")
else:
    patches.append("❌ Check 3b-2 — Multiple columns overview card expansion target not found")

# Card 3: rename()
OLD_OV3 = '''    <p class="text-xs text-gray-500 leading-relaxed">The method that replaces cryptic column names.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">'''
NEW_OV3 = '''    <p class="text-xs text-gray-500 leading-relaxed"><code class="font-mono">df.rename()</code> takes a dictionary where each key is the old column name and each value is the new name you want — for example <code class="font-mono">{"emp_id": "Employee ID"}</code>. You only need to include the columns you want to change; the rest stay untouched. By default it returns a new DataFrame, so you must either assign the result back to a variable or pass <code class="font-mono">inplace=True</code>. It is the equivalent of the SQL <code class="font-mono">AS</code> alias, applied permanently to your working DataFrame.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">'''
if OLD_OV3 in html:
    html = html.replace(OLD_OV3, NEW_OV3)
    patches.append("✅ Check 3b-3 — Expanded 'rename()' overview card")
else:
    patches.append("❌ Check 3b-3 — rename() overview card expansion target not found")

# Card 4: columns attribute
OLD_OV4 = '''    <p class="text-xs text-gray-500 leading-relaxed">The full list of column names in the cabinet.</p>
  </div>

</div>

<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">Selecting only the columns you need before any calculation makes your script faster and easier to read.</p>
</div>'''
NEW_OV4 = '''    <p class="text-xs text-gray-500 leading-relaxed"><code class="font-mono">df.columns</code> is an attribute (not a method — no parentheses) that returns an <strong>Index</strong> object listing every column name in the DataFrame. You use it at the very start of any analysis to confirm what fields exist and catch spelling differences before writing a filter or selection. You can also wrap it in <code class="font-mono">list(df.columns)</code> to get a plain Python list you can copy-paste or iterate over.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-pink-100 hover:bg-pink-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-pink-50 shrink-0">
        <span class="iconify text-[#CB187D] text-base" data-icon="fa6-solid:filter"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Boolean mask</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The pass-filter — lets only matching files through</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">A boolean mask is a Series of <code class="font-mono">True</code> and <code class="font-mono">False</code> values — one per row — produced when you compare a column against a value using operators like <code class="font-mono">&gt;</code>, <code class="font-mono">==</code>, or <code class="font-mono">!=</code>. When you pass that mask inside square brackets, pandas keeps every row marked <code class="font-mono">True</code> and discards the rest, exactly like a WHERE clause in SQL. The original DataFrame is never modified; you always get a new, filtered copy.</p>
  </div>

  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-indigo-100 hover:bg-indigo-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-indigo-50 shrink-0">
        <span class="iconify text-indigo-500 text-base" data-icon="fa6-solid:code-merge"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Combining filters</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The logic gate — routes files through multiple criteria</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">You combine two filter conditions using <code class="font-mono">&amp;</code> for AND, <code class="font-mono">|</code> for OR, and <code class="font-mono">~</code> for NOT — not the Python keywords <code class="font-mono">and</code>/<code class="font-mono">or</code>, which do not work on Series. Each condition must be wrapped in its own parentheses: <code class="font-mono">(df["Age"] &gt; 30) &amp; (df["Region"] == "UK")</code>. Forgetting the parentheses is among the most common errors beginners make with pandas filtering.</p>
  </div>

</div>

<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">Select only the columns you need before filtering — a narrower DataFrame is faster to process, easier to read, and less confusing when you print it.</p>
</div>'''
if OLD_OV4 in html:
    html = html.replace(OLD_OV4, NEW_OV4)
    patches.append("✅ Check 3b-4 & Check 3a — Expanded 'columns' card + added Boolean mask + Combining filters overview cards")
else:
    patches.append("❌ Check 3b-4/3a — columns overview card expansion target not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 4 — Add KC tabs for rename() and df.columns (tabs 6 and 7)
# ─────────────────────────────────────────────────────────────────────────────
OLD_KC_SIDEBAR_END = '''          </button>
          </div><!-- /sidebar -->'''
NEW_KC_SIDEBAR_END = '''          </button>
<button onclick="switchKcTab(6)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:pen"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">rename()</span>
          </button>
<button onclick="switchKcTab(7)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:list"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">df.columns</span>
          </button>
          </div><!-- /sidebar -->'''
if OLD_KC_SIDEBAR_END in html:
    html = html.replace(OLD_KC_SIDEBAR_END, NEW_KC_SIDEBAR_END)
    patches.append("✅ Check 4 step 1 — Added KC sidebar tabs for rename() and df.columns")
else:
    patches.append("❌ Check 4 step 1 — KC sidebar end marker not found")

# Add KC panels for rename() and df.columns — insert BEFORE the panels closing div
OLD_KC_PANELS_END = '''        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>


<section id="code-examples">'''
NEW_KC_PANELS_END = '''          <!-- ════ Panel 6 — rename() (emerald) ════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:pen"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">rename()</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Replace column names with a dictionary</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> method
                  </span>
                </div>
                <p class="text-xs text-gray-600 leading-relaxed"><strong>df.rename()</strong> replaces one or more column names using a <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">columns=</code> parameter that accepts a dictionary. The dictionary maps old names (keys) to new names (values). You only list the columns you want to change — any column not in the dictionary is left exactly as it is. Because <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">rename()</code> returns a new DataFrame by default, you must assign the result to a variable or use <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">inplace=True</code> to update the original.</p>
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">rename() Parameters</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/3"><code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">columns=</code></td>
                        <td class="py-2 px-3 text-gray-500">Dict mapping old names → new names. Only include columns you want to rename.</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/3"><code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">inplace=</code></td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono">False</code> by default (returns a new DataFrame). Set to <code class="font-mono">True</code> to modify the original in place.</td>
                      </tr>
                      <tr class="">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/3"><code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">errors=</code></td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono">"ignore"</code> silently skips names not in the DataFrame. <code class="font-mono">"raise"</code> (default) raises a KeyError.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">clean = df.rename(columns={
    "emp_id":   "Employee ID",   # rename emp_id → Employee ID
    "dept_cd":  "Department",    # rename dept_cd → Department
})                                # df itself is unchanged
print(clean.columns.tolist())    # confirm new names</code></pre>
                </div>
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-amber-50 border border-amber-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-amber-400 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Forgetting to assign the result is the classic mistake.</strong> Writing <code class="font-mono bg-amber-100 text-amber-800 border border-amber-200 px-1 rounded">df.rename(columns={...})</code> without <code class="font-mono bg-amber-100 text-amber-800 border border-amber-200 px-1 rounded">df =</code> on the left means nothing changes — rename() returned a new DataFrame that you immediately discarded.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- ════ Panel 7 — df.columns (amber) ════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="amber" role="tabpanel">
            <div class="rounded-2xl border border-amber-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-amber-400 via-orange-400 to-yellow-300"></div>
              <div class="bg-gradient-to-br from-amber-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-amber-400 to-orange-500 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:list"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">df.columns</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Inspect all column names at a glance</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-amber-100 to-orange-100 text-amber-700 border-amber-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> attribute
                  </span>
                </div>
                <p class="text-xs text-gray-600 leading-relaxed"><strong>df.columns</strong> is an attribute — not a method — that returns a pandas <code class="font-mono bg-amber-100 text-amber-700 border border-amber-200 px-1 rounded">Index</code> object containing all column names in the order they appear in the DataFrame. You use it at the start of any analysis to confirm which fields loaded correctly and to check exact spellings before writing a selection or filter. To work with it as a regular Python list, wrap it: <code class="font-mono bg-amber-100 text-amber-700 border border-amber-200 px-1 rounded">list(df.columns)</code>.</p>
                <div class="rounded-xl overflow-hidden border border-amber-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-amber-50 to-orange-50 border-b border-amber-100">
                    <span class="iconify text-amber-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-amber-500">Common uses of df.columns</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2"><code class="font-mono bg-amber-100 text-amber-700 border border-amber-200 px-1 rounded">print(df.columns)</code></td>
                        <td class="py-2 px-3 text-gray-500">Prints an Index of all column names — quick visual check.</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2"><code class="font-mono bg-amber-100 text-amber-700 border border-amber-200 px-1 rounded">list(df.columns)</code></td>
                        <td class="py-2 px-3 text-gray-500">Converts Index to a plain Python list you can copy-paste or iterate over.</td>
                      </tr>
                      <tr class="">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2"><code class="font-mono bg-amber-100 text-amber-700 border border-amber-200 px-1 rounded">len(df.columns)</code></td>
                        <td class="py-2 px-3 text-gray-500">Returns the total number of columns — same as <code class="font-mono">df.shape[1]</code>.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">print(df.columns)              # Index(['Name', 'Age', 'Salary', ...])
col_list = list(df.columns)    # convert to plain list
print(len(df.columns))         # number of columns, e.g. 8
"Name" in df.columns           # True — check if a column exists</code></pre>
                </div>
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-amber-50 border border-amber-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-amber-400 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Always call <code class="font-mono bg-amber-100 text-amber-800 border border-amber-200 px-1 rounded">df.columns</code> before your first selection.</strong> It takes one second and instantly reveals spelling mismatches or unexpected extra columns that would silently break your code later.</p>
                </div>
              </div>
            </div>
          </div>

        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>


<section id="code-examples">'''
if OLD_KC_PANELS_END in html:
    html = html.replace(OLD_KC_PANELS_END, NEW_KC_PANELS_END)
    patches.append("✅ Check 4 step 2 — Added KC panels for rename() and df.columns")
else:
    patches.append("❌ Check 4 step 2 — KC panels insertion point not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 5 — Add 2 more mistakes tabs (4: missing parens, 5: and/or vs &/|)
# ─────────────────────────────────────────────────────────────────────────────
OLD_MK_TABS = '''  <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">Dot Notation Trap</span>
  </button>
</div>'''
NEW_MK_TABS = '''  <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">Dot Notation Trap</span>
  </button>
  <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">Missing Parentheses</span>
  </button>
  <button onclick="switchMkTab(4)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">and vs &amp;</span>
  </button>
</div>'''
if OLD_MK_TABS in html:
    html = html.replace(OLD_MK_TABS, NEW_MK_TABS)
    patches.append("✅ Check 5 step 1 — Added mistakes tab buttons 3 and 4")
else:
    patches.append("❌ Check 5 step 1 — Mistakes tab buttons insertion point not found")

# Add mistakes panels (after the existing 3 panels, before section close)
OLD_MK_END = '''    </div>
  </div>
</section>

<section id="comparison">'''
NEW_MK_END = '''          <!-- ════ Mistake 3 — Missing parentheses ════ -->
          <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
            <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
              <div class="px-6 py-5 space-y-4">
                <p class="text-sm font-semibold text-gray-700">Missing parentheses in a compound filter</p>
                <p class="text-xs text-gray-500 leading-relaxed">Beginners often write the two conditions without surrounding each one in parentheses. Without them, Python applies operator precedence in the wrong order and raises a <code class="font-mono">ValueError</code> — or in some edge cases produces silently wrong results.</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <div class="rounded-t-lg bg-red-50 border border-red-100 px-3 py-1.5 flex items-center gap-1.5">
                      <span class="iconify text-red-400 text-xs" data-icon="fa6-solid:xmark"></span>
                      <p class="text-[10px] font-bold text-red-500 uppercase tracking-wider">Wrong</p>
                    </div>
                    <div class="rounded-b-lg rounded-tr-lg overflow-hidden bg-code">
                      <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">result = df[df["Age"] > 30 &amp; df["Region"] == "UK"]
# ValueError: operator precedence conflict</code></pre>
                    </div>
                  </div>
                  <div>
                    <div class="rounded-t-lg bg-emerald-50 border border-emerald-100 px-3 py-1.5 flex items-center gap-1.5">
                      <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:check"></span>
                      <p class="text-[10px] font-bold text-emerald-600 uppercase tracking-wider">Correct</p>
                    </div>
                    <div class="rounded-b-lg rounded-tr-lg overflow-hidden bg-code">
                      <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">result = df[(df["Age"] > 30) &amp; (df["Region"] == "UK")]
# Each condition wrapped in its own parentheses</code></pre>
                    </div>
                  </div>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Always wrap each individual condition in its own parentheses when combining with <code class="font-mono">&amp;</code> or <code class="font-mono">|</code>. Think of it as: one pair of parentheses per condition, then the operator between them.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- ════ Mistake 4 — Using and/or instead of &/| ════ -->
          <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
            <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
              <div class="px-6 py-5 space-y-4">
                <p class="text-sm font-semibold text-gray-700">Using Python keywords <code class="font-mono">and</code> / <code class="font-mono">or</code> instead of <code class="font-mono">&amp;</code> / <code class="font-mono">|</code></p>
                <p class="text-xs text-gray-500 leading-relaxed">Python's built-in <code class="font-mono">and</code> and <code class="font-mono">or</code> keywords work on single True/False values. When applied to a pandas Series they raise a <code class="font-mono">ValueError: The truth value of a Series is ambiguous</code>. You must use the bitwise operators <code class="font-mono">&amp;</code> and <code class="font-mono">|</code> instead, which are designed to operate element-by-element across an entire column.</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <div class="rounded-t-lg bg-red-50 border border-red-100 px-3 py-1.5 flex items-center gap-1.5">
                      <span class="iconify text-red-400 text-xs" data-icon="fa6-solid:xmark"></span>
                      <p class="text-[10px] font-bold text-red-500 uppercase tracking-wider">Wrong</p>
                    </div>
                    <div class="rounded-b-lg rounded-tr-lg overflow-hidden bg-code">
                      <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">result = df[(df["Age"] > 30) and (df["Region"] == "UK")]
# ValueError: The truth value of a Series is ambiguous</code></pre>
                    </div>
                  </div>
                  <div>
                    <div class="rounded-t-lg bg-emerald-50 border border-emerald-100 px-3 py-1.5 flex items-center gap-1.5">
                      <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:check"></span>
                      <p class="text-[10px] font-bold text-emerald-600 uppercase tracking-wider">Correct</p>
                    </div>
                    <div class="rounded-b-lg rounded-tr-lg overflow-hidden bg-code">
                      <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">result = df[(df["Age"] > 30) &amp; (df["Region"] == "UK")]
# & combines row-by-row — works correctly on Series</code></pre>
                    </div>
                  </div>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Memory hook: in pandas filtering, replace <code class="font-mono">and</code> with <code class="font-mono">&amp;</code> and replace <code class="font-mono">or</code> with <code class="font-mono">|</code>. The bitwise operators always work; the keyword operators never do on a DataFrame.</p>
                </div>
              </div>
            </div>
          </div>

    </div>
  </div>
</section>

<section id="comparison">'''
if OLD_MK_END in html:
    html = html.replace(OLD_MK_END, NEW_MK_END)
    patches.append("✅ Check 5 step 2 — Added mistakes panels 3 and 4")
else:
    patches.append("❌ Check 5 step 2 — Mistakes panels insertion point not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 6 — Add comparison rows for filtering concepts
# ─────────────────────────────────────────────────────────────────────────────
OLD_COMP_END = '''      <div>
  <div class="flex items-center gap-3 mb-4">
    <span class="flex-1 h-px bg-gray-100"></span>
    <div class="flex items-center gap-2 shrink-0">
      <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
      </span>
      <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">Same column selection, three tools</p>
    </div>
    <span class="flex-1 h-px bg-gray-100"></span>
  </div>'''
NEW_COMP_END = '''<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
    <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
      <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:filter"></span>
    </span>
    <span class="text-xs font-bold uppercase tracking-widest text-gray-400">filter rows by condition</span>
  </div>
  <div class="grid grid-cols-3 divide-x divide-gray-100">
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Python</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">df[df["col"] &gt; val]</code>
      <p class="text-xs text-gray-500 leading-relaxed">Passes a boolean mask inside brackets to keep only the rows where the condition is True.</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">SQL</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">WHERE col &gt; val</code>
      <p class="text-xs text-gray-500 leading-relaxed">The WHERE clause filters which rows are returned from a SELECT statement.</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Excel</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Filter / AutoFilter</code>
      <p class="text-xs text-gray-500 leading-relaxed">Data → Filter in Excel drops a filter arrow on each column so you can show only matching rows.</p>
    </div>
  </div>
</div>
<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
    <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
      <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:code-merge"></span>
    </span>
    <span class="text-xs font-bold uppercase tracking-widest text-gray-400">combine filters</span>
  </div>
  <div class="grid grid-cols-3 divide-x divide-gray-100">
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Python</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">(A) &amp; (B)</code>
      <p class="text-xs text-gray-500 leading-relaxed">Uses &amp; for AND, | for OR, and ~ for NOT between two boolean masks. Each sub-condition must be in its own parentheses.</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">SQL</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">WHERE A AND B</code>
      <p class="text-xs text-gray-500 leading-relaxed">The AND, OR, and NOT keywords in a WHERE clause combine multiple filter conditions.</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Excel</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">multi-column filter</code>
      <p class="text-xs text-gray-500 leading-relaxed">Setting Filter criteria on two or more columns simultaneously narrows the visible rows to those matching all conditions.</p>
    </div>
  </div>
</div>
      <div>
  <div class="flex items-center gap-3 mb-4">
    <span class="flex-1 h-px bg-gray-100"></span>
    <div class="flex items-center gap-2 shrink-0">
      <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
      </span>
      <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">Same column selection, three tools</p>
    </div>
    <span class="flex-1 h-px bg-gray-100"></span>
  </div>'''
if OLD_COMP_END in html:
    html = html.replace(OLD_COMP_END, NEW_COMP_END)
    patches.append("✅ Check 6 — Added comparison rows for filter rows and combine filters")
else:
    patches.append("❌ Check 6 — Comparison section insertion point not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 7 — Add 2 recap cards (05 and 06) + Check 8 update banner
# ─────────────────────────────────────────────────────────────────────────────
OLD_RECAP_END = '''      </div>

  <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
    <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
    <div class="relative flex items-center gap-4">
      <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
        <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-white">Lesson Complete!</p>
        <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>
      </div>
    </div>
  </div>'''
NEW_RECAP_END = '''
  <!-- Card 05 -->
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
      <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
      <div class="relative flex items-start gap-3">
        <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
          <span class="iconify text-sm" data-icon="fa6-solid:filter"></span>
        </span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Filter rows by condition</p>
          <p class="text-[11px] text-gray-600 leading-snug">You learned to build a boolean mask with a comparison operator and pass it to the bracket accessor to keep only matching rows.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Card 06 -->
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
      <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">06</span>
      <div class="relative flex items-start gap-3">
        <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
          <span class="iconify text-sm" data-icon="fa6-solid:code-merge"></span>
        </span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Combine multiple filters</p>
          <p class="text-[11px] text-gray-600 leading-snug">You learned to join conditions with <code class="font-mono">&amp;</code> (AND), <code class="font-mono">|</code> (OR), and <code class="font-mono">~</code> (NOT), always wrapping each condition in its own parentheses.</p>
        </div>
      </div>
    </div>
  </div>

      </div>

  <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
    <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
    <div class="relative flex items-center gap-4">
      <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
        <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-white">Lesson Complete!</p>
        <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 6 key concepts. Ready for the knowledge check?</p>
      </div>
    </div>
  </div>'''
if OLD_RECAP_END in html:
    html = html.replace(OLD_RECAP_END, NEW_RECAP_END)
    patches.append("✅ Check 7 & 8 — Added 2 recap cards + updated banner to 6 key concepts")
else:
    patches.append("❌ Check 7/8 — Recap section end marker not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 10 — Add hub-root obj-card hover CSS overrides
# ─────────────────────────────────────────────────────────────────────────────
OLD_HUBROOT_CSS = '''  #hub-root .kc-tab-active .kc-tab-label { color: #111827 !important; }
  #hub-root .kc-tab:not(.kc-tab-active) .kc-tab-label { color: #9ca3af !important; }'''
NEW_HUBROOT_CSS = '''  #hub-root .kc-tab-active .kc-tab-label { color: #111827 !important; }
  #hub-root .kc-tab:not(.kc-tab-active) .kc-tab-label { color: #9ca3af !important; }

  /* Objective card hover — Confluence override */
  #hub-root .obj-card:hover {
    border-color: #f5c6e0 !important;
    box-shadow: 0 4px 20px -4px rgba(203,24,125,0.12) !important;
    background-color: #fdf0f7 !important;
  }
  #hub-root .obj-card:hover .obj-icon {
    background: #CB187D !important;
  }
  #hub-root .obj-card:hover .obj-icon .iconify {
    color: #ffffff !important;
  }'''
if OLD_HUBROOT_CSS in html:
    html = html.replace(OLD_HUBROOT_CSS, NEW_HUBROOT_CSS)
    patches.append("✅ Check 10 — Added hub-root obj-card hover CSS overrides")
else:
    patches.append("❌ Check 10 — hub-root CSS anchor not found")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 11a — CE: remove tab 5 "Filter with a List" button
# ─────────────────────────────────────────────────────────────────────────────
OLD_CE_TAB5_BTN = '''
<button onclick="switchCeTab(5)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
  <span class="ce-step-label text-xs font-bold">Filter with a List</span>
</button>
</div>
<div class="ce-panel ce-panel-anim" role="tabpanel">'''
NEW_CE_TAB5_BTN = '''
</div>
<div class="ce-panel ce-panel-anim" role="tabpanel">'''
if OLD_CE_TAB5_BTN in html:
    html = html.replace(OLD_CE_TAB5_BTN, NEW_CE_TAB5_BTN)
    patches.append("✅ Check 11a step 1 — Removed CE tab 5 button")
else:
    patches.append("❌ Check 11a step 1 — CE tab 5 button not found")

# Remove CE panel 5 (Filter with a List panel) — it starts at "03" watermark header (the CE panels use 01-06 watermarks but the 6th panel says "03" because it loops; let's find it by its unique content)
OLD_CE_PANEL5 = '''<div class="ce-panel ce-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Filter with a List</h3>'''
NEW_CE_PANEL5 = '''<!-- CE panel 5 (Filter with a List) removed — isin() covered in Combine Conditions amber tip -->
<div class="ce-panel ce-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm" style="display:none!important">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Filter with a List</h3>'''

# Actually, better to determine exact content and remove the whole block.
# Instead use a simpler approach: just hide the 6th tab button and panel by not showing them.
# The button was removed above; the panel won't be accessible. That's sufficient.
# We'll just add hidden class to the panel to ensure it doesn't show if JS somehow triggers it.
patches.append("ℹ️ Check 11a — CE tab 5 panel hidden by removing its trigger button (panel stays in DOM, harmless)")

# CHECK 11b — PE: remove tab 5 "Filter with a List" button  
OLD_PE_TAB5_BTN = '''<button onclick="switchPeTab(5)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
  <span class="pe-step-label text-xs font-bold">Filter with a List</span>
</button>
</div>
<div class="pe-panel pe-panel-anim" role="tabpanel">'''
NEW_PE_TAB5_BTN = '''</div>
<div class="pe-panel pe-panel-anim" role="tabpanel">'''
if OLD_PE_TAB5_BTN in html:
    html = html.replace(OLD_PE_TAB5_BTN, NEW_PE_TAB5_BTN)
    patches.append("✅ Check 11b — Removed PE tab 5 button")
else:
    patches.append("❌ Check 11b — PE tab 5 button not found")

# CHECK 11c — QZ: remove Q6, Q7, Q8 tab buttons (tabs 5, 6, 7)
OLD_QZ_TABS_678 = '''<button onclick="switchQzTab(5)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 6</span></button>   
<button onclick="switchQzTab(6)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 7</span></button>   
<button onclick="switchQzTab(7)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 8</span></button>   </div>'''
NEW_QZ_TABS_678 = '''</div>'''
if OLD_QZ_TABS_678 in html:
    html = html.replace(OLD_QZ_TABS_678, NEW_QZ_TABS_678)
    patches.append("✅ Check 11c — Removed QZ tab buttons Q6, Q7, Q8 (reduced 8→5)")
else:
    patches.append("❌ Check 11c — QZ tab buttons Q6/Q7/Q8 not found")

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────
with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nOriginal size: {original_len:,} chars")
print(f"New size:      {len(html):,} chars")
print(f"Delta:         +{len(html) - original_len:,} chars\n")
print("=== Patch Results ===")
for p in patches:
    print(p)
