"""Rewrite #next-lesson section + bottom nav for every lesson in track_03."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_03_data_engineering")
HUB_PATH = "../../../hub_home_page.html"

# ── Regex patterns ───────────────────────────────────────────────
# Pattern 1: file HAS #next-lesson — grab from there to just before </main>
RE_WITH_NL = re.compile(
    r'\s*<section id="next-lesson".*?(?=\s*</main>)',
    re.DOTALL,
)
# Pattern 2: file has NO #next-lesson — grab the bare bottom-nav div before </main>
RE_NAV_ONLY = re.compile(
    r'\s*<div class="flex flex-col sm:flex-row[^"]*">.*?(?=\s*</main>)',
    re.DOTALL,
)


# ── HTML builders ────────────────────────────────────────────────

def build_next_section(nxt):
    """Build #next-lesson section for a lesson whose NEXT lesson is `nxt`."""
    return f'''
<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">{nxt["lesson_num"]}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module {nxt["mod_num"]} &middot; Lesson {nxt["lesson_num"]}</p>
          <h3 class="text-base font-bold text-gray-800">{nxt["title"]}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="{nxt["cards"][0][0]}"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">{nxt["cards"][0][1]}</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="{nxt["cards"][1][0]}"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">{nxt["cards"][1][1]}</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="{nxt["cards"][2][0]}"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">{nxt["cards"][2][1]}</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>'''


def build_track_complete_section():
    """Build #next-lesson section for the very last lesson of the track."""
    return '''
<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Track Complete</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">You have finished the Data Engineering track</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Congratulations!</p>
            <p class="text-xs text-white/80 mt-0.5">You have completed all lessons in the Data Engineering track. Head back to the hub to explore other tracks.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''


def build_bottom_nav(prev_info, next_info):
    """Build the bottom navigation bar section."""
    # Previous slot
    if prev_info:
        prev_html = f'''    <a href="{prev_info["href"]}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{prev_info["title"]}</p>
      </div>
    </a>'''
    else:
        prev_html = '    <div class="flex-1"></div>'

    # Hub link (always present)
    hub_html = f'''    <a href="{HUB_PATH}" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>'''

    # Next slot
    if next_info:
        next_html = f'''    <a href="{next_info["href"]}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{next_info["title"]}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>'''
    else:
        next_html = ''

    return f'''
<section>
  <div class="flex flex-col sm:flex-row gap-3">

{prev_html}

{hub_html}

{next_html}

  </div>
</section>'''


# ── Lesson registry (ordered sequence) ───────────────────────────
# Each entry: (mod_dir, mod_num, filename, title, cards)
# cards = [(icon, text), (icon, text), (icon, text)]

ALL_LESSONS = [
    # ═══ MODULE 01 — Data Engineering Foundations ═══════════════
    ("mod_01_data_engineering_foundations", 1,
     "lesson01_what_is_data_engineering.html",
     "What Is Data Engineering?",
     [("fa6-solid:gears", "The Role of a Data Engineer"),
      ("fa6-solid:arrows-split-up-and-left", "Data Engineering vs Data Science"),
      ("fa6-solid:diagram-project", "Pipelines, Tools &amp; Infrastructure")]),

    ("mod_01_data_engineering_foundations", 1,
     "lesson02_etl_vs_elt.html",
     "ETL vs ELT",
     [("fa6-solid:right-left", "ETL and ELT Defined"),
      ("fa6-solid:industry", "How Transform Timing Differs"),
      ("fa6-solid:scale-balanced", "Choosing the Right Architecture")]),

    ("mod_01_data_engineering_foundations", 1,
     "lesson03_handling_large_datasets.html",
     "Handling Large Datasets",
     [("fa6-solid:memory", "Memory Limits &amp; Why Files Crash"),
      ("fa6-solid:puzzle-piece", "Reading Files in Chunks"),
      ("fa6-solid:filter", "Selective Loading &amp; Type Downcasting")]),

    ("mod_01_data_engineering_foundations", 1,
     "lesson05_parquet_efficient_storage.html",
     "Parquet &amp; Efficient Storage",
     [("fa6-solid:file-zipper", "What Parquet Is &amp; Why It Matters"),
      ("fa6-solid:database", "Columnar Storage Benefits"),
      ("fa6-solid:arrow-right-arrow-left", "Converting Between CSV &amp; Parquet")]),

    ("mod_01_data_engineering_foundations", 1,
     "lesson06_intro_to_polars_optional.html",
     "Intro to Polars (Optional)",
     [("fa6-solid:bolt", "What Polars Is"),
      ("fa6-solid:gauge-high", "Speed &amp; Memory Advantages"),
      ("fa6-solid:code-compare", "Polars vs Pandas Comparison")]),

    ("mod_01_data_engineering_foundations", 1,
     "lesson07_pipeline_design_concepts.html",
     "Pipeline Design Concepts",
     [("fa6-solid:diagram-project", "Pipeline Stages &amp; Structure"),
      ("fa6-solid:cubes", "Modular, Testable Design"),
      ("fa6-solid:shield-halved", "Error Handling &amp; Idempotency")]),

    # ═══ MODULE 02 — NoSQL and Modern Data Storage ══════════════
    ("mod_02_nosql_and_modern_data_storage", 2,
     "lesson01_what_is_nosql.html",
     "What is NoSQL?",
     [("fa6-solid:database", "NoSQL Databases Defined"),
      ("fa6-solid:right-left", "How NoSQL Differs from SQL"),
      ("fa6-solid:bullseye", "Use Cases for NoSQL")]),

    ("mod_02_nosql_and_modern_data_storage", 2,
     "lesson02_types_of_nosql_databases.html",
     "Types of NoSQL Databases",
     [("fa6-solid:layer-group", "Four NoSQL Families"),
      ("fa6-solid:box-open", "How Each Type Stores Data"),
      ("fa6-solid:map-signs", "Matching Types to Problems")]),

    ("mod_02_nosql_and_modern_data_storage", 2,
     "lesson03_document_databases_mongodb.html",
     "Document Databases (MongoDB)",
     [("fa6-solid:file-lines", "The Document Data Model"),
      ("fa6-solid:pen-to-square", "Inserting &amp; Querying Documents"),
      ("fa6-solid:table-columns", "Documents vs SQL Tables")]),

    ("mod_02_nosql_and_modern_data_storage", 2,
     "lesson04_key_value_databases_redis.html",
     "Key-Value Databases (Redis)",
     [("fa6-solid:key", "The Key-Value Data Model"),
      ("fa6-solid:bolt", "In-Memory Speed &amp; Operations"),
      ("fa6-solid:clock-rotate-left", "Caching &amp; Real-Time Use Cases")]),

    ("mod_02_nosql_and_modern_data_storage", 2,
     "lesson05_column_family_databases_cassandra.html",
     "Column-Family Databases (Cassandra)",
     [("fa6-solid:table-cells", "The Column-Family Model"),
      ("fa6-solid:server", "Distributed Architecture"),
      ("fa6-solid:chart-line", "High-Throughput Write Scenarios")]),

    ("mod_02_nosql_and_modern_data_storage", 2,
     "lesson06_graph_databases_neo4j.html",
     "Graph Databases (Neo4j)",
     [("fa6-solid:circle-nodes", "Nodes, Edges &amp; Relationships"),
      ("fa6-solid:magnifying-glass", "Cypher Query Language"),
      ("fa6-solid:users", "Social Networks &amp; Fraud Detection")]),

    ("mod_02_nosql_and_modern_data_storage", 2,
     "lesson07_sql_vs_nosql_choosing_the_right_database.html",
     "SQL vs NoSQL: Choosing the Right Database",
     [("fa6-solid:scale-balanced", "SQL vs NoSQL Trade-Offs"),
      ("fa6-solid:list-check", "A Practical Decision Checklist"),
      ("fa6-solid:diagram-project", "Polyglot Persistence")]),

    # ═══ MODULE 03 — API Data Integration ═══════════════════════
    ("mod_03_api_data_integration", 3,
     "lesson01_what_is_an_api.html",
     "What is an API?",
     [("fa6-solid:plug", "APIs Defined"),
      ("fa6-solid:arrows-left-right", "The Request-Response Cycle"),
      ("fa6-solid:laptop-code", "Python &amp; APIs")]),

    ("mod_03_api_data_integration", 3,
     "lesson02_understanding_http_requests.html",
     "Understanding HTTP Requests",
     [("fa6-solid:globe", "How HTTP Works"),
      ("fa6-solid:list-ol", "Methods, Status Codes &amp; Headers"),
      ("fa6-solid:sliders", "Query Parameters &amp; Customisation")]),

    ("mod_03_api_data_integration", 3,
     "lesson03_using_the_python_requests_library.html",
     "Using the Python requests Library",
     [("fa6-solid:download", "Installing &amp; Importing requests"),
      ("fa6-solid:paper-plane", "Sending GET &amp; POST Requests"),
      ("fa6-solid:file-code", "Inspecting &amp; Parsing Responses")]),

    ("mod_03_api_data_integration", 3,
     "lesson04_working_with_json_data.html",
     "Working with JSON Data",
     [("fa6-solid:brackets-curly", "JSON Structure &amp; Syntax"),
      ("fa6-solid:sitemap", "Navigating Nested Data"),
      ("fa6-solid:file-export", "Reading &amp; Writing JSON in Python")]),

    ("mod_03_api_data_integration", 3,
     "lesson05_parsing_api_responses.html",
     "Parsing API Responses",
     [("fa6-solid:triangle-exclamation", "Status Codes &amp; Error Handling"),
      ("fa6-solid:layer-group", "Extracting Nested Data"),
      ("fa6-solid:table", "Building Clean Datasets")]),

    ("mod_03_api_data_integration", 3,
     "lesson06_authentication_with_api_keys.html",
     "Authentication with API Keys",
     [("fa6-solid:lock", "Why APIs Require Authentication"),
      ("fa6-solid:key", "API Keys &amp; How to Send Them"),
      ("fa6-solid:vault", "Secure Key Storage")]),

    ("mod_03_api_data_integration", 3,
     "lesson07_oauth_authentication.html",
     "OAuth Authentication",
     [("fa6-solid:user-shield", "What OAuth Is"),
      ("fa6-solid:arrows-rotate", "The Token-Based Auth Flow"),
      ("fa6-solid:laptop-code", "OAuth in Python")]),

    ("mod_03_api_data_integration", 3,
     "lesson08_handling_pagination_in_apis.html",
     "Handling Pagination in APIs",
     [("fa6-solid:book-open", "Why APIs Paginate Results"),
      ("fa6-solid:forward", "Looping Through Pages"),
      ("fa6-solid:list-check", "Collecting Complete Datasets")]),

    ("mod_03_api_data_integration", 3,
     "lesson09_handling_api_rate_limits.html",
     "Handling API Rate Limits",
     [("fa6-solid:gauge-high", "What Rate Limits Are"),
      ("fa6-solid:clock", "Delays, Retries &amp; Backoff"),
      ("fa6-solid:shield-halved", "Building Resilient Scripts")]),

    ("mod_03_api_data_integration", 3,
     "lesson10_loading_api_data_into_pandas.html",
     "Loading API Data into Pandas",
     [("fa6-solid:table", "JSON to DataFrame Conversion"),
      ("fa6-solid:filter", "Cleaning &amp; Filtering API Data"),
      ("fa6-solid:file-csv", "Exporting for Reuse")]),

    ("mod_03_api_data_integration", 3,
     "lesson11_saving_api_data_to_databases.html",
     "Saving API Data to Databases",
     [("fa6-solid:database", "Storing Data in SQLite"),
      ("fa6-solid:arrows-rotate", "Upsert &amp; Deduplication Logic"),
      ("fa6-solid:magnifying-glass", "Querying Stored API Data")]),

    ("mod_03_api_data_integration", 3,
     "lesson12_building_an_api_data_pipeline.html",
     "Building an API Data Pipeline",
     [("fa6-solid:diagram-project", "Pipeline Structure: Extract, Transform, Load"),
      ("fa6-solid:wand-magic-sparkles", "Transforming Raw API Data"),
      ("fa6-solid:database", "Loading into a Database")]),

    ("mod_03_api_data_integration", 3,
     "lesson13_real_world_api_integration_project.html",
     "Real-World API Integration Project",
     [("fa6-solid:flask", "A Complete API Pipeline Project"),
      ("fa6-solid:shield-halved", "Real-World Error Handling"),
      ("fa6-solid:database", "Persisting Data for Analysis")]),

    ("mod_03_api_data_integration", 3,
     "lesson14_api_best_practices.html",
     "API Best Practices",
     [("fa6-solid:shield-halved", "Defensive Error Handling"),
      ("fa6-solid:file-lines", "Logging &amp; Monitoring"),
      ("fa6-solid:vault", "Credential Management")]),

    # ═══ MODULE 04 — Data Pipelines and Orchestration ═══════════
    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson01_what_is_a_data_pipeline.html",
     "What is a Data Pipeline?",
     [("fa6-solid:diagram-project", "Data Pipelines Defined"),
      ("fa6-solid:layer-group", "Extract, Transform &amp; Load Stages"),
      ("fa6-solid:laptop-code", "Python in Pipeline Building")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson02_etl_vs_elt.html",
     "ETL vs ELT",
     [("fa6-solid:right-left", "ETL vs ELT Compared"),
      ("fa6-solid:industry", "When to Transform Before Loading"),
      ("fa6-solid:cloud-arrow-up", "When to Load Before Transforming")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson03_pipeline_design_patterns.html",
     "Pipeline Design Patterns",
     [("fa6-solid:cubes", "Batch, Streaming &amp; Fan-Out Patterns"),
      ("fa6-solid:arrows-split-up-and-left", "Parallel Branches &amp; Merges"),
      ("fa6-solid:arrows-rotate", "Idempotent Pipeline Steps")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson04_working_with_large_data_files.html",
     "Working with Large Data Files",
     [("fa6-solid:triangle-exclamation", "Memory Constraints &amp; Crashes"),
      ("fa6-solid:puzzle-piece", "Chunk-Based Processing"),
      ("fa6-solid:file-arrow-down", "Streaming Writes to Disk")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson05_data_validation_in_pipelines.html",
     "Data Validation in Pipelines",
     [("fa6-solid:clipboard-check", "Why Validate Pipeline Data"),
      ("fa6-solid:spell-check", "Common Validation Rules"),
      ("fa6-solid:ban", "Rejecting &amp; Quarantining Bad Data")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson09_scheduling_pipelines.html",
     "Scheduling Pipelines",
     [("fa6-solid:calendar-check", "Why Schedule Pipelines"),
      ("fa6-solid:terminal", "Cron Jobs &amp; Task Scheduler"),
      ("fa6-solid:bell", "Monitoring Scheduled Runs")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson10_building_a_simple_python_pipeline.html",
     "Building a Simple Python Pipeline",
     [("fa6-solid:hammer", "Building a Pipeline End to End"),
      ("fa6-solid:wand-magic-sparkles", "Extract, Transform &amp; Load in Code"),
      ("fa6-solid:database", "Loading Results into SQLite")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson11_pipeline_project_automating_data_ingestion.html",
     "Pipeline Project: Automating Data Ingestion",
     [("fa6-solid:folder-open", "Watching for New Files"),
      ("fa6-solid:clipboard-check", "Validating on Arrival"),
      ("fa6-solid:database", "Loading into the Database")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson12_pipeline_project_data_quality_checks.html",
     "Pipeline Project: Data Quality Checks",
     [("fa6-solid:magnifying-glass", "Detecting Bad Records"),
      ("fa6-solid:code-branch", "Splitting Good &amp; Bad Data"),
      ("fa6-solid:bell", "Quality Metrics &amp; Alerts")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson13_pipeline_project_database_loading.html",
     "Pipeline Project: Database Loading",
     [("fa6-solid:database", "Loading Validated Data"),
      ("fa6-solid:arrows-rotate", "Upsert &amp; Deduplication Strategy"),
      ("fa6-solid:file-lines", "Audit Trails &amp; Logging")]),

    ("mod_04_data_pipelines_and_orchestration", 4,
     "lesson14_production_pipeline_architecture.html",
     "Production Pipeline Architecture",
     [("fa6-solid:server", "Production Pipeline Components"),
      ("fa6-solid:gears", "Configuration &amp; Environment Variables"),
      ("fa6-solid:shield-halved", "Monitoring &amp; Error Recovery")]),

    # ═══ MODULE 05 — Large Scale Data Processing ════════════════
    ("mod_05_large_scale_data_processing", 5,
     "lesson02_memory_optimization.html",
     "Memory Optimization",
     [("fa6-solid:memory", "Measuring Memory Usage"),
      ("fa6-solid:arrow-down-short-wide", "Downcasting &amp; Category Types"),
      ("fa6-solid:trash-can", "Dropping Unneeded Columns")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson03_chunk_processing.html",
     "Chunk Processing",
     [("fa6-solid:puzzle-piece", "What Chunk Processing Is"),
      ("fa6-solid:file-import", "Reading Large CSVs in Batches"),
      ("fa6-solid:calculator", "Aggregating Across Chunks")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson04_processing_millions_of_rows.html",
     "Processing Millions of Rows",
     [("fa6-solid:bolt", "Vectorised pandas Operations"),
      ("fa6-solid:ban", "Avoiding Slow Python Loops"),
      ("fa6-solid:gauge-high", "Timing &amp; Benchmarking")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson05_columnar_storage.html",
     "Columnar Storage",
     [("fa6-solid:table-columns", "Row vs Column Storage"),
      ("fa6-solid:bolt", "Faster Analytics Queries"),
      ("fa6-solid:file-zipper", "Compression Benefits")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson06_parquet_files.html",
     "Parquet Files",
     [("fa6-solid:file-zipper", "Reading &amp; Writing Parquet"),
      ("fa6-solid:filter", "Selective Column Loading"),
      ("fa6-solid:right-left", "Parquet vs CSV Comparison")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson07_pyarrow_basics.html",
     "PyArrow Basics",
     [("fa6-solid:feather", "What PyArrow Is"),
      ("fa6-solid:table", "Arrow Tables &amp; Schema"),
      ("fa6-solid:right-left", "Converting Between Formats")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson08_introduction_to_polars.html",
     "Introduction to Polars",
     [("fa6-solid:bolt", "What Polars Is"),
      ("fa6-solid:laptop-code", "Basic Polars Operations"),
      ("fa6-solid:code-compare", "Polars vs Pandas")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson09_faster_dataframes_with_polars.html",
     "Faster DataFrames with Polars",
     [("fa6-solid:wand-magic-sparkles", "Lazy Evaluation &amp; Query Plans"),
      ("fa6-solid:link", "Expression Chaining"),
      ("fa6-solid:microchip", "Multi-Threaded Execution")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson10_duckdb_for_analytics.html",
     "DuckDB for Analytics",
     [("fa6-solid:database", "What DuckDB Is"),
      ("fa6-solid:file-code", "SQL Queries on Local Files"),
      ("fa6-solid:right-left", "DuckDB &amp; Pandas Integration")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson11_parallel_processing.html",
     "Parallel Processing",
     [("fa6-solid:microchip", "Splitting Work Across Cores"),
      ("fa6-solid:gears", "concurrent.futures &amp; multiprocessing"),
      ("fa6-solid:triangle-exclamation", "Overhead &amp; When to Parallelise")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson12_dask_basics.html",
     "Dask Basics",
     [("fa6-solid:cubes", "What Dask Is"),
      ("fa6-solid:table", "Dask DataFrames"),
      ("fa6-solid:diagram-project", "Task Graphs &amp; Parallel Execution")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson13_performance_profiling.html",
     "Performance Profiling",
     [("fa6-solid:stopwatch", "Timing Your Code"),
      ("fa6-solid:microscope", "cProfile &amp; Line Profiling"),
      ("fa6-solid:wrench", "Acting on Profiling Results")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson14_real_large_data_project.html",
     "Real Large Data Project",
     [("fa6-solid:flask", "A Complete Large-Data Project"),
      ("fa6-solid:bolt", "Optimise, Process &amp; Export"),
      ("fa6-solid:file-export", "Final Results to Parquet &amp; CSV")]),

    ("mod_05_large_scale_data_processing", 5,
     "lesson15_performance_best_practices.html",
     "Performance Best Practices",
     [("fa6-solid:file-zipper", "Choosing the Right File Format"),
      ("fa6-solid:code-compare", "Picking the Right Library"),
      ("fa6-solid:gauge-high", "Measure Before Optimising")]),

    # ═══ MODULE 06 — Automation and CI/CD ═══════════════════════
    ("mod_06_automation_and_ci_cd", 6,
     "lesson01_devops_concepts_for_data_analytics.html",
     "DevOps Concepts for Data &amp; Analytics",
     [("fa6-solid:gears", "What DevOps Means"),
      ("fa6-solid:arrows-rotate", "DevOps for Data Teams"),
      ("fa6-solid:server", "Deployment Basics")]),

    ("mod_06_automation_and_ci_cd", 6,
     "lesson02_gitlab_ci_cd_overview.html",
     "GitLab CI/CD Overview",
     [("fa6-solid:code-branch", "What CI/CD Is"),
      ("fa6-solid:file-code", "The .gitlab-ci.yml File"),
      ("fa6-solid:rocket", "Automated Testing &amp; Deployment")]),

    ("mod_06_automation_and_ci_cd", 6,
     "lesson03_scheduling_data_jobs.html",
     "Scheduling Data Jobs",
     [("fa6-solid:calendar-check", "Why Schedule Data Jobs"),
      ("fa6-solid:terminal", "Cron, Task Scheduler &amp; CI/CD"),
      ("fa6-solid:bell", "Monitoring &amp; Alerts")]),

    ("mod_06_automation_and_ci_cd", 6,
     "lesson05_deployment_workflow.html",
     "Deployment Workflow",
     [("fa6-solid:code-branch", "Development to Production"),
      ("fa6-solid:rocket", "Deploying with CI/CD"),
      ("fa6-solid:shield-halved", "Rollback &amp; Recovery")]),
]


def get_lesson_num(filename):
    """Extract numeric lesson number from filename."""
    m = re.search(r"lesson(\d+)", filename)
    return int(m.group(1)) if m else 0


def rel_path(from_mod_dir, to_mod_dir, to_filename):
    """Compute relative path between two lesson files."""
    if from_mod_dir == to_mod_dir:
        return to_filename
    return f"../{to_mod_dir}/{to_filename}"


def main():
    ok = 0
    total = len(ALL_LESSONS)

    for i, (mod_dir, mod_num, filename, title, cards) in enumerate(ALL_LESSONS):
        fpath = ROOT / mod_dir / filename
        if not fpath.exists():
            print(f"  SKIP  {mod_dir}/{filename} (not found)")
            continue

        html = fpath.read_text(encoding="utf-8")

        # ── Build the next-lesson section ────────────────────────
        is_last = (i == len(ALL_LESSONS) - 1)

        if is_last:
            next_section = build_track_complete_section()
        else:
            nxt_mod_dir, nxt_mod_num, nxt_filename, nxt_title, nxt_cards = ALL_LESSONS[i + 1]
            next_section = build_next_section({
                "mod_num": nxt_mod_num,
                "lesson_num": get_lesson_num(nxt_filename),
                "title": nxt_title,
                "cards": nxt_cards,
            })

        # ── Build the bottom nav ─────────────────────────────────
        prev_info = None
        if i > 0:
            prv_mod_dir, _, prv_filename, prv_title, _ = ALL_LESSONS[i - 1]
            prev_info = {
                "href": rel_path(mod_dir, prv_mod_dir, prv_filename),
                "title": prv_title,
            }

        next_nav_info = None
        if not is_last:
            nxt_mod_dir, _, nxt_filename, nxt_title, _ = ALL_LESSONS[i + 1]
            next_nav_info = {
                "href": rel_path(mod_dir, nxt_mod_dir, nxt_filename),
                "title": nxt_title,
            }

        bottom_nav = build_bottom_nav(prev_info, next_nav_info)

        replacement = next_section + "\n" + bottom_nav + "\n"

        # ── Apply regex replacement ──────────────────────────────
        # Try pattern 1: file has <section id="next-lesson">
        m = RE_WITH_NL.search(html)
        if m:
            new_html = html[:m.start()] + replacement + html[m.end():]
            fpath.write_text(new_html, encoding="utf-8")
            ok += 1
            print(f"  OK    {mod_dir}/{filename}")
            continue

        # Try pattern 2: file has no #next-lesson, only a bottom-nav div
        m = RE_NAV_ONLY.search(html)
        if m:
            new_html = html[:m.start()] + replacement + html[m.end():]
            fpath.write_text(new_html, encoding="utf-8")
            ok += 1
            print(f"  OK    {mod_dir}/{filename} (nav-only)")
            continue

        # Fallback: insert before </main>
        main_close = html.rfind("</main>")
        if main_close >= 0:
            new_html = html[:main_close] + replacement + "\n" + html[main_close:]
            fpath.write_text(new_html, encoding="utf-8")
            ok += 1
            print(f"  OK    {mod_dir}/{filename} (inserted)")
        else:
            print(f"  WARN  {mod_dir}/{filename} (no match, no </main>)")

    print(f"\n{ok}/{total} next-lesson sections rewritten")


if __name__ == "__main__":
    main()
