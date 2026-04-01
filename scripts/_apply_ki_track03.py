"""
Apply standardised Key Takeaways (#key-ideas) cards to ALL Track 03 lessons.

Each lesson gets exactly 3 cards (pink / violet / blue) following the
template from the lesson-key-takeaways prompt.

Also patches CSS:
  - Adds border-color to .obj-card-kt:hover if missing
"""

import os
import re
import html as html_mod

BASE = "pages/track_03_data_engineering"

# ─── Lesson data ────────────────────────────────────────────────────
# key = relative path from BASE (forward-slash)
# value = dict with:
#   cards: list of 3 dicts, each with:
#     title, desc, pills (list of 3), icon (iconify data-icon value)
#
# Card 1 = pink (obj-card-kt)
# Card 2 = violet (obj-card-violet)
# Card 3 = blue (obj-card-blue)

LESSONS = {

# ═══════════════════════════════════════════════════════════
# MODULE 01 — Data Engineering Foundations
# ═══════════════════════════════════════════════════════════

"mod_01_data_engineering_foundations/lesson01_what_is_data_engineering.html": {
    # Overview: Data Sources, Data Pipelines, Data Storage, Data Quality
    "cards": [
        {"title": "Pipelines Power Every Dashboard",
         "desc": "Every chart or report you see relies on a pipeline that moved raw data from its source, cleaned it, and delivered it to the right place.",
         "pills": ["Automation", "Reliability", "Delivery"],
         "icon": "fa6-solid:arrow-right-arrow-left"},
        {"title": "Analysts Depend on Engineers",
         "desc": "Without a data engineer maintaining pipelines, an analyst's SQL query would return stale or broken results — like opening a spreadsheet that was never updated.",
         "pills": ["Trust", "Freshness", "Accuracy"],
         "icon": "fa6-solid:handshake"},
        {"title": "Scale Changes Everything",
         "desc": "A CSV with 500 rows opens instantly in Excel, but a dataset with 50 million rows needs specialised tools and a plan for memory, storage, and speed.",
         "pills": ["Volume", "Memory", "Throughput"],
         "icon": "fa6-solid:expand"},
    ],
},

"mod_01_data_engineering_foundations/lesson02_etl_vs_elt.html": {
    # Overview: Extract, Transform, Load, Order of Steps
    "cards": [
        {"title": "ETL Cleans Before Storing",
         "desc": "ETL reshapes data before it reaches the warehouse, much like formatting a spreadsheet before sending it to your manager for review.",
         "pills": ["Pre-process", "Staging", "Warehouse"],
         "icon": "fa6-solid:filter"},
        {"title": "ELT Uses Warehouse Power",
         "desc": "ELT loads raw data first, then transforms it inside the warehouse using SQL — the same language analysts already know from querying databases.",
         "pills": ["Raw Load", "SQL Transform", "Cloud"],
         "icon": "fa6-solid:database"},
        {"title": "Choose Based on Tools",
         "desc": "Pick ETL when your destination has limited compute, and ELT when you use a cloud warehouse like BigQuery, Snowflake, or Redshift that can handle heavy transforms.",
         "pills": ["Decision", "Compute", "Cost"],
         "icon": "fa6-solid:scale-balanced"},
    ],
},

"mod_01_data_engineering_foundations/lesson03_handling_large_datasets.html": {
    # Overview: Memory Limits, Chunking, Streaming, File Formats
    "cards": [
        {"title": "RAM Sets the Ceiling",
         "desc": "Your computer's RAM determines how much data you can load at once — a 16 GB laptop cannot open a 20 GB CSV without running out of memory.",
         "pills": ["RAM", "Limits", "Crash Risk"],
         "icon": "fa6-solid:memory"},
        {"title": "Process in Small Batches",
         "desc": "Reading a file in 100,000-row chunks lets you handle billions of rows on a normal laptop, just like reading a book one chapter at a time.",
         "pills": ["Chunks", "Iteration", "Efficiency"],
         "icon": "fa6-solid:layer-group"},
        {"title": "File Format Matters",
         "desc": "Switching from CSV to Parquet can shrink your file by 80% and speed up reads by 10×, because Parquet only loads the columns you actually need.",
         "pills": ["Parquet", "Compression", "Speed"],
         "icon": "fa6-solid:file-zipper"},
    ],
},

"mod_01_data_engineering_foundations/lesson05_parquet_efficient_storage.html": {
    # Overview: Columnar Layout, Compression, Selective Reads, Schema Metadata
    "cards": [
        {"title": "Read Only What You Need",
         "desc": "Parquet lets you load just two columns from a 200-column file, like opening only the tabs you need in a massive Excel workbook instead of the whole thing.",
         "pills": ["Column Pruning", "Speed", "I/O"],
         "icon": "fa6-solid:filter-circle-xmark"},
        {"title": "Compression Saves Storage",
         "desc": "A 10 GB CSV often shrinks to under 2 GB in Parquet format because similar values in a column compress much better than mixed rows.",
         "pills": ["Snappy", "Gzip", "Disk Space"],
         "icon": "fa6-solid:minimize"},
        {"title": "Schema Travels with Data",
         "desc": "Parquet files carry their column names and data types in the footer, so you never wonder whether a column is text or a number — the file tells you.",
         "pills": ["Metadata", "Types", "Self-Describing"],
         "icon": "fa6-solid:tags"},
    ],
},

"mod_01_data_engineering_foundations/lesson06_intro_to_polars_optional.html": {
    # Overview: Parallel Execution, Lazy Evaluation, Expressions, Zero-Copy Reads
    "cards": [
        {"title": "Speed Without Code Changes",
         "desc": "Polars runs the same filter-and-group operation up to 10× faster than pandas because it uses all your CPU cores automatically — no extra code needed.",
         "pills": ["Multi-Core", "Auto-Parallel", "Faster"],
         "icon": "fa6-solid:bolt"},
        {"title": "Lazy Plans Save Work",
         "desc": "In lazy mode, Polars builds a query plan first and removes unnecessary steps before running — like a GPS recalculating the shortest route before you drive.",
         "pills": ["Query Plan", "Optimiser", "Less I/O"],
         "icon": "fa6-solid:route"},
        {"title": "Familiar Syntax for Pandas Users",
         "desc": "Polars uses select, filter, and group_by methods that mirror pandas patterns, so switching feels like moving from Excel 2019 to Excel 365 — similar, just faster.",
         "pills": ["select()", "filter()", "group_by()"],
         "icon": "fa6-solid:repeat"},
    ],
},

"mod_01_data_engineering_foundations/lesson07_pipeline_design_concepts.html": {
    # Overview: Stages, Dependencies, Error Handling, Idempotency
    "cards": [
        {"title": "Rerunning Should Be Safe",
         "desc": "An idempotent pipeline produces the same result whether you run it once or five times — like pressing 'Save' repeatedly in Word without duplicating your text.",
         "pills": ["Idempotent", "Safe Retry", "Consistent"],
         "icon": "fa6-solid:rotate"},
        {"title": "Failures Must Not Spread",
         "desc": "Good pipelines isolate each stage so a failure in the 'transform' step does not corrupt data already loaded — the same way a blown fuse protects the rest of the house.",
         "pills": ["Isolation", "Rollback", "Containment"],
         "icon": "fa6-solid:shield-halved"},
        {"title": "Logging Tells the Story",
         "desc": "Every pipeline run should write a log with timestamps, row counts, and error details so you can diagnose problems without re-reading the entire codebase.",
         "pills": ["Timestamps", "Row Counts", "Debugging"],
         "icon": "fa6-solid:clipboard-list"},
    ],
},

# ═══════════════════════════════════════════════════════════
# MODULE 02 — NoSQL and Modern Data Storage
# ═══════════════════════════════════════════════════════════

"mod_02_nosql_and_modern_data_storage/lesson01_what_is_nosql.html": {
    # Overview: Flexible Schema, Horizontal Scaling, Data Models, Trade-offs
    "cards": [
        {"title": "Schema Freedom Speeds Development",
         "desc": "NoSQL lets you store a new field without altering a table — like adding a sticky note to a filing cabinet folder instead of redesigning the entire filing system.",
         "pills": ["No ALTER TABLE", "Dynamic", "Agile"],
         "icon": "fa6-solid:pen-ruler"},
        {"title": "Scale Out, Not Up",
         "desc": "NoSQL databases add more servers to handle growth, while SQL databases typically need a bigger single server — the difference between hiring more staff versus finding a stronger employee.",
         "pills": ["Horizontal", "Sharding", "Clusters"],
         "icon": "fa6-solid:server"},
        {"title": "Trade-offs Are Real",
         "desc": "NoSQL sacrifices strict joins and transactions for speed and flexibility, so it fits best when your queries are simple lookups rather than complex multi-table reports.",
         "pills": ["CAP Theorem", "Eventual", "Consistency"],
         "icon": "fa6-solid:triangle-exclamation"},
    ],
},

"mod_02_nosql_and_modern_data_storage/lesson02_types_of_nosql_databases.html": {
    # Overview: Document Stores, Key-Value Stores, Column-Family, Graph Databases
    "cards": [
        {"title": "Match Data to Model",
         "desc": "Picking the wrong NoSQL type is like using a spreadsheet when you need a diagram — each model excels at a specific data shape and access pattern.",
         "pills": ["Shape", "Access Pattern", "Fit"],
         "icon": "fa6-solid:puzzle-piece"},
        {"title": "Real Systems Mix Models",
         "desc": "A shopping site might use Redis for sessions, MongoDB for product catalogues, and Neo4j for recommendations — all in the same application.",
         "pills": ["Polyglot", "Hybrid", "Microservices"],
         "icon": "fa6-solid:cubes"},
        {"title": "Query Language Differs",
         "desc": "Unlike SQL's universal SELECT statement, each NoSQL type has its own query syntax — learning the model first helps you learn the syntax faster.",
         "pills": ["MQL", "CQL", "Cypher"],
         "icon": "fa6-solid:language"},
    ],
},

"mod_02_nosql_and_modern_data_storage/lesson03_document_databases_mongodb.html": {
    # Overview: Documents, Collections, Queries, Nested Data
    "cards": [
        {"title": "One Document, Complete Record",
         "desc": "MongoDB stores an order with its line items in a single document, so you fetch everything in one read — no joins needed, unlike a SQL database with three separate tables.",
         "pills": ["Embedded", "Single Read", "Denormalised"],
         "icon": "fa6-solid:file-lines"},
        {"title": "JSON Matches Python Dicts",
         "desc": "MongoDB documents look like Python dictionaries, so converting API responses to database records requires almost no transformation code.",
         "pills": ["dict()", "BSON", "Native Feel"],
         "icon": "fa6-solid:code"},
        {"title": "Indexes Unlock Speed",
         "desc": "Without an index, MongoDB scans every document — adding one on a frequently queried field is like adding a table of contents to a 500-page book.",
         "pills": ["Scan vs Seek", "create_index()", "Performance"],
         "icon": "fa6-solid:magnifying-glass-chart"},
    ],
},

"mod_02_nosql_and_modern_data_storage/lesson04_key_value_databases_redis.html": {
    # Overview: Keys, Values, In-Memory Speed, Expiry
    "cards": [
        {"title": "Microsecond Response Times",
         "desc": "Redis serves data from RAM, returning results in under 1 millisecond — roughly 100× faster than a typical SQL query that reads from disk.",
         "pills": ["Sub-ms", "In-Memory", "Low Latency"],
         "icon": "fa6-solid:gauge-high"},
        {"title": "Caching Reduces Database Load",
         "desc": "Storing a frequent SQL query result in Redis means your database handles the heavy query once, then Redis serves the cached answer to every subsequent request.",
         "pills": ["Cache Layer", "Read-Heavy", "Offload"],
         "icon": "fa6-solid:clone"},
        {"title": "Expiry Keeps Data Fresh",
         "desc": "You set a time-to-live on each key so stale data deletes itself automatically — like a self-clearing whiteboard that erases every 5 minutes.",
         "pills": ["TTL", "Auto-Delete", "Freshness"],
         "icon": "fa6-solid:clock-rotate-left"},
    ],
},

"mod_02_nosql_and_modern_data_storage/lesson05_column_family_databases_cassandra.html": {
    # Overview: Partitions, Replication, Wide Rows, Write Speed
    "cards": [
        {"title": "Writes at Any Scale",
         "desc": "Cassandra writes data to the nearest node without waiting for a central coordinator, so it handles millions of inserts per second across a cluster.",
         "pills": ["Distributed", "No Bottleneck", "Append-Only"],
         "icon": "fa6-solid:pen-to-square"},
        {"title": "Design Queries First",
         "desc": "In Cassandra you model your tables around the queries you will run — the opposite of SQL, where you normalise first and query later.",
         "pills": ["Query-Driven", "Denormalise", "Partition Key"],
         "icon": "fa6-solid:compass-drafting"},
        {"title": "Replication Guards Data",
         "desc": "Every row is copied across multiple nodes automatically, so losing one server does not lose any data — like saving a file to three separate USB drives at once.",
         "pills": ["Replication Factor", "Fault Tolerant", "Multi-DC"],
         "icon": "fa6-solid:copy"},
    ],
},

"mod_02_nosql_and_modern_data_storage/lesson06_graph_databases_neo4j.html": {
    # Overview: Nodes, Relationships, Traversals, Properties
    "cards": [
        {"title": "Connections Are First-Class",
         "desc": "In a graph database, a relationship between two records is stored directly — not computed with a slow JOIN like in SQL tables.",
         "pills": ["Direct Link", "No JOIN", "O(1) Lookup"],
         "icon": "fa6-solid:circle-nodes"},
        {"title": "Cypher Reads Like English",
         "desc": "A Neo4j query like MATCH (a)-[:KNOWS]->(b) reads almost like a sentence: 'find person a who knows person b.'",
         "pills": ["Cypher", "Pattern Match", "Readable"],
         "icon": "fa6-solid:spell-check"},
        {"title": "Real Value in Deep Links",
         "desc": "Graph databases shine when you need to traverse many levels — friend-of-a-friend, supply chain hops, or fraud rings — where SQL would need dozens of self-joins.",
         "pills": ["Traversal", "Multi-Hop", "Fraud Detection"],
         "icon": "fa6-solid:diagram-project"},
    ],
},

"mod_02_nosql_and_modern_data_storage/lesson07_sql_vs_nosql_choosing_the_right_database.html": {
    # Overview: Data Shape, Query Patterns, Scale Needs, Consistency vs Speed
    "cards": [
        {"title": "Start With Your Questions",
         "desc": "The best database choice depends on what you will query most — frequent joins favour SQL, while simple key lookups favour NoSQL.",
         "pills": ["Query First", "Access Pattern", "Design"],
         "icon": "fa6-solid:magnifying-glass"},
        {"title": "Consistency Has a Cost",
         "desc": "SQL guarantees every read sees the latest write, but that coordination slows down distributed systems — NoSQL relaxes this to gain speed at massive scale.",
         "pills": ["ACID", "BASE", "Latency"],
         "icon": "fa6-solid:scale-unbalanced"},
        {"title": "Most Teams Use Both",
         "desc": "A common architecture uses PostgreSQL for transactions and MongoDB or Redis for caching and flexible data — choosing one does not mean rejecting the other.",
         "pills": ["Polyglot", "Hybrid Stack", "Best Fit"],
         "icon": "fa6-solid:arrows-split-up-and-left"},
    ],
},

# ═══════════════════════════════════════════════════════════
# MODULE 03 — API Data Integration
# ═══════════════════════════════════════════════════════════

"mod_03_api_data_integration/lesson01_what_is_an_api.html": {
    # Overview: Request, Response, Endpoint, Data Format
    "cards": [
        {"title": "APIs Connect Separate Systems",
         "desc": "An API lets your Python script pull live data from a remote server — the same way a cashier sends your order to the kitchen without you walking back there yourself.",
         "pills": ["Integration", "Remote Data", "Automation"],
         "icon": "fa6-solid:plug"},
        {"title": "Endpoints Are Addresses",
         "desc": "Each endpoint is a specific URL that returns a specific type of data, like different counters at a post office — one for parcels, one for stamps, one for tracking.",
         "pills": ["URL Path", "Resource", "Route"],
         "icon": "fa6-solid:location-dot"},
        {"title": "JSON Is the Common Language",
         "desc": "Most APIs send data back as JSON, a format that maps directly to Python dictionaries and lists — no manual file parsing required.",
         "pills": ["Key-Value", "Nested", "Lightweight"],
         "icon": "fa6-solid:file-code"},
    ],
},

"mod_03_api_data_integration/lesson02_understanding_http_requests.html": {
    # Overview: GET, POST, Status Codes, Headers
    "cards": [
        {"title": "GET Reads, POST Writes",
         "desc": "GET retrieves data without changing anything on the server, while POST sends new data — like the difference between reading a website and submitting a form.",
         "pills": ["Safe Read", "Create", "Idempotent"],
         "icon": "fa6-solid:arrow-right-arrow-left"},
        {"title": "Status Codes Tell Outcomes",
         "desc": "A 200 means success, a 404 means 'not found', and a 500 means the server broke — learning these three covers 90% of the errors you will encounter.",
         "pills": ["200 OK", "404 Not Found", "500 Error"],
         "icon": "fa6-solid:traffic-light"},
        {"title": "Headers Carry Metadata",
         "desc": "HTTP headers attach extra information to every request, like the return address on an envelope — they tell the server your content type, language, and authentication details.",
         "pills": ["Content-Type", "Authorization", "Accept"],
         "icon": "fa6-solid:envelope-open-text"},
    ],
},

"mod_03_api_data_integration/lesson03_using_the_python_requests_library.html": {
    # Overview: Installing, GET Requests, Response Object, Error Handling
    "cards": [
        {"title": "One Line Fetches Data",
         "desc": "With requests.get(url) you retrieve live data from any public API in a single line of Python — no sockets, no manual HTTP formatting.",
         "pills": ["requests.get()", "Simple", "One-liner"],
         "icon": "fa6-solid:download"},
        {"title": "Response Objects Are Rich",
         "desc": "The response carries status code, headers, and body all in one object, so you can check success with .status_code and parse JSON with .json() immediately.",
         "pills": [".status_code", ".json()", ".text"],
         "icon": "fa6-solid:box-open"},
        {"title": "Always Check for Errors",
         "desc": "Calling raise_for_status() after every request stops your script immediately on failure instead of silently processing garbage data downstream.",
         "pills": ["raise_for_status()", "try/except", "Fail Fast"],
         "icon": "fa6-solid:shield-halved"},
    ],
},

"mod_03_api_data_integration/lesson04_working_with_json_data.html": {
    # Overview: Key-Value Pairs, Nested Objects, Arrays, Parsing
    "cards": [
        {"title": "JSON Maps to Python Types",
         "desc": "A JSON object becomes a Python dict, a JSON array becomes a list, and strings and numbers stay the same — no custom parser needed.",
         "pills": ["dict", "list", "Auto-Convert"],
         "icon": "fa6-solid:right-left"},
        {"title": "Nesting Means Drilling Down",
         "desc": "Accessing data['user']['address']['city'] is like opening folder after folder on your desktop — each key takes you one level deeper into the structure.",
         "pills": ["Bracket Access", "Levels", "Path"],
         "icon": "fa6-solid:sitemap"},
        {"title": "Handle Missing Keys Safely",
         "desc": "Using dict.get('key', default) returns a fallback value instead of crashing your script — essential when API responses sometimes omit optional fields.",
         "pills": [".get()", "Default Value", "KeyError"],
         "icon": "fa6-solid:life-ring"},
    ],
},

"mod_03_api_data_integration/lesson05_parsing_api_responses.html": {
    # Overview: Status Check, Navigating Keys, Extracting Fields, Handling Missing Data
    "cards": [
        {"title": "Validate Before You Parse",
         "desc": "Always confirm the status code is 200 before reading the body — parsing a 404 error page as if it were valid data produces silent, hard-to-find bugs.",
         "pills": ["Status First", "Guard Clause", "200 OK"],
         "icon": "fa6-solid:clipboard-check"},
        {"title": "Flatten Nested Responses",
         "desc": "API data often nests three or four levels deep; extracting the fields you need into a flat dictionary makes the data ready for a pandas DataFrame or a CSV export.",
         "pills": ["Flatten", "dict Comp", "DataFrame"],
         "icon": "fa6-solid:table-cells"},
        {"title": "Log What You Discard",
         "desc": "When you skip a record because a required field is missing, log the record ID so you can investigate later instead of wondering why your final count is too low.",
         "pills": ["Logging", "Audit Trail", "Data Loss"],
         "icon": "fa6-solid:pen-to-square"},
    ],
},

"mod_03_api_data_integration/lesson06_authentication_with_api_keys.html": {
    # Overview: API Key, Headers vs Params, Permissions, Secret Management
    "cards": [
        {"title": "Keys Prove Your Identity",
         "desc": "An API key works like a library card — the server checks it to confirm who you are and what data you are allowed to access before returning any results.",
         "pills": ["Identity", "Access", "Verification"],
         "icon": "fa6-solid:key"},
        {"title": "Headers Beat Query Strings",
         "desc": "Sending your key in an HTTP header keeps it out of URLs and server logs, reducing the risk of accidental exposure — the same reason you whisper a password instead of shouting it.",
         "pills": ["Authorization", "Hidden", "Secure"],
         "icon": "fa6-solid:lock"},
        {"title": "Never Hard-Code Secrets",
         "desc": "Store API keys in environment variables or a .env file so they stay out of your Git history — a leaked key can cost real money if the API charges per call.",
         "pills": [".env File", "os.environ", "Git Safety"],
         "icon": "fa6-solid:vault"},
    ],
},

"mod_03_api_data_integration/lesson07_oauth_authentication.html": {
    # Overview: Access Token, Scopes, Refresh Token, OAuth Flow
    "cards": [
        {"title": "Tokens Replace Passwords",
         "desc": "OAuth gives your script a temporary token instead of your actual password, so the API never sees your credentials — like a hotel key card that expires at checkout.",
         "pills": ["Temporary", "Revocable", "Delegated"],
         "icon": "fa6-solid:ticket"},
        {"title": "Scopes Limit Access",
         "desc": "When you request a token, you list exactly what permissions you need — read-only, read-write, or admin — so a script cannot do more than intended.",
         "pills": ["read", "write", "Least Privilege"],
         "icon": "fa6-solid:sliders"},
        {"title": "Refresh Tokens Avoid Re-Login",
         "desc": "A refresh token lets your script get a new access token silently when the old one expires, without prompting the user to log in again.",
         "pills": ["Auto-Renew", "Expiry", "Seamless"],
         "icon": "fa6-solid:arrows-rotate"},
    ],
},

"mod_03_api_data_integration/lesson08_handling_pagination_in_apis.html": {
    # Overview: Page Size, Offset, Cursor-Based, Loop Pattern
    "cards": [
        {"title": "APIs Limit Result Size",
         "desc": "Most APIs cap each response at 20–100 records to protect server resources, so fetching 10,000 records requires many sequential requests.",
         "pills": ["Page Limit", "Batches", "Protection"],
         "icon": "fa6-solid:book-open"},
        {"title": "Cursors Beat Offsets",
         "desc": "Cursor-based pagination uses a bookmark token instead of a page number, which stays accurate even when new records are inserted mid-fetch.",
         "pills": ["Cursor Token", "Stable", "No Drift"],
         "icon": "fa6-solid:bookmark"},
        {"title": "Loop Until Empty",
         "desc": "The standard pattern is a while loop that requests the next page, appends results, and stops when the API returns an empty list or no next-page link.",
         "pills": ["while Loop", "Append", "Break"],
         "icon": "fa6-solid:repeat"},
    ],
},

"mod_03_api_data_integration/lesson09_handling_api_rate_limits.html": {
    # Overview: Rate Headers, Retry-After, Backoff, Throttling
    "cards": [
        {"title": "Respect the Server's Rules",
         "desc": "Rate limits exist to prevent one client from overloading a shared API — exceeding them gets your key temporarily blocked or permanently banned.",
         "pills": ["429 Status", "Ban Risk", "Fair Use"],
         "icon": "fa6-solid:hand"},
        {"title": "Backoff Retries Gracefully",
         "desc": "Exponential backoff doubles the wait time after each failure (1s, 2s, 4s, 8s), giving the server time to recover without hammering it with retries.",
         "pills": ["Exponential", "Wait", "Recover"],
         "icon": "fa6-solid:hourglass-half"},
        {"title": "Read Rate-Limit Headers",
         "desc": "Headers like X-RateLimit-Remaining and Retry-After tell you exactly how many calls you have left and when you can resume — always check them before retrying.",
         "pills": ["Remaining", "Retry-After", "Headers"],
         "icon": "fa6-solid:glasses"},
    ],
},

"mod_03_api_data_integration/lesson10_loading_api_data_into_pandas.html": {
    # Overview: json_normalize, Column Mapping, Type Conversion, Append Pattern
    "cards": [
        {"title": "Normalise Nested JSON",
         "desc": "pd.json_normalize() flattens deeply nested API responses into a flat DataFrame with one column per field — like converting a tree of folders into a single spreadsheet.",
         "pills": ["json_normalize()", "Flatten", "One-Step"],
         "icon": "fa6-solid:table-cells-large"},
        {"title": "Fix Types Early",
         "desc": "API dates arrive as strings and counts as floats; converting them with pd.to_datetime() and .astype(int) right after loading prevents subtle calculation errors later.",
         "pills": ["to_datetime()", "astype()", "Clean Types"],
         "icon": "fa6-solid:wrench"},
        {"title": "Append Pages Efficiently",
         "desc": "Collect each page's DataFrame in a list, then call pd.concat() once at the end — this is 50× faster than appending rows one at a time in a loop.",
         "pills": ["List + concat()", "No append()", "Batch"],
         "icon": "fa6-solid:layer-group"},
    ],
},

"mod_03_api_data_integration/lesson11_saving_api_data_to_databases.html": {
    # Overview: Connection String, Table Mapping, Insert Modes, Upsert
    "cards": [
        {"title": "DataFrames Write to SQL",
         "desc": "Calling df.to_sql('table', engine) pushes your entire DataFrame into a database table in one step — no row-by-row INSERT loop required.",
         "pills": ["to_sql()", "SQLAlchemy", "Bulk"],
         "icon": "fa6-solid:database"},
        {"title": "Upsert Prevents Duplicates",
         "desc": "An upsert inserts new rows and updates existing ones in a single operation, so re-running your pipeline does not create duplicate records.",
         "pills": ["INSERT OR UPDATE", "Idempotent", "Safe"],
         "icon": "fa6-solid:code-merge"},
        {"title": "Transactions Protect Integrity",
         "desc": "Wrapping your writes in a transaction means either all rows commit or none do — a half-loaded table is worse than no load at all.",
         "pills": ["BEGIN/COMMIT", "Rollback", "Atomic"],
         "icon": "fa6-solid:shield-halved"},
    ],
},

"mod_03_api_data_integration/lesson12_building_an_api_data_pipeline.html": {
    # Overview: Extract, Transform, Load, Orchestration
    "cards": [
        {"title": "Separate Each Stage",
         "desc": "Putting extract, transform, and load into separate functions lets you test and debug each stage independently — like checking each ingredient before cooking the dish.",
         "pills": ["Functions", "Testable", "Modular"],
         "icon": "fa6-solid:cubes"},
        {"title": "Config Drives Behaviour",
         "desc": "Storing API URLs, page sizes, and table names in a config file means you can change sources without editing pipeline code — one file, many data feeds.",
         "pills": ["Config File", "No Hard-Code", "Reusable"],
         "icon": "fa6-solid:gears"},
        {"title": "Logs Prove Success",
         "desc": "Your pipeline should log start time, row counts per stage, and end status so you can answer 'Did it run?' and 'How many rows?' without opening the database.",
         "pills": ["Timestamps", "Row Counts", "Status"],
         "icon": "fa6-solid:clipboard-list"},
    ],
},

"mod_03_api_data_integration/lesson13_real_world_api_integration_project.html": {
    # Overview: Planning, Data Extraction, Data Processing, Delivery
    "cards": [
        {"title": "Plan Before You Code",
         "desc": "Mapping out which endpoints to call, what fields to keep, and where to store results saves hours of rework — like drawing a blueprint before laying bricks.",
         "pills": ["Requirements", "Data Map", "Blueprint"],
         "icon": "fa6-solid:pen-ruler"},
        {"title": "Handle Edge Cases Early",
         "desc": "Real APIs return empty pages, missing fields, and unexpected formats — building checks for these from day one prevents your pipeline from failing silently at 2 AM.",
         "pills": ["Nulls", "Empty Pages", "Validation"],
         "icon": "fa6-solid:bug"},
        {"title": "Deliver to Stakeholders",
         "desc": "The final step is not just loading a database — it is confirming the data is correct, documented, and accessible to the analysts who will build reports from it.",
         "pills": ["Documentation", "Access", "Quality"],
         "icon": "fa6-solid:people-arrows"},
    ],
},

"mod_03_api_data_integration/lesson14_api_best_practices.html": {
    # Overview: Timeouts, Logging, Secrets Management, Idempotency
    "cards": [
        {"title": "Set Timeouts on Every Call",
         "desc": "A request without a timeout can hang forever if the server stops responding, blocking your entire pipeline — always pass timeout=30 as a safety net.",
         "pills": ["timeout=30", "Hang Prevention", "Reliability"],
         "icon": "fa6-solid:stopwatch"},
        {"title": "Retry With Limits",
         "desc": "Retrying a failed request three times with exponential backoff recovers from temporary blips without flooding a struggling server with an infinite loop of retries.",
         "pills": ["max_retries", "Backoff", "Circuit Breaker"],
         "icon": "fa6-solid:rotate-right"},
        {"title": "Version-Pin Your Dependencies",
         "desc": "Locking your requests library version in requirements.txt ensures your pipeline behaves the same way tomorrow as it does today — no surprise breaking changes.",
         "pills": ["requirements.txt", "Pin Version", "Reproducible"],
         "icon": "fa6-solid:thumbtack"},
    ],
},

# ═══════════════════════════════════════════════════════════
# MODULE 04 — Data Pipelines and Orchestration
# ═══════════════════════════════════════════════════════════

"mod_04_data_pipelines_and_orchestration/lesson01_what_is_a_data_pipeline.html": {
    # Overview: Source, Steps, Destination, Automation
    "cards": [
        {"title": "Pipelines Eliminate Manual Work",
         "desc": "A data pipeline replaces the repetitive copy-paste-clean cycle you do in Excel every Monday morning with code that runs itself on a schedule.",
         "pills": ["Automate", "Schedule", "Hands-Free"],
         "icon": "fa6-solid:robot"},
        {"title": "Steps Run in Order",
         "desc": "Each pipeline stage depends on the previous one — extract finishes before transform starts, and transform completes before load begins — like an assembly line.",
         "pills": ["Sequential", "Dependencies", "Flow"],
         "icon": "fa6-solid:arrow-down-1-9"},
        {"title": "Destinations Vary by Need",
         "desc": "The same pipeline can load data into a database for analysts, a CSV for auditors, and a dashboard for managers — one extraction, many outputs.",
         "pills": ["Database", "CSV", "Dashboard"],
         "icon": "fa6-solid:arrows-split-up-and-left"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson02_etl_vs_elt.html": {
    # Overview: ETL Flow, ELT Flow, When to Choose, Hybrid Approach
    "cards": [
        {"title": "ETL Suits Limited Targets",
         "desc": "When your destination is a small database or a flat file with no compute power, transforming data before loading keeps the target lean and ready to query.",
         "pills": ["Small Target", "Pre-Clean", "Low Compute"],
         "icon": "fa6-solid:filter"},
        {"title": "ELT Leverages Cloud Power",
         "desc": "Cloud warehouses like BigQuery charge only for queries, so loading raw data first and transforming with SQL is both cheaper and more flexible than pre-processing outside.",
         "pills": ["Cloud SQL", "Pay-per-Query", "Flexible"],
         "icon": "fa6-solid:cloud"},
        {"title": "Hybrid Pipelines Are Common",
         "desc": "Many teams clean obvious junk before loading (ETL-style), then run complex aggregations inside the warehouse (ELT-style) — combining the best of both approaches.",
         "pills": ["Pre-filter", "In-Warehouse", "Practical"],
         "icon": "fa6-solid:code-merge"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson03_pipeline_design_patterns.html": {
    # Overview: Linear Pipeline, Fan-Out / Fan-In, Delta (Incremental), Retry / Dead-Letter
    "cards": [
        {"title": "Patterns Solve Recurring Problems",
         "desc": "Design patterns are proven blueprints — choosing the right one for your data flow saves weeks of trial and error, like using a tested recipe instead of improvising.",
         "pills": ["Blueprint", "Reusable", "Proven"],
         "icon": "fa6-solid:shapes"},
        {"title": "Incremental Beats Full Reload",
         "desc": "Processing only the rows that changed since the last run (delta pattern) can reduce runtime from hours to minutes on large datasets.",
         "pills": ["Delta", "Changed Rows", "Fast"],
         "icon": "fa6-solid:forward"},
        {"title": "Dead Letters Capture Failures",
         "desc": "A dead-letter queue stores records that failed processing so you can inspect and re-process them later without losing data or blocking the rest of the pipeline.",
         "pills": ["Queue", "Inspect", "Recover"],
         "icon": "fa6-solid:inbox"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson04_working_with_large_data_files.html": {
    # Overview: Chunked Reading, Generators, File Formats, Progress Tracking
    "cards": [
        {"title": "Generators Save Memory",
         "desc": "A Python generator yields one chunk at a time instead of loading the entire file into RAM — like reading a book one page at a time instead of photocopying all 500 pages first.",
         "pills": ["yield", "Lazy", "Low RAM"],
         "icon": "fa6-solid:memory"},
        {"title": "Progress Bars Build Confidence",
         "desc": "Adding tqdm to your chunk loop shows a live progress bar so you know the job is running and can estimate when it will finish — no more staring at a blank terminal.",
         "pills": ["tqdm", "ETA", "Visibility"],
         "icon": "fa6-solid:bars-progress"},
        {"title": "Binary Formats Beat CSV",
         "desc": "Switching large files from CSV to Parquet or Feather cuts read time dramatically because binary formats skip the overhead of parsing every comma and newline.",
         "pills": ["Parquet", "Feather", "Binary"],
         "icon": "fa6-solid:bolt"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson05_data_validation_in_pipelines.html": {
    # Overview: Schema Checks, Value Rules, Null Detection, Quarantine
    "cards": [
        {"title": "Catch Errors Before Loading",
         "desc": "Validating data before it enters your database is like spell-checking an email before sending — fixing errors at the source is far cheaper than correcting them after delivery.",
         "pills": ["Pre-Load", "Early Check", "Prevention"],
         "icon": "fa6-solid:clipboard-check"},
        {"title": "Quarantine Bad Records",
         "desc": "Routing invalid rows to a separate 'quarantine' table lets the pipeline continue processing good data while preserving bad rows for investigation later.",
         "pills": ["Quarantine", "Continue", "Investigate"],
         "icon": "fa6-solid:box-archive"},
        {"title": "Assertions Document Rules",
         "desc": "Writing assert statements like 'no nulls in email column' turns your business rules into executable checks that fail loudly instead of silently passing dirty data.",
         "pills": ["assert", "Business Rules", "Fail Loud"],
         "icon": "fa6-solid:list-check"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson09_scheduling_pipelines.html": {
    # Overview: Cron Expressions, Intervals, Triggers, Monitoring
    "cards": [
        {"title": "Cron Handles Recurring Jobs",
         "desc": "A cron expression like 0 6 * * * means 'run at 6 AM every day' — five fields (minute, hour, day, month, weekday) control the entire schedule.",
         "pills": ["5 Fields", "Daily", "Weekly"],
         "icon": "fa6-solid:calendar-days"},
        {"title": "Triggers React to Events",
         "desc": "Event-based triggers start a pipeline when a new file arrives or a database row changes, so data flows in near-real-time instead of waiting for the next scheduled run.",
         "pills": ["File Arrival", "Webhook", "Real-Time"],
         "icon": "fa6-solid:bell"},
        {"title": "Alerts Catch Silent Failures",
         "desc": "A scheduled job that fails at 3 AM is invisible until someone notices stale dashboards — email or Slack alerts notify you within minutes of a failure.",
         "pills": ["Email Alert", "Slack", "On-Failure"],
         "icon": "fa6-solid:triangle-exclamation"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson10_building_a_simple_python_pipeline.html": {
    # Overview: Extract Function, Transform Function, Load Function, Main Runner
    "cards": [
        {"title": "Functions Are Pipeline Stages",
         "desc": "Wrapping each stage in its own function — extract(), transform(), load() — lets you call, test, and replace any stage without touching the others.",
         "pills": ["extract()", "transform()", "load()"],
         "icon": "fa6-solid:cubes"},
        {"title": "Main Orchestrates the Flow",
         "desc": "A simple if __name__ == '__main__' block calls each function in order and passes the output of one stage as the input to the next — your first pipeline in under 30 lines.",
         "pills": ["__main__", "Chain", "30 Lines"],
         "icon": "fa6-solid:play"},
        {"title": "Return Values Connect Stages",
         "desc": "Each function returns a DataFrame that the next function receives as input, creating a clean data handoff — no global variables, no side effects.",
         "pills": ["Return df", "Input/Output", "Clean"],
         "icon": "fa6-solid:right-left"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson11_pipeline_project_automating_data_ingestion.html": {
    # Overview: Source Config, Incremental Fetch, Error Recovery, Scheduling
    "cards": [
        {"title": "Config Files Define Sources",
         "desc": "Storing file paths, URLs, and credentials in a YAML or JSON config means adding a new data source is a one-line edit, not a code change.",
         "pills": ["YAML", "JSON Config", "One Edit"],
         "icon": "fa6-solid:file-pen"},
        {"title": "Incremental Fetch Saves Time",
         "desc": "Tracking the last-processed timestamp lets your pipeline fetch only new rows each run, cutting a 2-hour full reload down to a 5-minute incremental update.",
         "pills": ["Watermark", "New Rows Only", "Fast"],
         "icon": "fa6-solid:forward-fast"},
        {"title": "Recovery Means Restart Safety",
         "desc": "If a pipeline fails mid-run, writing checkpoints after each batch lets you restart from where it stopped instead of re-processing everything from scratch.",
         "pills": ["Checkpoint", "Resume", "No Reprocess"],
         "icon": "fa6-solid:rotate"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson12_pipeline_project_data_quality_checks.html": {
    # Overview: Completeness, Consistency, Range Checks, Alerting
    "cards": [
        {"title": "Measure Completeness First",
         "desc": "Counting null values per column as a percentage tells you instantly whether a data source started sending blanks — like checking if every cell in your spreadsheet has a value.",
         "pills": ["Null %", "Row Count", "Coverage"],
         "icon": "fa6-solid:chart-pie"},
        {"title": "Cross-Check with Source",
         "desc": "Comparing your loaded row count against the source system's count catches missing or duplicated records that would otherwise pollute your reports.",
         "pills": ["Source Count", "Loaded Count", "Match"],
         "icon": "fa6-solid:code-compare"},
        {"title": "Alert on Threshold Breaches",
         "desc": "Setting a rule like 'fail if null rate exceeds 5%' turns a quality check into an automatic gate that blocks bad data before it reaches analysts.",
         "pills": ["Threshold", "Auto-Block", "Gate"],
         "icon": "fa6-solid:bell"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson13_pipeline_project_database_loading.html": {
    # Overview: Bulk Insert, Upsert Logic, Transaction Safety, Post-Load Checks
    "cards": [
        {"title": "Bulk Inserts Are Faster",
         "desc": "Inserting 100,000 rows in one executemany() call is roughly 50× faster than looping with individual INSERT statements — fewer round trips to the database.",
         "pills": ["executemany()", "Batch", "Round Trips"],
         "icon": "fa6-solid:forward"},
        {"title": "Upsert Keeps Data Current",
         "desc": "An upsert updates existing rows and inserts new ones in a single pass, so re-running your pipeline refreshes data without creating duplicates.",
         "pills": ["ON CONFLICT", "Merge", "Idempotent"],
         "icon": "fa6-solid:arrows-rotate"},
        {"title": "Verify After Every Load",
         "desc": "Running a SELECT COUNT(*) after loading confirms the expected number of rows arrived — a two-second check that catches truncated loads before anyone notices.",
         "pills": ["COUNT(*)", "Post-Check", "Trust"],
         "icon": "fa6-solid:magnifying-glass-chart"},
    ],
},

"mod_04_data_pipelines_and_orchestration/lesson14_production_pipeline_architecture.html": {
    # Overview: Modular Design, Monitoring, Retry & Recovery, Scaling
    "cards": [
        {"title": "Modules Enable Team Work",
         "desc": "Breaking a pipeline into independently deployable modules lets one engineer fix the transform stage while another upgrades the extract stage — no merge conflicts.",
         "pills": ["Independent", "Parallel Dev", "Deploy"],
         "icon": "fa6-solid:puzzle-piece"},
        {"title": "Monitoring Is Not Optional",
         "desc": "A production pipeline without dashboards and alerts is like driving at night with your headlights off — you will not see failures until you crash into them.",
         "pills": ["Dashboards", "Metrics", "Alerts"],
         "icon": "fa6-solid:chart-line"},
        {"title": "Plan for 10× Growth",
         "desc": "Design your pipeline assuming data volume will grow tenfold in a year — adding partitioning, parallel workers, and queue-based ingestion now avoids an emergency rewrite later.",
         "pills": ["Partitioning", "Workers", "Queues"],
         "icon": "fa6-solid:chart-simple"},
    ],
},

# ═══════════════════════════════════════════════════════════
# MODULE 05 — Large Scale Data Processing
# ═══════════════════════════════════════════════════════════

"mod_05_large_scale_data_processing/lesson02_memory_optimization.html": {
    # Overview: Data Types, Categoricals, Column Pruning, In-Place Operations
    "cards": [
        {"title": "Downcast Numbers to Save RAM",
         "desc": "Changing a column from int64 to int32 halves its memory — like replacing a double-wide filing cabinet with a single-wide one that holds the same documents.",
         "pills": ["int64→int32", "pd.to_numeric()", "Half RAM"],
         "icon": "fa6-solid:compress"},
        {"title": "Categoricals Crush Strings",
         "desc": "Converting a 'country' column with 50 unique values from object to category can reduce memory by 95% because pandas stores each value once instead of repeating it.",
         "pills": [".astype('category')", "95% Less", "Lookup Table"],
         "icon": "fa6-solid:tags"},
        {"title": "Drop Columns You Don't Need",
         "desc": "Loading only the 5 columns you need from a 200-column file with usecols prevents 195 columns of wasted RAM — the simplest optimisation and often the most effective.",
         "pills": ["usecols", "Select Early", "Free RAM"],
         "icon": "fa6-solid:scissors"},
    ],
},

"mod_05_large_scale_data_processing/lesson03_chunk_processing.html": {
    # Overview: Chunk Size, Iterator, Accumulator, Memory Profile
    "cards": [
        {"title": "Chunks Keep RAM Constant",
         "desc": "Processing a 50 GB file in 100 MB chunks uses the same ~100 MB of RAM throughout — your laptop never sees the full file size.",
         "pills": ["Flat RAM", "chunksize=", "Scalable"],
         "icon": "fa6-solid:equals"},
        {"title": "Accumulate Results Gradually",
         "desc": "Appending each chunk's summary (counts, sums) to a small results list and concatenating once at the end avoids the overhead of growing a DataFrame in every iteration.",
         "pills": ["List Append", "One concat()", "Efficient"],
         "icon": "fa6-solid:plus"},
        {"title": "Profile to Pick Chunk Size",
         "desc": "Testing chunk sizes of 10k, 50k, and 100k rows with memory_profiler shows you the sweet spot — too small wastes I/O overhead, too large risks memory spikes.",
         "pills": ["memory_profiler", "Benchmark", "Sweet Spot"],
         "icon": "fa6-solid:gauge-simple-high"},
    ],
},

"mod_05_large_scale_data_processing/lesson04_processing_millions_of_rows.html": {
    # Overview: Vectorisation, Avoiding Loops, Indexing, Benchmarking
    "cards": [
        {"title": "Vectorised Operations Win",
         "desc": "A single df['total'] = df['price'] * df['qty'] processes a million rows thousands of times faster than a Python for-loop doing the same multiplication row by row.",
         "pills": ["No for-loop", "NumPy Core", "Bulk Math"],
         "icon": "fa6-solid:bolt"},
        {"title": "Measure Before Optimising",
         "desc": "Running %%timeit on your code shows exactly how many milliseconds each approach takes, so you optimise the slowest part first instead of guessing.",
         "pills": ["%%timeit", "Baseline", "Compare"],
         "icon": "fa6-solid:stopwatch"},
        {"title": "Indexes Speed Up Lookups",
         "desc": "Setting a frequently filtered column as the DataFrame index lets pandas use a hash lookup instead of scanning every row — the difference between a dictionary and a list search.",
         "pills": ["set_index()", "Hash Lookup", "O(1)"],
         "icon": "fa6-solid:magnifying-glass"},
    ],
},

"mod_05_large_scale_data_processing/lesson05_columnar_storage.html": {
    # Overview: Column Groups, Read Efficiency, Compression Ratio, Write Trade-off
    "cards": [
        {"title": "Columns Compress Better",
         "desc": "Values in the same column share a data type and often repeat, so compressing them together yields 5–10× smaller files than row-based formats like CSV.",
         "pills": ["Same Type", "Repetition", "5–10×"],
         "icon": "fa6-solid:minimize"},
        {"title": "Analytics Reads Fewer Bytes",
         "desc": "A query on 3 columns of a 200-column table reads only those 3 columns from disk — row storage would read all 200 columns and discard 197.",
         "pills": ["Column Pruning", "Less I/O", "Faster"],
         "icon": "fa6-solid:filter-circle-xmark"},
        {"title": "Writes Are Slower by Design",
         "desc": "Columnar storage splits each row across multiple column groups when writing, which is slower — but since analytics workflows read far more than they write, the trade-off pays off.",
         "pills": ["Write Penalty", "Read Benefit", "Analytics Fit"],
         "icon": "fa6-solid:scale-balanced"},
    ],
},

"mod_05_large_scale_data_processing/lesson06_parquet_files.html": {
    # Overview: Row Groups, Column Chunks, Footer Metadata, Predicate Pushdown
    "cards": [
        {"title": "Row Groups Enable Parallelism",
         "desc": "Parquet splits data into row groups of ~128 MB each, so multiple CPU cores can read and process different groups at the same time.",
         "pills": ["128 MB", "Parallel Read", "CPU Cores"],
         "icon": "fa6-solid:layer-group"},
        {"title": "Pushdown Skips Irrelevant Data",
         "desc": "Predicate pushdown reads the footer's min/max statistics and skips entire row groups that cannot contain matching rows — no decompression wasted.",
         "pills": ["Min/Max", "Skip Groups", "Zero Waste"],
         "icon": "fa6-solid:forward"},
        {"title": "Ecosystem Support Is Wide",
         "desc": "Pandas, Polars, Spark, DuckDB, and PyArrow all read Parquet natively, making it the universal exchange format for analytics pipelines.",
         "pills": ["pandas", "Polars", "Spark"],
         "icon": "fa6-solid:handshake"},
    ],
},

"mod_05_large_scale_data_processing/lesson07_pyarrow_basics.html": {
    # Overview: Tables, Schemas, File I/O, Interop
    "cards": [
        {"title": "Arrow Is the Memory Standard",
         "desc": "Apache Arrow defines a columnar memory format that tools like pandas, Polars, and Spark all share — data moves between them with zero copying.",
         "pills": ["Zero-Copy", "Standard", "Shared RAM"],
         "icon": "fa6-solid:memory"},
        {"title": "Schemas Enforce Structure",
         "desc": "A PyArrow schema declares each column's name and type up front, catching data-type mismatches the moment you load a file instead of after a failed calculation.",
         "pills": ["pa.schema()", "Type Check", "Early Fail"],
         "icon": "fa6-solid:shield-halved"},
        {"title": "Arrow Bridges Every Tool",
         "desc": "Converting from a PyArrow table to a pandas DataFrame with .to_pandas() or to Polars with pl.from_arrow() takes milliseconds because the underlying memory is already compatible.",
         "pills": [".to_pandas()", "pl.from_arrow()", "Instant"],
         "icon": "fa6-solid:bridge"},
    ],
},

"mod_05_large_scale_data_processing/lesson08_introduction_to_polars.html": {
    # Overview: DataFrame API, Lazy Mode, Multi-Threading, Memory Efficiency
    "cards": [
        {"title": "Polars Replaces Slow Loops",
         "desc": "Where pandas often falls back to Python-speed loops, Polars runs every operation in compiled Rust across all CPU cores — no extra configuration needed.",
         "pills": ["Rust Engine", "All Cores", "No Config"],
         "icon": "fa6-solid:rocket"},
        {"title": "Lazy Mode Optimises Queries",
         "desc": "Calling .lazy() tells Polars to build a query plan first and eliminate wasted steps — like a GPS finding the shortest route before you start driving.",
         "pills": [".lazy()", "Plan First", "Optimised"],
         "icon": "fa6-solid:route"},
        {"title": "Lower Memory Than pandas",
         "desc": "Polars uses Apache Arrow memory under the hood, avoiding pandas' object-dtype overhead — the same data often uses 30–50% less RAM.",
         "pills": ["Arrow Backend", "30–50% Less", "Efficient"],
         "icon": "fa6-solid:leaf"},
    ],
},

"mod_05_large_scale_data_processing/lesson09_faster_dataframes_with_polars.html": {
    # Overview: Expressions, Lazy Queries, Parallel Execution, Predicate Pushdown
    "cards": [
        {"title": "Expressions Chain Cleanly",
         "desc": "Polars expressions like pl.col('price').mul(pl.col('qty')).alias('total') read left to right and combine without intermediate DataFrames or temporary variables.",
         "pills": ["pl.col()", ".alias()", "No Temps"],
         "icon": "fa6-solid:link"},
        {"title": "Collect Triggers Execution",
         "desc": "A lazy query does nothing until you call .collect() — this lets Polars batch all your filters, joins, and aggregations into one optimised pass over the data.",
         "pills": [".collect()", "One Pass", "Batched"],
         "icon": "fa6-solid:play"},
        {"title": "Benchmarks Show Real Gains",
         "desc": "On a 10-million-row group-by, Polars typically finishes in seconds while pandas can take over a minute — profiling both proves when the switch is worth it.",
         "pills": ["10× Faster", "Group-By", "Profile"],
         "icon": "fa6-solid:chart-column"},
    ],
},

"mod_05_large_scale_data_processing/lesson10_duckdb_for_analytics.html": {
    # Overview: Embedded Engine, SQL on Files, DataFrame Bridge, Columnar Engine
    "cards": [
        {"title": "SQL Without a Server",
         "desc": "DuckDB runs inside your Python process with no installation, no server, and no network — just import duckdb and start writing SELECT statements.",
         "pills": ["import duckdb", "No Server", "Embedded"],
         "icon": "fa6-solid:laptop-code"},
        {"title": "Query Files Directly",
         "desc": "duckdb.sql(\"SELECT * FROM 'sales.parquet' WHERE year=2024\") reads the file without loading it into a DataFrame first — ideal for quick ad-hoc exploration.",
         "pills": ["Parquet", "CSV", "Direct SQL"],
         "icon": "fa6-solid:file-arrow-up"},
        {"title": "Bridges pandas and Polars",
         "desc": "DuckDB can read a pandas DataFrame as a virtual table and return results as a Polars DataFrame — mixing tools in the same script with zero data copying.",
         "pills": [".df()", ".pl()", "Zero Copy"],
         "icon": "fa6-solid:bridge"},
    ],
},

"mod_05_large_scale_data_processing/lesson11_parallel_processing.html": {
    # Overview: Processes, Threads, Pool Pattern, GIL Awareness
    "cards": [
        {"title": "Processes Bypass the GIL",
         "desc": "Python's GIL blocks threads from running CPU work simultaneously, but separate processes each get their own GIL — so multiprocessing gives true parallelism for heavy computation.",
         "pills": ["multiprocessing", "Own GIL", "True Parallel"],
         "icon": "fa6-solid:microchip"},
        {"title": "Pools Manage Workers",
         "desc": "A Pool(4) creates four worker processes that pull tasks from a shared queue — you submit work and collect results without managing process lifecycles yourself.",
         "pills": ["Pool()", ".map()", "Auto-Manage"],
         "icon": "fa6-solid:users-gear"},
        {"title": "Threads Fit I/O Tasks",
         "desc": "For network calls and file reads, threads work well because the GIL releases during I/O waits — use ThreadPoolExecutor for API fetching, ProcessPoolExecutor for number crunching.",
         "pills": ["ThreadPool", "I/O Bound", "Network"],
         "icon": "fa6-solid:network-wired"},
    ],
},

"mod_05_large_scale_data_processing/lesson12_dask_basics.html": {
    # Overview: Partitions, Lazy Graph, Familiar API, Compute
    "cards": [
        {"title": "Dask Scales pandas Syntax",
         "desc": "You write dask.dataframe.read_csv() and .groupby().sum() — the same syntax as pandas — but Dask splits the work across cores and partitions automatically.",
         "pills": ["Same Syntax", "Auto-Split", "Scalable"],
         "icon": "fa6-solid:up-right-and-down-left-from-center"},
        {"title": "Compute Triggers Execution",
         "desc": "Dask builds a task graph lazily and runs nothing until you call .compute(), letting it optimise the entire chain of operations before touching the data.",
         "pills": [".compute()", "Task Graph", "Optimised"],
         "icon": "fa6-solid:play"},
        {"title": "Partitions Control Memory",
         "desc": "Dask splits a large file into partition-sized chunks (e.g. 128 MB each), processes them one at a time, and never loads the full dataset into RAM.",
         "pills": ["128 MB", "One at a Time", "Low RAM"],
         "icon": "fa6-solid:puzzle-piece"},
    ],
},

"mod_05_large_scale_data_processing/lesson13_performance_profiling.html": {
    # Overview: Time Profiling, Memory Profiling, Bottleneck Detection, Before & After
    "cards": [
        {"title": "Profile the Slowest Part",
         "desc": "Running cProfile on your script shows exactly which function consumes the most time — optimising a 2% function while ignoring a 90% bottleneck wastes effort.",
         "pills": ["cProfile", "Hotspot", "Focus"],
         "icon": "fa6-solid:crosshairs"},
        {"title": "Memory Profiling Catches Leaks",
         "desc": "memory_profiler traces RAM usage line by line, revealing where your script allocates large objects that never get freed — the root cause of 'MemoryError' crashes.",
         "pills": ["@profile", "Line-by-Line", "Leak"],
         "icon": "fa6-solid:droplet"},
        {"title": "Compare Before and After",
         "desc": "Recording runtime and peak memory before and after a change gives you hard numbers to prove an optimisation worked — not just a feeling that 'it seems faster.'",
         "pills": ["Baseline", "After", "Proof"],
         "icon": "fa6-solid:code-compare"},
    ],
},

"mod_05_large_scale_data_processing/lesson14_real_large_data_project.html": {
    # Overview: Project Plan, Data Ingestion, Processing, Delivery
    "cards": [
        {"title": "Pick Tools for the Task",
         "desc": "A 500 MB dataset works fine with pandas; a 50 GB dataset needs Polars, DuckDB, or Dask — choosing the right tool avoids rewriting your code halfway through the project.",
         "pills": ["Size Check", "Right Tool", "No Rewrite"],
         "icon": "fa6-solid:toolbox"},
        {"title": "Pipeline Stages Stay Separate",
         "desc": "Keeping ingestion, processing, and delivery in distinct scripts means you can re-run just the broken stage after a failure instead of starting from scratch.",
         "pills": ["Ingest", "Process", "Deliver"],
         "icon": "fa6-solid:cubes"},
        {"title": "Aggregations Reduce Volume",
         "desc": "Summarising 50 million rows into a 5,000-row report before loading to the dashboard keeps the front-end fast and the storage cost low.",
         "pills": ["group_by()", "Summarise", "Small Output"],
         "icon": "fa6-solid:compress"},
    ],
},

"mod_05_large_scale_data_processing/lesson15_performance_best_practices.html": {
    # Overview: Right Tool, Avoid Copies, Batch I/O, Continuous Profiling
    "cards": [
        {"title": "Copies Waste RAM Silently",
         "desc": "Every df.copy() and chained .reset_index() creates a duplicate DataFrame in memory — on a 4 GB dataset, two copies consume 12 GB total.",
         "pills": ["Inplace", "Views", "RAM Budget"],
         "icon": "fa6-solid:clone"},
        {"title": "Batch I/O Reduces Overhead",
         "desc": "Reading or writing data in large batches (100k rows) instead of one row at a time cuts disk I/O overhead by orders of magnitude — the disk arm moves fewer times.",
         "pills": ["Batch Write", "Fewer Seeks", "Throughput"],
         "icon": "fa6-solid:hard-drive"},
        {"title": "Profile Regularly, Not Once",
         "desc": "Data volumes grow monthly, so a pipeline that runs in 10 minutes today may take 3 hours next quarter — schedule profiling as part of your maintenance routine.",
         "pills": ["Monthly Check", "Trend", "Prevent"],
         "icon": "fa6-solid:calendar-check"},
    ],
},

# ═══════════════════════════════════════════════════════════
# MODULE 06 — Automation and CI/CD
# ═══════════════════════════════════════════════════════════

"mod_06_automation_and_ci_cd/lesson01_devops_concepts_for_data_analytics.html": {
    # Overview: Version Control, Automated Testing, CI/CD, Infrastructure as Code
    "cards": [
        {"title": "Automation Cuts Human Mistakes",
         "desc": "Running tests and deployments through scripts instead of manual steps eliminates the 'I forgot to update the config' errors that break production on Friday afternoon.",
         "pills": ["Scripts", "Repeatable", "Reliable"],
         "icon": "fa6-solid:robot"},
        {"title": "Feedback Loops Speed Recovery",
         "desc": "A CI pipeline that runs tests on every commit tells you within minutes whether your change broke something — fixing a bug today costs far less than finding it next month.",
         "pills": ["Fast Feedback", "Early Fix", "Low Cost"],
         "icon": "fa6-solid:arrows-rotate"},
        {"title": "Infrastructure as Code Scales",
         "desc": "Defining servers, databases, and pipelines in code files means you can spin up an identical environment in minutes instead of manually configuring machines for hours.",
         "pills": ["Reproducible", "One Command", "Version Control"],
         "icon": "fa6-solid:file-code"},
    ],
},

"mod_06_automation_and_ci_cd/lesson02_gitlab_ci_cd_overview.html": {
    # Overview: .gitlab-ci.yml, Stages, Runners, Artifacts
    "cards": [
        {"title": "One File Defines Everything",
         "desc": "The .gitlab-ci.yml file lists every build, test, and deploy step in a single place — anyone on the team can read it to understand the full pipeline without asking.",
         "pills": [".gitlab-ci.yml", "Readable", "Single Source"],
         "icon": "fa6-solid:file-lines"},
        {"title": "Stages Run in Order",
         "desc": "GitLab executes stages sequentially — build first, then test, then deploy — but runs jobs within the same stage in parallel to save time.",
         "pills": ["Sequential", "Parallel Jobs", "Efficient"],
         "icon": "fa6-solid:layer-group"},
        {"title": "Artifacts Pass Data Forward",
         "desc": "A build stage can save compiled files or test reports as artifacts that later stages download automatically — no manual file copying between jobs.",
         "pills": ["artifacts:", "Download", "Automatic"],
         "icon": "fa6-solid:box-open"},
    ],
},

"mod_06_automation_and_ci_cd/lesson03_scheduling_data_jobs.html": {
    # Overview: Cron Jobs, Task Schedulers, Retry Logic, Logging
    "cards": [
        {"title": "Schedules Replace Reminders",
         "desc": "A cron job that runs your pipeline every morning at 6 AM is more reliable than a calendar reminder to run it yourself — machines do not oversleep or take holidays.",
         "pills": ["crontab", "Daily", "Unattended"],
         "icon": "fa6-solid:clock"},
        {"title": "Retries Handle Blips",
         "desc": "Configuring a job to retry twice on failure handles temporary network errors automatically, without waking someone up for a problem that fixes itself in 30 seconds.",
         "pills": ["max_retries=2", "Auto-Recover", "Transient"],
         "icon": "fa6-solid:rotate-right"},
        {"title": "Logs Prove Execution",
         "desc": "Every scheduled run should write a log file with start time, end time, row count, and status — when a stakeholder asks 'Did it run?', the log answers instantly.",
         "pills": ["Timestamp", "Row Count", "Audit"],
         "icon": "fa6-solid:scroll"},
    ],
},

"mod_06_automation_and_ci_cd/lesson05_deployment_workflow.html": {
    # Overview: Environments, Build Step, Approval Gate, Rollback
    "cards": [
        {"title": "Environments Isolate Risk",
         "desc": "Testing in a staging environment that mirrors production catches bugs before they affect real users — like a dress rehearsal before opening night.",
         "pills": ["Dev", "Staging", "Production"],
         "icon": "fa6-solid:layer-group"},
        {"title": "Approval Gates Add Safety",
         "desc": "Requiring a team lead to approve the deploy-to-production step prevents accidental releases and gives a human a final chance to review changes.",
         "pills": ["Manual Approve", "Review", "Control"],
         "icon": "fa6-solid:user-check"},
        {"title": "Rollback Plans Save You",
         "desc": "If a deployment fails, a one-command rollback reverts to the previous working version in seconds — without a plan, recovery could take hours of panicked debugging.",
         "pills": ["Revert", "One Command", "Seconds"],
         "icon": "fa6-solid:arrow-rotate-left"},
    ],
},

}

# ─── HTML template for the 3-card body ──────────────────────────────

CARD_TEMPLATE_PINK = """<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="{icon}"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">{title}</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">{desc}</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">{pill0}</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">{pill1}</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">{pill2}</span>
    </div>
  </div>
</div>"""

CARD_TEMPLATE_VIOLET = """<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="{icon}"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">{title}</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">{desc}</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">{pill0}</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">{pill1}</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">{pill2}</span>
    </div>
  </div>
</div>"""

CARD_TEMPLATE_BLUE = """<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="{icon}"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">{title}</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">{desc}</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">{pill0}</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">{pill1}</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">{pill2}</span>
    </div>
  </div>
</div>"""

TEMPLATES = [CARD_TEMPLATE_PINK, CARD_TEMPLATE_VIOLET, CARD_TEMPLATE_BLUE]


def build_body(cards):
    """Return the full <div class="bg-white px-8 py-7 space-y-4">…</div> block."""
    rendered = []
    for i, card in enumerate(cards):
        html = TEMPLATES[i].format(
            icon=html_mod.escape(card["icon"], quote=True),
            title=html_mod.escape(card["title"]),
            desc=card["desc"],  # may contain <strong>, keep as-is
            pill0=html_mod.escape(card["pills"][0]),
            pill1=html_mod.escape(card["pills"][1]),
            pill2=html_mod.escape(card["pills"][2]),
        )
        rendered.append(html)

    return '<div class="bg-white px-8 py-7 space-y-4">\n\n' + "\n\n".join(rendered) + "\n\n</div>"


def replace_key_ideas_body(content, new_body):
    """Replace the body div inside <section id="key-ideas"> … </section>."""
    # Match from opening body div to the closing </div> that sits before </div></section>
    pattern = re.compile(
        r'(<section id="key-ideas"[^>]*>.*?)'           # group 1: everything up to body
        r'(<div class="bg-white px-8 py-7 space-y-4">)'  # anchor start of body
        r'(.*?)'                                          # old body content
        r'(</div>\s*</div>\s*</section>)',                # closing wrappers
        re.DOTALL,
    )
    m = pattern.search(content)
    if not m:
        return None  # signal no match
    return content[:m.start(2)] + new_body + "\n" + m.group(4)[len("</div>"):].lstrip("\n")  # keep outer </div></section>


def fix_css_kt_hover(content):
    """Add border-color: #CB187D to .obj-card-kt:hover if missing."""
    # Check if border-color already present
    m = re.search(r"\.obj-card-kt:hover\s*\{([^}]+)\}", content)
    if not m:
        return content, False
    rule = m.group(1)
    if "border-color" in rule:
        return content, False  # already done
    # Add border-color before the closing brace
    old = m.group(0)
    new = old.replace("}", " border-color: #CB187D; }")
    return content.replace(old, new, 1), True


def main():
    ok = 0
    skip = 0
    fail = 0
    css_fixed = 0

    for rel, data in sorted(LESSONS.items()):
        fp = os.path.join(BASE, rel.replace("/", os.sep))
        if not os.path.isfile(fp):
            print(f"  ❌ NOT FOUND: {rel}")
            fail += 1
            continue

        with open(fp, "r", encoding="utf-8") as fh:
            content = fh.read()

        # Build new body
        new_body = build_body(data["cards"])

        # Replace body
        new_content = replace_key_ideas_body(content, new_body)
        if new_content is None:
            print(f"  ❌ NO MATCH: {rel}")
            fail += 1
            continue

        # Fix CSS
        new_content, did_fix_css = fix_css_kt_hover(new_content)
        if did_fix_css:
            css_fixed += 1

        with open(fp, "w", encoding="utf-8") as fh:
            fh.write(new_content)

        print(f"  ✅ {rel}" + (" (+ CSS fix)" if did_fix_css else ""))
        ok += 1

    print(f"\nDone: {ok} patched, {skip} skipped, {fail} failed, {css_fixed} CSS fixes")


if __name__ == "__main__":
    main()
