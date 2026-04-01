#!/usr/bin/env python3
"""Rewrite #recap section for all 56 track_03 lessons."""

import re, pathlib, html as html_mod

ROOT = pathlib.Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering")
PATTERN = re.compile(r'<section id="recap">.*?</section>', re.DOTALL)

MOD01 = "mod_01_data_engineering_foundations"
MOD02 = "mod_02_nosql_and_modern_data_storage"
MOD03 = "mod_03_api_data_integration"
MOD04 = "mod_04_data_pipelines_and_orchestration"
MOD05 = "mod_05_large_scale_data_processing"
MOD06 = "mod_06_automation_and_ci_cd"


def card_html(num, icon, label, sentence):
    """Build one recap card."""
    return (
        f'      <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">\n'
        f'        <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">\n'
        f'          <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num:02d}</span>\n'
        f'          <div class="relative flex items-start gap-3">\n'
        f'            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">\n'
        f'              <span class="iconify text-sm" data-icon="{icon}"></span>\n'
        f'            </span>\n'
        f'            <div>\n'
        f'              <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">{label}</p>\n'
        f'              <p class="text-[11px] text-gray-600 leading-snug">{sentence}</p>\n'
        f'            </div>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'      </div>'
    )


BANNER = (
    '      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">\n'
    '        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>\n'
    '        <div class="relative flex items-center gap-4">\n'
    '          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">\n'
    '            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>\n'
    '          </span>\n'
    '          <div>\n'
    '            <p class="text-sm font-bold text-white">Lesson Complete!</p>\n'
    '            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>'
)


def build_section(cards):
    """Build the full #recap section from 4 (icon, label, sentence) tuples."""
    c1, c2, c3, c4 = cards
    grid = (
        '      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n'
        + card_html(1, *c1) + '\n'
        + card_html(2, *c2) + '\n'
        + card_html(3, *c3) + '\n'
        + card_html(4, *c4) + '\n'
        '      </div>'
    )
    return (
        '<section id="recap">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:list-check"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Recap</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A quick summary of what you learned</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-6">\n'
        + grid + '\n'
        + BANNER + '\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── Lesson data ───────────────────────────────────────────────────────────────
# Each value: tuple of 4 cards, each card is (icon, label, sentence)

LESSONS = {

    # ── MOD 01 — Data Engineering Foundations ─────────────────────────────────

    f"{MOD01}/lesson01_what_is_data_engineering.html": (
        ("fa6-solid:gears", "Define data engineering",
         "You can explain what data engineers build and why organisations need them."),
        ("fa6-solid:arrows-split-up-and-left", "Distinguish related roles",
         "You can separate the daily work of engineers, analysts, and scientists."),
        ("fa6-solid:hammer", "Core responsibilities",
         "You know pipelines, storage, and infrastructure are the key deliverables."),
        ("fa6-solid:link", "Why it matters",
         "Reliable engineering is the foundation every downstream analysis depends on."),
    ),

    f"{MOD01}/lesson02_etl_vs_elt.html": (
        ("fa6-solid:right-left", "Compare ETL and ELT",
         "You can describe how both patterns move data from source to target."),
        ("fa6-solid:industry", "Traditional ETL pattern",
         "Transform-then-load works best when storage was expensive and slow."),
        ("fa6-solid:cloud-arrow-up", "Modern ELT pattern",
         "Load-then-transform leverages cheap cloud warehouses for heavy lifting."),
        ("fa6-solid:scale-balanced", "Choose the right approach",
         "You pick ETL or ELT based on where compute and storage are cheapest."),
    ),

    f"{MOD01}/lesson03_handling_large_datasets.html": (
        ("fa6-solid:triangle-exclamation", "Recognise memory limits",
         "You know a single large file can crash Python if loaded all at once."),
        ("fa6-solid:puzzle-piece", "Chunk-based reading",
         'You can pass <code class="font-mono">chunksize</code> to process a file in small batches.'),
        ("fa6-solid:filter", "Selective column loading",
         'The <code class="font-mono">usecols</code> parameter skips columns you do not need.'),
        ("fa6-solid:microchip", "Downcast data types",
         "Smaller numeric types cut memory usage without losing the values you need."),
    ),

    f"{MOD01}/lesson05_parquet_efficient_storage.html": (
        ("fa6-solid:file-zipper", "What Parquet is",
         "Parquet stores data in columns, compressing far smaller than CSV files."),
        ("fa6-solid:database", "Columnar storage benefits",
         "Analytics queries read only the columns they need, skipping the rest."),
        ("fa6-solid:arrow-right-arrow-left", "Convert CSV to Parquet",
         'One call to <code class="font-mono">to_parquet()</code> replaces an entire CSV export.'),
        ("fa6-solid:magnifying-glass-chart", "Read Parquet efficiently",
         'You can load selected columns with the <code class="font-mono">columns</code> parameter.'),
    ),

    f"{MOD01}/lesson06_intro_to_polars_optional.html": (
        ("fa6-solid:bolt", "What Polars is",
         "Polars is a high-speed DataFrame library written in Rust."),
        ("fa6-solid:gauge-high", "Why Polars is faster",
         "Multi-threaded execution and lazy evaluation eliminate unnecessary work."),
        ("fa6-solid:laptop-code", "Basic Polars operations",
         'You can filter, group, and sort data with <code class="font-mono">pl.col()</code> expressions.'),
        ("fa6-solid:code-compare", "Compare with pandas",
         "Polars syntax differs slightly, but the filter-group-sort pattern is identical."),
    ),

    f"{MOD01}/lesson07_pipeline_design_concepts.html": (
        ("fa6-solid:diagram-project", "Pipeline stages",
         "Extract, transform, and load are the three stages every pipeline follows."),
        ("fa6-solid:cubes", "Modular design",
         "Each stage lives in its own function so you can test it independently."),
        ("fa6-solid:arrows-rotate", "Idempotent processing",
         "A well-designed step produces the same result no matter how often it runs."),
        ("fa6-solid:shield-halved", "Error handling patterns",
         'Wrapping stages in <code class="font-mono">try/except</code> keeps one failure from stopping the whole pipeline.'),
    ),

    # ── MOD 02 — NoSQL and Modern Data Storage ───────────────────────────────

    f"{MOD02}/lesson01_what_is_nosql.html": (
        ("fa6-solid:database", "Define NoSQL",
         "NoSQL databases store data without requiring fixed rows and columns."),
        ("fa6-solid:lightbulb", "Why NoSQL was created",
         "Web-scale apps needed flexible schemas that relational tables could not deliver."),
        ("fa6-solid:right-left", "SQL vs NoSQL basics",
         "SQL enforces structure up front; NoSQL lets each record vary freely."),
        ("fa6-solid:crosshairs", "NoSQL use cases",
         "Real-time caching, document storage, and graph queries are natural fits."),
    ),

    f"{MOD02}/lesson02_types_of_nosql_databases.html": (
        ("fa6-solid:layer-group", "Four NoSQL families",
         "Document, key-value, column-family, and graph cover four distinct patterns."),
        ("fa6-solid:box-open", "How each stores data",
         "Documents use JSON, key-value uses simple pairs, columns use wide rows."),
        ("fa6-solid:wrench", "Problems each solves",
         "Each family optimises for a specific access pattern like lookups or traversals."),
        ("fa6-solid:map-signs", "Choosing a type",
         "Match the database type to the shape your queries will follow."),
    ),

    f"{MOD02}/lesson03_document_databases_mongodb.html": (
        ("fa6-solid:file-lines", "Document model",
         "MongoDB stores each record as a flexible JSON-like document."),
        ("fa6-solid:pen-to-square", "Insert and update documents",
         'You can add and modify records with <code class="font-mono">insert_one()</code> and <code class="font-mono">update_one()</code>.'),
        ("fa6-solid:magnifying-glass", "Query documents",
         "Filter dictionaries let you search collections the same way as SQL WHERE clauses."),
        ("fa6-solid:table-columns", "Documents vs SQL rows",
         "Documents nest related data inside one record instead of splitting across tables."),
    ),

    f"{MOD02}/lesson04_key_value_databases_redis.html": (
        ("fa6-solid:key", "Key-value model",
         "Redis stores each value under a unique key for instant retrieval."),
        ("fa6-solid:bolt", "In-memory speed",
         "Keeping data in RAM makes reads and writes thousands of times faster."),
        ("fa6-solid:box-archive", "Core Redis operations",
         'You can store and fetch values with <code class="font-mono">set()</code> and <code class="font-mono">get()</code> in one call.'),
        ("fa6-solid:clock-rotate-left", "Caching use cases",
         "Session tokens, API responses, and config values are ideal caching targets."),
    ),

    f"{MOD02}/lesson05_column_family_databases_cassandra.html": (
        ("fa6-solid:table-cells", "Column-family model",
         "Cassandra organises data into wide rows where each row can hold different columns."),
        ("fa6-solid:server", "Distributed architecture",
         "Data replicates across multiple nodes so the cluster stays available if one fails."),
        ("fa6-solid:pen-to-square", "Write and query data",
         "CQL syntax looks like SQL, so your existing query skills transfer directly."),
        ("fa6-solid:chart-line", "High-throughput scenarios",
         "Time-series data and IoT sensor streams are ideal Cassandra workloads."),
    ),

    f"{MOD02}/lesson06_graph_databases_neo4j.html": (
        ("fa6-solid:circle-nodes", "Graph model",
         "Nodes represent entities and edges represent the relationships between them."),
        ("fa6-solid:magnifying-glass", "Cypher queries",
         'Cypher uses arrow syntax like <code class="font-mono">(a)-[:KNOWS]-&gt;(b)</code> to match patterns.'),
        ("fa6-solid:share-nodes", "Relationship traversal",
         "Graph databases follow multi-hop paths far faster than SQL JOINs can."),
        ("fa6-solid:users", "Graph use cases",
         "Social networks, fraud detection, and recommendation engines rely on graphs."),
    ),

    f"{MOD02}/lesson07_sql_vs_nosql_choosing_the_right_database.html": (
        ("fa6-solid:scale-balanced", "Compare trade-offs",
         "SQL offers strong consistency; NoSQL offers flexibility and horizontal scale."),
        ("fa6-solid:list-check", "Decision criteria",
         "Data shape, query patterns, and scale requirements drive the choice."),
        ("fa6-solid:diagram-project", "Polyglot persistence",
         "Many systems use SQL and NoSQL together, each for the job it does best."),
        ("fa6-solid:route", "Make the call",
         "Start with the data access pattern and let it point you to the right engine."),
    ),

    # ── MOD 03 — API Data Integration ─────────────────────────────────────────

    f"{MOD03}/lesson01_what_is_an_api.html": (
        ("fa6-solid:plug", "Define an API",
         "An API is a contract that lets two systems exchange data through requests."),
        ("fa6-solid:network-wired", "Why APIs exist",
         "APIs let applications share data without exposing their internal databases."),
        ("fa6-solid:arrows-left-right", "Request-response cycle",
         "You send a request to a URL and the server returns structured data."),
        ("fa6-solid:laptop-code", "Python and APIs",
         'The <code class="font-mono">requests</code> library handles HTTP calls in a few lines of Python.'),
    ),

    f"{MOD03}/lesson02_understanding_http_requests.html": (
        ("fa6-solid:globe", "HTTP basics",
         "HTTP is the protocol every web request and API call travels over."),
        ("fa6-solid:list-ol", "Request methods",
         "GET reads data, POST creates it, PUT updates it, DELETE removes it."),
        ("fa6-solid:circle-check", "Status codes",
         "A 200 means success, a 404 means not found, a 500 means server error."),
        ("fa6-solid:sliders", "Headers and parameters",
         "Headers carry metadata while query parameters filter the data you receive."),
    ),

    f"{MOD03}/lesson03_using_the_python_requests_library.html": (
        ("fa6-solid:download", "Install and import requests",
         'A quick <code class="font-mono">pip install requests</code> gives you a full HTTP client.'),
        ("fa6-solid:paper-plane", "Send GET and POST requests",
         'You call <code class="font-mono">requests.get()</code> or <code class="font-mono">requests.post()</code> with a URL and optional data.'),
        ("fa6-solid:file-code", "Inspect responses",
         'Check <code class="font-mono">status_code</code> and <code class="font-mono">headers</code> to confirm the request succeeded.'),
        ("fa6-solid:code", "Parse JSON responses",
         'Calling <code class="font-mono">.json()</code> converts the response body into a Python dictionary.'),
    ),

    f"{MOD03}/lesson04_working_with_json_data.html": (
        ("fa6-solid:brackets-curly", "JSON structure",
         "JSON uses key-value pairs and arrays to represent structured data as text."),
        ("fa6-solid:file-import", "Parse JSON in Python",
         '<code class="font-mono">json.loads()</code> turns a JSON string into a Python dictionary.'),
        ("fa6-solid:sitemap", "Navigate nested data",
         "Chained key lookups let you drill into deeply nested JSON objects."),
        ("fa6-solid:file-export", "Write JSON files",
         '<code class="font-mono">json.dump()</code> saves a dictionary to a file with proper formatting.'),
    ),

    f"{MOD03}/lesson05_parsing_api_responses.html": (
        ("fa6-solid:triangle-exclamation", "Check status codes",
         "Always verify the status code before trying to read the response body."),
        ("fa6-solid:shield-halved", "Handle errors gracefully",
         '<code class="font-mono">try/except</code> blocks keep your script running when a request fails.'),
        ("fa6-solid:layer-group", "Extract nested data",
         "You can navigate nested JSON to pull exactly the fields your pipeline needs."),
        ("fa6-solid:table", "Build clean datasets",
         "Parsed API fields map directly into pandas DataFrames for analysis."),
    ),

    f"{MOD03}/lesson06_authentication_with_api_keys.html": (
        ("fa6-solid:lock", "Why APIs need auth",
         "Authentication prevents unauthorised access and tracks who makes each request."),
        ("fa6-solid:key", "What an API key is",
         "An API key is a unique token the server uses to identify your application."),
        ("fa6-solid:paper-plane", "Send keys in requests",
         "You pass the key in a header or query parameter with every API call."),
        ("fa6-solid:vault", "Store keys securely",
         "Environment variables keep secrets out of your source code and version control."),
    ),

    f"{MOD03}/lesson07_oauth_authentication.html": (
        ("fa6-solid:user-shield", "What OAuth is",
         "OAuth lets users grant limited access without sharing their password."),
        ("fa6-solid:arrows-rotate", "The OAuth flow",
         "Redirect, authorise, and token exchange are the three main handshake steps."),
        ("fa6-solid:ticket", "Access and refresh tokens",
         "Access tokens expire quickly; refresh tokens let you get new ones silently."),
        ("fa6-solid:laptop-code", "OAuth in Python",
         'Libraries handle the token exchange so you just pass credentials and call <code class="font-mono">.get()</code>.'),
    ),

    f"{MOD03}/lesson08_handling_pagination_in_apis.html": (
        ("fa6-solid:book-open", "What pagination is",
         "APIs split large result sets into pages to avoid overwhelming the client."),
        ("fa6-solid:forward", "Page through results",
         "Increment the page parameter in a loop until the server returns no data."),
        ("fa6-solid:link", "Follow next-page links",
         "Some APIs return a URL for the next page inside the response body."),
        ("fa6-solid:list-check", "Collect complete datasets",
         "Extend a list inside the loop to gather every page into one collection."),
    ),

    f"{MOD03}/lesson09_handling_api_rate_limits.html": (
        ("fa6-solid:gauge-high", "What rate limits are",
         "Servers cap how many requests you can send within a time window."),
        ("fa6-solid:magnifying-glass", "Detect rate-limit errors",
         "An HTTP 429 status code tells you the server has throttled your requests."),
        ("fa6-solid:clock", "Add delays and retries",
         '<code class="font-mono">time.sleep()</code> pauses your script before retrying a blocked request.'),
        ("fa6-solid:shield-halved", "Build resilient scripts",
         "Exponential backoff doubles the wait after each retry to reduce server pressure."),
    ),

    f"{MOD03}/lesson10_loading_api_data_into_pandas.html": (
        ("fa6-solid:table", "JSON to DataFrame",
         '<code class="font-mono">pd.DataFrame()</code> converts a list of JSON records into rows and columns.'),
        ("fa6-solid:filter", "Clean and filter",
         "Boolean masks and column selection trim the DataFrame to only useful data."),
        ("fa6-solid:chart-bar", "Analyse API data",
         "Group-by aggregations and value counts reveal patterns in the fetched data."),
        ("fa6-solid:file-csv", "Export for reuse",
         '<code class="font-mono">to_csv()</code> and <code class="font-mono">to_parquet()</code> save the cleaned data for later analysis.'),
    ),

    f"{MOD03}/lesson11_saving_api_data_to_databases.html": (
        ("fa6-solid:database", "Store data in SQLite",
         "SQLite gives you a local database file that needs no separate server."),
        ("fa6-solid:code", "Use pandas to_sql",
         '<code class="font-mono">df.to_sql()</code> writes a DataFrame straight into a database table.'),
        ("fa6-solid:arrows-rotate", "Upsert logic",
         "Combine insert and update to avoid duplicates when re-running the pipeline."),
        ("fa6-solid:magnifying-glass", "Query stored data",
         '<code class="font-mono">pd.read_sql()</code> pulls stored records back into a DataFrame for analysis.'),
    ),

    f"{MOD03}/lesson12_building_an_api_data_pipeline.html": (
        ("fa6-solid:diagram-project", "Pipeline structure",
         "A clear extract-transform-load sequence keeps your API pipeline organised."),
        ("fa6-solid:download", "Extract stage",
         "The extract function fetches raw JSON from the API and handles pagination."),
        ("fa6-solid:wand-magic-sparkles", "Transform stage",
         "Cleaning, renaming, and filtering happen in a dedicated transform function."),
        ("fa6-solid:database", "Load stage",
         "The load function writes the final DataFrame into the target database table."),
    ),

    f"{MOD03}/lesson13_real_world_api_integration_project.html": (
        ("fa6-solid:flask", "Build a complete pipeline",
         "You connected every stage into one script that runs end to end."),
        ("fa6-solid:shield-halved", "Handle real-world errors",
         "Timeouts, missing fields, and bad responses are caught before they crash the job."),
        ("fa6-solid:table", "Transform into DataFrames",
         "Raw API JSON becomes clean, typed columns ready for analysis."),
        ("fa6-solid:database", "Persist for analysis",
         "Final records land in a database table you can query any time."),
    ),

    f"{MOD03}/lesson14_api_best_practices.html": (
        ("fa6-solid:shield-halved", "Defensive error handling",
         '<code class="font-mono">try/except</code> with retries keeps your pipeline alive when requests fail.'),
        ("fa6-solid:file-lines", "Logging and monitoring",
         "Timestamped log messages tell you exactly which step succeeded or failed."),
        ("fa6-solid:vault", "Credential management",
         "Environment variables and secret stores keep API keys out of your code."),
        ("fa6-solid:book", "Document your integrations",
         "A short README listing endpoints, auth, and schedules saves future debugging time."),
    ),

    # ── MOD 04 — Data Pipelines and Orchestration ─────────────────────────────

    f"{MOD04}/lesson01_what_is_a_data_pipeline.html": (
        ("fa6-solid:diagram-project", "Define a data pipeline",
         "A pipeline is an automated chain of steps that moves data from source to target."),
        ("fa6-solid:building", "Why organisations build them",
         "Pipelines ensure fresh, trusted data is ready before anyone opens a dashboard."),
        ("fa6-solid:layer-group", "Pipeline stages",
         "Extract, transform, and load are the three stages every pipeline follows."),
        ("fa6-solid:laptop-code", "Python in pipelines",
         "Python scripts connect sources, clean data, and write results in one workflow."),
    ),

    f"{MOD04}/lesson02_etl_vs_elt.html": (
        ("fa6-solid:right-left", "ETL vs ELT",
         "ETL transforms before loading; ELT loads raw data then transforms in place."),
        ("fa6-solid:industry", "When to use ETL",
         "Choose ETL when your target system has limited compute for transformations."),
        ("fa6-solid:cloud-arrow-up", "When to use ELT",
         "Choose ELT when a powerful cloud warehouse can handle heavy transformations."),
        ("fa6-solid:scale-balanced", "Compare architectures",
         "Cost, latency, and team skills determine which pattern fits your project."),
    ),

    f"{MOD04}/lesson03_pipeline_design_patterns.html": (
        ("fa6-solid:cubes", "Common patterns",
         "Linear, branching, and merge topologies cover most real-world pipeline shapes."),
        ("fa6-solid:clock", "Batch vs streaming",
         "Batch runs on a schedule; streaming processes records as they arrive."),
        ("fa6-solid:arrows-split-up-and-left", "Fan-out and merge",
         "Splitting data across parallel branches and merging results speeds up throughput."),
        ("fa6-solid:arrows-rotate", "Idempotent steps",
         "A step that produces identical output on every re-run is safe to retry."),
    ),

    f"{MOD04}/lesson04_working_with_large_data_files.html": (
        ("fa6-solid:triangle-exclamation", "Memory constraints",
         "Loading a file larger than available RAM will crash your Python process."),
        ("fa6-solid:puzzle-piece", "Chunk-based processing",
         'The <code class="font-mono">chunksize</code> parameter processes a large file one batch at a time.'),
        ("fa6-solid:filter", "Selective loading",
         "Reading only the columns you need cuts memory usage dramatically."),
        ("fa6-solid:file-arrow-down", "Streaming writes",
         "Writing results chunk by chunk keeps memory flat for very large outputs."),
    ),

    f"{MOD04}/lesson05_data_validation_in_pipelines.html": (
        ("fa6-solid:clipboard-check", "Why validate data",
         "Catching bad records early prevents silent errors in downstream reports."),
        ("fa6-solid:spell-check", "Common validation rules",
         "Null checks, type checks, and range checks cover most quality issues."),
        ("fa6-solid:ban", "Reject bad records",
         "Route invalid rows to a quarantine table instead of dropping them silently."),
        ("fa6-solid:file-lines", "Log validation results",
         "A validation log tells you how many records passed, failed, and why."),
    ),

    f"{MOD04}/lesson09_scheduling_pipelines.html": (
        ("fa6-solid:calendar-check", "Why schedule pipelines",
         "Scheduled runs ensure fresh data is ready before the business day starts."),
        ("fa6-solid:terminal", "Cron and Task Scheduler",
         "Cron on Linux and Task Scheduler on Windows both trigger scripts on a timetable."),
        ("fa6-solid:clock-rotate-left", "Run intervals",
         "Match the schedule to how often your source data actually changes."),
        ("fa6-solid:bell", "Monitor scheduled runs",
         "Alerts on failure let you fix a broken pipeline before users notice stale data."),
    ),

    f"{MOD04}/lesson10_building_a_simple_python_pipeline.html": (
        ("fa6-solid:hammer", "Build end to end",
         "You connected extract, transform, and load into one runnable Python script."),
        ("fa6-solid:download", "Extract from files",
         "The extract function reads source CSV or Parquet files into a DataFrame."),
        ("fa6-solid:wand-magic-sparkles", "Transform data",
         "Cleaning, renaming, and filtering happen in a dedicated transform step."),
        ("fa6-solid:database", "Load into SQLite",
         '<code class="font-mono">to_sql()</code> writes the final DataFrame into a local SQLite database.'),
    ),

    f"{MOD04}/lesson11_pipeline_project_automating_data_ingestion.html": (
        ("fa6-solid:folder-open", "Watch for new files",
         "Your pipeline detects when a new file lands in the input folder."),
        ("fa6-solid:clipboard-check", "Validate on arrival",
         "Each incoming file passes schema and null checks before processing begins."),
        ("fa6-solid:database", "Load into the database",
         "Validated records are appended to the target table automatically."),
        ("fa6-solid:file-lines", "Log every step",
         "Timestamped log entries track each file from arrival to successful load."),
    ),

    f"{MOD04}/lesson12_pipeline_project_data_quality_checks.html": (
        ("fa6-solid:magnifying-glass", "Detect bad records",
         "Boolean masks flag rows that fail null, type, or range checks."),
        ("fa6-solid:code-branch", "Split good and bad data",
         "Good rows proceed to loading; bad rows route to a quarantine table."),
        ("fa6-solid:chart-pie", "Quality metrics",
         "Pass and fail counts give you a quick health score for every run."),
        ("fa6-solid:bell", "Alert on failures",
         "An alert fires when the failure rate crosses your defined threshold."),
    ),

    f"{MOD04}/lesson13_pipeline_project_database_loading.html": (
        ("fa6-solid:database", "Load validated data",
         "Only records that pass quality checks reach the final target table."),
        ("fa6-solid:arrows-rotate", "Upsert strategy",
         "Merge logic inserts new rows and updates existing ones in a single pass."),
        ("fa6-solid:layer-group", "Raw vs processed tables",
         "Keeping raw and clean tables separate lets you reprocess without re-ingesting."),
        ("fa6-solid:file-lines", "Audit trail",
         "Every load writes a row to the audit table with timestamp and row counts."),
    ),

    f"{MOD04}/lesson14_production_pipeline_architecture.html": (
        ("fa6-solid:server", "Production components",
         "Scheduler, runner, storage, and monitoring form the four production pillars."),
        ("fa6-solid:gears", "Configuration management",
         "Config files separate connection strings and paths from your pipeline code."),
        ("fa6-solid:eye", "Monitoring and alerts",
         "Dashboards and email alerts tell you the moment a pipeline run fails."),
        ("fa6-solid:shield-halved", "Graceful error recovery",
         "Transactions and retries protect your data when a step fails mid-run."),
    ),

    # ── MOD 05 — Large Scale Data Processing ──────────────────────────────────

    f"{MOD05}/lesson02_memory_optimization.html": (
        ("fa6-solid:memory", "Measure memory usage",
         '<code class="font-mono">df.memory_usage(deep=True)</code> shows exactly how many bytes each column takes.'),
        ("fa6-solid:arrow-down-short-wide", "Downcast numeric types",
         'Switching from <code class="font-mono">int64</code> to <code class="font-mono">int32</code> halves a column\u2019s memory footprint.'),
        ("fa6-solid:tags", "Use category dtype",
         "Repeated strings shrink dramatically when you convert them to category codes."),
        ("fa6-solid:trash-can", "Drop unneeded columns",
         "Removing columns you will never query frees memory before processing starts."),
    ),

    f"{MOD05}/lesson03_chunk_processing.html": (
        ("fa6-solid:puzzle-piece", "What chunk processing is",
         "Reading a file in fixed-size batches keeps memory usage flat and predictable."),
        ("fa6-solid:file-import", "Read CSV in chunks",
         'Pass <code class="font-mono">chunksize</code> to <code class="font-mono">read_csv()</code> and iterate over each batch.'),
        ("fa6-solid:calculator", "Aggregate across chunks",
         "Accumulate partial totals in a loop, then combine them into a final result."),
        ("fa6-solid:scale-balanced", "Choose the right chunk size",
         "Larger chunks run faster but use more memory \u2014 test to find the sweet spot."),
    ),

    f"{MOD05}/lesson04_processing_millions_of_rows.html": (
        ("fa6-solid:bolt", "Vectorised operations",
         "Operating on a whole column at once is hundreds of times faster than looping."),
        ("fa6-solid:ban", "Avoid slow loops",
         'Replace Python <code class="font-mono">for</code> loops with pandas or NumPy array operations.'),
        ("fa6-solid:gauge-high", "Time your code",
         '<code class="font-mono">%timeit</code> shows you exactly how long each approach takes to run.'),
        ("fa6-solid:layer-group", "Batch processing strategies",
         "Combine chunking with vectorised operations to handle datasets of any size."),
    ),

    f"{MOD05}/lesson05_columnar_storage.html": (
        ("fa6-solid:table-columns", "Row vs column storage",
         "Row stores read entire records; column stores read only the fields you need."),
        ("fa6-solid:bolt", "Faster analytics queries",
         "Columnar formats skip irrelevant columns, so aggregate queries run faster."),
        ("fa6-solid:file-zipper", "Better compression",
         "Similar values in a single column compress far better than mixed row data."),
        ("fa6-solid:database", "Where columnar is used",
         "Parquet, ORC, and warehouse engines all rely on columnar storage internally."),
    ),

    f"{MOD05}/lesson06_parquet_files.html": (
        ("fa6-solid:file-zipper", "Read and write Parquet",
         '<code class="font-mono">to_parquet()</code> and <code class="font-mono">read_parquet()</code> handle round-trip storage in one line each.'),
        ("fa6-solid:filter", "Select columns on read",
         'The <code class="font-mono">columns</code> parameter loads only the fields your analysis needs.'),
        ("fa6-solid:magnifying-glass-chart", "Inspect metadata",
         "Reading the file footer reveals row counts and column stats without loading data."),
        ("fa6-solid:right-left", "Compare with CSV",
         "Parquet files are smaller, faster to read, and preserve column data types."),
    ),

    f"{MOD05}/lesson07_pyarrow_basics.html": (
        ("fa6-solid:feather", "What PyArrow is",
         "PyArrow is a library for fast, type-safe columnar data operations."),
        ("fa6-solid:table", "Create Arrow tables",
         "Define a schema and pass your data to build a strictly typed Arrow table."),
        ("fa6-solid:right-left", "Convert to pandas",
         '<code class="font-mono">table.to_pandas()</code> converts Arrow data into a pandas DataFrame instantly.'),
        ("fa6-solid:file-lines", "Read Parquet metadata",
         "PyArrow reads file metadata to show row counts and stats without loading data."),
    ),

    f"{MOD05}/lesson08_introduction_to_polars.html": (
        ("fa6-solid:bolt", "What Polars is",
         "Polars is a Rust-powered DataFrame library built for speed and low memory."),
        ("fa6-solid:laptop-code", "Basic Polars operations",
         'Filter, select, and group data using <code class="font-mono">pl.col()</code> expressions.'),
        ("fa6-solid:gauge-high", "Speed and memory",
         "Multi-threaded execution processes millions of rows using a fraction of the RAM."),
        ("fa6-solid:code-compare", "Polars vs pandas",
         "Polars outperforms pandas on large data while keeping a similar API feel."),
    ),

    f"{MOD05}/lesson09_faster_dataframes_with_polars.html": (
        ("fa6-solid:wand-magic-sparkles", "Lazy evaluation",
         'Calling <code class="font-mono">.lazy()</code> builds a query plan that Polars optimises before executing.'),
        ("fa6-solid:link", "Expression chaining",
         "Chain multiple transformations in one statement for cleaner, faster pipelines."),
        ("fa6-solid:microchip", "Multi-threaded execution",
         "Polars splits work across all CPU cores automatically without extra code."),
        ("fa6-solid:chart-line", "Benchmark against pandas",
         "Timing both libraries on the same task shows Polars\u2019 real-world speed advantage."),
    ),

    f"{MOD05}/lesson10_duckdb_for_analytics.html": (
        ("fa6-solid:database", "What DuckDB is",
         "DuckDB is an embedded analytics database that runs SQL with no server setup."),
        ("fa6-solid:file-code", "SQL on files",
         "You can query CSV and Parquet files directly using standard SQL syntax."),
        ("fa6-solid:right-left", "Integrate with pandas",
         "DuckDB reads and writes pandas DataFrames as if they were database tables."),
        ("fa6-solid:bolt", "Performance advantages",
         "Columnar execution and automatic parallelism make large queries fast."),
    ),

    f"{MOD05}/lesson11_parallel_processing.html": (
        ("fa6-solid:microchip", "What parallel processing is",
         "Parallel processing divides work across multiple CPU cores to finish faster."),
        ("fa6-solid:gears", "concurrent.futures",
         '<code class="font-mono">ThreadPoolExecutor</code> and <code class="font-mono">ProcessPoolExecutor</code> run tasks on multiple workers.'),
        ("fa6-solid:code-branch", "multiprocessing module",
         '<code class="font-mono">multiprocessing.Pool</code> distributes CPU-heavy work across separate processes.'),
        ("fa6-solid:triangle-exclamation", "Pitfalls and overhead",
         "Spawning processes has a cost \u2014 small tasks run faster without parallelism."),
    ),

    f"{MOD05}/lesson12_dask_basics.html": (
        ("fa6-solid:cubes", "What Dask is",
         "Dask is a parallel computing library that scales pandas-like code to large data."),
        ("fa6-solid:table", "Dask DataFrames",
         "A Dask DataFrame splits data into partitions that process in parallel."),
        ("fa6-solid:diagram-project", "Task graphs",
         "Dask builds a graph of operations and executes them only when you call <code class=\"font-mono\">.compute()</code>."),
        ("fa6-solid:scale-balanced", "When to use Dask",
         "Choose Dask when your data is too large for pandas but you want familiar syntax."),
    ),

    f"{MOD05}/lesson13_performance_profiling.html": (
        ("fa6-solid:stopwatch", "Time your code",
         '<code class="font-mono">time.time()</code> and <code class="font-mono">%timeit</code> measure how long any block of code takes.'),
        ("fa6-solid:microscope", "Profile with cProfile",
         '<code class="font-mono">cProfile</code> lists every function call and how much time each one took.'),
        ("fa6-solid:chart-bar", "Line-level profiling",
         "Line profilers show exactly which line inside a function is the bottleneck."),
        ("fa6-solid:wrench", "Act on the results",
         "Fix the slowest function first \u2014 profiling tells you where to focus."),
    ),

    f"{MOD05}/lesson14_real_large_data_project.html": (
        ("fa6-solid:flask", "End-to-end project",
         "You combined every technique into one pipeline that handles real-scale data."),
        ("fa6-solid:memory", "Optimise memory first",
         "Downcasting and category types shrank the dataset before heavy processing."),
        ("fa6-solid:bolt", "Process at scale",
         "Chunking, Polars, or DuckDB handled the workload that pandas alone could not."),
        ("fa6-solid:file-export", "Export final results",
         "The clean output landed in Parquet or a database, ready for analysis."),
    ),

    f"{MOD05}/lesson15_performance_best_practices.html": (
        ("fa6-solid:file-zipper", "Choose the right format",
         "Parquet and Feather outperform CSV for analytics workloads every time."),
        ("fa6-solid:code-compare", "Pick the right library",
         "Match pandas, Polars, or DuckDB to the size and shape of your data."),
        ("fa6-solid:memory", "Manage memory early",
         "Downcast types and drop unused columns before any heavy processing begins."),
        ("fa6-solid:gauge-high", "Measure before optimising",
         "Profile first \u2014 guessing where the bottleneck is wastes more time than measuring."),
    ),

    # ── MOD 06 — Automation and CI/CD ─────────────────────────────────────────

    f"{MOD06}/lesson01_devops_concepts_for_data_analytics.html": (
        ("fa6-solid:gears", "What DevOps means",
         "DevOps merges development and operations into one continuous delivery workflow."),
        ("fa6-solid:arrows-rotate", "DevOps for data teams",
         "The same build-test-deploy loop applies to data pipelines and ETL scripts."),
        ("fa6-solid:robot", "Automation benefits",
         "Automated tests and deployments catch errors before they reach production."),
        ("fa6-solid:server", "Deployment basics",
         "Pushing code to a server or cloud follows a repeatable, version-controlled process."),
    ),

    f"{MOD06}/lesson02_gitlab_ci_cd_overview.html": (
        ("fa6-solid:code-branch", "What CI/CD is",
         "Continuous integration tests every push; continuous delivery deploys on success."),
        ("fa6-solid:file-code", "The .gitlab-ci.yml file",
         "One YAML file defines every stage, job, and script your pipeline will run."),
        ("fa6-solid:vials", "Automated testing",
         "Tests execute automatically on every push so broken code never reaches production."),
        ("fa6-solid:rocket", "Automated deployment",
         "Passing tests trigger deployment to staging or production without manual steps."),
    ),

    f"{MOD06}/lesson03_scheduling_data_jobs.html": (
        ("fa6-solid:calendar-check", "Why schedule jobs",
         "Scheduled runs ensure fresh data is waiting before the business day begins."),
        ("fa6-solid:terminal", "Cron and Task Scheduler",
         "Cron on Linux and Task Scheduler on Windows trigger scripts at set times."),
        ("fa6-solid:clock-rotate-left", "CI/CD triggers",
         "Pipeline schedules in GitLab CI can also kick off data jobs on a timetable."),
        ("fa6-solid:bell", "Monitor and alert",
         "Alerts on failure let you fix a broken job before users see stale data."),
    ),

    f"{MOD06}/lesson05_deployment_workflow.html": (
        ("fa6-solid:code-branch", "Development to production",
         "Code flows from a local branch through staging to production in clear stages."),
        ("fa6-solid:vials", "Test before deploying",
         "Automated tests must pass before any code is promoted to the next environment."),
        ("fa6-solid:rocket", "Deploy with CI/CD",
         "A passing pipeline automatically pushes your code to the production server."),
        ("fa6-solid:shield-halved", "Rollback strategy",
         "Reverting to the previous commit restores production if a release breaks."),
    ),
}


# ── Main ──────────────────────────────────────────────────────────────────────
assert len(LESSONS) == 56, f"Expected 56 lessons, got {len(LESSONS)}"

ok = fail = 0
for rel, cards in LESSONS.items():
    path = ROOT / rel
    if not path.exists():
        print(f"\u274c NOT FOUND  {rel}")
        fail += 1
        continue
    text = path.read_text(encoding="utf-8")
    new_sec = build_section(cards)
    new_text, n = PATTERN.subn(new_sec, text, count=1)
    if n == 0:
        print(f"\u274c NO MATCH   {rel}")
        fail += 1
        continue
    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {rel}")
    ok += 1

print(f"\n{ok}/{ok + fail} recap sections rewritten")
