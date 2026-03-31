"""
Apply the standardised hero section to all track_02 lesson files.
Prompt: lesson-hero.prompt.md
"""
import glob, re, os

BASE = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics'

# ── Difficulty dot helpers ─────────────────────────────────────────────────
DOT = {
    'Beginner':     ['#22c55e', '#d1d5db', '#d1d5db'],
    'Intermediate': ['#22c55e', '#22c55e', '#d1d5db'],
    'Advanced':     ['#22c55e', '#22c55e', '#22c55e'],
}

def dot_span(color):
    return f'<span style="width:6px;height:6px;border-radius:50%;background:{color};display:inline-block;"></span>'

# ── Locked SVG hex graphic ─────────────────────────────────────────────────
SVG_HEX = r"""        <div class="hero-abstract-card" style="padding:0.25rem;opacity:0.75;">
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
        </div>"""

# ── Per-lesson metadata ────────────────────────────────────────────────────
# Key: filename stem (without .html)
# Values: (lesson_num_label, title, subtitle, difficulty, read_time, module_num, module_icon, position, total, pub_date)
LESSONS = {
    # mod_01 — Data Analysis with Pandas — Module 1
    'lesson01_introduction_to_pandas': (
        'Lesson 01', 'Introduction to Pandas',
        'Discover pandas, the most powerful Python library for data analysis, and learn how it transforms raw data files into structured, query-ready tables.',
        'Beginner', '8 min read', 1, 'fa6-solid:rocket', 1, 10, 'March 30, 2026'
    ),
    'lesson02_dataframes_explained': (
        'Lesson 02', 'DataFrames Explained',
        'Learn how pandas DataFrames organise data into rows and columns, making it easy to inspect, filter, and analyse information with just a few lines of Python.',
        'Beginner', '7 min read', 1, 'fa6-solid:rocket', 2, 10, 'March 30, 2026'
    ),
    'lesson03_reading_data_csv_excel': (
        'Lesson 03', 'Reading Data (CSV / Excel)',
        'See how to load real-world data files — CSVs and Excel spreadsheets — directly into Python using pandas, so you can start analysing them immediately.',
        'Beginner', '7 min read', 1, 'fa6-solid:rocket', 3, 10, 'March 30, 2026'
    ),
    'lesson04_selecting_columns': (
        'Lesson 04', 'Selecting Columns',
        'Understand how to choose exactly the columns you need from a DataFrame, reducing noise and focusing your analysis on the data that matters most.',
        'Beginner', '6 min read', 1, 'fa6-solid:rocket', 4, 10, 'March 30, 2026'
    ),
    'lesson05_filtering_rows': (
        'Lesson 05', 'Filtering Rows',
        'Learn how to filter rows in a DataFrame by writing conditions in Python, so you can isolate the exact records that match your analysis criteria.',
        'Beginner', '7 min read', 1, 'fa6-solid:rocket', 5, 10, 'March 30, 2026'
    ),
    'lesson06_creating_calculated_columns': (
        'Lesson 06', 'Creating Calculated Columns',
        'Discover how to add new columns to a DataFrame by applying calculations to existing data, so you can build the derived metrics your reports depend on.',
        'Beginner', '7 min read', 1, 'fa6-solid:rocket', 6, 10, 'March 30, 2026'
    ),
    'lesson07_aggregations_group_by': (
        'Lesson 07', 'Aggregations (GROUP BY)',
        'Learn how to summarise large datasets by grouping rows and applying aggregate functions like sum, mean, and count — the pandas equivalent of a pivot table.',
        'Intermediate', '8 min read', 1, 'fa6-solid:rocket', 7, 10, 'March 30, 2026'
    ),
    'lesson08_joining_data_merge': (
        'Lesson 08', 'Joining Data (Merge)',
        'See how to combine data from two or more DataFrames using merge, the pandas equivalent of a SQL JOIN, to build richer and more complete datasets.',
        'Intermediate', '9 min read', 1, 'fa6-solid:rocket', 8, 10, 'March 30, 2026'
    ),
    'lesson09_handling_missing_data': (
        'Lesson 09', 'Handling Missing Data',
        'Understand how pandas represents missing values, and learn the essential techniques for detecting, filling, and dropping them to keep your data clean.',
        'Intermediate', '7 min read', 1, 'fa6-solid:rocket', 9, 10, 'March 30, 2026'
    ),
    'lesson10_exporting_data': (
        'Lesson 10', 'Exporting Data',
        'Learn how to save your cleaned and analysed DataFrames to CSV, Excel, and other formats so you can share results and feed downstream workflows.',
        'Beginner', '6 min read', 1, 'fa6-solid:rocket', 10, 10, 'March 30, 2026'
    ),

    # mod_02 — Working with Data Sources — Module 2
    'lesson01_reading_csv_files': (
        'Lesson 01', 'Reading CSV Files',
        'Learn the full range of options for reading CSV files with pandas, including handling different delimiters, encodings, date columns, and large files safely.',
        'Intermediate', '7 min read', 2, 'fa6-solid:cubes', 1, 6, 'March 30, 2026'
    ),
    'lesson02_working_with_json_files': (
        'Lesson 02', 'Working with JSON Files',
        'Discover how to read, navigate, and flatten JSON data in Python so you can turn nested API responses and log files into clean, analysis-ready DataFrames.',
        'Intermediate', '7 min read', 2, 'fa6-solid:cubes', 2, 6, 'March 30, 2026'
    ),
    'lesson03_connecting_to_databases': (
        'Lesson 03', 'Connecting to Databases',
        'Learn how to connect Python directly to a SQL database using SQLAlchemy and pandas, so you can query live data without manually exporting it first.',
        'Intermediate', '8 min read', 2, 'fa6-solid:cubes', 3, 6, 'March 30, 2026'
    ),
    'lesson04_running_sql_in_python': (
        'Lesson 04', 'Running SQL in Python',
        'See how to execute SQL queries from a Python script and retrieve the results as a pandas DataFrame, combining the power of both tools in one workflow.',
        'Intermediate', '8 min read', 2, 'fa6-solid:cubes', 4, 6, 'March 30, 2026'
    ),
    'lesson05_writing_data_back_to_a_database': (
        'Lesson 05', 'Writing Data Back to a Database',
        'Understand how to write a pandas DataFrame back to a database table, automating the process of updating or creating tables with your processed analysis results.',
        'Intermediate', '8 min read', 2, 'fa6-solid:cubes', 5, 6, 'March 30, 2026'
    ),
    'lesson06_managing_credentials_env': (
        'Lesson 06', 'Managing Credentials (.env)',
        'Learn how to keep database passwords and API keys out of your code by using environment variables and dotenv files — a critical security habit for every analyst.',
        'Intermediate', '6 min read', 2, 'fa6-solid:cubes', 6, 6, 'March 30, 2026'
    ),

    # mod_03 — Python for Analysts — Module 3
    'lesson01_why_analysts_use_python': (
        'Lesson 01', 'Why Analysts Use Python',
        'Understand why data analysts are replacing Excel-only workflows with Python, and see the practical advantages Python brings to your everyday analysis tasks.',
        'Beginner', '7 min read', 3, 'fa6-solid:diagram-project', 1, 6, 'March 30, 2026'
    ),
    'lesson02_replacing_excel_workflows_with_python': (
        'Lesson 02', 'Replacing Excel Workflows with Python',
        'Discover how to recreate common Excel tasks — filtering, sorting, pivot tables, and VLOOKUP — using pandas so you can handle larger datasets and automate repetitive steps.',
        'Intermediate', '9 min read', 3, 'fa6-solid:diagram-project', 2, 6, 'March 30, 2026'
    ),
    'lesson03_using_python_with_sql_queries': (
        'Lesson 03', 'Using Python with SQL Queries',
        'Learn how to combine Python and SQL in a single script, running parameterised queries against a database and processing the results with pandas in one smooth pipeline.',
        'Intermediate', '8 min read', 3, 'fa6-solid:diagram-project', 3, 6, 'March 30, 2026'
    ),
    'lesson04_automating_repetitive_data_tasks': (
        'Lesson 04', 'Automating Repetitive Data Tasks',
        'See how to write Python scripts that automatically fetch, clean, and process data on a schedule, saving hours of manual copy-and-paste work every single week.',
        'Intermediate', '8 min read', 3, 'fa6-solid:diagram-project', 4, 6, 'March 30, 2026'
    ),
    'lesson05_building_a_simple_reporting_script': (
        'Lesson 05', 'Building a Simple Reporting Script',
        'Learn how to build a reusable Python script that pulls data, performs analysis, and writes a formatted output file ready to share with your stakeholders.',
        'Intermediate', '9 min read', 3, 'fa6-solid:diagram-project', 5, 6, 'March 30, 2026'
    ),
    'lesson06_automating_reports_end_to_end': (
        'Lesson 06', 'Automating Reports End-to-End',
        'Bring together everything from this module to build a complete automated reporting pipeline — from raw data source all the way to a finished, distributable report.',
        'Intermediate', '10 min read', 3, 'fa6-solid:diagram-project', 6, 6, 'March 30, 2026'
    ),

    # mod_04 — Handling Large Data — Module 4
    'lesson02_memory_optimization': (
        'Lesson 02', 'Memory Optimization',
        'Learn how to dramatically reduce the memory footprint of your DataFrames by choosing the right data types, so Python can handle far larger datasets than RAM allows.',
        'Advanced', '9 min read', 4, 'fa6-solid:star', 1, 6, 'March 30, 2026'
    ),
    'lesson03_chunk_processing': (
        'Lesson 03', 'Chunk Processing',
        'Discover how to process files that are too large to load at once by reading them in chunks, applying transformations to each piece, and combining the results efficiently.',
        'Advanced', '9 min read', 4, 'fa6-solid:star', 2, 6, 'March 30, 2026'
    ),
    'lesson04_processing_millions_of_rows': (
        'Lesson 04', 'Processing Millions of Rows',
        'See practical techniques for processing millions of rows efficiently in Python, including vectorised operations and avoiding the most common performance traps analysts hit.',
        'Advanced', '10 min read', 4, 'fa6-solid:star', 3, 6, 'March 30, 2026'
    ),
    'lesson05_columnar_storage': (
        'Lesson 05', 'Columnar Storage',
        'Understand why columnar storage formats are dramatically faster for analytical queries than row-based CSVs, and learn how to work with them directly in Python.',
        'Advanced', '9 min read', 4, 'fa6-solid:star', 4, 6, 'March 30, 2026'
    ),
    'lesson06_parquet_files': (
        'Lesson 06', 'Parquet Files',
        'Learn how to read and write Parquet files with pandas — the format of choice for large-scale analytical pipelines thanks to its built-in compression and speed.',
        'Advanced', '8 min read', 4, 'fa6-solid:star', 5, 6, 'March 30, 2026'
    ),
    'lesson13_performance_profiling': (
        'Lesson 13', 'Performance Profiling',
        'Discover how to measure where your pandas code is slow, identify bottlenecks using profiling tools, and apply targeted optimisations to get real speed improvements.',
        'Advanced', '9 min read', 4, 'fa6-solid:star', 6, 6, 'March 30, 2026'
    ),
}

# ── Hero template builder ──────────────────────────────────────────────────
def build_hero(lesson_num_label, title, subtitle, difficulty, read_time,
               module_num, module_icon, position, total, pub_date,
               goals, examples, exercises):
    dots = DOT[difficulty]
    d1, d2, d3 = dot_span(dots[0]), dot_span(dots[1]), dot_span(dots[2])
    pos_frac = f'{position}<span class="font-bold opacity-50">/{total}</span>'

    return f"""<section class="hero-container">
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
            <span class="iconify text-[10px]" data-icon="{module_icon}"></span> Module {module_num}
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="inline-flex items-center gap-1">
              {d1}
              {d2}
              {d3}
            </span>
            {difficulty}
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> {read_time}
          </span>
        </div>

        <!-- Lesson number label -->
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">{lesson_num_label}</p>

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
            <span class="font-extrabold">{pos_frac}</span>
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
</section>"""


# ── Process each file ──────────────────────────────────────────────────────
pattern = os.path.join(BASE, '**', '*.html')
files = sorted(glob.glob(pattern, recursive=True))
print(f'Processing {len(files)} files...\n')

for fp in files:
    stem = os.path.basename(fp).replace('.html', '')
    if stem not in LESSONS:
        print(f'⚠️  SKIP (no metadata): {os.path.basename(fp)}')
        continue

    meta = LESSONS[stem]
    lesson_num_label, title, subtitle, difficulty, read_time, mod_num, mod_icon, pos, total, pub_date = meta

    content = open(fp, encoding='utf-8').read()

    # Count tabs
    examples = content.count('class="ce-step ')
    exercises = content.count('class="pe-step ')
    goals = 4  # always 4 per spec

    new_hero = build_hero(
        lesson_num_label, title, subtitle, difficulty, read_time,
        mod_num, mod_icon, pos, total, pub_date,
        goals, examples, exercises
    )

    # Replace existing hero section
    new_content, n = re.subn(
        r'<section class="hero-container">.*?</section>',
        new_hero,
        content,
        count=1,
        flags=re.DOTALL
    )

    if n == 0:
        print(f'❌  {os.path.basename(fp)} — hero section not found!')
        continue

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'✅  {os.path.basename(fp)} — mod{mod_num} pos{pos}/{total} {difficulty} ce={examples} pe={exercises}')

print('\nDone.')
