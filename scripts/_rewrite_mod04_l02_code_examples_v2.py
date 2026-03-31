"""Two changes to lesson02_project_folder_structure.html:

  1. Add a 5th Key Concepts tab: __init__.py File (amber)
  2. Rewrite Code Examples — 3 cohesive panels around one sales_report/ project:
       Panel 1 — Set Up the Project          → setup_project.py
       Panel 2 — Write the Cleaning Module   → modules/cleaning.py
       Panel 3 — Run the Full Pipeline       → main.py
"""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

# ═══════════════════════════════════════════════════════════════════════════════
# CHANGE 1A — Insert 5th kc-tab button (amber, __init__.py)
# ═══════════════════════════════════════════════════════════════════════════════
OLD_KC_BTN = """\
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Entry Point</span>
          </button>

        </div><!-- /sidebar -->"""

NEW_KC_BTN = """\
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Entry Point</span>
          </button>

          <!-- Tab 4 — __init__.py File (amber) -->
          <button onclick="switchKcTab(4)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:file-code"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">__init__.py</span>
          </button>

        </div><!-- /sidebar -->"""

# ═══════════════════════════════════════════════════════════════════════════════
# CHANGE 1B — Insert 5th kc-panel (amber, __init__.py)
# ═══════════════════════════════════════════════════════════════════════════════
OLD_KC_PANEL_END = """\
          </div><!-- /panel 3 -->

        </div><!-- /panels -->"""

NEW_KC_PANEL_END = """\
          </div><!-- /panel 3 -->

          <!-- ═══════════════════════════════════════════ -->
          <!-- Panel 4 — __init__.py File (amber, HIDDEN) -->
          <!-- ═══════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="amber" role="tabpanel">
            <div class="rounded-2xl border border-amber-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-amber-500 via-orange-400 to-yellow-300"></div>
              <div class="bg-gradient-to-br from-amber-50/60 to-white p-5 space-y-4">

                <!-- Header -->
                <div class="flex items-center gap-3">
                  <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 shrink-0 shadow-sm">
                    <span class="iconify text-white text-sm" data-icon="fa6-solid:file-code"></span>
                  </span>
                  <div>
                    <p class="text-sm font-bold text-gray-800">The __init__.py File</p>
                    <p class="text-xs text-gray-400">What it is and why every modules/ folder needs one</p>
                  </div>
                </div>

                <!-- Plain-English explanation -->
                <p class="text-xs text-gray-600 leading-relaxed">Python tells the difference between a plain folder and an importable <strong class="text-gray-800">package</strong> by looking for a special file called <code class="text-xs font-mono px-1 py-0.5 rounded bg-amber-100 text-amber-800">__init__.py</code> inside that folder. When Python sees it, it treats the whole folder as a package and lets you use <code class="text-xs font-mono px-1 py-0.5 rounded bg-amber-100 text-amber-800">from modules.cleaning import …</code>. Without it, Python has no way to know the folder holds code you want to import, and the statement fails with a <code class="text-xs font-mono px-1 py-0.5 rounded bg-amber-100 text-amber-800">ModuleNotFoundError</code>.</p>

                <!-- With / Without comparison grid -->
                <div class="rounded-xl overflow-hidden border border-amber-100 text-[11px] font-mono">
                  <div class="grid grid-cols-2 divide-x divide-amber-100">
                    <div class="p-3 bg-red-50/50">
                      <p class="text-[10px] font-sans font-bold uppercase tracking-widest text-red-500 mb-2">Without __init__.py</p>
                      <pre class="leading-relaxed text-gray-600">modules/
└── cleaning.py</pre>
                      <p class="text-[10px] font-sans text-red-500 mt-2 font-semibold">→ import fails with ModuleNotFoundError</p>
                    </div>
                    <div class="p-3 bg-emerald-50/50">
                      <p class="text-[10px] font-sans font-bold uppercase tracking-widest text-emerald-600 mb-2">With __init__.py</p>
                      <pre class="leading-relaxed text-gray-600">modules/
├── __init__.py
└── cleaning.py</pre>
                      <p class="text-[10px] font-sans text-emerald-600 mt-2 font-semibold">→ import works correctly</p>
                    </div>
                  </div>
                </div>

                <!-- What goes inside -->
                <div class="rounded-xl border border-amber-100 overflow-hidden">
                  <div class="bg-amber-50 px-3 py-2 border-b border-amber-100">
                    <p class="text-[10px] font-bold uppercase tracking-widest text-amber-700">What goes inside __init__.py?</p>
                  </div>
                  <div class="p-3 bg-white space-y-2">
                    <p class="text-xs text-gray-600">Almost always — <strong class="text-gray-800">nothing</strong>. The file exists purely so Python can recognise the folder. Leave it completely empty. The easiest way to create it in your setup script is one line of Python:</p>
                    <div class="rounded-lg bg-gray-900 px-4 py-3">
                      <pre class="text-xs font-mono text-emerald-400 overflow-x-auto"># one line — creates an empty file and closes it immediately
open("modules/__init__.py", "w").close()</pre>
                    </div>
                  </div>
                </div>

                <!-- Tip callout — amber -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-amber-50 border border-amber-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-amber-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Python 3.3+ note:</strong> Modern Python sometimes allows imports without <code class="text-xs font-mono px-1 py-0.5 rounded bg-amber-100 text-amber-800">__init__.py</code> through a feature called <em>namespace packages</em>. Even so, always creating it is best practice — it makes your intention clear and prevents subtle import errors that can be very hard to trace.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 4 -->

        </div><!-- /panels -->"""

# ═══════════════════════════════════════════════════════════════════════════════
# CHANGE 2 — Code Examples body: 3 cohesive panels (one sales_report/ project)
# ═══════════════════════════════════════════════════════════════════════════════
NEW_CE_BODY = """\
<div class="bg-white px-8 py-7 space-y-6">

<!-- ── Project context callout ──────────────────────────────── -->
<div class="rounded-xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-4 flex items-start gap-3">
  <span class="iconify text-brand text-base shrink-0 mt-0.5" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600"><strong class="text-gray-800">These three examples form one project.</strong> Step through them in order and you will have a working <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-pink-100 text-pink-800">sales_report/</code> project — folders set up, a reusable module written, and a pipeline that runs from a single command.</p>
</div>

<!-- ── Tab pill row ─────────────────────────────────────────── -->
<div class="flex flex-wrap items-center gap-2 mb-2" role="tablist">

  <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:folder-plus"></span>
    <span class="ce-step-label text-xs font-bold">1 · Set Up the Project</span>
  </button>

  <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:file-code"></span>
    <span class="ce-step-label text-xs font-bold">2 · Write the Module</span>
  </button>

  <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:play"></span>
    <span class="ce-step-label text-xs font-bold">3 · Run the Pipeline</span>
  </button>

</div>

<!-- ════════════════════════════════════════════════════════════ -->
<!-- Panel 1 — Set Up the Project (visible)                      -->
<!-- ════════════════════════════════════════════════════════════ -->
<div class="ce-panel ce-panel-anim" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:folder-plus"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Set Up the Project</h3>
          <div class="flex flex-wrap items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">os.makedirs()</span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">__init__.py</span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Project Setup</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <!-- What This Does -->
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">This script creates the standard <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">sales_report/</code> folder structure using Python's built-in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">os</code> module, then creates the empty <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">modules/__init__.py</code> file that tells Python the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">modules/</code> folder is a package. Run it once before you write any analysis code.</p>
        </div>
      </div>

      <!-- Code block -->
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
            <span class="iconify text-yellow-400" data-icon="logos:python" data-width="12" data-height="12"></span>
            <span class="text-[11px] font-semibold text-gray-400">setup_project.py</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import os                                          # os gives Python access to the file system

# ── Step 1: create the folder structure ─────────────────────────────────────
os.makedirs("data/raw",       exist_ok=True)       # source files live here — never overwrite them
os.makedirs("data/processed", exist_ok=True)       # output files from your scripts go here
os.makedirs("modules",        exist_ok=True)       # one .py file per task (cleaning, reports…)

# ── Step 2: create modules/__init__.py ──────────────────────────────────────
# This empty file tells Python that modules/ is a "package" you can import from.
# Without it, "from modules.cleaning import …" raises a ModuleNotFoundError.
open("modules/__init__.py", "w").close()           # create the file — always leave it empty

# ── Step 3: confirm what was created ────────────────────────────────────────
print("Project ready. Your folder structure is now:")
print("")
print("  sales_report/")
print("  ├── data/")
print("  │   ├── raw/            ← put source files here")
print("  │   └── processed/      ← outputs from your scripts go here")
print("  ├── modules/")
print("  │   └── __init__.py     ← marks modules/ as importable")
print("  └── setup_project.py")</code></pre>
        </div>

        <!-- Terminal output -->
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">$ python setup_project.py</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">
            Project ready. Your folder structure is now:<br>
            <br>
            &nbsp;&nbsp;sales_report/<br>
            &nbsp;&nbsp;├── data/<br>
            &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── raw/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;← put source files here<br>
            &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── processed/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;← outputs from your scripts go here<br>
            &nbsp;&nbsp;├── modules/<br>
            &nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── __init__.py&nbsp;&nbsp;&nbsp;&nbsp; ← marks modules/ as importable<br>
            &nbsp;&nbsp;└── setup_project.py
          </div>
        </div>
      </div>

      <!-- Tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">exist_ok=True</code> means the script is safe to re-run — Python won't raise an error if a folder already exists. Add a new folder path any time your project grows.</p>
      </div>

    </div>
  </div>
</div><!-- /panel 1 -->

<!-- ════════════════════════════════════════════════════════════ -->
<!-- Panel 2 — Write the Cleaning Module (hidden)                -->
<!-- ════════════════════════════════════════════════════════════ -->
<div class="ce-panel ce-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:file-code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Write the Cleaning Module</h3>
          <div class="flex flex-wrap items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">def</span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">return</span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">modules/cleaning.py</span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">if __name__</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <!-- What This Does -->
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">This file defines a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">clean_sales()</code> function and saves it inside <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">modules/</code> as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">cleaning.py</code>. The function removes blank rows from a list of sales records. Because it lives in a module, any other script in the project can import and reuse it without copy-pasting.</p>
        </div>
      </div>

      <!-- Code block -->
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
            <span class="iconify text-yellow-400" data-icon="logos:python" data-width="12" data-height="12"></span>
            <span class="text-[11px] font-semibold text-gray-400">modules/cleaning.py</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python"># modules/cleaning.py
# Purpose: remove blank rows from a list of sales records.
# This file is a MODULE — import it; do not run it directly.


def clean_sales(raw_data):
    # Removes any row where the salesperson name or amount is blank.

    clean = []                                     # start with an empty results list

    for row in raw_data:                           # loop through every row in the raw list
        salesperson, amount = row                  # unpack each row into two variables

        if salesperson == "" or amount == "":      # if either field is blank …
            continue                               # … skip this row entirely

        clean.append([salesperson, int(amount)])   # convert amount to a number and keep the row

    return clean                                   # hand the cleaned list back to the caller


# ── Built-in self-test ───────────────────────────────────────────────────────
# The block below only runs when you open THIS file directly (python modules/cleaning.py).
# It is silently ignored when another script imports clean_sales.
if __name__ == "__main__":
    sample = [
        ["Alice", 150],    # valid row
        ["",      ""],     # blank row — should be removed
        ["Bob",   220],    # valid row
    ]
    result = clean_sales(sample)
    print("Self-test passed:", result)             # expected: [['Alice', 150], ['Bob', 220]]</code></pre>
        </div>

        <!-- Terminal output -->
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">$ python modules/cleaning.py</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">Self-test passed: [['Alice', 150], ['Bob', 220]]</div>
        </div>
      </div>

      <!-- if __name__ callout -->
      <div class="rounded-xl border border-violet-100 bg-violet-50/40 px-4 py-3 flex items-start gap-3">
        <span class="iconify text-violet-500 text-base shrink-0 mt-0.5" data-icon="fa6-solid:circle-question"></span>
        <div>
          <p class="text-xs font-bold text-violet-700 mb-1">What does <code class="font-mono">if __name__ == "__main__":</code> mean?</p>
          <p class="text-xs text-gray-600">Every Python file has a built-in variable called <code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">__name__</code>. When you <em>run</em> a file directly, Python sets it to <code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">"__main__"</code>. When another script <em>imports</em> the file, Python sets it to the module's own name instead. This guard lets you put test code at the bottom of a module — it runs when you open the file for a quick check, but stays silent when the module is imported by <code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">main.py</code>.</p>
        </div>
      </div>

      <!-- Tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Keep every module focused on <strong>one type of task</strong>. If you find yourself adding a "calculate" function to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">cleaning.py</code>, that's a sign the calculation belongs in a separate <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">calculations.py</code> module instead.</p>
      </div>

    </div>
  </div>
</div><!-- /panel 2 -->

<!-- ════════════════════════════════════════════════════════════ -->
<!-- Panel 3 — Run the Full Pipeline (hidden)                    -->
<!-- ════════════════════════════════════════════════════════════ -->
<div class="ce-panel ce-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:play"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Run the Full Pipeline</h3>
          <div class="flex flex-wrap items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">from … import</span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">main.py</span>
            <span class="inline-flex text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Pipeline</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <!-- What This Does -->
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">This is <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">main.py</code> — the entry point for the whole project. It imports <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">clean_sales</code> from the module you wrote in Step 2, runs it on raw sales records, calculates a total, and prints a formatted report. This is the only file you ever need to run.</p>
        </div>
      </div>

      <!-- Code block -->
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
            <span class="iconify text-yellow-400" data-icon="logos:python" data-width="12" data-height="12"></span>
            <span class="text-[11px] font-semibold text-gray-400">main.py</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python"># main.py — the entry point for the whole project.
# Run this file: python main.py

from modules.cleaning import clean_sales           # import our reusable cleaning function

# ── Step 1: raw data ─────────────────────────────────────────────────────────
# In a real project this might be read from data/raw/sales.csv.
# Here we define it inline so you can run this example without any extra files.
raw_data = [
    ["Alice",  150],    # valid row
    ["",       ""],     # blank row — will be removed by clean_sales
    ["Bob",    220],    # valid row
    ["Carol",  190],    # valid row
    ["",       ""],     # another blank row — will be removed
    ["Dave",   310],    # valid row
]

# ── Step 2: clean the data ───────────────────────────────────────────────────
cleaned = clean_sales(raw_data)                    # remove blanks using the module

# ── Step 3: calculate the total ──────────────────────────────────────────────
total = sum(row[1] for row in cleaned)             # add up every amount in the cleaned list

# ── Step 4: print the sales report ───────────────────────────────────────────
print("=" * 30)
print("  SALES REPORT")
print("=" * 30)
for row in cleaned:
    name, amount = row                             # unpack each cleaned row
    print(f"  {name:<10}  ${amount:>6}")           # align names left, amounts right
print("-" * 30)
print(f"  {'TOTAL':<10}  ${total:>6}")             # print the grand total
print("=" * 30)
print(f"\n{len(raw_data) - len(cleaned)} blank row(s) removed.")  # report how many rows were dropped</code></pre>
        </div>

        <!-- Terminal output -->
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">$ python main.py</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">
            ==============================<br>
            &nbsp;&nbsp;SALES REPORT<br>
            ==============================<br>
            &nbsp;&nbsp;Alice&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$&nbsp;&nbsp;&nbsp;150<br>
            &nbsp;&nbsp;Bob&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$&nbsp;&nbsp;&nbsp;220<br>
            &nbsp;&nbsp;Carol&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$&nbsp;&nbsp;&nbsp;190<br>
            &nbsp;&nbsp;Dave&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$&nbsp;&nbsp;&nbsp;310<br>
            ------------------------------<br>
            &nbsp;&nbsp;TOTAL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$&nbsp;&nbsp;&nbsp;870<br>
            ==============================<br>
            <br>
            2 blank row(s) removed.
          </div>
        </div>
      </div>

      <!-- Tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Notice that <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">main.py</code> has no cleaning logic of its own — it just calls the module. If the cleaning rules ever change, you update <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">modules/cleaning.py</code> once and every script that imports it gets the fix automatically.</p>
      </div>

    </div>
  </div>
</div><!-- /panel 3 -->

</div>"""


def main():
    html = TARGET.read_text(encoding="utf-8")
    original_len = len(html)

    # ── Change 1A: insert 5th kc-tab button ─────────────────────────────────
    assert OLD_KC_BTN in html, "ERROR: KC tab button anchor not found"
    html = html.replace(OLD_KC_BTN, NEW_KC_BTN, 1)
    print("✅  KC tab button inserted (5th tab: __init__.py)")

    # ── Change 1B: insert 5th kc-panel ──────────────────────────────────────
    assert OLD_KC_PANEL_END in html, "ERROR: KC panel end anchor not found"
    html = html.replace(OLD_KC_PANEL_END, NEW_KC_PANEL_END, 1)
    print("✅  KC panel inserted (panel 4: __init__.py)")

    # ── Change 2: replace code-examples body ────────────────────────────────
    ce_start      = html.index('id="code-examples"')
    ce_start      = html.rindex("<section", 0, ce_start)
    ce_end        = html.index("</section>", ce_start) + len("</section>")

    body_marker   = '<div class="bg-white px-8 py-7 space-y-6">'
    body_open_pos = html.index(body_marker, ce_start)

    closing       = "\n  </div>\n</section>"
    closing_pos   = html.rindex(closing, body_open_pos, ce_end)

    old_body      = html[body_open_pos:closing_pos]
    html          = html[:body_open_pos] + NEW_CE_BODY + html[closing_pos:]
    print(f"✅  Code Examples body replaced  ({len(old_body):,} → {len(NEW_CE_BODY):,} chars)")

    TARGET.write_text(html, encoding="utf-8")
    print(f"\nFile size: {original_len:,} → {len(html):,} chars")


if __name__ == "__main__":
    main()
