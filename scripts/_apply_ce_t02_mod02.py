"""Rewrite #code-examples for every lesson in track_02 / mod_02."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_02_working_with_data_sources")
SECTION_RE = re.compile(
    r'(<section id="code-examples"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── HTML builder helpers ─────────────────────────────────────────

def pill_tabs(tabs):
    parts = []
    for i, t in enumerate(tabs):
        label = t[0]
        if i == 0:
            cls = ('ce-step ce-step-active flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
                   'text-white shadow-lg shadow-pink-200/50 transition-all duration-250')
        else:
            cls = ('ce-step flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gray-800 text-gray-400 transition-all duration-250')
        parts.append(
            f'<button onclick="switchCeTab({i})" class="{cls}" role="tab">\n'
            f'  <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>\n'
            f'  <span class="ce-step-label text-xs font-bold">{label}</span>\n'
            f'</button>'
        )
    return ('<div class="flex items-center gap-2 mb-6" role="tablist">\n'
            + '\n'.join(parts) + '\n</div>')


def keyword_pill(text):
    return (f'<span class="flex items-center gap-1 text-[10px] px-2 py-0.5 '
            f'rounded-full bg-gray-100 text-gray-500 font-medium">{text}</span>')


def build_panel(idx, ex):
    hidden = ' hidden' if idx > 0 else ''
    watermark = f'{idx+1:02d}'
    extra_pills = '\n            '.join(keyword_pill(p) for p in ex['pills'])
    return f'''<div class="ce-panel ce-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{watermark}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{ex['title']}</h3>
          <div class="flex items-center gap-2 mt-1 flex-wrap">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            {keyword_pill(ex['domain'])}
            {extra_pills}
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">{ex['desc']}</p>
        </div>
      </div>
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
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">{ex['tip']}</p>
      </div>
    </div>
  </div>
</div>'''


def make_section(examples):
    tabs = [(ex['tab'],) for ex in examples]
    pills_html = pill_tabs(tabs)
    panels_html = '\n'.join(build_panel(i, ex) for i, ex in enumerate(examples))
    body = f'{pills_html}\n{panels_html}'
    return (
        '<section id="code-examples">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:code"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Code Examples</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Hands-on code snippets to explore the concepts</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-6">\n'
        f'{body}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── lesson content ───────────────────────────────────────────────

def lesson01_examples():
    return [
        {
            'tab': 'Custom Delimiter',
            'domain': 'Sales',
            'title': 'Custom Delimiter',
            'pills': ['sep=', 'pd.read_csv()'],
            'desc': 'This script loads a CSV file that uses a tab character as its separator. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">sep</code> parameter tells pandas what character separates each value.',
            'filename': 'tab_delimited.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;sales.tsv&quot;,  # file path\n'
                '                 sep=&quot;\\t&quot;)      # tab-separated values\n'
                '\n'
                'print(df.head())  # show first 5 rows'
            ),
            'cmd': '$ python tab_delimited.py',
            'output': '   date        product  amount<br>0  2025-01-01  Widget     150',
            'tip': 'If your CSV looks like one giant column, the separator is probably wrong &#8212; try tab, semicolon, or pipe.',
        },
        {
            'tab': 'Load Selected Columns',
            'domain': 'Employees',
            'title': 'Load Selected Columns',
            'pills': ['usecols', 'memory saving'],
            'desc': 'This script loads only the columns you need from a large file using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">usecols</code>. This saves memory and speeds up loading.',
            'filename': 'select_cols.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'cols = [&quot;name&quot;, &quot;department&quot;, &quot;salary&quot;]  # columns to load\n'
                '\n'
                'df = pd.read_csv(&quot;employees.csv&quot;,    # file path\n'
                '                 usecols=cols)         # load only these columns\n'
                '\n'
                'print(df.head())  # confirm only 3 columns loaded'
            ),
            'cmd': '$ python select_cols.py',
            'output': '     name  department  salary<br>0   Alice  Engineering   85000<br>1     Bob    Marketing   72000',
            'tip': 'On large files, loading fewer columns can cut memory usage in half &#8212; only pull what you actually need.',
        },
        {
            'tab': 'Fix Encoding Issues',
            'domain': 'Transactions',
            'title': 'Fix Encoding Issues',
            'pills': ['encoding', 'dtype'],
            'desc': 'This script fixes two common CSV problems at once: garbled characters from wrong encoding, and slow loads from unoptimised column types.',
            'filename': 'fix_encoding.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;transactions.csv&quot;,      # file path\n'
                '                 encoding=&quot;latin-1&quot;,       # fix special characters\n'
                '                 dtype={&quot;trans_id&quot;: str})  # keep IDs as text\n'
                '\n'
                'print(df.head())   # check for correct characters\n'
                'print(df.dtypes)   # confirm trans_id is object (text)'
            ),
            'cmd': '$ python fix_encoding.py',
            'output': '  trans_id  merchant    amount<br>0    T5001  CaféShop    42.50<br>trans_id     object',
            'tip': 'If you see weird symbols like Ã© instead of é, switch the encoding to latin-1 or utf-8-sig.',
        },
    ]


def lesson02_examples():
    return [
        {
            'tab': 'Read a JSON File',
            'domain': 'Products',
            'title': 'Read a JSON File',
            'pills': ['pd.read_json()', 'records'],
            'desc': 'This script reads a JSON file into a DataFrame. When the file is a list of objects, each object becomes one row.',
            'filename': 'read_json.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_json(&quot;products.json&quot;)  # read JSON into DataFrame\n'
                '\n'
                'print(df.head())   # show first rows\n'
                'print(df.shape)    # count rows and columns'
            ),
            'cmd': '$ python read_json.py',
            'output': '       name  price  stock<br>0    Laptop    999     12<br>(50, 3)',
            'tip': 'pd.read_json() works best with flat lists of objects &#8212; if your file has deep nesting, you will need json_normalize.',
        },
        {
            'tab': 'Flatten Nested JSON',
            'domain': 'Users',
            'title': 'Flatten Nested JSON',
            'pills': ['json_normalize()', 'nested data'],
            'desc': 'This script flattens nested JSON objects into a flat table using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">pd.json_normalize()</code>. Nested keys become dot-separated column names.',
            'filename': 'flatten_json.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                'import json          # for reading raw JSON\n'
                '\n'
                'with open(&quot;users.json&quot;) as f:           # open the file\n'
                '    data = json.load(f)                   # parse into Python list\n'
                '\n'
                'df = pd.json_normalize(data)  # flatten nested objects\n'
                'print(df.head())'
            ),
            'cmd': '$ python flatten_json.py',
            'output': '    name  address.city  address.postcode<br>0  Alice        London           SW1A 1AA',
            'tip': 'After normalising, check df.columns &#8212; the dot-separated names tell you exactly where each value came from in the original JSON.',
        },
        {
            'tab': 'Export as JSON',
            'domain': 'Orders',
            'title': 'Export as JSON',
            'pills': ['to_json()', 'orient'],
            'desc': 'This script converts a DataFrame to JSON and saves it to a file. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">orient</code> parameter controls the output shape.',
            'filename': 'export_json.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;orders.csv&quot;)  # load source data\n'
                '\n'
                'df.to_json(&quot;orders.json&quot;,            # output file\n'
                '           orient=&quot;records&quot;,           # list of objects\n'
                '           indent=2)                    # readable formatting\n'
                'print(&quot;JSON saved&quot;)'
            ),
            'cmd': '$ python export_json.py',
            'output': 'JSON saved',
            'tip': 'Use orient="records" when other systems expect a simple list of objects &#8212; it is the most widely compatible format.',
        },
    ]


def lesson03_examples():
    return [
        {
            'tab': 'Create a Connection',
            'domain': 'Finance',
            'title': 'Create a Connection',
            'pills': ['create_engine()', 'SQLAlchemy'],
            'desc': 'This script builds a database <strong class="text-gray-800">connection string</strong> and creates a SQLAlchemy engine. The engine is your link between Python and the database.',
            'filename': 'connect_db.py',
            'code': (
                'from sqlalchemy import create_engine  # database connector\n'
                '\n'
                'conn_str = &quot;sqlite:///finance.db&quot;  # connection string\n'
                'engine = create_engine(conn_str)     # create the engine\n'
                '\n'
                'print(engine)  # confirm connection object exists'
            ),
            'cmd': '$ python connect_db.py',
            'output': 'Engine(sqlite:///finance.db)',
            'tip': 'The connection string format changes for each database type &#8212; SQLite uses three slashes, PostgreSQL uses two.',
        },
        {
            'tab': 'Load a Table',
            'domain': 'Inventory',
            'title': 'Load a Table',
            'pills': ['pd.read_sql_table()', 'engine'],
            'desc': 'This script loads an entire database table into a DataFrame using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">pd.read_sql_table()</code>.',
            'filename': 'load_table.py',
            'code': (
                'import pandas as pd                    # load pandas\n'
                'from sqlalchemy import create_engine    # database connector\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///inventory.db&quot;)  # connect\n'
                '\n'
                'df = pd.read_sql_table(&quot;products&quot;, engine)  # load the table\n'
                'print(df.head())  # show first rows'
            ),
            'cmd': '$ python load_table.py',
            'output': '   product_id  name      price<br>0           1  Widget    12.99',
            'tip': 'The table name must match exactly what is in the database &#8212; use engine.table_names() to see all available tables.',
        },
        {
            'tab': 'Close Safely',
            'domain': 'Customers',
            'title': 'Close Safely',
            'pills': ['with statement', 'context manager'],
            'desc': 'This script uses a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">with</code> block to open and automatically close the connection, even if an error occurs.',
            'filename': 'safe_connect.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///customers.db&quot;)  # connect\n'
                '\n'
                'with engine.connect() as conn:               # auto-close on exit\n'
                '    df = pd.read_sql(&quot;SELECT * FROM customers&quot;, conn)\n'
                'print(df.shape)  # connection is already closed here'
            ),
            'cmd': '$ python safe_connect.py',
            'output': '(1500, 6)',
            'tip': 'Always use a with block for database connections &#8212; it guarantees cleanup even when your code hits an unexpected error.',
        },
    ]


def lesson04_examples():
    return [
        {
            'tab': 'Run a Query',
            'domain': 'Products',
            'title': 'Run a Query',
            'pills': ['pd.read_sql()', 'SELECT'],
            'desc': 'This script sends a SQL query to the database and receives the results as a DataFrame.',
            'filename': 'run_query.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///shop.db&quot;)  # connect\n'
                '\n'
                'query = &quot;SELECT name, price FROM products WHERE price &gt; 50&quot;\n'
                'df = pd.read_sql(query, engine)  # run query, get DataFrame\n'
                'print(df)'
            ),
            'cmd': '$ python run_query.py',
            'output': '       name  price<br>0    Laptop  999.0<br>1   Monitor  350.0',
            'tip': 'Filtering in SQL (WHERE) is faster than loading everything and filtering in pandas &#8212; let the database do the work.',
        },
        {
            'tab': 'Safe Parameters',
            'domain': 'Orders',
            'title': 'Safe Parameters',
            'pills': ['params', 'SQL injection'],
            'desc': 'This script uses <strong class="text-gray-800">parameterised queries</strong> to insert values safely. Never paste user input directly into a SQL string.',
            'filename': 'safe_params.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine, text\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///orders.db&quot;)\n'
                '\n'
                'query = text(&quot;SELECT * FROM orders WHERE total &gt; :min_total&quot;)\n'
                'df = pd.read_sql(query, engine, params={&quot;min_total&quot;: 100})\n'
                'print(df.head())'
            ),
            'cmd': '$ python safe_params.py',
            'output': '   order_id  customer_id  total<br>0     1001          101    250',
            'tip': 'Parameterised queries protect your database from SQL injection &#8212; never use f-strings or string concatenation for query values.',
        },
        {
            'tab': 'Query Two Tables',
            'domain': 'HR',
            'title': 'Query Two Tables',
            'pills': ['multiple queries', 'pd.merge()'],
            'desc': 'This script runs two separate queries and joins the results in pandas. This is useful when you cannot or prefer not to write SQL JOINs.',
            'filename': 'two_tables.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///hr.db&quot;)\n'
                'staff = pd.read_sql(&quot;SELECT * FROM staff&quot;, engine)\n'
                'depts = pd.read_sql(&quot;SELECT * FROM departments&quot;, engine)\n'
                '\n'
                'result = pd.merge(staff, depts, on=&quot;dept_id&quot;)\n'
                'print(result.head())'
            ),
            'cmd': '$ python two_tables.py',
            'output': '     name  dept_id  dept_name<br>0   Alice        1  Engineering',
            'tip': 'You can load tables separately and merge in pandas &#8212; useful when you need to do transformations that are hard in SQL.',
        },
    ]


def lesson05_examples():
    return [
        {
            'tab': 'Write to a Table',
            'domain': 'Survey',
            'title': 'Write to a Table',
            'pills': ['to_sql()', 'if_exists'],
            'desc': 'This script writes a DataFrame to a new database table using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">to_sql()</code>. If the table does not exist, pandas creates it.',
            'filename': 'write_table.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///survey.db&quot;)\n'
                'df = pd.read_csv(&quot;responses.csv&quot;)  # load CSV data\n'
                '\n'
                'df.to_sql(&quot;responses&quot;, engine, if_exists=&quot;replace&quot;, index=False)\n'
                'print(&quot;Wrote&quot;, len(df), &quot;rows&quot;)'
            ),
            'cmd': '$ python write_table.py',
            'output': 'Wrote 250 rows',
            'tip': 'Use if_exists="replace" during development and testing &#8212; switch to "append" in production to avoid deleting existing data.',
        },
        {
            'tab': 'Append New Rows',
            'domain': 'Logs',
            'title': 'Append New Rows',
            'pills': ['if_exists="append"', 'incremental'],
            'desc': 'This script adds new rows to an existing table without deleting old data. Setting <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">if_exists="append"</code> keeps previous rows intact.',
            'filename': 'append_rows.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///logs.db&quot;)\n'
                'new_logs = pd.read_csv(&quot;todays_logs.csv&quot;)  # today&apos;s data\n'
                '\n'
                'new_logs.to_sql(&quot;audit_log&quot;, engine, if_exists=&quot;append&quot;, index=False)\n'
                'print(&quot;Appended&quot;, len(new_logs), &quot;rows&quot;)'
            ),
            'cmd': '$ python append_rows.py',
            'output': 'Appended 45 rows',
            'tip': 'Check your column names and types before appending &#8212; mismatched columns will cause the write to fail silently.',
        },
        {
            'tab': 'Set Column Types',
            'domain': 'Inventory',
            'title': 'Set Column Types',
            'pills': ['dtype mapping', 'sqlalchemy types'],
            'desc': 'This script specifies exact database column types when writing. This prevents pandas from guessing wrong types, such as storing dates as plain text.',
            'filename': 'set_types.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine, String, Float\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///inventory.db&quot;)\n'
                'df = pd.read_csv(&quot;stock.csv&quot;)\n'
                '\n'
                'type_map = {&quot;sku&quot;: String(20), &quot;price&quot;: Float()}\n'
                'df.to_sql(&quot;stock&quot;, engine, dtype=type_map, if_exists=&quot;replace&quot;, index=False)'
            ),
            'cmd': '$ python set_types.py',
            'output': '',
            'tip': 'Setting dtype= prevents the database from storing numbers as text or truncating long strings &#8212; always map critical columns.',
        },
    ]


def lesson06_examples():
    return [
        {
            'tab': 'Load from .env',
            'domain': 'Database',
            'title': 'Load from .env',
            'pills': ['dotenv', 'os.getenv()'],
            'desc': 'This script reads a database password from a <strong class="text-gray-800">.env</strong> file instead of hard-coding it. The password never appears in your code.',
            'filename': 'load_env.py',
            'code': (
                'import os                          # access environment variables\n'
                'from dotenv import load_dotenv      # load .env file\n'
                '\n'
                'load_dotenv()                       # read .env into environment\n'
                '\n'
                'db_host = os.getenv(&quot;DB_HOST&quot;)      # get the host value\n'
                'db_pass = os.getenv(&quot;DB_PASSWORD&quot;)  # get the password\n'
                'print(&quot;Host:&quot;, db_host)              # confirm it loaded'
            ),
            'cmd': '$ python load_env.py',
            'output': 'Host: localhost',
            'tip': 'If os.getenv() returns None, your .env file is either missing the key or is not in the same folder as your script.',
        },
        {
            'tab': 'Build a Connection String',
            'domain': 'Analytics',
            'title': 'Build a Connection String',
            'pills': ['f-string', 'create_engine()'],
            'desc': 'This script builds a database connection string from .env values. The password stays in the .env file, not your Python code.',
            'filename': 'build_conn.py',
            'code': (
                'import os\n'
                'from dotenv import load_dotenv\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'load_dotenv()  # load credentials from .env\n'
                'user = os.getenv(&quot;DB_USER&quot;)\n'
                'pwd = os.getenv(&quot;DB_PASSWORD&quot;)\n'
                'engine = create_engine(f&quot;postgresql://{user}:{pwd}@localhost/analytics&quot;)'
            ),
            'cmd': '$ python build_conn.py',
            'output': '',
            'tip': 'Using an f-string with .env variables keeps your connection string flexible &#8212; change credentials without touching code.',
        },
        {
            'tab': 'Add .env to .gitignore',
            'domain': 'Security',
            'title': 'Add .env to .gitignore',
            'pills': ['.gitignore', 'version control'],
            'desc': 'This script checks whether your .env file is listed in .gitignore. If it is missing, you risk uploading passwords to a public repository.',
            'filename': 'check_gitignore.py',
            'code': (
                'with open(&quot;.gitignore&quot;) as f:  # open the gitignore file\n'
                '    lines = f.read()              # read all lines\n'
                '\n'
                'if &quot;.env&quot; in lines:               # check for .env entry\n'
                '    print(&quot;.env is safely ignored&quot;)\n'
                'else:\n'
                '    print(&quot;WARNING: .env is NOT in .gitignore!&quot;)'
            ),
            'cmd': '$ python check_gitignore.py',
            'output': '.env is safely ignored',
            'tip': 'Add .env to .gitignore before your first commit &#8212; once a password is in Git history, removing it is extremely difficult.',
        },
    ]


REGISTRY = {
    "lesson01_reading_csv_files.html": lesson01_examples,
    "lesson02_working_with_json_files.html": lesson02_examples,
    "lesson03_connecting_to_databases.html": lesson03_examples,
    "lesson04_running_sql_in_python.html": lesson04_examples,
    "lesson05_writing_data_back_to_a_database.html": lesson05_examples,
    "lesson06_managing_credentials_env.html": lesson06_examples,
}


def main():
    for fname, fn in REGISTRY.items():
        fpath = ROOT / fname
        if not fpath.exists():
            print(f"  SKIP  {fname} (not found)")
            continue
        html = fpath.read_text(encoding="utf-8")
        examples = fn()
        new_section = make_section(examples)
        new_html, count = SECTION_RE.subn(new_section, html)
        if count == 0:
            print(f"  WARN  {fname} (no #code-examples section)")
            continue
        fpath.write_text(new_html, encoding="utf-8")
        print(f"  OK    {fname} ({len(examples)} examples)")
    print("\nDone.")


if __name__ == "__main__":
    main()
