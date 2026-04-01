"""Rewrite <section id="objective"> for every lesson in track_03."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_03_data_engineering")
OBJ_RE = re.compile(
    r'<section id="objective">.*?</section>',
    re.DOTALL,
)

SECTION_TEMPLATE = '''<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Objective</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The goal and expected outcome of this lesson</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="{icon1}"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">{title1}</p>
            <p class="text-xs text-gray-500 mt-0.5">{desc1}</p>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="{icon2}"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">{title2}</p>
            <p class="text-xs text-gray-500 mt-0.5">{desc2}</p>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="{icon3}"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">{title3}</p>
            <p class="text-xs text-gray-500 mt-0.5">{desc3}</p>
          </div>
        </div>

        <!-- Card 4 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="{icon4}"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">{title4}</p>
            <p class="text-xs text-gray-500 mt-0.5">{desc4}</p>
          </div>
        </div>

      </div>
      <div class="mt-5">
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">{tip}</p>
        </div>
      </div>
    </div>
  </div>
</section>'''


def build(icon1, title1, desc1, icon2, title2, desc2,
          icon3, title3, desc3, icon4, title4, desc4, tip):
    return {
        "icon1": icon1, "title1": title1, "desc1": desc1,
        "icon2": icon2, "title2": title2, "desc2": desc2,
        "icon3": icon3, "title3": title3, "desc3": desc3,
        "icon4": icon4, "title4": title4, "desc4": desc4,
        "tip": tip,
    }


LESSONS = {
    # ═══════════════════════════════════════════════════════════════
    # MODULE 01 — Data Engineering Foundations
    # ═══════════════════════════════════════════════════════════════
    "mod_01_data_engineering_foundations/lesson01_what_is_data_engineering.html": build(
        "fa6-solid:gears", "Define data engineering",
        "Explain what data engineering is and how it supports analytics and machine learning workflows.",
        "fa6-solid:arrows-split-up-and-left", "Distinguish related roles",
        "Describe how data engineering differs from data analysis and data science in daily work.",
        "fa6-solid:hammer", "Core responsibilities",
        "Identify the main tasks a data engineer handles, from pipelines to infrastructure.",
        "fa6-solid:link", "Why it matters",
        "Understand why reliable data engineering is essential before any analysis can begin.",
        "This lesson introduces data engineering as a discipline so you can see where pipeline-building fits in the broader data landscape.",
    ),
    "mod_01_data_engineering_foundations/lesson02_etl_vs_elt.html": build(
        "fa6-solid:right-left", "Compare ETL and ELT",
        "Describe the key difference between transforming data before versus after loading it.",
        "fa6-solid:industry", "Traditional ETL pattern",
        "Explain how ETL transforms data in a staging area before it reaches the warehouse.",
        "fa6-solid:cloud-arrow-up", "Modern ELT pattern",
        "Explain how ELT loads raw data first and transforms it inside the warehouse.",
        "fa6-solid:scale-balanced", "Choose the right approach",
        "Decide which architecture fits a given project based on data volume and tooling.",
        "This lesson compares ETL and ELT so you can pick the right pipeline architecture for your next project.",
    ),
    "mod_01_data_engineering_foundations/lesson03_handling_large_datasets.html": build(
        "fa6-solid:triangle-exclamation", "Recognise memory limits",
        "Explain why loading a multi-gigabyte file into memory crashes most Python scripts.",
        "fa6-solid:puzzle-piece", "Chunk-based reading",
        "Read large CSV files in manageable chunks instead of loading them all at once.",
        "fa6-solid:filter", "Selective column loading",
        "Reduce memory usage by loading only the columns your analysis actually needs.",
        "fa6-solid:microchip", "Downcast data types",
        "Shrink DataFrame memory by converting columns to smaller numeric or categorical types.",
        "This lesson gives you practical techniques for working with datasets too large for a single pandas read.",
    ),
    "mod_01_data_engineering_foundations/lesson05_parquet_efficient_storage.html": build(
        "fa6-solid:file-zipper", "What Parquet is",
        "Describe the Parquet columnar format and why data engineers prefer it over CSV.",
        "fa6-solid:database", "Columnar storage benefits",
        "Explain how storing data by column speeds up analytical queries and compresses files.",
        "fa6-solid:arrow-right-arrow-left", "Convert CSV to Parquet",
        "Write Python code that reads a CSV file and saves it as a Parquet file using pandas.",
        "fa6-solid:magnifying-glass-chart", "Read Parquet efficiently",
        "Load only the columns you need from a Parquet file to cut memory and read time.",
        "This lesson shows you why Parquet is the default file format in modern data pipelines and how to use it from Python.",
    ),
    "mod_01_data_engineering_foundations/lesson06_intro_to_polars_optional.html": build(
        "fa6-solid:bolt", "What Polars is",
        "Describe Polars as a Rust-powered DataFrame library designed for speed and low memory use.",
        "fa6-solid:gauge-high", "Why Polars is faster",
        "Explain how Polars uses multi-threading and Apache Arrow to outperform pandas on large data.",
        "fa6-solid:laptop-code", "Basic Polars operations",
        "Filter, select, and aggregate data using the Polars expression API in Python.",
        "fa6-solid:code-compare", "Compare with pandas",
        "Recognise when Polars is a better fit than pandas based on dataset size and workflow.",
        "This lesson introduces Polars as an optional high-performance alternative to pandas for large-scale data processing.",
    ),
    "mod_01_data_engineering_foundations/lesson07_pipeline_design_concepts.html": build(
        "fa6-solid:diagram-project", "Pipeline stages",
        "Describe how extract, transform, and load stages connect to form a complete pipeline.",
        "fa6-solid:cubes", "Modular design",
        "Explain why each pipeline step should be a separate, testable function or module.",
        "fa6-solid:arrows-rotate", "Idempotent processing",
        "Understand why running a pipeline twice should produce the same result without duplicating data.",
        "fa6-solid:shield-halved", "Error handling patterns",
        "Identify common failure points in pipelines and how logging and retries keep them reliable.",
        "This lesson teaches you how to structure a data pipeline so each stage is modular, testable, and easy to maintain.",
    ),

    # ═══════════════════════════════════════════════════════════════
    # MODULE 02 — NoSQL and Modern Data Storage
    # ═══════════════════════════════════════════════════════════════
    "mod_02_nosql_and_modern_data_storage/lesson01_what_is_nosql.html": build(
        "fa6-solid:database", "Define NoSQL",
        "Explain what NoSQL databases are and how they differ from traditional relational databases.",
        "fa6-solid:lightbulb", "Why NoSQL was created",
        "Describe the scalability and flexibility challenges that led to NoSQL adoption.",
        "fa6-solid:right-left", "SQL vs NoSQL basics",
        "Identify the key structural differences between table-based SQL and schema-flexible NoSQL.",
        "fa6-solid:crosshairs", "NoSQL use cases",
        "Recognise the types of problems — high-volume, unstructured, real-time — NoSQL is built to solve.",
        "This lesson introduces NoSQL databases so you understand when they solve problems that relational databases cannot.",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson02_types_of_nosql_databases.html": build(
        "fa6-solid:layer-group", "Four NoSQL families",
        "Name the four main NoSQL categories: document, key-value, column-family, and graph.",
        "fa6-solid:box-open", "How each stores data",
        "Describe the data model each family uses and how it shapes queries and performance.",
        "fa6-solid:wrench", "Problems each solves",
        "Match each NoSQL type to the real-world scenarios where it is the strongest choice.",
        "fa6-solid:map-signs", "Choosing a type",
        "Decide which NoSQL category fits a project based on data shape and access patterns.",
        "This lesson maps the four NoSQL families so you can quickly match a database type to your data problem.",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson03_document_databases_mongodb.html": build(
        "fa6-solid:file-lines", "Document model",
        "Explain how MongoDB stores records as flexible JSON-like documents instead of fixed-row tables.",
        "fa6-solid:pen-to-square", "Insert and update documents",
        "Write Python code that inserts new documents and updates existing fields in a MongoDB collection.",
        "fa6-solid:magnifying-glass", "Query documents",
        "Build MongoDB queries that filter, project, and sort documents from Python.",
        "fa6-solid:table-columns", "Documents vs SQL rows",
        "Compare the document model with relational tables to understand the flexibility trade-offs.",
        "This lesson teaches you to create, read, and update MongoDB documents from Python so you can work with flexible, schema-free data.",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson04_key_value_databases_redis.html": build(
        "fa6-solid:key", "Key-value model",
        "Describe how Redis stores every piece of data as a simple key mapped to a value.",
        "fa6-solid:bolt", "In-memory speed",
        "Explain why keeping all data in RAM makes Redis reads and writes extremely fast.",
        "fa6-solid:box-archive", "Core Redis operations",
        "Use Python to set, get, and delete keys, and work with lists, hashes, and counters.",
        "fa6-solid:clock-rotate-left", "Caching use cases",
        "Identify when Redis caching improves application performance and reduces database load.",
        "This lesson shows you how Redis stores and retrieves data at in-memory speed, making it ideal for caching and real-time features.",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson05_column_family_databases_cassandra.html": build(
        "fa6-solid:table-cells", "Column-family model",
        "Describe how Cassandra organises data into column families instead of traditional rows and columns.",
        "fa6-solid:server", "Distributed architecture",
        "Explain how Cassandra spreads data across many nodes for high availability and fault tolerance.",
        "fa6-solid:pen-to-square", "Write and query data",
        "Use Python to insert rows and run CQL queries against a Cassandra cluster.",
        "fa6-solid:chart-line", "High-throughput scenarios",
        "Recognise workloads — like IoT streams and logging — where Cassandra excels over relational databases.",
        "This lesson explains how Cassandra handles massive write volumes across distributed clusters so you know when to choose it.",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson06_graph_databases_neo4j.html": build(
        "fa6-solid:circle-nodes", "Graph model",
        "Explain how Neo4j represents data as nodes and relationships instead of tables and joins.",
        "fa6-solid:magnifying-glass", "Cypher queries",
        "Write basic Cypher queries to find nodes and traverse relationships in a graph database.",
        "fa6-solid:share-nodes", "Relationship traversal",
        "Describe how following edges between nodes replaces the need for expensive multi-table joins.",
        "fa6-solid:users", "Graph use cases",
        "Identify real problems — social networks, fraud detection, recommendations — where graphs shine.",
        "This lesson introduces graph databases so you can model and query highly connected data that would be slow in SQL.",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson07_sql_vs_nosql_choosing_the_right_database.html": build(
        "fa6-solid:scale-balanced", "Compare trade-offs",
        "Weigh the consistency, scalability, and flexibility trade-offs between SQL and NoSQL databases.",
        "fa6-solid:list-check", "Decision criteria",
        "Use a practical checklist of data shape, query pattern, and scale to guide your database choice.",
        "fa6-solid:diagram-project", "Polyglot persistence",
        "Understand how real systems combine multiple database types to handle different data needs.",
        "fa6-solid:route", "Make the call",
        "Choose the right database technology for a given data scenario and justify the decision.",
        "This lesson gives you a decision framework so you can confidently pick SQL, NoSQL, or both for any data project.",
    ),

    # ═══════════════════════════════════════════════════════════════
    # MODULE 03 — API Data Integration
    # ═══════════════════════════════════════════════════════════════
    "mod_03_api_data_integration/lesson01_what_is_an_api.html": build(
        "fa6-solid:plug", "Define an API",
        "Explain what an API is and how it lets one program request data from another over the internet.",
        "fa6-solid:network-wired", "Why APIs exist",
        "Describe why modern data systems use APIs to share data between services and platforms.",
        "fa6-solid:arrows-left-right", "Request-response cycle",
        "Outline the basic flow: your code sends a request, the server returns a response.",
        "fa6-solid:laptop-code", "Python and APIs",
        "Understand how Python scripts call APIs to pull live data into your analysis workflow.",
        "This lesson introduces APIs as the standard way programs exchange data, setting the foundation for every API lesson that follows.",
    ),
    "mod_03_api_data_integration/lesson02_understanding_http_requests.html": build(
        "fa6-solid:globe", "HTTP basics",
        "Describe what an HTTP request is and how it carries data between a client and a server.",
        "fa6-solid:list-ol", "Request methods",
        "Distinguish GET, POST, PUT, and DELETE and know when each method is used.",
        "fa6-solid:circle-check", "Status codes",
        "Read common status codes — 200, 401, 404, 500 — and understand what each one means.",
        "fa6-solid:sliders", "Headers and parameters",
        "Explain how headers and query parameters customise the data a server sends back.",
        "This lesson teaches you the HTTP building blocks your code uses every time it talks to an API.",
    ),
    "mod_03_api_data_integration/lesson03_using_the_python_requests_library.html": build(
        "fa6-solid:download", "Install and import requests",
        "Set up the requests library and import it into a Python script ready for API calls.",
        "fa6-solid:paper-plane", "Send GET and POST requests",
        "Write Python code that sends GET and POST requests to an API endpoint.",
        "fa6-solid:file-code", "Inspect responses",
        "Access the status code, headers, and body of an API response in Python.",
        "fa6-solid:code", "Parse JSON responses",
        "Convert the JSON body of an API response into a Python dictionary for processing.",
        "This lesson shows you how to use the requests library to send API calls and handle the responses entirely in Python.",
    ),
    "mod_03_api_data_integration/lesson04_working_with_json_data.html": build(
        "fa6-solid:brackets-curly", "JSON structure",
        "Describe how JSON uses key-value pairs and arrays to represent structured data.",
        "fa6-solid:file-import", "Parse JSON in Python",
        "Use the json module and response.json() to turn a JSON string into a Python dictionary.",
        "fa6-solid:sitemap", "Navigate nested data",
        "Access deeply nested fields in a JSON response using chained dictionary keys.",
        "fa6-solid:file-export", "Write JSON files",
        "Save Python data to a JSON file so you can reuse it without re-calling the API.",
        "This lesson teaches you to read, navigate, and write JSON — the format nearly every API uses to send data.",
    ),
    "mod_03_api_data_integration/lesson05_parsing_api_responses.html": build(
        "fa6-solid:triangle-exclamation", "Check status codes",
        "Inspect the response status code to determine whether an API call succeeded or failed.",
        "fa6-solid:shield-halved", "Handle errors gracefully",
        "Write try/except blocks that catch connection and HTTP errors without crashing your script.",
        "fa6-solid:layer-group", "Extract nested data",
        "Pull specific fields from deeply nested JSON structures returned by real APIs.",
        "fa6-solid:table", "Build clean datasets",
        "Flatten nested API data into a list of dictionaries ready for a DataFrame.",
        "This lesson teaches you to validate, error-handle, and extract data from API responses so your scripts stay robust.",
    ),
    "mod_03_api_data_integration/lesson06_authentication_with_api_keys.html": build(
        "fa6-solid:lock", "Why APIs need auth",
        "Explain why many APIs require authentication before they will return data.",
        "fa6-solid:key", "What an API key is",
        "Describe an API key as a unique token that identifies your application to the server.",
        "fa6-solid:paper-plane", "Send keys in requests",
        "Include an API key in headers or query parameters when calling a protected endpoint.",
        "fa6-solid:vault", "Store keys securely",
        "Keep API keys out of your source code by using environment variables or config files.",
        "This lesson shows you how to authenticate with API keys and store them safely so your credentials stay protected.",
    ),
    "mod_03_api_data_integration/lesson07_oauth_authentication.html": build(
        "fa6-solid:user-shield", "What OAuth is",
        "Describe OAuth as a token-based protocol that grants access without sharing passwords.",
        "fa6-solid:arrows-rotate", "The OAuth flow",
        "Outline the authorisation code flow — redirect, consent, token exchange — step by step.",
        "fa6-solid:ticket", "Access and refresh tokens",
        "Explain how access tokens expire and refresh tokens keep your session alive without re-login.",
        "fa6-solid:laptop-code", "OAuth in Python",
        "Use Python to obtain an OAuth token and attach it to API requests as a Bearer header.",
        "This lesson walks you through OAuth so you can connect to APIs like Google and GitHub that require token-based authentication.",
    ),
    "mod_03_api_data_integration/lesson08_handling_pagination_in_apis.html": build(
        "fa6-solid:book-open", "What pagination is",
        "Explain why APIs split large result sets into multiple pages instead of one response.",
        "fa6-solid:forward", "Page through results",
        "Write a Python loop that requests each page of data until all records are collected.",
        "fa6-solid:link", "Follow next-page links",
        "Parse Link headers and next-page URLs to navigate cursor-based pagination schemes.",
        "fa6-solid:list-check", "Collect complete datasets",
        "Build a script that assembles all pages into a single list without missing any records.",
        "This lesson teaches you to loop through paginated API responses so you always collect the full dataset.",
    ),
    "mod_03_api_data_integration/lesson09_handling_api_rate_limits.html": build(
        "fa6-solid:gauge-high", "What rate limits are",
        "Explain why APIs cap how many requests a client can send per minute or hour.",
        "fa6-solid:magnifying-glass", "Detect rate-limit errors",
        "Check for HTTP 429 status codes and Retry-After headers that signal you have been throttled.",
        "fa6-solid:clock", "Add delays and retries",
        "Use time.sleep and exponential backoff to space out requests and retry after limits reset.",
        "fa6-solid:shield-halved", "Build resilient scripts",
        "Combine rate-limit detection with retry logic so your data collection runs unattended overnight.",
        "This lesson teaches you to respect API rate limits and add retry logic so your scripts finish reliably without getting blocked.",
    ),
    "mod_03_api_data_integration/lesson10_loading_api_data_into_pandas.html": build(
        "fa6-solid:table", "JSON to DataFrame",
        "Convert a list of JSON records from an API response into a pandas DataFrame in one step.",
        "fa6-solid:filter", "Clean and filter",
        "Select, rename, and filter columns so the DataFrame contains only the data you need.",
        "fa6-solid:chart-bar", "Analyse API data",
        "Run pandas groupby, value_counts, and describe on data that came straight from an API.",
        "fa6-solid:file-csv", "Export for reuse",
        "Save the DataFrame to CSV or Parquet so you can analyse it again without re-calling the API.",
        "This lesson connects APIs to pandas so you can load live data directly into a DataFrame for analysis and export.",
    ),
    "mod_03_api_data_integration/lesson11_saving_api_data_to_databases.html": build(
        "fa6-solid:database", "Store data in SQLite",
        "Write API data into a SQLite database table using Python so it persists between script runs.",
        "fa6-solid:code", "Use pandas to_sql",
        "Load a DataFrame of API records into a database table with a single pandas method call.",
        "fa6-solid:arrows-rotate", "Upsert logic",
        "Handle duplicate records by replacing or ignoring rows that already exist in the table.",
        "fa6-solid:magnifying-glass", "Query stored data",
        "Run SQL queries against your database to retrieve and filter the API data you saved earlier.",
        "This lesson shows you how to persist API data in a SQLite database so you stop making repeated API calls for the same data.",
    ),
    "mod_03_api_data_integration/lesson12_building_an_api_data_pipeline.html": build(
        "fa6-solid:diagram-project", "Pipeline structure",
        "Design a three-stage pipeline that extracts API data, transforms it, and loads it into a database.",
        "fa6-solid:download", "Extract stage",
        "Write the extraction function that calls the API, paginates, and returns raw JSON records.",
        "fa6-solid:wand-magic-sparkles", "Transform stage",
        "Clean, rename, and reshape the raw records into a DataFrame ready for storage.",
        "fa6-solid:database", "Load stage",
        "Insert the transformed data into a SQLite table and log how many rows were written.",
        "This lesson ties extraction, transformation, and loading together into one script you can run end to end.",
    ),
    "mod_03_api_data_integration/lesson13_real_world_api_integration_project.html": build(
        "fa6-solid:flask", "Build a complete pipeline",
        "Combine API calls, error handling, pagination, and storage into one working project.",
        "fa6-solid:shield-halved", "Handle real-world errors",
        "Add retry logic, rate-limit detection, and timeout handling to keep the pipeline running.",
        "fa6-solid:table", "Transform into DataFrames",
        "Parse raw API responses, flatten nested fields, and produce a clean DataFrame.",
        "fa6-solid:database", "Persist for analysis",
        "Save the final dataset to a database and verify it is ready for downstream queries.",
        "This lesson is a hands-on project that pulls together every API skill you have learned into a production-style data pipeline.",
    ),
    "mod_03_api_data_integration/lesson14_api_best_practices.html": build(
        "fa6-solid:shield-halved", "Defensive error handling",
        "Wrap every API call in error handling that logs failures and retries before giving up.",
        "fa6-solid:file-lines", "Logging and monitoring",
        "Add Python logging so you can trace what your pipeline did and diagnose problems fast.",
        "fa6-solid:vault", "Credential management",
        "Store API keys and tokens in environment variables or secret managers, never in source code.",
        "fa6-solid:book", "Document your integrations",
        "Write clear README notes that describe each API endpoint, authentication method, and data schema.",
        "This lesson collects the habits that keep API integrations reliable in production — error handling, logging, and safe credential storage.",
    ),

    # ═══════════════════════════════════════════════════════════════
    # MODULE 04 — Data Pipelines and Orchestration
    # ═══════════════════════════════════════════════════════════════
    "mod_04_data_pipelines_and_orchestration/lesson01_what_is_a_data_pipeline.html": build(
        "fa6-solid:diagram-project", "Define a data pipeline",
        "Explain what a data pipeline is and how it moves data from source to destination automatically.",
        "fa6-solid:building", "Why organisations build them",
        "Describe the business problems — inconsistent data, manual steps, stale reports — that pipelines solve.",
        "fa6-solid:layer-group", "Pipeline stages",
        "Identify the extract, transform, and load stages that make up a typical data pipeline.",
        "fa6-solid:laptop-code", "Python in pipelines",
        "Understand why Python is one of the most common languages for writing pipeline scripts.",
        "This lesson introduces data pipelines as the backbone of any analytics workflow and shows how Python fits into the picture.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson02_etl_vs_elt.html": build(
        "fa6-solid:right-left", "ETL vs ELT",
        "Describe the key difference between transforming data before loading and after loading.",
        "fa6-solid:industry", "When to use ETL",
        "Identify scenarios where transforming data in a staging area before loading is the better choice.",
        "fa6-solid:cloud-arrow-up", "When to use ELT",
        "Recognise when loading raw data first and transforming inside the warehouse is more efficient.",
        "fa6-solid:scale-balanced", "Compare architectures",
        "Evaluate the cost, complexity, and latency trade-offs between ETL and ELT for a given project.",
        "This lesson compares ETL and ELT pipeline architectures so you can justify the right choice for your data workflow.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson03_pipeline_design_patterns.html": build(
        "fa6-solid:cubes", "Common patterns",
        "Name the most widely used pipeline design patterns — batch, streaming, fan-out, and star.",
        "fa6-solid:clock", "Batch vs streaming",
        "Explain when to process data in scheduled batches versus continuously in real time.",
        "fa6-solid:arrows-split-up-and-left", "Fan-out and merge",
        "Describe how fan-out splits one data stream into parallel branches that merge back together.",
        "fa6-solid:arrows-rotate", "Idempotent steps",
        "Understand why each pipeline step should produce the same result if it runs more than once.",
        "This lesson surveys pipeline design patterns so you can choose the right architecture before writing any code.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson04_working_with_large_data_files.html": build(
        "fa6-solid:triangle-exclamation", "Memory constraints",
        "Explain why loading a multi-gigabyte file all at once crashes most Python scripts.",
        "fa6-solid:puzzle-piece", "Chunk-based processing",
        "Read and transform large CSV files in chunks so only a small portion sits in memory at a time.",
        "fa6-solid:filter", "Selective loading",
        "Reduce memory by loading only the columns and rows your pipeline step actually needs.",
        "fa6-solid:file-arrow-down", "Streaming writes",
        "Write processed chunks directly to disk or a database instead of holding results in memory.",
        "This lesson equips you to process files that are too large for memory by reading, transforming, and writing in chunks.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson05_data_validation_in_pipelines.html": build(
        "fa6-solid:clipboard-check", "Why validate data",
        "Explain why catching bad data early prevents errors in downstream reports and models.",
        "fa6-solid:spell-check", "Common validation rules",
        "Write checks for missing values, wrong types, duplicate rows, and out-of-range numbers.",
        "fa6-solid:ban", "Reject bad records",
        "Separate invalid rows into a quarantine file while letting clean data flow through the pipeline.",
        "fa6-solid:file-lines", "Log validation results",
        "Record how many rows passed and failed so you can monitor data quality over time.",
        "This lesson adds validation checks to your pipeline so bad data is caught and logged before it reaches your database.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson09_scheduling_pipelines.html": build(
        "fa6-solid:calendar-check", "Why schedule pipelines",
        "Explain why data pipelines need to run automatically on a fixed schedule without manual effort.",
        "fa6-solid:terminal", "Cron and Task Scheduler",
        "Set up a cron job on Linux or a Scheduled Task on Windows to run a Python script daily.",
        "fa6-solid:clock-rotate-left", "Run intervals",
        "Choose the right frequency — hourly, daily, weekly — based on how often your data changes.",
        "fa6-solid:bell", "Monitor scheduled runs",
        "Add logging and email alerts so you know immediately when a scheduled pipeline fails.",
        "This lesson teaches you to schedule Python pipelines so your data refreshes automatically without anyone clicking Run.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson10_building_a_simple_python_pipeline.html": build(
        "fa6-solid:hammer", "Build end to end",
        "Write a complete Python pipeline that extracts, transforms, and loads data in one script.",
        "fa6-solid:download", "Extract from files",
        "Read source data from a CSV file into a pandas DataFrame as the first pipeline stage.",
        "fa6-solid:wand-magic-sparkles", "Transform data",
        "Clean, filter, and reshape the DataFrame so it matches the target schema.",
        "fa6-solid:database", "Load into SQLite",
        "Insert the transformed data into a SQLite table and confirm the row count matches expectations.",
        "This lesson walks you through building a working extract-transform-load pipeline in Python from start to finish.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson11_pipeline_project_automating_data_ingestion.html": build(
        "fa6-solid:folder-open", "Watch for new files",
        "Write a script that scans a folder for new CSV files and picks them up automatically.",
        "fa6-solid:clipboard-check", "Validate on arrival",
        "Run basic checks — file size, required columns, no empty rows — before processing each file.",
        "fa6-solid:database", "Load into the database",
        "Insert validated records into a SQLite table and move the processed file to an archive folder.",
        "fa6-solid:file-lines", "Log every step",
        "Record timestamps, file names, and row counts so you can audit what the pipeline did.",
        "This lesson builds an automated ingestion script that watches for new files, validates them, and loads them into a database.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson12_pipeline_project_data_quality_checks.html": build(
        "fa6-solid:magnifying-glass", "Detect bad records",
        "Write checks that flag missing values, duplicate rows, and numbers outside expected ranges.",
        "fa6-solid:code-branch", "Split good and bad data",
        "Route clean rows to the main table and quarantine invalid rows in a separate file for review.",
        "fa6-solid:chart-pie", "Quality metrics",
        "Calculate pass rates and failure counts so you can track data quality across pipeline runs.",
        "fa6-solid:bell", "Alert on failures",
        "Log warnings and raise alerts when the failure rate exceeds a threshold you define.",
        "This lesson adds quality gates to your pipeline so invalid records are flagged and isolated before they corrupt your database.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson13_pipeline_project_database_loading.html": build(
        "fa6-solid:database", "Load validated data",
        "Write validated records into a production SQLite table with proper column types and constraints.",
        "fa6-solid:arrows-rotate", "Upsert strategy",
        "Handle repeat runs by updating existing rows and inserting new ones without creating duplicates.",
        "fa6-solid:layer-group", "Raw vs processed tables",
        "Separate raw ingestion data from cleaned, analytics-ready tables inside the same database.",
        "fa6-solid:file-lines", "Audit trail",
        "Log load timestamps, row counts, and any skipped records so every pipeline run is traceable.",
        "This lesson completes the pipeline project by loading clean data into analytics tables with upsert logic and full audit logging.",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson14_production_pipeline_architecture.html": build(
        "fa6-solid:server", "Production components",
        "Identify the key parts of a production pipeline — config files, logging, monitoring, and secrets.",
        "fa6-solid:gears", "Configuration management",
        "Use config files and environment variables so the same script works in dev, staging, and production.",
        "fa6-solid:eye", "Monitoring and alerts",
        "Set up health checks and alerts that notify you when a pipeline run fails or stalls.",
        "fa6-solid:shield-halved", "Graceful error recovery",
        "Design retry logic and checkpoint files so a failed pipeline can resume where it left off.",
        "This lesson shows you how production pipelines are structured with configuration, monitoring, and error recovery built in.",
    ),

    # ═══════════════════════════════════════════════════════════════
    # MODULE 05 — Large Scale Data Processing
    # ═══════════════════════════════════════════════════════════════
    "mod_05_large_scale_data_processing/lesson02_memory_optimization.html": build(
        "fa6-solid:memory", "Measure memory usage",
        "Use DataFrame.info() and memory_usage() to see exactly how much RAM your data consumes.",
        "fa6-solid:arrow-down-short-wide", "Downcast numeric types",
        "Shrink integer and float columns by converting them to smaller types that still hold the data.",
        "fa6-solid:tags", "Use category dtype",
        "Convert low-cardinality string columns to the category type to cut memory by 90% or more.",
        "fa6-solid:trash-can", "Drop unneeded columns",
        "Remove columns your analysis does not need so they stop consuming memory from the start.",
        "This lesson teaches you to measure and reduce DataFrame memory so you can work with larger datasets on the same machine.",
    ),
    "mod_05_large_scale_data_processing/lesson03_chunk_processing.html": build(
        "fa6-solid:puzzle-piece", "What chunk processing is",
        "Explain how reading a file in small pieces lets you process data that does not fit in memory.",
        "fa6-solid:file-import", "Read CSV in chunks",
        "Use the chunksize parameter in pandas.read_csv to iterate over a large file one batch at a time.",
        "fa6-solid:calculator", "Aggregate across chunks",
        "Accumulate sums, counts, and means across chunks to produce a final result without loading everything.",
        "fa6-solid:scale-balanced", "Choose the right chunk size",
        "Pick a chunk size that balances memory usage against processing overhead for your hardware.",
        "This lesson shows you how to process files larger than memory by reading, computing, and writing one chunk at a time.",
    ),
    "mod_05_large_scale_data_processing/lesson04_processing_millions_of_rows.html": build(
        "fa6-solid:bolt", "Vectorised operations",
        "Use pandas vectorisation to apply calculations to millions of rows without writing Python loops.",
        "fa6-solid:ban", "Avoid slow loops",
        "Recognise why iterating row-by-row with a for loop is thousands of times slower than vectorised code.",
        "fa6-solid:gauge-high", "Time your code",
        "Measure execution time with %%timeit and time.perf_counter to prove your optimisations work.",
        "fa6-solid:layer-group", "Batch processing strategies",
        "Combine chunked reading with vectorised transforms to handle datasets that exceed available memory.",
        "This lesson shows you how to process millions of rows in seconds using vectorised pandas instead of slow Python loops.",
    ),
    "mod_05_large_scale_data_processing/lesson05_columnar_storage.html": build(
        "fa6-solid:table-columns", "Row vs column storage",
        "Explain how row-based formats read entire records while column-based formats read only the columns you need.",
        "fa6-solid:bolt", "Faster analytics queries",
        "Describe why columnar storage speeds up aggregations and filters by skipping irrelevant columns.",
        "fa6-solid:file-zipper", "Better compression",
        "Understand how storing similar values together lets columnar files compress much smaller than CSV.",
        "fa6-solid:database", "Where columnar is used",
        "Name the tools and databases — Parquet, Arrow, BigQuery — that rely on columnar storage.",
        "This lesson explains why columnar storage is faster and smaller than CSV so you understand the format behind Parquet.",
    ),
    "mod_05_large_scale_data_processing/lesson06_parquet_files.html": build(
        "fa6-solid:file-zipper", "Read and write Parquet",
        "Use pandas to save a DataFrame as a Parquet file and read it back with a single method call.",
        "fa6-solid:filter", "Select columns on read",
        "Load only the columns you need from a Parquet file to save memory and speed up reads.",
        "fa6-solid:magnifying-glass-chart", "Inspect metadata",
        "Use PyArrow to check row counts, column names, and compression stats without reading the data.",
        "fa6-solid:right-left", "Compare with CSV",
        "Benchmark file size and read speed between CSV and Parquet to see the difference on your own data.",
        "This lesson teaches you to read, write, and inspect Parquet files so you can replace slow CSV workflows.",
    ),
    "mod_05_large_scale_data_processing/lesson07_pyarrow_basics.html": build(
        "fa6-solid:feather", "What PyArrow is",
        "Describe PyArrow as the Python library that provides in-memory columnar data and Parquet support.",
        "fa6-solid:table", "Create Arrow tables",
        "Build an Arrow Table from Python lists or dictionaries and inspect its schema and row count.",
        "fa6-solid:right-left", "Convert to pandas",
        "Move data between Arrow Tables and pandas DataFrames with zero-copy when possible.",
        "fa6-solid:file-lines", "Read Parquet metadata",
        "Use PyArrow to read file-level and row-group metadata without loading any data into memory.",
        "This lesson introduces PyArrow so you can create Arrow tables, convert between formats, and inspect Parquet metadata.",
    ),
    "mod_05_large_scale_data_processing/lesson08_introduction_to_polars.html": build(
        "fa6-solid:bolt", "What Polars is",
        "Describe Polars as a Rust-based DataFrame library that is often faster than pandas on large data.",
        "fa6-solid:laptop-code", "Basic Polars operations",
        "Filter, select, group, and aggregate data using the Polars expression syntax.",
        "fa6-solid:gauge-high", "Speed and memory",
        "Explain how multi-threading and Apache Arrow give Polars its performance advantage.",
        "fa6-solid:code-compare", "Polars vs pandas",
        "Compare equivalent operations in both libraries so you can switch between them confidently.",
        "This lesson introduces the Polars library so you can start using a faster alternative to pandas for large datasets.",
    ),
    "mod_05_large_scale_data_processing/lesson09_faster_dataframes_with_polars.html": build(
        "fa6-solid:wand-magic-sparkles", "Lazy evaluation",
        "Explain how Polars lazy mode builds a query plan and optimises it before executing anything.",
        "fa6-solid:link", "Expression chaining",
        "Write fluent Polars expressions that filter, transform, and aggregate in a single readable chain.",
        "fa6-solid:microchip", "Multi-threaded execution",
        "Describe how Polars automatically uses all CPU cores to parallelise DataFrame operations.",
        "fa6-solid:chart-line", "Benchmark against pandas",
        "Run the same operations in pandas and Polars to measure the speed difference on your own data.",
        "This lesson goes deeper with Polars — lazy evaluation, expression chaining, and multi-threading — so you can process millions of rows fast.",
    ),
    "mod_05_large_scale_data_processing/lesson10_duckdb_for_analytics.html": build(
        "fa6-solid:database", "What DuckDB is",
        "Describe DuckDB as an in-process SQL database optimised for analytical queries on local files.",
        "fa6-solid:file-code", "SQL on files",
        "Write SQL queries that run directly on CSV and Parquet files without importing data first.",
        "fa6-solid:right-left", "Integrate with pandas",
        "Move data between DuckDB query results and pandas DataFrames in a single line of Python.",
        "fa6-solid:bolt", "Performance advantages",
        "Explain why DuckDB runs analytical queries faster than pandas on large datasets.",
        "This lesson shows you how DuckDB lets you run SQL directly on CSV and Parquet files for fast, serverless analytics.",
    ),
    "mod_05_large_scale_data_processing/lesson11_parallel_processing.html": build(
        "fa6-solid:microchip", "What parallel processing is",
        "Explain how splitting work across multiple CPU cores finishes data tasks faster.",
        "fa6-solid:gears", "concurrent.futures",
        "Use ProcessPoolExecutor to run a function on many data chunks in parallel with minimal code.",
        "fa6-solid:code-branch", "multiprocessing module",
        "Write a multiprocessing Pool that distributes rows across workers and collects the results.",
        "fa6-solid:triangle-exclamation", "Pitfalls and overhead",
        "Recognise when parallel processing helps and when the overhead of spawning processes makes it slower.",
        "This lesson teaches you to split data work across CPU cores so processing-heavy tasks finish in a fraction of the time.",
    ),
    "mod_05_large_scale_data_processing/lesson12_dask_basics.html": build(
        "fa6-solid:cubes", "What Dask is",
        "Describe Dask as a library that scales pandas-like operations across multiple cores and beyond memory.",
        "fa6-solid:table", "Dask DataFrames",
        "Create a Dask DataFrame from a large CSV and run familiar pandas operations on it lazily.",
        "fa6-solid:diagram-project", "Task graphs",
        "Understand how Dask builds a task graph of operations and executes them in parallel on compute.",
        "fa6-solid:scale-balanced", "When to use Dask",
        "Decide whether Dask, Polars, or plain pandas is the right tool for your data size and workflow.",
        "This lesson introduces Dask so you can apply familiar pandas operations to datasets that do not fit in memory.",
    ),
    "mod_05_large_scale_data_processing/lesson13_performance_profiling.html": build(
        "fa6-solid:stopwatch", "Time your code",
        "Use time.perf_counter and %%timeit to measure how long each part of your script takes.",
        "fa6-solid:microscope", "Profile with cProfile",
        "Run cProfile to find which functions consume the most time across an entire script run.",
        "fa6-solid:chart-bar", "Line-level profiling",
        "Use line_profiler to pinpoint the exact lines of code that are slowing your data processing.",
        "fa6-solid:wrench", "Act on the results",
        "Translate profiling output into targeted fixes — vectorise, cache, or switch to a faster library.",
        "This lesson teaches you to find the slow parts of your code so you optimise where it actually matters.",
    ),
    "mod_05_large_scale_data_processing/lesson14_real_large_data_project.html": build(
        "fa6-solid:flask", "End-to-end project",
        "Build a complete workflow that loads, optimises, processes, and exports a multi-million-row dataset.",
        "fa6-solid:memory", "Optimise memory first",
        "Apply downcasting, category types, and selective loading before any transformation step.",
        "fa6-solid:bolt", "Process at scale",
        "Use Parquet, Polars, or DuckDB to transform millions of rows without waiting or crashing.",
        "fa6-solid:file-export", "Export final results",
        "Write the processed data to Parquet and CSV so it is ready for dashboards or further analysis.",
        "This lesson is a hands-on project where you apply every large-data technique from this module on a real dataset.",
    ),
    "mod_05_large_scale_data_processing/lesson15_performance_best_practices.html": build(
        "fa6-solid:file-zipper", "Choose the right format",
        "Pick Parquet over CSV for any dataset you read more than once or share with a team.",
        "fa6-solid:code-compare", "Pick the right library",
        "Decide between pandas, Polars, DuckDB, and Dask based on your data size and query style.",
        "fa6-solid:memory", "Manage memory early",
        "Downcast types and load only needed columns at the start of every script, not as an afterthought.",
        "fa6-solid:gauge-high", "Measure before optimising",
        "Profile your code first so you spend effort on the lines that are actually slow.",
        "This lesson collects the key performance principles so you have a quick-reference checklist for every large-data project.",
    ),

    # ═══════════════════════════════════════════════════════════════
    # MODULE 06 — Automation and CI/CD
    # ═══════════════════════════════════════════════════════════════
    "mod_06_automation_and_ci_cd/lesson01_devops_concepts_for_data_analytics.html": build(
        "fa6-solid:gears", "What DevOps means",
        "Describe DevOps as a set of practices that automate building, testing, and deploying software.",
        "fa6-solid:arrows-rotate", "DevOps for data teams",
        "Explain how version control, testing, and CI/CD apply to data scripts and pipeline code.",
        "fa6-solid:robot", "Automation benefits",
        "Identify the manual steps — running scripts, copying files, checking results — that automation eliminates.",
        "fa6-solid:server", "Deployment basics",
        "Understand how Python applications move from a developer's laptop to a production server.",
        "This lesson introduces DevOps practices so you can see how automation keeps data projects reliable and repeatable.",
    ),
    "mod_06_automation_and_ci_cd/lesson02_gitlab_ci_cd_overview.html": build(
        "fa6-solid:code-branch", "What CI/CD is",
        "Describe continuous integration and continuous delivery as automated build-test-deploy pipelines.",
        "fa6-solid:file-code", "The .gitlab-ci.yml file",
        "Write a basic YAML pipeline file that defines stages, jobs, and scripts for GitLab CI/CD.",
        "fa6-solid:vials", "Automated testing",
        "Set up a CI job that runs your Python tests every time you push a code change.",
        "fa6-solid:rocket", "Automated deployment",
        "Add a deploy stage that ships your data script to a server after all tests pass.",
        "This lesson shows you how GitLab CI/CD automates testing and deployment so your data scripts ship safely on every push.",
    ),
    "mod_06_automation_and_ci_cd/lesson03_scheduling_data_jobs.html": build(
        "fa6-solid:calendar-check", "Why schedule jobs",
        "Explain why data scripts need to run automatically on a timer instead of being triggered manually.",
        "fa6-solid:terminal", "Cron and Task Scheduler",
        "Set up a cron job on Linux or a Scheduled Task on Windows to run a Python script on a schedule.",
        "fa6-solid:clock-rotate-left", "CI/CD triggers",
        "Configure a GitLab CI/CD scheduled pipeline that runs your data job at a set interval.",
        "fa6-solid:bell", "Monitor and alert",
        "Add logging and notifications so you know immediately when a scheduled job fails.",
        "This lesson teaches you three ways to schedule Python scripts — cron, Task Scheduler, and CI/CD — so data refreshes happen automatically.",
    ),
    "mod_06_automation_and_ci_cd/lesson05_deployment_workflow.html": build(
        "fa6-solid:code-branch", "Development to production",
        "Describe the stages — local dev, staging, production — that code passes through before going live.",
        "fa6-solid:vials", "Test before deploying",
        "Run automated tests in a staging environment to catch bugs before they reach production.",
        "fa6-solid:rocket", "Deploy with CI/CD",
        "Use a CI/CD pipeline to push tested code to production automatically on every merge.",
        "fa6-solid:shield-halved", "Rollback strategy",
        "Plan a rollback procedure so you can revert to the last working version if a deployment fails.",
        "This lesson walks you through a deployment workflow — from local development through staging to production — so your data scripts ship safely.",
    ),
}


def main():
    ok = 0
    total = 0
    for rel_path, fields in LESSONS.items():
        fpath = ROOT / rel_path
        if not fpath.exists():
            print(f"  SKIP  {rel_path} (not found)")
            continue
        total += 1
        html = fpath.read_text(encoding="utf-8")
        new_section = SECTION_TEMPLATE.format(**fields)
        new_html, count = OBJ_RE.subn(new_section, html, count=1)
        if count == 0:
            print(f"  WARN  {rel_path} (no #objective section found)")
            continue
        fpath.write_text(new_html, encoding="utf-8")
        ok += 1
        print(f"  OK    {rel_path}")

    print(f"\n{ok}/{total} objective sections rewritten")


if __name__ == "__main__":
    main()
