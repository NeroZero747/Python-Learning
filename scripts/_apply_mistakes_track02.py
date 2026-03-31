"""
Rewrite <section id="mistakes"> for all 18 lessons in
track_02 / mod_02, mod_03, mod_04.

Uses the prompt spec from lesson-common-mistakes.prompt.md.
Reuses the same builder functions as _apply_mistakes_mod01.py.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
T2 = BASE / "pages" / "track_02_data_analytics"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

# ── mod_02: Working With Data Sources ──────────────────────────────────

MOD02_LESSONS = {

    # ── Lesson 01: Reading CSV Files ──
    "lesson01_reading_csv_files.html": {
        "topic": "reading CSV files",
        "mistakes": [
            {
                "tab": "Wrong File Path",
                "title": "Passing an Incorrect or Mistyped File Path",
                "subtitle": "Python raises a FileNotFoundError because the file cannot be located.",
                "explanation": 'The path string must match the actual file location exactly — including folder names, spelling, and case. A single wrong character triggers <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">FileNotFoundError</code>.',
                "wrong_label": "wrong path",
                "wrong_code": 'df = pd.read_csv("data/Sale.csv")   # typo in filename',
                "correct_label": "exact path",
                "correct_code": 'df = pd.read_csv("data/sales.csv")  # matches the actual file\nprint(df.head())                     # confirm data loaded',
                "tip": "Copy the filename from your file explorer and paste it into the string. Your eyes will miss a typo; your clipboard will not.",
            },
            {
                "tab": "Wrong Separator",
                "title": "Loading a Semicolon-Delimited File Without Specifying sep",
                "subtitle": "All data lands in a single column because Pandas assumes commas.",
                "explanation": 'European CSV exports often use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">;</code> as the separator. Without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">sep=";"</code>, Pandas treats each row as one long string and creates one column.',
                "wrong_label": "default comma",
                "wrong_code": 'df = pd.read_csv("report.csv")\nprint(df.shape)   # (100, 1) — one column!',
                "correct_label": "set sep",
                "correct_code": 'df = pd.read_csv("report.csv", sep=";")  # match the delimiter\nprint(df.shape)                           # (100, 5) — correct',
                "tip": "Open the CSV in a plain text editor first. If you see semicolons between values instead of commas, you need <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">sep=\";\"</code>.",
            },
            {
                "tab": "Encoding Error",
                "title": "Loading a CSV With the Wrong Character Encoding",
                "subtitle": "Special characters appear garbled or Python raises a UnicodeDecodeError.",
                "explanation": 'Files created on older Windows systems often use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">latin-1</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">cp1252</code> encoding. Without specifying it, accented names appear as garbage characters.',
                "wrong_label": "default encoding",
                "wrong_code": 'df = pd.read_csv("clients.csv")\n# names show as Ã©, Ã±, Ã¼',
                "correct_label": "specify encoding",
                "correct_code": 'df = pd.read_csv("clients.csv",\n                  encoding="latin-1")  # match the source\nprint(df.head())                        # names display correctly',
                "tip": "If special characters look garbled, try <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">encoding=\"latin-1\"</code> first. It covers most Western European character sets.",
            },
        ],
    },

    # ── Lesson 02: Working With JSON Files ──
    "lesson02_working_with_json_files.html": {
        "topic": "JSON files",
        "mistakes": [
            {
                "tab": "Nested Data Flat",
                "title": "Loading Nested JSON Without Normalising It",
                "subtitle": "Nested dictionaries become a single column of objects instead of separate columns.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_json()</code> keeps nested keys as dictionary objects. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.json_normalize()</code> to flatten nested structures into separate columns.',
                "wrong_label": "nested stays nested",
                "wrong_code": 'df = pd.read_json("orders.json")\nprint(df["address"])   # column of dict objects',
                "correct_label": "normalise first",
                "correct_code": 'import json                                    # load raw JSON\nwith open("orders.json") as f:                  # open the file\n    raw = json.load(f)                           # parse JSON\ndf = pd.json_normalize(raw)                     # flatten nested keys\nprint(df.columns.tolist())                       # address.city, etc.',
                "tip": "If you see curly braces <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">{}</code> inside a cell, the data is nested. Switch to <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">json_normalize()</code> to unpack it.",
            },
            {
                "tab": "Wrong Orient",
                "title": "Mismatching the orient Parameter With the JSON Structure",
                "subtitle": "Pandas raises a ValueError or creates a DataFrame with wrong dimensions.",
                "explanation": 'JSON files can store data as a list of records, a dictionary of columns, or several other layouts. The <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">orient</code> parameter must match the actual structure.',
                "wrong_label": "wrong orient",
                "wrong_code": 'df = pd.read_json("data.json", orient="columns")\n# ValueError or wrong shape',
                "correct_label": "match orient",
                "correct_code": 'df = pd.read_json("data.json", orient="records")  # matches file\nprint(df.shape)                                     # correct shape',
                "tip": "Open the JSON file and look at the first character. <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">[</code> usually means <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">orient=\"records\"</code>. <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">{</code> usually means <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">orient=\"columns\"</code> or <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">orient=\"index\"</code>.",
            },
            {
                "tab": "Encoding Mismatch",
                "title": "Loading a Non-UTF-8 JSON File Without Specifying Encoding",
                "subtitle": "Python raises a UnicodeDecodeError when the file uses a different encoding.",
                "explanation": 'JSON should be UTF-8 by convention, but files exported from legacy tools may use other encodings. Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">encoding</code> to handle them.',
                "wrong_label": "default encoding",
                "wrong_code": 'df = pd.read_json("legacy.json")\n# UnicodeDecodeError',
                "correct_label": "specify encoding",
                "correct_code": 'df = pd.read_json("legacy.json",\n                   encoding="latin-1")  # match the source\nprint(df.head())                         # reads cleanly',
                "tip": "If you get a UnicodeDecodeError in the first line of your script, the encoding is the culprit. Try <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">latin-1</code> or <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">utf-8-sig</code>.",
            },
        ],
    },

    # ── Lesson 03: Connecting to Databases ──
    "lesson03_connecting_to_databases.html": {
        "topic": "database connections",
        "mistakes": [
            {
                "tab": "Wrong Connection String",
                "title": "Using an Incorrect Connection String Format",
                "subtitle": "SQLAlchemy raises an ArgumentError because it cannot parse the URL.",
                "explanation": 'Each database type needs a specific URL prefix. SQLite uses <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">sqlite:///</code> (three slashes for relative path). PostgreSQL uses <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">postgresql://</code>. A wrong prefix triggers <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ArgumentError</code>.',
                "wrong_label": "wrong prefix",
                "wrong_code": 'engine = create_engine("sqlite://data.db")\n# ArgumentError — missing a slash',
                "correct_label": "correct prefix",
                "correct_code": 'from sqlalchemy import create_engine              # import first\nengine = create_engine("sqlite:///data.db")       # three slashes\nprint(engine)                                      # confirms connection',
                "tip": "Count the slashes: <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">sqlite:///</code> means \"protocol + empty host + relative path\". Two slashes is never enough for SQLite.",
            },
            {
                "tab": "No Context Manager",
                "title": "Opening a Connection Without Closing It",
                "subtitle": "Open connections pile up and may lock the database or exhaust server resources.",
                "explanation": 'Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">engine.connect()</code> without a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">with</code> block leaves the connection open. Use a context manager to close it automatically.',
                "wrong_label": "no close",
                "wrong_code": 'conn = engine.connect()\ndf = pd.read_sql("SELECT * FROM sales", conn)\n# connection stays open forever',
                "correct_label": "use with block",
                "correct_code": 'with engine.connect() as conn:                # auto-closes\n    df = pd.read_sql("SELECT * FROM sales", conn)\nprint(df.shape)                                # connection closed here',
                "tip": "A <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">with</code> block is like a self-closing door — you walk through, do your work, and the door shuts behind you without you remembering to close it.",
            },
            {
                "tab": "Missing Driver",
                "title": "Forgetting to Install the Database Driver Package",
                "subtitle": "Python raises a ModuleNotFoundError or SQLAlchemy cannot find the dialect.",
                "explanation": 'SQLAlchemy needs a separate driver for each database — <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">psycopg2</code> for PostgreSQL, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pymysql</code> for MySQL. Without the driver installed, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">create_engine()</code> fails.',
                "wrong_label": "driver missing",
                "wrong_code": 'engine = create_engine("postgresql://user:pw@host/db")\n# ModuleNotFoundError: No module named psycopg2',
                "correct_label": "install driver",
                "correct_code": '# first, in terminal: pip install psycopg2-binary\nfrom sqlalchemy import create_engine                 # import\nengine = create_engine("postgresql://user:pw@host/db") # works now',
                "tip": "Check the SQLAlchemy docs for your database type. Each has a recommended driver package you need to <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pip install</code> once.",
            },
        ],
    },

    # ── Lesson 04: Running SQL in Python ──
    "lesson04_running_sql_in_python.html": {
        "topic": "running SQL queries in Python",
        "mistakes": [
            {
                "tab": "String Injection",
                "title": "Building SQL With f-strings Instead of Parameters",
                "subtitle": "F-string queries are vulnerable to SQL injection and introduce quoting bugs.",
                "explanation": 'Pasting user values directly into a SQL string opens the door to SQL injection — a security attack where malicious input rewrites your query. Always use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">params</code> to pass values safely.',
                "wrong_label": "f-string injection risk",
                "wrong_code": 'city = "London"\nquery = f"SELECT * FROM sales WHERE city = \'{city}\'"\ndf = pd.read_sql(query, conn)   # SQL injection risk',
                "correct_label": "use params",
                "correct_code": 'from sqlalchemy import text                       # safe SQL helper\nquery = text("SELECT * FROM sales WHERE city = :c") # placeholder\ndf = pd.read_sql(query, conn, params={"c": "London"}) # safe bind',
                "tip": "Parameters work like a form with labelled blanks — the database fills each blank safely without letting rogue input rewrite the query.",
            },
            {
                "tab": "No text() Wrapper",
                "title": "Passing a Raw String to read_sql With SQLAlchemy 2.x",
                "subtitle": "SQLAlchemy 2.x raises a RemovedIn20Warning or an error for raw string queries.",
                "explanation": 'SQLAlchemy 2.x requires queries to be wrapped in <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">text()</code>. A bare string triggers a deprecation warning or an outright error.',
                "wrong_label": "raw string",
                "wrong_code": 'df = pd.read_sql("SELECT * FROM sales", conn)\n# RemovedIn20Warning or error',
                "correct_label": "wrap in text()",
                "correct_code": 'from sqlalchemy import text                       # import helper\nquery = text("SELECT * FROM sales")                # wrap the string\ndf = pd.read_sql(query, conn)                      # no warning',
                "tip": "If you see \"RemovedIn20Warning\" in your output, wrap every SQL string in <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">text()</code>. It takes five seconds and silences the warning permanently.",
            },
            {
                "tab": "SELECT * Overload",
                "title": "Using SELECT * When You Only Need a Few Columns",
                "subtitle": "The query fetches every column, wasting memory and slowing down the read.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">SELECT *</code> loads all columns into memory. Name only the columns you need to reduce transfer time and DataFrame size.',
                "wrong_label": "select all",
                "wrong_code": 'query = text("SELECT * FROM sales")\ndf = pd.read_sql(query, conn)   # 50 columns loaded',
                "correct_label": "name columns",
                "correct_code": 'query = text("SELECT order_id, total FROM sales")  # 2 columns\ndf = pd.read_sql(query, conn)                        # smaller result\nprint(df.shape)                                       # fewer columns',
                "tip": "Fetching all columns from a large table is like photocopying an entire binder when you only need two pages. Name what you need in the SELECT list.",
            },
        ],
    },

    # ── Lesson 05: Writing Data Back to a Database ──
    "lesson05_writing_data_back_to_a_database.html": {
        "topic": "writing data to a database",
        "mistakes": [
            {
                "tab": "Table Overwrite",
                "title": "Using if_exists='replace' When You Meant to Append",
                "subtitle": "The existing table is dropped and recreated, deleting all previous rows.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">if_exists="replace"</code> drops the entire table first. If you want to add new rows to an existing table, use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"append"</code> instead.',
                "wrong_label": "replaces all data",
                "wrong_code": 'df.to_sql("sales", engine,\n          if_exists="replace")   # all old rows deleted',
                "correct_label": "append rows",
                "correct_code": 'df.to_sql("sales", engine,\n          if_exists="append",    # adds to existing rows\n          index=False)            # no extra index column',
                "tip": "Think of <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">replace</code> as \"delete and recreate\" and <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">append</code> as \"add to the bottom\". Choose carefully — there is no undo.",
            },
            {
                "tab": "Extra Index Column",
                "title": "Writing the DataFrame Index as an Extra Column",
                "subtitle": "The database table gets a nameless column of row numbers you did not intend.",
                "explanation": 'By default, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_sql()</code> writes the DataFrame index as the first column. Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">index=False</code> to exclude it.',
                "wrong_label": "index included",
                "wrong_code": 'df.to_sql("sales", engine,\n          if_exists="append")  # adds 0, 1, 2… column',
                "correct_label": "no index",
                "correct_code": 'df.to_sql("sales", engine,\n          if_exists="append",\n          index=False)          # clean table, no extra column',
                "tip": "Unless your index carries meaning (like a date), always pass <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">index=False</code>. Database tables have their own primary keys.",
            },
            {
                "tab": "Type Mismatch",
                "title": "Inserting Data With Mismatched Column Types",
                "subtitle": "The database raises an IntegrityError or silently truncates values.",
                "explanation": 'If a DataFrame column holds strings but the database column expects integers, the insert fails. Check <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.dtypes</code> and convert before writing.',
                "wrong_label": "type clash",
                "wrong_code": 'df["order_total"] = "150"            # string, not number\ndf.to_sql("orders", engine,\n          if_exists="append")         # IntegrityError',
                "correct_label": "convert first",
                "correct_code": 'df["order_total"] = pd.to_numeric(\n    df["order_total"])                # ensure numeric\ndf.to_sql("orders", engine,\n          if_exists="append",\n          index=False)                 # matches the schema',
                "tip": "Run <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">df.dtypes</code> before every <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">to_sql()</code> call. If a column says <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">object</code>, it is probably text and needs conversion.",
            },
        ],
    },

    # ── Lesson 06: Managing Credentials & .env ──
    "lesson06_managing_credentials_env.html": {
        "topic": "managing credentials and .env files",
        "mistakes": [
            {
                "tab": "Hardcoded Password",
                "title": "Pasting Credentials Directly Into Source Code",
                "subtitle": "Anyone who reads the file — or your Git history — can see the password.",
                "explanation": 'Hardcoded passwords in Python files get committed to Git and shared with every collaborator. Store secrets in a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> file and load them with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">os.getenv()</code>.',
                "wrong_label": "password in code",
                "wrong_code": 'engine = create_engine(\n    "postgresql://admin:S3cret!@host/db")  # exposed',
                "correct_label": "use .env",
                "correct_code": 'import os                                         # standard library\ndb_pass = os.getenv("DB_PASSWORD")                 # read from .env\nengine = create_engine(\n    f"postgresql://admin:{db_pass}@host/db")        # secret hidden',
                "tip": "Treat passwords like house keys — keep them in your pocket (<code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.env</code>), never taped to the front door (source code).",
            },
            {
                "tab": "No .gitignore",
                "title": "Committing the .env File to Git",
                "subtitle": "The secrets are pushed to the remote repository and visible to everyone with access.",
                "explanation": 'Adding <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> to version control defeats the purpose of environment variables. Add <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> to your <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.gitignore</code> before the first commit.',
                "wrong_label": ".env committed",
                "wrong_code": 'git add .\ngit commit -m "add config"   # .env is included!',
                "correct_label": "add to .gitignore",
                "correct_code": '# in .gitignore file, add this line:\n.env                                  # never track secrets\n# then commit — .env is excluded',
                "tip": "Add <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.env</code> to <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.gitignore</code> as the very first step of a new project. Removing a secret from Git history later is painful.",
            },
            {
                "tab": "Missing dotenv Load",
                "title": "Calling os.getenv() Without Loading the .env File First",
                "subtitle": "os.getenv() returns None because the .env values are not in memory.",
                "explanation": 'The <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> file is not read automatically. You must call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">load_dotenv()</code> from the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">python-dotenv</code> package first, or the variables return <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">None</code>.',
                "wrong_label": "returns None",
                "wrong_code": 'import os\ndb_pass = os.getenv("DB_PASSWORD")\nprint(db_pass)   # None',
                "correct_label": "load first",
                "correct_code": 'from dotenv import load_dotenv         # pip install python-dotenv\nimport os\nload_dotenv()                           # reads .env into memory\ndb_pass = os.getenv("DB_PASSWORD")      # now returns the value',
                "tip": "Think of <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">load_dotenv()</code> as opening an envelope. The secrets are written inside, but you must open it before you can read them.",
            },
        ],
    },
}

# ── mod_03: Python for Analysts ───────────────────────────────────────

MOD03_LESSONS = {

    # ── Lesson 01: Why Analysts Use Python ──
    "lesson01_why_analysts_use_python.html": {
        "topic": "choosing Python for analysis work",
        "mistakes": [
            {
                "tab": "Replace Everything",
                "title": "Expecting Python to Replace Every Existing Tool",
                "subtitle": "Python complements Excel and SQL — it does not eliminate the need for them.",
                "explanation": 'Python is best for automation, large datasets, and reproducible workflows. Quick ad-hoc lookups are often faster in Excel or SQL. Use each tool where it excels.',
                "wrong_label": "force Python everywhere",
                "wrong_code": '# rewriting a simple 5-row lookup in Python\ndf = pd.read_csv("data.csv")          # overkill\nprint(df[df["ID"] == 42]["Name"])      # Excel was faster',
                "correct_label": "right tool for the job",
                "correct_code": '# Python shines with repeatable large-scale work\ndf = pd.read_csv("transactions.csv")   # 500K rows\nsummary = df.groupby("Region").sum()    # instant aggregation\nsummary.to_excel("report.xlsx")         # automated export',
                "tip": "Ask yourself: \"Will I do this more than once?\" or \"Is the data too big for a spreadsheet?\" If yes, use Python. If it is five rows and one-off, open Excel.",
            },
            {
                "tab": "Overcomplicating",
                "title": "Writing Complex Code for a Task Excel Handles in Seconds",
                "subtitle": "A 20-line script for a one-off sum wastes time Python is meant to save.",
                "explanation": 'Python saves time through automation and repeatability. If a task takes 30 seconds in Excel and you will never repeat it, the Excel route is better.',
                "wrong_label": "one-off in Python",
                "wrong_code": 'df = pd.read_csv("five_items.csv")\ntotal = df["Price"].sum()\nprint(total)   # 3 lines for one number',
                "correct_label": "automate the repeated task",
                "correct_code": '# automate a weekly report across 12 files\nfor month_file in monthly_files:              # loop each file\n    df = pd.read_csv(month_file)              # load month data\n    df.groupby("Team").sum().to_excel(         # aggregate + save\n        f"summary_{month_file}")               # one file per month',
                "tip": "Python's strength is not doing one thing faster — it is doing the same thing hundreds of times without you lifting a finger.",
            },
            {
                "tab": "Skipping Exploration",
                "title": "Jumping Straight Into Code Without Exploring the Data First",
                "subtitle": "Errors appear deep in the pipeline because assumptions about the data were wrong.",
                "explanation": 'Always start with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.head()</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.info()</code>, and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.describe()</code> before writing transformation code. These three commands reveal missing values, wrong types, and unexpected ranges.',
                "wrong_label": "code blindly",
                "wrong_code": 'df = pd.read_csv("data.csv")\ndf["Revenue"] = df["Qty"] * df["Price"]  # crashes — Qty is text',
                "correct_label": "explore first",
                "correct_code": 'df = pd.read_csv("data.csv")   # load data\nprint(df.info())                # check types and nulls\nprint(df.describe())            # check numeric ranges\nprint(df.head())                # eyeball the first rows',
                "tip": "Spending sixty seconds on <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">info()</code> and <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">describe()</code> saves sixty minutes of debugging later.",
            },
        ],
    },

    # ── Lesson 02: Replacing Excel Workflows ──
    "lesson02_replacing_excel_workflows_with_python.html": {
        "topic": "replacing Excel workflows with Python",
        "mistakes": [
            {
                "tab": "VLOOKUP Mindset",
                "title": "Trying to Recreate VLOOKUP Instead of Using merge()",
                "subtitle": "Looping row-by-row to match values is extremely slow on large datasets.",
                "explanation": 'Excel\'s VLOOKUP scans one row at a time. Python\'s <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.merge()</code> joins entire tables at once and is orders of magnitude faster.',
                "wrong_label": "row-by-row loop",
                "wrong_code": 'for idx, row in orders.iterrows():          # very slow\n    match = lookup[lookup["ID"] == row["ID"]]\n    orders.at[idx, "Name"] = match["Name"].values[0]',
                "correct_label": "use merge()",
                "correct_code": 'merged = orders.merge(lookup,               # join tables\n                      on="ID",              # match key\n                      how="left")            # keep all orders\nprint(merged.head())                         # instant result',
                "tip": "Every time you think \"VLOOKUP\", type <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">merge()</code> instead. It does the same lookup for every row in a single operation.",
            },
            {
                "tab": "Pivot Table Confusion",
                "title": "Using groupby() When pivot_table() Matches the Excel Mental Model",
                "subtitle": "The output shape does not match the cross-tab layout you expected from Excel.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">groupby()</code> produces a long, stacked result. If you want rows and columns like an Excel Pivot Table, use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.pivot_table()</code>.',
                "wrong_label": "long format only",
                "wrong_code": 'summary = df.groupby(["Region", "Product"]).sum()\n# nested index — hard to read as a cross-tab',
                "correct_label": "use pivot_table",
                "correct_code": 'summary = pd.pivot_table(df,\n    values="Sales",                # what to aggregate\n    index="Region",                # row labels\n    columns="Product",             # column headers\n    aggfunc="sum")                 # sum each cell\nprint(summary)                     # cross-tab layout',
                "tip": "If you want the result to look like an Excel Pivot Table — with row headers on the left and category headers across the top — reach for <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pivot_table()</code>.",
            },
            {
                "tab": "Manual Formatting",
                "title": "Formatting Numbers in Python Instead of in the Output File",
                "subtitle": "Rounding or formatting strings inside the DataFrame loses numeric precision.",
                "explanation": 'Apply formatting at the export step, not inside the DataFrame. Converting numbers to formatted strings prevents further calculations on those columns.',
                "wrong_label": "format too early",
                "wrong_code": 'df["Total"] = df["Total"].apply(\n    lambda v: f"${v:,.2f}")   # now a string — cannot sum',
                "correct_label": "format at export",
                "correct_code": 'df["Total"] = df["Price"] * df["Qty"]  # keep as number\ndf.to_excel("report.xlsx",\n            index=False,\n            float_format="%.2f")            # format on export only',
                "tip": "Keep your data numeric as long as possible — format it only at the very last step when writing to Excel or displaying on screen.",
            },
        ],
    },

    # ── Lesson 03: Using Python With SQL Queries ──
    "lesson03_using_python_with_sql_queries.html": {
        "topic": "Python and SQL together",
        "mistakes": [
            {
                "tab": "String Injection",
                "title": "Concatenating User Input Into a SQL String",
                "subtitle": "The query is vulnerable to SQL injection — a critical security risk.",
                "explanation": 'Never paste variables directly into SQL strings. Malicious input can rewrite the query. Use parameterised queries with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">params</code> to bind values safely.',
                "wrong_label": "string concat",
                "wrong_code": 'city = user_input\nquery = f"SELECT * FROM orders WHERE city = \'{city}\'"  # unsafe\ndf = pd.read_sql(query, conn)',
                "correct_label": "parameterised query",
                "correct_code": 'from sqlalchemy import text                            # safe helper\nquery = text("SELECT * FROM orders WHERE city = :c")    # placeholder\ndf = pd.read_sql(query, conn, params={"c": user_input}) # safe bind',
                "tip": "Parameters are like fill-in-the-blank forms — the database treats each value as data, never as executable code.",
            },
            {
                "tab": "Fetch All Rows",
                "title": "Loading an Entire Table When You Only Need a Filtered Subset",
                "subtitle": "Memory usage balloons because Python holds millions of unneeded rows.",
                "explanation": 'Filtering a large table in Python after loading all rows wastes memory. Move the filter into the SQL WHERE clause so the database does the work.',
                "wrong_label": "filter in Python",
                "wrong_code": 'query = text("SELECT * FROM orders")           # all rows\ndf = pd.read_sql(query, conn)\ndf = df[df["region"] == "EMEA"]                 # filter after load',
                "correct_label": "filter in SQL",
                "correct_code": 'query = text("SELECT * FROM orders WHERE region = :r")  # filtered\ndf = pd.read_sql(query, conn, params={"r": "EMEA"})      # less data\nprint(df.shape)                                           # smaller',
                "tip": "Let the database do the heavy lifting. A WHERE clause in SQL is always faster than loading everything and filtering in Python.",
            },
            {
                "tab": "Mixing Engines",
                "title": "Using a Different Connection Object Than the One That Created the Engine",
                "subtitle": "A stale or wrong connection object causes OperationalError or returns no data.",
                "explanation": 'Each <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">create_engine()</code> call targets one database. Passing a connection from engine A to a query meant for engine B silently fails or errors out. Keep engine and connection paired.',
                "wrong_label": "mismatched conn",
                "wrong_code": 'engine_a = create_engine("sqlite:///sales.db")\nengine_b = create_engine("sqlite:///hr.db")\nwith engine_a.connect() as conn:\n    df = pd.read_sql(query_for_hr, conn)  # wrong database',
                "correct_label": "match engine",
                "correct_code": 'with engine_b.connect() as conn:               # correct engine\n    df = pd.read_sql(query_for_hr, conn)       # right database\nprint(df.head())                                # expected data',
                "tip": "If your query returns zero rows when you know data exists, double-check which engine created the connection. It is the easiest mistake to overlook.",
            },
        ],
    },

    # ── Lesson 04: Automating Repetitive Data Tasks ──
    "lesson04_automating_repetitive_data_tasks.html": {
        "topic": "automating data tasks",
        "mistakes": [
            {
                "tab": "Hardcoded Paths",
                "title": "Hardcoding File Paths Instead of Using Patterns",
                "subtitle": "The script breaks the moment a new file is added or a name changes.",
                "explanation": 'Listing every filename by hand is fragile. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">glob.glob()</code> to match file patterns dynamically.',
                "wrong_label": "manual list",
                "wrong_code": 'files = ["jan.csv", "feb.csv", "mar.csv"]   # breaks in April\nfor f in files:\n    df = pd.read_csv(f)',
                "correct_label": "use glob",
                "correct_code": 'from glob import glob                    # pattern matcher\nfiles = glob("data/*.csv")               # finds all CSVs\nfor filepath in files:                    # loop dynamically\n    df = pd.read_csv(filepath)            # handles any new file',
                "tip": "<code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">glob()</code> is like telling your assistant \"process every CSV in this folder\" instead of handing them a handwritten list that goes stale.",
            },
            {
                "tab": "No Error Handling",
                "title": "Letting One Bad File Crash the Entire Loop",
                "subtitle": "A single corrupt file stops the script before it processes the remaining files.",
                "explanation": 'Without a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">try/except</code> block, one bad file raises an exception and halts everything. Wrap the loop body so the script skips failures and continues.',
                "wrong_label": "crash on error",
                "wrong_code": 'for filepath in files:\n    df = pd.read_csv(filepath)   # crashes on corrupt file\n    process(df)',
                "correct_label": "skip and log",
                "correct_code": 'for filepath in files:                     # loop all files\n    try:\n        df = pd.read_csv(filepath)         # attempt read\n        process(df)                         # do the work\n    except Exception as err:\n        print(f"Skipped {filepath}: {err}") # log and continue',
                "tip": "An automation script should be like a postman — if one letterbox is jammed, skip it and deliver the rest instead of going home.",
            },
            {
                "tab": "No Logging",
                "title": "Running a Script With No Output or Log Messages",
                "subtitle": "When something goes wrong, there is no trail to follow — nothing tells you what ran or failed.",
                "explanation": 'Silent scripts are hard to debug. Add <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">print()</code> statements (or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">logging</code>) at key steps so you can trace what happened after the script finishes.',
                "wrong_label": "silent script",
                "wrong_code": 'for filepath in files:\n    df = pd.read_csv(filepath)\n    df.to_excel(filepath.replace(".csv", ".xlsx"))',
                "correct_label": "log progress",
                "correct_code": 'for filepath in files:\n    print(f"Processing {filepath}...")       # log start\n    df = pd.read_csv(filepath)              # load\n    out = filepath.replace(".csv", ".xlsx")  # output name\n    df.to_excel(out, index=False)            # save\nprint(f"Done — {len(files)} files processed") # log total',
                "tip": "Print statements are breadcrumbs through the forest. When something goes wrong at 2 AM, those breadcrumbs show you exactly where the script stopped.",
            },
        ],
    },

    # ── Lesson 05: Building a Simple Reporting Script ──
    "lesson05_building_a_simple_reporting_script.html": {
        "topic": "building reporting scripts",
        "mistakes": [
            {
                "tab": "One Giant Block",
                "title": "Writing the Entire Script as One Long Block of Code",
                "subtitle": "A monolithic script is hard to debug, test, and reuse.",
                "explanation": 'Break the script into small functions — one for loading, one for transforming, one for exporting. Each function has a single job and can be tested independently.',
                "wrong_label": "monolithic script",
                "wrong_code": 'df = pd.read_csv("data.csv")\ndf = df[df["Status"] == "Active"]\ndf.groupby("Team").sum().to_excel("report.xlsx")',
                "correct_label": "use functions",
                "correct_code": 'def load_data(path):                           # step 1\n    return pd.read_csv(path)                    # single job\ndef build_summary(df):                          # step 2\n    active = df[df["Status"] == "Active"]        # filter\n    return active.groupby("Team").sum()          # aggregate',
                "tip": "Functions are like labelled drawers — if the load step breaks, you open only that drawer to fix it, instead of searching through the whole desk.",
            },
            {
                "tab": "No describe()",
                "title": "Skipping Summary Statistics Before Formatting the Report",
                "subtitle": "Outliers or missing values silently distort totals without you noticing.",
                "explanation": 'Run <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.describe()</code> before exporting to catch unexpected extremes or zero counts. A quick sanity check prevents misleading reports.',
                "wrong_label": "skip sanity check",
                "wrong_code": 'summary = df.groupby("Team")["Revenue"].sum()\nsummary.to_excel("report.xlsx")   # outliers hidden',
                "correct_label": "check first",
                "correct_code": 'print(df["Revenue"].describe())    # spot outliers first\nsummary = df.groupby("Team")["Revenue"].sum()  # aggregate\nprint(summary)                      # verify before export\nsummary.to_excel("report.xlsx", index=False)    # save clean',
                "tip": "A report is only as good as the data behind it. Running <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">describe()</code> is like proofreading before you hit Send.",
            },
            {
                "tab": "Hardcoded Dates",
                "title": "Hardcoding Report Dates Instead of Generating Them",
                "subtitle": "The script produces last month's filename every time it runs.",
                "explanation": 'Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">datetime</code> to build the report name automatically. Hardcoded date strings silently overwrite previous reports when you forget to update them.',
                "wrong_label": "static date",
                "wrong_code": 'df.to_excel("report_march.xlsx")   # wrong in April',
                "correct_label": "dynamic date",
                "correct_code": 'from datetime import date                      # date helper\ntoday = date.today().strftime("%Y-%m-%d")       # e.g. 2026-03-31\ndf.to_excel(f"report_{today}.xlsx",\n            index=False)                         # auto-versioned',
                "tip": "Let the code generate its own timestamps. You will never forget to update the month, and every run creates a uniquely named file.",
            },
        ],
    },

    # ── Lesson 06: Automating Reports End to End ──
    "lesson06_automating_reports_end_to_end.html": {
        "topic": "end-to-end report automation",
        "mistakes": [
            {
                "tab": "No try/except",
                "title": "Running an Entire Pipeline Without Error Handling",
                "subtitle": "One failure in the middle leaves the report half-finished with no notification.",
                "explanation": 'Wrap the pipeline in a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">try/except</code> block so failures are caught, logged, and — if an email step exists — reported automatically.',
                "wrong_label": "no error handling",
                "wrong_code": 'df = load_data()\nsummary = transform(df)\nexport(summary)\nsend_email(summary)   # crashes silently if transform fails',
                "correct_label": "wrap in try/except",
                "correct_code": 'try:\n    df = load_data()                # step 1\n    summary = transform(df)          # step 2\n    export(summary)                  # step 3\nexcept Exception as err:\n    print(f"Pipeline failed: {err}") # log the failure',
                "tip": "An automated pipeline that fails silently is worse than no automation. The <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">except</code> block is your smoke alarm.",
            },
            {
                "tab": "Email Credentials",
                "title": "Storing SMTP Credentials in the Script File",
                "subtitle": "The email password is visible to anyone who can read the code or Git history.",
                "explanation": 'Hard-coded SMTP passwords get committed to version control. Store them in a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> file and load with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">os.getenv()</code>.',
                "wrong_label": "password in code",
                "wrong_code": 'smtp_password = "MyS3cret!"          # exposed in source\nserver.login("me@co.com", smtp_password)',
                "correct_label": "use .env",
                "correct_code": 'import os                                    # standard library\nsmtp_password = os.getenv("SMTP_PASSWORD")   # from .env\nserver.login("me@co.com", smtp_password)      # secret hidden',
                "tip": "Never type a password inside a <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.py</code> file. Use a <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.env</code> file — and add it to <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.gitignore</code> immediately.",
            },
            {
                "tab": "Stale Data Path",
                "title": "Running the Pipeline on Yesterday's File Because the Path Is Hardcoded",
                "subtitle": "The export overwrites the previous report with the same stale data.",
                "explanation": 'If the input path never changes, the pipeline reprocesses old data every time. Generate the path dynamically from today\'s date or use the latest file in the folder.',
                "wrong_label": "hardcoded path",
                "wrong_code": 'df = pd.read_csv("data/march_extract.csv")  # stale in April',
                "correct_label": "dynamic path",
                "correct_code": 'from glob import glob                         # pattern matcher\nfiles = sorted(glob("data/*_extract.csv"))    # sorted by name\nlatest = files[-1]                             # pick the newest\ndf = pd.read_csv(latest)                       # always fresh data',
                "tip": "Sort the matching files and pick the last one. As long as your naming is chronological, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">files[-1]</code> always grabs the latest extract.",
            },
        ],
    },
}

# ── mod_04: Handling Large Data ───────────────────────────────────────

MOD04_LESSONS = {

    # ── Lesson 02: Memory Optimization ──
    "lesson02_memory_optimization.html": {
        "topic": "memory optimisation",
        "mistakes": [
            {
                "tab": "Default dtypes",
                "title": "Loading Data With Default int64 and float64 Types",
                "subtitle": "Each column uses 8 bytes per value when 1–4 bytes would suffice.",
                "explanation": 'Pandas defaults to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int64</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">float64</code>. Downcasting to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int32</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">float32</code> can cut memory use in half with no precision loss for most analytics.',
                "wrong_label": "default 64-bit",
                "wrong_code": 'df = pd.read_csv("big_data.csv")\nprint(df.memory_usage(deep=True).sum())  # very large',
                "correct_label": "downcast types",
                "correct_code": 'df = pd.read_csv("big_data.csv")               # load first\ndf["age"] = pd.to_numeric(\n    df["age"], downcast="integer")               # int64 → int8\nprint(df.memory_usage(deep=True).sum())          # much smaller',
                "tip": "Downcasting is like choosing a carry-on bag instead of a suitcase when you only have a few items. Same contents, less space.",
            },
            {
                "tab": "Object Columns",
                "title": "Leaving Repeated Text as object Instead of category",
                "subtitle": "Object columns store every string separately, consuming far more memory than necessary.",
                "explanation": 'A column with few unique values (like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"Yes"</code>/<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"No"</code> or country names) wastes memory as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">object</code>. Converting to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">category</code> stores each unique value once.',
                "wrong_label": "object type",
                "wrong_code": 'print(df["country"].dtype)        # object — full string copy\nprint(df["country"].memory_usage(deep=True))  # 8 MB',
                "correct_label": "use category",
                "correct_code": 'df["country"] = df["country"].astype("category")  # convert\nprint(df["country"].dtype)                          # category\nprint(df["country"].memory_usage(deep=True))         # 0.5 MB',
                "tip": "If a column has fewer than ~1,000 unique values out of millions of rows, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">category</code> is almost always a win.",
            },
            {
                "tab": "Optimise Blind",
                "title": "Optimising Before Measuring Current Memory Usage",
                "subtitle": "You waste time converting columns that were already small.",
                "explanation": 'Always run <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.memory_usage(deep=True)</code> first to find the biggest offenders. Optimise the largest columns first for the biggest gains.',
                "wrong_label": "guess and convert",
                "wrong_code": 'df["id"] = df["id"].astype("int8")         # already tiny\ndf["flag"] = df["flag"].astype("category") # already tiny',
                "correct_label": "measure first",
                "correct_code": 'mem = df.memory_usage(deep=True)    # measure each column\nprint(mem.sort_values(ascending=False).head())  # biggest first\n# then optimise only the top offenders',
                "tip": "Measuring before optimising is like checking your bank statement before cutting expenses. Fix the biggest leak first.",
            },
        ],
    },

    # ── Lesson 03: Chunk Processing ──
    "lesson03_chunk_processing.html": {
        "topic": "chunk processing",
        "mistakes": [
            {
                "tab": "No Chunksize",
                "title": "Loading a Massive CSV Into Memory All at Once",
                "subtitle": "Python runs out of memory and crashes with a MemoryError.",
                "explanation": 'Files larger than available RAM cannot be loaded in one call. Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">chunksize</code> to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read_csv()</code> to process the file in smaller pieces.',
                "wrong_label": "load all at once",
                "wrong_code": 'df = pd.read_csv("huge_file.csv")  # MemoryError\nprint(df.shape)',
                "correct_label": "use chunksize",
                "correct_code": 'chunks = pd.read_csv("huge_file.csv",\n                     chunksize=100_000)  # 100K rows at a time\nfor chunk in chunks:\n    print(chunk.shape)                    # process each piece',
                "tip": "Chunking is like reading a book one chapter at a time instead of memorising the entire thing before you start.",
            },
            {
                "tab": "Append in Loop",
                "title": "Growing a List in a Loop and Concatenating at the End",
                "subtitle": "Appending DataFrames inside a loop is slow and doubles memory at concat time.",
                "explanation": 'Storing each chunk result in a list and calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.concat()</code> at the end temporarily doubles memory. Aggregate each chunk independently and combine only the small summaries.',
                "wrong_label": "collect all chunks",
                "wrong_code": 'parts = []\nfor chunk in chunks:\n    parts.append(chunk)              # stores everything\ndf = pd.concat(parts)                # doubles memory',
                "correct_label": "aggregate per chunk",
                "correct_code": 'totals = []\nfor chunk in chunks:\n    summary = chunk.groupby("Region")["Sales"].sum()  # small result\n    totals.append(summary)                             # tiny piece\nfinal = pd.concat(totals).groupby(level=0).sum()       # combine sums',
                "tip": "Process each chunk down to a small result before collecting it. Storing 100 tiny summaries uses far less memory than storing 100 full chunks.",
            },
            {
                "tab": "Wrong Chunk Size",
                "title": "Choosing a Chunk Size That Is Too Small or Too Large",
                "subtitle": "Too small wastes time on overhead; too large triggers MemoryError.",
                "explanation": 'A chunk of 10 rows creates millions of iterations. A chunk of 10 million rows may still exceed memory. Start with 100,000–500,000 rows and adjust based on <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">memory_usage()</code>.',
                "wrong_label": "too small",
                "wrong_code": 'chunks = pd.read_csv("huge.csv",\n                     chunksize=10)   # millions of iterations',
                "correct_label": "reasonable size",
                "correct_code": 'chunks = pd.read_csv("huge.csv",\n                     chunksize=200_000)  # balanced choice\nfor chunk in chunks:\n    print(chunk.memory_usage(deep=True).sum())  # monitor usage',
                "tip": "Start at 100,000 rows. If each chunk fits comfortably in memory and the loop finishes in reasonable time, you have found a good balance.",
            },
        ],
    },

    # ── Lesson 04: Processing Millions of Rows ──
    "lesson04_processing_millions_of_rows.html": {
        "topic": "processing millions of rows",
        "mistakes": [
            {
                "tab": "iterrows() Loop",
                "title": "Using iterrows() to Process Every Row One at a Time",
                "subtitle": "Row-by-row iteration is hundreds of times slower than vectorised operations.",
                "explanation": 'Pandas is built for column-wide operations. <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">iterrows()</code> converts each row to a Series, which is extremely slow on millions of rows. Use vectorised expressions instead.',
                "wrong_label": "iterrows loop",
                "wrong_code": 'for idx, row in df.iterrows():               # very slow\n    df.at[idx, "total"] = row["qty"] * row["price"]',
                "correct_label": "vectorised",
                "correct_code": 'df["total"] = df["qty"] * df["price"]  # instant on millions\nprint(df["total"].head())               # verify result',
                "tip": "Vectorised operations process the entire column at once, like stamping a sheet of labels instead of writing each one by hand.",
            },
            {
                "tab": "apply() Overuse",
                "title": "Using apply() When a Built-In Method Exists",
                "subtitle": "apply() runs a Python function per row, bypassing Pandas' fast C engine.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">apply()</code> is flexible but slow. If Pandas has a built-in method for the operation — like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.str.upper()</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.fillna()</code> — always use the built-in.',
                "wrong_label": "apply for upper",
                "wrong_code": 'df["name"] = df["name"].apply(lambda v: v.upper())  # slow',
                "correct_label": "built-in method",
                "correct_code": 'df["name"] = df["name"].str.upper()  # fast vectorised method\nprint(df["name"].head())              # same result, much faster',
                "tip": "Before writing <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">apply()</code>, search the Pandas docs for a built-in method. Nine times out of ten, one exists and runs faster.",
            },
            {
                "tab": "No Timing Check",
                "title": "Assuming Code Is Fast Without Measuring It",
                "subtitle": "A slow operation hides inside the script because nothing reports how long it took.",
                "explanation": 'Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">%%timeit</code> in a notebook or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">time.perf_counter()</code> in a script to measure execution time. You cannot optimise what you do not measure.',
                "wrong_label": "no measurement",
                "wrong_code": 'df["total"] = df["qty"] * df["price"]\n# no idea how long this took',
                "correct_label": "time it",
                "correct_code": 'import time                                  # timing helper\nstart = time.perf_counter()                   # start clock\ndf["total"] = df["qty"] * df["price"]         # operation\nelapsed = time.perf_counter() - start          # stop clock\nprint(f"Took {elapsed:.2f}s")                  # report duration',
                "tip": "Adding two lines of timing code costs almost nothing but tells you immediately whether your change made things faster or slower.",
            },
        ],
    },

    # ── Lesson 05: Columnar Storage ──
    "lesson05_columnar_storage.html": {
        "topic": "columnar storage formats",
        "mistakes": [
            {
                "tab": "CSV for Analytics",
                "title": "Using CSV for Large Analytical Workloads",
                "subtitle": "CSV files are slow to read and large on disk because they store every value as text.",
                "explanation": 'CSV is row-based text. Columnar formats like Parquet store data by column and compress it. Reading two columns from a Parquet file is much faster than parsing an entire CSV.',
                "wrong_label": "CSV for big data",
                "wrong_code": 'df = pd.read_csv("sales.csv")         # slow — parses all text\nprint(df[["Region", "Total"]].head())  # only needed 2 columns',
                "correct_label": "use Parquet",
                "correct_code": 'df = pd.read_parquet("sales.parquet",\n    columns=["Region", "Total"])  # reads only 2 columns\nprint(df.head())                      # instantly loaded',
                "tip": "Parquet reads only the columns you ask for. CSV reads everything and throws the rest away. For large files, the speed difference is enormous.",
            },
            {
                "tab": "Type Loss on CSV",
                "title": "Losing Column Types When Round-Tripping Through CSV",
                "subtitle": "Dates become strings and categories become objects after a CSV save and reload.",
                "explanation": 'CSV has no type metadata. A <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">datetime64</code> column saved to CSV loads back as a string. Parquet preserves types automatically.',
                "wrong_label": "CSV loses types",
                "wrong_code": 'df.to_csv("data.csv", index=False)\ndf2 = pd.read_csv("data.csv")\nprint(df2["date"].dtype)   # object — was datetime64',
                "correct_label": "Parquet keeps types",
                "correct_code": 'df.to_parquet("data.parquet")             # saves with types\ndf2 = pd.read_parquet("data.parquet")      # loads with types\nprint(df2["date"].dtype)                    # datetime64 — preserved',
                "tip": "If you save to CSV and reload, you lose type information — like photocopying a colour document in black-and-white. Parquet keeps full fidelity.",
            },
            {
                "tab": "Ignoring Columns Param",
                "title": "Reading an Entire Parquet File When You Only Need a Few Columns",
                "subtitle": "Memory usage balloons because all columns are loaded into the DataFrame.",
                "explanation": 'Parquet supports column-level reads. Passing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">columns=[...]</code> skips the rest on disk, saving both time and memory.',
                "wrong_label": "all columns loaded",
                "wrong_code": 'df = pd.read_parquet("big.parquet")    # loads all 100 columns\nprint(df[["date", "total"]].head())     # only needed 2',
                "correct_label": "select columns",
                "correct_code": 'df = pd.read_parquet("big.parquet",\n    columns=["date", "total"])   # only loads 2 columns\nprint(df.head())                      # fast and lean',
                "tip": "Name the columns you need upfront. Parquet physically skips the ones you did not list — you get speed and memory savings in one parameter.",
            },
        ],
    },

    # ── Lesson 06: Parquet Files ──
    "lesson06_parquet_files.html": {
        "topic": "Parquet files",
        "mistakes": [
            {
                "tab": "Missing Engine",
                "title": "Calling to_parquet() Without a Parquet Engine Installed",
                "subtitle": "Python raises an ImportError because neither pyarrow nor fastparquet is available.",
                "explanation": 'Pandas needs a Parquet engine — either <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pyarrow</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">fastparquet</code>. Without one, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_parquet()</code> raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ImportError</code>. Install one with pip.',
                "wrong_label": "no engine",
                "wrong_code": 'df.to_parquet("output.parquet")\n# ImportError: Missing optional dependency pyarrow',
                "correct_label": "install engine",
                "correct_code": '# first in terminal: pip install pyarrow\ndf.to_parquet("output.parquet",\n              engine="pyarrow")     # explicit engine\nprint("Parquet file saved")          # confirm',
                "tip": "Run <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pip install pyarrow</code> once in your virtual environment. It is the most widely used Parquet engine and installs in seconds.",
            },
            {
                "tab": "Wrong Extension",
                "title": "Saving a Parquet File With a .csv Extension",
                "subtitle": "Other tools treat the file as CSV and fail to parse the binary Parquet format.",
                "explanation": 'Parquet is a binary format. Giving it a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.csv</code> extension confuses colleagues and downstream tools that rely on the extension to choose a reader.',
                "wrong_label": "wrong extension",
                "wrong_code": 'df.to_parquet("data.csv")   # binary data, csv extension',
                "correct_label": "correct extension",
                "correct_code": 'df.to_parquet("data.parquet")  # extension matches format\nprint("Saved as .parquet")      # clear for all consumers',
                "tip": "File extensions are labels on boxes. A label that says \"CSV\" on a box that contains binary Parquet data will confuse everyone who picks it up.",
            },
            {
                "tab": "No Compression",
                "title": "Saving Large Parquet Files Without Compression",
                "subtitle": "The file is larger than necessary, wasting disk space and slowing transfers.",
                "explanation": 'Parquet supports built-in compression. The default is usually <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">snappy</code>, which is fast. For maximum compression, use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">gzip</code>.',
                "wrong_label": "no compression",
                "wrong_code": 'df.to_parquet("data.parquet",\n              compression=None)   # file is 2 GB',
                "correct_label": "enable compression",
                "correct_code": 'df.to_parquet("data.parquet",\n              compression="snappy")  # fast + compressed\nprint("Compressed Parquet saved")     # typically 30-50% smaller',
                "tip": "Snappy compression adds almost no time to the write but typically cuts file size by 30–50%. There is almost never a reason to turn it off.",
            },
        ],
    },

    # ── Lesson 13: Performance Profiling ──
    "lesson13_performance_profiling.html": {
        "topic": "performance profiling",
        "mistakes": [
            {
                "tab": "Guessing Bottleneck",
                "title": "Optimising Code Without Profiling It First",
                "subtitle": "You waste time speeding up a fast section while the real bottleneck stays slow.",
                "explanation": 'Run <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">cProfile</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">%%timeit</code> before changing anything. Profiling shows where the time actually goes, not where you think it goes.',
                "wrong_label": "guess and change",
                "wrong_code": 'df["name"] = df["name"].str.strip()     # fast — 0.01s\n# you optimised this, but the real bottleneck is below\ndf = df.merge(lookup, on="id")           # slow — 12s',
                "correct_label": "profile first",
                "correct_code": 'import cProfile                            # built-in profiler\ncProfile.run(\'run_pipeline()\')             # shows time per call\n# then fix only the slowest function',
                "tip": "Profiling is like an X-ray for your code. It shows you exactly which bone is broken instead of guessing from the outside.",
            },
            {
                "tab": "Timing One Run",
                "title": "Timing a Single Execution and Trusting the Result",
                "subtitle": "A single run includes warm-up time and random system noise.",
                "explanation": 'One measurement is unreliable. Background processes and caching distort the result. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">timeit</code> with multiple iterations for a stable average.',
                "wrong_label": "single run",
                "wrong_code": 'import time\nstart = time.time()\ndf["total"] = df["qty"] * df["price"]\nprint(time.time() - start)   # one noisy sample',
                "correct_label": "multiple runs",
                "correct_code": 'import timeit                                  # benchmarking tool\nt = timeit.timeit(\n    \'df["total"] = df["qty"] * df["price"]\',\n    globals=globals(), number=100)              # 100 runs\nprint(f"Avg: {t/100:.4f}s")                     # stable average',
                "tip": "Running a benchmark once is like weighing yourself right after a big meal. Multiple measurements give you the true number.",
            },
            {
                "tab": "Micro-Optimise",
                "title": "Micro-Optimising Fast Code While Ignoring Slow I/O",
                "subtitle": "Shaving milliseconds off an in-memory calculation while the CSV read takes 30 seconds.",
                "explanation": 'Disk I/O and database queries are almost always the slowest parts of a data pipeline. Optimise those first — switch CSV reads to Parquet, add SQL indexes, or reduce columns.',
                "wrong_label": "optimise the wrong part",
                "wrong_code": 'df = pd.read_csv("huge.csv")        # 30 seconds — ignored\ndf["x"] = df["a"] + df["b"]         # 0.01s — you optimised this',
                "correct_label": "fix the slow part",
                "correct_code": 'df = pd.read_parquet("huge.parquet",\n    columns=["a", "b"])              # 2 seconds — 15x faster\ndf["x"] = df["a"] + df["b"]          # 0.01s — already fast',
                "tip": "Profile first, then fix the biggest number. A 30-second CSV read dwarfs every in-memory tweak you could ever make.",
            },
        ],
    },
}


# ── HTML builders (same as mod01) ──────────────────────────────────────

def build_tab_pill(idx: int, tab_label: str, active: bool) -> str:
    if active:
        return (
            f'  <button onclick="switchMkTab({idx})" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">\n'
            f'    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
            f'    <span class="mk-step-label text-xs font-bold">{tab_label}</span>\n'
            f'  </button>'
        )
    return (
        f'  <button onclick="switchMkTab({idx})" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">\n'
        f'    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
        f'    <span class="mk-step-label text-xs font-bold">{tab_label}</span>\n'
        f'  </button>'
    )


def build_panel(idx: int, mk: dict) -> str:
    hidden = "" if idx == 0 else " hidden"
    return f'''<div class="mk-panel mk-panel-anim{hidden}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

    <!-- Card header -->
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["subtitle"]}</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>

    <!-- Explanation paragraph -->
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">{mk["explanation"]}</p>
    </div>

    <!-- Wrong / Correct split panel -->
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — {mk["wrong_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["wrong_code"]}</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — {mk["correct_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["correct_code"]}</code></pre>
        </div>
      </div>
    </div>

    <!-- Amber tip footer -->
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["tip"]}</p>
    </div>

  </div>
</div>'''


def build_section(topic: str, mistakes: list[dict]) -> str:
    pills = "\n".join(
        build_tab_pill(i, mk["tab"], i == 0)
        for i, mk in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{pills}\n</div>'

    panels = "\n\n".join(
        build_panel(i, mk)
        for i, mk in enumerate(mistakes)
    )

    return f'''<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with {topic}</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

      {tab_row}

      {panels}

    </div>
  </div>
</section>'''


# ── Apply ──────────────────────────────────────────────────────────────

def apply_module(mod_dir: pathlib.Path, lessons: dict) -> int:
    updated = 0
    for filename, content in lessons.items():
        path = mod_dir / filename
        if not path.exists():
            print(f"  ❌ {filename} — file not found")
            continue

        html = path.read_text(encoding="utf-8")
        new_section = build_section(content["topic"], content["mistakes"])
        new_html, count = SECTION_RE.subn(new_section, html)

        if count == 0:
            print(f'  ⚠️  {filename} — <section id="mistakes"> not found')
            continue

        path.write_text(new_html, encoding="utf-8")
        print(f"  ✅ {filename}")
        updated += 1
    return updated


def main():
    total = 0

    print("\n── mod_02: Working With Data Sources ──")
    total += apply_module(
        T2 / "mod_02_working_with_data_sources", MOD02_LESSONS)

    print("\n── mod_03: Python for Analysts ──")
    total += apply_module(
        T2 / "mod_03_python_for_analysts", MOD03_LESSONS)

    print("\n── mod_04: Handling Large Data ──")
    total += apply_module(
        T2 / "mod_04_handling_large_data", MOD04_LESSONS)

    print(f"\n  Done: {total}/18 files updated.")


if __name__ == "__main__":
    main()
