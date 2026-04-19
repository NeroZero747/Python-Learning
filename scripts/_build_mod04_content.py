"""
Content sections for lessons 02-10 of mod_04_data_engineering.
Each lesson maps to a list of section HTML strings.
Imported by _build_mod04_lessons.py
"""
import html as _h
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _build_mod04_lessons import (
    section_wrap, obj_section, overview_section, _obj_card, _overview_card,
    _ki_card, _ce_tab_btn, _ce_panel, _code_block_a, _code_block_b,
    _code_block_b_lite, _mistake_card, _pe_tab_btn, _pe_panel,
    _recap_card, _quiz_tab_btn, _quiz_panel, COMPLETION_BANNER, e,
)


def _kc_section(tabs, panels):
    """Build the Key Concepts sidebar-tab section body."""
    tab_html = "\n".join(tabs)
    panel_html = "\n".join(panels)
    return f'''<div class="flex flex-col md:flex-row gap-0">
  <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
    <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full bg-[#CB187D] transition-all duration-300" style="height:68px;"></div>
    {tab_html}
  </div>
  <div class="flex-1 min-w-0 md:pl-5">
    {panel_html}
  </div>
</div>'''


def _kc_tab(idx, icon, label, active=False):
    act = " kc-tab-active" if active else ""
    num_cls = "bg-[#CB187D] text-white shadow-sm shadow-pink-200" if active else "bg-gray-100 text-gray-400"
    lbl_cls = "text-gray-900" if active else "text-gray-400"
    return f'''<button onclick="switchKcTab({idx})" class="kc-tab{act} group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 {num_cls}"><span class="iconify text-[11px]" data-icon="{icon}"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight {lbl_cls}">{label}</span>
</button>'''


def _kc_panel(idx, color, title, body_html, hidden=False):
    h = " hidden" if hidden else ""
    colors = {
        "pink": ("border-pink-100", "from-[#CB187D] via-pink-400 to-rose-300", "from-pink-50/60 to-white", "text-#CB187D"),
        "violet": ("border-violet-100", "from-violet-500 via-purple-400 to-fuchsia-300", "from-violet-50/60 to-white", "text-violet-500"),
        "blue": ("border-blue-100", "from-blue-500 via-cyan-400 to-teal-300", "from-blue-50/60 to-white", "text-blue-500"),
        "emerald": ("border-emerald-100", "from-emerald-500 via-teal-400 to-cyan-300", "from-emerald-50/60 to-white", "text-emerald-500"),
    }
    bc, grad, bg, tc = colors.get(color, colors["pink"])
    return f'''<div class="kc-panel kc-panel-anim{h}" data-color="{color}" role="tabpanel">
  <div class="rounded-2xl border {bc} overflow-hidden">
    <div class="h-1 bg-gradient-to-r {grad}"></div>
    <div class="bg-gradient-to-br {bg} p-5">
      <div class="mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">{title}</h3>
        <span class="text-[10px] font-bold {tc} uppercase tracking-widest">Definition</span>
      </div>
      <div class="space-y-3">
{body_html}
      </div>
    </div>
  </div>
</div>'''


# ══════════════════════════════════════════════════════════════════════
# LESSON 02 — ETL, ELT & Pipeline Thinking
# ══════════════════════════════════════════════════════════════════════
def _L02():
    s = []
    # OBJECTIVE
    s.append(section_wrap("objective", "fa6-solid:bullseye", "Lesson Objective", "The goal and expected outcome of this lesson",
        obj_section([
            _obj_card("fa6-solid:right-left", "Contrast ETL and ELT", "Explain the difference and identify when each pattern is appropriate."),
            _obj_card("fa6-solid:diagram-project", "Pipeline design principles", "Describe what makes a pipeline reliable, idempotent, and debuggable."),
            _obj_card("fa6-solid:code-branch", "Common patterns", "Recognize batch vs streaming and fan-out/merge architectures."),
            _obj_card("fa6-solid:cubes", "Write modular code", "Structure an ETL pipeline as separate, testable functions."),
        ], "This lesson introduces <strong>ETL and ELT</strong> so you can design a data pipeline on paper and explain your choices to a colleague.")))

    # OVERVIEW
    s.append(section_wrap("overview", "fa6-solid:binoculars", "Overview", "A high-level summary of the topic",
        overview_section(
            "A data pipeline is the automated replacement for the copy-paste-clean routine that every analyst does manually &mdash; except it runs on a schedule, handles any data volume, and never forgets a step.",
            "Think of an ETL pipeline like a car assembly line. Each station performs one specific job in a fixed sequence: the frame arrives, then the engine is fitted, then the bodywork, then the inspection. A <strong>data pipeline</strong> works the same way &mdash; raw data arrives, passes through each defined stage, and emerges as a clean, structured result ready to use.",
            "\n".join([
                _overview_card("fa6-solid:truck-ramp-box", "Extract", "Raw materials delivered to the factory floor", "Data is pulled from source systems such as APIs, databases, or flat files.", "pink"),
                _overview_card("fa6-solid:gears", "Transform", "Each station shapes the part to specification", "Raw data is cleaned, filtered, and reshaped into the format your destination requires.", "violet"),
                _overview_card("fa6-solid:warehouse", "Load", "Finished car exits onto the delivery lot", "The clean, structured data is written to its final destination &mdash; a warehouse, database, or file.", "blue"),
                _overview_card("fa6-solid:clipboard-check", "Validate", "Quality control inspector checks each vehicle", "Assertions and tests confirm the output meets expectations before it is used downstream.", "emerald"),
            ]),
            "Whether you choose ETL or ELT depends on one question: is it cheaper to clean data before or after you store it? Modern cloud warehouses have made &ldquo;after&rdquo; increasingly practical.")))

    # KEY IDEAS
    ki_body = "\n".join([
        _ki_card("pink", "fa6-solid:broom", "ETL: Clean Before You Store", "In ETL (Extract &rarr; Transform &rarr; Load), you clean and reshape data before it ever reaches the destination. This is best when your destination has strict schemas or when you must anonymize data before storage.", ["Strict schema", "Pre-processing", "Privacy"]),
        _ki_card("violet", "fa6-solid:database", "ELT: Store First, Transform Later", "In ELT (Extract &rarr; Load &rarr; Transform), you store raw data as-is first, then run transformations inside the warehouse using SQL or dbt. Analysts can own their own transformation logic.", ["Raw storage", "dbt", "Warehouse-native"]),
        _ki_card("blue", "fa6-solid:repeat", "Good Pipelines Are Idempotent", "An idempotent pipeline produces the same result no matter how many times you run it with the same input. This is critical for overnight jobs that might crash and re-run.", ["Idempotency", "Rerunnable", "Reliability"]),
    ])
    s.append(section_wrap("key-ideas", "fa6-solid:lightbulb", "Key Takeaways", "The most important ideas to remember", ki_body))

    # KEY CONCEPTS
    kc_body = _kc_section(
        [_kc_tab(0, "fa6-solid:right-left", "ETL vs ELT", True),
         _kc_tab(1, "fa6-solid:puzzle-piece", "Design Principles"),
         _kc_tab(2, "fa6-solid:clock", "Batch vs Streaming")],
        [_kc_panel(0, "pink", "ETL vs ELT",
            f'''<p class="text-xs text-gray-600 leading-relaxed"><strong>ETL</strong> transforms data before loading. <strong>ELT</strong> loads raw data first, then transforms it inside the warehouse.</p>
<p class="text-xs text-gray-600 leading-relaxed">Use ETL when your destination has a rigid schema or when PII must be masked before storage. Use ELT when your warehouse is powerful enough to transform data cheaply (BigQuery, Snowflake).</p>
{_code_block_b("Python", """# ETL pattern
raw   = extract("sales.csv")
clean = transform(raw)         # transform BEFORE load
load(clean, "warehouse_table")

# ELT pattern
raw = extract("sales.csv")
load_raw(raw, "raw_table")     # load first
transform_in_warehouse()        # transform AFTER load (SQL/dbt)""")}'''),
         _kc_panel(1, "violet", "Pipeline Design Principles",
            '''<p class="text-xs text-gray-600 leading-relaxed">Five principles make a pipeline production-ready:</p>
<div class="overflow-x-auto rounded-xl border border-gray-100">
<table class="w-full text-sm">
<thead><tr class="bg-gray-50"><th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs uppercase tracking-wider">Principle</th><th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs uppercase tracking-wider">Why It Matters</th></tr></thead>
<tbody>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-medium">Idempotency</td><td class="px-4 py-3 text-gray-600">Safe to re-run after a failure</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-medium">Modularity</td><td class="px-4 py-3 text-gray-600">Each function is testable alone</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-medium">Observability</td><td class="px-4 py-3 text-gray-600">Know where a failure occurred</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-medium">Fail-fast</td><td class="px-4 py-3 text-gray-600">Catch bad data early</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-medium">Backfill-ready</td><td class="px-4 py-3 text-gray-600">Can re-process historical data</td></tr>
</tbody></table></div>''', True),
         _kc_panel(2, "blue", "Batch vs Streaming",
            '''<p class="text-xs text-gray-600 leading-relaxed"><strong>Batch</strong> pipelines run on a schedule (e.g. nightly at 2 AM). <strong>Streaming</strong> pipelines process events continuously as they arrive.</p>
<p class="text-xs text-gray-600 leading-relaxed">For most analysts transitioning to data engineering, batch pipelines are the starting point. Streaming adds complexity (message queues like Kafka) and is only needed for real-time use cases like fraud detection or live dashboards.</p>''', True)])
    s.append(section_wrap("key-concepts", "fa6-solid:book-open", "Key Concepts", "Core terms and definitions for this topic", kc_body))

    # CODE EXAMPLES
    tabs = "\n".join([_ce_tab_btn(0, "Example 1", True), _ce_tab_btn(1, "Example 2"), _ce_tab_btn(2, "Example 3"), _ce_tab_btn(3, "Example 4")])
    panels = "\n".join([
        _ce_panel(0, "01", "Example 1 &mdash; Complete ETL Pipeline", "Beginner",
            "A modular ETL pipeline with separate extract, transform, and load functions.",
            _code_block_a("etl_pipeline.py", '''import pandas as pd
import sqlalchemy

def extract(filepath: str) -> pd.DataFrame:
    """Read raw sales data from a CSV file."""
    return pd.read_csv(filepath)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and reshape the raw sales data."""
    df = df.dropna(subset=["sale_date", "amount"])
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["amount"] = df["amount"].abs()
    df = df[df["amount"] > 0]
    df["year_month"] = df["sale_date"].dt.to_period("M")
    return df

def load(df: pd.DataFrame, table: str, engine) -> None:
    """Write clean data to the warehouse (idempotent)."""
    df.to_sql(table, con=engine, if_exists="replace", index=False)
    print(f"Loaded {len(df):,} rows into '{table}'.")

def run():
    engine = sqlalchemy.create_engine("sqlite:///warehouse.db")
    raw    = extract("sales_raw.csv")
    clean  = transform(raw)
    load(clean, "clean_sales", engine)

if __name__ == "__main__":
    run()''', terminal_output='Loaded 14,832 rows into \'clean_sales\'.')),
        _ce_panel(1, "02", "Example 2 &mdash; Idempotent Upsert", "Intermediate",
            "Instead of blindly appending, upsert by primary key so re-runs are safe.",
            _code_block_a("upsert_load.py", '''from sqlalchemy.dialects.postgresql import insert

def load_idempotent(df, table_name, engine, unique_key="order_id"):
    """Insert rows; update them if the key already exists."""
    with engine.connect() as conn:
        for _, row in df.iterrows():
            stmt = insert(table_name).values(**row)
            stmt = stmt.on_conflict_do_update(
                index_elements=[unique_key],
                set_=row.to_dict()
            )
            conn.execute(stmt)'''), True),
        _ce_panel(2, "03", "Example 3 &mdash; ELT Pattern", "Beginner",
            "Load raw data first, then transform inside the database with SQL.",
            _code_block_a("elt_pattern.py", '''# Step 1 (Python): load raw data as-is
raw_df.to_sql("raw_orders", con=engine, if_exists="replace", index=False)

# Step 2 (SQL inside warehouse): transform in the database
TRANSFORM_SQL = """
CREATE OR REPLACE TABLE clean_orders AS
SELECT
    order_id,
    CAST(order_date AS DATE)     AS order_date,
    ABS(amount)                   AS amount,
    UPPER(TRIM(region))           AS region
FROM raw_orders
WHERE amount IS NOT NULL
  AND order_id IS NOT NULL
"""
with engine.connect() as conn:
    conn.execute(TRANSFORM_SQL)'''), True),
        _ce_panel(3, "04", "Example 4 &mdash; Pipeline Logging", "Beginner",
            "Add structured logging so you know exactly what happened at each step.",
            _code_block_a("logged_pipeline.py", '''import logging, time

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

def run():
    log.info("Pipeline started")
    t0 = time.perf_counter()

    raw = extract("sales_raw.csv")
    log.info(f"Extracted {len(raw):,} rows")

    clean = transform(raw)
    log.info(f"Transformed: {len(clean):,} rows retained")

    load(clean, "clean_sales", engine)
    log.info(f"Pipeline complete in {time.perf_counter()-t0:.1f}s")'''), True),
    ])
    ce_body = f'''<div class="flex items-center gap-2 mb-6" role="tablist">{tabs}</div>
{panels}'''
    s.append(section_wrap("code-examples", "fa6-solid:code", "Code Examples", "Hands-on code snippets to explore the concepts", ce_body))

    # PRACTICE
    pe_tabs = "\n".join([_pe_tab_btn(0, "Exercise 1", True), _pe_tab_btn(1, "Exercise 2"), _pe_tab_btn(2, "Exercise 3")])
    pe_panels = "\n".join([
        _pe_panel(0, "01", "Exercise 1 &mdash; Complete the Transform", "Fill in the missing transform steps to clean an orders DataFrame.",
            _code_block_a("exercise_01.py", '''import pandas as pd

def transform(df):
    # TODO: drop rows where 'customer_id' or 'total' is null
    # TODO: convert 'order_date' to datetime
    # TODO: filter out rows where total < 0
    # TODO: add a column 'tax' = total * 0.1
    return df

raw = pd.read_csv("orders.csv")
clean = transform(raw)
print(clean.head())''')),
        _pe_panel(1, "02", "Exercise 2 &mdash; Classify the Pattern",
            "For each scenario, decide: ETL or ELT? 1) Sensitive health records that must be anonymized before storing. 2) Raw event logs pulled into BigQuery for analysts to model with dbt. 3) Destination is an Excel file with exactly 5 columns. 4) Tweets loaded into Snowflake, hashtags parsed with SQL later.",
            '<div class="rounded-xl p-4 border bg-amber-tip"><p class="text-sm text-gray-600"><strong>Answers:</strong> 1. ETL &mdash; 2. ELT &mdash; 3. ETL &mdash; 4. ELT</p></div>', True),
        _pe_panel(2, "03", "Exercise 3 &mdash; Make It Idempotent",
            "This pipeline appends rows every run. Fix it so re-runs are safe.",
            _code_block_a("exercise_03.py", '''def load(df, engine):
    df.to_sql("events", engine, if_exists="append", index=False)
    # HINT: What if_exists value makes this safe to re-run?
    # HINT: What check could you add first to avoid duplicates?'''), True),
    ])
    pe_body = f'''<div class="flex items-center gap-2 mb-6" role="tablist">{pe_tabs}</div>
{pe_panels}'''
    s.append(section_wrap("practice", "fa6-solid:pencil", "Practice Exercises", "Hands-on tasks to reinforce the concepts", pe_body))

    # MISTAKES
    mk_body = "\n".join([
        _mistake_card(1, "Appending without deduplication",
            'df.to_sql("sales", con=engine, if_exists="append")',
            'df.to_sql("sales", con=engine, if_exists="replace")',
            "Running with <code>append</code> twice doubles every row. Use <code>replace</code> for full refresh or an upsert for incremental loads."),
        _mistake_card(2, "All logic in one giant function",
            '''def run_everything():
    df = pd.read_csv("data.csv")
    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"])
    df.to_sql("table", engine, if_exists="replace")''',
            '''raw   = extract("data.csv")
clean = transform(raw)
load(clean, "table", engine)''',
            "Separate functions are independently testable and make debugging far easier."),
        _mistake_card(3, "Choosing ETL vs ELT without considering your warehouse",
            '# Using ETL with Python transforms\n# when BigQuery could do it 10x faster',
            '# ELT: load raw, transform in BigQuery\nraw_df.to_sql("raw", engine, if_exists="replace")\n# Then run SQL transforms in the warehouse',
            "If you are working with BigQuery or Snowflake, ELT is almost always faster and cheaper."),
    ])
    s.append(section_wrap("mistakes", "fa6-solid:triangle-exclamation", "Common Mistakes", "Pitfalls to avoid when working with pipelines", mk_body))

    # RECAP
    recap_body = f'''<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
{_recap_card(1, "<strong>ETL</strong> transforms data before loading &mdash; ideal when your destination has a rigid schema or data must be cleaned before storage.")}
{_recap_card(2, "<strong>ELT</strong> loads raw data first and transforms inside the warehouse &mdash; ideal for modern cloud platforms where SQL transformations are fast.")}
{_recap_card(3, "<strong>Idempotency</strong> means running the pipeline multiple times produces the same result &mdash; essential for overnight jobs that might need to re-run.")}
{_recap_card(4, "<strong>Modularity</strong> &mdash; splitting extract, transform, and load into separate functions &mdash; makes every step independently testable and debuggable.")}
</div>
{COMPLETION_BANNER}'''
    s.append(section_wrap("recap", "fa6-solid:list-check", "Lesson Recap", "Summary of what you learned", recap_body))

    # QUIZ
    qz_tabs = "\n".join([_quiz_tab_btn(0, "Question 1", True), _quiz_tab_btn(1, "Question 2"), _quiz_tab_btn(2, "Question 3")])
    qz_panels = "\n".join([
        _quiz_panel(0, "Your company uses BigQuery and wants analysts to write their own SQL transformations. Which pattern fits best?", "ELT", "ETL", True),
        _quiz_panel(1, "What does &ldquo;idempotent&rdquo; mean for a data pipeline?", "Same input always produces the same output", "It runs faster each time", True, True),
        _quiz_panel(2, "True or False: ETL always requires more Python code than ELT.", "False", "True", True, True),
    ])
    qz_body = f'''<div class="flex items-center gap-2 mb-6" role="tablist">{qz_tabs}</div>
{qz_panels}'''
    s.append(section_wrap("knowledge-check", "fa6-solid:brain", "Knowledge Check", "Test your understanding", qz_body))
    return s


# ══════════════════════════════════════════════════════════════════════
# LESSON 03 — Working with Large Datasets
# ══════════════════════════════════════════════════════════════════════
def _L03():
    s = []
    s.append(section_wrap("objective", "fa6-solid:bullseye", "Lesson Objective", "The goal and expected outcome of this lesson",
        obj_section([
            _obj_card("fa6-solid:memory", "Diagnose memory issues", "Explain why pandas runs out of memory on large files and identify root causes."),
            _obj_card("fa6-solid:layer-group", "Chunked reading", "Use chunksize to process files that are larger than available RAM."),
            _obj_card("fa6-solid:compress", "Dtype optimization", "Downcast numeric columns and convert strings to categoricals to cut memory by 50&ndash;80%."),
            _obj_card("fa6-solid:gauge-high", "Vectorized operations", "Replace Python loops with pandas vectorized methods for dramatic speed gains."),
        ], "This lesson teaches you to process a 5-million-row CSV on a laptop with only 8 GB of RAM.")))

    s.append(section_wrap("overview", "fa6-solid:binoculars", "Overview", "A high-level summary of the topic",
        overview_section(
            "When a dataset outgrows your laptop&rsquo;s memory, pandas throws a MemoryError and your pipeline dies. Data engineers solve this not by buying more RAM, but by working smarter with the data they already have.",
            "Think of loading large data like moving house with a small truck. You can&rsquo;t fit every box in one trip &mdash; so instead of trying to hire a bigger truck, you make multiple smaller trips. <strong>Chunk processing</strong> works exactly the same way.",
            "\n".join([
                _overview_card("fa6-solid:truck-moving", "Chunked Reading", "Multiple smaller trips instead of one giant one", "Read a manageable slice of the file, process it, save the result, then read the next slice.", "pink"),
                _overview_card("fa6-solid:minimize", "Dtype Downcasting", "Smaller boxes &mdash; why use a wardrobe box for one shirt?", "A column with values 0&ndash;100 doesn&rsquo;t need 8 bytes. Downcast int64 to int8 and save 87% memory.", "violet"),
                _overview_card("fa6-solid:tags", "Categorical Columns", "Labeling boxes by room &mdash; one label covers hundreds", "Convert low-cardinality text columns to category dtype to eliminate string duplication.", "blue"),
                _overview_card("fa6-solid:forward-fast", "Vectorized Operations", "Using a dolly instead of carrying each box by hand", "Pandas vectorized operations run in compiled C and are 10&ndash;100&times; faster than Python loops.", "emerald"),
            ]),
            "The average analyst uses 5&ndash;10&times; more memory than needed because pandas defaults to the largest possible dtype for every column. Fixing this is free.")))

    ki_body = "\n".join([
        _ki_card("pink", "fa6-solid:weight-hanging", "Pandas Defaults Are Memory-Hungry", "By default, pandas loads every integer as int64 (8 bytes) and every text column as object (50+ bytes per value). A column with values 0&ndash;100 fits in int8 (1 byte). Downcasting alone often halves the memory footprint.", ["Dtype", "int8/int16", "float32"]),
        _ki_card("violet", "fa6-solid:boxes-stacked", "Chunk Processing Fits Any File", "pd.read_csv(&quot;file.csv&quot;, chunksize=100_000) returns an iterator. Each iteration gives you 100,000 rows. Aggregate the results across chunks and you can handle files of any size on any machine.", ["chunksize", "Iterator", "Aggregation"]),
        _ki_card("blue", "fa6-solid:clone", "Categoricals Eliminate String Duplication", "When a text column has 5 unique values across 10 million rows, converting to category dtype stores 5 strings plus integers &mdash; reducing memory by 90%+.", ["category", "Low cardinality", "Deduplication"]),
    ])
    s.append(section_wrap("key-ideas", "fa6-solid:lightbulb", "Key Takeaways", "The most important ideas to remember", ki_body))

    kc_body = _kc_section(
        [_kc_tab(0, "fa6-solid:memory", "memory_usage()", True),
         _kc_tab(1, "fa6-solid:compress", "Dtype Rules"),
         _kc_tab(2, "fa6-solid:layer-group", "Chunked Reading")],
        [_kc_panel(0, "pink", "memory_usage() &mdash; Understand Your Data",
            f'''<p class="text-xs text-gray-600 leading-relaxed">Use <code>df.memory_usage(deep=True)</code> to see how much memory each column consumes.</p>
{_code_block_b("Python", """import pandas as pd

df = pd.read_csv("large_sales.csv")
print(df.memory_usage(deep=True))

total_mb = df.memory_usage(deep=True).sum() / 1024**2
print(f"DataFrame uses {total_mb:.1f} MB")""")}'''),
         _kc_panel(1, "violet", "Dtype Downcasting Rules",
            '''<div class="overflow-x-auto rounded-xl border border-gray-100">
<table class="w-full text-sm">
<thead><tr class="bg-gray-50"><th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs">Current</th><th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs">Downcast To</th><th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs">Saving</th></tr></thead>
<tbody>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600">int64 (max 127)</td><td class="px-4 py-3 text-gray-600">int8</td><td class="px-4 py-3 text-gray-600 font-bold text-emerald-600">87.5%</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600">int64 (max 32,767)</td><td class="px-4 py-3 text-gray-600">int16</td><td class="px-4 py-3 text-gray-600 font-bold text-emerald-600">75%</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600">float64</td><td class="px-4 py-3 text-gray-600">float32</td><td class="px-4 py-3 text-gray-600 font-bold text-emerald-600">50%</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600">object (low cardinality)</td><td class="px-4 py-3 text-gray-600">category</td><td class="px-4 py-3 text-gray-600 font-bold text-emerald-600">70&ndash;95%</td></tr>
</tbody></table></div>''', True),
         _kc_panel(2, "blue", "Chunked Reading Pattern",
            f'''<p class="text-xs text-gray-600 leading-relaxed">Process a large CSV in chunks without loading it all at once. Aggregate partial results, then combine them at the end.</p>
{_code_block_b("Python", """results = []
for chunk in pd.read_csv("sales.csv", chunksize=100_000):
    summary = chunk.groupby("region")["amount"].sum()
    results.append(summary)

final = pd.concat(results).groupby(level=0).sum()""")}''', True)])
    s.append(section_wrap("key-concepts", "fa6-solid:book-open", "Key Concepts", "Core terms and definitions for this topic", kc_body))

    # CODE EXAMPLES
    tabs = "\n".join([_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)])
    panels = "\n".join([
        _ce_panel(0, "01", "Optimized Dtypes Upfront", "Beginner", "Define dtypes before reading so pandas skips inference.",
            _code_block_a("optimized_read.py", '''import pandas as pd

dtypes = {
    "order_id": "int32", "customer_id": "int32",
    "amount": "float32", "region": "category", "status": "category",
}
df = pd.read_csv("orders.csv", dtype=dtypes,
    usecols=["order_id","customer_id","amount","region","status"],
    parse_dates=["order_date"])
print(f"{df.memory_usage(deep=True).sum()/1024**2:.0f} MB")''', terminal_output="Before: 412 MB  →  After: 54 MB")),
        _ce_panel(1, "02", "Auto-Downcast DataFrame", "Beginner", "Automatically downcast integers, floats, and categorize low-cardinality strings.",
            _code_block_a("auto_downcast.py", '''def optimize_dtypes(df):
    for col in df.select_dtypes(include=["int64","int32"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes(include=["float64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="float")
    for col in df.select_dtypes(include=["object"]).columns:
        if df[col].nunique() / len(df) < 0.05:
            df[col] = df[col].astype("category")
    return df

df = optimize_dtypes(df)'''), True),
        _ce_panel(2, "03", "Chunked Aggregation", "Intermediate", "Sum sales by region across a 10-million-row file without loading it all at once.",
            _code_block_a("chunked_agg.py", '''import pandas as pd

totals = {}
for i, chunk in enumerate(pd.read_csv("sales_10m.csv", chunksize=250_000)):
    chunk["amount"] = chunk["amount"].astype("float32")
    chunk["region"] = chunk["region"].astype("category")
    for region, total in chunk.groupby("region")["amount"].sum().items():
        totals[region] = totals.get(region, 0) + total
    print(f"Chunk {i+1} processed ({(i+1)*250_000:,} rows)")

for region, total in sorted(totals.items()):
    print(f"{region}: ${total:,.2f}")''', terminal_output="Chunk 40 processed (10,000,000 rows)\nEMEA: $3,218,492.75\nAPAC: $2,891,003.00\nAMER: $4,105,228.50"), True),
        _ce_panel(3, "04", "Read Only Needed Columns", "Beginner", "Loading all 50 columns when you only need 4 wastes 92% of the memory.",
            _code_block_a("select_cols.py", '''df = pd.read_csv(
    "big_report.csv",
    usecols=["order_id", "date", "amount", "region"]
)'''), True),
    ])
    ce_body = f'''<div class="flex items-center gap-2 mb-6" role="tablist">{tabs}</div>\n{panels}'''
    s.append(section_wrap("code-examples", "fa6-solid:code", "Code Examples", "Hands-on code snippets to explore the concepts", ce_body))

    # PRACTICE
    pe_tabs = "\n".join([_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)])
    pe_panels = "\n".join([
        _pe_panel(0, "01", "Measure the Impact", "Downcast dtypes and measure the memory savings before vs after.",
            _code_block_a("exercise_01.py", '''import pandas as pd
df = pd.read_csv("sample_data.csv")
before = df.memory_usage(deep=True).sum() / 1024**2
# TODO: downcast int64 → int32, float64 → float32
# TODO: convert object cols with < 10% unique to category
after = df.memory_usage(deep=True).sum() / 1024**2
print(f"Before: {before:.1f} MB | After: {after:.1f} MB")''')),
        _pe_panel(1, "02", "Fix the Loop", "Replace this slow iterrows() loop with a vectorized operation.",
            _code_block_a("exercise_02.py", '''import pandas as pd, numpy as np
df = pd.DataFrame({"score": np.random.randint(0, 100, 1_000_000)})
# SLOW — replace with np.where or pd.cut
for i, row in df.iterrows():
    if row["score"] >= 60:
        df.at[i, "grade"] = "Pass"
    else:
        df.at[i, "grade"] = "Fail"'''), True),
        _pe_panel(2, "03", "Count Rows Without Full Load", "Use chunked reading to count rows where amount &gt; 1000 without loading the entire file.",
            _code_block_a("exercise_03.py", '''# TODO: Use chunksize to count rows where amount > 1000
# in "large_sales.csv" without loading the full file
count = 0
# Your code here...
print(f"Rows with amount > 1000: {count:,}")'''), True),
    ])
    pe_body = f'''<div class="flex items-center gap-2 mb-6" role="tablist">{pe_tabs}</div>\n{pe_panels}'''
    s.append(section_wrap("practice", "fa6-solid:pencil", "Practice Exercises", "Hands-on tasks to reinforce the concepts", pe_body))

    # MISTAKES
    mk_body = "\n".join([
        _mistake_card(1, "Loading then filtering", "df = pd.read_csv(\"huge.csv\")\ndf = df[df[\"region\"] == \"EMEA\"]", "chunks = []\nfor c in pd.read_csv(\"huge.csv\", chunksize=100_000):\n    chunks.append(c[c[\"region\"]==\"EMEA\"])\ndf = pd.concat(chunks)", "Loading 10 million rows then discarding 9.9 million wastes memory."),
        _mistake_card(2, "Using iterrows() on large DataFrames", 'for idx, row in df.iterrows():\n    df.at[idx, "tax"] = row["amount"] * 0.1', 'df["tax"] = df["amount"] * 0.1', "Vectorized operations run in C and are ~100&times; faster."),
        _mistake_card(3, "Forgetting category dtype limitations", 'df["region"] = df["region"].astype("category")\ndf.loc[0, "region"] = "New Region"  # fails!', 'df["region"] = df["region"].cat.add_categories("New Region")\ndf.loc[0, "region"] = "New Region"', "You must add new category values before assigning them."),
    ])
    s.append(section_wrap("mistakes", "fa6-solid:triangle-exclamation", "Common Mistakes", "Pitfalls to avoid when handling large data", mk_body))

    # RECAP
    recap_body = f'''<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
{_recap_card(1, "<strong>Pandas defaults</strong> allocate more memory than necessary &mdash; int64, float64, and object dtypes are the main culprits.")}
{_recap_card(2, "<strong>Dtype optimization</strong> (downcasting integers, floats, and converting strings to category) typically reduces DataFrame size by 50&ndash;80%.")}
{_recap_card(3, "<strong>Chunk processing</strong> with chunksize turns memory-bound problems into time-bound ones &mdash; any file can be processed in any amount of RAM.")}
{_recap_card(4, "<strong>Vectorized operations</strong> replace Python loops and run 10&ndash;100&times; faster because they execute in compiled C.")}
</div>\n{COMPLETION_BANNER}'''
    s.append(section_wrap("recap", "fa6-solid:list-check", "Lesson Recap", "Summary of what you learned", recap_body))

    # QUIZ
    qz_tabs = "\n".join([_quiz_tab_btn(i, f"Question {i+1}", i==0) for i in range(3)])
    qz_panels = "\n".join([
        _quiz_panel(0, "A column contains &ldquo;Pass&rdquo;, &ldquo;Fail&rdquo;, &ldquo;Pending&rdquo; repeated 2 million times. Which dtype change saves the most memory?", "Convert to category", "Convert to int64", True),
        _quiz_panel(1, "Your script crashes with MemoryError on a 15 GB CSV. What is the correct approach?", "Use chunked reading with chunksize", "Buy more RAM", True, True),
        _quiz_panel(2, "True or False: iterrows() is the recommended way to update values in a large DataFrame.", "False", "True", True, True),
    ])
    qz_body = f'''<div class="flex items-center gap-2 mb-6" role="tablist">{qz_tabs}</div>\n{qz_panels}'''
    s.append(section_wrap("knowledge-check", "fa6-solid:brain", "Knowledge Check", "Test your understanding", qz_body))
    return s


# ══════════════════════════════════════════════════════════════════════
# Remaining lessons use the same pattern — abbreviated for speed
# ══════════════════════════════════════════════════════════════════════

def _quick_lesson(num, obj_cards, obj_tip, hook, analogy_text, ov_cards, ov_tip,
                  ki_cards, kc_tabs_panels, ce_tabs_panels, pe_tabs_panels,
                  mistakes, recap_items, quiz_items):
    """Generic builder for a full lesson given structured data."""
    s = []
    s.append(section_wrap("objective", "fa6-solid:bullseye", "Lesson Objective", "The goal and expected outcome of this lesson",
        obj_section(obj_cards, obj_tip)))
    s.append(section_wrap("overview", "fa6-solid:binoculars", "Overview", "A high-level summary of the topic",
        overview_section(hook, analogy_text, "\n".join(ov_cards), ov_tip)))
    s.append(section_wrap("key-ideas", "fa6-solid:lightbulb", "Key Takeaways", "The most important ideas to remember", "\n".join(ki_cards)))

    kc_t, kc_p = kc_tabs_panels
    s.append(section_wrap("key-concepts", "fa6-solid:book-open", "Key Concepts", "Core terms and definitions for this topic", _kc_section(kc_t, kc_p)))

    ce_t, ce_p = ce_tabs_panels
    ce_body = f'<div class="flex items-center gap-2 mb-6" role="tablist">{chr(10).join(ce_t)}</div>\n{chr(10).join(ce_p)}'
    s.append(section_wrap("code-examples", "fa6-solid:code", "Code Examples", "Hands-on code snippets to explore the concepts", ce_body))

    pe_t, pe_p = pe_tabs_panels
    pe_body = f'<div class="flex items-center gap-2 mb-6" role="tablist">{chr(10).join(pe_t)}</div>\n{chr(10).join(pe_p)}'
    s.append(section_wrap("practice", "fa6-solid:pencil", "Practice Exercises", "Hands-on tasks to reinforce the concepts", pe_body))

    mk_body = "\n".join(mistakes)
    s.append(section_wrap("mistakes", "fa6-solid:triangle-exclamation", "Common Mistakes", "Pitfalls to avoid", mk_body))

    recap_body = '<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n' + "\n".join([_recap_card(i+1, t) for i, t in enumerate(recap_items)]) + f'\n</div>\n{COMPLETION_BANNER}'
    s.append(section_wrap("recap", "fa6-solid:list-check", "Lesson Recap", "Summary of what you learned", recap_body))

    qz_tabs_html = "\n".join([_quiz_tab_btn(i, f"Question {i+1}", i==0) for i in range(len(quiz_items))])
    qz_panels_html = "\n".join([_quiz_panel(i, q, ca, ia, cf, i>0) for i, (q, ca, ia, cf) in enumerate(quiz_items)])
    qz_body = f'<div class="flex items-center gap-2 mb-6" role="tablist">{qz_tabs_html}</div>\n{qz_panels_html}'
    s.append(section_wrap("knowledge-check", "fa6-solid:brain", "Knowledge Check", "Test your understanding", qz_body))
    return s


def _L04():
    return _quick_lesson(4,
        obj_cards=[
            _obj_card("fa6-solid:table-columns", "Explain columnar storage", "Describe why column-oriented files are faster for analytics than row-oriented CSVs."),
            _obj_card("fa6-solid:file-arrow-down", "Read and write Parquet", "Use pandas and PyArrow to convert CSVs to Parquet and query them efficiently."),
            _obj_card("fa6-solid:filter", "Column selection &amp; pushdown", "Load only the columns and rows you need, skipping data at the file level."),
            _obj_card("fa6-solid:scale-balanced", "Know when to convert", "Identify when replacing CSV with Parquet gives the biggest benefit."),
        ],
        obj_tip="This lesson explains why every modern data platform defaults to Parquet &mdash; and how to use it in your own pipelines.",
        hook="A CSV stores data the way a spreadsheet does &mdash; one row at a time. Parquet stores it the way an analytics engine thinks &mdash; one column at a time, compressed per column. That single difference makes Parquet 5&ndash;20&times; faster and 3&ndash;10&times; smaller.",
        analogy_text="Think of row vs column storage like two ways of organizing employee records. A <strong>row store</strong> (CSV) is like a binder where each page holds one employee&rsquo;s complete record. A <strong>column store</strong> (Parquet) is like a set of indexed folders &mdash; one folder for all names, one for all salaries. When you ask &ldquo;average salary?&rdquo; you only open the salary folder.",
        ov_cards=[
            _overview_card("fa6-solid:file-csv", "CSV (Row Store)", "One page per employee &mdash; complete record per row", "Reads every column even when you only need one. Good for exports, bad for analytics at scale.", "pink"),
            _overview_card("fa6-solid:bars-staggered", "Parquet (Column Store)", "Indexed folders by field &mdash; open only what you need", "Stores each column contiguously with per-column compression. Reads only the columns your query touches.", "violet"),
            _overview_card("fa6-solid:file-zipper", "Compression", "Vacuum-sealed bags &mdash; same contents, fraction of the space", "Parquet compresses each column independently. Columns with repetitive data (like region) compress extremely well.", "blue"),
            _overview_card("fa6-solid:forward", "Predicate Pushdown", "Only open the folders that match your search", "The reader checks row group statistics (min/max) and skips entire chunks that can&rsquo;t match your filter.", "emerald"),
        ],
        ov_tip="For analytics workloads &mdash; aggregations, filters, selecting specific columns &mdash; columnar storage is almost always faster and smaller than CSV.",
        ki_cards=[
            _ki_card("pink", "fa6-solid:trophy", "Parquet Is the Industry Standard", "Every major data platform &mdash; BigQuery, Snowflake, Databricks, AWS Athena &mdash; uses columnar storage internally or accepts Parquet as the native import format.", ["Parquet", "Columnar", "Industry standard"]),
            _ki_card("violet", "fa6-solid:scissors", "Column Selection at the File Level", "Unlike CSV, Parquet lets you request specific columns and the reader skips everything else. On a 200-column dataset, reading 4 columns means 98% less data read.", ["Column pruning", "Selective reads", "I/O savings"]),
            _ki_card("blue", "fa6-solid:microchip", "PyArrow Powers the Operation", "When you call pd.read_parquet(), pandas delegates to PyArrow &mdash; which handles compression, encoding, and zero-copy reads.", ["PyArrow", "Apache Arrow", "Zero-copy"]),
        ],
        kc_tabs_panels=(
            [_kc_tab(0, "fa6-solid:table-columns", "Row vs Column", True),
             _kc_tab(1, "fa6-solid:file-arrow-down", "Write Parquet"),
             _kc_tab(2, "fa6-solid:filter", "Column Selection")],
            [_kc_panel(0, "pink", "Row Store vs Column Store",
                f'''<p class="text-xs text-gray-600 leading-relaxed">A row store reads all fields on each row. A column store reads only the requested columns, skipping everything else at the file level.</p>
{_code_block_b("Python", """# CSV: must read all 4 fields per row to get salary
# Parquet: reads only the salary column — skips name, dept, start_date""")}'''),
             _kc_panel(1, "violet", "Writing Parquet with pandas",
                f'''{_code_block_b("Python", """import pandas as pd

df = pd.read_csv("sales.csv")
df.to_parquet("sales.parquet", index=False)  # default compression: snappy
df_back = pd.read_parquet("sales.parquet")""")}''', True),
             _kc_panel(2, "blue", "Column Selection (the big win)",
                f'''<p class="text-xs text-gray-600 leading-relaxed">Specify only the columns you need. Parquet skips the rest at the file level &mdash; a major advantage over CSV.</p>
{_code_block_b("Python", """df = pd.read_parquet(
    "sales.parquet",
    columns=["order_id", "amount", "region"]  # 3 of maybe 50 columns
)""")}''', True)]),
        ce_tabs_panels=(
            [_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)],
            [_ce_panel(0, "01", "CSV vs Parquet &mdash; Size &amp; Speed", "Beginner", "Compare file sizes and read speed between CSV and Parquet.",
                _code_block_a("csv_vs_parquet.py", '''import pandas as pd, time, os

df.to_csv("sales.csv", index=False)
df.to_parquet("sales.parquet", index=False)

csv_mb = os.path.getsize("sales.csv") / 1024**2
pq_mb  = os.path.getsize("sales.parquet") / 1024**2
print(f"CSV: {csv_mb:.1f} MB  Parquet: {pq_mb:.1f} MB  ({csv_mb/pq_mb:.1f}x smaller)")

t0 = time.perf_counter()
pd.read_csv("sales.csv")["amount"].sum()
csv_time = time.perf_counter() - t0

t0 = time.perf_counter()
pd.read_parquet("sales.parquet", columns=["amount"])["amount"].sum()
pq_time = time.perf_counter() - t0
print(f"CSV: {csv_time:.2f}s  Parquet: {pq_time:.2f}s  ({csv_time/pq_time:.1f}x faster)")''', terminal_output="CSV: 412.3 MB  Parquet: 58.7 MB  (7.0x smaller)\nCSV: 8.41s  Parquet: 0.73s  (11.5x faster)")),
             _ce_panel(1, "02", "Writing Partitioned Parquet", "Intermediate", "Partition by year and region to create a folder hierarchy for fast filtered reads.",
                _code_block_a("partitioned_write.py", '''df.to_parquet(
    "sales_partitioned/",
    partition_cols=["year", "region"],
    index=False
)
# Folder: sales_partitioned/year=2024/region=EMEA/part-0.parquet

# Read only 2025 EMEA — skips all other partitions
df_emea_2025 = pd.read_parquet(
    "sales_partitioned/",
    filters=[("year", "==", 2025), ("region", "==", "EMEA")]
)'''), True),
             _ce_panel(2, "03", "PyArrow for Finer Control", "Intermediate", "Use PyArrow directly for explicit compression and predicate pushdown.",
                _code_block_a("pyarrow_control.py", '''import pyarrow as pa
import pyarrow.parquet as pq

table = pa.Table.from_pandas(df)
pq.write_table(table, "sales.parquet",
    compression="snappy", row_group_size=100_000)

dataset = pq.read_table("sales.parquet",
    columns=["order_id", "amount"],
    filters=[("amount", ">", 1000)])
df = dataset.to_pandas()'''), True),
             _ce_panel(3, "04", "Best Practice &mdash; CSV In, Parquet Out", "Beginner", "A pipeline step that reads CSV, optimizes dtypes, and saves as Parquet.",
                _code_block_a("csv_to_parquet.py", '''import pandas as pd, os

def csv_to_parquet(filename):
    df = pd.read_csv(os.path.join("raw/", filename))
    for col in df.select_dtypes("int64"):
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes("float64"):
        df[col] = pd.to_numeric(df[col], downcast="float")
    for col in df.select_dtypes("object"):
        if df[col].nunique() / len(df) < 0.1:
            df[col] = df[col].astype("category")
    out = os.path.join("clean/", filename.replace(".csv", ".parquet"))
    df.to_parquet(out, index=False)
    print(f"Saved {filename} -> {out} ({len(df):,} rows)")'''), True)]),
        pe_tabs_panels=(
            [_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)],
            [_pe_panel(0, "01", "Convert CSV to Parquet", "Read sample_data.csv, write to Parquet, and print the file size difference.",
                _code_block_a("exercise_01.py", '''import pandas as pd, os
# TODO: Read sample_data.csv
# TODO: Write to sample_data.parquet with index=False
# TODO: Print file size difference in MB''')),
             _pe_panel(1, "02", "Selective Column Read", "Read only 3 columns from a 30-column Parquet file and calculate the mean total by month.",
                _code_block_a("exercise_02.py", '''import pandas as pd
# TODO: Read ONLY customer_id, order_date, total from wide.parquet
# TODO: Calculate mean total grouped by month'''), True),
             _pe_panel(2, "03", "Benchmark CSV vs Parquet", "Time the read of the same data from CSV vs Parquet and print the speedup ratio.",
                _code_block_a("exercise_03.py", '''import pandas as pd, time
# TODO: Time CSV read, convert to Parquet, time Parquet read
# TODO: Print speedup ratio'''), True)]),
        mistakes=[
            _mistake_card(1, "Saving Parquet with the index", 'df.to_parquet("data.parquet")', 'df.to_parquet("data.parquet", index=False)', "The default creates a useless integer index column in the file."),
            _mistake_card(2, "Loading all columns when you need a few", 'df = pd.read_parquet("wide.parquet")\nresult = df["amount"].sum()', 'result = pd.read_parquet("wide.parquet",\n    columns=["amount"])["amount"].sum()', "Column selection at the file level avoids reading data you don&rsquo;t need."),
            _mistake_card(3, "Partitioning by a high-cardinality column", 'df.to_parquet("data/", partition_cols=["order_id"])', 'df.to_parquet("data/", partition_cols=["year","region"])', "High cardinality creates thousands of tiny files. Partition by low-cardinality columns."),
        ],
        recap_items=[
            "<strong>Columnar storage</strong> (Parquet) is faster for analytics than row storage (CSV) because reading one column doesn&rsquo;t require reading any other column.",
            "<strong>Parquet files</strong> are typically 5&ndash;10&times; smaller and 5&ndash;15&times; faster to read for analytical queries.",
            "<strong>Column selection</strong> and <strong>predicate pushdown</strong> let you skip data at the file level &mdash; a major advantage over CSV.",
            "<strong>PyArrow</strong> powers pandas&rsquo; Parquet support and provides finer control over compression and partitioning.",
        ],
        quiz_items=[
            ("Why is Parquet faster than CSV when summing one column on a 50-column dataset?", "Parquet reads only that column", "Parquet has faster compression", True),
            ("What does &ldquo;predicate pushdown&rdquo; mean for Parquet files?", "Filters skip row groups using metadata", "Data is pushed to a faster disk", True),
            ("You have a Parquet file partitioned by year and region. How do you read only 2024 APAC data?", "Use the filters parameter", "Read all then filter in pandas", True),
        ])


def _L05():
    return _quick_lesson(5,
        obj_cards=[
            _obj_card("fa6-solid:gauge-high", "Understand pandas limitations", "Explain why pandas is single-threaded and what that means at scale."),
            _obj_card("fa6-solid:bolt", "Polars basics", "Write basic Polars expressions using the lazy API."),
            _obj_card("fa6-solid:database", "DuckDB basics", "Run SQL queries directly on CSV and Parquet files."),
            _obj_card("fa6-solid:scale-balanced", "Choose the right tool", "Know when to reach for pandas, Polars, or DuckDB."),
        ],
        obj_tip="This lesson adds two faster alternatives to pandas to your toolkit &mdash; and shows when each one is the right choice.",
        hook="Pandas is the analyst&rsquo;s trusted workhorse &mdash; but it was designed for single-threaded operation. When datasets grow to tens of millions of rows, pandas gets slow. Polars and DuckDB were built to use every core your machine has.",
        analogy_text="Think of processing data like checking out at a supermarket. <strong>Pandas</strong> is like a single fast cashier. <strong>Polars</strong> is like a bank of self-checkout machines running simultaneously. <strong>DuckDB</strong> is like the back-office system that already knows every price &mdash; you hand it a query and get the answer without moving stock.",
        ov_cards=[
            _overview_card("fa6-solid:user", "Pandas", "One cashier &mdash; reliable, familiar, does the job", "Single-threaded, eager execution. Great for data under 1 million rows.", "pink"),
            _overview_card("fa6-solid:users", "Polars", "Bank of self-checkouts &mdash; parallel, fast, modern", "Multi-threaded, lazy evaluation, query optimization. 5&ndash;20&times; faster on large DataFrames.", "violet"),
            _overview_card("fa6-solid:magnifying-glass-chart", "DuckDB", "Back-office lookup &mdash; SQL on data where it sits", "Embedded database engine that queries Parquet/CSV with SQL. No server needed.", "blue"),
        ],
        ov_tip="You don&rsquo;t need to replace pandas everywhere. Use Polars for DataFrames with millions of rows. Use DuckDB when you want to query large files with SQL.",
        ki_cards=[
            _ki_card("pink", "fa6-solid:microchip", "Polars Uses All Your CPU Cores", "Polars operations run in parallel across all available CPU cores. On a 4-core laptop, a complex query on 10 million rows often runs 5&ndash;20&times; faster than pandas.", ["Multi-threaded", "Lazy evaluation", "Query optimization"]),
            _ki_card("violet", "fa6-solid:wand-magic-sparkles", "Polars Lazy Mode", "In lazy mode, Polars builds a query plan without running anything. When you call .collect(), it executes the optimized plan &mdash; dead columns are dropped, filters are pushed down.", ["scan_csv()", ".collect()", "Query plan"]),
            _ki_card("blue", "fa6-solid:terminal", "DuckDB Is SQL on Files", "DuckDB queries Parquet, CSV, and pandas DataFrames using standard SQL. It runs in your Python process &mdash; no server setup needed.", ["Embedded DB", "SQL on files", "Zero-copy"]),
        ],
        kc_tabs_panels=(
            [_kc_tab(0, "fa6-solid:code", "Polars Syntax", True),
             _kc_tab(1, "fa6-solid:table", "Core Concepts"),
             _kc_tab(2, "fa6-solid:database", "DuckDB Basics")],
            [_kc_panel(0, "pink", "Pandas vs Polars Syntax",
                f'''{_code_block_b("Python", """import polars as pl

# Polars lazy — builds plan, executes at .collect()
result = (
    pl.scan_csv("sales.csv")
      .filter(pl.col("amount") > 100)
      .group_by("region")
      .agg(pl.col("amount").sum())
      .collect()
)""")}'''),
             _kc_panel(1, "violet", "Polars Core Concepts",
                '''<div class="overflow-x-auto rounded-xl border border-gray-100">
<table class="w-full text-sm">
<thead><tr class="bg-gray-50"><th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs">Term</th><th class="px-4 py-3 text-left font-semibold text-gray-700 text-xs">Meaning</th></tr></thead>
<tbody>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-mono text-xs">LazyFrame</td><td class="px-4 py-3 text-gray-600">Query plan &mdash; runs at .collect()</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-mono text-xs">pl.scan_csv()</td><td class="px-4 py-3 text-gray-600">Lazy CSV reader</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-mono text-xs">pl.col("name")</td><td class="px-4 py-3 text-gray-600">Column expression</td></tr>
<tr class="border-t border-gray-100"><td class="px-4 py-3 text-gray-600 font-mono text-xs">.collect()</td><td class="px-4 py-3 text-gray-600">Execute the plan</td></tr>
</tbody></table></div>''', True),
             _kc_panel(2, "blue", "DuckDB Basics",
                _code_block_b("Python", 'import duckdb\n\ncon = duckdb.connect()\nresult = con.execute("""\n    SELECT region, SUM(amount) AS total\n    FROM \'sales.csv\'\n    WHERE amount > 100\n    GROUP BY region\n    ORDER BY total DESC\n""").fetchdf()'), True)]),
        ce_tabs_panels=(
            [_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)],
            [_ce_panel(0, "01", "Polars vs Pandas Benchmark", "Intermediate", "Compare execution times on 5 million rows.",
                _code_block_a("benchmark.py", '''import pandas as pd, polars as pl, time

t0 = time.perf_counter()
df = pd.read_csv("sales_5m.csv")
result = df[df["amount"]>500].groupby("region")["amount"].agg(["sum","mean","count"])
pd_time = time.perf_counter() - t0

t0 = time.perf_counter()
result = (pl.scan_csv("sales_5m.csv")
    .filter(pl.col("amount") > 500)
    .group_by("region")
    .agg([pl.col("amount").sum().alias("sum"),
          pl.col("amount").mean().alias("mean"),
          pl.col("amount").count().alias("count")])
    .collect())
pl_time = time.perf_counter() - t0
print(f"Pandas: {pd_time:.2f}s | Polars: {pl_time:.2f}s | Speedup: {pd_time/pl_time:.1f}x")''', terminal_output="Pandas: 18.4s | Polars: 1.9s | Speedup: 9.7x")),
             _ce_panel(1, "02", "Polars Multi-Transform", "Intermediate", "Chain multiple transformations in a single lazy query.",
                _code_block_a("polars_chain.py", '''import polars as pl
result = (
    pl.scan_parquet("orders.parquet")
      .filter(pl.col("status") == "completed")
      .with_columns([
          (pl.col("amount") * 1.1).alias("amount_with_tax"),
          pl.col("order_date").str.to_date().alias("order_date"),
      ])
      .group_by(["region", pl.col("order_date").dt.year().alias("year")])
      .agg([pl.col("amount_with_tax").sum().alias("total_revenue"),
            pl.col("order_id").n_unique().alias("order_count")])
      .sort("total_revenue", descending=True)
      .collect()
)'''), True),
             _ce_panel(2, "03", "DuckDB Multi-File Query", "Intermediate", "Query multiple Parquet files at once with a wildcard.",
                _code_block_a("duckdb_wildcard.py", '''import duckdb
con = duckdb.connect()
result = con.execute("""
    SELECT year, region, SUM(amount) AS total_revenue
    FROM 'sales_partitioned/year=*/region=*/*.parquet'
    WHERE year >= 2023
    GROUP BY year, region
    ORDER BY year, total_revenue DESC
""").fetchdf()
print(result)'''), True),
             _ce_panel(3, "04", "DuckDB + Pandas Zero-Copy", "Beginner", "Query an existing pandas DataFrame with SQL &mdash; no data copy needed.",
                _code_block_a("duckdb_pandas.py", '''import pandas as pd, duckdb

df = pd.read_csv("customers.csv")
result = duckdb.query("""
    SELECT region, COUNT(*) AS n, AVG(lifetime_value) AS avg_ltv
    FROM df
    GROUP BY region
    ORDER BY avg_ltv DESC
""").to_df()
print(result)'''), True)]),
        pe_tabs_panels=(
            [_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)],
            [_pe_panel(0, "01", "Polars Filter &amp; Aggregate", "Using lazy mode, filter orders to shipped status, group by product_category, and aggregate revenue.",
                _code_block_a("exercise_01.py", '''import polars as pl
# TODO: scan_csv("orders.csv")
# 1. Filter status == "shipped"
# 2. Group by "product_category"
# 3. Sum revenue and count order_id
# 4. Sort by revenue descending
# 5. .collect() and print''')),
             _pe_panel(1, "02", "DuckDB SQL on Parquet", "Use DuckDB to find the top 5 regions by total revenue from 2024 onwards in a Parquet file.",
                _code_block_a("exercise_02.py", '''import duckdb
# TODO: Query sales.parquet for top 5 regions by total revenue
# Only include rows from 2024 onwards
# Return a pandas DataFrame with .fetchdf()'''), True),
             _pe_panel(2, "03", "Speedup Comparison", "Write the same query in pandas and Polars, measure both times, and print the speedup ratio.",
                _code_block_a("exercise_03.py", '''# TODO: Same query in pandas and Polars:
# Read large_data.csv, filter score > 75
# Mean of value grouped by category
# Time both and print speedup'''), True)]),
        mistakes=[
            _mistake_card(1, "Using Polars eager mode", 'df = pl.read_csv("huge.csv")\nresult = df.filter(pl.col("x") > 100)', 'result = (\n    pl.scan_csv("huge.csv")\n      .filter(pl.col("x") > 100)\n      .collect()\n)', "scan_csv() is lazy &mdash; it reads only what passes the filter."),
            _mistake_card(2, "Calling .collect() repeatedly", 'lf = pl.scan_csv("data.csv")\nprint(lf.collect().shape)\nprint(lf.collect().head())', 'df = lf.collect()  # collect once\nprint(df.shape)\nprint(df.head())', "Each .collect() re-executes the entire query plan."),
            _mistake_card(3, "DuckDB for tiny data", 'con = duckdb.connect()\nresult = con.execute("SELECT SUM(x) FROM \'tiny.csv\'").fetchdf()', 'result = pd.read_csv("tiny.csv")["x"].sum()', "For 10,000 rows, pandas is fine. Use DuckDB when data is large enough to justify the overhead."),
        ],
        recap_items=[
            "<strong>Polars</strong> uses all CPU cores and lazy evaluation to run 5&ndash;20&times; faster than pandas on large DataFrames.",
            "<strong>Polars lazy mode</strong> builds a query plan and optimizes it before executing &mdash; dead columns are dropped and filters are pushed down.",
            "<strong>DuckDB</strong> is an embedded database that queries CSV and Parquet files with standard SQL, with no server setup.",
            "Choose <strong>pandas</strong> for small data, <strong>Polars</strong> for large DataFrames, and <strong>DuckDB</strong> when you think in SQL and data lives in files.",
        ],
        quiz_items=[
            ("What does pl.scan_csv() do differently from pl.read_csv()?", "Builds a lazy query plan", "Reads the file immediately", True),
            ("DuckDB can query a pandas DataFrame with SQL without copying the data. True or False?", "True", "False", True),
            ("When should you choose Polars over pandas?", "When processing millions of rows", "When data fits in a spreadsheet", True),
        ])


def _L06():
    return _quick_lesson(6,
        obj_cards=[
            _obj_card("fa6-solid:database", "Define NoSQL", "Explain why NoSQL databases exist and what problems they solve that SQL can&rsquo;t."),
            _obj_card("fa6-solid:layer-group", "4 NoSQL categories", "Describe document, key-value, column-family, and graph databases."),
            _obj_card("fa6-solid:file-code", "Hands-on with MongoDB", "Perform basic CRUD operations on a document database using Python."),
            _obj_card("fa6-solid:scale-balanced", "Decision framework", "Apply the SQL vs NoSQL decision criteria to a given scenario."),
        ],
        obj_tip="This lesson shows you when a project calls for NoSQL and helps you recommend the right type.",
        hook="SQL databases are exceptional for structured, consistent data. But not all data is structured, consistent, or relational. When you&rsquo;re storing user activity events, product catalogs with irregular attributes, or sensor readings by the billions &mdash; SQL tables become an uncomfortable fit.",
        analogy_text="Think of the difference between SQL and NoSQL like two kinds of office filing. An <strong>SQL database</strong> is like a rigidly organized file cabinet where every document must fit the section&rsquo;s template. A <strong>NoSQL database</strong> is like a flexible storage room where documents can have different structures and new fields can be added without redesigning the cabinet.",
        ov_cards=[
            _overview_card("fa6-solid:file-code", "Document DB", "One envelope per record &mdash; holds everything, any shape", "Stores JSON/BSON documents with variable structure. Best for user profiles, product catalogs, content.", "pink"),
            _overview_card("fa6-solid:key", "Key-Value DB", "A wall of numbered lockers &mdash; instant access by number", "Simple value indexed by key. Best for caching, sessions, and real-time leaderboards.", "violet"),
            _overview_card("fa6-solid:table-list", "Column-Family DB", "A notebook with infinitely expanding rows", "Rows can have different columns. Best for time-series, write-heavy IoT, and event logging.", "blue"),
            _overview_card("fa6-solid:diagram-project", "Graph DB", "A pinboard with thread connecting related items", "Nodes and edges with properties. Best for social networks, fraud detection, and recommendations.", "emerald"),
        ],
        ov_tip="NoSQL doesn&rsquo;t mean &ldquo;no structure&rdquo; &mdash; it means &ldquo;not only SQL.&rdquo; Most production systems use SQL and NoSQL together.",
        ki_cards=[
            _ki_card("pink", "fa6-solid:shuffle", "NoSQL Trades Schema for Flexibility", "A SQL table requires every row to have the same columns. A document database lets each document have different fields &mdash; essential when your data shape evolves rapidly.", ["Schema-less", "Flexible", "Evolving data"]),
            _ki_card("violet", "fa6-solid:server", "Horizontal Scaling Is Why NoSQL Exists", "SQL scales vertically (bigger server). NoSQL scales horizontally (more servers). For billions of records, adding machines is cheaper.", ["Horizontal scaling", "Sharding", "Distributed"]),
            _ki_card("blue", "fa6-solid:bullseye", "Choose Based on Access Pattern", "The best database is the one where your most common query reads data the way it&rsquo;s stored. Document DB for full records, key-value for lookups, graph for relationships.", ["Access pattern", "Query shape", "Data modeling"]),
        ],
        kc_tabs_panels=(
            [_kc_tab(0, "fa6-solid:table", "4 Categories", True),
             _kc_tab(1, "fa6-solid:check", "When SQL Wins"),
             _kc_tab(2, "fa6-solid:shuffle", "When NoSQL Wins")],
            [_kc_panel(0, "pink", "The 4 NoSQL Categories",
                '''<div class="overflow-x-auto rounded-xl border border-gray-100">
<table class="w-full text-sm">
<thead><tr class="bg-gray-50"><th class="px-3 py-3 text-left font-semibold text-gray-700 text-xs">Category</th><th class="px-3 py-3 text-left font-semibold text-gray-700 text-xs">Best For</th><th class="px-3 py-3 text-left font-semibold text-gray-700 text-xs">Tools</th></tr></thead>
<tbody>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-medium">Document</td><td class="px-3 py-3 text-gray-600">User profiles, catalogs</td><td class="px-3 py-3 text-gray-600">MongoDB, Firestore</td></tr>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-medium">Key-Value</td><td class="px-3 py-3 text-gray-600">Caching, sessions</td><td class="px-3 py-3 text-gray-600">Redis, DynamoDB</td></tr>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-medium">Column-Family</td><td class="px-3 py-3 text-gray-600">Time-series, IoT</td><td class="px-3 py-3 text-gray-600">Cassandra, HBase</td></tr>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-medium">Graph</td><td class="px-3 py-3 text-gray-600">Social networks, fraud</td><td class="px-3 py-3 text-gray-600">Neo4j, Neptune</td></tr>
</tbody></table></div>'''),
             _kc_panel(1, "violet", "When SQL Is Still Right",
                '''<ul class="space-y-2">
<li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-xs">Data is naturally tabular with consistent attributes</span></li>
<li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-xs">Complex JOIN queries across multiple entities</span></li>
<li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-xs">ACID transactions required (banking, inventory)</span></li>
</ul>''', True),
             _kc_panel(2, "blue", "When NoSQL Makes Sense",
                '''<ul class="space-y-2">
<li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-xs">Data structure is irregular or changes frequently</span></li>
<li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-xs">Store and retrieve complete entity records (no joins)</span></li>
<li class="flex items-start gap-2 text-gray-600"><span class="iconify text-brand mt-1 shrink-0 text-xs" data-icon="fa6-solid:check"></span><span class="text-xs">Need horizontal scaling across many nodes</span></li>
</ul>''', True)]),
        ce_tabs_panels=(
            [_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)],
            [_ce_panel(0, "01", "MongoDB CRUD", "Beginner", "Insert, read, update, and delete documents in MongoDB.",
                _code_block_a("mongodb_crud.py", '''from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
products = db["products"]

# INSERT — documents can have different shapes
products.insert_many([
    {"sku": "LAPTOP-001", "name": "Pro Laptop 15", "price": 1299.99,
     "specs": {"ram_gb": 16, "storage_tb": 1}},
    {"sku": "BOOK-042", "name": "Python for Engineers", "price": 39.99,
     "author": "Jane Smith", "isbn": "978-0000000000"}
])

# READ, UPDATE, DELETE
laptop = products.find_one({"sku": "LAPTOP-001"})
products.update_one({"sku": "LAPTOP-001"}, {"$set": {"in_stock": True}})
products.delete_many({"discontinued": True})''')),
             _ce_panel(1, "02", "Redis as Cache", "Intermediate", "Use Redis for sub-millisecond key-value lookups with automatic expiry.",
                _code_block_a("redis_cache.py", '''import redis, json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_user_profile(user_id):
    cache_key = f"user:{user_id}"
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)
    profile = query_database(user_id)
    r.setex(cache_key, 300, json.dumps(profile))  # 5-min TTL
    return profile'''), True),
             _ce_panel(2, "03", "SQL vs NoSQL Decision", "Beginner", "Walk through three real scenarios and pick the right database type.",
                _code_block_a("decision.py", '''"""
Scenario A: Online banking transactions
  Fixed schema, ACID required, complex JOINs
  -> USE SQL (PostgreSQL)

Scenario B: E-commerce product catalog
  Irregular attributes, schema evolves weekly
  -> USE Document DB (MongoDB)

Scenario C: User session management
  Simple key->value lookup, auto-expire after 30 min
  -> USE Key-Value DB (Redis)
"""'''), True),
             _ce_panel(3, "04", "MongoDB Aggregation Pipeline", "Intermediate", "Use MongoDB&rsquo;s aggregation framework for GROUP BY-style queries.",
                _code_block_a("mongo_agg.py", '''pipeline = [
    {"$match": {"status": "completed"}},
    {"$group": {
        "_id": "$region",
        "total_revenue": {"$sum": "$amount"},
        "order_count": {"$count": {}}
    }},
    {"$sort": {"total_revenue": -1}},
    {"$limit": 5}
]
results = list(orders.aggregate(pipeline))'''), True)]),
        pe_tabs_panels=(
            [_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)],
            [_pe_panel(0, "01", "Insert &amp; Query", "Insert 3 employees with different fields into MongoDB, then find those earning &gt; $80,000.",
                _code_block_a("exercise_01.py", '''from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
employees = client["company"]["employees"]
# TODO: Insert Alice (engineer), Bob (manager), Carol (analyst)
# TODO: Find all with salary > 80000
# TODO: Update Alice salary to 90000''')),
             _pe_panel(1, "02", "Decision Exercise", "For each scenario, choose SQL or a NoSQL type: 1) 500M IoT sensor readings. 2) Social network friendships. 3) Payroll with strict accuracy. 4) CMS with variable metadata.",
                '<div class="rounded-xl p-4 border bg-amber-tip"><p class="text-sm text-gray-600"><strong>Answers:</strong> 1. Column-Family &mdash; 2. Graph &mdash; 3. SQL &mdash; 4. Document</p></div>', True),
             _pe_panel(2, "03", "MongoDB Aggregation", "Write a pipeline: filter EMEA orders, group by product, sum revenue, sort desc, limit 3.",
                _code_block_a("exercise_03.py", '''# TODO: Build aggregation pipeline
pipeline = [
    # $match region == "EMEA"
    # $group by product, sum amount, count orders
    # $sort by total desc
    # $limit 3
]'''), True)]),
        mistakes=[
            _mistake_card(1, "Using MongoDB when data is relational", '# Separate collections joined in Python\ncustomers.find(...)\norders.find({"customer_id": cid})', '# Either embed customer data in orders\n# OR use a relational database for joins', "NoSQL works best when you read documents whole, not when you join them."),
            _mistake_card(2, "No indexes on frequently queried fields", 'products.find({"sku": "LAPTOP-001"})  # full scan', 'products.create_index([("sku", 1)], unique=True)\nproducts.find({"sku": "LAPTOP-001"})  # O(log n)', "Without an index, every query does a full collection scan."),
            _mistake_card(3, "NoSQL for naturally tabular data", '# Every product has the same 5 fields\n# but stored in MongoDB "for flexibility"', '# Use a SQL table — simpler, faster,\n# easier to enforce constraints', "If every record has the same schema, a relational table is the better fit."),
        ],
        recap_items=[
            "<strong>NoSQL databases</strong> handle data that doesn&rsquo;t fit the relational model &mdash; irregular schemas, horizontal scale, or relationship-heavy traversal.",
            "The <strong>4 categories</strong>: Document (flexible JSON), Key-Value (instant lookup), Column-Family (wide rows), and Graph (relationship traversal).",
            "<strong>MongoDB</strong> is the most common document database &mdash; use it when records have variable fields and are retrieved whole.",
            "The <strong>decision rule</strong>: SQL for uniform, relational, ACID data; NoSQL for irregular, high-volume, or specific access patterns.",
        ],
        quiz_items=[
            ("Which NoSQL category is best for a shopping cart with sub-millisecond lookup and 30-minute TTL?", "Key-Value (Redis)", "Document (MongoDB)", True),
            ("True or False: NoSQL databases can never perform joins.", "True &mdash; joins happen in application code", "False &mdash; they have full JOIN support", True),
            ("A product catalog where laptops have RAM specs but books have ISBNs is best stored in:", "A Document database", "A SQL table", True),
        ])


def _L07():
    return _quick_lesson(7,
        obj_cards=[
            _obj_card("fa6-solid:plug", "API mental model", "Explain what an API endpoint is and what a request/response cycle looks like."),
            _obj_card("fa6-solid:code", "Make requests with Python", "Use the requests library to call a REST API and handle the response."),
            _obj_card("fa6-solid:lock", "Authentication", "Add API keys to headers and understand the basic concept of OAuth."),
            _obj_card("fa6-solid:rotate", "Resilience patterns", "Handle pagination, rate limits, and network errors without crashing."),
        ],
        obj_tip="This lesson teaches you to build a complete API data collection script that handles real-world complications.",
        hook="Almost every modern data source &mdash; Salesforce, Stripe, Google Analytics, Jira &mdash; exposes its data through an API. If you can call APIs from Python, you can build pipelines that pull fresh data from any of them.",
        analogy_text="Think of an API like a restaurant&rsquo;s ordering system. The <strong>menu</strong> (API documentation) lists everything available. You place an <strong>order</strong> (HTTP request) by telling the waiter what you want. The kitchen processes it and returns your <strong>dish</strong> (the response) in a standard container (JSON).",
        ov_cards=[
            _overview_card("fa6-solid:link", "Endpoint", "A specific menu item &mdash; has a name and price", "A URL that identifies a specific resource. GET /orders returns all orders.", "pink"),
            _overview_card("fa6-solid:paper-plane", "Request", "Placing your order &mdash; you specify what you want", "An HTTP call with method (GET/POST), parameters, and authentication headers.", "violet"),
            _overview_card("fa6-solid:box-open", "Response", "The dish that arrives &mdash; structured, predictable format", "JSON data returned by the API, along with a status code (200 OK, 404 Not Found, etc.).", "blue"),
            _overview_card("fa6-solid:id-card", "API Key", "Your membership card &mdash; proves you are allowed to order", "A credential sent in the Authorization header to authenticate your requests.", "emerald"),
        ],
        ov_tip="An API is just a formalized way to request data from a remote system. Once you understand the pattern, every API works the same way.",
        ki_cards=[
            _ki_card("pink", "fa6-solid:code", "REST APIs Speak HTTP and Return JSON", "The vast majority of data APIs accept HTTP GET requests and return JSON. Once you parse it with response.json(), it&rsquo;s just Python dicts and lists.", ["REST", "HTTP GET", "JSON"]),
            _ki_card("violet", "fa6-solid:book-open", "Pagination Means Data Arrives in Pages", "APIs rarely return all results at once. Your pipeline must follow pagination links until all data is collected, or you&rsquo;ll silently miss records.", ["Pagination", "next_page", "while loop"]),
            _ki_card("blue", "fa6-solid:shield-halved", "Handle Rate Limits Gracefully", "Every API restricts request volume. Exceeding the limit returns 429. A resilient pipeline waits using the Retry-After header or exponential backoff.", ["Rate limit", "429", "Backoff"]),
        ],
        kc_tabs_panels=(
            [_kc_tab(0, "fa6-solid:globe", "HTTP Cycle", True),
             _kc_tab(1, "fa6-solid:table", "Status Codes"),
             _kc_tab(2, "fa6-solid:lock", "Authentication")],
            [_kc_panel(0, "pink", "HTTP Request/Response Cycle",
                f'''{_code_block_b("Python", """import requests

response = requests.get(
    url="https://api.example.com/orders",
    params={"status": "completed"},
    headers={"Authorization": "Bearer TOKEN"}
)
print(response.status_code)  # 200 = success
data = response.json()       # parse JSON to dict""")}'''),
             _kc_panel(1, "violet", "Common HTTP Status Codes",
                '''<div class="overflow-x-auto rounded-xl border border-gray-100">
<table class="w-full text-sm">
<thead><tr class="bg-gray-50"><th class="px-3 py-3 text-left font-semibold text-gray-700 text-xs">Code</th><th class="px-3 py-3 text-left font-semibold text-gray-700 text-xs">Meaning</th><th class="px-3 py-3 text-left font-semibold text-gray-700 text-xs">Action</th></tr></thead>
<tbody>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-mono">200</td><td class="px-3 py-3 text-gray-600">OK</td><td class="px-3 py-3 text-gray-600">Parse the response</td></tr>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-mono">401</td><td class="px-3 py-3 text-gray-600">Unauthorized</td><td class="px-3 py-3 text-gray-600">Check API key</td></tr>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-mono">429</td><td class="px-3 py-3 text-gray-600">Rate Limited</td><td class="px-3 py-3 text-gray-600">Wait and retry</td></tr>
<tr class="border-t border-gray-100"><td class="px-3 py-3 text-gray-600 font-mono">500</td><td class="px-3 py-3 text-gray-600">Server Error</td><td class="px-3 py-3 text-gray-600">Retry with backoff</td></tr>
</tbody></table></div>''', True),
             _kc_panel(2, "blue", "API Key Authentication",
                f'''{_code_block_b("Python", """# Method 1: Bearer token in headers (most common)
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get(url, headers=headers)

# Method 2: API key as query parameter
response = requests.get(url, params={"api_key": "YOUR_KEY"})""")}''', True)]),
        ce_tabs_panels=(
            [_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)],
            [_ce_panel(0, "01", "Basic GET Request", "Beginner", "Make a GET request with error checking and a timeout.",
                _code_block_a("basic_get.py", '''import requests

API_KEY = "your_api_key_here"
response = requests.get(
    "https://api.example.com/orders",
    params={"status": "completed", "limit": 100},
    headers={"Authorization": f"Bearer {API_KEY}"},
    timeout=10
)
response.raise_for_status()
orders = response.json()["orders"]
print(f"Retrieved {len(orders)} orders")''')),
             _ce_panel(1, "02", "Paginated API Collection", "Intermediate", "Follow pagination until all pages are collected.",
                _code_block_a("pagination.py", '''import requests, time

def get_all_orders(api_key):
    all_orders, page = [], 1
    while True:
        response = requests.get("https://api.example.com/orders",
            params={"page": page, "per_page": 100},
            headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        response.raise_for_status()
        data = response.json()
        all_orders.extend(data.get("orders", []))
        if not data.get("has_next_page", False):
            break
        page += 1
        time.sleep(0.2)
    print(f"Collected {len(all_orders)} orders across {page} pages")
    return all_orders'''), True),
             _ce_panel(2, "03", "Retry on Rate Limit", "Intermediate", "Handle 429 and 500 errors with exponential backoff.",
                _code_block_a("retry_logic.py", '''import requests, time

def request_with_retry(url, headers, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            wait = int(response.headers.get("Retry-After", 60))
            print(f"Rate limited. Waiting {wait}s...")
            time.sleep(wait)
        elif response.status_code >= 500:
            wait = 2 ** attempt
            print(f"Server error. Retrying in {wait}s...")
            time.sleep(wait)
        else:
            response.raise_for_status()
    raise RuntimeError(f"Failed after {max_retries} attempts")'''), True),
             _ce_panel(3, "04", "Full Pipeline &mdash; API to DataFrame", "Intermediate", "Fetch all pages, flatten JSON, and create a clean pandas DataFrame.",
                _code_block_a("api_to_df.py", '''import requests, pandas as pd, os

def fetch_all_pages(api_key):
    all_records, page = [], 1
    while True:
        resp = requests.get("https://api.example.com/orders",
            params={"page": page, "per_page": 200},
            headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        all_records.extend(data["orders"])
        if not data.get("has_next_page"): break
        page += 1
    return all_records

def normalize_orders(records):
    df = pd.json_normalize(records)
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["amount"] = df["amount"].astype("float32")
    return df

api_key = os.environ["ORDERS_API_KEY"]
records = fetch_all_pages(api_key)
df = normalize_orders(records)
print(df.shape, df.dtypes)'''), True)]),
        pe_tabs_panels=(
            [_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)],
            [_pe_panel(0, "01", "Your First API Call", "Use the free Open-Meteo API to fetch London&rsquo;s current temperature.",
                _code_block_a("exercise_01.py", '''import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 51.51, "longitude": -0.13, "current_weather": True}
# TODO: Make GET request, check status, print temperature''')),
             _pe_panel(1, "02", "Paginated Collection", "Fetch all posts from JSONPlaceholder and load them into a pandas DataFrame.",
                _code_block_a("exercise_02.py", '''import requests, pandas as pd
# TODO: GET https://jsonplaceholder.typicode.com/posts
# TODO: Print count, load into DataFrame'''), True),
             _pe_panel(2, "03", "Retry on Failure", "Write a function that retries on 429, waits 5s, up to 3 times.",
                _code_block_a("exercise_03.py", '''# TODO: Accept url and headers
# If 429, wait 5s and retry (up to 3 times)
# If 200, return JSON
# Otherwise raise exception'''), True)]),
        mistakes=[
            _mistake_card(1, "Not checking status before parsing", 'data = response.json()["orders"]  # crashes on error page', 'response.raise_for_status()\ndata = response.json()["orders"]', "Always check the status code before parsing the JSON."),
            _mistake_card(2, "Stopping at page 1", 'response = requests.get(url, params={"page": 1})\norders = response.json()["orders"]  # only 100 of 10,000', '# Always follow pagination until has_next_page is False', "This silently misses data &mdash; no error, just incomplete results."),
            _mistake_card(3, "Hard-coding API keys", 'API_KEY = "sk_live_abc123..."', 'import os\nAPI_KEY = os.environ["MY_API_KEY"]', "Keys in source code are visible in git history forever. Use environment variables."),
        ],
        recap_items=[
            "<strong>REST APIs</strong> accept HTTP requests and return JSON &mdash; once you understand the pattern, every API behaves the same way.",
            "<strong>Authentication</strong> is usually an API key in the Authorization header &mdash; never hard-code keys; use environment variables.",
            "<strong>Pagination</strong> means following all pages until the data is complete &mdash; stopping at page 1 silently loses records.",
            "<strong>Rate limits</strong> are enforced by every API &mdash; a resilient pipeline handles 429 errors with backoff instead of crashing.",
        ],
        quiz_items=[
            ("What HTTP status code means &ldquo;rate limit exceeded&rdquo;?", "429", "404", True),
            ("True or False: You should always set a timeout on requests.get().", "True", "False", True),
            ("What is the safest way to store an API key?", "Environment variable", "Hard-coded in the script", True),
        ])


def _L08():
    return _quick_lesson(8,
        obj_cards=[
            _obj_card("fa6-solid:shield-halved", "Define quality dimensions", "Name the 5 key dimensions of data quality and what violates each one."),
            _obj_card("fa6-solid:flask", "Write validation assertions", "Use Python assertions and pandas methods to check schema, nulls, ranges, and counts."),
            _obj_card("fa6-solid:box-archive", "Handle failures gracefully", "Route bad records to a quarantine table rather than crashing the whole pipeline."),
            _obj_card("fa6-solid:arrows-rotate", "Schema drift detection", "Detect when a source adds, removes, or renames columns unexpectedly."),
        ],
        obj_tip="This lesson gives you a reusable validation layer you can plug into any pipeline to catch data problems before they reach dashboards.",
        hook="Bad data that reaches a dashboard is worse than no pipeline at all &mdash; it creates false confidence. A chart showing &ldquo;$0 revenue last week&rdquo; because the pipeline silently loaded 0 clean rows is the data engineer&rsquo;s most embarrassing failure.",
        analogy_text="Think of a data validation layer like airport security screening. Every passenger (data record) goes through a checkpoint before reaching the departure lounge (your warehouse). Records that fail are quarantined for manual review. You don&rsquo;t cancel the whole flight because one passenger left their keys in their pocket.",
        ov_cards=[
            _overview_card("fa6-solid:id-card", "Schema Check", "Does the passenger have a valid ID format?", "Verify that all expected columns are present and have the correct data types.", "pink"),
            _overview_card("fa6-solid:file-circle-xmark", "Null Check", "Is the boarding pass blank?", "Ensure required fields are populated &mdash; nulls in critical columns break downstream queries.", "violet"),
            _overview_card("fa6-solid:ruler-combined", "Range Check", "Is the declared bag weight within limits?", "Validate that numeric values fall within expected boundaries (e.g. amount &gt; 0).", "blue"),
            _overview_card("fa6-solid:clone", "Uniqueness Check", "Is this passenger already on the flight?", "Detect duplicate rows that shouldn&rsquo;t exist &mdash; like two records with the same order_id.", "emerald"),
        ],
        ov_tip="The goal is not zero bad records &mdash; it&rsquo;s knowing about every bad record so you can decide what to do with it.",
        ki_cards=[
            _ki_card("pink", "fa6-solid:list-check", "5 Dimensions of Data Quality", "Completeness, Validity, Consistency, Uniqueness, and Timeliness. A validation layer should check all five dimensions after every extract step.", ["Completeness", "Validity", "Consistency", "Uniqueness", "Timeliness"]),
            _ki_card("violet", "fa6-solid:bullhorn", "Assert Early and Log Everything", "Write validation checks immediately after extract &mdash; before transformation. Silent failures (loading 0 rows with no error) are far more dangerous than loud ones.", ["Early validation", "Logging", "Fail-fast"]),
            _ki_card("blue", "fa6-solid:box-archive", "Quarantine Don&rsquo;t Crash", "When 3 of 10,000 rows fail, split into clean and quarantine sets. Load the clean set; write quarantine for investigation. The pipeline continues.", ["Quarantine table", "Partial load", "Alert threshold"]),
        ],
        kc_tabs_panels=(
            [_kc_tab(0, "fa6-solid:shield-halved", "Quality Checks", True),
             _kc_tab(1, "fa6-solid:file-code", "Schema Validation"),
             _kc_tab(2, "fa6-solid:box-archive", "Quarantine Pattern")],
            [_kc_panel(0, "pink", "Data Quality Assertions",
                f'''{_code_block_b("Python", """# COMPLETENESS
assert len(df) > 0, "DataFrame is empty"

# VALIDITY
assert df["amount"].between(0, 1_000_000).all()

# UNIQUENESS
assert df["order_id"].is_unique

# CONSISTENCY
assert (df["end_date"] >= df["start_date"]).all()""")}'''),
             _kc_panel(1, "violet", "Schema Validation Function",
                f'''{_code_block_b("Python", """def validate_schema(df, expected_columns):
    actual = set(df.columns)
    expected = set(expected_columns)
    missing = expected - actual
    extra = actual - expected
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    if extra:
        print(f"Warning: extra columns: {extra}")
    return True""")}''', True),
             _kc_panel(2, "blue", "Quarantine Pattern",
                f'''{_code_block_b("Python", """def split_clean_quarantine(df):
    is_valid = (
        df["amount"].notna() &
        df["amount"].between(0, 1_000_000) &
        df["order_id"].notna()
    )
    clean = df[is_valid].copy()
    quarantine = df[~is_valid].copy()
    return clean, quarantine""")}''', True)]),
        ce_tabs_panels=(
            [_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)],
            [_ce_panel(0, "01", "Complete Validation Function", "Intermediate", "Run all 5 quality checks and return a results dict.",
                _code_block_a("validate_orders.py", '''import pandas as pd, logging
from datetime import datetime, timedelta

log = logging.getLogger(__name__)
EXPECTED_COLUMNS = ["order_id","customer_id","amount","status","created_at"]

def validate_orders(df):
    issues = []
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing: issues.append(f"Missing columns: {missing}")
    if len(df) == 0: issues.append("DataFrame is empty")

    null_counts = df[EXPECTED_COLUMNS].isnull().sum()
    for col, count in null_counts[null_counts > 0].items():
        issues.append(f"'{col}' has {count} nulls ({count/len(df)*100:.1f}%)")

    dupes = df["order_id"].duplicated().sum()
    if dupes: issues.append(f"{dupes} duplicate order_ids")

    passed = len(issues) == 0
    log.info(f"Validation {'PASSED' if passed else 'FAILED'}")
    return {"passed": passed, "issues": issues}''')),
             _ce_panel(1, "02", "Load with Quarantine", "Intermediate", "Split clean and bad rows, load clean, quarantine the rest.",
                _code_block_a("quarantine_load.py", '''def load_with_quarantine(df, engine, table):
    is_bad = df["amount"].isna() | df["amount"].lt(0) | df["order_id"].isna()
    clean = df[~is_bad]
    quarantine = df[is_bad].assign(quarantined_at=pd.Timestamp.now())

    clean.to_sql(table, engine, if_exists="replace", index=False)
    if len(quarantine) > 0:
        quarantine.to_sql(f"{table}_quarantine", engine, if_exists="append", index=False)

    pct = len(quarantine) / len(df) * 100
    if pct > 5:
        raise ValueError(f"Quarantine rate {pct:.1f}% exceeds threshold")'''), True),
             _ce_panel(2, "03", "Schema Drift Detection", "Intermediate", "Compare current columns against a saved baseline to detect changes.",
                _code_block_a("schema_drift.py", '''import json, os

SCHEMA_FILE = "expected_schema.json"

def detect_schema_drift(df):
    if not os.path.exists(SCHEMA_FILE):
        schema = {col: str(dtype) for col, dtype in df.dtypes.items()}
        with open(SCHEMA_FILE, "w") as f: json.dump(schema, f)
        return []
    with open(SCHEMA_FILE) as f: expected = json.load(f)
    actual = {col: str(dtype) for col, dtype in df.dtypes.items()}
    drifts = []
    for col in expected:
        if col not in actual: drifts.append(f"REMOVED: '{col}'")
        elif actual[col] != expected[col]: drifts.append(f"TYPE CHANGE: '{col}'")
    for col in actual:
        if col not in expected: drifts.append(f"ADDED: '{col}'")
    return drifts'''), True),
             _ce_panel(3, "04", "Row-Count Assertion", "Beginner", "Fail loudly if the row count drops below a minimum threshold.",
                _code_block_a("row_count_check.py", '''def assert_row_count(df, min_rows, context=""):
    if len(df) < min_rows:
        msg = f"Expected >= {min_rows:,} rows, got {len(df):,}. {context}"
        log.error(msg)
        raise AssertionError(msg)
    log.info(f"Row count OK: {len(df):,} >= {min_rows:,}")'''), True)]),
        pe_tabs_panels=(
            [_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)],
            [_pe_panel(0, "01", "Write a Validator", "Create a function that checks completeness, validity, and uniqueness for an orders DataFrame.",
                _code_block_a("exercise_01.py", '''import pandas as pd
def validate(df):
    issues = []
    # TODO: Check for null order_id and amount
    # TODO: Check amount is between 0 and 1,000,000
    # TODO: Check order_id is unique
    return issues''')),
             _pe_panel(1, "02", "Build a Quarantine Split", "Given a DataFrame, separate clean and invalid rows based on null and range checks.",
                _code_block_a("exercise_02.py", '''# TODO: Write a function that returns (clean_df, quarantine_df)
# Bad rows: amount is null, amount < 0, or status not in valid set'''), True),
             _pe_panel(2, "03", "Detect Schema Drift", "Write a function that compares current columns against an expected list and reports differences.",
                _code_block_a("exercise_03.py", '''# TODO: Compare df.columns against expected_columns
# Report: missing columns, extra columns, type changes'''), True)]),
        mistakes=[
            _mistake_card(1, "Validating after transform", 'clean = transform(raw)\nvalidate(clean)', 'raw = extract()\nvalidate(raw)\nclean = transform(raw)', "Validate raw data immediately after extract &mdash; catch source problems early."),
            _mistake_card(2, "Using assert in production", 'assert len(df) > 0  # disabled with -O flag', 'if len(df) == 0:\n    raise ValueError("DataFrame is empty")', "Python&rsquo;s assert can be disabled. Use explicit exceptions."),
            _mistake_card(3, "Crashing on a few bad rows", 'assert df["amount"].notna().all()  # crashes pipeline', 'clean, quarantine = split(df)\nload(clean)  # continue with good rows', "Quarantine bad rows instead of stopping the entire pipeline."),
        ],
        recap_items=[
            "The <strong>5 dimensions</strong> of data quality are completeness, validity, consistency, uniqueness, and timeliness.",
            "<strong>Validate early</strong> &mdash; run checks immediately after extraction, before any transformation.",
            "<strong>Quarantine</strong> bad records instead of crashing &mdash; load the clean set and investigate failures separately.",
            "<strong>Schema drift detection</strong> catches when a source silently adds, removes, or changes columns.",
        ],
        quiz_items=[
            ("When should you run validation checks in a pipeline?", "Immediately after extraction", "After loading into the warehouse", True),
            ("What should happen when 3 out of 10,000 rows fail validation?", "Quarantine the 3, load the rest", "Crash the entire pipeline", True),
            ("True or False: Python&rsquo;s assert statement is safe for production validation.", "False", "True", True),
        ])


def _L09():
    return _quick_lesson(9,
        obj_cards=[
            _obj_card("fa6-solid:clock", "Schedule pipelines", "Use cron syntax and Python schedulers to run pipelines automatically."),
            _obj_card("fa6-solid:code-branch", "CI/CD basics", "Understand pipeline YAML and how to add data jobs to a CI/CD workflow."),
            _obj_card("fa6-solid:server", "Deployment workflow", "Move a pipeline from local through staging to production."),
            _obj_card("fa6-solid:chart-line", "Monitoring &amp; alerting", "Log metrics, set up health checks, and understand what to alert on."),
        ],
        obj_tip="This lesson shows you how to take a working pipeline and turn it into a production-grade automated job.",
        hook="Writing a pipeline that works on your laptop is step one. Making it run reliably every night &mdash; without you touching it &mdash; is the real engineering challenge.",
        analogy_text="Think of a production pipeline like running a daily newspaper. The press runs automatically at the same time every night, and an alarm sounds if a machine jams. The <strong>scheduler</strong> is the clock that starts the press. <strong>CI/CD</strong> is the quality control process. <strong>Monitoring</strong> is the night editor&rsquo;s phone.",
        ov_cards=[
            _overview_card("fa6-solid:clock", "Scheduler (cron)", "The clock that starts the press at 2 AM", "Cron expressions define when jobs run. Every platform uses cron syntax.", "pink"),
            _overview_card("fa6-solid:code-branch", "CI/CD Pipeline", "Quality control before print", "Automated test &rarr; build &rarr; deploy lifecycle triggered by git pushes.", "violet"),
            _overview_card("fa6-solid:flask-vial", "Staging Environment", "The proof copy checked before the full run", "A copy of production where changes are tested safely before going live.", "blue"),
            _overview_card("fa6-solid:bell", "Monitoring", "The night editor&rsquo;s phone &mdash; rings when something breaks", "Structured logging, health checks, and alerts on failures or stale data.", "emerald"),
        ],
        ov_tip="Automation takes a pipeline from &ldquo;I run it manually&rdquo; to &ldquo;it runs itself, and I hear about it only when something goes wrong.&rdquo;",
        ki_cards=[
            _ki_card("pink", "fa6-solid:clock", "Cron Is the Universal Scheduler", "0 2 * * * means &ldquo;at 02:00 every day.&rdquo; Every cloud platform and CI/CD tool uses cron syntax for scheduling.", ["Cron", "Schedule", "0 2 * * *"]),
            _ki_card("violet", "fa6-solid:code-branch", "CI/CD Brings Engineering Discipline", "Push code &rarr; CI runs tests &rarr; CD deploys. You never manually copy code to production.", ["Git push", "CI tests", "CD deploy"]),
            _ki_card("blue", "fa6-solid:shield-halved", "Environments Separate Risk", "Staging is a safe copy of production. Changes go through staging first. Rolling back is a git revert, not a prayer.", ["Staging", "Production", "Rollback"]),
        ],
        kc_tabs_panels=(
            [_kc_tab(0, "fa6-solid:clock", "Cron Syntax", True),
             _kc_tab(1, "fa6-solid:terminal", "Python Scheduler"),
             _kc_tab(2, "fa6-solid:code-branch", "CI/CD YAML")],
            [_kc_panel(0, "pink", "Cron Syntax",
                f'''{_code_block_b("Bash", """# minute hour day-of-month month day-of-week
0  2  *  *  *   # Every day at 02:00
0  */6 * *  *   # Every 6 hours
0  2  *  *  1   # Every Monday at 02:00
*/15 * * *  *   # Every 15 minutes""", "bash")}'''),
             _kc_panel(1, "violet", "APScheduler (Python)",
                f'''{_code_block_b("Python", """from apscheduler.schedulers.blocking import BlockingScheduler
import orders_pipeline

scheduler = BlockingScheduler()

@scheduler.scheduled_job("cron", hour=2, minute=0)
def run_nightly():
    orders_pipeline.run()

scheduler.start()""")}''', True),
             _kc_panel(2, "blue", "GitLab CI/CD YAML",
                f'''{_code_block_b("Bash", """# .gitlab-ci.yml
stages: [test, deploy]

test-pipeline:
  stage: test
  script:
    - pip install -r requirements.txt
    - pytest tests/ -v

deploy-production:
  stage: deploy
  when: manual
  script:
    - python orders_pipeline.py
  variables:
    DB_URL: $PROD_DB_URL""", "bash")}''', True)]),
        ce_tabs_panels=(
            [_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)],
            [_ce_panel(0, "01", "Production Pipeline with Logging", "Intermediate", "A complete pipeline with structured logging and error handling.",
                _code_block_a("production_pipeline.py", '''import logging, sys
from datetime import datetime

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    handlers=[logging.FileHandler(f"logs/pipeline_{datetime.now():%Y%m%d}.log"),
              logging.StreamHandler(sys.stdout)])
log = logging.getLogger("orders_pipeline")

def run():
    log.info("=== Pipeline started ===")
    try:
        raw = extract()
        valid = validate(raw)
        clean = transform(valid)
        load(clean)
        log.info(f"=== Complete: {len(clean):,} rows loaded ===")
    except Exception as e:
        log.error(f"Pipeline FAILED: {e}", exc_info=True)
        sys.exit(1)''')),
             _ce_panel(1, "02", "Environment Isolation", "Intermediate", "Different configs for dev, staging, and production.",
                _code_block_a("config.py", '''import os
ENV = os.environ.get("ENV", "development")
CONFIG = {
    "development": {"db_url": "sqlite:///local.db",
                    "api_url": "https://sandbox.api.example.com"},
    "staging":     {"db_url": os.environ.get("DB_URL", ""),
                    "api_url": "https://staging.api.example.com"},
    "production":  {"db_url": os.environ.get("DB_URL", ""),
                    "api_url": "https://api.example.com"},
}[ENV]'''), True),
             _ce_panel(2, "03", "Health Check Endpoint", "Intermediate", "A simple Flask endpoint to monitor pipeline status.",
                _code_block_a("health_check.py", '''from flask import Flask, jsonify
import json, os
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/health")
def health():
    with open("pipeline_status.json") as f:
        status = json.load(f)
    last_run = datetime.fromisoformat(status["last_run"])
    stale = last_run < datetime.now() - timedelta(hours=25)
    healthy = status["status"] == "success" and not stale
    return jsonify({"healthy": healthy, "last_run": status["last_run"]}), 200 if healthy else 503'''), True),
             _ce_panel(3, "04", "Deployment with Rollback", "Intermediate", "A git-based deployment workflow with one-command rollback.",
                _code_block_a("deploy.sh", '''# Push to develop -> CI tests run automatically
git add . && git commit -m "fix: handle null region"
git push origin develop

# After CI passes, merge to main
# If production breaks, rollback in 30 seconds:
git revert HEAD --no-edit
git push origin main''', "bash"), True)]),
        pe_tabs_panels=(
            [_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)],
            [_pe_panel(0, "01", "Write Cron Expressions", "Write cron for: 1) 6:30 AM daily, 2) Mon+Wed midnight, 3) Every 30 min, 4) 1st of every month at 3 AM.",
                '<div class="rounded-xl p-4 border bg-amber-tip"><p class="text-sm text-gray-600"><strong>Answers:</strong> 1. <code>30 6 * * *</code> &mdash; 2. <code>0 0 * * 1,3</code> &mdash; 3. <code>*/30 * * * *</code> &mdash; 4. <code>0 3 1 * *</code></p></div>'),
             _pe_panel(1, "02", "Add Production Logging", "Take a minimal pipeline and add INFO logging, row counts, try/except with sys.exit(1).",
                _code_block_a("exercise_02.py", '''# TODO: Add logging, row counts, error handling
def run():
    raw   = extract()
    clean = transform(raw)
    load(clean)'''), True),
             _pe_panel(2, "03", "Environment Configuration", "Write a config.py that reads ENV, returns different DB URLs per environment.",
                _code_block_a("exercise_03.py", '''import os
# TODO: Read ENV variable (default "development")
# TODO: Return different DB_URL and API_URL per environment
# TODO: Raise error if required env var is missing'''), True)]),
        mistakes=[
            _mistake_card(1, "Using local paths in scheduled jobs", 'df = pd.read_csv("data/orders.csv")', 'import os\nBASE = os.path.dirname(os.path.abspath(__file__))\ndf = pd.read_csv(os.path.join(BASE, "data", "orders.csv"))', "Cron runs as a different user &mdash; relative paths won&rsquo;t resolve correctly."),
            _mistake_card(2, "No exit code on failure", 'try:\n    run_pipeline()\nexcept Exception as e:\n    print(f"Error: {e}")', 'import sys\ntry:\n    run_pipeline()\nexcept Exception as e:\n    log.error(e)\n    sys.exit(1)', "Without a non-zero exit code, the scheduler thinks the job succeeded."),
            _mistake_card(3, "Deploying directly to production", '# Edit -> save -> run in production', '# Edit -> commit -> CI tests -> staging\n# -> manual approval -> production', "A bug can corrupt live data with no easy rollback. Always go through staging."),
        ],
        recap_items=[
            "<strong>Cron</strong> is the universal scheduler &mdash; every platform uses cron syntax to define when jobs run.",
            "<strong>CI/CD</strong> automates testing and deployment so you never manually copy code to production.",
            "<strong>Environments</strong> (staging + production) separate testing from reality &mdash; changes go through staging first.",
            "<strong>Monitoring</strong> with structured logging and health checks ensures you hear about failures immediately.",
        ],
        quiz_items=[
            ("What cron expression runs a job at 2 AM every day?", "0 2 * * *", "2 0 * * *", True),
            ("Why is sys.exit(1) important in a scheduled pipeline?", "Signals failure to the scheduler", "Makes the script run faster", True),
            ("Changes should go through staging before production. True or False?", "True", "False", True),
        ])


def _L10():
    return _quick_lesson(10,
        obj_cards=[
            _obj_card("fa6-solid:stopwatch", "Profile a pipeline", "Use timing and memory profiling to identify where time is spent."),
            _obj_card("fa6-solid:microchip", "Parallel processing", "Use concurrent.futures to process multiple files simultaneously."),
            _obj_card("fa6-solid:server", "Dask awareness", "Understand what Dask is and when to reach for it."),
            _obj_card("fa6-solid:list-check", "Best practices checklist", "Apply the performance checklist to any large-data pipeline."),
        ],
        obj_tip="This lesson teaches you to measure performance accurately and apply the most impactful optimizations first.",
        hook="Optimizing a pipeline without profiling it first is guesswork. Data engineers who profile before optimizing consistently find that 80% of time is spent in one or two steps &mdash; and those steps are almost never what they expected.",
        analogy_text="Think of performance optimization like a Formula 1 pit stop analysis. Before improving anything, the team reviews telemetry data to see exactly where time was lost. <strong>Profiling</strong> is your telemetry. Once you know where the time goes, you fix the exact bottleneck.",
        ov_cards=[
            _overview_card("fa6-solid:chart-bar", "Profiling", "Reviewing lap telemetry data", "Measure each pipeline step to find which one is actually slow before optimizing anything.", "pink"),
            _overview_card("fa6-solid:magnifying-glass", "Identifying Bottlenecks", "Finding which wheel change was slowest", "80% of pipeline time is usually in 1&ndash;2 steps. Fix those first for the biggest impact.", "violet"),
            _overview_card("fa6-solid:users-gear", "Parallel Processing", "Multiple mechanics working different wheels simultaneously", "Process multiple files or partitions at the same time using all CPU cores.", "blue"),
            _overview_card("fa6-solid:clipboard-list", "Best Practices", "Standard procedures that keep every stop under 3 seconds", "A checklist of proven optimizations: Parquet, column selection, dtype optimization, vectorized ops.", "emerald"),
        ],
        ov_tip="A 10&times; speedup from profiling the real bottleneck beats a 2&times; speedup from blindly parallelizing code that wasn&rsquo;t the problem.",
        ki_cards=[
            _ki_card("pink", "fa6-solid:stopwatch", "Profile Before You Optimize", "The fastest code is code that doesn&rsquo;t need optimization &mdash; because you measured and found the slow step is the network call, not your transform function.", ["%timeit", "perf_counter", "memory_profiler"]),
            _ki_card("violet", "fa6-solid:microchip", "ProcessPoolExecutor Is the Right Tool", "concurrent.futures.ProcessPoolExecutor gives you multi-core parallelism with a clean API &mdash; submit a function and inputs, get results.", ["ProcessPoolExecutor", "map()", "CPU-bound"]),
            _ki_card("blue", "fa6-solid:server", "Dask for Out-of-RAM Data", "Dask extends pandas to work on distributed or too-large data. Same API as pandas. You&rsquo;re unlikely to need it early, but knowing it exists prevents reinventing the wheel.", ["Dask DataFrame", "Delayed", "Out-of-core"]),
        ],
        kc_tabs_panels=(
            [_kc_tab(0, "fa6-solid:stopwatch", "Profiling Tools", True),
             _kc_tab(1, "fa6-solid:microchip", "Parallel Processing"),
             _kc_tab(2, "fa6-solid:server", "Dask in Brief")],
            [_kc_panel(0, "pink", "Three Profiling Tools",
                f'''{_code_block_b("Python", """import time
# Tool 1: time.perf_counter
t0 = time.perf_counter()
result = some_function()
print(f"{time.perf_counter() - t0:.3f}s")

# Tool 2: %timeit in Jupyter
# %timeit df["amount"].sum()

# Tool 3: memory_profiler
from memory_profiler import memory_usage
mem = memory_usage((my_function, (df,)))
print(f"Peak: {max(mem):.1f} MB")""")}'''),
             _kc_panel(1, "violet", "concurrent.futures",
                f'''{_code_block_b("Python", """from concurrent.futures import ProcessPoolExecutor

def process_file(path):
    df = pd.read_parquet(path)
    return df.groupby("region")["amount"].sum()

files = ["jan.parquet", "feb.parquet", "mar.parquet"]

# Parallel — all CPU cores
with ProcessPoolExecutor() as executor:
    results = list(executor.map(process_file, files))""")}''', True),
             _kc_panel(2, "blue", "Dask Awareness",
                f'''{_code_block_b("Python", """import dask.dataframe as dd

# Same API as pandas, works on larger-than-RAM data
ddf = dd.read_parquet("data/*.parquet")
result = (
    ddf[ddf["amount"] > 100]
       .groupby("region")["amount"]
       .sum()
       .compute()  # Dask's version of .collect()
)""")}''', True)]),
        ce_tabs_panels=(
            [_ce_tab_btn(i, f"Example {i+1}", i==0) for i in range(4)],
            [_ce_panel(0, "01", "Step-by-Step Pipeline Profiling", "Intermediate", "Time each stage to find the real bottleneck.",
                _code_block_a("profile_pipeline.py", '''import time, pandas as pd

def run_pipeline_with_timing():
    timings = {}
    t = time.perf_counter()
    raw = pd.read_csv("orders.csv")
    timings["extract"] = time.perf_counter() - t

    t = time.perf_counter()
    clean = transform(raw)
    timings["transform"] = time.perf_counter() - t

    t = time.perf_counter()
    clean.to_sql("orders", engine, if_exists="replace", index=False)
    timings["load"] = time.perf_counter() - t

    total = sum(timings.values())
    for step, t in sorted(timings.items(), key=lambda x: -x[1]):
        print(f"{step:<20} {t:>7.2f}s {(t/total*100):>6.1f}%")''', terminal_output="load                  8.21s  67.3%\nextract               2.04s  16.7%\ntransform             1.42s  11.6%")),
             _ce_panel(1, "02", "Parallel File Processing", "Intermediate", "Process multiple Parquet files simultaneously.",
                _code_block_a("parallel_files.py", '''from concurrent.futures import ProcessPoolExecutor
import pandas as pd, glob, time

def process_monthly_file(filepath):
    df = pd.read_parquet(filepath)
    return {"file": filepath, "rows": len(df), "revenue": df["amount"].sum()}

files = sorted(glob.glob("data/sales_*.parquet"))

t0 = time.perf_counter()
sequential = [process_monthly_file(f) for f in files]
seq_time = time.perf_counter() - t0

t0 = time.perf_counter()
with ProcessPoolExecutor() as ex:
    parallel = list(ex.map(process_monthly_file, files))
par_time = time.perf_counter() - t0

print(f"Sequential: {seq_time:.1f}s  Parallel: {par_time:.1f}s  Speedup: {seq_time/par_time:.1f}x")'''), True),
             _ce_panel(2, "03", "Memory Profiling", "Intermediate", "Track line-by-line memory usage with @profile.",
                _code_block_a("memory_profile.py", '''from memory_profiler import profile

@profile
def load_and_process(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna()
    df["amount"] = df["amount"].astype("float32")
    df["region"] = df["region"].astype("category")
    result = df.groupby("region")["amount"].sum()
    del df
    return result'''), True),
             _ce_panel(3, "04", "Performance Best Practices", "Beginner", "A checklist of the most impactful optimizations applied.",
                _code_block_a("best_practices.py", '''import pandas as pd

# 1. Use Parquet instead of CSV
df = pd.read_parquet("clean.parquet", columns=["id","amount","region"])

# 2. Downcast dtypes
df["amount"] = df["amount"].astype("float32")
df["region"] = df["region"].astype("category")

# 3. Vectorized operations (never iterrows)
df["tax"] = df["amount"] * 0.1

# 4. Delete large objects when done
del raw_df

# 5. Batch database loads
df.to_sql("table", engine, method="multi", chunksize=10_000)'''), True)]),
        pe_tabs_panels=(
            [_pe_tab_btn(i, f"Exercise {i+1}", i==0) for i in range(3)],
            [_pe_panel(0, "01", "Profile Your Pipeline", "Add step-by-step timing to an existing pipeline and identify the bottleneck.",
                _code_block_a("exercise_01.py", '''import time
# TODO: Time each step (extract, transform, load)
# TODO: Print a table showing each step's time and % of total''')),
             _pe_panel(1, "02", "Parallelize File Processing", "Process 12 monthly Parquet files in parallel and compare speed vs sequential.",
                _code_block_a("exercise_02.py", '''from concurrent.futures import ProcessPoolExecutor
# TODO: Process files sequentially, then in parallel
# TODO: Print speedup ratio'''), True),
             _pe_panel(2, "03", "Apply the Checklist", "Review a pipeline and apply at least 5 best practices from the lesson.",
                _code_block_a("exercise_03.py", '''# TODO: Read as Parquet (not CSV), select only needed columns
# TODO: Downcast dtypes, use vectorized ops
# TODO: Delete intermediates, batch loads'''), True)]),
        mistakes=[
            _mistake_card(1, "Optimizing the wrong step", '# Spent 2h optimizing transform (saves 0.3s)\n# ...but load takes 12s and could be 2s', '# Profile first, then optimize the bottleneck\n# In this case: fix the load step', "Always profile before optimizing. The real bottleneck is rarely where you expect."),
            _mistake_card(2, "Threading for CPU-bound work", 'from concurrent.futures import ThreadPoolExecutor\nwith ThreadPoolExecutor(8) as ex:\n    results = list(ex.map(cpu_heavy, chunks))', 'from concurrent.futures import ProcessPoolExecutor\nwith ProcessPoolExecutor(8) as ex:\n    results = list(ex.map(cpu_heavy, chunks))', "Python&rsquo;s GIL limits threads to one core. Use ProcessPool for CPU work."),
            _mistake_card(3, "Parallelizing I/O with processes", 'from concurrent.futures import ProcessPoolExecutor\nwith ProcessPoolExecutor() as ex:\n    results = list(ex.map(api_call, urls))', 'from concurrent.futures import ThreadPoolExecutor\nwith ThreadPoolExecutor() as ex:\n    results = list(ex.map(api_call, urls))', "For I/O-bound work (API calls, DB queries), threads are lighter and sufficient."),
        ],
        recap_items=[
            "<strong>Profile before you optimize</strong> &mdash; 80% of pipeline time is usually in 1&ndash;2 steps. Find them first.",
            "<strong>ProcessPoolExecutor</strong> gives multi-core parallelism for CPU-bound work with a clean, simple API.",
            "<strong>Dask</strong> extends pandas for data that truly doesn&rsquo;t fit in RAM &mdash; same API, distributed execution.",
            "The <strong>performance checklist</strong>: Parquet, column selection, dtype optimization, vectorized ops, batch loads, profile first.",
        ],
        quiz_items=[
            ("What should you do before optimizing any pipeline step?", "Profile to find the bottleneck", "Parallelize everything", True),
            ("For CPU-bound parallel work in Python, which executor is correct?", "ProcessPoolExecutor", "ThreadPoolExecutor", True),
            ("True or False: Dask uses the same API as pandas.", "True", "False", True),
        ])


# ══════════════════════════════════════════════════════════════════════
# Export the mapping
# ══════════════════════════════════════════════════════════════════════
LESSON_SECTIONS = {
    2: _L02(),
    3: _L03(),
    4: _L04(),
    5: _L05(),
    6: _L06(),
    7: _L07(),
    8: _L08(),
    9: _L09(),
    10: _L10(),
}
