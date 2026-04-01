#!/usr/bin/env python3
"""Rewrite #recap section for track_03 mod_04 + mod_05 + mod_06 lessons."""

import re, pathlib

ROOT = pathlib.Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering")
MOD04 = "mod_04_data_pipelines_and_orchestration"
MOD05 = "mod_05_large_scale_data_processing"
MOD06 = "mod_06_automation_and_ci_cd"

PATTERN = re.compile(
    r'(<section id="recap">\s*<div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\s*'
    r'<div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-\[#CB187D\]">.*?</div>\s*</div>\s*)'
    r'<div class="bg-white px-8 py-7 space-y-6">.*?</div>\s*'
    r'(</div>\s*</section>)',
    re.DOTALL
)


def card_html(num, icon, label, sentence):
    n = f"{num:02d}"
    return (
        f'  <!-- Card {n} -->\n'
        f'  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">\n'
        f'    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">\n'
        f'      <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{n}</span>\n'
        f'      <div class="relative flex items-start gap-3">\n'
        f'        <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">\n'
        f'          <span class="iconify text-sm" data-icon="{icon}"></span>\n'
        f'        </span>\n'
        f'        <div>\n'
        f'          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">{label}</p>\n'
        f'          <p class="text-[11px] text-gray-600 leading-snug">{sentence}</p>\n'
        f'        </div>\n'
        f'      </div>\n'
        f'    </div>\n'
        f'  </div>'
    )


BANNER = (
    '<div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">\n'
    '  <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>\n'
    '  <div class="relative flex items-center gap-4">\n'
    '    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">\n'
    '      <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>\n'
    '    </span>\n'
    '    <div>\n'
    '      <p class="text-sm font-bold text-white">Lesson Complete!</p>\n'
    '      <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>\n'
    '    </div>\n'
    '  </div>\n'
    '</div>'
)


def build_body(cards):
    card_blocks = "\n\n".join(card_html(i+1, ic, lb, st) for i,(ic,lb,st) in enumerate(cards))
    grid = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n\n{card_blocks}\n\n</div>'
    return f'<div class="bg-white px-8 py-7 space-y-6">\n\n{grid}\n\n{BANNER}\n\n</div>'


# ── Lesson data ───────────────────────────────────────────────────────────────

LESSONS = {

    # ── MOD 04 — Data Pipelines and Orchestration ─────────────────────────────

    f"{MOD04}/lesson01_what_is_a_data_pipeline.html": [
        ("fa6-solid:diagram-project", "Define a data pipeline",
         "A data pipeline moves raw data through extraction, transformation, and loading stages."),
        ("fa6-solid:building", "Why organisations build them",
         "Automated pipelines replace fragile manual processes and cut hours of repetitive work."),
        ("fa6-solid:layer-group", "Pipeline stages",
         "Extract, transform, and load are the three stages every pipeline follows."),
        ("fa6-solid:laptop-code", "Python in pipelines",
         "Python scripts connect sources, apply transformations, and write to destinations."),
    ],

    f"{MOD04}/lesson02_etl_vs_elt.html": [
        ("fa6-solid:right-left", "ETL vs ELT",
         "ETL transforms before loading; ELT loads raw data then transforms in place."),
        ("fa6-solid:industry", "When to use ETL",
         "Choose ETL when data must be cleaned and shaped before entering the warehouse."),
        ("fa6-solid:cloud-arrow-up", "When to use ELT",
         "Choose ELT when your cloud warehouse can handle heavy transformations after loading."),
        ("fa6-solid:scale-balanced", "Compare architectures",
         "You can evaluate cost, latency, and flexibility to pick the right approach."),
    ],

    f"{MOD04}/lesson03_pipeline_design_patterns.html": [
        ("fa6-solid:cubes", "Common patterns",
         "Linear, fan-out, and merge patterns handle most real-world data flows."),
        ("fa6-solid:clock", "Batch vs streaming",
         "Batch processes data on a schedule; streaming processes it as it arrives."),
        ("fa6-solid:arrows-split-up-and-left", "Fan-out and merge",
         "Fan-out splits one stream into many; merge combines them back together."),
        ("fa6-solid:arrows-rotate", "Idempotent steps",
         "Running an idempotent step twice produces the same result with no duplicates."),
    ],

    f"{MOD04}/lesson04_working_with_large_data_files.html": [
        ("fa6-solid:triangle-exclamation", "Memory constraints",
         "Loading a file bigger than RAM crashes your script without chunk-based reading."),
        ("fa6-solid:puzzle-piece", "Chunk-based processing",
         'Use <code class="font-mono">chunksize</code> in <code class="font-mono">pd.read_csv()</code> to process data in manageable pieces.'),
        ("fa6-solid:filter", "Selective loading",
         'Pass <code class="font-mono">usecols</code> and <code class="font-mono">dtype</code> to load only the columns you need.'),
        ("fa6-solid:file-arrow-down", "Streaming writes",
         "Write each processed chunk to disk immediately so memory stays flat."),
    ],

    f"{MOD04}/lesson05_data_validation_in_pipelines.html": [
        ("fa6-solid:clipboard-check", "Why validate data",
         "Catching bad records early prevents silent errors from reaching your database."),
        ("fa6-solid:spell-check", "Common validation rules",
         "Check for nulls, wrong types, out-of-range values, and duplicate keys."),
        ("fa6-solid:ban", "Reject bad records",
         "Route invalid rows to a quarantine file instead of loading them."),
        ("fa6-solid:file-lines", "Log validation results",
         "Write pass and fail counts to a log so you can audit every run."),
    ],

    f"{MOD04}/lesson09_scheduling_pipelines.html": [
        ("fa6-solid:calendar-check", "Why schedule pipelines",
         "Scheduled runs ensure fresh data arrives automatically without manual triggers."),
        ("fa6-solid:terminal", "Cron and Task Scheduler",
         "Use cron on Linux or Task Scheduler on Windows to trigger scripts."),
        ("fa6-solid:clock-rotate-left", "Run intervals",
         "Set hourly, daily, or weekly intervals that match your data freshness needs."),
        ("fa6-solid:bell", "Monitor scheduled runs",
         "Check exit codes and log files to confirm each run completed successfully."),
    ],

    f"{MOD04}/lesson10_building_a_simple_python_pipeline.html": [
        ("fa6-solid:hammer", "Build end to end",
         "You wired extract, transform, and load functions into one runnable script."),
        ("fa6-solid:download", "Extract from files",
         "Read source CSVs into DataFrames as the first stage of the pipeline."),
        ("fa6-solid:wand-magic-sparkles", "Transform data",
         "Clean columns, filter rows, and add derived fields before loading."),
        ("fa6-solid:database", "Load into SQLite",
         'Call <code class="font-mono">to_sql()</code> to write the final DataFrame into a local database.'),
    ],

    f"{MOD04}/lesson11_pipeline_project_automating_data_ingestion.html": [
        ("fa6-solid:folder-open", "Watch for new files",
         "Scan an inbox folder and pick up only files that have not been processed."),
        ("fa6-solid:clipboard-check", "Validate on arrival",
         "Run schema and value checks before any data enters the database."),
        ("fa6-solid:database", "Load into the database",
         "Insert validated records and skip or quarantine anything that fails checks."),
        ("fa6-solid:file-lines", "Log every step",
         "Timestamped log entries let you trace exactly what happened on each run."),
    ],

    f"{MOD04}/lesson12_pipeline_project_data_quality_checks.html": [
        ("fa6-solid:magnifying-glass", "Detect bad records",
         "Apply null, type, and range checks to flag rows that break your rules."),
        ("fa6-solid:code-branch", "Split good and bad data",
         "Route clean records forward and send rejects to a separate quarantine table."),
        ("fa6-solid:chart-pie", "Quality metrics",
         "Calculate pass rates and reject counts so you can track trends over time."),
        ("fa6-solid:bell", "Alert on failures",
         "Trigger a warning when the reject rate exceeds a configured threshold."),
    ],

    f"{MOD04}/lesson13_pipeline_project_database_loading.html": [
        ("fa6-solid:database", "Load validated data",
         "Write only records that passed quality checks into the destination table."),
        ("fa6-solid:arrows-rotate", "Upsert strategy",
         "Use insert-or-update logic so reruns never create duplicate rows."),
        ("fa6-solid:layer-group", "Raw vs processed tables",
         "Keep raw ingested data separate from cleaned, analysis-ready tables."),
        ("fa6-solid:file-lines", "Audit trail",
         "Record row counts, timestamps, and source files for every load operation."),
    ],

    f"{MOD04}/lesson14_production_pipeline_architecture.html": [
        ("fa6-solid:server", "Production components",
         "A production pipeline combines scheduling, logging, storage, and alerting layers."),
        ("fa6-solid:gears", "Configuration management",
         "Store paths, credentials, and thresholds in config files, not in your code."),
        ("fa6-solid:eye", "Monitoring and alerts",
         "Dashboard metrics and automated alerts catch failures before users notice."),
        ("fa6-solid:shield-halved", "Graceful error recovery",
         "Retry logic and checkpoints let your pipeline resume instead of restarting."),
    ],

    # ── MOD 05 — Large-Scale Data Processing ──────────────────────────────────

    f"{MOD05}/lesson02_memory_optimization.html": [
        ("fa6-solid:memory", "Measure memory usage",
         'Use <code class="font-mono">df.memory_usage(deep=True)</code> to see exactly how many bytes each column takes.'),
        ("fa6-solid:arrow-down-short-wide", "Downcast numeric types",
         'Convert <code class="font-mono">int64</code> to <code class="font-mono">int32</code> or smaller to cut memory by half or more.'),
        ("fa6-solid:tags", "Use category dtype",
         'Switch low-cardinality string columns to <code class="font-mono">category</code> for massive savings.'),
        ("fa6-solid:trash-can", "Drop unneeded columns",
         "Remove columns you will never query so they stop consuming memory."),
    ],

    f"{MOD05}/lesson03_chunk_processing.html": [
        ("fa6-solid:puzzle-piece", "What chunk processing is",
         "Reading data in fixed-size pieces lets you process files larger than RAM."),
        ("fa6-solid:file-import", "Read CSV in chunks",
         'Pass <code class="font-mono">chunksize</code> to <code class="font-mono">pd.read_csv()</code> and iterate over each batch.'),
        ("fa6-solid:calculator", "Aggregate across chunks",
         "Accumulate partial results in a loop, then combine them at the end."),
        ("fa6-solid:scale-balanced", "Choose the right chunk size",
         "Balance memory headroom against per-chunk overhead to find the sweet spot."),
    ],

    f"{MOD05}/lesson04_processing_millions_of_rows.html": [
        ("fa6-solid:bolt", "Vectorised operations",
         "Pandas vectorised methods run compiled C code across entire columns at once."),
        ("fa6-solid:ban", "Avoid slow loops",
         'Replace Python <code class="font-mono">for</code> loops with <code class="font-mono">.apply()</code> or vectorised expressions.'),
        ("fa6-solid:gauge-high", "Time your code",
         'Use <code class="font-mono">%%timeit</code> or <code class="font-mono">time.perf_counter()</code> to measure real execution speed.'),
        ("fa6-solid:layer-group", "Batch processing strategies",
         "Split large jobs into batches so each one fits comfortably in memory."),
    ],

    f"{MOD05}/lesson05_columnar_storage.html": [
        ("fa6-solid:table-columns", "Row vs column storage",
         "Row stores write fast; column stores read and compress analytical data better."),
        ("fa6-solid:bolt", "Faster analytics queries",
         "Columnar files skip irrelevant columns, making aggregation queries much faster."),
        ("fa6-solid:file-zipper", "Better compression",
         "Identical values in a column compress far better than mixed-type rows."),
        ("fa6-solid:database", "Where columnar is used",
         "Data warehouses, Parquet files, and analytics engines all rely on columnar storage."),
    ],

    f"{MOD05}/lesson06_parquet_files.html": [
        ("fa6-solid:file-zipper", "Read and write Parquet",
         'Call <code class="font-mono">to_parquet()</code> and <code class="font-mono">read_parquet()</code> for fast columnar file I/O.'),
        ("fa6-solid:filter", "Select columns on read",
         'Pass a <code class="font-mono">columns</code> list to load only the fields your analysis needs.'),
        ("fa6-solid:magnifying-glass-chart", "Inspect metadata",
         "Read row counts, schema, and statistics from the file header without scanning data."),
        ("fa6-solid:right-left", "Compare with CSV",
         "Parquet files are smaller, faster to read, and preserve column types automatically."),
    ],

    f"{MOD05}/lesson07_pyarrow_basics.html": [
        ("fa6-solid:feather", "What PyArrow is",
         "PyArrow is a library for fast, memory-efficient columnar data operations in Python."),
        ("fa6-solid:table", "Create Arrow tables",
         'Build a <code class="font-mono">pa.Table</code> from dictionaries, lists, or pandas DataFrames.'),
        ("fa6-solid:right-left", "Convert to pandas",
         'Call <code class="font-mono">.to_pandas()</code> to move Arrow data back into a familiar DataFrame.'),
        ("fa6-solid:file-lines", "Read Parquet metadata",
         "Inspect schemas, row-group sizes, and column stats without loading the full file."),
    ],

    f"{MOD05}/lesson08_introduction_to_polars.html": [
        ("fa6-solid:bolt", "What Polars is",
         "Polars is a Rust-powered DataFrame library built for speed and low memory use."),
        ("fa6-solid:laptop-code", "Basic Polars operations",
         'Use <code class="font-mono">select</code>, <code class="font-mono">filter</code>, and <code class="font-mono">group_by</code> to query data in Polars.'),
        ("fa6-solid:gauge-high", "Speed and memory",
         "Polars processes millions of rows faster than pandas on the same hardware."),
        ("fa6-solid:code-compare", "Polars vs pandas",
         "Polars uses expressions and lazy evaluation; pandas uses eager column methods."),
    ],

    f"{MOD05}/lesson09_faster_dataframes_with_polars.html": [
        ("fa6-solid:wand-magic-sparkles", "Lazy evaluation",
         'Call <code class="font-mono">.lazy()</code> to build a query plan Polars optimises before executing.'),
        ("fa6-solid:link", "Expression chaining",
         "Chain multiple transformations into one readable, efficient expression pipeline."),
        ("fa6-solid:microchip", "Multi-threaded execution",
         "Polars splits work across CPU cores automatically with no extra code."),
        ("fa6-solid:chart-line", "Benchmark against pandas",
         "Time both libraries on the same task to see when Polars gives the biggest win."),
    ],

    f"{MOD05}/lesson10_duckdb_for_analytics.html": [
        ("fa6-solid:database", "What DuckDB is",
         "DuckDB is an in-process analytics database you run with zero server setup."),
        ("fa6-solid:file-code", "SQL on files",
         "Query CSV and Parquet files directly with SQL, no loading step required."),
        ("fa6-solid:right-left", "Integrate with pandas",
         'Pass a DataFrame to <code class="font-mono">duckdb.sql()</code> and get results back as a DataFrame.'),
        ("fa6-solid:bolt", "Performance advantages",
         "DuckDB\u2019s columnar engine runs analytical queries far faster than row-at-a-time tools."),
    ],

    f"{MOD05}/lesson11_parallel_processing.html": [
        ("fa6-solid:microchip", "What parallel processing is",
         "Running tasks on multiple CPU cores at the same time to finish faster."),
        ("fa6-solid:gears", "concurrent.futures",
         'Use <code class="font-mono">ProcessPoolExecutor</code> to fan work out across cores in a few lines.'),
        ("fa6-solid:code-branch", "multiprocessing module",
         'The <code class="font-mono">multiprocessing</code> module gives finer control over processes, queues, and shared state.'),
        ("fa6-solid:triangle-exclamation", "Pitfalls and overhead",
         "Spawning processes has a startup cost, so small tasks may run slower in parallel."),
    ],

    f"{MOD05}/lesson12_dask_basics.html": [
        ("fa6-solid:cubes", "What Dask is",
         "Dask scales pandas-like code across multiple cores or machines transparently."),
        ("fa6-solid:table", "Dask DataFrames",
         "A Dask DataFrame splits one large table into many partitions processed in parallel."),
        ("fa6-solid:diagram-project", "Task graphs",
         "Dask builds a directed graph of operations and executes them lazily on demand."),
        ("fa6-solid:scale-balanced", "When to use Dask",
         "Choose Dask when your data outgrows pandas but does not need a full cluster."),
    ],

    f"{MOD05}/lesson13_performance_profiling.html": [
        ("fa6-solid:stopwatch", "Time your code",
         'Wrap critical sections with <code class="font-mono">time.perf_counter()</code> to spot the slowest parts.'),
        ("fa6-solid:microscope", "Profile with cProfile",
         'Run <code class="font-mono">cProfile.run()</code> to see which functions consume the most time.'),
        ("fa6-solid:chart-bar", "Line-level profiling",
         "Use a line profiler to find the exact lines where your code stalls."),
        ("fa6-solid:wrench", "Act on the results",
         "Focus optimisation effort on the one or two hotspots the profiler reveals."),
    ],

    f"{MOD05}/lesson14_real_large_data_project.html": [
        ("fa6-solid:flask", "End-to-end project",
         "You built a complete pipeline that ingests, transforms, and exports large data."),
        ("fa6-solid:memory", "Optimise memory first",
         "Downcasting and category types freed enough RAM to process the full dataset."),
        ("fa6-solid:bolt", "Process at scale",
         "Vectorised operations and chunked reads handled millions of rows efficiently."),
        ("fa6-solid:file-export", "Export final results",
         "Saved the cleaned dataset to Parquet for fast, compact downstream analysis."),
    ],

    f"{MOD05}/lesson15_performance_best_practices.html": [
        ("fa6-solid:file-zipper", "Choose the right format",
         "Parquet beats CSV for analytics; CSV stays useful for simple data exchange."),
        ("fa6-solid:code-compare", "Pick the right library",
         "Match the library to the job: pandas for small data, Polars or DuckDB for large."),
        ("fa6-solid:memory", "Manage memory early",
         "Downcast types and drop unused columns before any heavy processing begins."),
        ("fa6-solid:gauge-high", "Measure before optimising",
         "Profile first so you spend effort on the bottleneck, not the wrong function."),
    ],

    # ── MOD 06 — Automation and CI/CD ─────────────────────────────────────────

    f"{MOD06}/lesson01_devops_concepts_for_data_analytics.html": [
        ("fa6-solid:gears", "What DevOps means",
         "DevOps combines development and operations to ship reliable software faster."),
        ("fa6-solid:arrows-rotate", "DevOps for data teams",
         "Data teams use the same version control, testing, and deployment practices."),
        ("fa6-solid:robot", "Automation benefits",
         "Automated pipelines eliminate manual steps and reduce the risk of human error."),
        ("fa6-solid:server", "Deployment basics",
         "Deploying means moving tested code from your machine to a production server."),
    ],

    f"{MOD06}/lesson02_gitlab_ci_cd_overview.html": [
        ("fa6-solid:code-branch", "What CI/CD is",
         "Continuous integration and delivery automate testing and deployment on every commit."),
        ("fa6-solid:file-code", "The .gitlab-ci.yml file",
         'Define pipeline stages, jobs, and scripts inside one <code class="font-mono">.gitlab-ci.yml</code> file.'),
        ("fa6-solid:vials", "Automated testing",
         "Every push triggers tests automatically so broken code never reaches production."),
        ("fa6-solid:rocket", "Automated deployment",
         "Passing tests trigger a deploy job that pushes your code to the server."),
    ],

    f"{MOD06}/lesson03_scheduling_data_jobs.html": [
        ("fa6-solid:calendar-check", "Why schedule jobs",
         "Scheduled runs ensure fresh data is ready before anyone opens a dashboard."),
        ("fa6-solid:terminal", "Cron and Task Scheduler",
         "Use cron on Linux or Task Scheduler on Windows to trigger scripts on time."),
        ("fa6-solid:clock-rotate-left", "CI/CD triggers",
         "GitLab scheduled pipelines can run your data jobs without a dedicated server."),
        ("fa6-solid:bell", "Monitor and alert",
         "Set up notifications so you know immediately when a scheduled job fails."),
    ],

    f"{MOD06}/lesson05_deployment_workflow.html": [
        ("fa6-solid:code-branch", "Development to production",
         "Code moves from a feature branch through review and testing to production."),
        ("fa6-solid:vials", "Test before deploying",
         "Automated tests catch bugs in the pipeline before they affect real data."),
        ("fa6-solid:rocket", "Deploy with CI/CD",
         "A passing pipeline automatically promotes your code to the production environment."),
        ("fa6-solid:shield-halved", "Rollback strategy",
         "Tag every release so you can revert to the last working version instantly."),
    ],
}


# ── Main ──────────────────────────────────────────────────────────────────────

assert len(LESSONS) == 29, f"Expected 29 lessons, got {len(LESSONS)}"

ok = fail = 0
for rel, cards in LESSONS.items():
    path = ROOT / rel
    if not path.exists():
        print(f"\u274c NOT FOUND  {rel}")
        fail += 1
        continue
    text = path.read_text(encoding="utf-8")
    body = build_body(cards)
    new_text, n = PATTERN.subn(lambda m: m.group(1) + body + "\n" + m.group(2), text, count=1)
    if n == 0:
        print(f"\u274c NO MATCH   {rel}")
        fail += 1
        continue
    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {rel}")
    ok += 1

print(f"\n{ok}/{ok + fail} recap sections rewritten")
