"""Simplify the three Code Examples panels — shorter, cleaner code blocks.

Panel 1: setup_project.py        → 8 lines
Panel 2: modules/cleaning.py     → 7 lines, remove if-__name__ guard + callout
Panel 3: main.py                 → 8 lines, remove formatted SALES REPORT
"""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

# ─── Panel 1: code block ────────────────────────────────────────────────────
OLD_P1_CODE = (
    '        <div class="bg-code">\n'
    '          <pre class="overflow-x-auto pre-reset">'
    '<code class="language-python">import os                                          '
    '# os gives Python access to the file system\n'
    '\n'
    '# \u2500\u2500 Step 1: create the folder structure \u2500'
)
NEW_P1_CODE_FULL = (
    '        <div class="bg-code">\n'
    '          <pre class="overflow-x-auto pre-reset">'
    '<code class="language-python">import os\n'
    '\n'
    'os.makedirs("data/raw",       exist_ok=True)  '
    '# folder for raw source files\n'
    'os.makedirs("data/processed", exist_ok=True)  '
    '# folder for cleaned output files\n'
    'os.makedirs("modules",        exist_ok=True)  '
    '# folder for your reusable scripts\n'
    '\n'
    'open("modules/__init__.py", "w").close()      '
    '# marks modules/ as importable\n'
    '\n'
    'print("Folders created!")</code></pre>\n'
    '        </div>'
)

# ─── Panel 1: terminal ──────────────────────────────────────────────────────
OLD_P1_TERM = (
    '          <div class="font-mono text-xs text-emerald-400 leading-relaxed">\n'
    '            Project ready. Your folder structure is now:<br>'
)
NEW_P1_TERM = (
    '          <div class="font-mono text-xs text-emerald-400 leading-relaxed">'
    'Folders created!</div>'
)
# We need to close the old terminal div too — find the old block end
OLD_P1_TERM_END = '          </div>\n        </div>\n      </div>\n\n      <!-- Tip -->'
NEW_P1_TERM_END = '\n        </div>\n      </div>\n\n      <!-- Tip -->'

# ─── Panel 2: "What This Does" ──────────────────────────────────────────────
OLD_P2_WTD = (
    '          <p class="text-sm text-gray-600">This file defines a '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'clean_sales()</code> function'
)
NEW_P2_WTD = (
    '          <p class="text-sm text-gray-600">This file defines a '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'remove_blanks()</code> function and saves it as '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'modules/cleaning.py</code>. Any script in your project can import and call it '
    '\u2014 you only ever write the logic once.</p>'
)
OLD_P2_WTD_END = (
    ' function and saves it inside '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'modules/</code> as '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'cleaning.py</code>. The function removes blank rows from a list of sales records. '
    'Because it lives in a module, any other script in the project can import and reuse it '
    'without copy-pasting.</p>'
)

# ─── Panel 2: code block ────────────────────────────────────────────────────
OLD_P2_CODE_START = (
    '        <div class="bg-code">\n'
    '          <pre class="overflow-x-auto pre-reset">'
    '<code class="language-python"># modules/cleaning.py\n'
    '# Purpose: remove blank rows'
)
OLD_P2_CODE_END = (
    "    print(\"Self-test passed:\", result)             "
    "# expected: [['Alice', 150], ['Bob', 220]]</code></pre>\n"
    '        </div>'
)
NEW_P2_CODE_FULL = (
    '        <div class="bg-code">\n'
    '          <pre class="overflow-x-auto pre-reset">'
    '<code class="language-python"># modules/cleaning.py \u2014 save this inside the modules/ folder\n'
    '\n'
    'def remove_blanks(names):\n'
    '    result = []\n'
    '    for name in names:\n'
    '        if name != "":         # skip any blank entry\n'
    '            result.append(name)\n'
    '    return result</code></pre>\n'
    '        </div>'
)

# ─── Panel 2: terminal ──────────────────────────────────────────────────────
OLD_P2_TERM = (
    '          <div class="font-mono text-xs text-emerald-400 leading-relaxed">'
    "Self-test passed: [['Alice', 150], ['Bob', 220]]</div>"
)
NEW_P2_TERM = (
    '          <div class="font-mono text-xs text-gray-500 leading-relaxed italic">'
    'No output \u2014 modules just define functions. The result appears in Step\u00a03 '
    'when main.py imports this file.</div>'
)

# ─── Panel 2: remove if-__name__ callout box ────────────────────────────────
OLD_P2_CALLOUT = (
    '      <!-- if __name__ callout -->\n'
    '      <div class="rounded-xl border border-violet-100 bg-violet-50/40 '
    'px-4 py-3 flex items-start gap-3">\n'
    '        <span class="iconify text-violet-500 text-base shrink-0 mt-0.5" '
    'data-icon="fa6-solid:circle-question"></span>\n'
    '        <div>\n'
)
OLD_P2_CALLOUT_END = (
    '          <p class="text-xs text-gray-600">Every Python file has a built-in variable called '
    '<code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">'
    '__name__</code>. When you <em>run</em> a file directly, Python sets it to '
    '<code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">'
    '"__main__"</code>. When another script <em>imports</em> the file, Python sets it to the '
    "module's own name instead. This guard lets you put test code at the bottom of a module "
    '\u2014 it runs when you open the file for a quick check, but stays silent when the module is '
    'imported by <code class="text-xs font-mono px-1 py-0.5 rounded bg-violet-100 text-violet-700">'
    'main.py</code>.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '\n'
    '      <!-- Tip -->'
)

# ─── Panel 2: tip ───────────────────────────────────────────────────────────
OLD_P2_TIP = (
    '        <p class="text-sm text-gray-600">Keep every module focused on '
    '<strong>one type of task</strong>. If you find yourself adding a '
    '"calculate" function to '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    "cleaning.py</code>, that's a sign the calculation belongs in a separate "
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    'calculations.py</code> module instead.</p>'
)
NEW_P2_TIP = (
    '        <p class="text-sm text-gray-600">Give each module one job. If '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    'cleaning.py</code> starts doing calculations too, move that logic to a separate '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    'calculations.py</code> file.</p>'
)

# ─── Panel 3: "What This Does" ──────────────────────────────────────────────
OLD_P3_WTD = (
    '          <p class="text-sm text-gray-600">This is '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'main.py</code> \u2014 the entry point for the whole project. It imports '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'clean_sales</code> from the module you wrote in Step 2, runs it on raw sales records, '
    'calculates a total, and prints a formatted report. This is the only file you ever need to run.</p>'
)
NEW_P3_WTD = (
    '          <p class="text-sm text-gray-600">This is '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'main.py</code> \u2014 the only file you run. It imports '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">'
    'remove_blanks</code> from the module you created in Step\u00a02 and calls it on a '
    'short list of names. You can see the module doing its job in the output below.</p>'
)

# ─── Panel 3: tip ───────────────────────────────────────────────────────────
OLD_P3_TIP = (
    '        <p class="text-sm text-gray-600">Notice that '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    'main.py</code> has no cleaning logic of its own \u2014 it just calls the module. If the '
    'cleaning rules ever change, you update '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    'modules/cleaning.py</code> once and every script that imports it gets the fix automatically.</p>'
)
NEW_P3_TIP = (
    '        <p class="text-sm text-gray-600">'
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    'main.py</code> contains no cleaning logic \u2014 it just calls the module. If you change '
    'the rules in '
    '<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">'
    'modules/cleaning.py</code>, every script that imports it gets the update automatically.</p>'
)

# ─── Panel 3 terminal output ────────────────────────────────────────────────
OLD_P3_TERM_START = (
    '          <div class="font-mono text-xs text-emerald-400 leading-relaxed">\n'
    '            ==============================<br>'
)
OLD_P3_TERM_END = (
    '\n'
    '            2 blank row(s) removed.\n'
    '          </div>'
)
NEW_P3_TERM = (
    '          <div class="font-mono text-xs text-emerald-400 leading-relaxed">'
    "Clean list: ['Alice', 'Bob', 'Carol']<br>Count: 3</div>"
)

# ─── New Panel 3 code block (full replacement via position) ─────────────────
NEW_P3_CODE_BLOCK = (
    '        <div class="bg-code">\n'
    '          <pre class="overflow-x-auto pre-reset">'
    '<code class="language-python"># main.py \u2014 run this file: python main.py\n'
    '\n'
    'from modules.cleaning import remove_blanks  '
    '# import the function from our module\n'
    '\n'
    'names = ["Alice", "", "Bob", "", "Carol"]   '
    '# raw list \u2014 some entries are blank\n'
    '\n'
    'clean = remove_blanks(names)               '
    '# remove the blanks using the module\n'
    '\n'
    'print("Clean list:", clean)                '
    '# show the result\n'
    'print("Count:", len(clean))                '
    '# how many names remain</code></pre>\n'
    '        </div>'
)


def main():
    html = TARGET.read_text(encoding="utf-8")
    original_len = len(html)

    # Locate the code-examples section boundaries
    ce_marker  = html.index('id="code-examples"')
    ce_sec_start = html.rindex("<section", 0, ce_marker)
    ce_sec_end   = html.index("</section>", ce_marker) + len("</section>")

    # ── Panel 1: replace code block (find by unique start, replace through end tag) ──
    p1_code_start = html.index(OLD_P1_CODE, ce_sec_start, ce_sec_end)
    p1_code_end   = html.index('</div>', p1_code_start + len(OLD_P1_CODE))
    # OLD ends at the closing </div> of bg-code div — find it properly
    # Simpler: find the code block end pattern after the start
    code_end_tag = '</code></pre>\n        </div>'
    p1_code_close = html.index(code_end_tag, p1_code_start) + len(code_end_tag)
    html = html[:p1_code_start] + NEW_P1_CODE_FULL + html[p1_code_close:]
    print("  ✅  Panel 1 code block")

    # Refresh section end after edit
    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 1: replace terminal output ──────────────────────────────────────
    p1_term_start = html.index(OLD_P1_TERM, ce_sec_start, ce_sec_end)
    # Find the closing </div> of the terminal font div
    p1_term_close = html.index('</div>\n        </div>\n      </div>\n\n      <!-- Tip -->',
                                p1_term_start)
    p1_term_close += len('</div>\n        </div>\n      </div>')
    html = html[:p1_term_start] + NEW_P1_TERM + '\n        </div>\n      </div>' + html[p1_term_close:]
    print("  ✅  Panel 1 terminal")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 2: WTD paragraph — replace from start to end ────────────────────
    p2_wtd_start = html.index(OLD_P2_WTD, ce_sec_start, ce_sec_end)
    p2_wtd_end   = html.index(OLD_P2_WTD_END, p2_wtd_start) + len(OLD_P2_WTD_END)
    html = html[:p2_wtd_start] + NEW_P2_WTD + html[p2_wtd_end:]
    print("  ✅  Panel 2 WTD")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 2: code block — replace from unique start to close tag ──────────
    p2_code_start = html.index(OLD_P2_CODE_START, ce_sec_start, ce_sec_end)
    p2_code_end   = html.index(OLD_P2_CODE_END, p2_code_start) + len(OLD_P2_CODE_END)
    html = html[:p2_code_start] + NEW_P2_CODE_FULL + html[p2_code_end:]
    print("  ✅  Panel 2 code block")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 2: terminal ──────────────────────────────────────────────────────
    assert OLD_P2_TERM in html, "ERROR: P2 terminal anchor not found"
    html = html.replace(OLD_P2_TERM, NEW_P2_TERM, 1)
    print("  ✅  Panel 2 terminal")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 2: remove if-__name__ callout box ───────────────────────────────
    p2_callout_start = html.index(OLD_P2_CALLOUT, ce_sec_start, ce_sec_end)
    p2_callout_end   = html.index(OLD_P2_CALLOUT_END, p2_callout_start) + len(OLD_P2_CALLOUT_END)
    html = html[:p2_callout_start] + '\n      <!-- Tip -->' + html[p2_callout_end:]
    print("  ✅  Panel 2 callout removed")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 2: tip ──────────────────────────────────────────────────────────
    assert OLD_P2_TIP in html, "ERROR: P2 tip anchor not found"
    html = html.replace(OLD_P2_TIP, NEW_P2_TIP, 1)
    print("  ✅  Panel 2 tip")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 3: WTD paragraph ────────────────────────────────────────────────
    assert OLD_P3_WTD in html, "ERROR: P3 WTD anchor not found"
    html = html.replace(OLD_P3_WTD, NEW_P3_WTD, 1)
    print("  ✅  Panel 3 WTD")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 3: code block — position-based (find 3rd ce-panel) ─────────────
    # Find Panel 3's start (3rd ce-panel, which is the 2nd "hidden" one)
    p3_start = html.index('<!-- /panel 2 -->', ce_sec_start, ce_sec_end)
    # Within panel 3, find the bg-code div start
    p3_bgcode_start = html.index('<div class="bg-code">', p3_start, ce_sec_end)
    # Find its closing </div> by scanning for </code></pre>\n        </div>
    p3_bgcode_end   = html.index('</code></pre>\n        </div>', p3_bgcode_start, ce_sec_end)
    p3_bgcode_end  += len('</code></pre>\n        </div>')
    html = html[:p3_bgcode_start] + NEW_P3_CODE_BLOCK + html[p3_bgcode_end:]
    print("  ✅  Panel 3 code block")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 3: terminal — position-based ────────────────────────────────────
    p3_term_start = html.index(OLD_P3_TERM_START, p3_start, ce_sec_end)
    p3_term_end   = html.index(OLD_P3_TERM_END, p3_term_start) + len(OLD_P3_TERM_END)
    html = html[:p3_term_start] + NEW_P3_TERM + html[p3_term_end:]
    print("  ✅  Panel 3 terminal")

    ce_sec_end = html.index("</section>", html.index('id="code-examples"')) + len("</section>")

    # ── Panel 3: tip ──────────────────────────────────────────────────────────
    assert OLD_P3_TIP in html, "ERROR: P3 tip anchor not found"
    html = html.replace(OLD_P3_TIP, NEW_P3_TIP, 1)
    print("  ✅  Panel 3 tip")

    TARGET.write_text(html, encoding="utf-8")
    print(f"\nFile size: {original_len:,} → {len(html):,} chars")


if __name__ == "__main__":
    main()
