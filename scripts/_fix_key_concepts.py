"""Replace the 3 kc-panel bodies in the Key Concepts section.
Keeps the outer tab shell, section header, and sidebar tabs untouched.
Only the inner panel content is replaced.
"""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson01_what_is_programming.html"

# ── Panel 1: Instruction ──────────────────────────────────────────────────────
OLD_P1 = '''      <div class="space-y-3 mb-4"><p class="text-xs text-gray-600 leading-relaxed">An instruction is a command given to a computer.</p>
<p class="text-xs text-gray-600 leading-relaxed">Example:</p></div>
      <div class="space-y-3"><div class="rounded-xl overflow-hidden bg-code">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Python</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-python">print(&quot;Hello&quot;)</code></pre>
</div>
</div>'''

NEW_P1 = '''      <!-- Definition row -->
      <p class="text-xs text-gray-600 leading-relaxed mb-3">An <strong>instruction</strong> is a single command you give to a computer — one specific action it should perform right now. Every program is made up of instructions executed one after another.</p>

      <!-- You already know this -->
      <div class="flex items-start gap-3 rounded-xl bg-amber-50 border border-amber-100 px-4 py-3 mb-4">
        <span class="iconify text-amber-400 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:lightbulb"></span>
        <p class="text-xs text-gray-600 leading-relaxed">You already do this in Excel: <code class="bg-gray-100 px-1 rounded text-[11px]">=SUM(A1:A10)</code> is an instruction that tells Excel to add up a column. In Python, you write instructions using plain words instead of formula syntax.</p>
      </div>

      <!-- Code example -->
      <p class="text-[11px] font-semibold text-gray-500 uppercase tracking-wider mb-2">Python instruction — one line, one action:</p>
      <div class="rounded-xl overflow-hidden bg-code mb-3">
        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
          <div class="flex items-center gap-2">
            <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
            <span class="text-[11px] font-semibold text-gray-400">Python</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <pre class="overflow-x-auto pre-reset"><code class="language-python">print("Hello, world!")   # This is one instruction — display text on screen</code></pre>
      </div>

      <!-- Key point -->
      <div class="flex items-start gap-2 rounded-lg bg-pink-50 border border-pink-100 px-3 py-2.5">
        <span class="iconify text-[#CB187D] text-xs mt-0.5 shrink-0" data-icon="fa6-solid:circle-check"></span>
        <p class="text-[11px] text-gray-600 leading-relaxed">One instruction = one action. Python runs it immediately when the line is reached — no button clicks, no pressing Enter in a cell.</p>
      </div>'''

# ── Panel 2: Program ─────────────────────────────────────────────────────────
OLD_P2 = '''      <div class="space-y-3 mb-4"><p class="text-xs text-gray-600 leading-relaxed">A program is a collection of instructions.</p>
<p class="text-xs text-gray-600 leading-relaxed">Example program:</p></div>
      <div class="space-y-3"><div class="rounded-xl overflow-hidden bg-code">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Python</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-python">print(&quot;Loading data&quot;)
print(&quot;Calculating results&quot;)
print(&quot;Process complete&quot;)</code></pre>
</div>
</div>'''

NEW_P2 = '''      <!-- Definition -->
      <p class="text-xs text-gray-600 leading-relaxed mb-3">A <strong>program</strong> is a complete set of instructions that work together to accomplish a task. While a single instruction does one thing, a program chains many instructions into a workflow — carried out in order, from the first line to the last.</p>

      <!-- SQL comparison -->
      <div class="flex items-start gap-3 rounded-xl bg-violet-50 border border-violet-100 px-4 py-3 mb-4">
        <span class="iconify text-violet-500 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:database"></span>
        <p class="text-xs text-gray-600 leading-relaxed">In SQL, each query is a separate action. A Python program replaces a whole sequence of queries — load the data, clean it, calculate totals, and export the result — all in one automated run.</p>
      </div>

      <!-- Code example with inline comments -->
      <p class="text-[11px] font-semibold text-gray-500 uppercase tracking-wider mb-2">A simple 3-step program:</p>
      <div class="rounded-xl overflow-hidden bg-code mb-3">
        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
          <div class="flex items-center gap-2">
            <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
            <span class="text-[11px] font-semibold text-gray-400">Python</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <pre class="overflow-x-auto pre-reset"><code class="language-python">print("Step 1: Loading data...")       # instruction 1
print("Step 2: Calculating totals...")  # instruction 2
print("Step 3: Export complete.")       # instruction 3</code></pre>
      </div>

      <!-- Flow indicator -->
      <div class="flex items-center gap-2 flex-wrap">
        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">
          <span class="iconify text-[10px]" data-icon="fa6-solid:1"></span> Line 1 runs first
        </span>
        <span class="iconify text-gray-300 text-xs" data-icon="fa6-solid:arrow-right"></span>
        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">
          <span class="iconify text-[10px]" data-icon="fa6-solid:2"></span> Then line 2
        </span>
        <span class="iconify text-gray-300 text-xs" data-icon="fa6-solid:arrow-right"></span>
        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">
          <span class="iconify text-[10px]" data-icon="fa6-solid:3"></span> Then line 3
        </span>
      </div>'''

# ── Panel 3: Programming Language ────────────────────────────────────────────
OLD_P3 = '''      <div class="space-y-3 mb-4"><p class="text-xs text-gray-600 leading-relaxed">A programming language is the system used to write instructions.</p>
<p class="text-xs text-gray-600 leading-relaxed">Examples:</p></div>
      <div class="space-y-3"><div class="overflow-x-auto rounded-xl border border-gray-100">
<table class="w-full text-sm">
<thead>
<tr class="bg-gray-50">
  <th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs uppercase tracking-wider">Language</th>
  <th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs uppercase tracking-wider">Common Use</th>
</tr>
</thead>
<tbody>
<tr class="border-t border-gray-100 hover:bg-gray-50">
  <td class="px-4 py-3 text-gray-600">Python</td>
  <td class="px-4 py-3 text-gray-600">automation, analytics</td>
</tr>
<tr class="border-t border-gray-100 hover:bg-gray-50">
  <td class="px-4 py-3 text-gray-600">SQL</td>
  <td class="px-4 py-3 text-gray-600">querying databases</td>
</tr>
<tr class="border-t border-gray-100 hover:bg-gray-50">
  <td class="px-4 py-3 text-gray-600">JavaScript</td>
  <td class="px-4 py-3 text-gray-600">web development</td>
</tr>
<tr class="border-t border-gray-100 hover:bg-gray-50">
  <td class="px-4 py-3 text-gray-600">R</td>
  <td class="px-4 py-3 text-gray-600">statistical analysis</td>
</tr>
</tbody>
</table>
</div>
</div>'''

NEW_P3 = '''      <!-- Definition -->
      <p class="text-xs text-gray-600 leading-relaxed mb-3">A <strong>programming language</strong> is a set of rules and vocabulary that lets you write instructions a computer can understand. Think of it like a spoken language — French, Spanish, Mandarin all express ideas, but each has its own grammar. Python, SQL, and JavaScript are all programming languages, each with its own syntax for different jobs.</p>

      <!-- Why Python -->
      <div class="flex items-start gap-3 rounded-xl bg-blue-50 border border-blue-100 px-4 py-3 mb-4">
        <span class="iconify text-blue-500 mt-0.5 shrink-0 text-sm" data-icon="fa6-solid:star"></span>
        <p class="text-xs text-gray-600 leading-relaxed">Python was designed to read like plain English. You don't need semicolons, curly braces, or special symbols to end a line — which makes it the most beginner-friendly language for data work.</p>
      </div>

      <!-- Comparison table — improved -->
      <p class="text-[11px] font-semibold text-gray-500 uppercase tracking-wider mb-2">How Python compares to tools you already use:</p>
      <div class="overflow-x-auto rounded-xl border border-gray-100 mb-3">
        <table class="w-full text-sm">
          <thead>
            <tr class="bg-gray-50">
              <th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs uppercase tracking-wider">Tool</th>
              <th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs uppercase tracking-wider">What it does well</th>
              <th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs uppercase tracking-wider">Where Python goes further</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-t border-gray-100 hover:bg-gray-50">
              <td class="px-4 py-3"><span class="inline-flex items-center gap-1.5 font-semibold text-gray-700 text-xs"><span class="iconify text-emerald-500 text-sm" data-icon="fa6-solid:table"></span>Excel</span></td>
              <td class="px-4 py-3 text-xs text-gray-500">Formulas, pivot tables, charts</td>
              <td class="px-4 py-3 text-xs text-gray-500">Automates multi-step workflows across many files</td>
            </tr>
            <tr class="border-t border-gray-100 hover:bg-gray-50">
              <td class="px-4 py-3"><span class="inline-flex items-center gap-1.5 font-semibold text-gray-700 text-xs"><span class="iconify text-blue-500 text-sm" data-icon="fa6-solid:database"></span>SQL</span></td>
              <td class="px-4 py-3 text-xs text-gray-500">Querying and filtering data in databases</td>
              <td class="px-4 py-3 text-xs text-gray-500">Adds logic, loops, and file handling around queries</td>
            </tr>
            <tr class="border-t border-gray-100 hover:bg-gray-50">
              <td class="px-4 py-3"><span class="inline-flex items-center gap-1.5 font-semibold text-[#CB187D] text-xs"><span class="iconify text-[#CB187D] text-sm" data-icon="logos:python"></span>Python</span></td>
              <td class="px-4 py-3 text-xs text-gray-500">Automation, data analysis, scripting</td>
              <td class="px-4 py-3 text-xs text-[#CB187D] font-medium">End-to-end workflows that no single tool can match alone</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Reminder -->
      <div class="flex items-start gap-2 rounded-lg bg-blue-50 border border-blue-100 px-3 py-2.5">
        <span class="iconify text-blue-500 text-xs mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-[11px] text-gray-600 leading-relaxed">You don't need to learn every programming language. Python is the right starting point for data and automation — it works equally well alongside SQL and Excel rather than replacing them.</p>
      </div>'''

# ── Run ───────────────────────────────────────────────────────────────────────
with open(TARGET, "r", encoding="utf-8") as f:
    src = f.read()

results = []
for label, old, new in [("Panel 1 (Instruction)", OLD_P1, NEW_P1),
                         ("Panel 2 (Program)",     OLD_P2, NEW_P2),
                         ("Panel 3 (Prog.Lang.)",  OLD_P3, NEW_P3)]:
    if old in src:
        src = src.replace(old, new, 1)
        results.append(f"✅ {label}")
    else:
        results.append(f"❌ {label} — marker not found")

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(src)

for r in results:
    print(r)
