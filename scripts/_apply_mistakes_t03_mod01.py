#!/usr/bin/env python3
"""
Rewrite <section id="mistakes"> for all 6 lessons in
track_03 / mod_01_data_engineering_foundations.

Uses the prompt spec from lesson-common-mistakes.prompt.md:
- Descriptive tab labels (never "Mistake N")
- Explanation paragraph above the split panel
- Style B-lite code blocks (px-4 py-3 on <pre>, no header)
- Wrong — label / Correct — label
- Amber tip on every card
"""

import re, pathlib, html as html_mod

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_03_data_engineering" / "mod_01_data_engineering_foundations"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

# ── Content definitions ────────────────────────────────────────────────

LESSONS = {
    # ── Lesson 01: What Is Data Engineering ──
    "lesson01_what_is_data_engineering.html": {
        "topic": "data engineering concepts",
        "mistakes": [
            {
                "tab": "Analysing in the Pipeline",
                "title": "Putting Analysis Logic Inside a Data Pipeline",
                "subtitle": "Pipelines should prepare data, not generate reports or run statistical models.",
                "explanation": 'A pipeline\u2019s job is to extract, clean, and load. Adding model training or chart generation makes the pipeline slow and fragile. Move analysis into a separate script that reads the pipeline\u2019s output.',
                "wrong_label": "analysis inside pipeline",
                "wrong_code": 'data = pd.read_csv("sales.csv")       # extract\ndata["total"] = data["price"] * data["quantity"]\nmodel = train_regression(data)         # analysis step\nplot_chart(model.predictions)          # reporting step',
                "correct_label": "pipeline only prepares data",
                "correct_code": 'data = pd.read_csv("sales.csv")       # extract\ndata["total"] = data["price"] * data["quantity"]  # transform\ndata.to_csv("clean_sales.csv", index=False)        # load',
                "tip": "Think of the pipeline as the kitchen prep station \u2014 it washes and chops ingredients but does not plate the final dish.",
            },
            {
                "tab": "Hardcoded Paths",
                "title": "Hardcoding Absolute File Paths in Pipeline Scripts",
                "subtitle": "The script breaks on any machine where the folder structure differs.",
                "explanation": 'An absolute path like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">C:/Users/me/data.csv</code> only works on one computer. Use relative paths or variables so the same script runs anywhere.',
                "wrong_label": "absolute path",
                "wrong_code": 'data = pd.read_csv("C:/Users/me/data/sales.csv")',
                "correct_label": "relative path",
                "correct_code": 'import os\ndata_dir = os.getenv("DATA_DIR", "data")  # configurable\ndata = pd.read_csv(f"{data_dir}/sales.csv") # portable path',
                "tip": "Store folder locations in environment variables or a config file. Your laptop and the production server will never share the same folder tree.",
            },
            {
                "tab": "Skipping Validation",
                "title": "Loading Data Without Checking Quality First",
                "subtitle": "Null values and wrong types slip into downstream tables silently.",
                "explanation": 'Skipping validation means bad records reach your database unnoticed. Check for nulls, duplicate keys, and unexpected types before writing output.',
                "wrong_label": "no checks",
                "wrong_code": 'data = pd.read_csv("orders.csv")\ndata.to_csv("clean_orders.csv", index=False)  # trusts input',
                "correct_label": "validate before loading",
                "correct_code": 'data = pd.read_csv("orders.csv")\nassert data["order_id"].notnull().all()  # check for nulls\nassert data["order_id"].is_unique         # check duplicates\ndata.to_csv("clean_orders.csv", index=False)',
                "tip": "Adding two assert lines takes seconds but catches errors that would otherwise hide in your data for weeks.",
            },
        ],
    },

    # ── Lesson 02: ETL vs ELT ──
    "lesson02_etl_vs_elt.html": {
        "topic": "ETL and ELT patterns",
        "mistakes": [
            {
                "tab": "Transform Before Extract",
                "title": "Transforming Data Before Extracting It Completely",
                "subtitle": "Applying transforms to a partial read causes missing or inconsistent rows.",
                "explanation": 'Both ETL and ELT start with a full extract. Transforming a half-loaded DataFrame drops rows that arrive later. Always complete the extract stage before any transformation.',
                "wrong_label": "partial extract then transform",
                "wrong_code": 'chunk = pd.read_csv("sales.csv", nrows=100)  # partial\nchunk["total"] = chunk["price"] * chunk["quantity"]\nchunk.to_csv("warehouse.csv", index=False)  # incomplete',
                "correct_label": "full extract first",
                "correct_code": 'data = pd.read_csv("sales.csv")              # full extract\ndata["total"] = data["price"] * data["quantity"]  # transform\ndata.to_csv("warehouse.csv", index=False)    # complete load',
                "tip": "Extract is the foundation. Cutting it short is like photocopying only half a document and then trying to summarise the full report.",
            },
            {
                "tab": "ELT Without Raw Copy",
                "title": "Running ELT Without Saving the Raw Data First",
                "subtitle": "Transforming in place destroys the original, making re-processing impossible.",
                "explanation": 'The whole point of ELT is that raw data is preserved in the warehouse. If you transform the only copy, you cannot rerun or audit the pipeline. Save raw data before transforming.',
                "wrong_label": "overwrite raw data",
                "wrong_code": 'data = pd.read_csv("sales.csv")\ndata["total"] = data["price"] * data["quantity"]\ndata.to_csv("sales.csv", index=False)  # overwrites source',
                "correct_label": "preserve raw, write processed",
                "correct_code": 'data = pd.read_csv("sales.csv")              # extract\ndata.to_csv("raw_sales.csv", index=False)    # save raw copy\ndata["total"] = data["price"] * data["quantity"]\ndata.to_csv("processed_sales.csv", index=False)',
                "tip": "Raw data is your safety net. Overwriting it is like shredding the original receipt after writing the expense report.",
            },
            {
                "tab": "Wrong Pattern Choice",
                "title": "Choosing ETL When ELT Would Be Simpler",
                "subtitle": "Heavy pre-processing in Python wastes time when the warehouse can transform faster.",
                "explanation": 'If your target database supports SQL transforms, loading raw data and transforming there (ELT) is often faster and more scalable. Reserve ETL for cases where the destination cannot run transforms.',
                "wrong_label": "heavy Python transforms",
                "wrong_code": 'data = pd.read_csv("events.csv")        # 50 million rows\ndata = data.groupby("user_id").sum()     # slow in Python\ndata.to_sql("events", engine, index=False)',
                "correct_label": "load raw, transform in SQL",
                "correct_code": 'data = pd.read_csv("events.csv")        # extract\ndata.to_sql("raw_events", engine, index=False)  # load raw\n# then run: SELECT user_id, SUM(amount)\n#           FROM raw_events GROUP BY user_id',
                "tip": "Databases are built for aggregation. Let the warehouse do the heavy lifting instead of making Python churn through millions of rows.",
            },
        ],
    },

    # ── Lesson 03: Handling Large Datasets ──
    "lesson03_handling_large_datasets.html": {
        "topic": "large dataset handling",
        "mistakes": [
            {
                "tab": "Loading Everything",
                "title": "Reading an Entire Large File Into Memory at Once",
                "subtitle": "Python raises a MemoryError or the system freezes when the file exceeds available RAM.",
                "explanation": 'Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_csv()</code> without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">chunksize</code> loads the whole file. For multi-gigabyte files this exhausts memory. Use chunked reading instead.',
                "wrong_label": "load everything",
                "wrong_code": 'data = pd.read_csv("large_orders.csv")  # 8 GB file\nprint(data.shape)                        # MemoryError',
                "correct_label": "read in chunks",
                "correct_code": 'chunks = pd.read_csv("large_orders.csv",\n                     chunksize=50000)   # manageable batches\nfor chunk in chunks:\n    print(chunk.shape)                   # process each piece',
                "tip": "Chunked reading is like drinking from a glass instead of a fire hose \u2014 your computer can only swallow so much data at once.",
            },
            {
                "tab": "Loading All Columns",
                "title": "Loading Every Column When You Only Need a Few",
                "subtitle": "Unused columns waste memory and slow down every operation on the DataFrame.",
                "explanation": 'Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">usecols</code> to load only the columns your analysis needs. A 20-column file uses five times the memory of the four columns you actually want.',
                "wrong_label": "all columns",
                "wrong_code": 'data = pd.read_csv("orders.csv")  # loads all 20 columns',
                "correct_label": "select columns",
                "correct_code": 'needed = ["order_id", "price", "quantity", "date"]\ndata = pd.read_csv("orders.csv",\n                   usecols=needed)  # only 4 columns loaded',
                "tip": "List the columns you actually use before loading. If a column never appears in your code, it should not be in your DataFrame.",
            },
            {
                "tab": "Ignoring dtypes",
                "title": "Leaving Default Data Types on Large Numeric Columns",
                "subtitle": "Pandas defaults to int64 and float64, which use double the memory needed for most values.",
                "explanation": 'A column of small integers (0\u2013255) stored as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int64</code> uses 8 bytes per value. Downcasting to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int8</code> uses 1 byte. Multiply that saving across millions of rows.',
                "wrong_label": "default int64",
                "wrong_code": 'data = pd.read_csv("orders.csv")\nprint(data["quantity"].dtype)  # int64 \u2014 8 bytes each',
                "correct_label": "downcast types",
                "correct_code": 'data = pd.read_csv("orders.csv")\ndata["quantity"] = pd.to_numeric(\n    data["quantity"], downcast="integer")  # int8 or int16\nprint(data["quantity"].dtype)              # much smaller',
                "tip": "Downcasting is free performance. The numbers stay the same, but each one takes less space \u2014 like switching from hardcover books to paperbacks on a crowded shelf.",
            },
        ],
    },

    # ── Lesson 05: Parquet \u2014 Efficient Storage ──
    "lesson05_parquet_efficient_storage.html": {
        "topic": "Parquet files",
        "mistakes": [
            {
                "tab": "Missing Library",
                "title": "Writing Parquet Without Installing the Engine",
                "subtitle": "Pandas raises an ImportError because no Parquet engine is available.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_parquet()</code> needs either <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pyarrow</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">fastparquet</code> installed. Without one, Pandas raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ImportError: Unable to find a usable engine</code>.',
                "wrong_label": "no engine installed",
                "wrong_code": 'data = pd.read_csv("sales.csv")\ndata.to_parquet("sales.parquet")  # ImportError',
                "correct_label": "install engine first",
                "correct_code": '# pip install pyarrow              # run once in terminal\ndata = pd.read_csv("sales.csv")\ndata.to_parquet("sales.parquet")   # works with pyarrow',
                "tip": "Add <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pyarrow</code> to your project\u2019s requirements file. It is the most widely used Parquet engine in the Python ecosystem.",
            },
            {
                "tab": "Reading With read_csv",
                "title": "Using read_csv() to Open a Parquet File",
                "subtitle": "Pandas cannot parse binary Parquet bytes as CSV text and returns garbled data or an error.",
                "explanation": 'Parquet is a binary columnar format, not comma-separated text. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_parquet()</code> to read it correctly.',
                "wrong_label": "wrong reader",
                "wrong_code": 'data = pd.read_csv("sales.parquet")   # garbled output',
                "correct_label": "use read_parquet",
                "correct_code": 'data = pd.read_parquet("sales.parquet")  # correct reader\nprint(data.head())                        # clean data',
                "tip": "Match the reader to the file format: <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.csv</code> \u2192 <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">read_csv()</code>, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.parquet</code> \u2192 <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">read_parquet()</code>.",
            },
            {
                "tab": "Loading All Columns",
                "title": "Ignoring Column Selection When Reading Parquet",
                "subtitle": "Parquet can skip unused columns entirely, but only if you tell it which ones you need.",
                "explanation": 'Parquet stores data by column, so it can read just two columns from a 50-column file almost instantly. Pass the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">columns</code> parameter to skip the rest.',
                "wrong_label": "all columns loaded",
                "wrong_code": 'data = pd.read_parquet("sales.parquet")  # loads everything',
                "correct_label": "select columns",
                "correct_code": 'needed = ["product", "total"]\ndata = pd.read_parquet("sales.parquet",\n                       columns=needed)    # two columns only',
                "tip": "One of Parquet\u2019s biggest advantages is column pruning. Skipping columns you do not need makes reads dramatically faster.",
            },
        ],
    },

    # ── Lesson 06: Intro to Polars (Optional) ──
    "lesson06_intro_to_polars_optional.html": {
        "topic": "Polars basics",
        "mistakes": [
            {
                "tab": "Pandas Syntax in Polars",
                "title": "Using Pandas Bracket Syntax in Polars",
                "subtitle": "Polars does not support df[\"column\"] bracket selection like Pandas.",
                "explanation": 'Polars uses <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.select()</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pl.col()</code> expressions instead of bracket indexing. Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["price"]</code> raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TypeError</code> in Polars.',
                "wrong_label": "Pandas bracket syntax",
                "wrong_code": 'import polars as pl\ndata = pl.read_csv("orders.csv")\nprices = data["price"]          # TypeError in Polars',
                "correct_label": "Polars select syntax",
                "correct_code": 'import polars as pl\ndata = pl.read_csv("orders.csv")\nprices = data.select(pl.col("price"))  # Polars expression',
                "tip": "Polars looks like Pandas at first glance, but its selection API is entirely expression-based. Check the docs before translating code line by line.",
            },
            {
                "tab": "Mutating In Place",
                "title": "Trying to Modify a Polars DataFrame In Place",
                "subtitle": "Polars DataFrames are immutable \u2014 operations return a new DataFrame instead of changing the original.",
                "explanation": 'In Pandas you can write <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["new"] = values</code>. Polars requires <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">with_columns()</code>, which returns a new DataFrame. The original stays unchanged.',
                "wrong_label": "in-place assignment",
                "wrong_code": 'data["total"] = data["price"] * data["quantity"]  # error',
                "correct_label": "use with_columns",
                "correct_code": 'data = data.with_columns(\n    (pl.col("price") * pl.col("quantity"))  # compute\n    .alias("total")                          # name the column\n)',
                "tip": "Immutability sounds limiting, but it prevents accidental overwrites. Every transformation produces a clean, traceable copy.",
            },
            {
                "tab": "Wrong Filter Syntax",
                "title": "Filtering With Python Comparison Instead of Polars Expressions",
                "subtitle": "A plain Python comparison does not produce the row-level filter Polars expects.",
                "explanation": 'Polars filters need <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pl.col("col") &gt; value</code> inside <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.filter()</code>. Writing a bare Python comparison like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">data["price"] &gt; 50</code> fails because Polars does not support bracket indexing.',
                "wrong_label": "Python-style filter",
                "wrong_code": 'expensive = data[data["price"] &gt; 50]   # not valid Polars',
                "correct_label": "Polars expression filter",
                "correct_code": 'expensive = data.filter(\n    pl.col("price") &gt; 50                # Polars expression\n)',
                "tip": "Every Polars operation starts with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pl.col()</code>. Once you build that habit, the rest of the API clicks into place.",
            },
        ],
    },

    # ── Lesson 07: Pipeline Design Concepts ──
    "lesson07_pipeline_design_concepts.html": {
        "topic": "pipeline design",
        "mistakes": [
            {
                "tab": "Monolithic Script",
                "title": "Writing the Entire Pipeline as One Long Script",
                "subtitle": "A single-function pipeline is hard to test, debug, and reuse.",
                "explanation": 'When extract, transform, and load live in one block, a bug anywhere forces you to rerun everything. Splitting into separate functions lets you test and rerun each stage independently.',
                "wrong_label": "one big script",
                "wrong_code": 'data = pd.read_csv("orders.csv")\ndata["total"] = data["price"] * data["quantity"]\ndata = data.dropna()\ndata.to_csv("output.csv", index=False)',
                "correct_label": "modular functions",
                "correct_code": 'def extract():\n    return pd.read_csv("orders.csv")      # stage 1\ndef transform(data):\n    data["total"] = data["price"] * data["quantity"]\n    return data.dropna()                   # stage 2\ndef load(data):\n    data.to_csv("output.csv", index=False) # stage 3',
                "tip": "Each function should do one job. If you cannot describe what a function does in one sentence, it is doing too much.",
            },
            {
                "tab": "Non-Idempotent Steps",
                "title": "Writing Transform Steps That Produce Different Results on Rerun",
                "subtitle": "Rerunning the pipeline creates duplicate rows or inconsistent output.",
                "explanation": 'An idempotent step produces the same result whether you run it once or ten times. Appending without checking for duplicates is the most common violation. Use overwrite or upsert logic.',
                "wrong_label": "appends duplicates",
                "wrong_code": 'data.to_csv("output.csv", mode="a",\n            header=False)  # appends every run',
                "correct_label": "overwrite safely",
                "correct_code": 'data.to_csv("output.csv",\n            index=False)   # overwrites \u2014 same result every run',
                "tip": "Ask yourself: \u201cIf this step runs twice, do I get the same file?\u201d If the answer is no, the step is not idempotent and will cause trouble in production.",
            },
            {
                "tab": "No Error Handling",
                "title": "Ignoring Errors Instead of Catching and Logging Them",
                "subtitle": "A silent failure in one stage corrupts every stage that follows.",
                "explanation": 'Without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">try/except</code>, a missing file or bad record crashes the entire pipeline with no record of what went wrong. Wrap each stage and log the error.',
                "wrong_label": "no error handling",
                "wrong_code": 'data = pd.read_csv("orders.csv")  # crashes if missing\ndata.to_csv("output.csv", index=False)',
                "correct_label": "catch and log errors",
                "correct_code": 'import logging\ntry:\n    data = pd.read_csv("orders.csv")       # extract\n    data.to_csv("output.csv", index=False) # load\nexcept Exception as err:\n    logging.error(f"Pipeline failed: {err}")',
                "tip": "A pipeline that crashes silently is worse than one that crashes loudly. Good error handling turns a mystery into a diagnosis.",
            },
        ],
    },
}


# ── HTML builders ──────────────────────────────────────────────────────

def _tab_btn(index: int, label: str, *, active: bool) -> str:
    if active:
        cls = (
            'mk-step mk-step-active flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
            'text-white shadow-lg shadow-pink-200/50 transition-all duration-250'
        )
    else:
        cls = (
            'mk-step flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gray-800 text-gray-400 transition-all duration-250'
        )
    return (
        f'<button onclick="switchMkTab({index})" '
        f'class="{cls}" role="tab">\n'
        f'  <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
        f'  <span class="mk-step-label text-xs font-bold">{label}</span>\n'
        f'</button>'
    )


def _panel(mk: dict, *, hidden: bool) -> str:
    hide = " hidden" if hidden else ""
    return f'''\
<div class="mk-panel mk-panel-anim{hide}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

    <!-- Card header -->
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["subtitle"]}</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>

    <!-- Explanation paragraph -->
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">{mk["explanation"]}</p>
    </div>

    <!-- Wrong / Correct split panel -->
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong \u2014 {mk["wrong_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["wrong_code"]}</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct \u2014 {mk["correct_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["correct_code"]}</code></pre>
        </div>
      </div>
    </div>

    <!-- Amber tip footer -->
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["tip"]}</p>
    </div>

  </div>
</div>'''


def build_section(topic: str, mistakes: list[dict]) -> str:
    """Build the full <section id="mistakes"> HTML."""

    # Tab row
    tabs = "\n".join(
        _tab_btn(i, m["tab"], active=(i == 0))
        for i, m in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{tabs}\n</div>'

    # Panels
    panels = "\n\n".join(
        _panel(m, hidden=(i > 0))
        for i, m in enumerate(mistakes)
    )

    body = f'{tab_row}\n\n{panels}'

    return f'''\
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with {topic}</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

{body}

    </div>
  </div>
</section>'''


# ── Main ───────────────────────────────────────────────────────────────

ok = fail = 0
for filename, lesson in LESSONS.items():
    path = MOD / filename
    if not path.exists():
        print(f"\u274c NOT FOUND  {filename}")
        fail += 1
        continue

    text = path.read_text(encoding="utf-8")
    replacement = build_section(lesson["topic"], lesson["mistakes"])
    new_text, n = SECTION_RE.subn(replacement, text, count=1)

    if n == 0:
        print(f"\u274c NO MATCH   {filename}")
        fail += 1
        continue

    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {filename}")
    ok += 1

print(f"\n{ok}/{ok + fail} mistakes sections rewritten")
