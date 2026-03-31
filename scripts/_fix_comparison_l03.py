path = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"
with open(path) as f:
    content = f.read()

COMP_OPEN    = '<section id="comparison">'
PRAC_OPEN    = '<section id="practice">'

comp_idx = content.index(COMP_OPEN)
prac_idx = content.index(PRAC_OPEN)

header_end_marker = '\n    <div class="bg-white px-8 py-7 space-y-5">'
body_start = content.index(header_end_marker, comp_idx)
section_end_marker = '\n\n' + PRAC_OPEN
section_end = content.index(section_end_marker, comp_idx)

print(f"body_start line ~{content[:body_start].count(chr(10))+1}")
print(f"section_end line ~{content[:section_end].count(chr(10))+1}")

new_body = """
    <div class="bg-white px-8 py-7 space-y-5">

      <!-- Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">If you already use SQL or Excel, you will recognise all three concepts in this lesson — SQL has <code class="font-mono text-xs">NULL</code> and <code class="font-mono text-xs">DISTINCT</code>, Excel has blank cells and "Remove Duplicates", and Python expresses the same ideas with <code class="font-mono text-xs">None</code>, sets, and tuples.</p>

      <!-- Tool header cards -->
      <div class="grid grid-cols-3 gap-3">
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel
        </div>
      </div>

      <!-- Row 1: fixed ordered record -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:table-list"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">fixed ordered record</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">tuple</code>
            <p class="text-xs text-gray-500 leading-relaxed">An ordered, unchangeable collection — once you create it, the values and their positions are locked in.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">table row</code>
            <p class="text-xs text-gray-500 leading-relaxed">A row in a table holds a fixed set of columns in a defined order — you can read it but cannot rearrange its column positions.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">named range / row</code>
            <p class="text-xs text-gray-500 leading-relaxed">A named range locks a group of cells together so you can reference them as a unit without worrying about their position changing.</p>
          </div>
        </div>
      </div>

      <!-- Row 2: unique values only -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:filter"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">unique values only</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">set</code>
            <p class="text-xs text-gray-500 leading-relaxed">A collection that automatically keeps only one copy of each value — duplicates are silently dropped the moment you add them.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">SELECT DISTINCT</code>
            <p class="text-xs text-gray-500 leading-relaxed"><code class="font-mono">DISTINCT</code> tells the database to return only one row per unique value, removing any repeated entries from the result set.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Remove Duplicates</code>
            <p class="text-xs text-gray-500 leading-relaxed">The Data &rarr; Remove Duplicates tool deletes rows where every selected column matches an earlier row, leaving one copy of each unique combination.</p>
          </div>
        </div>
      </div>

      <!-- Row 3: missing / absent value -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:ban"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">missing / absent value</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">None</code>
            <p class="text-xs text-gray-500 leading-relaxed">A special value meaning "nothing here yet" — you assign it as a placeholder when a real value has not arrived yet.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">NULL</code>
            <p class="text-xs text-gray-500 leading-relaxed"><code class="font-mono">NULL</code> marks a cell in a table that has no value — you test for it with <code class="font-mono">IS NULL</code>, not with <code class="font-mono">=</code>.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">blank cell / #N/A</code>
            <p class="text-xs text-gray-500 leading-relaxed">An empty cell or <code class="font-mono">#N/A</code> error signals that a value is absent — <code class="font-mono">=ISBLANK()</code> or <code class="font-mono">=ISNA()</code> detects this.</p>
          </div>
        </div>
      </div>

      <!-- Row 4: check whether value is absent -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:magnifying-glass"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">check whether value is absent</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">is None</code>
            <p class="text-xs text-gray-500 leading-relaxed">Use <code class="font-mono">if x is None</code> to safely test whether a variable has been assigned a real value yet.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">IS NULL</code>
            <p class="text-xs text-gray-500 leading-relaxed"><code class="font-mono">WHERE specialty IS NULL</code> filters rows that have no value in the specialty column — the same intent as Python&apos;s <code class="font-mono">is None</code>.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">=ISBLANK()</code>
            <p class="text-xs text-gray-500 leading-relaxed"><code class="font-mono">=ISBLANK(B2)</code> returns TRUE when the cell is empty — the Excel equivalent of checking <code class="font-mono">is None</code>.</p>
          </div>
        </div>
      </div>

      <!-- Centered divider + side-by-side code blocks -->
      <div>
        <div class="flex items-center gap-3 mb-4">
          <span class="flex-1 h-px bg-gray-100"></span>
          <div class="flex items-center gap-2 shrink-0">
            <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
            </span>
            <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">Same duplicate removal, three tools</p>
          </div>
          <span class="flex-1 h-px bg-gray-100"></span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 items-stretch">

          <!-- Python column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Python code</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify" data-icon="logos:python" data-width="16" data-height="16"></span>
                  <span class="text-xs font-semibold text-gray-400">Python</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-python">diagnosis_codes = [&quot;I10&quot;, &quot;Z00.00&quot;, &quot;I10&quot;, &quot;E11.9&quot;]
unique_codes = set(diagnosis_codes)</code></pre>
            </div>
          </div>

          <!-- SQL column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">SQL query</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-orange-400" data-icon="fa6-solid:database"></span>
                  <span class="text-xs font-semibold text-gray-400">SQL</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-sql">SELECT DISTINCT diagnosis_code
FROM claims;</code></pre>
            </div>
          </div>

          <!-- Excel column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Excel formula</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-green-400" data-icon="fa6-solid:table"></span>
                  <span class="text-xs font-semibold text-gray-400">Excel</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-text">Data &rarr; Remove Duplicates
(select Diagnosis Code column)</code></pre>
            </div>
          </div>

        </div>

        <p class="text-xs text-gray-400 mt-2">All three remove duplicate diagnosis codes from a list of claim values — the same result, just written in a different tool.</p>
      </div>

      <!-- Closing amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">The ideas behind tuples, sets, and <code class="font-mono text-xs">None</code> exist in SQL and Excel too — Python just gives them precise names so you can use them intentionally. If you already know how to spot a <code class="font-mono text-xs">NULL</code> or remove duplicates in SQL, you already understand the concept; the only thing new is the Python syntax.</p>
      </div>

    </div>
  </div>
</section>"""

content = content[:body_start] + new_body + content[section_end:]

with open(path, "w") as f:
    f.write(content)

print("Done — comparison section rewritten successfully")
