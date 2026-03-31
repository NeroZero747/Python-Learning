"""Simplify the three Code Examples panels — shorter, cleaner code blocks.

Panel 1: setup_project.py        → 8 lines
Panel 2: modules/cleaning.py     → 8 lines, remove if-__name__ guard + callout
Panel 3: main.py                 → 8 lines, remove the formatted SALES REPORT
"""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

# ── Panel 1 code: OLD → NEW ──────────────────────────────────────────────────
OLD_P1_CODE = """\
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
        </div>"""

NEW_P1_CODE = """\
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import os

os.makedirs("data/raw",       exist_ok=True)  # folder for raw source files
os.makedirs("data/processed", exist_ok=True)  # folder for cleaned output files
os.makedirs("modules",        exist_ok=True)  # folder for your reusable scripts

open("modules/__init__.py", "w").close()      # marks modules/ as importable

print("Folders created!")</code></pre>
        </div>"""

# ── Panel 1 terminal: OLD → NEW ──────────────────────────────────────────────
OLD_P1_TERM = """\
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
          </div>"""

NEW_P1_TERM = """\
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">Folders created!</div>"""

# ── Panel 2 code: OLD → NEW ──────────────────────────────────────────────────
OLD_P2_CODE = """\
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
        </div>"""

NEW_P2_CODE = """\
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python"># modules/cleaning.py — save this file inside the modules/ folder

def remove_blanks(names):
    result = []
    for name in names:
        if name != "":         # skip any blank entry
            result.append(name)
    return result</code></pre>
        </div>"""

# ── Panel 2 terminal: OLD → NEW ──────────────────────────────────────────────
OLD_P2_TERM = """\
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">Self-test passed: [['Alice', 150], ['Bob', 220]]</div>"""

NEW_P2_TERM = """\
          <div class="font-mono text-xs text-gray-500 leading-relaxed italic">No output — modules just define functions. The result appears in Step 3 when main.py imports this file.</div>"""

# ── Panel 2: remove the if-__name__ callout box ──────────────────────────────
OLD_P2_CALLOUT = """\
      <!-- if __name__ callout -->
      <div class="rounded-xl border border-violet-100 bg-violet-50/40 px-4 py-3 flex items-start gap-3">
        <span class="iconify text-violet-500 text-base shrink-0 mt-0.5" data-icon="fa6-solid:circle-question"></span>
        <div>
          <p class="text-xs font-bold text-violet-700 mb-1">What does <code class="font-mono">if __name__ == "__main__":</code> mean?</p>
          <p class="text-xs text-gray-600">Every Python file has a built-in variable called <code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">__name__</code>. When you <em>run</em> a file directly, Python sets it to <code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">"__main__"</code>. When another script <em>imports</em> the file, Python sets it to the module's own name instead. This guard lets you put test code at the bottom of a module — it runs when you open the file for a quick check, but stays silent when the module is imported by <code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">main.py</code>.</p>
        </div>
      </div>

      <!-- Tip -->"""

NEW_P2_CALLOUT = """\
      <!-- Tip -->"""

# ── Panel 2 "What This Does": update to match new function name ───────────────
OLD_P2_WTD = """\
          <p class="text-sm text-gray-600">This file defines a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">clean_sales()</code> function and saves it inside <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">modules/</code> as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">cleaning.py</code>. The function removes blank rows from a list of sales records. Because it lives in a module, any other script in the project can import and reuse it without copy-pasting.</p>"""

NEW_P2_WTD = """\
          <p class="text-sm text-gray-600">This file defines a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">remove_blanks()</code> function and saves it as <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">modules/cleaning.py</code>. Any script in your project can import and call it — you only ever write the logic once.</p>"""

# ── Panel 2 tip: update to match new function name ────────────────────────────
OLD_P2_TIP = """\
        <p class="text-sm text-gray-600">Keep every module focused on <strong>one type of task</strong>. If you find yourself adding a "calculate" function to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">cleaning.py</code>, that's a sign the calculation belongs in a separate <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">calculations.py</code> module instead.</p>"""

NEW_P2_TIP = """\
        <p class="text-sm text-gray-600">Give each module one job. If <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">cleaning.py</code> starts doing calculations too, move that logic to a separate <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">calculations.py</code> file.</p>"""

# ── Panel 3 code: OLD → NEW ──────────────────────────────────────────────────
OLD_P3_CODE = """\
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
print(f"""</code></pre>"""

NEW_P3_CODE = """\
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python"># main.py — run this file: python main.py

from modules.cleaning import remove_blanks  # import the function from our module

names = ["Alice", "", "Bob", "", "Carol"]   # raw list — some entries are blank

clean = remove_blanks(names)               # remove the blanks using the module

print("Clean list:", clean)                # show the result
print("Count:", len(clean))                # how many names remain</code></pre>
        </div>"""

# ── Panel 3 terminal: OLD → NEW ──────────────────────────────────────────────
OLD_P3_TERM = """\
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
          </div>"""

NEW_P3_TERM = """\
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">Clean list: ['Alice', 'Bob', 'Carol']<br>Count: 3</div>"""

# ── Panel 3 "What This Does": simplify ────────────────────────────────────────
OLD_P3_WTD = """\
          <p class="text-sm text-gray-600">This is <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">main.py</code> — the entry point for the whole project. It imports <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">clean_sales</code> from the module you wrote in Step 2, runs it on raw sales records, calculates a total, and prints a formatted report. This is the only file you ever need to run.</p>"""

NEW_P3_WTD = """\
          <p class="text-sm text-gray-600">This is <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">main.py</code> — the only file you run. It imports <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">remove_blanks</code> from the module you created in Step 2 and calls it on a short list of names. You can see the module doing its job in the output below.</p>"""

# ── Panel 3 tip: simplify ─────────────────────────────────────────────────────
OLD_P3_TIP = """\
        <p class="text-sm text-gray-600">Notice that <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">main.py</code> has no cleaning logic of its own — it just calls the module. If the cleaning rules ever change, you update <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">modules/cleaning.py</code> once and every script that imports it gets the fix automatically.</p>"""

NEW_P3_TIP = """\
        <p class="text-sm text-gray-600"><code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">main.py</code> contains no cleaning logic — it just calls the module. If you change the rules in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">modules/cleaning.py</code>, every script that imports it gets the update automatically.</p>"""

# ── Panel 3: find and replace the broken last print line too ─────────────────
# The old script has a literal newline inside an f-string — fix it in the new code above


def apply(html, old, new, label):
    assert old in html, f"ERROR: anchor not found — {label}"
    return html.replace(old, new, 1), label


def main():
    html = TARGET.read_text(encoding="utf-8")

    replacements = [
        (OLD_P1_CODE,     NEW_P1_CODE,     "Panel 1 code"),
        (OLD_P1_TERM,     NEW_P1_TERM,     "Panel 1 terminal"),
        (OLD_P2_CODE,     NEW_P2_CODE,     "Panel 2 code"),
        (OLD_P2_TERM,     NEW_P2_TERM,     "Panel 2 terminal"),
        (OLD_P2_CALLOUT,  NEW_P2_CALLOUT,  "Panel 2 callout removed"),
        (OLD_P2_WTD,      NEW_P2_WTD,      "Panel 2 WTD"),
        (OLD_P2_TIP,      NEW_P2_TIP,      "Panel 2 tip"),
        (OLD_P3_CODE,     NEW_P3_CODE,     "Panel 3 code"),
        (OLD_P3_TERM,     NEW_P3_TERM,     "Panel 3 terminal"),
        (OLD_P3_WTD,      NEW_P3_WTD,      "Panel 3 WTD"),
        (OLD_P3_TIP,      NEW_P3_TIP,      "Panel 3 tip"),
    ]

    original_len = len(html)
    for old, new, label in replacements:
        html, label = apply(html, old, new, label)
        print(f"  ✅  {label}")

    TARGET.write_text(html, encoding="utf-8")
    print(f"\nFile size: {original_len:,} → {len(html):,} chars")


if __name__ == "__main__":
    main()
