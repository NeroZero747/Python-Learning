"""
Replace the #mistakes section body in lesson04_efficient_storage_parquet.html
with the new tab-pill design from lesson-common-mistakes.prompt.md.
"""
import re, pathlib

TARGET = pathlib.Path(
    r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson04_efficient_storage_parquet.html"
)

NEW_SUBTITLE = "Pitfalls beginners hit when working with Parquet files"

NEW_BODY = """\
      <div class="flex flex-wrap items-center gap-2 mb-6" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Index Included</span>
        </button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">All Columns Loaded</span>
        </button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Bad Partition Key</span>
        </button>
        <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Filter After Load</span>
        </button>
        <button onclick="switchMkTab(4)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Missing PyArrow</span>
        </button>
      </div>

      <!-- ── Mistake 1: Index Included ── -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Saving Parquet with the Row Index Included</h4>
              <p class="text-xs text-gray-500 mt-0.5">The default <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_parquet()</code> call silently adds an <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">__index_level_0__</code> column that was not in your original data.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.to_parquet()</code> writes the pandas integer row index as an extra column by default. Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">index=False</code> to write only the columns that were in your original DataFrame.</p>
          </div>
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; extra column written
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">df.to_parquet(&quot;data.parquet&quot;)
# adds __index_level_0__ silently</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; index excluded
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">df.to_parquet(&quot;data.parquet&quot;, index=False)
# writes only your data columns</code></pre>
              </div>
            </div>
          </div>
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">index=False</code> as "save the spreadsheet, not the row numbers." Every Parquet file written to a data warehouse should use it to keep the schema clean and avoid a phantom column appearing in downstream queries.</p>
          </div>
        </div>
      </div>

      <!-- ── Mistake 2: All Columns Loaded ── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Reading Every Column When You Need Just One</h4>
              <p class="text-xs text-gray-500 mt-0.5"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_parquet()</code> without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">columns=</code> loads all columns into memory, even ones your analysis never uses.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Parquet supports column-level loading at read time. Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read_parquet()</code> without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">columns=</code> loads every column into memory first, then your pandas expression filters down — the opposite of efficient. Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">columns=</code> so unwanted columns are never decompressed.</p>
          </div>
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; all 30 columns loaded
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">df = pd.read_parquet(&quot;wide.parquet&quot;)
# all 30 columns enter memory
profit_total = df[&quot;profit&quot;].sum()</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; one column loaded
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">df = pd.read_parquet(&quot;wide.parquet&quot;,
    columns=[&quot;profit&quot;])  # 1 of 30 loaded
profit_total = df[&quot;profit&quot;].sum()</code></pre>
              </div>
            </div>
          </div>
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Column pruning is Parquet's biggest advantage over CSV — a CSV reader must scan every byte in every row to locate the columns you want, while Parquet skips entire column chunks at the storage layer. Name exactly the columns you need and Parquet does the rest.</p>
          </div>
        </div>
      </div>

      <!-- ── Mistake 3: Bad Partition Key ── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Partitioning by a High-Cardinality Column</h4>
              <p class="text-xs text-gray-500 mt-0.5">Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">order_id</code> as a partition key creates one file per order — millions of tiny files that are slower to read than no partitioning at all.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Parquet creates one sub-directory per unique value in the partition column. A column like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">order_id</code> with millions of unique values produces millions of tiny files — each with its own metadata overhead — which completely cancels any read-time benefit. Partition by low-cardinality columns like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">year</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">region</code> that split your data into a small number of meaningful folders.</p>
          </div>
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; millions of files
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">df.to_parquet(&quot;orders/&quot;,
    partition_cols=[&quot;order_id&quot;])
# 500 k unique IDs → 500 k files</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; small number of folders
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">df.to_parquet(&quot;orders/&quot;,
    partition_cols=[&quot;year&quot;, &quot;region&quot;])
# ~8 folders — fast and manageable</code></pre>
              </div>
            </div>
          </div>
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">A good partition column has between 2 and roughly 200 unique values — enough to give queries a meaningful shortcut, small enough that each resulting file holds a reasonably sized block of data. When in doubt, partition by month or region first and only add more levels if query patterns justify it.</p>
          </div>
        </div>
      </div>

      <!-- ── Mistake 4: Filter After Load ── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Filtering Rows in pandas After Reading the Full File</h4>
              <p class="text-xs text-gray-500 mt-0.5">A pandas boolean mask loads every row into memory first — Parquet's <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">filters=</code> skips non-matching row groups before any data is decompressed.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">A pandas boolean mask filters rows after they are already in memory — all rows were loaded and most are then discarded. Passing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">filters=</code> directly to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read_parquet()</code> enables predicate pushdown: the Parquet reader skips entire row groups whose min/max statistics prove they cannot match, so those bytes are never decompressed.</p>
          </div>
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; all rows loaded first
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">df = pd.read_parquet(&quot;sales.parquet&quot;)
# all 10 M rows enter memory
emea = df[df[&quot;region&quot;] == &quot;EMEA&quot;]</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; unmatched rows never read
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">emea = pd.read_parquet(&quot;sales.parquet&quot;,
    filters=[(&quot;region&quot;, &quot;==&quot;, &quot;EMEA&quot;)])
# row groups skipped at file level</code></pre>
              </div>
            </div>
          </div>
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">The key difference from a pandas <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">.query()</code> is <em>where</em> the filtering happens — <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">filters=</code> runs inside the Parquet file format before Python sees any data, whereas <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">.query()</code> runs after every row is already in a DataFrame.</p>
          </div>
        </div>
      </div>

      <!-- ── Mistake 5: Missing PyArrow ── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Forgetting to Install PyArrow in the Project Dependencies</h4>
              <p class="text-xs text-gray-500 mt-0.5"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_parquet()</code> raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ModuleNotFoundError</code> at runtime because pandas does not bundle a Parquet engine — it delegates all I/O to PyArrow or fastparquet.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Pandas does not include a Parquet engine — it calls PyArrow (or fastparquet) as a separate installed library. If neither is present, every <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read_parquet()</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_parquet()</code> call raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ModuleNotFoundError: No module named 'pyarrow'</code> the first time it runs in a new environment.</p>
          </div>
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; engine not declared
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># requirements.txt
pandas==2.2.0
# pyarrow absent → crashes at runtime</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; engine declared
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># requirements.txt
pandas==2.2.0
pyarrow&gt;=14.0  # required Parquet engine</code></pre>
              </div>
            </div>
          </div>
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">The error only surfaces when you deploy or create a fresh environment — everything works locally if PyArrow was already installed for another project. Always declare <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">pyarrow</code> explicitly in <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">requirements.txt</code> so it is never accidentally omitted.</p>
          </div>
        </div>
      </div>
"""

html = TARGET.read_text(encoding="utf-8")

# ── Patch 1: update section subtitle ─────────────────────────────────────────
OLD_SUBTITLE_LINE = '<p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls to avoid</p>'
NEW_SUBTITLE_LINE = f'<p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">{NEW_SUBTITLE}</p>'

# Only replace the one inside #mistakes (not any other section)
# We replace within the mistakes section context
mistakes_section_start = html.find('<section id="mistakes">')
if OLD_SUBTITLE_LINE in html[mistakes_section_start:mistakes_section_start + 1000]:
    html = html[:mistakes_section_start] + html[mistakes_section_start:].replace(
        OLD_SUBTITLE_LINE, NEW_SUBTITLE_LINE, 1
    )
    print("✅ subtitle updated")
else:
    print("⚠️  subtitle not found — check manually")

# ── Patch 2: replace section body ────────────────────────────────────────────
# Match the body div opening, all its content, and the two closing divs + </section>
# The body div is the direct child of the rounded-2xl div inside #mistakes
OLD_BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">\n'

# Find the body div within the mistakes section
mk_start = html.find('<section id="mistakes">')
mk_chunk = html[mk_start:]

body_pos_in_chunk = mk_chunk.find(OLD_BODY_OPEN)
if body_pos_in_chunk == -1:
    print("❌ body div not found inside #mistakes section")
    exit(1)

# Find the matching closing </div> for the body div
# We need to count depth from after the opening tag
body_abs_start = mk_start + body_pos_in_chunk
search_start = body_abs_start + len(OLD_BODY_OPEN)

depth = 1
i = search_start
while i < len(html) and depth > 0:
    open_pos = html.find("<div", i)
    close_pos = html.find("</div>", i)
    if open_pos == -1 and close_pos == -1:
        break
    if open_pos != -1 and (close_pos == -1 or open_pos < close_pos):
        depth += 1
        i = open_pos + 4
    else:
        depth -= 1
        if depth == 0:
            body_abs_end = close_pos + len("</div>")
        i = close_pos + 6

# Reconstruct file with new body
old_body_block = html[body_abs_start:body_abs_end]
new_body_block = f'    <div class="bg-white px-8 py-7 space-y-6">\n{NEW_BODY}\n    </div>'

html = html[:body_abs_start] + new_body_block + html[body_abs_end:]
print(f"✅ section body replaced ({len(old_body_block)} chars → {len(new_body_block)} chars)")

TARGET.write_text(html, encoding="utf-8")
print("✅ file written")

# ── Quick balance check ───────────────────────────────────────────────────────
import re as _re
for tag in ['div', 'section', 'button', 'pre', 'code']:
    opens  = len(_re.findall(rf'<{tag}[\s>]', html, _re.I))
    closes = len(_re.findall(rf'</{tag}>', html, _re.I))
    status = '✅' if opens == closes else '❌'
    print(f'{status} <{tag}>: opens={opens} closes={closes}')
print(f'mk-panels  : {html.count("mk-panel mk-panel-anim")} (expected 5)')
print(f'mk-steps   : {html.count("mk-step")} (expected 10+)')
print(f'total lines: {html.count(chr(10))+1}')
