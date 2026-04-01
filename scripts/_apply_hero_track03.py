"""Rewrite <section class="hero-container"> for every lesson in track_03."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_03_data_engineering")
HERO_RE = re.compile(
    r'<section class="hero-container">.*?</section>',
    re.DOTALL,
)

PUB_DATE = "March 31, 2026"

DOT_COLORS = {
    "Beginner":     ("#22c55e", "#d1d5db", "#d1d5db"),
    "Intermediate": ("#22c55e", "#22c55e", "#d1d5db"),
    "Advanced":     ("#22c55e", "#22c55e", "#22c55e"),
}

MODULE_ICONS = {
    1: "fa6-solid:rocket",
    2: "fa6-solid:cubes",
    3: "fa6-solid:diagram-project",
    4: "fa6-solid:star",
    5: "fa6-solid:star",
    6: "fa6-solid:star",
}

# SVG hex — locked, never change
SVG_HEX = r'''<div class="hero-abstract-card" style="padding:0.25rem;opacity:0.75;">
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
        </div>'''


def build_hero(d):
    """Build the full <section class="hero-container">…</section> block."""
    dot1, dot2, dot3 = DOT_COLORS[d["difficulty"]]
    mod_icon = MODULE_ICONS[d["mod_num"]]

    return f'''<section class="hero-container">
  <div class="hero-dots"></div>
  <div class="hero-glow hero-glow-1"></div>
  <div class="hero-glow hero-glow-2"></div>
  <div class="hero-glow-line"></div>
  <div class="relative z-10 px-8 py-8 md:px-12 md:py-10">
    <div class="hero-split flex flex-col md:flex-row items-center gap-6 md:gap-10">

      <!-- LEFT COLUMN — Lesson info -->
      <div class="flex-1 min-w-0">

        <!-- Badge row -->
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="{mod_icon}"></span> Module {d["mod_num"]}
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="inline-flex items-center gap-1">
              <span style="width:6px;height:6px;border-radius:50%;background:{dot1};display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:{dot2};display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:{dot3};display:inline-block;"></span>
            </span>
            {d["difficulty"]}
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> {d["read_time"]}
          </span>
        </div>

        <!-- Lesson number label -->
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">{d["lesson_label"]}</p>

        <!-- Title -->
        <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">{d["title"]}</h1>

        <!-- Subtitle -->
        <p class="text-white/80 text-sm md:text-base leading-relaxed mt-4 mb-5 max-w-prose">{d["subtitle"]}</p>

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
            <span class="text-white/85 font-medium text-xs">{PUB_DATE}</span>
          </div>
        </div>

        <!-- Stat pills -->
        <div class="flex items-center gap-2 flex-wrap">
          <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span>
            <span class="font-extrabold">{d["goals"]}</span>
            <span class="font-semibold opacity-55">Goals</span>
          </a>
          <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span>
            <span class="font-extrabold">{d["examples"]}</span>
            <span class="font-semibold opacity-55">Examples</span>
          </a>
          <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span>
            <span class="font-extrabold">{d["exercises"]}</span>
            <span class="font-semibold opacity-55">Exercises</span>
          </a>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span>
            <span class="font-extrabold">{d["position"]}<span class="font-bold opacity-50">/{d["total"]}</span></span>
            <span class="font-semibold opacity-55">Progress</span>
          </span>
        </div>

      </div>

      <!-- RIGHT COLUMN — Hex graphic (locked — never edit) -->
      <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
        {SVG_HEX}
      </div>

    </div>
  </div>
</section>'''


# ── Lesson registry ──────────────────────────────────────────────
# Each entry: (filename, {metadata dict})
# Tab counts from audit; goals always 4

def L(title, subtitle, difficulty="Beginner", read_time="5 min read",
      lesson_label="Lesson 01", goals=4, examples=4, exercises=3,
      position=1, total=6, mod_num=1):
    return {
        "title": title, "subtitle": subtitle, "difficulty": difficulty,
        "read_time": read_time, "lesson_label": lesson_label,
        "goals": goals, "examples": examples, "exercises": exercises,
        "position": position, "total": total, "mod_num": mod_num,
    }


LESSONS = {
    # ── mod_01: Data Engineering Foundations (6 lessons) ──────────
    "mod_01_data_engineering_foundations/lesson01_what_is_data_engineering.html": L(
        "What Is Data Engineering?",
        "Discover what data engineers do — building the pipelines and infrastructure that move raw data from sources into systems analysts and scientists can use.",
        position=1, total=6, mod_num=1, examples=4, exercises=3,
    ),
    "mod_01_data_engineering_foundations/lesson02_etl_vs_elt.html": L(
        "ETL vs ELT",
        "Learn the difference between Extract-Transform-Load and Extract-Load-Transform, and understand when each approach fits your data workflow best.",
        position=2, total=6, mod_num=1, examples=4, exercises=3,
    ),
    "mod_01_data_engineering_foundations/lesson03_handling_large_datasets.html": L(
        "Handling Large Datasets",
        "Understand practical strategies for working with files too large to fit in memory, from chunked reading to selective column loading.",
        position=3, total=6, mod_num=1, examples=4, exercises=3,
    ),
    "mod_01_data_engineering_foundations/lesson05_parquet_efficient_storage.html": L(
        "Parquet &amp; Efficient Storage",
        "Learn how the Parquet columnar format compresses data and speeds up reads compared to CSV, and see how to convert between the two.",
        position=4, total=6, mod_num=1, examples=4, exercises=3,
    ),
    "mod_01_data_engineering_foundations/lesson06_intro_to_polars_optional.html": L(
        "Intro to Polars (Optional)",
        "See how the Polars library offers a faster, memory-efficient alternative to pandas for processing large datasets with a clean expression syntax.",
        position=5, total=6, mod_num=1, examples=4, exercises=3,
    ),
    "mod_01_data_engineering_foundations/lesson07_pipeline_design_concepts.html": L(
        "Pipeline Design Concepts",
        "Explore how to structure a data pipeline into clear stages — extract, transform, and load — so each step is modular, testable, and easy to maintain.",
        position=6, total=6, mod_num=1, examples=4, exercises=3,
    ),

    # ── mod_02: NoSQL and Modern Data Storage (7 lessons) ────────
    "mod_02_nosql_and_modern_data_storage/lesson01_what_is_nosql.html": L(
        "What is NoSQL?",
        "Discover what NoSQL databases are, how they differ from traditional relational databases, and when choosing a NoSQL approach makes sense for your data.",
        position=1, total=7, mod_num=2, examples=4, exercises=4,
        difficulty="Beginner",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson02_types_of_nosql_databases.html": L(
        "Types of NoSQL Databases",
        "Learn the four main NoSQL families — document, key-value, column-family, and graph — and understand which data shapes each one handles best.",
        position=2, total=7, mod_num=2, examples=4, exercises=4,
    ),
    "mod_02_nosql_and_modern_data_storage/lesson03_document_databases_mongodb.html": L(
        "Document Databases (MongoDB)",
        "Understand how MongoDB stores data as flexible JSON-like documents and learn to insert, query, and update records from Python.",
        position=3, total=7, mod_num=2, examples=4, exercises=4,
        difficulty="Intermediate",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson04_key_value_databases_redis.html": L(
        "Key-Value Databases (Redis)",
        "See how Redis stores data as simple key-value pairs in memory, making it ideal for caching, counters, and real-time lookups.",
        position=4, total=7, mod_num=2, examples=4, exercises=4,
        difficulty="Intermediate",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson05_column_family_databases_cassandra.html": L(
        "Column-Family Databases (Cassandra)",
        "Learn how Apache Cassandra organises data into column families for high-throughput writes and understand when this model fits your workload.",
        position=5, total=7, mod_num=2, examples=4, exercises=4,
        difficulty="Intermediate",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson06_graph_databases_neo4j.html": L(
        "Graph Databases (Neo4j)",
        "Discover how Neo4j models data as nodes and relationships, making it easy to explore connections like social networks and recommendation paths.",
        position=6, total=7, mod_num=2, examples=4, exercises=4,
        difficulty="Intermediate",
    ),
    "mod_02_nosql_and_modern_data_storage/lesson07_sql_vs_nosql_choosing_the_right_database.html": L(
        "SQL vs NoSQL: Choosing the Right Database",
        "Learn a practical decision framework for choosing between SQL and NoSQL databases based on your data structure, query patterns, and scale requirements.",
        position=7, total=7, mod_num=2, examples=4, exercises=4,
    ),

    # ── mod_03: API Data Integration (14 lessons) ────────────────
    "mod_03_api_data_integration/lesson01_what_is_an_api.html": L(
        "What is an API?",
        "Discover what APIs are, how they let programs talk to each other over the internet, and why they matter for pulling data into your Python projects.",
        position=1, total=14, mod_num=3, examples=2, exercises=3,
        read_time="4 min read",
    ),
    "mod_03_api_data_integration/lesson02_understanding_http_requests.html": L(
        "Understanding HTTP Requests",
        "Learn how web requests work — the methods, status codes, and headers your code sends and receives every time it talks to an API.",
        position=2, total=14, mod_num=3, examples=3, exercises=3,
    ),
    "mod_03_api_data_integration/lesson03_using_the_python_requests_library.html": L(
        "Using the Python requests Library",
        "See how to install and use the requests library to send GET and POST requests, handle responses, and start pulling live data from APIs.",
        position=3, total=14, mod_num=3, examples=4, exercises=3,
    ),
    "mod_03_api_data_integration/lesson04_working_with_json_data.html": L(
        "Working with JSON Data",
        "Understand the JSON format that most APIs return, and learn to parse, navigate, and extract the fields you need in Python.",
        position=4, total=14, mod_num=3, examples=4, exercises=3,
    ),
    "mod_03_api_data_integration/lesson05_parsing_api_responses.html": L(
        "Parsing API Responses",
        "Learn to inspect status codes, handle errors gracefully, and extract nested data from real API responses so your scripts stay robust.",
        position=5, total=14, mod_num=3, examples=4, exercises=3,
    ),
    "mod_03_api_data_integration/lesson06_authentication_with_api_keys.html": L(
        "Authentication with API Keys",
        "Discover how API keys work, where to store them securely, and how to include them in your Python requests to access protected endpoints.",
        position=6, total=14, mod_num=3, examples=3, exercises=3,
    ),
    "mod_03_api_data_integration/lesson07_oauth_authentication.html": L(
        "OAuth Authentication",
        "Understand the OAuth flow that services like Google and GitHub use, and learn to obtain and refresh access tokens from Python.",
        position=7, total=14, mod_num=3, examples=2, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_03_api_data_integration/lesson08_handling_pagination_in_apis.html": L(
        "Handling Pagination in APIs",
        "Learn how to loop through paginated API responses so you can collect complete datasets instead of just the first page of results.",
        position=8, total=14, mod_num=3, examples=3, exercises=3,
    ),
    "mod_03_api_data_integration/lesson09_handling_api_rate_limits.html": L(
        "Handling API Rate Limits",
        "Understand why APIs limit how many requests you can send, and learn to add delays and retries so your scripts stay within those limits.",
        position=9, total=14, mod_num=3, examples=3, exercises=3,
    ),
    "mod_03_api_data_integration/lesson10_loading_api_data_into_pandas.html": L(
        "Loading API Data into Pandas",
        "See how to take JSON data from an API response and load it straight into a pandas DataFrame for analysis, filtering, and export.",
        position=10, total=14, mod_num=3, examples=4, exercises=3,
    ),
    "mod_03_api_data_integration/lesson11_saving_api_data_to_databases.html": L(
        "Saving API Data to Databases",
        "Learn to store API data in a SQLite database so you can query it later without making repeated API calls.",
        position=11, total=14, mod_num=3, examples=4, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_03_api_data_integration/lesson12_building_an_api_data_pipeline.html": L(
        "Building an API Data Pipeline",
        "Combine everything you have learned into a complete pipeline that extracts data from an API, transforms it, and loads it into a database.",
        position=12, total=14, mod_num=3, examples=3, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_03_api_data_integration/lesson13_real_world_api_integration_project.html": L(
        "Real-World API Integration Project",
        "Apply your API skills end to end — fetch live data, handle errors, paginate results, and save everything to a database in one project.",
        position=13, total=14, mod_num=3, examples=0, exercises=3,
        difficulty="Intermediate", read_time="8 min read",
    ),
    "mod_03_api_data_integration/lesson14_api_best_practices.html": L(
        "API Best Practices",
        "Learn the habits that keep API integrations reliable in production — error handling, logging, credential management, and documentation.",
        position=14, total=14, mod_num=3, examples=0, exercises=3,
    ),

    # ── mod_04: Data Pipelines and Orchestration (11 lessons) ────
    "mod_04_data_pipelines_and_orchestration/lesson01_what_is_a_data_pipeline.html": L(
        "What is a Data Pipeline?",
        "Understand what a data pipeline is, why organisations need them, and how the extract-transform-load pattern moves data from source to destination.",
        position=1, total=11, mod_num=4, examples=0, exercises=3,
        difficulty="Beginner",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson02_etl_vs_elt.html": L(
        "ETL vs ELT",
        "Compare the two main pipeline architectures — transform before loading versus after — and learn which approach suits different data scenarios.",
        position=2, total=11, mod_num=4, examples=0, exercises=3,
    ),
    "mod_04_data_pipelines_and_orchestration/lesson03_pipeline_design_patterns.html": L(
        "Pipeline Design Patterns",
        "Explore common design patterns for data pipelines — batch versus streaming, fan-out, and idempotent steps — so you can pick the right structure.",
        position=3, total=11, mod_num=4, examples=0, exercises=3,
    ),
    "mod_04_data_pipelines_and_orchestration/lesson04_working_with_large_data_files.html": L(
        "Working with Large Data Files",
        "Learn practical techniques for processing files that do not fit in memory, including chunked reading, selective columns, and streaming writes.",
        position=4, total=11, mod_num=4, examples=0, exercises=3,
    ),
    "mod_04_data_pipelines_and_orchestration/lesson05_data_validation_in_pipelines.html": L(
        "Data Validation in Pipelines",
        "Discover how to add validation checks to your pipeline so bad data is caught early, before it reaches your database or dashboard.",
        position=5, total=11, mod_num=4, examples=0, exercises=3,
    ),
    "mod_04_data_pipelines_and_orchestration/lesson09_scheduling_pipelines.html": L(
        "Scheduling Pipelines",
        "Learn how to schedule your Python pipelines to run automatically on a timer using cron jobs and task schedulers.",
        position=6, total=11, mod_num=4, examples=0, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson10_building_a_simple_python_pipeline.html": L(
        "Building a Simple Python Pipeline",
        "Build a complete pipeline from scratch — extract data from a file, transform it with pandas, and load the results into a SQLite database.",
        position=7, total=11, mod_num=4, examples=0, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson11_pipeline_project_automating_data_ingestion.html": L(
        "Pipeline Project: Automating Data Ingestion",
        "Create an automated ingestion script that watches a folder for new CSV files, validates them, and loads each one into the database.",
        position=8, total=11, mod_num=4, examples=0, exercises=3,
        difficulty="Intermediate", read_time="8 min read",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson12_pipeline_project_data_quality_checks.html": L(
        "Pipeline Project: Data Quality Checks",
        "Add data quality checks to your pipeline that flag missing values, duplicate rows, and out-of-range numbers before data reaches the database.",
        position=9, total=11, mod_num=4, examples=0, exercises=3,
        difficulty="Intermediate", read_time="8 min read",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson13_pipeline_project_database_loading.html": L(
        "Pipeline Project: Database Loading",
        "Complete the pipeline by writing validated data into a production database with proper upsert logic, logging, and rollback handling.",
        position=10, total=11, mod_num=4, examples=0, exercises=3,
        difficulty="Intermediate", read_time="8 min read",
    ),
    "mod_04_data_pipelines_and_orchestration/lesson14_production_pipeline_architecture.html": L(
        "Production Pipeline Architecture",
        "Learn how production pipelines are structured with configuration files, environment variables, monitoring, and graceful error recovery.",
        position=11, total=11, mod_num=4, examples=0, exercises=3,
        difficulty="Intermediate",
    ),

    # ── mod_05: Large Scale Data Processing (14 lessons) ─────────
    "mod_05_large_scale_data_processing/lesson02_memory_optimization.html": L(
        "Memory Optimization",
        "Learn how to measure and reduce the memory footprint of your DataFrames by downcasting types, using categories, and dropping unneeded columns.",
        position=1, total=14, mod_num=5, examples=5, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson03_chunk_processing.html": L(
        "Chunk Processing",
        "Discover how to read and process large CSV files in manageable chunks so your scripts stay fast without running out of memory.",
        position=2, total=14, mod_num=5, examples=4, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson04_processing_millions_of_rows.html": L(
        "Processing Millions of Rows",
        "See how vectorised pandas operations handle millions of rows in seconds, and learn to avoid slow Python loops on large DataFrames.",
        position=3, total=14, mod_num=5, examples=4, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson05_columnar_storage.html": L(
        "Columnar Storage",
        "Understand why columnar file formats like Parquet load faster and use less disk space than CSV, and when to choose each format.",
        position=4, total=14, mod_num=5, examples=3, exercises=3,
    ),
    "mod_05_large_scale_data_processing/lesson06_parquet_files.html": L(
        "Parquet Files",
        "Learn to read, write, and inspect Parquet files with pandas and PyArrow, and see how columnar compression shrinks your data on disk.",
        position=5, total=14, mod_num=5, examples=4, exercises=2,
    ),
    "mod_05_large_scale_data_processing/lesson07_pyarrow_basics.html": L(
        "PyArrow Basics",
        "Discover the PyArrow library that powers Parquet support — learn to create Arrow tables, convert between pandas and Arrow, and read metadata.",
        position=6, total=14, mod_num=5, examples=4, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson08_introduction_to_polars.html": L(
        "Introduction to Polars",
        "Meet Polars — a modern DataFrame library built in Rust that offers a familiar API with dramatically faster performance than pandas on large data.",
        position=7, total=14, mod_num=5, examples=5, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson09_faster_dataframes_with_polars.html": L(
        "Faster DataFrames with Polars",
        "Go deeper with Polars — learn lazy evaluation, expression chaining, and multi-threaded execution to process millions of rows in seconds.",
        position=8, total=14, mod_num=5, examples=5, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson10_duckdb_for_analytics.html": L(
        "DuckDB for Analytics",
        "See how DuckDB lets you run SQL queries directly on CSV and Parquet files without a server, combining the speed of a database with the simplicity of a file.",
        position=9, total=14, mod_num=5, examples=5, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson11_parallel_processing.html": L(
        "Parallel Processing",
        "Learn to split work across multiple CPU cores using Python's multiprocessing and concurrent.futures so data-heavy tasks finish faster.",
        position=10, total=14, mod_num=5, examples=4, exercises=3,
        difficulty="Advanced",
    ),
    "mod_05_large_scale_data_processing/lesson12_dask_basics.html": L(
        "Dask Basics",
        "Discover how Dask extends the pandas API to datasets larger than memory by splitting work into parallel tasks across your machine.",
        position=11, total=14, mod_num=5, examples=5, exercises=3,
        difficulty="Advanced",
    ),
    "mod_05_large_scale_data_processing/lesson13_performance_profiling.html": L(
        "Performance Profiling",
        "Learn to find the slow parts of your code using timing, cProfile, and line-level profiling so you optimise where it actually matters.",
        position=12, total=14, mod_num=5, examples=4, exercises=3,
        difficulty="Intermediate",
    ),
    "mod_05_large_scale_data_processing/lesson14_real_large_data_project.html": L(
        "Real Large Data Project",
        "Apply everything from this module in a hands-on project — load, optimise, process, and export a multi-million-row dataset end to end.",
        position=13, total=14, mod_num=5, examples=5, exercises=3,
        difficulty="Advanced", read_time="10 min read",
    ),
    "mod_05_large_scale_data_processing/lesson15_performance_best_practices.html": L(
        "Performance Best Practices",
        "Review the key principles for keeping Python data scripts fast — from choosing the right file format to picking the right library for the job.",
        position=14, total=14, mod_num=5, examples=4, exercises=3,
        difficulty="Intermediate",
    ),

    # ── mod_06: Automation and CI/CD (4 lessons) ─────────────────
    "mod_06_automation_and_ci_cd/lesson01_devops_concepts_for_data_analytics.html": L(
        "DevOps Concepts for Data &amp; Analytics",
        "Understand the DevOps practices — version control, continuous integration, and automated testing — that keep data projects reliable and repeatable.",
        position=1, total=4, mod_num=6, examples=4, exercises=3,
    ),
    "mod_06_automation_and_ci_cd/lesson02_gitlab_ci_cd_overview.html": L(
        "GitLab CI/CD Overview",
        "Learn how GitLab CI/CD pipelines automate testing, building, and deploying your data scripts every time you push a code change.",
        position=2, total=4, mod_num=6, examples=4, exercises=3,
    ),
    "mod_06_automation_and_ci_cd/lesson03_scheduling_data_jobs.html": L(
        "Scheduling Data Jobs",
        "Discover how to schedule Python scripts to run automatically using cron, Windows Task Scheduler, and CI/CD pipeline triggers.",
        position=3, total=4, mod_num=6, examples=4, exercises=4,
        difficulty="Intermediate",
    ),
    "mod_06_automation_and_ci_cd/lesson05_deployment_workflow.html": L(
        "Deployment Workflow",
        "Learn a step-by-step deployment workflow — from local development through staging to production — so your data scripts ship safely every time.",
        position=4, total=4, mod_num=6, examples=4, exercises=4,
        difficulty="Intermediate",
    ),
}

# Add lesson_label to each based on filename
for path_key, meta in LESSONS.items():
    fname = pathlib.Path(path_key).name
    # Extract lesson number from filename
    m = re.search(r"lesson(\d+)", fname)
    if m:
        num = int(m.group(1))
        meta["lesson_label"] = f"Lesson {num:02d}"


def main():
    ok = 0
    total = 0
    for rel_path, meta in LESSONS.items():
        fpath = ROOT / rel_path
        if not fpath.exists():
            print(f"  SKIP  {rel_path} (not found)")
            continue
        total += 1
        html = fpath.read_text(encoding="utf-8")
        new_hero = build_hero(meta)
        new_html, count = HERO_RE.subn(new_hero, html, count=1)
        if count == 0:
            print(f"  WARN  {rel_path} (no hero-container)")
            continue
        fpath.write_text(new_html, encoding="utf-8")
        ok += 1
        print(f"  OK    {rel_path}")

    print(f"\n{ok}/{total} heroes rewritten")


if __name__ == "__main__":
    main()
