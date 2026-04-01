"""
Apply standardised hero banners to all track_03 lesson files.
Replaces the entire <section class="hero-container">...</section> block.
"""
import os, re, html as html_mod

BASE = "pages/track_03_data_engineering"
PUB_DATE = "March 31, 2026"

# Module icon mapping per prompt: 1=rocket, 2=cubes, 3=diagram-project, 4+=star
MOD_ICONS = {
    1: "fa6-solid:rocket",
    2: "fa6-solid:cubes",
    3: "fa6-solid:diagram-project",
    4: "fa6-solid:star",
    5: "fa6-solid:star",
    6: "fa6-solid:star",
}

DIFF_DOTS = {
    "Beginner":     ("#22c55e", "#d1d5db", "#d1d5db"),
    "Intermediate": ("#22c55e", "#22c55e", "#d1d5db"),
    "Advanced":     ("#22c55e", "#22c55e", "#22c55e"),
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LESSON DATA — one entry per file
# Keys: title, subtitle, difficulty, read_time, ce, pe
# (goals always 4; lesson_pos and total auto-computed)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LESSONS = {
# ── MODULE 01: Data Engineering Foundations (6 lessons) ──────────
"mod_01_data_engineering_foundations/lesson01_what_is_data_engineering.html": {
    "title": "What Is Data Engineering?",
    "subtitle": "Discover what data engineers do every day and why pipelines, storage, and automation form the backbone of every data-driven organisation.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 8, "pe": 6,
},
"mod_01_data_engineering_foundations/lesson02_etl_vs_elt.html": {
    "title": "ETL vs ELT",
    "subtitle": "Learn the two main strategies for moving data from source to destination and understand when to clean before or after loading.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 8, "pe": 6,
},
"mod_01_data_engineering_foundations/lesson03_handling_large_datasets.html": {
    "title": "Handling Large Datasets",
    "subtitle": "See how to process files that exceed your laptop's memory by reading data in manageable chunks and choosing the right file format.",
    "difficulty": "Beginner", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_01_data_engineering_foundations/lesson05_parquet_efficient_storage.html": {
    "title": "Parquet &amp; Efficient Storage",
    "subtitle": "Understand why columnar Parquet files load faster and use less disk space than CSV, and learn to read and write them with Python.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 8, "pe": 6,
},
"mod_01_data_engineering_foundations/lesson06_intro_to_polars_optional.html": {
    "title": "Intro to Polars (Optional)",
    "subtitle": "Explore the Polars DataFrame library that runs the same operations as pandas but finishes faster by using all your CPU cores automatically.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_01_data_engineering_foundations/lesson07_pipeline_design_concepts.html": {
    "title": "Pipeline Design Concepts",
    "subtitle": "Learn the core design principles that make data pipelines reliable, rerunnable, and easy to debug when something goes wrong at 3 AM.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 8, "pe": 6,
},

# ── MODULE 02: NoSQL and Modern Data Storage (7 lessons) ────────
"mod_02_nosql_and_modern_data_storage/lesson01_what_is_nosql.html": {
    "title": "What Is NoSQL?",
    "subtitle": "Discover why some applications store data without fixed tables and rows, and learn when a NoSQL database is a better fit than traditional SQL.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 8, "pe": 8,
},
"mod_02_nosql_and_modern_data_storage/lesson02_types_of_nosql_databases.html": {
    "title": "Types of NoSQL Databases",
    "subtitle": "Learn the four main NoSQL categories \u2014 document, key-value, column-family, and graph \u2014 and see which data shapes each one handles best.",
    "difficulty": "Beginner", "read_time": "10 min read", "ce": 8, "pe": 8,
},
"mod_02_nosql_and_modern_data_storage/lesson03_document_databases_mongodb.html": {
    "title": "Document Databases (MongoDB)",
    "subtitle": "Learn to store, query, and update JSON-like documents in MongoDB using Python, and see why embedded documents eliminate the need for joins.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 8, "pe": 8,
},
"mod_02_nosql_and_modern_data_storage/lesson04_key_value_databases_redis.html": {
    "title": "Key-Value Databases (Redis)",
    "subtitle": "Discover how Redis delivers sub-millisecond reads from memory and learn to use it as a cache layer that protects your main database from heavy traffic.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 8,
},
"mod_02_nosql_and_modern_data_storage/lesson05_column_family_databases_cassandra.html": {
    "title": "Column-Family Databases (Cassandra)",
    "subtitle": "Understand how Cassandra distributes writes across a cluster with no single point of failure, and learn to model tables around your query patterns.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 8, "pe": 8,
},
"mod_02_nosql_and_modern_data_storage/lesson06_graph_databases_neo4j.html": {
    "title": "Graph Databases (Neo4j)",
    "subtitle": "Learn to model and query relationships directly with nodes and edges, and see why graph traversals outperform SQL joins on deeply connected data.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 8, "pe": 8,
},
"mod_02_nosql_and_modern_data_storage/lesson07_sql_vs_nosql_choosing_the_right_database.html": {
    "title": "SQL vs NoSQL: Choosing the Right Database",
    "subtitle": "Compare the strengths and trade-offs of SQL and NoSQL databases so you can pick the right tool based on your data shape and query needs.",
    "difficulty": "Beginner", "read_time": "10 min read", "ce": 8, "pe": 8,
},

# ── MODULE 03: API Data Integration (14 lessons) ────────────────
"mod_03_api_data_integration/lesson01_what_is_an_api.html": {
    "title": "What Is an API?",
    "subtitle": "Discover how APIs let your Python script fetch live data from remote servers, and understand endpoints, requests, and JSON responses.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 4, "pe": 6,
},
"mod_03_api_data_integration/lesson02_understanding_http_requests.html": {
    "title": "Understanding HTTP Requests",
    "subtitle": "Learn how GET, POST, and other HTTP methods work, and decode the status codes that tell you whether your request succeeded or failed.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 6, "pe": 6,
},
"mod_03_api_data_integration/lesson03_using_the_python_requests_library.html": {
    "title": "Using the Python requests Library",
    "subtitle": "See how to fetch data from any API in a single line of Python with the requests library, and learn to handle errors gracefully.",
    "difficulty": "Beginner", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_03_api_data_integration/lesson04_working_with_json_data.html": {
    "title": "Working with JSON Data",
    "subtitle": "Learn to navigate nested JSON structures using Python dictionaries and lists, and safely handle missing keys without crashing your script.",
    "difficulty": "Beginner", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_03_api_data_integration/lesson05_parsing_api_responses.html": {
    "title": "Parsing API Responses",
    "subtitle": "Discover how to validate, flatten, and extract the exact fields you need from complex API responses before loading them into a DataFrame.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_03_api_data_integration/lesson06_authentication_with_api_keys.html": {
    "title": "Authentication with API Keys",
    "subtitle": "Learn to send API keys securely in HTTP headers and store secrets in environment variables so they never leak into your Git history.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 6, "pe": 6,
},
"mod_03_api_data_integration/lesson07_oauth_authentication.html": {
    "title": "OAuth Authentication",
    "subtitle": "Understand how OAuth tokens replace passwords with temporary, scoped credentials and learn to request and refresh them in Python.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 4, "pe": 6,
},
"mod_03_api_data_integration/lesson08_handling_pagination_in_apis.html": {
    "title": "Handling Pagination in APIs",
    "subtitle": "Learn to loop through paginated API responses so you can collect thousands of records that the server delivers in small batches.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 6, "pe": 6,
},
"mod_03_api_data_integration/lesson09_handling_api_rate_limits.html": {
    "title": "Handling API Rate Limits",
    "subtitle": "Discover how to respect rate limits with exponential backoff and header inspection so your script retries gracefully instead of getting banned.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 6, "pe": 6,
},
"mod_03_api_data_integration/lesson10_loading_api_data_into_pandas.html": {
    "title": "Loading API Data into Pandas",
    "subtitle": "See how to convert nested JSON API responses into flat pandas DataFrames using json_normalize and proper type casting for clean analysis.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 8, "pe": 6,
},
"mod_03_api_data_integration/lesson11_saving_api_data_to_databases.html": {
    "title": "Saving API Data to Databases",
    "subtitle": "Learn to push DataFrames into SQL tables with to_sql, prevent duplicates with upserts, and wrap writes in transactions for safety.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 8, "pe": 6,
},
"mod_03_api_data_integration/lesson12_building_an_api_data_pipeline.html": {
    "title": "Building an API Data Pipeline",
    "subtitle": "Combine extraction, transformation, and loading into a single reusable pipeline script with config files, logging, and modular functions.",
    "difficulty": "Intermediate", "read_time": "14 min read", "ce": 6, "pe": 6,
},
"mod_03_api_data_integration/lesson13_real_world_api_integration_project.html": {
    "title": "Real-World API Integration Project",
    "subtitle": "Apply everything you have learned to build a complete pipeline that fetches, cleans, and stores live data from a real public API.",
    "difficulty": "Advanced", "read_time": "16 min read", "ce": 0, "pe": 6,
},
"mod_03_api_data_integration/lesson14_api_best_practices.html": {
    "title": "API Best Practices",
    "subtitle": "Learn the production habits that keep API pipelines reliable \u2014 timeouts, retries, version pinning, and defensive error handling.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 0, "pe": 6,
},

# ── MODULE 04: Data Pipelines and Orchestration (11 lessons) ────
"mod_04_data_pipelines_and_orchestration/lesson01_what_is_a_data_pipeline.html": {
    "title": "What Is a Data Pipeline?",
    "subtitle": "Discover how data pipelines automate the repetitive copy-paste-clean cycle and deliver fresh data to dashboards, databases, and reports on schedule.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson02_etl_vs_elt.html": {
    "title": "ETL vs ELT",
    "subtitle": "Compare the two main pipeline strategies and learn when to transform data before loading versus leveraging your warehouse's compute power.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson03_pipeline_design_patterns.html": {
    "title": "Pipeline Design Patterns",
    "subtitle": "Learn proven design blueprints \u2014 incremental loads, dead-letter queues, and idempotency \u2014 that make your pipelines robust and easy to maintain.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson04_working_with_large_data_files.html": {
    "title": "Working with Large Data Files",
    "subtitle": "See how to process files that exceed your available memory using generators, chunked reads, and binary formats like Parquet and Feather.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson05_data_validation_in_pipelines.html": {
    "title": "Data Validation in Pipelines",
    "subtitle": "Learn to catch bad data before it reaches your database by adding validation rules, quarantine tables, and executable assertions to every pipeline stage.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson09_scheduling_pipelines.html": {
    "title": "Scheduling Pipelines",
    "subtitle": "Understand cron expressions, event-based triggers, and failure alerts so your pipelines run on time and notify you the moment something breaks.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson10_building_a_simple_python_pipeline.html": {
    "title": "Building a Simple Python Pipeline",
    "subtitle": "Write your first end-to-end pipeline in under 30 lines of Python, with separate extract, transform, and load functions connected by return values.",
    "difficulty": "Beginner", "read_time": "10 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson11_pipeline_project_automating_data_ingestion.html": {
    "title": "Pipeline Project: Automating Data Ingestion",
    "subtitle": "Build an ingestion pipeline that reads config files, tracks watermarks for incremental loads, and recovers gracefully from mid-run failures.",
    "difficulty": "Intermediate", "read_time": "14 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson12_pipeline_project_data_quality_checks.html": {
    "title": "Pipeline Project: Data Quality Checks",
    "subtitle": "Add automated quality gates that measure completeness, cross-check row counts against the source, and block bad data on threshold breaches.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson13_pipeline_project_database_loading.html": {
    "title": "Pipeline Project: Database Loading",
    "subtitle": "Learn bulk insert techniques, upsert patterns, and post-load verification checks that make your database loading stage fast and trustworthy.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 0, "pe": 6,
},
"mod_04_data_pipelines_and_orchestration/lesson14_production_pipeline_architecture.html": {
    "title": "Production Pipeline Architecture",
    "subtitle": "Design pipelines for the real world with modular deployments, monitoring dashboards, alerting, and a plan for tenfold data growth.",
    "difficulty": "Advanced", "read_time": "14 min read", "ce": 0, "pe": 6,
},

# ── MODULE 05: Large Scale Data Processing (14 lessons) ─────────
"mod_05_large_scale_data_processing/lesson02_memory_optimization.html": {
    "title": "Memory Optimization",
    "subtitle": "Learn to halve DataFrame memory usage by downcasting numbers, converting strings to categoricals, and dropping columns you do not need.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 10, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson03_chunk_processing.html": {
    "title": "Chunk Processing",
    "subtitle": "Discover how to process files that exceed your RAM by reading them in fixed-size chunks and accumulating results without loading everything at once.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson04_processing_millions_of_rows.html": {
    "title": "Processing Millions of Rows",
    "subtitle": "See why vectorised pandas operations finish in milliseconds while Python for-loops take minutes, and learn to measure the difference with timeit.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson05_columnar_storage.html": {
    "title": "Columnar Storage",
    "subtitle": "Understand why storing data by column instead of by row makes analytics queries faster and files dramatically smaller through better compression.",
    "difficulty": "Intermediate", "read_time": "8 min read", "ce": 6, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson06_parquet_files.html": {
    "title": "Parquet Files",
    "subtitle": "Learn how Parquet's row groups, predicate pushdown, and built-in compression let you query terabyte datasets without loading them into memory.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 4,
},
"mod_05_large_scale_data_processing/lesson07_pyarrow_basics.html": {
    "title": "PyArrow Basics",
    "subtitle": "Discover Apache Arrow's columnar memory format and learn to use PyArrow for zero-copy data exchange between pandas, Polars, and Spark.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson08_introduction_to_polars.html": {
    "title": "Introduction to Polars",
    "subtitle": "Explore the Polars library that uses Rust and Apache Arrow to run the same DataFrame operations as pandas but finishes up to ten times faster.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 10, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson09_faster_dataframes_with_polars.html": {
    "title": "Faster DataFrames with Polars",
    "subtitle": "Learn to chain Polars expressions, use lazy evaluation, and benchmark real group-by queries to see measurable speed gains over pandas.",
    "difficulty": "Intermediate", "read_time": "12 min read", "ce": 10, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson10_duckdb_for_analytics.html": {
    "title": "DuckDB for Analytics",
    "subtitle": "See how DuckDB lets you run SQL queries on Parquet files and pandas DataFrames directly inside Python \u2014 no server, no installation, no setup.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 10, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson11_parallel_processing.html": {
    "title": "Parallel Processing",
    "subtitle": "Understand Python's GIL, learn when to use processes versus threads, and apply Pool and ThreadPoolExecutor to speed up CPU and I/O tasks.",
    "difficulty": "Advanced", "read_time": "12 min read", "ce": 8, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson12_dask_basics.html": {
    "title": "Dask Basics",
    "subtitle": "Discover how Dask scales familiar pandas syntax across multiple cores and partitions so you can process datasets that do not fit in memory.",
    "difficulty": "Advanced", "read_time": "12 min read", "ce": 10, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson13_performance_profiling.html": {
    "title": "Performance Profiling",
    "subtitle": "Learn to find bottlenecks with cProfile, track memory leaks with memory_profiler, and compare before-and-after results to prove your optimisations work.",
    "difficulty": "Advanced", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson14_real_large_data_project.html": {
    "title": "Real Large Data Project",
    "subtitle": "Apply every technique from this module to build a complete pipeline that ingests, processes, and summarises a multi-gigabyte dataset end to end.",
    "difficulty": "Advanced", "read_time": "16 min read", "ce": 10, "pe": 6,
},
"mod_05_large_scale_data_processing/lesson15_performance_best_practices.html": {
    "title": "Performance Best Practices",
    "subtitle": "Review the habits that keep large-data pipelines fast over time \u2014 avoiding hidden copies, batching I/O, and scheduling regular profiling checks.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 6,
},

# ── MODULE 06: Automation and CI/CD (4 lessons) ─────────────────
"mod_06_automation_and_ci_cd/lesson01_devops_concepts_for_data_analytics.html": {
    "title": "DevOps Concepts for Data &amp; Analytics",
    "subtitle": "Discover how automation, fast feedback loops, and infrastructure as code eliminate manual deployment mistakes and speed up data team delivery.",
    "difficulty": "Beginner", "read_time": "8 min read", "ce": 8, "pe": 6,
},
"mod_06_automation_and_ci_cd/lesson02_gitlab_ci_cd_overview.html": {
    "title": "GitLab CI/CD Overview",
    "subtitle": "Learn how a single .gitlab-ci.yml file defines your build, test, and deploy stages so the entire team can see the pipeline at a glance.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 6,
},
"mod_06_automation_and_ci_cd/lesson03_scheduling_data_jobs.html": {
    "title": "Scheduling Data Jobs",
    "subtitle": "Understand cron schedules, retry policies, and execution logs so your data jobs run on time and leave a clear trail when something goes wrong.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 8,
},
"mod_06_automation_and_ci_cd/lesson05_deployment_workflow.html": {
    "title": "Deployment Workflow",
    "subtitle": "Learn to move code safely from development to staging to production using approval gates, environment isolation, and one-command rollback plans.",
    "difficulty": "Intermediate", "read_time": "10 min read", "ce": 8, "pe": 8,
},
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Compute lesson positions and totals per module
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

mod_lessons = {}  # mod_folder -> sorted list of rel keys
for key in LESSONS:
    mod = key.split("/")[0]
    mod_lessons.setdefault(mod, []).append(key)
for mod in mod_lessons:
    mod_lessons[mod].sort()

def get_position(key):
    mod = key.split("/")[0]
    ls = mod_lessons[mod]
    return ls.index(key) + 1, len(ls)

def get_mod_num(key):
    m = re.search(r"mod_(\d+)", key)
    return int(m.group(1)) if m else 0

def get_lesson_label(key):
    m = re.search(r"lesson(\d+)", key)
    n = int(m.group(1)) if m else 0
    return f"Lesson {n:02d}"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Hero HTML template
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HERO_TEMPLATE = """<section class="hero-container">
  <div class="hero-dots"></div>
  <div class="hero-glow hero-glow-1"></div>
  <div class="hero-glow hero-glow-2"></div>
  <div class="hero-glow-line"></div>
  <div class="relative z-10 px-8 py-8 md:px-12 md:py-10">
    <div class="hero-split flex flex-col md:flex-row items-center gap-6 md:gap-10">

      <!-- LEFT COLUMN -- Lesson info -->
      <div class="flex-1 min-w-0">

        <!-- Badge row -->
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="{mod_icon}"></span> Module {mod_num}
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="inline-flex items-center gap-1">
              <span style="width:6px;height:6px;border-radius:50%;background:{dot1};display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:{dot2};display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:{dot3};display:inline-block;"></span>
            </span>
            {difficulty}
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> {read_time}
          </span>
        </div>

        <!-- Lesson number label -->
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">{lesson_label}</p>

        <!-- Title -->
        <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">{title}</h1>

        <!-- Subtitle -->
        <p class="text-white/80 text-sm md:text-base leading-relaxed mt-4 mb-5 max-w-prose">{subtitle}</p>

        <!-- Author & Date -->
        <div class="flex items-center gap-4 mb-5 text-sm">
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
              <span class="iconify text-white text-[10px]" data-icon="fa6-solid:user"></span>
            </span>
            <span class="text-white/85 font-medium text-xs">Python Learning Hub</span>
          </div>
          <span class="text-white/30">|</span>
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
              <span class="iconify text-white text-[10px]" data-icon="fa6-regular:calendar"></span>
            </span>
            <span class="text-white/85 font-medium text-xs">{pub_date}</span>
          </div>
        </div>

        <!-- Stat pills -->
        <div class="flex items-center gap-2 flex-wrap">
          <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span>
            <span class="font-extrabold">{goals}</span>
            <span class="font-semibold opacity-55">Goals</span>
          </a>
          <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span>
            <span class="font-extrabold">{examples}</span>
            <span class="font-semibold opacity-55">Examples</span>
          </a>
          <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span>
            <span class="font-extrabold">{exercises}</span>
            <span class="font-semibold opacity-55">Exercises</span>
          </a>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span>
            <span class="font-extrabold">{pos}<span class="font-bold opacity-50">/{total}</span></span>
            <span class="font-semibold opacity-55">Progress</span>
          </span>
        </div>

      </div>

      <!-- RIGHT COLUMN -- Hex graphic (locked) -->
      <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
        <div class="hero-abstract-card" style="padding:0.25rem;opacity:0.75;">
          <svg viewBox="0 0 280 324" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" style="max-height:320px;" aria-hidden="true">
            <defs>
              <linearGradient id="hexFill" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a0a12"/><stop offset="45%" stop-color="#2d0a1e"/><stop offset="100%" stop-color="#0d0610"/></linearGradient>
              <linearGradient id="hexBorder" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#CB187D"/><stop offset="50%" stop-color="#e84aad"/><stop offset="100%" stop-color="#CB187D"/></linearGradient>
              <radialGradient id="hexGlow" cx="50%" cy="38%" r="45%"><stop offset="0%" stop-color="#CB187D" stop-opacity="0.18"/><stop offset="100%" stop-color="#CB187D" stop-opacity="0"/></radialGradient>
              <radialGradient id="pyGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFD43B" stop-opacity="0.12"/><stop offset="100%" stop-color="#FFD43B" stop-opacity="0"/></radialGradient>
              <clipPath id="hexClip"><polygon points="140,14 268,88 268,236 140,310 12,236 12,88"/></clipPath>
            </defs>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexFill)"/>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexGlow)"/>
            <g clip-path="url(#hexClip)" opacity="1">
              <g opacity="0.06"><circle cx="40" cy="100" r="1.2" fill="white"/><circle cx="60" cy="100" r="1.2" fill="white"/><circle cx="80" cy="100" r="1.2" fill="white"/><circle cx="100" cy="100" r="1.2" fill="white"/><circle cx="120" cy="100" r="1.2" fill="white"/><circle cx="160" cy="100" r="1.2" fill="white"/><circle cx="180" cy="100" r="1.2" fill="white"/><circle cx="200" cy="100" r="1.2" fill="white"/><circle cx="220" cy="100" r="1.2" fill="white"/><circle cx="240" cy="100" r="1.2" fill="white"/><circle cx="50" cy="120" r="1.2" fill="white"/><circle cx="70" cy="120" r="1.2" fill="white"/><circle cx="90" cy="120" r="1.2" fill="white"/><circle cx="110" cy="120" r="1.2" fill="white"/><circle cx="170" cy="120" r="1.2" fill="white"/><circle cx="190" cy="120" r="1.2" fill="white"/><circle cx="210" cy="120" r="1.2" fill="white"/><circle cx="230" cy="120" r="1.2" fill="white"/><circle cx="40" cy="200" r="1.2" fill="white"/><circle cx="60" cy="200" r="1.2" fill="white"/><circle cx="80" cy="200" r="1.2" fill="white"/><circle cx="100" cy="200" r="1.2" fill="white"/><circle cx="120" cy="200" r="1.2" fill="white"/><circle cx="160" cy="200" r="1.2" fill="white"/><circle cx="180" cy="200" r="1.2" fill="white"/><circle cx="200" cy="200" r="1.2" fill="white"/><circle cx="220" cy="200" r="1.2" fill="white"/><circle cx="240" cy="200" r="1.2" fill="white"/><circle cx="50" cy="220" r="1.2" fill="white"/><circle cx="70" cy="220" r="1.2" fill="white"/><circle cx="90" cy="220" r="1.2" fill="white"/><circle cx="110" cy="220" r="1.2" fill="white"/><circle cx="170" cy="220" r="1.2" fill="white"/><circle cx="190" cy="220" r="1.2" fill="white"/><circle cx="210" cy="220" r="1.2" fill="white"/><circle cx="230" cy="220" r="1.2" fill="white"/></g>
              <g opacity="0.12" stroke="#CB187D" stroke-width="1" fill="none"><path d="M30,95 L55,95 L55,115 L80,115"/><path d="M35,110 L60,110 L60,130"/><circle cx="80" cy="115" r="2.5" fill="#CB187D" opacity="0.4"/><circle cx="55" cy="95" r="2" fill="#CB187D" opacity="0.35"/><circle cx="60" cy="130" r="2" fill="#CB187D" opacity="0.3"/></g>
              <g opacity="0.12" stroke="#e84aad" stroke-width="1" fill="none"><path d="M250,95 L225,95 L225,115 L200,115"/><path d="M245,110 L220,110 L220,130"/><circle cx="200" cy="115" r="2.5" fill="#e84aad" opacity="0.4"/><circle cx="225" cy="95" r="2" fill="#e84aad" opacity="0.35"/><circle cx="220" cy="130" r="2" fill="#e84aad" opacity="0.3"/></g>
              <g opacity="0.1" stroke="#CB187D" stroke-width="1" fill="none"><path d="M35,210 L60,210 L60,230 L85,230"/><path d="M40,225 L65,225 L65,240"/><circle cx="85" cy="230" r="2.5" fill="#CB187D" opacity="0.35"/><circle cx="65" cy="240" r="2" fill="#CB187D" opacity="0.3"/></g>
              <g opacity="0.1" stroke="#e84aad" stroke-width="1" fill="none"><path d="M245,210 L220,210 L220,230 L195,230"/><path d="M240,225 L215,225 L215,240"/><circle cx="195" cy="230" r="2.5" fill="#e84aad" opacity="0.35"/><circle cx="215" cy="240" r="2" fill="#e84aad" opacity="0.3"/></g>
              <g opacity="0.08" fill="white" font-family="'Fira Code',monospace" font-size="7"><text x="42" y="145">&gt;&gt;&gt; import pandas</text><text x="185" y="92">def main():</text><text x="38" y="92">class Data:</text></g>
              <g opacity="0.07" fill="white" font-family="'Fira Code',monospace" font-size="7"><text x="160" y="255">return result</text><text x="42" y="260">for i in range:</text><text x="175" y="275">print("done")</text></g>
              <g opacity="0.15" stroke="#FFD43B" stroke-width="1.5" fill="none" stroke-linecap="round"><polyline points="52,72 42,72 42,85"/><polyline points="228,72 238,72 238,85"/><polyline points="52,252 42,252 42,239"/><polyline points="228,252 238,252 238,239"/></g>
              <g opacity="0.04" stroke="white" stroke-width="1" fill="none"><polygon points="70,155 85,146 100,155 100,173 85,182 70,173"/><polygon points="180,155 195,146 210,155 210,173 195,182 180,173"/><polygon points="125,260 140,251 155,260 155,278 140,287 125,278"/><polygon points="125,40 140,31 155,40 155,58 140,67 125,58"/></g>
              <g opacity="0.08" stroke="white" stroke-width="0.8" fill="none" stroke-dasharray="4,4"><path d="M25,160 Q60,140 60,162 Q60,185 95,165"/><path d="M25,180 Q55,195 75,180"/></g>
              <g opacity="0.08" stroke="white" stroke-width="0.8" fill="none" stroke-dasharray="4,4"><path d="M255,160 Q220,140 220,162 Q220,185 185,165"/><path d="M255,180 Q225,195 205,180"/></g>
              <circle cx="140" cy="145" r="55" fill="url(#pyGlow)"/>
            </g>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="none" stroke="url(#hexBorder)" stroke-width="4" stroke-linejoin="round"/>
            <polygon points="140,24 258,93 258,231 140,300 22,231 22,93" fill="none" stroke="#CB187D" stroke-width="0.8" stroke-linejoin="round" stroke-opacity="0.25"/>
            <foreignObject x="95" y="85" width="90" height="90"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;width:100%;height:100%;"><span class="iconify" data-icon="logos:python" style="font-size:70px;filter:drop-shadow(0 0 14px rgba(255,212,59,0.25));"></span></div></foreignObject>
            <text x="140" y="205" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="800" font-size="30" letter-spacing="4" opacity="0.95">PYTHON</text>
            <text x="140" y="230" text-anchor="middle" fill="#f5c6e0" font-family="Inter,sans-serif" font-weight="600" font-size="14" letter-spacing="5" opacity="0.8">LEARNING HUB</text>
            <line x1="85" y1="185" x2="195" y2="185" stroke="#CB187D" stroke-width="1" stroke-opacity="0.35" stroke-linecap="round"/>
            <line x1="100" y1="248" x2="180" y2="248" stroke="#FFD43B" stroke-width="1.2" stroke-opacity="0.25" stroke-linecap="round"/>
            <g opacity="0.5"><rect x="113" y="255" width="54" height="16" rx="8" fill="#CB187D" opacity="0.2"/><rect x="113" y="255" width="54" height="16" rx="8" fill="none" stroke="#CB187D" stroke-width="0.6" opacity="0.35"/><text x="140" y="266.5" text-anchor="middle" fill="#f5c6e0" font-family="'Fira Code',monospace" font-weight="600" font-size="8" opacity="0.8">v1.0</text></g>
          </svg>
        </div>
      </div>

    </div>
  </div>
</section>"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Apply logic
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HERO_PAT = re.compile(r'<section class="hero-container">.*?</section>', re.DOTALL)

def build_hero(key, data):
    mod_num = get_mod_num(key)
    mod_icon = MOD_ICONS.get(mod_num, "fa6-solid:star")
    pos, total = get_position(key)
    dots = DIFF_DOTS[data["difficulty"]]
    return HERO_TEMPLATE.format(
        mod_icon=mod_icon,
        mod_num=mod_num,
        dot1=dots[0], dot2=dots[1], dot3=dots[2],
        difficulty=data["difficulty"],
        read_time=data["read_time"],
        lesson_label=get_lesson_label(key),
        title=data["title"],
        subtitle=data["subtitle"],
        pub_date=PUB_DATE,
        goals=4,
        examples=data["ce"],
        exercises=data["pe"],
        pos=pos,
        total=total,
    )

ok = 0
fail = 0
for key, data in sorted(LESSONS.items()):
    fp = os.path.join(BASE, key.replace("/", os.sep))
    if not os.path.isfile(fp):
        print(f"  [FAIL] NOT FOUND: {key}")
        fail += 1
        continue

    content = open(fp, encoding="utf-8").read()
    new_hero = build_hero(key, data)

    m = HERO_PAT.search(content)
    if not m:
        print(f"  [FAIL] NO HERO: {key}")
        fail += 1
        continue

    new_content = content[:m.start()] + new_hero + content[m.end():]

    # Verify no section loss
    old_sections = re.findall(r'<section id="([^"]+)"', content)
    new_sections = re.findall(r'<section id="([^"]+)"', new_content)
    if old_sections != new_sections:
        print(f"  [FAIL] SECTION MISMATCH: {key}")
        fail += 1
        continue

    open(fp, "w", encoding="utf-8").write(new_content)
    print(f"  [OK] {key}")
    ok += 1

print(f"\nDone: {ok} patched, {fail} failed")
