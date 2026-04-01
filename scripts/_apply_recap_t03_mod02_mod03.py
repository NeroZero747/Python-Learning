#!/usr/bin/env python3
"""Rewrite #recap section for track_03 mod_02 + mod_03 lessons."""

import re, pathlib

ROOT = pathlib.Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering")
MOD02 = "mod_02_nosql_and_modern_data_storage"
MOD03 = "mod_03_api_data_integration"

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

    # ── MOD 02 — NoSQL and Modern Data Storage ───────────────────────────────

    f"{MOD02}/lesson01_what_is_nosql.html": [
        ("fa6-solid:database", "Define NoSQL",
         "You can explain how NoSQL databases store data outside traditional tables."),
        ("fa6-solid:lightbulb", "Why NoSQL was created",
         "Scale and flexibility demands drove the creation of non-relational databases."),
        ("fa6-solid:right-left", "SQL vs NoSQL basics",
         "You can list the key trade-offs between relational and non-relational stores."),
        ("fa6-solid:crosshairs", "NoSQL use cases",
         "Real-time apps, flexible schemas, and massive scale all favour NoSQL."),
    ],

    f"{MOD02}/lesson02_types_of_nosql_databases.html": [
        ("fa6-solid:layer-group", "Four NoSQL families",
         "Document, key-value, column-family, and graph cover most non-relational needs."),
        ("fa6-solid:box-open", "How each stores data",
         "Each family organises records differently to optimise specific access patterns."),
        ("fa6-solid:wrench", "Problems each solves",
         "You can match a data shape to the NoSQL type built for it."),
        ("fa6-solid:map-signs", "Choosing a type",
         "Start from your query pattern, then pick the family that fits."),
    ],

    f"{MOD02}/lesson03_document_databases_mongodb.html": [
        ("fa6-solid:file-lines", "Document model",
         "MongoDB stores each record as a flexible JSON-like document, not a row."),
        ("fa6-solid:pen-to-square", "Insert and update documents",
         'Use <code class="font-mono">insert_one()</code> and <code class="font-mono">update_one()</code> to write and modify records.'),
        ("fa6-solid:magnifying-glass", "Query documents",
         'Pass a filter dictionary to <code class="font-mono">find()</code> to retrieve matching documents.'),
        ("fa6-solid:table-columns", "Documents vs SQL rows",
         "Documents can hold nested objects; SQL rows cannot without extra joins."),
    ],

    f"{MOD02}/lesson04_key_value_databases_redis.html": [
        ("fa6-solid:key", "Key-value model",
         "Every record is a simple pair: one unique key mapped to one value."),
        ("fa6-solid:bolt", "In-memory speed",
         "Redis stores data in RAM, delivering sub-millisecond read and write times."),
        ("fa6-solid:box-archive", "Core Redis operations",
         'You can <code class="font-mono">SET</code>, <code class="font-mono">GET</code>, and <code class="font-mono">DELETE</code> values using straightforward commands.'),
        ("fa6-solid:clock-rotate-left", "Caching use cases",
         "Session tokens, page fragments, and API results are common caching targets."),
    ],

    f"{MOD02}/lesson05_column_family_databases_cassandra.html": [
        ("fa6-solid:table-cells", "Column-family model",
         "Cassandra groups columns into families so each row can have different fields."),
        ("fa6-solid:server", "Distributed architecture",
         "Data replicates across nodes automatically, so no single server is critical."),
        ("fa6-solid:pen-to-square", "Write and query data",
         "CQL looks like SQL, letting you insert and select with familiar syntax."),
        ("fa6-solid:chart-line", "High-throughput scenarios",
         "IoT sensors and event logs benefit from Cassandra\u2019s fast, distributed writes."),
    ],

    f"{MOD02}/lesson06_graph_databases_neo4j.html": [
        ("fa6-solid:circle-nodes", "Graph model",
         "Nodes represent entities and edges represent the relationships between them."),
        ("fa6-solid:magnifying-glass", "Cypher queries",
         'Use <code class="font-mono">MATCH</code> and arrow syntax to find patterns in connected data.'),
        ("fa6-solid:share-nodes", "Relationship traversal",
         "Graphs follow multi-hop connections without expensive recursive joins."),
        ("fa6-solid:users", "Graph use cases",
         "Social networks, fraud detection, and recommendation engines rely on graphs."),
    ],

    f"{MOD02}/lesson07_sql_vs_nosql_choosing_the_right_database.html": [
        ("fa6-solid:scale-balanced", "Compare trade-offs",
         "SQL offers consistency and joins; NoSQL offers flexibility and horizontal scale."),
        ("fa6-solid:list-check", "Decision criteria",
         "Data shape, query patterns, and scale requirements drive the database choice."),
        ("fa6-solid:diagram-project", "Polyglot persistence",
         "Many systems combine SQL and NoSQL, using each where it fits best."),
        ("fa6-solid:route", "Make the call",
         "You can evaluate a new project and recommend the right database type."),
    ],

    # ── MOD 03 — API Data Integration ─────────────────────────────────────────

    f"{MOD03}/lesson01_what_is_an_api.html": [
        ("fa6-solid:plug", "Define an API",
         "An API is a contract that lets two programs exchange data over a network."),
        ("fa6-solid:network-wired", "Why APIs exist",
         "They let separate systems share data without exposing internal logic."),
        ("fa6-solid:arrows-left-right", "Request-response cycle",
         "Your code sends a request; the server processes it and returns a response."),
        ("fa6-solid:laptop-code", "Python and APIs",
         'Python\u2019s <code class="font-mono">requests</code> library makes calling any API a few lines of code.'),
    ],

    f"{MOD03}/lesson02_understanding_http_requests.html": [
        ("fa6-solid:globe", "HTTP basics",
         "HTTP is the protocol every web API uses to send and receive data."),
        ("fa6-solid:list-ol", "Request methods",
         "GET reads data, POST creates it, PUT updates it, DELETE removes it."),
        ("fa6-solid:circle-check", "Status codes",
         "A 200 means success, a 404 means not found, and 500 means server error."),
        ("fa6-solid:sliders", "Headers and parameters",
         "Headers carry metadata; query parameters filter what the server returns."),
    ],

    f"{MOD03}/lesson03_using_the_python_requests_library.html": [
        ("fa6-solid:download", "Install and import requests",
         'Run <code class="font-mono">pip install requests</code> and import it in one line.'),
        ("fa6-solid:paper-plane", "Send GET and POST requests",
         'Use <code class="font-mono">requests.get()</code> or <code class="font-mono">.post()</code> to talk to any web API.'),
        ("fa6-solid:file-code", "Inspect responses",
         'Check <code class="font-mono">.status_code</code>, <code class="font-mono">.headers</code>, and <code class="font-mono">.text</code> to understand what came back.'),
        ("fa6-solid:code", "Parse JSON responses",
         'Call <code class="font-mono">.json()</code> to convert the response body into a Python dictionary.'),
    ],

    f"{MOD03}/lesson04_working_with_json_data.html": [
        ("fa6-solid:brackets-curly", "JSON structure",
         "JSON uses key-value pairs and arrays to represent structured data as text."),
        ("fa6-solid:file-import", "Parse JSON in Python",
         'Use <code class="font-mono">json.loads()</code> to turn a JSON string into a Python dictionary.'),
        ("fa6-solid:sitemap", "Navigate nested data",
         "Chain bracket lookups to reach values buried inside nested dictionaries and lists."),
        ("fa6-solid:file-export", "Write JSON files",
         'Call <code class="font-mono">json.dump()</code> to save a Python object as a JSON file.'),
    ],

    f"{MOD03}/lesson05_parsing_api_responses.html": [
        ("fa6-solid:triangle-exclamation", "Check status codes",
         'Test <code class="font-mono">response.status_code</code> before touching the response body.'),
        ("fa6-solid:shield-halved", "Handle errors gracefully",
         'Wrap API calls in <code class="font-mono">try/except</code> so failures log instead of crash.'),
        ("fa6-solid:layer-group", "Extract nested data",
         "Drill into nested keys and lists to pull out the fields you need."),
        ("fa6-solid:table", "Build clean datasets",
         "Collect parsed records into a list of dictionaries ready for analysis."),
    ],

    f"{MOD03}/lesson06_authentication_with_api_keys.html": [
        ("fa6-solid:lock", "Why APIs need auth",
         "Authentication controls who can access data and prevents unauthorised use."),
        ("fa6-solid:key", "What an API key is",
         "A unique string the server checks to verify your identity on every request."),
        ("fa6-solid:paper-plane", "Send keys in requests",
         'Pass the key in a header or query parameter with <code class="font-mono">requests.get()</code>.'),
        ("fa6-solid:vault", "Store keys securely",
         'Keep keys in environment variables, never hard-coded in your source files.'),
    ],

    f"{MOD03}/lesson07_oauth_authentication.html": [
        ("fa6-solid:user-shield", "What OAuth is",
         "A protocol that grants limited access without sharing your actual password."),
        ("fa6-solid:arrows-rotate", "The OAuth flow",
         "Redirect, authorise, receive a code, then exchange it for a token."),
        ("fa6-solid:ticket", "Access and refresh tokens",
         "Access tokens expire quickly; refresh tokens let you get new ones silently."),
        ("fa6-solid:laptop-code", "OAuth in Python",
         'Use <code class="font-mono">requests</code> to exchange credentials and attach Bearer tokens.'),
    ],

    f"{MOD03}/lesson08_handling_pagination_in_apis.html": [
        ("fa6-solid:book-open", "What pagination is",
         "APIs split large result sets into pages so each response stays small."),
        ("fa6-solid:forward", "Page through results",
         "Increment a page number or offset parameter to fetch the next batch."),
        ("fa6-solid:link", "Follow next-page links",
         "Some APIs return a URL for the next page inside the response body."),
        ("fa6-solid:list-check", "Collect complete datasets",
         "Loop until no more pages remain, extending one list with every batch."),
    ],

    f"{MOD03}/lesson09_handling_api_rate_limits.html": [
        ("fa6-solid:gauge-high", "What rate limits are",
         "Servers cap how many requests you can send in a given time window."),
        ("fa6-solid:magnifying-glass", "Detect rate-limit errors",
         'A <code class="font-mono">429</code> status code tells you to slow down immediately.'),
        ("fa6-solid:clock", "Add delays and retries",
         'Use <code class="font-mono">time.sleep()</code> and exponential backoff between retry attempts.'),
        ("fa6-solid:shield-halved", "Build resilient scripts",
         "Combine retry logic with logging so your pipeline recovers automatically."),
    ],

    f"{MOD03}/lesson10_loading_api_data_into_pandas.html": [
        ("fa6-solid:table", "JSON to DataFrame",
         'Pass a list of dictionaries to <code class="font-mono">pd.DataFrame()</code> for instant tabular data.'),
        ("fa6-solid:filter", "Clean and filter",
         "Drop nulls, rename columns, and filter rows before any analysis begins."),
        ("fa6-solid:chart-bar", "Analyse API data",
         "Apply groupby, value counts, and summary statistics to the loaded DataFrame."),
        ("fa6-solid:file-csv", "Export for reuse",
         'Call <code class="font-mono">to_csv()</code> or <code class="font-mono">to_parquet()</code> to save your cleaned data.'),
    ],

    f"{MOD03}/lesson11_saving_api_data_to_databases.html": [
        ("fa6-solid:database", "Store data in SQLite",
         "SQLite gives you a local database in a single file with zero setup."),
        ("fa6-solid:code", "Use pandas to_sql",
         'Call <code class="font-mono">df.to_sql()</code> to write a DataFrame directly into a database table.'),
        ("fa6-solid:arrows-rotate", "Upsert logic",
         'Use <code class="font-mono">if_exists=\'replace\'</code> or merge queries to handle duplicate records.'),
        ("fa6-solid:magnifying-glass", "Query stored data",
         'Read it back with <code class="font-mono">pd.read_sql()</code> to confirm the data loaded correctly.'),
    ],

    f"{MOD03}/lesson12_building_an_api_data_pipeline.html": [
        ("fa6-solid:diagram-project", "Pipeline structure",
         "Extract, transform, and load stages form the backbone of every pipeline."),
        ("fa6-solid:download", "Extract stage",
         "Fetch raw data from one or more API endpoints into Python objects."),
        ("fa6-solid:wand-magic-sparkles", "Transform stage",
         "Clean, reshape, and validate the raw data before it reaches storage."),
        ("fa6-solid:database", "Load stage",
         "Write the final DataFrame to a database table or export file."),
    ],

    f"{MOD03}/lesson13_real_world_api_integration_project.html": [
        ("fa6-solid:flask", "Build a complete pipeline",
         "You connected extraction, transformation, and loading into one working script."),
        ("fa6-solid:shield-halved", "Handle real-world errors",
         "Timeouts, missing fields, and bad responses no longer crash your pipeline."),
        ("fa6-solid:table", "Transform into DataFrames",
         "Raw API records become clean, analysis-ready pandas tables in a few steps."),
        ("fa6-solid:database", "Persist for analysis",
         "Saved results live in a database so any query can reach them later."),
    ],

    f"{MOD03}/lesson14_api_best_practices.html": [
        ("fa6-solid:shield-halved", "Defensive error handling",
         'Always check status codes and wrap calls in <code class="font-mono">try/except</code> blocks.'),
        ("fa6-solid:file-lines", "Logging and monitoring",
         "Write timestamped log entries so you can trace failures after the fact."),
        ("fa6-solid:vault", "Credential management",
         "Store API keys in environment variables, never in committed source code."),
        ("fa6-solid:book", "Document your integrations",
         "Record endpoints, auth methods, and rate limits so teammates can maintain them."),
    ],
}


# ── Main ──────────────────────────────────────────────────────────────────────

assert len(LESSONS) == 21, f"Expected 21 lessons, got {len(LESSONS)}"

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
