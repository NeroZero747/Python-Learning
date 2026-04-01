#!/usr/bin/env python3
"""
Rewrite <section id="mistakes"> for all 14 lessons in
track_03 / mod_05_large_scale_data_processing.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_03_data_engineering" / "mod_05_large_scale_data_processing"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

LESSONS = {
    # ── Lesson 02: Memory Optimisation ──
    "lesson02_memory_optimization.html": {
        "topic": "memory optimisation",
        "mistakes": [
            {
                "tab": "Skipping memory_usage()",
                "title": "Optimising Memory Without Measuring It First",
                "subtitle": "You cannot improve what you have not measured.",
                "explanation": 'Before downcasting or dropping columns, call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.memory_usage(deep=True)</code> to see where the memory is going. Guessing wastes time on columns that are already small.',
                "wrong_label": "guess and optimise",
                "wrong_code": 'df["quantity"] = df["quantity"].astype("int8")\n# did this actually save meaningful memory? unknown',
                "correct_label": "measure first",
                "correct_code": 'print(df.memory_usage(deep=True).sum() / 1e6, "MB")\ndf["quantity"] = df["quantity"].astype("int8")\nprint(df.memory_usage(deep=True).sum() / 1e6, "MB")',
                "tip": "Always print memory before and after optimisation. If the saving is tiny, the effort was not worth the complexity.",
            },
            {
                "tab": "Ignoring Object Columns",
                "title": "Focusing Only on Numeric Columns and Ignoring Object (String) Columns",
                "subtitle": "String columns often consume the most memory in a DataFrame.",
                "explanation": 'Pandas stores strings as Python objects, which are far larger than numeric types. A column of repeated categories like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"active"</code> / <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"inactive"</code> can shrink dramatically when converted to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">category</code> dtype.',
                "wrong_label": "ignore string columns",
                "wrong_code": 'df["qty"] = df["qty"].astype("int16")  # saves a little\n# df["status"] is object — still using 80% of memory',
                "correct_label": "convert to category",
                "correct_code": 'df["status"] = df["status"].astype("category")\n# "active"/"inactive" stored as integers internally',
                "tip": "Convert any column with fewer than ~1,000 unique values to <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">category</code>. It stores the strings once and uses integer codes per row.",
            },
            {
                "tab": "Downcasting Blindly",
                "title": "Downcasting Without Checking the Value Range First",
                "subtitle": "Casting int64 to int8 silently overflows if values exceed the int8 range.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int8</code> holds values from -128 to 127. If your column has values up to 5,000, downcasting to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int8</code> wraps around silently and corrupts the data. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.to_numeric(downcast=...)</code> which picks the smallest safe type automatically.',
                "wrong_label": "force int8",
                "wrong_code": 'df["sales"] = df["sales"].astype("int8")\n# values > 127 silently wrap to negatives',
                "correct_label": "safe downcast",
                "correct_code": 'df["sales"] = pd.to_numeric(\n    df["sales"], downcast="integer")  # picks int16 or int32',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pd.to_numeric(downcast=\"integer\")</code> instead of manual <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">astype()</code>. It checks the range and picks the smallest type that fits.",
            },
        ],
    },

    # ── Lesson 03: Chunk Processing ──
    "lesson03_chunk_processing.html": {
        "topic": "chunk processing",
        "mistakes": [
            {
                "tab": "Aggregating Per Chunk Only",
                "title": "Aggregating Inside Each Chunk Without Combining Results Across Chunks",
                "subtitle": "Each chunk's result is independent — you need a final merge to get the correct total.",
                "explanation": 'If you compute a mean inside each chunk, you get per-chunk means, not the global mean. Collect partial results (sum and count) from each chunk, then combine them at the end.',
                "wrong_label": "per-chunk mean",
                "wrong_code": 'for chunk in pd.read_csv("big.csv", chunksize=10000):\n    print(chunk["amount"].mean())  # different per chunk\n# no combined result',
                "correct_label": "accumulate and combine",
                "correct_code": 'total, count = 0, 0\nfor chunk in pd.read_csv("big.csv", chunksize=10000):\n    total += chunk["amount"].sum()\n    count += len(chunk)\nprint(total / count)  # correct global mean',
                "tip": "Keep a running total and count across chunks. Compute the final statistic only after all chunks are processed.",
            },
            {
                "tab": "Too Small Chunk Size",
                "title": "Setting a Very Small Chunk Size That Creates Thousands of Iterations",
                "subtitle": "Tiny chunks add I/O overhead and slow the pipeline dramatically.",
                "explanation": 'A chunk size of 100 on a 10-million-row file means 100,000 iterations. The overhead of reading and processing that many chunks is far greater than the memory you save. Use a chunk size of 10,000\u2013100,000.',
                "wrong_label": "tiny chunks",
                "wrong_code": 'for chunk in pd.read_csv("big.csv", chunksize=100):\n    process(chunk)  # 100,000 iterations — very slow',
                "correct_label": "reasonable chunk size",
                "correct_code": 'for chunk in pd.read_csv("big.csv", chunksize=50000):\n    process(chunk)  # 200 iterations — fast',
                "tip": "Start with 50,000 rows and adjust based on available memory. Monitor RAM usage during a test run to find the sweet spot.",
            },
            {
                "tab": "Collecting All Chunks Into a List",
                "title": "Appending Every Chunk to a List and Then Concatenating",
                "subtitle": "This loads the entire file into memory — the same problem chunking was supposed to solve.",
                "explanation": 'Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">chunks.append(chunk)</code> followed by <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.concat(chunks)</code> reconstructs the full DataFrame in memory. Process each chunk and write results immediately to avoid accumulating data.',
                "wrong_label": "collect all chunks",
                "wrong_code": 'chunks = []\nfor chunk in pd.read_csv("big.csv", chunksize=50000):\n    chunks.append(chunk)\ndf = pd.concat(chunks)  # full file in memory again',
                "correct_label": "process and write each chunk",
                "correct_code": 'for i, chunk in enumerate(pd.read_csv("big.csv", chunksize=50000)):\n    chunk = transform(chunk)\n    chunk.to_csv("out.csv", mode="a",\n                 header=(i == 0), index=False)',
                "tip": "The whole point of chunking is to avoid loading the full file. If you collect chunks into a list, you have defeated the purpose.",
            },
        ],
    },

    # ── Lesson 04: Processing Millions of Rows ──
    "lesson04_processing_millions_of_rows.html": {
        "topic": "processing millions of rows",
        "mistakes": [
            {
                "tab": "Using iterrows()",
                "title": "Looping Over Rows With iterrows() Instead of Vectorised Operations",
                "subtitle": "iterrows() is 100–1,000x slower than vectorised pandas operations.",
                "explanation": 'Pandas is built for column-wise (vectorised) operations that run in compiled C code. Looping row-by-row with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">iterrows()</code> drops back to pure Python speed. Replace loops with vectorised expressions.',
                "wrong_label": "row-by-row loop",
                "wrong_code": 'for idx, row in df.iterrows():\n    df.loc[idx, "total"] = row["price"] * row["qty"]\n# minutes on 1M rows',
                "correct_label": "vectorised operation",
                "correct_code": 'df["total"] = df["price"] * df["qty"]\n# seconds on 1M rows',
                "tip": "If you write a <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">for</code> loop over DataFrame rows, stop and ask: can I express this as a column operation? The answer is almost always yes.",
            },
            {
                "tab": "apply() With a Slow Function",
                "title": "Using apply() With a Complex Python Function Instead of Built-In Methods",
                "subtitle": "apply() runs a Python function per row — still slow on millions of rows.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">apply()</code> is faster than <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">iterrows()</code> but far slower than native pandas methods. If a built-in method exists (like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">str.upper()</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">fillna()</code>, or arithmetic), prefer it.',
                "wrong_label": "apply per row",
                "wrong_code": 'df["name_upper"] = df["name"].apply(lambda x: x.upper())',
                "correct_label": "built-in vectorised method",
                "correct_code": 'df["name_upper"] = df["name"].str.upper()',
                "tip": "Search the pandas docs for a built-in method before writing a custom function. Pandas has optimised methods for most common string, date, and numeric operations.",
            },
            {
                "tab": "Not Timing Your Code",
                "title": "Assuming Your Code Is Fast Without Actually Timing It",
                "subtitle": "You cannot optimise what you have not benchmarked.",
                "explanation": 'Wrap your code in a timer before and after optimising to see the actual difference. Without measurements, you might spend an hour \"optimising\" a step that was already fast, while the slow step goes unnoticed.',
                "wrong_label": "no timing",
                "wrong_code": 'df["total"] = df.apply(calc_total, axis=1)\n# "it feels fast" — but is it?',
                "correct_label": "time it",
                "correct_code": 'import time\nstart = time.time()\ndf["total"] = df["price"] * df["qty"]\nprint(f"Took {time.time() - start:.2f}s")',
                "tip": "Timing one-liners with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">time.time()</code> is good enough for quick checks. For detailed profiling, use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">%%timeit</code> in Jupyter.",
            },
        ],
    },

    # ── Lesson 05: Columnar Storage ──
    "lesson05_columnar_storage.html": {
        "topic": "columnar storage",
        "mistakes": [
            {
                "tab": "Using CSV for Analytics",
                "title": "Using CSV for Large Analytical Datasets When Columnar Formats Exist",
                "subtitle": "CSV reads every column on every scan — columnar formats skip unused columns entirely.",
                "explanation": 'CSV is row-based: reading one column means scanning every row from start to finish. Columnar formats like Parquet store data by column, so a query on two columns out of fifty reads only those two. For analytics, columnar is dramatically faster.',
                "wrong_label": "CSV for analytics",
                "wrong_code": 'df = pd.read_csv("big_data.csv")\n# reads all 50 columns even if you need 2',
                "correct_label": "Parquet with column selection",
                "correct_code": 'df = pd.read_parquet("big_data.parquet",\n                     columns=["region", "total"])\n# reads only 2 columns — much faster',
                "tip": "Convert your large CSV files to Parquet once. Every subsequent read will be faster, smaller, and support column pruning.",
            },
            {
                "tab": "Ignoring Compression",
                "title": "Storing Columnar Files Without Compression",
                "subtitle": "Columnar formats compress far better than CSV — skipping compression wastes disk space.",
                "explanation": 'Parquet with Snappy compression is often 5\u201310x smaller than the same data in CSV. Compression also means less data to read from disk, so queries are faster even though decompression adds a small cost.',
                "wrong_label": "no compression",
                "wrong_code": 'df.to_parquet("data.parquet", compression=None)\n# file is much larger than necessary',
                "correct_label": "use Snappy compression",
                "correct_code": 'df.to_parquet("data.parquet", compression="snappy")\n# default in most tools — fast and compact',
                "tip": "Snappy is the default compression for Parquet and offers the best balance of speed and size. Only change it if you have a specific reason.",
            },
            {
                "tab": "Row-Based Thinking",
                "title": "Iterating Row by Row Over Columnar Data Like It Were CSV",
                "subtitle": "Columnar data is designed for column-wise operations — row loops miss the performance benefit.",
                "explanation": 'The whole point of columnar storage is enabling vectorised column operations. Looping over rows with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">iterrows()</code> after reading a Parquet file throws away the speed advantage. Use column operations instead.',
                "wrong_label": "row loop on Parquet data",
                "wrong_code": 'df = pd.read_parquet("sales.parquet")\nfor idx, row in df.iterrows():\n    total += row["amount"]  # slow row loop',
                "correct_label": "vectorised column operation",
                "correct_code": 'df = pd.read_parquet("sales.parquet")\ntotal = df["amount"].sum()  # instant',
                "tip": "If you load data from Parquet, commit to column-wise operations. Vectorised pandas, Polars, or DuckDB SQL will keep you in the fast lane.",
            },
        ],
    },

    # ── Lesson 06: Parquet Files ──
    "lesson06_parquet_files.html": {
        "topic": "Parquet files",
        "mistakes": [
            {
                "tab": "Missing pyarrow",
                "title": "Calling to_parquet() Without Installing a Parquet Engine",
                "subtitle": "Pandas raises an ImportError because no Parquet engine is available.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_parquet()</code> needs <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pyarrow</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">fastparquet</code> installed. Without one, pandas cannot read or write Parquet files. Install the engine before calling any Parquet function.',
                "wrong_label": "no engine installed",
                "wrong_code": 'df.to_parquet("sales.parquet")  # ImportError',
                "correct_label": "install pyarrow first",
                "correct_code": '# pip install pyarrow\ndf.to_parquet("sales.parquet")  # works',
                "tip": "Add <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pyarrow</code> to your project's <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">requirements.txt</code>. It is the most widely used Parquet engine in the Python ecosystem.",
            },
            {
                "tab": "Reading With read_csv()",
                "title": "Using read_csv() to Open a Parquet File",
                "subtitle": "Parquet is a binary format — read_csv() returns garbled data or an error.",
                "explanation": 'Parquet files are not comma-separated text. Passing a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.parquet</code> file to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read_csv()</code> produces a garbled DataFrame or a parse error. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_parquet()</code> instead.',
                "wrong_label": "wrong reader",
                "wrong_code": 'df = pd.read_csv("sales.parquet")  # garbled output',
                "correct_label": "correct reader",
                "correct_code": 'df = pd.read_parquet("sales.parquet")  # clean data',
                "tip": "Match the reader to the file extension: <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.csv</code> \u2192 <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">read_csv()</code>, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.parquet</code> \u2192 <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">read_parquet()</code>.",
            },
            {
                "tab": "Loading All Columns",
                "title": "Reading All Columns From Parquet When You Need Only a Few",
                "subtitle": "Parquet's biggest advantage is column pruning — skipping it wastes the speed benefit.",
                "explanation": 'Parquet stores data by column, so it can skip entire columns during a read. Passing the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">columns</code> parameter lets the engine read only what you need, dramatically reducing I/O and memory.',
                "wrong_label": "all columns",
                "wrong_code": 'df = pd.read_parquet("sales.parquet")  # loads everything',
                "correct_label": "select columns",
                "correct_code": 'df = pd.read_parquet("sales.parquet",\n                     columns=["product", "total"])',
                "tip": "Always specify <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">columns=</code> when reading Parquet. It is one of the format\u2019s biggest performance wins and costs nothing.",
            },
        ],
    },

    # ── Lesson 07: PyArrow Basics ──
    "lesson07_pyarrow_basics.html": {
        "topic": "PyArrow basics",
        "mistakes": [
            {
                "tab": "Schema Mismatch",
                "title": "Creating an Arrow Table Without Defining a Schema",
                "subtitle": "PyArrow infers types that may not match your downstream expectations.",
                "explanation": 'Without an explicit schema, PyArrow guesses types from the data. An integer column with one <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">None</code> value can become <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">float64</code> instead of <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int32</code>. Define a schema to control types precisely.',
                "wrong_label": "inferred schema",
                "wrong_code": 'import pyarrow as pa\ntable = pa.table({"age": [30, None, 25]})\nprint(table.schema)  # age: float64 (not int)',
                "correct_label": "explicit schema",
                "correct_code": 'schema = pa.schema([(\"age\", pa.int32())])\ntable = pa.table({\"age\": [30, None, 25]}, schema=schema)\nprint(table.schema)  # age: int32',
                "tip": "Define your schema once and reuse it for all tables from the same source. It prevents type surprises and makes Parquet files consistent.",
            },
            {
                "tab": "Mixing Arrow and Pandas Ops",
                "title": "Converting Arrow Tables to Pandas for Every Operation",
                "subtitle": "Repeated conversions waste time and memory — stay in one API.",
                "explanation": 'Arrow and pandas have different memory layouts. Converting back and forth copies the data each time. If you need pandas for analysis, convert once at the end. For reads and metadata, stay in Arrow.',
                "wrong_label": "convert for every step",
                "wrong_code": 'table = pq.read_table("data.parquet")\ndf = table.to_pandas()       # copy 1\ntable2 = pa.Table.from_pandas(df)  # copy 2',
                "correct_label": "convert once",
                "correct_code": 'table = pq.read_table("data.parquet")\n# do Arrow operations here (filter, select)\ndf = table.to_pandas()  # single conversion at the end',
                "tip": "Decide early whether to work in Arrow or pandas. Convert once and stay there for the rest of the pipeline.",
            },
            {
                "tab": "Ignoring Metadata",
                "title": "Skipping Parquet File Metadata When Debugging Data Issues",
                "subtitle": "Parquet metadata tells you schema, row counts, and column statistics without reading the data.",
                "explanation": 'Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pq.read_metadata()</code> reads the file footer in milliseconds and shows you schema, row group counts, and min/max statistics. Reading the full file to check these things is unnecessarily slow.',
                "wrong_label": "read full file",
                "wrong_code": 'import pyarrow.parquet as pq\ntable = pq.read_table("big.parquet")  # loads everything\nprint(len(table), table.schema)',
                "correct_label": "read metadata only",
                "correct_code": 'meta = pq.read_metadata("big.parquet")  # instant\nprint(meta.num_rows, meta.schema)',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pq.read_metadata()</code> for quick inspections. It reads only the file footer, not the data — even on multi-gigabyte files.",
            },
        ],
    },

    # ── Lesson 08: Introduction to Polars ──
    "lesson08_introduction_to_polars.html": {
        "topic": "Polars basics",
        "mistakes": [
            {
                "tab": "Pandas Syntax in Polars",
                "title": "Using Pandas Bracket Syntax in Polars",
                "subtitle": "Polars does not support df[\"column\"] bracket selection like Pandas.",
                "explanation": 'Polars uses <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.select()</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pl.col()</code> expressions instead of bracket indexing. Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["price"]</code> raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TypeError</code>.',
                "wrong_label": "Pandas bracket syntax",
                "wrong_code": 'import polars as pl\ndf = pl.read_csv("orders.csv")\nprices = df["price"]          # TypeError',
                "correct_label": "Polars expression syntax",
                "correct_code": 'import polars as pl\ndf = pl.read_csv("orders.csv")\nprices = df.select(pl.col("price"))',
                "tip": "Polars looks like Pandas at first glance, but selection is expression-based. Start with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pl.col()</code> and the rest follows.",
            },
            {
                "tab": "Mutating In Place",
                "title": "Trying to Modify a Polars DataFrame In Place",
                "subtitle": "Polars DataFrames are immutable — operations return a new DataFrame.",
                "explanation": 'In Pandas you assign with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["new"] = values</code>. Polars requires <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.with_columns()</code>, which returns a new DataFrame without modifying the original.',
                "wrong_label": "in-place assignment",
                "wrong_code": 'df["total"] = df["price"] * df["qty"]  # error',
                "correct_label": "with_columns",
                "correct_code": 'df = df.with_columns(\n    (pl.col("price") * pl.col("qty")).alias("total")\n)',
                "tip": "Immutability prevents accidental overwrites. Every Polars transformation produces a clean, traceable copy.",
            },
            {
                "tab": "Wrong Filter Syntax",
                "title": "Filtering With Pandas-Style Boolean Indexing in Polars",
                "subtitle": "Polars uses .filter() with pl.col() expressions, not bracket boolean masks.",
                "explanation": 'Polars filters use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.filter(pl.col("col") &gt; value)</code>. The Pandas pattern <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df[df["col"] &gt; value]</code> does not work because Polars does not support bracket indexing.',
                "wrong_label": "Pandas-style filter",
                "wrong_code": 'expensive = df[df["price"] > 50]  # not valid in Polars',
                "correct_label": "Polars filter expression",
                "correct_code": 'expensive = df.filter(pl.col("price") > 50)',
                "tip": "Every Polars operation starts with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pl.col()</code>. Once you build that habit, the rest of the API clicks into place.",
            },
        ],
    },

    # ── Lesson 09: Faster DataFrames With Polars ──
    "lesson09_faster_dataframes_with_polars.html": {
        "topic": "faster DataFrames with Polars",
        "mistakes": [
            {
                "tab": "Skipping Lazy Mode",
                "title": "Using Eager Mode When Lazy Mode Would Be Faster",
                "subtitle": "Eager mode executes every step immediately — lazy mode lets Polars optimise the whole plan.",
                "explanation": 'In lazy mode, Polars builds a query plan and optimises it before executing: predicate pushdown, projection pushdown, and parallel execution. Eager mode runs each step sequentially without optimisation.',
                "wrong_label": "eager mode",
                "wrong_code": 'df = pl.read_csv("big.csv")\ndf = df.filter(pl.col("active"))\ndf = df.group_by("dept").agg(pl.col("salary").mean())',
                "correct_label": "lazy mode",
                "correct_code": 'result = (\n    pl.scan_csv("big.csv")\n    .filter(pl.col("active"))\n    .group_by("dept")\n    .agg(pl.col("salary").mean())\n    .collect()\n)',
                "tip": "Start with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pl.scan_csv()</code> instead of <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pl.read_csv()</code> to enter lazy mode. Call <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.collect()</code> at the end to execute the optimised plan.",
            },
            {
                "tab": "Chaining Without Expressions",
                "title": "Writing Separate Statements Instead of Chaining Expressions",
                "subtitle": "Separate steps prevent Polars from optimising across operations.",
                "explanation": 'Polars expressions are designed to be chained. When you write separate statements, each one materialises an intermediate DataFrame. Chaining lets the optimiser combine steps and reduce memory copies.',
                "wrong_label": "separate steps",
                "wrong_code": 'df = df.filter(pl.col("active"))\ndf = df.with_columns(pl.col("salary") * 1.1)\ndf = df.select(["name", "salary"])',
                "correct_label": "chained expression",
                "correct_code": 'result = (\n    df.lazy()\n    .filter(pl.col("active"))\n    .with_columns(pl.col("salary") * 1.1)\n    .select(["name", "salary"])\n    .collect()\n)',
                "tip": "Chain everything into one pipeline expression. Polars can then optimise the entire plan — filtering early, pushing projections down, and parallelising.",
            },
            {
                "tab": "Benchmarking Wrong",
                "title": "Comparing Polars and Pandas Without Controlling for Warm-Up and Caching",
                "subtitle": "The first run includes file I/O and JIT warm-up — it is not representative.",
                "explanation": 'A fair benchmark runs the operation multiple times and takes the median. The first run includes disk reads and Python import time that do not apply in steady-state. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">timeit</code> for reliable comparisons.',
                "wrong_label": "single-run benchmark",
                "wrong_code": 'import time\nstart = time.time()\ndf = pl.read_csv("big.csv")\ndf.group_by("x").agg(pl.col("y").sum())\nprint(time.time() - start)  # includes I/O warm-up',
                "correct_label": "multi-run benchmark",
                "correct_code": 'import timeit\ndef bench():\n    df = pl.read_csv("big.csv")\n    df.group_by("x").agg(pl.col("y").sum())\nt = timeit.timeit(bench, number=5)\nprint(f"Avg: {t / 5:.3f}s")',
                "tip": "Run the benchmark at least 3\u20135 times and use the median. Discard the first run if it includes cold-start I/O.",
            },
        ],
    },

    # ── Lesson 10: DuckDB for Analytics ──
    "lesson10_duckdb_for_analytics.html": {
        "topic": "DuckDB for analytics",
        "mistakes": [
            {
                "tab": "Not Using SQL on Files",
                "title": "Loading a File Into Pandas First and Then Querying With DuckDB",
                "subtitle": "DuckDB can query CSV and Parquet files directly — no intermediate DataFrame needed.",
                "explanation": 'DuckDB reads files natively. Loading into pandas first and then querying the DataFrame adds an unnecessary data copy. Point DuckDB straight at the file for the fastest path.',
                "wrong_label": "pandas middleman",
                "wrong_code": 'import duckdb, pandas as pd\ndf = pd.read_csv("sales.csv")\nresult = duckdb.sql("SELECT region, SUM(amount) FROM df GROUP BY region")',
                "correct_label": "query the file directly",
                "correct_code": 'import duckdb\nresult = duckdb.sql("""\n    SELECT region, SUM(amount)\n    FROM \'sales.csv\'\n    GROUP BY region\n""")',
                "tip": "DuckDB reads CSV, Parquet, and JSON files directly. Skip the pandas step and let DuckDB handle I/O — it is optimised for it.",
            },
            {
                "tab": "Forgetting .fetchdf()",
                "title": "Forgetting to Convert the DuckDB Result to a DataFrame",
                "subtitle": "The raw DuckDB result object is not a pandas DataFrame — you need an explicit conversion.",
                "explanation": 'DuckDB\u2019s <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">sql()</code> returns a DuckDB relation, not a pandas DataFrame. To use the result with pandas, call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.fetchdf()</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.df()</code>.',
                "wrong_label": "raw result object",
                "wrong_code": 'result = duckdb.sql("SELECT * FROM \'sales.csv\'")\nprint(result.head())  # not a DataFrame method',
                "correct_label": "convert to DataFrame",
                "correct_code": 'result = duckdb.sql("SELECT * FROM \'sales.csv\'").df()\nprint(result.head())  # now a pandas DataFrame',
                "tip": "Chain <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.df()</code> at the end of your DuckDB query to get a pandas DataFrame. Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.pl()</code> to get a Polars DataFrame instead.",
            },
            {
                "tab": "SELECT * on Large Files",
                "title": "Running SELECT * on a Multi-Gigabyte File Without Filters or Limits",
                "subtitle": "Loading the entire file defeats the purpose of an analytical query engine.",
                "explanation": 'DuckDB pushes filters and column selections down to the file reader. A <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SELECT *</code> without WHERE or LIMIT loads everything into memory, which is no better than <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_csv()</code>.',
                "wrong_label": "SELECT * no filter",
                "wrong_code": 'result = duckdb.sql("SELECT * FROM \'big.parquet\'").df()\n# loads entire file into memory',
                "correct_label": "filter and select columns",
                "correct_code": 'result = duckdb.sql("""\n    SELECT region, SUM(amount)\n    FROM \'big.parquet\'\n    WHERE year = 2024\n    GROUP BY region\n""").df()',
                "tip": "Always include a WHERE clause or column list when querying large files. DuckDB skips data it does not need — but only if you tell it what you need.",
            },
        ],
    },

    # ── Lesson 11: Parallel Processing ──
    "lesson11_parallel_processing.html": {
        "topic": "parallel processing",
        "mistakes": [
            {
                "tab": "Parallelising Tiny Tasks",
                "title": "Using Multiprocessing for Tasks That Are Too Small to Benefit",
                "subtitle": "The overhead of spawning processes outweighs the speed gain on small data.",
                "explanation": 'Starting a new process takes time: memory copying, serialisation, and IPC. If each task completes in milliseconds, the overhead dominates. Parallelise only when individual tasks take at least a few seconds.',
                "wrong_label": "parallel on tiny data",
                "wrong_code": 'from multiprocessing import Pool\ndef add_one(x): return x + 1\nwith Pool(4) as p:\n    result = p.map(add_one, range(100))  # overhead > work',
                "correct_label": "parallel on real workload",
                "correct_code": 'def process_chunk(chunk):\n    return chunk["amount"].sum()    # meaningful work\nwith Pool(4) as p:\n    results = p.map(process_chunk, big_chunks)',
                "tip": "Time the serial version first. If it takes under a second, parallelism will not help. Focus parallel processing on large, CPU-bound tasks.",
            },
            {
                "tab": "Sharing Mutable State",
                "title": "Sharing a Mutable Object Between Processes Without Synchronisation",
                "subtitle": "Multiple processes writing to the same object causes race conditions and corruption.",
                "explanation": 'Each process in <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">multiprocessing</code> gets its own memory space — writes to a \"shared\" variable in one process are invisible to others. Collect results from each process and merge them in the main process.',
                "wrong_label": "shared mutable list",
                "wrong_code": 'results = []  # not shared across processes\ndef work(chunk):\n    results.append(chunk.sum())  # each process has its own copy',
                "correct_label": "return and collect",
                "correct_code": 'def work(chunk):\n    return chunk["amount"].sum()\nwith Pool(4) as p:\n    results = p.map(work, chunks)  # collected in main process\ntotal = sum(results)',
                "tip": "Always return values from worker functions instead of writing to shared state. The <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">Pool.map()</code> pattern handles collection for you.",
            },
            {
                "tab": "Too Many Processes",
                "title": "Spawning More Processes Than CPU Cores",
                "subtitle": "Extra processes compete for the same cores, adding context-switch overhead.",
                "explanation": 'For CPU-bound work, the optimal number of processes equals your CPU core count. Spawning 16 processes on a 4-core machine means four processes running and twelve waiting, with constant context switching.',
                "wrong_label": "too many processes",
                "wrong_code": 'with Pool(16) as p:  # only 4 cores\n    results = p.map(work, chunks)',
                "correct_label": "match core count",
                "correct_code": 'import os\nwith Pool(os.cpu_count()) as p:  # matches hardware\n    results = p.map(work, chunks)',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">os.cpu_count()</code> to match the number of processes to your hardware. For I/O-bound tasks, threads may be a better fit than processes.",
            },
        ],
    },

    # ── Lesson 12: Dask Basics ──
    "lesson12_dask_basics.html": {
        "topic": "Dask basics",
        "mistakes": [
            {
                "tab": "Calling .compute() Too Early",
                "title": "Calling .compute() After Every Step Instead of Deferring Execution",
                "subtitle": "Premature compute forces Dask to materialise intermediate results, wasting memory and time.",
                "explanation": 'Dask builds a task graph and optimises it before executing. Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.compute()</code> after every step materialises the intermediate DataFrame, which defeats lazy evaluation. Chain operations and compute once at the end.',
                "wrong_label": "compute too early",
                "wrong_code": 'ddf = dd.read_csv("big.csv")\ndf1 = ddf[ddf["active"]].compute()   # materialises here\ndf2 = df1.groupby("dept")["salary"].mean()  # now pandas',
                "correct_label": "defer compute",
                "correct_code": 'result = (\n    dd.read_csv("big.csv")\n    .query("active == True")\n    .groupby("dept")[\"salary\"].mean()\n    .compute()   # one compute at the end\n)',
                "tip": "Think of <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.compute()</code> as the \"go\" button. Build the full pipeline first, then press it once.",
            },
            {
                "tab": "Using Dask for Small Data",
                "title": "Using Dask When Pandas Can Handle the Data in Memory",
                "subtitle": "Dask adds complexity and overhead — use it only when data does not fit in RAM.",
                "explanation": 'Dask shines when datasets exceed your machine\u2019s memory. For a 200 MB file that pandas loads in seconds, Dask\u2019s task scheduling is unnecessary overhead. Stick with pandas for data that fits comfortably in memory.',
                "wrong_label": "Dask on small data",
                "wrong_code": 'import dask.dataframe as dd\nddf = dd.read_csv("small.csv")  # 50 MB file\nresult = ddf.groupby("x").sum().compute()',
                "correct_label": "pandas for small data",
                "correct_code": 'import pandas as pd\ndf = pd.read_csv("small.csv")  # 50 MB file\nresult = df.groupby("x").sum()',
                "tip": "If <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pd.read_csv()</code> loads the file without a MemoryError, you probably do not need Dask. Save Dask for files that are too large for pandas.",
            },
            {
                "tab": "Assuming Full Pandas API",
                "title": "Assuming Dask Supports Every Pandas Method",
                "subtitle": "Some pandas operations are not supported or behave differently in Dask.",
                "explanation": 'Dask implements a subset of the pandas API. Methods like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.iloc[]</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.apply()</code> with complex functions, and some groupby operations behave differently or are unavailable. Check the Dask documentation before assuming compatibility.',
                "wrong_label": "assumes full pandas API",
                "wrong_code": 'ddf = dd.read_csv("big.csv")\nrow = ddf.iloc[42]  # not supported in Dask',
                "correct_label": "use Dask-supported methods",
                "correct_code": 'ddf = dd.read_csv("big.csv")\nsample = ddf.head(5)  # supported — reads first partition',
                "tip": "When a pandas method fails in Dask, check the Dask docs for an alternative. Most common operations have a Dask-compatible counterpart.",
            },
        ],
    },

    # ── Lesson 13: Performance Profiling ──
    "lesson13_performance_profiling.html": {
        "topic": "performance profiling",
        "mistakes": [
            {
                "tab": "Optimising Without Profiling",
                "title": "Optimising Code Without Profiling It First",
                "subtitle": "You might spend hours on a fast section while the real bottleneck goes untouched.",
                "explanation": 'Intuition about what is slow is often wrong. Profile with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">cProfile</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">time.time()</code> to find the actual bottleneck before changing anything.',
                "wrong_label": "guess and optimise",
                "wrong_code": '# "I think reading the file is slow"\ndf = pd.read_parquet("data.parquet")  # actually fast\nresult = df.apply(slow_fn, axis=1)     # actual bottleneck',
                "correct_label": "profile first",
                "correct_code": 'import time\nt0 = time.time()\ndf = pd.read_parquet("data.parquet")\nprint(f"Read: {time.time() - t0:.2f}s")\nt1 = time.time()\nresult = df.apply(slow_fn, axis=1)\nprint(f"Apply: {time.time() - t1:.2f}s")',
                "tip": "Always profile before optimising. The slowest step is rarely where you think it is.",
            },
            {
                "tab": "Single-Run Timing",
                "title": "Timing Code Once Instead of Running Multiple Iterations",
                "subtitle": "A single run includes warm-up, caching, and OS jitter — it is not reliable.",
                "explanation": 'The first run often includes file I/O caching and Python import overhead. Run the operation at least 3\u20135 times and take the median. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">timeit</code> for automated multi-run benchmarks.',
                "wrong_label": "single run",
                "wrong_code": 'import time\nstart = time.time()\nresult = compute()\nprint(f"{time.time() - start:.2f}s")  # one data point',
                "correct_label": "multi-run benchmark",
                "correct_code": 'import timeit\nt = timeit.timeit(compute, number=5)\nprint(f"Avg: {t / 5:.3f}s")',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">timeit</code> for reliable benchmarks. Discard the first run if it includes cold-start I/O.",
            },
            {
                "tab": "Not Acting on Results",
                "title": "Profiling the Code but Not Changing Anything Based on the Results",
                "subtitle": "Profiling is only useful if you act on the findings.",
                "explanation": 'A profile report shows you exactly where time is spent. If the top function takes 80% of the runtime, that is where you optimise. Ignoring the report and \"optimising everywhere\" wastes effort on low-impact changes.',
                "wrong_label": "profile then ignore",
                "wrong_code": 'import cProfile\ncProfile.run("pipeline()")\n# reads the report... changes nothing',
                "correct_label": "profile then fix the hotspot",
                "correct_code": 'import cProfile\ncProfile.run("pipeline()")\n# Report: slow_fn takes 78% of time\n# Fix: replace slow_fn with a vectorised alternative',
                "tip": "After profiling, sort by cumulative time. Fix the top one or two functions and re-profile. Two targeted fixes usually deliver 80% of the speedup.",
            },
        ],
    },

    # ── Lesson 14: Real Large-Data Project ──
    "lesson14_real_large_data_project.html": {
        "topic": "real large-data projects",
        "mistakes": [
            {
                "tab": "No Memory Check",
                "title": "Starting a Large-Data Project Without Checking Memory Requirements",
                "subtitle": "The project crashes halfway when the data exceeds available RAM.",
                "explanation": 'Before processing a multi-gigabyte file, check available memory and the file size. If the data is larger than your RAM, plan for chunking or columnar reads from the start — not after the crash.',
                "wrong_label": "load and hope",
                "wrong_code": 'df = pd.read_csv("10gb_file.csv")  # MemoryError',
                "correct_label": "check size first",
                "correct_code": 'import os\nsize_gb = os.path.getsize("10gb_file.csv") / 1e9\nprint(f"File: {size_gb:.1f} GB")\n# File > RAM → use chunking or Parquet',
                "tip": "A quick file-size check takes one line and saves you from a crash that wipes out unsaved progress.",
            },
            {
                "tab": "Skipping Intermediate Saves",
                "title": "Running the Entire Pipeline Without Saving Intermediate Results",
                "subtitle": "A failure in the last step means redoing everything from scratch.",
                "explanation": 'Save intermediate results (raw extract, cleaned data) as Parquet files between stages. If the pipeline fails at the load step, you restart from the saved checkpoint instead of re-extracting and re-transforming.',
                "wrong_label": "no checkpoints",
                "wrong_code": 'df = extract()    # 20 minutes\ndf = transform(df) # 10 minutes\nload(df)           # fails → redo all 30 minutes',
                "correct_label": "save checkpoints",
                "correct_code": 'df = extract()\ndf.to_parquet("checkpoint_raw.parquet")\ndf = transform(df)\ndf.to_parquet("checkpoint_clean.parquet")\nload(df)  # fails → restart from checkpoint_clean',
                "tip": "Parquet checkpoints are fast to write and read. A 30-second save can prevent a 30-minute restart.",
            },
            {
                "tab": "No Final Validation",
                "title": "Finishing the Project Without Validating the Final Output",
                "subtitle": "The output file or table may contain silent errors that invalidate your results.",
                "explanation": 'After the pipeline finishes, verify the output: row count, column types, null counts, and sample values. A quick sanity check catches issues like dropped rows, wrong aggregations, or type mismatches.',
                "wrong_label": "no final check",
                "wrong_code": 'load(df)  # done — "it ran, so it must be correct"',
                "correct_label": "validate output",
                "correct_code": 'load(df)\ncheck = pd.read_sql("SELECT COUNT(*) FROM summary", engine)\nassert check.iloc[0, 0] > 0, "Output table is empty"\nprint(f"Final rows: {check.iloc[0, 0]}")',
                "tip": "A pipeline that completes without errors is not the same as a pipeline that produces correct output. Always verify the final result.",
            },
        ],
    },

    # ── Lesson 15: Performance Best Practices ──
    "lesson15_performance_best_practices.html": {
        "topic": "performance best practices",
        "mistakes": [
            {
                "tab": "Optimising Too Early",
                "title": "Optimising Code Before It Works Correctly",
                "subtitle": "Premature optimisation adds complexity to code that may still have bugs.",
                "explanation": 'Write correct, readable code first. Profile it, identify the bottleneck, and optimise only that part. Optimising every line from the start makes the code harder to debug and maintain.',
                "wrong_label": "optimise from scratch",
                "wrong_code": '# "Let me use Polars lazy mode, multi-threading,\n#  and Parquet partitioning from line 1"\n# ...but the logic is still wrong',
                "correct_label": "correct first, optimise later",
                "correct_code": '# Step 1: correct pandas code\ndf = pd.read_csv("data.csv")\nresult = df.groupby("region")["amount"].sum()\n# Step 2: profile → slow read → switch to Parquet',
                "tip": "Make it work, make it right, then make it fast — in that order. Optimising broken code is a waste.",
            },
            {
                "tab": "Wrong Tool for the Job",
                "title": "Using pandas for Everything When Specialised Tools Exist",
                "subtitle": "Pandas is not always the fastest choice — DuckDB, Polars, or Dask may be better.",
                "explanation": 'Pandas is excellent for moderate datasets, but it is single-threaded and in-memory. For SQL-style analytics, DuckDB is faster. For parallel processing, Polars or Dask are better. Choose the right tool for the task size and type.',
                "wrong_label": "pandas for everything",
                "wrong_code": 'df = pd.read_csv("5gb_file.csv")  # MemoryError\nresult = df.groupby("x").sum()',
                "correct_label": "match tool to task",
                "correct_code": '# SQL analytics on files → DuckDB\nimport duckdb\nresult = duckdb.sql("""\n    SELECT x, SUM(amount)\n    FROM \'5gb_file.csv\'\n    GROUP BY x\n""").df()',
                "tip": "Learn the strengths of each tool: pandas for exploration, DuckDB for SQL analytics, Polars for speed, and Dask for out-of-memory datasets.",
            },
            {
                "tab": "Measuring After Instead of Before",
                "title": "Measuring Performance After Deployment Instead of During Development",
                "subtitle": "Performance issues found in production are expensive to fix.",
                "explanation": 'Profile during development when you can still change the approach. Discovering a 10x performance problem after deployment means rewriting code under pressure, with users waiting.',
                "wrong_label": "measure in production",
                "wrong_code": '# deploy → users complain it is slow\n# now profiling under pressure',
                "correct_label": "measure during development",
                "correct_code": 'import time\nstart = time.time()\nresult = pipeline(test_data)\nprint(f"Pipeline: {time.time() - start:.2f}s")\n# fix before deploying',
                "tip": "Run your pipeline on a realistic sample during development. If it takes 5 minutes on 1% of the data, it will take hours on the full dataset.",
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
    tabs = "\n".join(
        _tab_btn(i, m["tab"], active=(i == 0))
        for i, m in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{tabs}\n</div>'

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
