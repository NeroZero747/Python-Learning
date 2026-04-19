"""
Rewrites KC panels 4 and 5 in lesson02 to teach pd.read_json() and pd.json_normalize()
instead of the raw Python json module (which is not the pandas analyst workflow).
Also updates the corresponding tab button labels.
"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

FILE = r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_03_python_for_data_analysts\lesson02_reading_files_csv_excel_json.html'

with open(FILE, 'r', encoding='utf-8') as fh:
    html = fh.read()

# ── Tab button 4 label ──────────────────────────────────────────────────────
OLD_BTN4 = '''<button onclick="switchKcTab(4)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:file-import"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Loading JSON Files</span>
          </button>'''

NEW_BTN4 = '''<button onclick="switchKcTab(4)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:file-import"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">pd.read_json()</span>
          </button>'''

# ── Tab button 5 label ──────────────────────────────────────────────────────
OLD_BTN5 = '''<button onclick="switchKcTab(5)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:sitemap"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Nested JSON</span>
          </button>'''

NEW_BTN5 = '''<button onclick="switchKcTab(5)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:sitemap"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">json_normalize()</span>
          </button>'''

# ── Panel 4 — full replacement (pd.read_json) ───────────────────────────────
# Use unique subtitle "Read JSON into Python" to locate; the panel start is the
# kc-panel div that contains it.  We locate by finding the panel whose header
# subtitle reads "Read JSON into Python".

def find_panel_bounds(html, unique_subtitle):
    """Return (start, end) char indices of the kc-panel div that contains unique_subtitle."""
    sub_pos = html.index(unique_subtitle)
    # Walk back to find the opening kc-panel div
    panel_open_tag = '<div class="kc-panel'
    start = html.rfind(panel_open_tag, 0, sub_pos)
    # Walk forward to find the matching closing </div> at the panel level.
    # The panel is opened by the first <div> found at `start`.
    # We need to count nested divs.
    depth = 0
    pos = start
    while pos < len(html):
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_open == -1 and next_close == -1:
            break
        if next_open != -1 and (next_close == -1 or next_open < next_close):
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            pos = next_close + 6
            if depth == 0:
                return start, pos
    raise ValueError(f'Could not find panel for subtitle: {unique_subtitle!r}')


NEW_PANEL4 = '''\
<div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:file-import"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">pd.read_json()</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Load JSON directly into a DataFrame</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> function
                  </span>
                </div>

                <p class="text-xs text-gray-600 leading-relaxed"><strong>pd.read_json()</strong> reads a JSON file directly into a pandas DataFrame. You do not need to <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">open()</code> the file first — pandas handles the file reading for you, just like <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">read_csv()</code> does for CSV files.</p>

                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:sliders"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Key Parameters</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/3">filepath</td>
                        <td class="py-2 px-3 text-gray-500">Path to the JSON file (required)</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">orient</td>
                        <td class="py-2 px-3 text-gray-500">JSON structure — default <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">columns</code>; use <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">records</code> for arrays of objects</td>
                      </tr>
                      <tr class="">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">lines</td>
                        <td class="py-2 px-3 text-gray-500">Set <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">True</code> to read JSON Lines format (one object per line, common in log files)</td>
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

# Standard JSON — array of objects (most common format)
df = pd.read_json("sales.json")

# JSON Lines format — one object per line (.jsonl)
df = pd.read_json("data.jsonl", lines=True)

print(df.head())    # inspect the first 5 rows
print(df.dtypes)    # check column types were read correctly</code></pre>
                </div>

                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>pd.read_json() works best with flat JSON.</strong> If your file contains nested objects (objects inside objects), the nested columns will appear as Python dicts in your DataFrame. Use <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">pd.json_normalize()</code> to flatten them into separate columns first.</p>
                </div>

              </div>
            </div>
          </div>'''

NEW_PANEL5 = '''\
<div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:sitemap"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">json_normalize()</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Flatten nested JSON into a DataFrame</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> function
                  </span>
                </div>

                <p class="text-xs text-gray-600 leading-relaxed">When a JSON file contains nested objects, <strong>pd.json_normalize()</strong> flattens the structure into a flat table. Nested keys are joined with a dot to form column names — so <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">{"address": {"city": "London"}}</code> becomes a column named <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">address.city</code>.</p>

                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:layer-group"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">Nested → Flattened Column Names</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-gray-100">
                        <th class="py-2 px-3 text-left font-bold text-gray-400">JSON input</th>
                        <th class="py-2 px-3 text-left font-bold text-gray-400">Column name after normalize</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-mono text-gray-600 text-[10px]">"name": "Alice"</td>
                        <td class="py-2 px-3 font-mono text-blue-700 text-[10px]">name</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-mono text-gray-600 text-[10px]">"address": {"city": "London"}</td>
                        <td class="py-2 px-3 font-mono text-blue-700 text-[10px]">address.city</td>
                      </tr>
                      <tr class="">
                        <td class="py-2 px-3 font-mono text-gray-600 text-[10px]">"address": {"zip": "EC1A"}</td>
                        <td class="py-2 px-3 font-mono text-blue-700 text-[10px]">address.zip</td>
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import json
import pandas as pd

# Step 1 — load the JSON file into a Python list/dict
with open("users.json") as f:
    data = json.load(f)

# Step 2 — flatten nested keys into DataFrame columns
df = pd.json_normalize(data)

# Nested keys become dot-separated column names
print(df.columns.tolist())
# ['name', 'address.city', 'address.zip']

# Step 3 — rename columns to remove the dots
df = df.rename(columns={"address.city": "city", "address.zip": "zip_code"})</code></pre>
                </div>

                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>If a column prints as dicts, your JSON is nested.</strong> Run <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">print(df["column_name"][0])</code> — if the output looks like <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">{'city': 'London'}</code>, that column still contains a nested object. Pass the list to <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">pd.json_normalize()</code> to flatten it.</p>
                </div>

              </div>
            </div>
          </div>'''

# ── Apply all 4 replacements ────────────────────────────────────────────────
changes = [
    ('Tab btn 4', OLD_BTN4, NEW_BTN4),
    ('Tab btn 5', OLD_BTN5, NEW_BTN5),
]

for label, old, new in changes:
    count = html.count(old)
    if count == 1:
        html = html.replace(old, new)
        print(f'✅ {label}: replaced')
    elif count == 0:
        print(f'❌ {label}: NOT FOUND')
    else:
        print(f'⚠️  {label}: {count} matches — skipped (ambiguous)')

# Panel 4 replacement using find_panel_bounds
try:
    s4, e4 = find_panel_bounds(html, 'Read JSON into Python')
    old_panel4 = html[s4:e4]
    html = html[:s4] + NEW_PANEL4 + html[e4:]
    print('✅ Panel 4: replaced')
except Exception as ex:
    print(f'❌ Panel 4: {ex}')

# Panel 5 replacement using find_panel_bounds
try:
    s5, e5 = find_panel_bounds(html, 'Access data inside nested objects')
    old_panel5 = html[s5:e5]
    html = html[:s5] + NEW_PANEL5 + html[e5:]
    print('✅ Panel 5: replaced')
except Exception as ex:
    print(f'❌ Panel 5: {ex}')

with open(FILE, 'w', encoding='utf-8') as fh:
    fh.write(html)
print('\nFile saved.')
