"""Rewrite #practice for every lesson in track_02 / mod_02."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_02_working_with_data_sources")
SECTION_RE = re.compile(
    r'(<section id="practice"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── HTML builder helpers (identical across all pe scripts) ───────

def pill_tabs(tabs):
    parts = []
    for i, label in enumerate(tabs):
        if i == 0:
            cls = ('pe-step pe-step-active flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
                   'text-white shadow-lg shadow-pink-200/50 transition-all duration-250')
        else:
            cls = ('pe-step flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gray-800 text-gray-400 transition-all duration-250')
        parts.append(
            f'<button onclick="switchPeTab({i})" class="{cls}" role="tab">\n'
            f'  <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>\n'
            f'  <span class="pe-step-label text-xs font-bold">{label}</span>\n'
            f'</button>'
        )
    return ('<div class="flex items-center gap-2 mb-6" role="tablist">\n'
            + '\n'.join(parts) + '\n</div>')


def badge_pill(text):
    return (f'<span class="flex items-center gap-1 text-[10px] px-2 py-0.5 '
            f'rounded-full bg-gray-100 text-gray-500 font-medium">{text}</span>')


def build_panel(idx, ex):
    hidden = ' hidden' if idx > 0 else ''
    watermark = f'{idx+1:02d}'
    extra = '\n            '.join(badge_pill(b) for b in ex['badges'])
    return f'''<div class="pe-panel pe-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{watermark}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{ex['title']}</h3>
          <div class="flex items-center gap-2 mt-1 flex-wrap">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            {badge_pill(ex['domain'])}
            {extra}
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
          <p class="text-sm text-gray-600">{ex['task']}</p>
        </div>
      </div>
      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">{ex['filename']}</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">{ex['code']}</code></pre>
          </div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">{ex['cmd']}</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">{ex['output']}</div>
          </div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">{ex['tip']}</p>
        </div>
      </div>
    </div>
  </div>
</div>'''


def make_section(exercises):
    tabs = [ex['tab'] for ex in exercises]
    pills_html = pill_tabs(tabs)
    panels_html = '\n'.join(build_panel(i, ex) for i, ex in enumerate(exercises))
    body = f'{pills_html}\n{panels_html}'
    return (
        '<section id="practice">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Guided exercises to reinforce your learning</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-6">\n'
        f'{body}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── lesson content ───────────────────────────────────────────────

def lesson01():
    """Reading CSV Files"""
    return [
        {
            'tab': 'Load Pipe-Delimited',
            'title': 'Load Pipe-Delimited',
            'domain': 'Logs',
            'badges': ['sep="|"', 'read_csv()'],
            'task': 'A server log file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">access.log</code> uses pipe characters (|) to separate columns instead of commas. Load it with the correct delimiter and print the first three rows.',
            'filename': 'load_pipe.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;access.log&quot;, sep=&quot;|&quot;)  # pipe delimiter\n'
                'print(df.head(3))                          # preview'
            ),
            'cmd': '$ python load_pipe.py',
            'output': '       timestamp     endpoint  status<br>0  2026-03-01 08:12  /api/users     200<br>1  2026-03-01 08:13  /api/login     401<br>2  2026-03-01 08:15  /api/data      200',
            'tip': 'Always check which character separates the columns before loading &#8212; common alternatives to commas are pipes, tabs, and semicolons.',
        },
        {
            'tab': 'Skip Header Rows',
            'title': 'Skip Header Rows',
            'domain': 'Reports',
            'badges': ['skiprows', 'header'],
            'task': 'A report file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">quarterly.csv</code> has two title rows at the top before the real column headers. Load it by skipping those rows and print the column names.',
            'filename': 'skip_rows.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;quarterly.csv&quot;, skiprows=2)  # skip 2 title rows\n'
                'print(df.columns.tolist())                      # show real headers'
            ),
            'cmd': '$ python skip_rows.py',
            'output': '[&apos;region&apos;, &apos;q1_sales&apos;, &apos;q2_sales&apos;, &apos;q3_sales&apos;]',
            'tip': 'Set skiprows to the number of non-data lines at the top of the file. The first un-skipped row becomes the column header.',
        },
        {
            'tab': 'Load Specific Columns',
            'title': 'Load Specific Columns',
            'domain': 'Payroll',
            'badges': ['usecols', 'subset'],
            'task': 'A payroll file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">payroll.csv</code> has 15 columns but you only need <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">employee</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">net_pay</code>. Load just those two columns and print the first three rows.',
            'filename': 'load_cols.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'cols = [&quot;employee&quot;, &quot;net_pay&quot;]                       # columns to keep\n'
                'df = pd.read_csv(&quot;payroll.csv&quot;, usecols=cols)  # load subset\n'
                'print(df.head(3))                                  # preview'
            ),
            'cmd': '$ python load_cols.py',
            'output': '  employee  net_pay<br>0    Alice  3450.00<br>1      Bob  2980.00<br>2    Carol  3720.00',
            'tip': 'Loading only the columns you need saves memory and speeds up the read &#8212; especially valuable for files with dozens of columns.',
        },
    ]


def lesson02():
    """Working with JSON Files"""
    return [
        {
            'tab': 'Read a JSON File',
            'title': 'Read a JSON File',
            'domain': 'Recipes',
            'badges': ['pd.read_json()', 'flat JSON'],
            'task': 'A recipe site exported its data to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">recipes.json</code>. Each record has a name, cuisine, and prep_time. Load the file and print the first three rows.',
            'filename': 'read_recipes.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_json(&quot;recipes.json&quot;)  # load JSON file\n'
                'print(df.head(3))                   # preview'
            ),
            'cmd': '$ python read_recipes.py',
            'output': '           name   cuisine  prep_time<br>0     Pad Thai      Thai         30<br>1  Fish Tacos   Mexican         25<br>2  Ramen Bowl  Japanese         45',
            'tip': 'read_json() works exactly like read_csv() when the JSON is a flat list of records &#8212; each record becomes one row.',
        },
        {
            'tab': 'Flatten Nested Data',
            'title': 'Flatten Nested Data',
            'domain': 'Events',
            'badges': ['json_normalize()', 'nested'],
            'task': 'A JSON file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">events.json</code> has a nested "location" object with city and country. Load the raw JSON with the json module, flatten it with pandas, and print the column names.',
            'filename': 'flatten_events.py',
            'code': (
                'import json\n'
                'import pandas as pd\n'
                '\n'
                'with open(&quot;events.json&quot;) as f:        # open the file\n'
                '    raw = json.load(f)                  # parse to Python\n'
                '\n'
                'df = pd.json_normalize(raw)             # flatten nested keys\n'
                'print(df.columns.tolist())'
            ),
            'cmd': '$ python flatten_events.py',
            'output': '[&apos;name&apos;, &apos;date&apos;, &apos;location.city&apos;, &apos;location.country&apos;]',
            'tip': 'json_normalize() turns nested dictionaries into flat columns using dot notation &#8212; no manual parsing needed.',
        },
        {
            'tab': 'Export to JSON',
            'title': 'Export to JSON',
            'domain': 'Catalogue',
            'badges': ['to_json()', 'orient'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">catalogue.csv</code> and export it to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">catalogue.json</code> in records format. Print a confirmation message.',
            'filename': 'export_json.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;catalogue.csv&quot;)  # load CSV data\n'
                '\n'
                'df.to_json(&quot;catalogue.json&quot;, orient=&quot;records&quot;, indent=2)\n'
                'print(f&quot;Exported {len(df)} records to JSON&quot;)'
            ),
            'cmd': '$ python export_json.py',
            'output': 'Exported 64 records to JSON',
            'tip': 'Use orient="records" for a list of objects &#8212; it is the format most web APIs and JavaScript code expect.',
        },
    ]


def lesson03():
    """Connecting to Databases"""
    return [
        {
            'tab': 'Open a Connection',
            'title': 'Open a Connection',
            'domain': 'Retail',
            'badges': ['create_engine()', 'SQLite'],
            'task': 'Create a connection to a SQLite database called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">retail.db</code> using SQLAlchemy. Load the "products" table and print the row count.',
            'filename': 'connect_db.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///retail.db&quot;)  # connect\n'
                'df = pd.read_sql_table(&quot;products&quot;, engine)     # load table\n'
                '\n'
                'print(f&quot;Loaded {len(df)} products&quot;)'
            ),
            'cmd': '$ python connect_db.py',
            'output': 'Loaded 250 products',
            'tip': 'The connection string tells SQLAlchemy which database engine and file to use &#8212; change "sqlite" to "postgresql" for a Postgres database.',
        },
        {
            'tab': 'Load a Full Table',
            'title': 'Load a Full Table',
            'domain': 'HR',
            'badges': ['read_sql_table()', 'inspect'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">hr.db</code> and load the "employees" table. Print the column names and data types.',
            'filename': 'load_table.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///hr.db&quot;)       # connect\n'
                'df = pd.read_sql_table(&quot;employees&quot;, engine)    # load table\n'
                '\n'
                'print(df.dtypes)'
            ),
            'cmd': '$ python load_table.py',
            'output': 'emp_id       int64<br>name        object<br>dept        object<br>salary     float64<br>dtype: object',
            'tip': 'read_sql_table() loads every row and column from the table. Use read_sql() with a query when you only need a subset.',
        },
        {
            'tab': 'Use a Context Manager',
            'title': 'Use a Context Manager',
            'domain': 'Logistics',
            'badges': ['with statement', 'safe close'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">logistics.db</code> and load the "shipments" table using a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">with</code> block so the connection closes automatically. Print the first three rows.',
            'filename': 'safe_connect.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///logistics.db&quot;)\n'
                '\n'
                'with engine.connect() as conn:                   # auto-close\n'
                '    df = pd.read_sql(&quot;SELECT * FROM shipments&quot;, conn)\n'
                'print(df.head(3))'
            ),
            'cmd': '$ python safe_connect.py',
            'output': '   shipment_id destination  weight<br>0         3001      London    12.5<br>1         3002       Tokyo    28.0<br>2         3003      Sydney     6.2',
            'tip': 'A with block guarantees the connection closes even if an error occurs &#8212; this prevents resource leaks in long-running scripts.',
        },
    ]


def lesson04():
    """Running SQL in Python"""
    return [
        {
            'tab': 'Select Rows',
            'title': 'Select Rows',
            'domain': 'Warehouse',
            'badges': ['read_sql()', 'WHERE'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">warehouse.db</code> and run a SQL query to fetch all items where quantity is below 10. Print the result.',
            'filename': 'select_rows.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///warehouse.db&quot;)\n'
                '\n'
                'query = &quot;SELECT item, quantity FROM stock WHERE quantity &lt; 10&quot;\n'
                'df = pd.read_sql(query, engine)\n'
                'print(df)'
            ),
            'cmd': '$ python select_rows.py',
            'output': '        item  quantity<br>0    Widgets         3<br>1  Connectors         7',
            'tip': 'Let the database do the filtering with WHERE &#8212; it is much faster than loading all rows into Python first.',
        },
        {
            'tab': 'Safe Parameters',
            'title': 'Safe Parameters',
            'domain': 'Clients',
            'badges': ['text()', 'params'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">clients.db</code>. Use a parameterised query to find clients whose <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">city</code> matches a variable. Print the matching rows.',
            'filename': 'safe_params.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine, text\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///clients.db&quot;)\n'
                '\n'
                'query = text(&quot;SELECT name, city FROM clients WHERE city = :city&quot;)\n'
                'df = pd.read_sql(query, engine, params={&quot;city&quot;: &quot;London&quot;})\n'
                'print(df)'
            ),
            'cmd': '$ python safe_params.py',
            'output': '      name    city<br>0    Alice  London<br>1  Charles  London',
            'tip': 'Never paste user input into a SQL string. Parameterised queries protect your database from injection attacks.',
        },
        {
            'tab': 'Join in SQL',
            'title': 'Join in SQL',
            'domain': 'Payroll',
            'badges': ['SQL JOIN', 'combined'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">payroll.db</code> and run a SQL JOIN between "staff" and "departments" on dept_id. Load the result into a DataFrame and print the first three rows.',
            'filename': 'sql_join.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///payroll.db&quot;)\n'
                'query = (&quot;SELECT s.name, d.dept_name, s.salary &quot;\n'
                '         &quot;FROM staff s JOIN departments d ON s.dept_id = d.id&quot;)\n'
                '\n'
                'df = pd.read_sql(query, engine)\n'
                'print(df.head(3))'
            ),
            'cmd': '$ python sql_join.py',
            'output': '     name   dept_name  salary<br>0   Alice  Marketing   65000<br>1     Bob    Finance   72000<br>2   Carol  Marketing   61000',
            'tip': 'Running the JOIN in SQL means the database does the heavy lifting &#8212; Python only receives the already-combined result.',
        },
    ]


def lesson05():
    """Writing Data Back to a Database"""
    return [
        {
            'tab': 'Write a DataFrame',
            'title': 'Write a DataFrame',
            'domain': 'Feedback',
            'badges': ['to_sql()', 'new table'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">feedback.csv</code> into a DataFrame. Write it to a new SQLite table called "responses" in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">survey.db</code>. Print the number of rows written.',
            'filename': 'write_table.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'df = pd.read_csv(&quot;feedback.csv&quot;)                  # load CSV\n'
                'engine = create_engine(&quot;sqlite:///survey.db&quot;)     # connect\n'
                '\n'
                'df.to_sql(&quot;responses&quot;, engine, index=False,\n'
                '          if_exists=&quot;replace&quot;)                     # write table\n'
                'print(f&quot;Wrote {len(df)} rows&quot;)'
            ),
            'cmd': '$ python write_table.py',
            'output': 'Wrote 120 rows',
            'tip': 'Set index=False to avoid writing the DataFrame index as an extra column in the database table.',
        },
        {
            'tab': 'Append New Rows',
            'title': 'Append New Rows',
            'domain': 'Sensors',
            'badges': ['if_exists="append"', 'incremental'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">new_readings.csv</code> and append its rows to the existing "readings" table in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">sensors.db</code>. Print a confirmation message.',
            'filename': 'append_rows.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'df = pd.read_csv(&quot;new_readings.csv&quot;)              # new data\n'
                'engine = create_engine(&quot;sqlite:///sensors.db&quot;)    # connect\n'
                '\n'
                'df.to_sql(&quot;readings&quot;, engine, index=False,\n'
                '          if_exists=&quot;append&quot;)                      # add rows\n'
                'print(f&quot;Appended {len(df)} readings&quot;)'
            ),
            'cmd': '$ python append_rows.py',
            'output': 'Appended 48 readings',
            'tip': 'Use "append" when you add new data regularly. Use "replace" only when you want to wipe the table and start fresh.',
        },
        {
            'tab': 'Replace a Table',
            'title': 'Replace a Table',
            'domain': 'Prices',
            'badges': ['if_exists="replace"', 'overwrite'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">updated_prices.csv</code> and overwrite the "prices" table in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">shop.db</code> with the new data. Print the row count.',
            'filename': 'replace_table.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'df = pd.read_csv(&quot;updated_prices.csv&quot;)          # fresh data\n'
                'engine = create_engine(&quot;sqlite:///shop.db&quot;)      # connect\n'
                '\n'
                'df.to_sql(&quot;prices&quot;, engine, index=False,\n'
                '          if_exists=&quot;replace&quot;)                    # overwrite\n'
                'print(f&quot;Replaced with {len(df)} rows&quot;)'
            ),
            'cmd': '$ python replace_table.py',
            'output': 'Replaced with 310 rows',
            'tip': 'The "replace" option drops the old table before writing &#8212; make sure you have a backup if the original data matters.',
        },
    ]


def lesson06():
    """Managing Credentials (.env)"""
    return [
        {
            'tab': 'Load from .env',
            'title': 'Load from .env',
            'domain': 'API',
            'badges': ['dotenv', 'os.getenv()'],
            'task': 'Create a script that loads database credentials from a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">.env</code> file using python-dotenv. Print the host value to confirm it loaded.',
            'filename': 'load_env.py',
            'code': (
                'import os\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()  # read .env file into environment\n'
                '\n'
                'db_host = os.getenv(&quot;DB_HOST&quot;)  # fetch the host\n'
                'print(f&quot;Host: {db_host}&quot;)         # confirm'
            ),
            'cmd': '$ python load_env.py',
            'output': 'Host: db.example.com',
            'tip': 'The .env file stays on your machine and is never committed to Git &#8212; this keeps credentials out of shared code.',
        },
        {
            'tab': 'Build a Connection',
            'title': 'Build a Connection',
            'domain': 'Warehouse',
            'badges': ['f-string', 'connection URL'],
            'task': 'Load credentials from <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">.env</code> and build a PostgreSQL connection string. Print the string with the password masked as asterisks.',
            'filename': 'build_url.py',
            'code': (
                'import os\n'
                'from dotenv import load_dotenv\n'
                '\n'
                'load_dotenv()  # load .env\n'
                'user = os.getenv(&quot;DB_USER&quot;)      # username\n'
                'pwd = os.getenv(&quot;DB_PASS&quot;)       # password\n'
                'host = os.getenv(&quot;DB_HOST&quot;)      # server\n'
                'print(f&quot;postgresql://{user}:****@{host}/warehouse&quot;)'
            ),
            'cmd': '$ python build_url.py',
            'output': 'postgresql://analyst:****@db.example.com/warehouse',
            'tip': 'Never print or log the real password. Mask it any time you display a connection string.',
        },
        {
            'tab': 'Protect with .gitignore',
            'title': 'Protect with .gitignore',
            'domain': 'DevOps',
            'badges': ['.gitignore', 'security'],
            'task': 'Write a script that checks whether <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">.env</code> is listed in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">.gitignore</code>. If not, append it. Print the result.',
            'filename': 'check_gitignore.py',
            'code': (
                'from pathlib import Path  # file utilities\n'
                '\n'
                'gi = Path(&quot;.gitignore&quot;)                         # gitignore path\n'
                'content = gi.read_text() if gi.exists() else &quot;&quot;  # read or empty\n'
                '\n'
                'if &quot;.env&quot; not in content:                        # not listed yet\n'
                '    gi.open(&quot;a&quot;).write(&quot;\\n.env\\n&quot;)              # append it\n'
                '    print(&quot;Added .env to .gitignore&quot;)\n'
                'else:\n'
                '    print(&quot;.env is already in .gitignore&quot;)'
            ),
            'cmd': '$ python check_gitignore.py',
            'output': 'Added .env to .gitignore',
            'tip': 'Run this check once when setting up a new project &#8212; accidentally committing a .env file can expose passwords to everyone with repo access.',
        },
    ]


REGISTRY = {
    "lesson01_reading_csv_files.html": lesson01,
    "lesson02_working_with_json_files.html": lesson02,
    "lesson03_connecting_to_databases.html": lesson03,
    "lesson04_running_sql_in_python.html": lesson04,
    "lesson05_writing_data_back_to_a_database.html": lesson05,
    "lesson06_managing_credentials_env.html": lesson06,
}


def main():
    for fname, fn in REGISTRY.items():
        fpath = ROOT / fname
        if not fpath.exists():
            print(f"  SKIP  {fname} (not found)")
            continue
        html = fpath.read_text(encoding="utf-8")
        exercises = fn()
        new_section = make_section(exercises)
        new_html, count = SECTION_RE.subn(new_section, html)
        if count == 0:
            print(f"  WARN  {fname} (no #practice section)")
            continue
        fpath.write_text(new_html, encoding="utf-8")
        print(f"  OK    {fname} ({len(exercises)} exercises)")
    print("\nDone.")


if __name__ == "__main__":
    main()
