"""Rewrite the #key-concepts section in lesson02_project_folder_structure.html.

4 tabs:
  0. Project Root   (pink)    — rules-table: folder naming rules
  1. Module         (violet)  — rules-table: module naming rules
  2. Data Folder    (blue)    — comparison-table: raw/ vs processed/
  3. Entry Point    (emerald) — comparison-table: main.py vs modules/

CSS + JS already present — no changes needed there.
"""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

NEW_SECTION = '''\
<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Project root, modules, data folder, and entry point — with examples for each.</p>
      </div>
    </div>

    <!-- Two-column layout: sidebar left, panel right -->
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar tabs ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <!-- Active indicator bar (desktop only) -->
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — Project Root (pink, active) -->
          <button onclick="switchKcTab(0)"
            class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:folder-open"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Project Root</span>
          </button>

          <!-- Tab 1 — Module (violet, inactive) -->
          <button onclick="switchKcTab(1)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:file-code"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Module</span>
          </button>

          <!-- Tab 2 — Data Folder (blue, inactive) -->
          <button onclick="switchKcTab(2)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:database"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Data Folder</span>
          </button>

          <!-- Tab 3 — Entry Point (emerald, inactive) -->
          <button onclick="switchKcTab(3)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:play"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Entry Point</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Content panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ═══════════════════════════════════════════ -->
          <!-- Panel 0 — Project Root (pink, ACTIVE)      -->
          <!-- ═══════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:folder-open"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Project Root</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">The master folder that holds everything</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:folder"></span> folder
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <strong>project root is the single top-level folder that contains every file and subfolder in your project</strong>. You create one root folder per project, and every path in your code is relative to it.</p>

                <!-- Widget: rules-table — folder naming rules -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">Folder Naming Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">No spaces — use <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">_</code> instead</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">Sales Analysis</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">sales_analysis</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Describe the project, not the date</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">project_march</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">customer_churn</code> ✓
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Use underscores, not hyphens</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">hr-data</code> → prefer
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">hr_data</code> ✓
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># A well-structured project root looks like this:
# sales_analysis/          ← the project root folder
# ├── main.py             # entry point — run this file to start
# ├── modules/            # reusable scripts live here
# ├── data/               # all data files live here
# └── config.env          # settings: file paths, passwords</code></pre>
                </div>

                <!-- Tip callout — pink -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Keep your root at a stable path.</strong> Python builds file paths from the root, so moving the root folder will break your <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">import</code> statements. Put it in your Documents folder and leave it there.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ════════════════════════════════════════════ -->
          <!-- Panel 1 — Module (violet, hidden)           -->
          <!-- ════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:file-code"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Module</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">A .py file with one clear responsibility</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> .py file
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>module is a single Python file that handles one specific task</strong>, such as cleaning data or calculating totals. You import it into your main script instead of copying and pasting the same code into every project.</p>

                <!-- Widget: rules-table — module naming rules -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Module Naming Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">All <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">lowercase</code> letters</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">Cleaning.py</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">cleaning.py</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Separate words with <code class="font-mono bg-violet-100 text-violet-700 border border-violet-200 px-1 rounded">_</code></td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">datacleaning.py</code> → prefer
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">data_cleaning.py</code>
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Name by task, not by person</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">johns_script.py</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">exports.py</code> ✓
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># modules/cleaning.py — handles data cleaning only
def remove_blanks(df):
    return df.dropna()        # drops every row that has an empty cell

# main.py — imports and uses the cleaning module
from modules.cleaning import remove_blanks  # bring in the function
clean_df = remove_blanks(raw_df)            # use it without copy-pasting</code></pre>
                </div>

                <!-- Tip callout — violet -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>One module, one job.</strong> If <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">cleaning.py</code> starts calculating totals, split it. A module that does too much is just as hard to navigate as one enormous file.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ════════════════════════════════════════════ -->
          <!-- Panel 2 — Data Folder (blue, hidden)        -->
          <!-- ════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:database"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Data Folder</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Separate raw data from processed results</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:folder-tree"></span> data/
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <strong>data folder keeps all your CSV and Excel files separate from your Python scripts</strong>. Split it into a <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">raw/</code> subfolder for original files and a <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">processed/</code> subfolder for cleaned outputs — so you never overwrite your source data by accident.</p>

                <!-- Widget: comparison-table — raw/ vs processed/ -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">raw/ vs processed/</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">raw/</span>
                        </th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-700 border border-indigo-200 text-[10px] font-bold">processed/</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">What goes here</td>
                        <td class="py-2 px-3 text-gray-500">Unedited original files</td>
                        <td class="py-2 px-3 text-gray-500">Files your scripts produced</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Write to it?</td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">&#x2717;</span> <span class="text-gray-400">Never</span></td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">&#x2713;</span> <span class="text-gray-400">Every run</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Example file</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">sales_jan.csv</code></td>
                        <td class="py-2 px-3"><code class="font-mono bg-indigo-100 text-indigo-700 border border-indigo-200 px-1 rounded">sales_jan_clean.csv</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
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

# Read from raw/ — treat this folder as read-only
df = pd.read_csv("data/raw/sales_jan.csv")

# Save cleaned result to processed/ — safe to overwrite each run
df.dropna().to_csv("data/processed/sales_jan_clean.csv", index=False)</code></pre>
                </div>

                <!-- Tip callout — blue -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Never write back to <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">raw/</code>.</strong> Treat those files as backup originals — if a script corrupts its output, you can always reprocess from <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">data/raw/</code> without losing anything.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ════════════════════════════════════════════ -->
          <!-- Panel 3 — Entry Point (emerald, hidden)     -->
          <!-- ════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:play"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Entry Point</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">The one script that starts your pipeline</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> main.py
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <strong>entry point is the single script you run to start your entire project</strong> — usually called <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">main.py</code>. It imports functions from your modules and calls them in order. You never run the individual module files directly.</p>

                <!-- Widget: comparison-table — main.py vs modules/ -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">main.py vs modules/</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-emerald-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 border border-emerald-200 text-[10px] font-bold">main.py</span>
                        </th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-teal-100 text-teal-700 border border-teal-200 text-[10px] font-bold">modules/</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Purpose</td>
                        <td class="py-2 px-3 text-gray-500">Coordinates the pipeline</td>
                        <td class="py-2 px-3 text-gray-500">Does one specific task</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Contains</td>
                        <td class="py-2 px-3 text-gray-500">Imports + function calls</td>
                        <td class="py-2 px-3 text-gray-500">Function definitions</td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Run directly?</td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">&#x2713;</span> <span class="text-gray-400">Yes</span></td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">&#x2717;</span> <span class="text-gray-400">No — imported only</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block -->
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
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># main.py — the entry point; run: python main.py
from modules.cleaning import remove_blanks   # step 1: import the cleaner
from modules.calculations import get_totals  # step 2: import the calculator
from modules.exports import save_to_csv      # step 3: import the exporter

df     = remove_blanks("data/raw/sales.csv") # clean the data
totals = get_totals(df)                       # calculate totals from clean data
save_to_csv(totals, "data/processed/")        # write results to processed/</code></pre>
                </div>

                <!-- Tip callout — emerald -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>main.py should read like a checklist.</strong> If you open it and can't tell what the project does in 10 seconds, split more tasks into separate module files.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->

      </div><!-- /flex row -->
    </div><!-- /section body -->

  </div>
</section>'''


def main():
    html = TARGET.read_text(encoding="utf-8")

    # Locate the full key-concepts section
    kc_start = html.index('<section id="key-concepts">')
    kc_end   = html.index("</section>", kc_start) + len("</section>")

    old_section = html[kc_start:kc_end]
    old_len = len(old_section)

    html = html[:kc_start] + NEW_SECTION + html[kc_end:]

    TARGET.write_text(html, encoding="utf-8")
    print(f"✅  #key-concepts section replaced  ({old_len:,} chars → {len(NEW_SECTION):,} chars)")
    print(f"File size: {len(html):,} chars")


if __name__ == "__main__":
    main()
