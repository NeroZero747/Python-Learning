#!/usr/bin/env python3
"""Rewrite the #overview section for all 56 track_03 lessons."""

import re, pathlib

BASE = pathlib.Path(r"pages/track_03_data_engineering")

OV_RE = re.compile(r'<section id="overview">.*?</section>', re.DOTALL)

# ── Card accent styles (pink, violet, blue, emerald) ────────────────
STYLES = [
    # (hover_border, hover_bg, icon_bg, icon_text_cls)
    ("[#f5c6e0]", "[#fdf0f7]/40", "[#fdf0f7]", "text-brand"),
    ("violet-100", "violet-50/30", "violet-50", "text-violet-500"),
    ("blue-100", "blue-50/30", "blue-50", "text-blue-500"),
    ("emerald-100", "emerald-50/30", "emerald-50", "text-emerald-500"),
]


def build_card(icon, title, subtitle, desc, idx):
    hb, hbg, ibg, itxt = STYLES[idx]
    return (
        f'      <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4'
        f" hover:border-{hb} hover:bg-{hbg} transition-colors\">\n"
        f'        <div class="flex items-center gap-3 mb-2.5">\n'
        f'          <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-{ibg} shrink-0">\n'
        f'            <span class="iconify {itxt} text-base" data-icon="{icon}"></span>\n'
        f"          </span>\n"
        f"          <div>\n"
        f'            <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>\n'
        f'            <p class="text-[10px] text-gray-400 italic leading-tight">{subtitle}</p>\n'
        f"          </div>\n"
        f"        </div>\n"
        f'        <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>\n'
        f"      </div>"
    )


def build_section(hook, intro, cards, tip):
    chtml = "\n\n".join(build_card(*c, i) for i, c in enumerate(cards))
    return (
        '<section id="overview">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:binoculars"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Overview</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A high-level summary of the topic</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-5">\n'
        "\n"
        '      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">\n'
        '        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>\n'
        '        <div class="relative flex items-center gap-4">\n'
        '          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">\n'
        '            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>\n'
        '          </span>\n'
        f'          <p class="text-base text-gray-800 leading-relaxed font-medium">{hook}</p>\n'
        '        </div>\n'
        '      </div>\n'
        "\n"
        f'      <p class="text-sm text-gray-600 leading-relaxed">{intro}</p>\n'
        "\n"
        '      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">\n'
        "\n"
        f"{chtml}\n"
        "\n"
        '      </div>\n'
        "\n"
        '      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        '        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        f'        <p class="text-sm text-gray-600">{tip}</p>\n'
        '      </div>\n'
        "\n"
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── Lesson definitions ──────────────────────────────────────────────
# Each entry: { hook, intro, cards [(icon, title, subtitle, desc) x4], tip }

LESSONS = {

    # ── Module 01 — Data Engineering Foundations ─────────────────────

    "mod_01_data_engineering_foundations/lesson01_what_is_data_engineering.html": {
        "hook": "Data engineering is the work of collecting raw data from many sources, cleaning it, and delivering it in a form that analysts and scientists can trust.",
        "intro": "Think of data engineering like running a water treatment plant. Raw water flows in from rivers and wells. The plant filters it, tests it, and pumps clean water to every tap in the city. A <strong>data engineer</strong> builds and maintains that plant, and Python is one of the main tools for the job.",
        "cards": [
            ("fa6-solid:faucet-drip", "Data Sources", "The intake pipes \u2014 where raw water arrives", "Every river, well, and reservoir feeding into the plant."),
            ("fa6-solid:arrows-turn-right", "Data Pipelines", "The treatment stages \u2014 filters in sequence", "Each stage moves water one step closer to the tap."),
            ("fa6-solid:database", "Data Storage", "The reservoir \u2014 holds clean water ready", "A large tank keeping treated water available on demand."),
            ("fa6-solid:vial", "Data Quality", "The testing lab \u2014 checks every batch", "Samples tested at each stage so nothing unsafe gets through."),
        ],
        "tip": "If you have ever tidied a spreadsheet \u2014 removing blanks, fixing dates, merging columns \u2014 you have already done mini data engineering.",
    },

    "mod_01_data_engineering_foundations/lesson02_etl_vs_elt.html": {
        "hook": "ETL and ELT are two strategies for moving data from where it is created to where it can be analysed.",
        "intro": "Think of data movement like a post office. Letters arrive in bags, get sorted, and are delivered to the right addresses. <strong>ETL</strong> sorts the letters before they leave the central depot. <strong>ELT</strong> ships the bags first and sorts them at the local branch.",
        "cards": [
            ("fa6-solid:box-open", "Extract", "The mail bags \u2014 collecting letters from drop-offs", "Gathering raw letters before any sorting begins."),
            ("fa6-solid:filter", "Transform", "The sorting room \u2014 organising by postcode", "Rearranging and labelling so each letter reaches the right address."),
            ("fa6-solid:truck-fast", "Load", "The delivery van \u2014 carrying sorted mail", "Moving processed letters into the target mailbox."),
            ("fa6-solid:arrows-rotate", "Order of Steps", "Sort first or deliver first \u2014 two workflows", "The key choice: clean before shipping, or ship and clean on arrival."),
        ],
        "tip": "Most modern cloud warehouses favour ELT because storage is cheap and compute can transform data in place.",
    },

    "mod_01_data_engineering_foundations/lesson03_handling_large_datasets.html": {
        "hook": "Handling large datasets means processing more data than your computer\u2019s memory can hold at once.",
        "intro": "Think of a large dataset like a house full of furniture, but you only have a small van. You cannot fit everything in one trip. Instead, you load the van, drive to the new house, unload, and come back for the next load. <strong>Chunking</strong> is that strategy, and Python gives you the tools to do it.",
        "cards": [
            ("fa6-solid:microchip", "Memory Limits", "The van\u2019s cargo space \u2014 only so much fits", "Your computer\u2019s RAM sets the ceiling for each load."),
            ("fa6-solid:layer-group", "Chunking", "Multiple trips \u2014 a vanload at a time", "Breaking the job into smaller loads you can handle."),
            ("fa6-solid:water", "Streaming", "A conveyor belt \u2014 items pass without piling up", "Processing rows one by one so nothing queues in memory."),
            ("fa6-solid:file-zipper", "File Formats", "Flat-pack furniture \u2014 compact for the journey", "Smaller, compressed formats that fit more into each trip."),
        ],
        "tip": "Pandas reads entire files into RAM by default. For files bigger than your RAM, chunking or a streaming tool like Polars is essential.",
    },

    "mod_01_data_engineering_foundations/lesson05_parquet_efficient_storage.html": {
        "hook": "Parquet is a file format that stores data by column instead of by row, making it faster to read and smaller to store.",
        "intro": "Think of a stack of folders on your desk \u2014 each folder holds one row of data, so reading a single column means opening every folder. A <strong>filing cabinet</strong> organises by column: one drawer for names, another for dates, another for amounts. Parquet works like that cabinet, and Python can open any drawer directly.",
        "cards": [
            ("fa6-solid:table-columns", "Columnar Layout", "One drawer per column \u2014 names, dates separated", "Each column sits in its own drawer, ready for quick access."),
            ("fa6-solid:minimize", "Compression", "Vacuum bags \u2014 similar items shrink together", "Grouping identical types reduces the storage footprint."),
            ("fa6-solid:hand-pointer", "Selective Reads", "Open one drawer, not every folder", "Read only the columns you need without touching the rest."),
            ("fa6-solid:tags", "Schema Metadata", "Drawer labels \u2014 what type of data lives inside", "Built-in labels that describe each column\u2019s data type."),
        ],
        "tip": "A CSV file that takes up 500\u202fMB can shrink to under 100\u202fMB in Parquet \u2014 and load ten times faster because you skip unneeded columns.",
    },

    "mod_01_data_engineering_foundations/lesson06_intro_to_polars_optional.html": {
        "hook": "Polars is a fast DataFrame library that processes data in parallel, making it ideal when Pandas feels too slow.",
        "intro": "Think of Pandas as a single-lane road: one car passes at a time, so traffic backs up when the road is busy. <strong>Polars</strong> is a multi-lane motorway \u2014 several cars travel side by side, clearing the queue much faster. Python lets you switch between either road.",
        "cards": [
            ("fa6-solid:road", "Parallel Execution", "Multiple lanes \u2014 cars moving side by side", "Work splits across lanes so nothing waits in a queue."),
            ("fa6-solid:clock", "Lazy Evaluation", "Route planning \u2014 mapping the journey first", "Polars plans the fastest route, then executes in one pass."),
            ("fa6-solid:sliders", "Expressions", "Dashboard controls \u2014 each knob adjusts one thing", "Compact instructions that tell Polars exactly what to compute."),
            ("fa6-solid:bolt", "Zero-Copy Reads", "Direct on-ramp \u2014 no toll booth delay", "Data loads straight into memory without extra copying."),
        ],
        "tip": "If your Pandas job takes minutes, try the same logic in Polars \u2014 the syntax is similar, but the speed difference can be dramatic.",
    },

    "mod_01_data_engineering_foundations/lesson07_pipeline_design_concepts.html": {
        "hook": "A data pipeline is a sequence of steps that automatically moves data from its source to its destination, transforming it along the way.",
        "intro": "Think of a data pipeline like a factory assembly line. Raw materials arrive at one end, each station performs one task \u2014 cutting, welding, painting \u2014 and a finished product rolls off the other end. A <strong>pipeline</strong> is that assembly line, and each station is a Python function.",
        "cards": [
            ("fa6-solid:link", "Stages", "Stations on the line \u2014 each does one job", "Every stage handles a single task before passing data on."),
            ("fa6-solid:code-branch", "Dependencies", "Station order \u2014 welding before painting", "Some stages must finish before the next one can start."),
            ("fa6-solid:triangle-exclamation", "Error Handling", "Quality control \u2014 pulling defects off the belt", "A checkpoint catches bad data before it reaches the end."),
            ("fa6-solid:rotate", "Idempotency", "Re-running a station \u2014 same input, same output", "Running a stage twice produces the exact same result."),
        ],
        "tip": "If you have ever chained Excel formulas across worksheets \u2014 each one feeding the next \u2014 you have already built a simple pipeline.",
    },

    # ── Module 02 — NoSQL and Modern Data Storage ────────────────────

    "mod_02_nosql_and_modern_data_storage/lesson01_what_is_nosql.html": {
        "hook": "NoSQL databases store data without the strict rows-and-columns structure that traditional SQL databases require.",
        "intro": "Think of a SQL database as a grid of identical filing cabinets \u2014 every drawer is the same size. A <strong>NoSQL</strong> database is more like a warehouse with adjustable shelving: you can store boxes of any shape and size, rearranging the shelves as your needs change. Python connects to both.",
        "cards": [
            ("fa6-solid:expand", "Flexible Schema", "Adjustable shelves \u2014 resize to fit any box", "Shelves that slide wider or narrower for any box shape."),
            ("fa6-solid:arrows-left-right", "Horizontal Scaling", "Adding more aisles \u2014 extend the warehouse", "Spread data across many machines instead of one bigger one."),
            ("fa6-solid:shapes", "Data Models", "Box types \u2014 crates, tubes, flat-packs", "Documents, key-value pairs, columns, and graphs each suit a shape."),
            ("fa6-solid:scale-balanced", "Trade-offs", "Shelf labels vs speed \u2014 flexibility costs clarity", "Wide shelves hold anything, but finding one item takes longer."),
        ],
        "tip": "Most analytics teams use SQL and NoSQL side by side \u2014 SQL for structured reports, NoSQL for logs, events, or rapidly changing schemas.",
    },

    "mod_02_nosql_and_modern_data_storage/lesson02_types_of_nosql_databases.html": {
        "hook": "NoSQL databases come in four main types, each designed for a different shape of data and a different access pattern.",
        "intro": "Think of a library with four specialised rooms. One room stores thick reference books, another holds index cards, a third has tall columns of newspapers, and the last maps connections on a corkboard. Each <strong>NoSQL type</strong> is one of those rooms, optimised for its own kind of content.",
        "cards": [
            ("fa6-solid:book", "Document Stores", "The reference room \u2014 thick books with chapters", "Each book holds nested sections all in one place."),
            ("fa6-solid:key", "Key-Value Stores", "The index card drawer \u2014 one card per keyword", "A simple lookup: give the key, get the value back instantly."),
            ("fa6-solid:table-columns", "Column-Family", "The newspaper archive \u2014 stacked by column", "Data grouped by column for fast scans across millions of rows."),
            ("fa6-solid:diagram-project", "Graph Databases", "The corkboard \u2014 pins and strings linking topics", "Nodes and connections that map how things relate to each other."),
        ],
        "tip": "You do not need to memorise every NoSQL type now. Focus on recognising which room your data belongs in.",
    },

    "mod_02_nosql_and_modern_data_storage/lesson03_document_databases_mongodb.html": {
        "hook": "MongoDB is a document database that stores data as flexible JSON-like records instead of fixed rows and columns.",
        "intro": "Think of a traditional database as a printed spreadsheet \u2014 every row must have the same columns. <strong>MongoDB</strong> is more like a notebook full of sticky notes. Each note can hold different information, and you can stick extra fields onto any note without redesigning the page. Python talks to MongoDB through PyMongo.",
        "cards": [
            ("fa6-solid:note-sticky", "Documents", "The sticky note \u2014 holds its own unique fields", "Each note carries whatever information it needs."),
            ("fa6-solid:folder-open", "Collections", "A section in the notebook \u2014 related notes grouped", "Related notes live in the same section for easy browsing."),
            ("fa6-solid:magnifying-glass", "Queries", "Flipping through notes \u2014 find by any field", "Search for notes by any piece of information they contain."),
            ("fa6-solid:sitemap", "Nested Data", "A note with sub-notes clipped underneath", "A single note can hold smaller notes inside it."),
        ],
        "tip": "If your data changes shape often \u2014 new fields appear, old ones vanish \u2014 a document database handles that naturally without ALTER TABLE migrations.",
    },

    "mod_02_nosql_and_modern_data_storage/lesson04_key_value_databases_redis.html": {
        "hook": "Redis is a key-value database that stores data in memory, making it one of the fastest ways to look up information.",
        "intro": "Think of Redis like a coat-check counter at a busy event. You hand over your coat and get a numbered ticket. To get it back, you show the ticket \u2014 the attendant grabs your coat instantly. A <strong>key</strong> is that ticket, and the <strong>value</strong> is whatever you stored behind the counter.",
        "cards": [
            ("fa6-solid:ticket", "Keys", "The numbered ticket \u2014 your unique claim token", "A short label that identifies exactly what you stored."),
            ("fa6-solid:box-archive", "Values", "The coat behind the counter \u2014 any item checked in", "Strings, numbers, or small structures attached to a key."),
            ("fa6-solid:bolt-lightning", "In-Memory Speed", "No trip to the back room \u2014 everything at the counter", "Data lives in RAM, so lookups return in microseconds."),
            ("fa6-solid:hourglass-half", "Expiry", "A timed ticket \u2014 auto-discarded after closing", "Keys can disappear automatically after a set interval."),
        ],
        "tip": "Redis is commonly used for caching \u2014 storing a copy of a slow query\u2019s result so the next request gets it instantly.",
    },

    "mod_02_nosql_and_modern_data_storage/lesson05_column_family_databases_cassandra.html": {
        "hook": "Cassandra is a column-family database designed to handle massive amounts of data spread across many machines.",
        "intro": "Think of Cassandra like a chain of identical supermarkets across a country. Every store carries the same products on the same shelves. If one store closes, customers walk to the next one and find exactly the same stock. <strong>Cassandra</strong> copies your data across many nodes the same way, so nothing is lost if one machine fails.",
        "cards": [
            ("fa6-solid:store", "Partitions", "Each store \u2014 holds a slice of the total stock", "Data splits across nodes so no single machine holds everything."),
            ("fa6-solid:copy", "Replication", "Identical shelves \u2014 same stock in every branch", "Copies of each partition sit on multiple nodes for safety."),
            ("fa6-solid:grip-lines", "Wide Rows", "A long aisle \u2014 thousands of products in one row", "A single partition key can hold millions of related columns."),
            ("fa6-solid:feather-pointed", "Write Speed", "Express checkout \u2014 thousands of shoppers at once", "Built for fast writes across many machines simultaneously."),
        ],
        "tip": "Cassandra trades flexible querying for raw speed. Plan your queries before you design your tables \u2014 the data model follows the questions you ask.",
    },

    "mod_02_nosql_and_modern_data_storage/lesson06_graph_databases_neo4j.html": {
        "hook": "Neo4j is a graph database that stores data as nodes and relationships, making it natural to explore how things connect.",
        "intro": "Think of a graph database like a wall chart of your team\u2019s contacts. Each person is a pin on the board, and strings connect people who know each other. Following the strings lets you answer questions like \u201cWho knows someone at Company X?\u201d A <strong>graph database</strong> stores those pins and strings, and Python can walk along them.",
        "cards": [
            ("fa6-solid:circle-dot", "Nodes", "Pins on the board \u2014 each one is an entity", "Every person, product, or place is its own pin."),
            ("fa6-solid:link", "Relationships", "Strings between pins \u2014 named connections", "Each string carries a label like KNOWS or BOUGHT."),
            ("fa6-solid:route", "Traversals", "Following the strings \u2014 walking pin to pin", "You hop along connections to discover paths and patterns."),
            ("fa6-solid:tag", "Properties", "Labels on each pin \u2014 extra details attached", "Nodes and relationships can carry key-value attributes."),
        ],
        "tip": "Graph databases shine when your questions involve chains \u2014 friend-of-a-friend, supply chains, or dependency trees.",
    },

    "mod_02_nosql_and_modern_data_storage/lesson07_sql_vs_nosql_choosing_the_right_database.html": {
        "hook": "SQL and NoSQL databases solve different problems, and the best choice depends on how your data is shaped and how you need to query it.",
        "intro": "Think of SQL and NoSQL like choosing between a ruler and a tape measure. A ruler is rigid and precise \u2014 perfect for straight lines. A tape measure bends around curves and odd shapes. Neither tool is better; each fits a different job. <strong>Choosing</strong> between SQL and NoSQL follows the same logic.",
        "cards": [
            ("fa6-solid:shapes", "Data Shape", "Straight or curved \u2014 does your data fit a grid?", "Uniform rows suit the ruler; varied shapes suit the tape."),
            ("fa6-solid:magnifying-glass", "Query Patterns", "What questions will you ask most often?", "Complex joins favour the ruler; fast lookups favour the tape."),
            ("fa6-solid:chart-line", "Scale Needs", "One desk or an entire floor \u2014 how big will it grow?", "Vertical scaling fits the ruler; horizontal fits the tape."),
            ("fa6-solid:gauge-high", "Consistency vs Speed", "Precision or pace \u2014 which matters more?", "Strict accuracy suits the ruler; eventual consistency suits the tape."),
        ],
        "tip": "Many production systems use both \u2014 SQL for financial records that need strict consistency, NoSQL for user sessions that need speed.",
    },

    # ── Module 03 — API Data Integration ─────────────────────────────

    "mod_03_api_data_integration/lesson01_what_is_an_api.html": {
        "hook": "An API is a set of rules that lets one program send requests to another and get structured data back.",
        "intro": "Think of an API like a waiter in a restaurant. You do not walk into the kitchen to cook your own meal. Instead, you tell the waiter what you want, the waiter takes your order to the kitchen, and brings back exactly what you asked for. An <strong>API</strong> is that waiter, carrying your request to a server and returning its response.",
        "cards": [
            ("fa6-solid:paper-plane", "Request", "Your order \u2014 telling the waiter what you want", "A structured message you send to the server."),
            ("fa6-solid:reply", "Response", "The dish \u2014 what the kitchen sends back", "The data the server returns after processing your order."),
            ("fa6-solid:location-dot", "Endpoint", "The menu item \u2014 a specific dish you can order", "A URL that points to one resource or action on the server."),
            ("fa6-solid:code", "Data Format", "The plate \u2014 a standard shape the dish arrives on", "JSON or XML structure that every response follows."),
        ],
        "tip": "If you have ever used a lookup formula in Excel that pulls values from another sheet, you have already used the same idea \u2014 asking one system for data from another.",
    },

    "mod_03_api_data_integration/lesson02_understanding_http_requests.html": {
        "hook": "HTTP requests are the standard messages your code sends to a web server to ask for data or tell it to do something.",
        "intro": "Think of HTTP requests like office memos. A <strong>GET</strong> memo asks for a report. A <strong>POST</strong> memo submits new information. A <strong>PUT</strong> memo updates an existing document. A <strong>DELETE</strong> memo asks to shred a file. Each memo type tells the office exactly what action you need.",
        "cards": [
            ("fa6-solid:download", "GET", "The request memo \u2014 send me this report", "Asks the server to return data without changing anything."),
            ("fa6-solid:upload", "POST", "The submission memo \u2014 here is new information", "Sends new data for the server to create or process."),
            ("fa6-solid:signal", "Status Codes", "The reply stamp \u2014 received, rejected, or not found", "A number like 200 or 404 that tells you what happened."),
            ("fa6-solid:id-badge", "Headers", "The memo header \u2014 who sent it and what format", "Metadata attached to every request and response."),
        ],
        "tip": "Every time you open a web page, your browser sends a GET request behind the scenes. Python\u2019s requests library does the same thing in code.",
    },

    "mod_03_api_data_integration/lesson03_using_the_python_requests_library.html": {
        "hook": "The requests library is Python\u2019s most popular tool for sending HTTP requests and handling responses with just a few lines of code.",
        "intro": "Think of the requests library like a phone with speed-dial buttons. Instead of dialling a long number every time, you press one button and the phone handles the connection. <strong>requests</strong> gives you simple functions \u2014 get, post, put \u2014 that handle all the networking details behind the scenes.",
        "cards": [
            ("fa6-solid:download", "Installing", "Adding the phone to your desk \u2014 a one-time setup", "One pip install command makes the library available."),
            ("fa6-solid:phone", "GET Requests", "Pressing speed-dial \u2014 calling the server in one line", "A single function call that fetches data from a URL."),
            ("fa6-solid:inbox", "Response Object", "The call log \u2014 status, duration, and transcript", "An object holding the status code, headers, and body."),
            ("fa6-solid:phone-slash", "Error Handling", "Busy signal \u2014 the call did not connect", "Checking status codes so your script handles failures."),
        ],
        "tip": "The requests library is not built into Python \u2014 you install it with pip. Most data engineering projects include it as a core dependency.",
    },

    "mod_03_api_data_integration/lesson04_working_with_json_data.html": {
        "hook": "JSON is a lightweight text format that uses keys and values to represent structured data, and it is the standard language of web APIs.",
        "intro": "Think of JSON like a set of labelled storage boxes. Each box has a label on the outside (the key) and something inside (the value). Some boxes hold single items; others hold smaller boxes nested inside. <strong>JSON</strong> follows the same logic, and Python can open, read, and repack these boxes easily.",
        "cards": [
            ("fa6-solid:tag", "Key-Value Pairs", "Label and contents \u2014 one name, one value", "Each label points to exactly one item inside its box."),
            ("fa6-solid:boxes-stacked", "Nested Objects", "Boxes inside boxes \u2014 layers of structure", "A box can contain smaller labelled boxes within it."),
            ("fa6-solid:list-ol", "Arrays", "A row of identical items \u2014 an ordered set", "A list of values stored under a single label."),
            ("fa6-solid:box-open", "Parsing", "Opening the box \u2014 turning text into Python data", "Converting a JSON string into dictionaries and lists."),
        ],
        "tip": "JSON looks almost identical to Python dictionaries. If you can read a dictionary, you can read JSON \u2014 the only difference is double quotes.",
    },

    "mod_03_api_data_integration/lesson05_parsing_api_responses.html": {
        "hook": "Parsing an API response means extracting the specific pieces of data you need from the structured result the server sends back.",
        "intro": "Think of an API response like a stack of morning post. Some envelopes hold invoices, others hold newsletters, and a few are junk. <strong>Parsing</strong> is opening each envelope, deciding what matters, and filing the important items. Python lets you sort through JSON responses the same way.",
        "cards": [
            ("fa6-solid:envelope-open", "Status Check", "The envelope flap \u2014 is it sealed or damaged?", "Verifying the response arrived intact before opening it."),
            ("fa6-solid:signs-post", "Navigating Keys", "The address label \u2014 which department gets this?", "Following nested keys to reach the data you want."),
            ("fa6-solid:scissors", "Extracting Fields", "Cutting out the cheque \u2014 taking only what you need", "Pulling specific values from a larger response."),
            ("fa6-solid:circle-question", "Handling Missing Data", "A missing page \u2014 the field is absent", "Using defaults or checks when expected keys are not there."),
        ],
        "tip": "Always check the status code before parsing. A 200 means the body contains your data; anything else may hold an error message.",
    },

    "mod_03_api_data_integration/lesson06_authentication_with_api_keys.html": {
        "hook": "An API key is a unique code that identifies your application and controls what data the server will share with you.",
        "intro": "Think of an API key like a building access card. The card proves you are allowed inside and determines which doors open for you. Without it, the lobby guard turns you away. An <strong>API key</strong> works the same way \u2014 your script sends it with every request so the server knows who is asking.",
        "cards": [
            ("fa6-solid:id-card", "API Key", "Your access card \u2014 proves who you are", "A string your script attaches to every request."),
            ("fa6-solid:right-left", "Headers vs Params", "Badge slot or sign-in sheet \u2014 two ways to present", "Keys travel in the header or as a URL parameter."),
            ("fa6-solid:lock", "Permissions", "Door access levels \u2014 some areas are restricted", "Different keys grant access to different endpoints."),
            ("fa6-solid:shield-halved", "Secret Management", "Keeping your card safe \u2014 never leave it on a desk", "Store keys in environment variables, never in your code."),
        ],
        "tip": "Treat API keys like passwords. If you accidentally commit one to Git, revoke it immediately and generate a new one.",
    },

    "mod_03_api_data_integration/lesson07_oauth_authentication.html": {
        "hook": "OAuth is an authentication protocol that lets a user grant your application limited access to their data without sharing their password.",
        "intro": "Think of OAuth like a hotel key card. The front desk (the provider) verifies your identity and issues a card that opens only your room for a limited time. You never see the master key, and the card expires at checkout. An <strong>OAuth token</strong> works the same way \u2014 temporary, scoped, and revocable.",
        "cards": [
            ("fa6-solid:key", "Access Token", "The room key card \u2014 opens specific doors", "A temporary credential your script sends with each request."),
            ("fa6-solid:door-open", "Scopes", "Which rooms the card unlocks \u2014 limited access", "Permissions that define what data the token can reach."),
            ("fa6-solid:rotate-right", "Refresh Token", "Extending your stay \u2014 getting a new card", "A long-lived token that fetches a fresh access token."),
            ("fa6-solid:arrows-spin", "OAuth Flow", "Check-in process \u2014 ID check, card issued, room accessed", "The handshake between your app, the user, and the provider."),
        ],
        "tip": "OAuth is more complex than API keys, but it is the standard for any service that handles user data \u2014 Google, GitHub, and Salesforce all use it.",
    },

    "mod_03_api_data_integration/lesson08_handling_pagination_in_apis.html": {
        "hook": "Pagination is how an API breaks a large result set into smaller pages so your code can fetch them one batch at a time.",
        "intro": "Think of a paginated API like a long book. The server does not hand you every page at once \u2014 it gives you one chapter, with a bookmark pointing to the next. You read the chapter, follow the bookmark, and repeat until you reach the end. <strong>Pagination</strong> is that chapter-by-chapter delivery.",
        "cards": [
            ("fa6-solid:file-lines", "Page Size", "Chapter length \u2014 how many records per page", "Controls how many items each batch contains."),
            ("fa6-solid:bookmark", "Offset", "The bookmark \u2014 where to start reading next", "A number telling the API which record to begin from."),
            ("fa6-solid:arrow-right", "Cursor-Based", "A page-turner \u2014 the server remembers your place", "A token the server returns so you can fetch the next batch."),
            ("fa6-solid:repeat", "Loop Pattern", "Reading to the end \u2014 chapter after chapter", "A while-loop that keeps fetching until no pages remain."),
        ],
        "tip": "Always check for an empty page or a missing \u2018next\u2019 link to stop your loop. An infinite loop against a live API can exhaust your rate limit in seconds.",
    },

    "mod_03_api_data_integration/lesson09_handling_api_rate_limits.html": {
        "hook": "Rate limits cap how many requests your code can send to an API in a given time window, protecting the server from overload.",
        "intro": "Think of rate limits like a busy coffee shop that serves only ten customers per minute. If you rush to the counter too fast, the barista asks you to wait. <strong>Rate limiting</strong> is that queue \u2014 the API tells your script to slow down so the server can keep up with everyone.",
        "cards": [
            ("fa6-solid:gauge-high", "Rate Headers", "The counter display \u2014 how many orders remain", "Response headers that report your remaining requests."),
            ("fa6-solid:clock", "Retry-After", "The \u2018please wait\u2019 sign \u2014 when to try again", "A header telling your script when to come back."),
            ("fa6-solid:hourglass-start", "Backoff", "Stepping to the back of the queue \u2014 longer waits", "Increasing the delay between retries to avoid more rejections."),
            ("fa6-solid:hand", "Throttling", "Pacing yourself \u2014 ordering slowly on purpose", "Adding deliberate pauses between requests to stay under the limit."),
        ],
        "tip": "A 429 status code means \u2018too many requests\u2019. Always read the Retry-After header so your script waits the right amount of time.",
    },

    "mod_03_api_data_integration/lesson10_loading_api_data_into_pandas.html": {
        "hook": "Loading API data into Pandas means converting JSON responses into DataFrames so you can filter, group, and analyse the results.",
        "intro": "Think of API data like a bag of mixed ingredients. To follow a recipe, you pour each ingredient into its own measuring cup. <strong>Loading into Pandas</strong> does the same thing \u2014 it pours your JSON response into neat columns and rows so you can start analysing.",
        "cards": [
            ("fa6-solid:table", "json_normalize", "The measuring cups \u2014 one cup per ingredient", "Flattening nested JSON into tidy DataFrame columns."),
            ("fa6-solid:arrows-turn-to-dots", "Column Mapping", "Relabelling cups \u2014 clear names for each one", "Renaming or selecting only the columns you actually need."),
            ("fa6-solid:arrows-rotate", "Type Conversion", "Weighing vs measuring \u2014 numbers vs text", "Casting strings to dates, numbers, or categories."),
            ("fa6-solid:layer-group", "Append Pattern", "Combining batches \u2014 all cups into one bowl", "Appending pages of API data into a single DataFrame."),
        ],
        "tip": "If the JSON structure is flat, use pd.DataFrame() directly. Use pd.json_normalize() only when the response contains nested objects.",
    },

    "mod_03_api_data_integration/lesson11_saving_api_data_to_databases.html": {
        "hook": "Saving API data to a database means writing the records you fetched into a permanent store so they survive beyond your script\u2019s runtime.",
        "intro": "Think of your API data like meeting notes scribbled on a notepad. If you do not file them, they disappear when you toss the pad. <strong>Saving to a database</strong> is the filing step \u2014 you open the right drawer, slot the notes in, and close it. Python\u2019s SQLAlchemy and Pandas make that filing almost automatic.",
        "cards": [
            ("fa6-solid:plug", "Connection String", "The key to the filing room \u2014 address and door code", "A URI that tells Python where the database lives."),
            ("fa6-solid:table-cells", "Table Mapping", "The folder labels \u2014 which drawer gets which notes", "Matching DataFrame columns to database table columns."),
            ("fa6-solid:file-import", "Insert Modes", "Replace or append \u2014 dump old notes or add new ones", "Choosing whether to overwrite the table or add rows."),
            ("fa6-solid:arrows-rotate", "Upsert", "Update or insert \u2014 replace if it exists, add if not", "A merge strategy that avoids duplicate records."),
        ],
        "tip": "Use to_sql with if_exists='append' for most pipelines. \u2018replace\u2019 drops the table first \u2014 dangerous if other processes depend on it.",
    },

    "mod_03_api_data_integration/lesson12_building_an_api_data_pipeline.html": {
        "hook": "An API data pipeline is a sequence of automated steps that extracts data from APIs, transforms it, and loads it into a destination.",
        "intro": "Think of an API pipeline like a bottling factory. Liquid arrives from a supplier, machines filter and mix it, bottles are filled and labelled, and pallets ship to warehouses. Each station does one job automatically. A <strong>data pipeline</strong> chains extract, transform, and load stations together the same way.",
        "cards": [
            ("fa6-solid:faucet", "Extract", "The supply hose \u2014 pulling liquid from the source", "Fetching raw records from one or more API endpoints."),
            ("fa6-solid:flask", "Transform", "The mixing tank \u2014 blending and filtering", "Cleaning, reshaping, and enriching the raw data."),
            ("fa6-solid:box", "Load", "The labelling station \u2014 sealed and shelved", "Writing finished records to a database or file."),
            ("fa6-solid:gears", "Orchestration", "The factory control room \u2014 scheduling and monitoring", "Coordinating when each station runs and in what order."),
        ],
        "tip": "Keep each step in its own function. If the transform breaks, you can re-run it without re-fetching data from the API.",
    },

    "mod_03_api_data_integration/lesson13_real_world_api_integration_project.html": {
        "hook": "A real-world API integration project combines every skill you have learned \u2014 authentication, pagination, error handling, and storage \u2014 into one working pipeline.",
        "intro": "Think of this project like assembling a flat-pack bookshelf. The box contains panels, screws, and instructions from earlier steps. You have practised each skill separately \u2014 now you follow the full instruction sheet from start to finish. A <strong>real-world project</strong> is that complete assembly.",
        "cards": [
            ("fa6-solid:clipboard-list", "Planning", "The instruction sheet \u2014 steps in order", "Mapping every stage before writing any code."),
            ("fa6-solid:screwdriver", "Data Extraction", "Opening the box \u2014 pulling out all the parts", "Connecting to the API, authenticating, and fetching pages."),
            ("fa6-solid:hammer", "Data Processing", "Fitting panels together \u2014 shaping raw parts", "Cleaning, joining, and validating the extracted data."),
            ("fa6-solid:truck-ramp-box", "Delivery", "The finished shelf on the wall \u2014 ready to use", "Loading results into a database or dashboard."),
        ],
        "tip": "Start by building the extract step and printing the first page. Add transform and load one at a time \u2014 debugging is easier when you add stages gradually.",
    },

    "mod_03_api_data_integration/lesson14_api_best_practices.html": {
        "hook": "API best practices are the habits that make your integration code reliable, secure, and easy to maintain over time.",
        "intro": "Think of best practices like keeping a workshop tidy. Tools go back on hooks, safety goggles stay on the bench, and every cable has a label. A messy workshop slows you down and causes accidents. <strong>API best practices</strong> keep your code clean, safe, and easy to fix when something breaks.",
        "cards": [
            ("fa6-solid:stopwatch", "Timeouts", "A timer on the workbench \u2014 stop after a set time", "Preventing your script from hanging on a slow server."),
            ("fa6-solid:clipboard-check", "Logging", "The job log \u2014 notes on every task completed", "Recording what happened so you can trace problems later."),
            ("fa6-solid:vault", "Secrets Management", "The locked toolbox \u2014 keys inside, not on the hook", "Storing credentials outside your code in secure locations."),
            ("fa6-solid:rotate", "Idempotency", "A reversible cut \u2014 no damage from a retry", "Designing requests so running them twice causes no harm."),
        ],
        "tip": "Add a timeout to every request call. A missing timeout means your script waits forever if the server stops responding.",
    },

    # ── Module 04 — Data Pipelines and Orchestration ─────────────────

    "mod_04_data_pipelines_and_orchestration/lesson01_what_is_a_data_pipeline.html": {
        "hook": "A data pipeline is a series of automated steps that move data from its source to a destination, transforming it along the way.",
        "intro": "Think of a data pipeline like a conveyor belt in a factory. Raw materials arrive at one end, each station cleans, sorts, or reshapes them, and finished goods come out the other end. A <strong>data pipeline</strong> is that belt, and each station is a step in your Python code.",
        "cards": [
            ("fa6-solid:right-to-bracket", "Source", "The loading dock \u2014 where raw materials arrive", "Where your pipeline picks up its raw data."),
            ("fa6-solid:list-check", "Steps", "Stations on the belt \u2014 each performs one task", "Individual functions that clean, filter, or reshape data."),
            ("fa6-solid:warehouse", "Destination", "The finished-goods warehouse \u2014 products ready", "The database or file that stores the processed results."),
            ("fa6-solid:clock-rotate-left", "Automation", "The on-switch \u2014 the belt runs without you", "Scheduling so the pipeline runs on its own."),
        ],
        "tip": "If you have ever set up an email rule that filters, labels, and moves messages automatically, you have already built a simple pipeline.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson02_etl_vs_elt.html": {
        "hook": "ETL transforms data before loading it into the target. ELT loads it first and transforms it inside the target.",
        "intro": "Think of ETL and ELT like two ways to unpack groceries. With <strong>ETL</strong>, you sort the bags on the kitchen counter \u2014 putting fruit in one pile, dairy in another \u2014 before loading everything into the fridge. With <strong>ELT</strong>, you load all the bags straight into the fridge and sort them on the shelves later.",
        "cards": [
            ("fa6-solid:arrow-right-to-bracket", "ETL Flow", "Sort then store \u2014 organise before the fridge", "Transform happens outside the target system."),
            ("fa6-solid:right-left", "ELT Flow", "Store then sort \u2014 dump bags in, organise later", "Transform happens inside the target using its own engine."),
            ("fa6-solid:code-branch", "When to Choose", "Counter space vs fridge space \u2014 where is room?", "Pick ETL when the target is small, ELT when it is powerful."),
            ("fa6-solid:shuffle", "Hybrid Approach", "Quick rinse first \u2014 then sort inside the fridge", "Some cleaning outside, heavier transforms inside."),
        ],
        "tip": "Cloud data warehouses like BigQuery and Snowflake are built for ELT \u2014 they have the compute power to transform data after loading.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson03_pipeline_design_patterns.html": {
        "hook": "Pipeline design patterns are reusable blueprints that solve common data-flow problems so you do not have to design from scratch.",
        "intro": "Think of design patterns like recipe templates in a cookbook. A \u2018stir-fry\u2019 template covers the basic steps \u2014 heat oil, add protein, add vegetables, season. You swap in different ingredients each time, but the method stays the same. <strong>Pipeline patterns</strong> give your code that same repeatable structure.",
        "cards": [
            ("fa6-solid:arrow-right-long", "Linear Pipeline", "A one-pot recipe \u2014 step A then B then C", "Each stage feeds directly into the next in a straight line."),
            ("fa6-solid:code-branch", "Fan-Out / Fan-In", "Prep stations \u2014 chop, dice, and mix in parallel", "Split data into parallel paths, then merge the results."),
            ("fa6-solid:filter-circle-xmark", "Delta (Incremental)", "Only cook what is new \u2014 skip dishes already served", "Process only the records that changed since the last run."),
            ("fa6-solid:rotate-right", "Retry / Dead-Letter", "A second chance \u2014 re-cook a failed dish", "Retry failures and quarantine records that keep failing."),
        ],
        "tip": "Start with a linear pipeline. Add fan-out or delta patterns only when you have a real performance or freshness requirement.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson04_working_with_large_data_files.html": {
        "hook": "Working with large data files means reading, processing, and writing datasets that are too big to fit in memory all at once.",
        "intro": "Think of a large file like a baguette that is too long for your plate. You cannot eat it in one bite, so you slice it into rounds, eat each slice, and move on to the next. <strong>Chunking</strong> and <strong>streaming</strong> let Python do the same with files that exceed your computer\u2019s memory.",
        "cards": [
            ("fa6-solid:scissors", "Chunked Reading", "Slicing the baguette \u2014 one round at a time", "Reading a set number of rows per pass through the file."),
            ("fa6-solid:forward", "Generators", "One slice at a time \u2014 no plate needed", "Yielding rows on demand so memory stays flat."),
            ("fa6-solid:file-zipper", "File Formats", "Thin-sliced vs thick \u2014 format affects size", "Parquet and compressed CSVs take up less space per slice."),
            ("fa6-solid:bars-progress", "Progress Tracking", "Counting slices eaten \u2014 how far along?", "Logging chunk numbers or using tqdm to track progress."),
        ],
        "tip": "Pass chunksize to pd.read_csv() and process each chunk inside a for-loop. You will use a fraction of the memory.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson05_data_validation_in_pipelines.html": {
        "hook": "Data validation checks that incoming records meet your rules before the pipeline processes or stores them.",
        "intro": "Think of data validation like airport security. Every passenger walks through a scanner before reaching the gate. If something in your bag breaks the rules, you are pulled aside. A <strong>validation step</strong> in your pipeline scans every record the same way \u2014 pass or flag.",
        "cards": [
            ("fa6-solid:clipboard-check", "Schema Checks", "The boarding pass scan \u2014 is the format correct?", "Verifying that column names and types match expectations."),
            ("fa6-solid:ruler", "Value Rules", "The size limit \u2014 bags must fit the overhead bin", "Checking that values fall within allowed ranges."),
            ("fa6-solid:ban", "Null Detection", "Empty pockets \u2014 items that should be there", "Flagging records with missing required fields."),
            ("fa6-solid:triangle-exclamation", "Quarantine", "Secondary screening \u2014 set aside for review", "Routing invalid records to a separate table for inspection."),
        ],
        "tip": "Validate early \u2014 ideally right after the extract step. Catching bad data before the transform saves hours of debugging later.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson09_scheduling_pipelines.html": {
        "hook": "Scheduling a pipeline means telling it when and how often to run automatically so you never have to start it by hand.",
        "intro": "Think of scheduling like setting an alarm clock. You choose the time, press set, and the alarm fires every morning without you lifting a finger. <strong>Scheduling</strong> a pipeline works the same way \u2014 you configure the trigger, and Python runs the job on time, every time.",
        "cards": [
            ("fa6-solid:calendar-day", "Cron Expressions", "The alarm time \u2014 minute, hour, day", "A short string that defines exactly when the job runs."),
            ("fa6-solid:clock", "Intervals", "Every 15 minutes \u2014 a repeating timer", "Running at fixed time gaps instead of fixed clock times."),
            ("fa6-solid:bell", "Triggers", "The alarm sound \u2014 what fires the run", "Events like a new file arrival or a database change."),
            ("fa6-solid:eye", "Monitoring", "Checking the alarm worked \u2014 did it ring?", "Logs and alerts confirming each scheduled run completed."),
        ],
        "tip": "Start with cron for time-based schedules. Switch to event triggers only when data arrives at unpredictable times.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson10_building_a_simple_python_pipeline.html": {
        "hook": "Building a simple Python pipeline means chaining extract, transform, and load functions together in a single script that runs end to end.",
        "intro": "Think of a simple pipeline like a sandwich-making station. One person slices bread, the next adds filling, and the last wraps the sandwich. Each station does one job, and the sandwich moves down the line. Your Python pipeline chains three functions \u2014 extract, transform, load \u2014 the same way.",
        "cards": [
            ("fa6-solid:bread-slice", "Extract Function", "Slicing the bread \u2014 pulling raw ingredients", "A function that reads data from the source."),
            ("fa6-solid:kitchen-set", "Transform Function", "Adding the filling \u2014 shaping the data", "A function that cleans, filters, or reshapes the input."),
            ("fa6-solid:box", "Load Function", "Wrapping the sandwich \u2014 delivering the result", "A function that writes finished data to its destination."),
            ("fa6-solid:play", "Main Runner", "The conveyor switch \u2014 each station in order", "A main block that calls extract, then transform, then load."),
        ],
        "tip": "Keep each function under 20 lines. If a function grows, split it \u2014 small functions are easier to test and debug.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson11_pipeline_project_automating_data_ingestion.html": {
        "hook": "Automating data ingestion means building a pipeline that fetches new data from external sources on a schedule without manual intervention.",
        "intro": "Think of automated ingestion like an automatic pet feeder. You fill the hopper once, set the timer, and food drops into the bowl at the right time every day. A <strong>data ingestion pipeline</strong> fills your database the same way \u2014 it fetches, cleans, and stores data on schedule.",
        "cards": [
            ("fa6-solid:sliders", "Source Config", "Filling the hopper \u2014 choosing what goes in", "Defining which API, file, or database to pull from."),
            ("fa6-solid:forward-step", "Incremental Fetch", "Only new kibble \u2014 skipping what is in the bowl", "Tracking a watermark so you only fetch new records."),
            ("fa6-solid:rotate-right", "Error Recovery", "Jam sensor \u2014 resetting when pellets get stuck", "Retrying or logging when a fetch fails mid-run."),
            ("fa6-solid:calendar-check", "Scheduling", "The timer dial \u2014 set it and forget it", "A cron job or scheduler that triggers each run automatically."),
        ],
        "tip": "Store the last-fetched timestamp in a file or database row. On the next run, pass it as a filter so you never re-process old data.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson12_pipeline_project_data_quality_checks.html": {
        "hook": "Data quality checks are automated tests inside your pipeline that verify records are complete, consistent, and within expected ranges.",
        "intro": "Think of data quality checks like the inspection station on a production line. An inspector measures each product, checks the label, and pulls anything that does not meet the standard. <strong>Quality checks</strong> in your pipeline do the same \u2014 they test every batch before it reaches the database.",
        "cards": [
            ("fa6-solid:list-check", "Completeness", "No missing parts \u2014 every field filled in", "Making sure no parts are missing from each product."),
            ("fa6-solid:equals", "Consistency", "Matching labels \u2014 dates in the same format", "Labels stamped the same way on every single product."),
            ("fa6-solid:ruler-combined", "Range Checks", "Within spec \u2014 measurements inside tolerance", "Measurements that fall between the minimum and maximum."),
            ("fa6-solid:bell", "Alerting", "The reject buzzer \u2014 notify when something fails", "A warning that sounds when inspection catches a defect."),
        ],
        "tip": "Add quality checks between transform and load. That way, bad data never reaches your production tables.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson13_pipeline_project_database_loading.html": {
        "hook": "Database loading is the final stage of a pipeline, where your cleaned and validated data is written into a database table.",
        "intro": "Think of database loading like stacking books on a library shelf. Each book has a catalogue number, and you slot it into the correct position. <strong>Loading</strong> takes your processed records and writes them into the right table, handling duplicates and conflicts along the way.",
        "cards": [
            ("fa6-solid:boxes-packing", "Bulk Insert", "An armload of books \u2014 placing many at once", "Writing thousands of rows in a single operation."),
            ("fa6-solid:arrows-rotate", "Upsert Logic", "Swap if it exists \u2014 add if it does not", "Updating existing rows and inserting new ones seamlessly."),
            ("fa6-solid:shield-halved", "Transaction Safety", "All or nothing \u2014 the cart rolls back if one breaks", "Wrapping the load so partial writes never stick."),
            ("fa6-solid:magnifying-glass-chart", "Post-Load Checks", "Shelf audit \u2014 counting books after stacking", "Verifying row counts and checksums after the load completes."),
        ],
        "tip": "Use if_exists='append' for incremental loads. Combine it with an upsert pattern to avoid duplicating rows.",
    },

    "mod_04_data_pipelines_and_orchestration/lesson14_production_pipeline_architecture.html": {
        "hook": "Production pipeline architecture is the blueprint for running data pipelines reliably in a live environment where failures, scale, and monitoring all matter.",
        "intro": "Think of production architecture like designing a building\u2019s plumbing. A single garden hose works for your back garden, but a high-rise needs pressure pumps, shut-off valves, and leak detectors on every floor. <strong>Production architecture</strong> adds those safeguards to your pipeline so it can run around the clock.",
        "cards": [
            ("fa6-solid:cubes", "Modular Design", "Separate pipe sections \u2014 swap one without draining all", "Each pipeline stage is an independent, replaceable module."),
            ("fa6-solid:chart-line", "Monitoring", "Pressure gauges \u2014 spotting drops before a burst", "Dashboards and alerts that track pipeline health."),
            ("fa6-solid:wrench", "Retry &amp; Recovery", "Shut-off valves \u2014 isolate a leak and re-route", "Automatic retries and fallback paths when a stage fails."),
            ("fa6-solid:up-right-and-down-left-from-center", "Scaling", "Thicker pipes \u2014 handling more flow as it grows", "Adding workers or resources when data volume increases."),
        ],
        "tip": "Start simple: a cron job, a log file, and an email alert. Add orchestration tools like Airflow only when you outgrow that setup.",
    },

    # ── Module 05 — Large Scale Data Processing ──────────────────────

    "mod_05_large_scale_data_processing/lesson02_memory_optimization.html": {
        "hook": "Memory optimisation means reducing how much of your computer\u2019s RAM your data uses so you can process larger datasets without running out.",
        "intro": "Think of your computer\u2019s memory like a suitcase. You have a fixed amount of space, and every item you pack takes up room. <strong>Memory optimisation</strong> is the art of rolling your clothes, using compression bags, and leaving unnecessary items at home so everything fits.",
        "cards": [
            ("fa6-solid:ruler-horizontal", "Data Types", "Folded vs flat \u2014 smaller types take less space", "Rolling your clothes tight to free up room in the suitcase."),
            ("fa6-solid:tags", "Categoricals", "Colour-coded packing cubes \u2014 labels not copies", "Replacing repeated items with compact colour-coded tags."),
            ("fa6-solid:scissors", "Column Pruning", "Leaving behind what you will not wear", "Packing only the outfits you actually plan to use."),
            ("fa6-solid:minimize", "In-Place Operations", "Repacking inside the case \u2014 no second bag", "Rearranging inside the same suitcase without opening another."),
        ],
        "tip": "Run df.info(memory_usage='deep') to see exactly how much RAM each column uses. Target the biggest columns first.",
    },

    "mod_05_large_scale_data_processing/lesson03_chunk_processing.html": {
        "hook": "Chunk processing means splitting a large dataset into smaller pieces and handling each piece one at a time.",
        "intro": "Think of chunk processing like washing dishes after a big dinner party. You cannot fit every plate in the sink at once, so you wash a stack, dry it, put it away, and grab the next stack. <strong>Chunking</strong> handles a massive file the same way \u2014 one manageable batch at a time.",
        "cards": [
            ("fa6-solid:layer-group", "Chunk Size", "The stack height \u2014 how many plates per wash", "A number that controls how many rows each batch holds."),
            ("fa6-solid:forward", "Iterator", "Grabbing the next stack \u2014 plate by plate", "A loop that yields one chunk at a time from the file."),
            ("fa6-solid:bucket", "Accumulator", "The drying rack \u2014 collecting results per batch", "A list or counter gathering output across all chunks."),
            ("fa6-solid:chart-area", "Memory Profile", "Checking the water level \u2014 sink not overflowing", "Monitoring RAM usage to confirm chunks stay within limits."),
        ],
        "tip": "Start with a chunk size of 10,000 rows and adjust. Smaller chunks use less memory; larger chunks run faster.",
    },

    "mod_05_large_scale_data_processing/lesson04_processing_millions_of_rows.html": {
        "hook": "Processing millions of rows means applying operations across very large tables efficiently, without waiting hours for results.",
        "intro": "Think of processing millions of rows like counting election ballots. Hand-counting takes weeks, but a machine scans thousands per minute by automating repetitive steps. <strong>Vectorised operations</strong> and <strong>parallel processing</strong> are the machines that let Python count millions of records fast.",
        "cards": [
            ("fa6-solid:bolt", "Vectorisation", "The scanner \u2014 processing a whole tray in one pass", "Applying one operation to an entire column at once."),
            ("fa6-solid:ban", "Avoiding Loops", "No hand-counting \u2014 skip the one-by-one approach", "Replacing Python for-loops with built-in array operations."),
            ("fa6-solid:filter", "Indexing", "Pre-sorted trays \u2014 ballots grouped by district", "Setting an index so lookups skip scanning every row."),
            ("fa6-solid:stopwatch", "Benchmarking", "The tally clock \u2014 timing each method", "Measuring how long each approach takes to find the fastest."),
        ],
        "tip": "A single vectorised Pandas operation can be 100\u00d7 faster than a Python for-loop over the same data.",
    },

    "mod_05_large_scale_data_processing/lesson05_columnar_storage.html": {
        "hook": "Columnar storage saves data by column instead of by row, making reads faster and files smaller when you only need a few columns.",
        "intro": "Think of columnar storage like a bead organiser with one compartment per colour. If you need red beads, you open one compartment instead of digging through a mixed jar. <strong>Columnar files</strong> store each column separately so Python reads only the compartments it needs.",
        "cards": [
            ("fa6-solid:table-columns", "Column Groups", "One compartment per colour \u2014 sorted by type", "Each column lives in its own section of the file."),
            ("fa6-solid:bolt", "Read Efficiency", "Grab one compartment \u2014 skip the rest", "Loading two columns from a hundred takes almost no extra time."),
            ("fa6-solid:minimize", "Compression Ratio", "Similar beads compress well \u2014 red with red", "Identical data types in a column compress better than mixed rows."),
            ("fa6-solid:pen", "Write Trade-off", "Sorting beads takes time \u2014 slower to organise", "Writes are slower because data must be grouped by column."),
        ],
        "tip": "Use columnar formats like Parquet whenever your analytics only query a subset of columns. The I/O savings add up fast.",
    },

    "mod_05_large_scale_data_processing/lesson06_parquet_files.html": {
        "hook": "Parquet is an open-source columnar file format designed for fast analytics and efficient storage of large datasets.",
        "intro": "Think of Parquet like a recipe binder with tabbed dividers. Each tab holds one type of recipe \u2014 starters, mains, desserts \u2014 and each section has a label on the spine. You flip straight to desserts without reading the whole book. <strong>Parquet</strong> indexes your data the same way.",
        "cards": [
            ("fa6-solid:layer-group", "Row Groups", "Binder sections \u2014 a block of recipes per tab", "Horizontal slices that divide the file into manageable blocks."),
            ("fa6-solid:grip-lines-vertical", "Column Chunks", "Columns within a tab \u2014 prep time and servings", "Each column inside a row group is stored and compressed separately."),
            ("fa6-solid:circle-info", "Footer Metadata", "The spine label \u2014 summary stats on the outside", "A small footer storing schema, row counts, and min/max values."),
            ("fa6-solid:forward-fast", "Predicate Pushdown", "Skipping tabs \u2014 jump past recipes you will not cook", "The reader skips row groups that cannot match your filter."),
        ],
        "tip": "Reading a Parquet file with Pandas is one line: pd.read_parquet('file.parquet'). Add the columns= parameter to load only what you need.",
    },

    "mod_05_large_scale_data_processing/lesson07_pyarrow_basics.html": {
        "hook": "PyArrow is a Python library that gives you high-speed tools for reading, writing, and processing columnar data formats like Parquet.",
        "intro": "Think of PyArrow like a power drill. A manual screwdriver (pure Python) gets the job done, but the drill drives screws in a fraction of the time. <strong>PyArrow</strong> runs at compiled speed under the hood, making file I/O and data conversion dramatically faster.",
        "cards": [
            ("fa6-solid:table", "Tables", "The workbench \u2014 a sturdy surface for your pieces", "PyArrow\u2019s main data structure, similar to a DataFrame."),
            ("fa6-solid:clipboard-list", "Schemas", "The blueprint \u2014 every screw, size, and type listed", "A typed definition of column names and data types."),
            ("fa6-solid:hard-drive", "File I/O", "Power-driving screws \u2014 fast reads and writes", "Reading and writing Parquet, CSV, and IPC files at speed."),
            ("fa6-solid:arrows-turn-to-dots", "Interop", "Switching drill bits \u2014 compatible with tools", "Converting seamlessly between PyArrow, Pandas, and NumPy."),
        ],
        "tip": "Pandas uses PyArrow behind the scenes when you call read_parquet(). Learning PyArrow directly gives you more control over memory and speed.",
    },

    "mod_05_large_scale_data_processing/lesson08_introduction_to_polars.html": {
        "hook": "Polars is a DataFrame library built for speed, with a syntax similar to Pandas but an engine that runs operations in parallel.",
        "intro": "Think of moving from Pandas to Polars like upgrading from a bicycle to an electric bike. You still pedal and steer the same way, but the motor does the heavy lifting on hills. <strong>Polars</strong> uses the same DataFrame concepts, but its engine handles the hard work much faster.",
        "cards": [
            ("fa6-solid:table", "DataFrame API", "The handlebars \u2014 familiar controls from Pandas", "Selecting, filtering, and grouping with a similar syntax."),
            ("fa6-solid:lightbulb", "Lazy Mode", "Route planner \u2014 mapping the ride before you start", "Building a query plan that Polars optimises before running."),
            ("fa6-solid:microchip", "Multi-Threading", "The electric motor \u2014 power behind the pedals", "Polars uses all CPU cores automatically."),
            ("fa6-solid:leaf", "Memory Efficiency", "Lightweight frame \u2014 goes further on less energy", "Uses Apache Arrow format, which avoids unnecessary copies."),
        ],
        "tip": "You do not need to replace Pandas everywhere. Use Polars when you hit a speed wall \u2014 it handles the same logic, just faster.",
    },

    "mod_05_large_scale_data_processing/lesson09_faster_dataframes_with_polars.html": {
        "hook": "Faster DataFrames with Polars means using expressions, lazy evaluation, and parallel execution to speed up operations that bottleneck in Pandas.",
        "intro": "Think of Polars like a team of chefs in one kitchen. Instead of one chef doing every task, each chef handles a different dish at the same time. <strong>Polars expressions</strong> are the recipe cards each chef follows, and <strong>lazy mode</strong> is the head chef planning who does what before anyone starts cooking.",
        "cards": [
            ("fa6-solid:receipt", "Expressions", "Recipe cards \u2014 clear instructions for each chef", "Compact operations that describe what to compute."),
            ("fa6-solid:brain", "Lazy Queries", "Menu planning \u2014 decide dishes before lighting the stove", "Building the full plan so Polars can optimise the order."),
            ("fa6-solid:users", "Parallel Execution", "Chefs working side by side \u2014 many tasks at once", "Splitting work across CPU cores automatically."),
            ("fa6-solid:filter", "Predicate Pushdown", "Shopping only what you need \u2014 fewer pantry trips", "Filtering rows early so less data flows through the pipeline."),
        ],
        "tip": "Call .lazy() at the start and .collect() at the end. Everything in between is a plan, not a computation, so Polars can remove unnecessary steps.",
    },

    "mod_05_large_scale_data_processing/lesson10_duckdb_for_analytics.html": {
        "hook": "DuckDB is an embedded analytics database that lets you run SQL queries directly on files and DataFrames without a server.",
        "intro": "Think of DuckDB like a pocket calculator. A mainframe (a full database server) is powerful but requires setup, administration, and a network. DuckDB fits inside your Python script and crunches numbers right where you are \u2014 no server needed.",
        "cards": [
            ("fa6-solid:microchip", "Embedded Engine", "Built into your pocket \u2014 no external hardware", "Runs inside your Python process with zero setup."),
            ("fa6-solid:file-code", "SQL on Files", "Calculate from the page \u2014 query CSVs and Parquets", "Point a SQL query at a file instead of loading it first."),
            ("fa6-solid:bridge", "DataFrame Bridge", "Plug into Pandas \u2014 share data without copying", "Query DataFrames as if they were database tables."),
            ("fa6-solid:bolt", "Columnar Engine", "Column at a time \u2014 fast analytical sums", "Processes data by column for speed on GROUP BY and joins."),
        ],
        "tip": "DuckDB is ideal for ad-hoc analysis on local files. When you outgrow it, the SQL you wrote translates easily to a cloud warehouse.",
    },

    "mod_05_large_scale_data_processing/lesson11_parallel_processing.html": {
        "hook": "Parallel processing means running multiple tasks at the same time across different CPU cores so your program finishes faster.",
        "intro": "Think of parallel processing like opening extra checkout lanes in a supermarket. One lane handles one customer at a time. Four lanes handle four customers simultaneously, clearing the queue four times faster. <strong>Parallel processing</strong> opens those extra lanes for your Python code.",
        "cards": [
            ("fa6-solid:cash-register", "Processes", "Extra checkout lanes \u2014 each with its own cashier", "Separate workers, each with their own memory space."),
            ("fa6-solid:people-arrows", "Threads", "Baggers helping one cashier \u2014 sharing the same till", "Lightweight workers sharing memory within one process."),
            ("fa6-solid:people-group", "Pool Pattern", "Opening lanes as needed \u2014 a pool of cashiers", "A manager that assigns tasks to a fixed set of workers."),
            ("fa6-solid:lock", "GIL Awareness", "One scanner at the register \u2014 turn-taking rule", "A Python lock that limits threads for CPU-heavy work."),
        ],
        "tip": "Use multiprocessing for CPU-heavy work like number-crunching. Use threading for I/O-heavy work like downloading files.",
    },

    "mod_05_large_scale_data_processing/lesson12_dask_basics.html": {
        "hook": "Dask is a Python library that scales Pandas, NumPy, and scikit-learn workflows to datasets larger than your computer\u2019s memory.",
        "intro": "Think of Dask like a team of accountants splitting a ledger. Each accountant takes a section, tallies it up, and they combine the results at the end. <strong>Dask</strong> splits your DataFrame into sections (partitions) and processes them in parallel.",
        "cards": [
            ("fa6-solid:puzzle-piece", "Partitions", "Ledger sections \u2014 each accountant gets a chunk", "Your DataFrame split into smaller pieces handled in parallel."),
            ("fa6-solid:diagram-project", "Lazy Graph", "The task list \u2014 written down but not started yet", "Dask records operations as a graph and runs them on demand."),
            ("fa6-solid:table", "Familiar API", "Same spreadsheet skills \u2014 just a bigger ledger", "Dask DataFrames use Pandas-like syntax you already know."),
            ("fa6-solid:play", "Compute", "Telling the team to start \u2014 triggering the work", "Calling .compute() to execute the queued operations."),
        ],
        "tip": "Dask is not a replacement for Pandas. Use Pandas for data that fits in memory. Switch to Dask when it does not.",
    },

    "mod_05_large_scale_data_processing/lesson13_performance_profiling.html": {
        "hook": "Performance profiling means measuring where your code spends its time and memory so you know exactly what to optimise.",
        "intro": "Think of profiling like a doctor\u2019s health check-up. Instead of guessing what hurts, the doctor runs tests \u2014 blood pressure, heart rate, X-rays \u2014 and pinpoints the problem. <strong>Profiling</strong> runs the same kind of tests on your code, showing you which functions are slow and which use too much memory.",
        "cards": [
            ("fa6-solid:stopwatch", "Time Profiling", "The heart-rate monitor \u2014 how long each beat takes", "Measuring how many seconds each function consumes."),
            ("fa6-solid:microchip", "Memory Profiling", "The blood test \u2014 tracking resource consumption", "Checking how much RAM each line allocates."),
            ("fa6-solid:magnifying-glass", "Bottleneck Detection", "The X-ray \u2014 seeing what is hidden inside", "Finding the one function that causes most of the delay."),
            ("fa6-solid:chart-column", "Before &amp; After", "Lab results comparison \u2014 did the treatment work?", "Re-profiling after a fix to confirm the improvement."),
        ],
        "tip": "Profile before optimising. Guessing which line is slow wastes time \u2014 the real bottleneck is often somewhere you did not expect.",
    },

    "mod_05_large_scale_data_processing/lesson14_real_large_data_project.html": {
        "hook": "A real large-data project combines chunking, columnar storage, parallel processing, and profiling into one end-to-end pipeline.",
        "intro": "Think of this project like running a warehouse. You receive shipments (extract), sort and pack items (transform), load pallets onto trucks (load), and check the manifest before departure (validate). Each skill you have learned is one station in this warehouse. Now you run them all together.",
        "cards": [
            ("fa6-solid:clipboard-list", "Project Plan", "The manifest \u2014 listing every station and its order", "Mapping the full pipeline before writing code."),
            ("fa6-solid:truck-ramp-box", "Data Ingestion", "Receiving dock \u2014 shipments into the warehouse", "Reading large files in chunks or from Parquet."),
            ("fa6-solid:gears", "Processing", "The sorting floor \u2014 packing and labelling", "Transforming and aggregating across millions of rows."),
            ("fa6-solid:truck-fast", "Delivery", "Loading dock \u2014 pallets onto the truck", "Writing results to a database or export file."),
        ],
        "tip": "Build the pipeline in stages. Get ingestion working first, then add transform, then load. Test each stage before connecting them.",
    },

    "mod_05_large_scale_data_processing/lesson15_performance_best_practices.html": {
        "hook": "Performance best practices are the habits and techniques that keep your data code fast, lean, and predictable as datasets grow.",
        "intro": "Think of performance best practices like maintaining a race car. Regular oil changes, tyre pressure checks, and weight reduction keep the car competitive lap after lap. <strong>Best practices</strong> in your code \u2014 choosing the right data types, avoiding copies, profiling regularly \u2014 keep your pipelines fast as data volumes grow.",
        "cards": [
            ("fa6-solid:toolbox", "Right Tool", "The right wrench \u2014 best library for the job", "Pandas, Polars, or DuckDB depending on your data size."),
            ("fa6-solid:clone", "Avoid Copies", "Stripping spare parts \u2014 no extra weight on the car", "Reducing unnecessary DataFrame copies to save memory."),
            ("fa6-solid:boxes-stacked", "Batch I/O", "Pit stops \u2014 fewer stops, more laps", "Reading and writing in bulk instead of row by row."),
            ("fa6-solid:gauge-simple-high", "Continuous Profiling", "Dashboard gauges \u2014 watching speed and temperature", "Profiling regularly so regressions are caught early."),
        ],
        "tip": "Most performance gains come from two things: vectorised operations instead of loops, and reading only the columns you need.",
    },

    # ── Module 06 — Automation and CI/CD ─────────────────────────────

    "mod_06_automation_and_ci_cd/lesson01_devops_concepts_for_data_analytics.html": {
        "hook": "DevOps for data means applying software engineering practices \u2014 version control, testing, and automation \u2014 to your data pipelines and analytics code.",
        "intro": "Think of DevOps like running a professional print shop. Amateur printing means one person does everything by hand \u2014 designing, proofing, and printing. A print shop automates the press, quality-checks every sheet, and keeps templates under version control so any operator can reproduce a job. <strong>DevOps</strong> brings that same discipline to your data work.",
        "cards": [
            ("fa6-solid:code-branch", "Version Control", "The template archive \u2014 every revision saved", "Tracking changes so you can roll back any mistake."),
            ("fa6-solid:vial", "Automated Testing", "The proof sheet \u2014 checking before the full run", "Scripts that verify your code works after every change."),
            ("fa6-solid:rotate", "CI/CD", "The automated press \u2014 proof, print, deliver", "A system that tests and deploys your code automatically."),
            ("fa6-solid:server", "Infrastructure as Code", "The press settings file \u2014 reproducible config", "Defining servers and environments in code, not by hand."),
        ],
        "tip": "You do not need to learn every DevOps tool. Start with Git for version control and a simple CI pipeline for automated testing.",
    },

    "mod_06_automation_and_ci_cd/lesson02_gitlab_ci_cd_overview.html": {
        "hook": "GitLab CI/CD is a built-in system that automatically tests, builds, and deploys your code every time you push a change.",
        "intro": "Think of GitLab CI/CD like an assembly line triggered by a doorbell. Every time you push code (ring the bell), the line fires up: a testing station checks your work, a build station packages it, and a deploy station ships it out. <strong>GitLab CI/CD</strong> is that assembly line, defined in a single YAML file.",
        "cards": [
            ("fa6-solid:file-lines", ".gitlab-ci.yml", "The assembly instructions \u2014 one file runs the line", "A YAML file that defines every stage and job."),
            ("fa6-solid:arrows-turn-right", "Stages", "Stations on the line \u2014 test, build, deploy", "Ordered groups of jobs that run one stage at a time."),
            ("fa6-solid:server", "Runners", "The assembly workers \u2014 machines that execute jobs", "Servers that pick up and run your pipeline\u2019s tasks."),
            ("fa6-solid:box-archive", "Artifacts", "The finished product \u2014 passed along the line", "Files produced by one job and available to the next."),
        ],
        "tip": "Start with a single \u2018test\u2019 stage that runs your unit tests. Add build and deploy stages as your project matures.",
    },

    "mod_06_automation_and_ci_cd/lesson03_scheduling_data_jobs.html": {
        "hook": "Scheduling data jobs means setting your scripts to run automatically at specific times or intervals, removing the need for manual execution.",
        "intro": "Think of scheduling like a garden sprinkler system. You set the timer to water the lawn at 6\u202fa.m. every day, and it runs whether you are home or not. <strong>Scheduling</strong> your data jobs works the same way \u2014 a timer triggers your Python script on a fixed timetable.",
        "cards": [
            ("fa6-solid:clock", "Cron Jobs", "The timer dial \u2014 minute, hour, day, month", "A system scheduler that fires scripts at set times."),
            ("fa6-solid:calendar-days", "Task Schedulers", "The smart controller \u2014 drag-and-drop scheduling", "Tools like Windows Task Scheduler or systemd timers."),
            ("fa6-solid:rotate-right", "Retry Logic", "Rain sensor \u2014 re-run if the first cycle fails", "Automatically restarting a job when it encounters an error."),
            ("fa6-solid:scroll", "Logging", "The watering log \u2014 recording every run", "Writing timestamps and outcomes so you know what happened."),
        ],
        "tip": "Always log the start time, end time, and row count of every scheduled job. When something breaks at 3\u202fa.m., the log is your only witness.",
    },

    "mod_06_automation_and_ci_cd/lesson05_deployment_workflow.html": {
        "hook": "A deployment workflow is the sequence of steps that moves your tested code from your laptop to a live server where it runs in production.",
        "intro": "Think of deployment like launching a ship from a dry dock. The ship is built and inspected on land (development), tested in a harbour basin (staging), and finally released into open water (production). A <strong>deployment workflow</strong> formalises those steps so every launch is safe and repeatable.",
        "cards": [
            ("fa6-solid:layer-group", "Environments", "Dry dock, harbour, open water \u2014 three zones", "Dev, staging, and production each with its own config."),
            ("fa6-solid:hammer", "Build Step", "Fitting the hull \u2014 assembling the parts", "Packaging your code and dependencies into a deployable unit."),
            ("fa6-solid:clipboard-check", "Approval Gate", "Harbour inspection \u2014 sign-off before launch", "A manual or automated check before promoting to production."),
            ("fa6-solid:rotate-left", "Rollback", "Tow back to dock \u2014 reverse if something leaks", "Returning to the previous version when production breaks."),
        ],
        "tip": "Never deploy directly to production. Always test in a staging environment first \u2014 it is your safety net before the real launch.",
    },
}

# ── Main ─────────────────────────────────────────────────────────────
assert len(LESSONS) == 56, f"Expected 56 lessons, got {len(LESSONS)}"

ok = fail = 0
for rel, data in LESSONS.items():
    path = BASE / rel
    if not path.exists():
        print(f"\u274c NOT FOUND  {rel}")
        fail += 1
        continue
    text = path.read_text(encoding="utf-8")
    new_sec = build_section(data["hook"], data["intro"], data["cards"], data["tip"])
    new_text, n = OV_RE.subn(new_sec, text, count=1)
    if n == 0:
        print(f"\u274c NO MATCH   {rel}")
        fail += 1
        continue
    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {rel}")
    ok += 1

print(f"\n{ok}/{ok + fail} overview sections rewritten")
