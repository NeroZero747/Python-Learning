"""
Replace all SQLite / PostgreSQL / MySQL references in lesson 09 with
SQL Server, Oracle, Snowflake, and Teradata.
"""

import pathlib, sys

TARGET = pathlib.Path(
    "pages/mod_03_python_for_data_analysts/"
    "lesson09_connecting_to_databases_and_running_sql.html"
)

content = TARGET.read_text(encoding="utf-8")
orig = content  # keep for diff count

# Helper
def r(old, new, label=""):
    global content
    if old not in content:
        print(f"  ⚠️  NOT FOUND: {label or old[:60]}")
        return
    count = content.count(old)
    content = content.replace(old, new)
    print(f"  ✅  {label or old[:60]}  ({count}x)")


# ── 1. Overview tip ─────────────────────────────────────────────
r(
    "SQLAlchemy supports PostgreSQL, MySQL, SQL Server, and SQLite",
    "SQLAlchemy supports SQL Server, Oracle, Snowflake, and Teradata",
    "Overview tip",
)

# ── 2. KC Tab 0 — Connection String Parts table ────────────────
r(
    "Database type — sqlite, postgresql, mysql",
    "Database type — mssql, oracle, snowflake",
    "KC-0 dialect field",
)
r(
    "Login credentials (omit for SQLite)",
    "Login credentials",
    "KC-0 credentials note",
)

# KC Tab 0 — code block (literal quotes)
r(
    '# SQLite — local file, no server needed\n'
    'conn = "sqlite:///company.db"\n'
    '# PostgreSQL — remote server\n'
    'conn = "postgresql://admin:secret@localhost/sales"',

    '# SQL Server — uses pyodbc driver\n'
    'conn = "mssql+pyodbc://admin:pw@sqlserver01/company?driver=ODBC+Driver+18+for+SQL+Server"\n'
    '# Oracle — uses oracledb driver\n'
    'conn = "oracle+oracledb://admin:pw@oracle01:1521/sales"',
    "KC-0 code block",
)

# KC Tab 0 — warning box
r(
    '<strong>SQLite uses three slashes.</strong> <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">sqlite:///file.db</code> — two from the protocol, one for the local path.',
    '<strong>Always include the driver parameter for SQL Server.</strong> The <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">?driver=</code> part tells SQLAlchemy which ODBC driver is installed on your machine.',
    "KC-0 warning box",
)

# ── 3. KC Tab 1 — Engine code ──────────────────────────────────
r(
    'engine = create_engine("sqlite:///company.db")  # create once',
    'engine = create_engine("mssql+pyodbc://admin:pw@sqlserver01/company?driver=ODBC+Driver+18+for+SQL+Server")\n'
    'print(engine)                                    # Engine object',
    "KC-1 engine code (line 1)",
)
# The original also had print(engine) on the next line — remove the duplicate
r(
    'print(engine)                                    # Engine object\n'
    'print(engine)                                    # Engine object',
    'print(engine)                                    # Engine object',
    "KC-1 deduplicate print",
)

# ── 4. KC Tab 2 — Database Types ───────────────────────────────
r(
    "SQLite, PostgreSQL, and MySQL",
    "SQL Server, Oracle, Snowflake, and Teradata",
    "KC-2 subtitle",
)
r(
    "SQLite is built in. Others need a driver.",
    "Each database needs its own driver package.",
    "KC-2 description",
)

# KC Tab 2 — dialects table rows (replace all 4 rows)
OLD_TABLE_ROWS = """                      <tr class=" border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">sqlite</code></td>
                        <td class="py-2 px-3 text-gray-500">File-based, no server</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">sqlite:///data.db</code></td>
                      </tr>
                      <tr class=" border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">postgresql</code></td>
                        <td class="py-2 px-3 text-gray-500">Enterprise, full features</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">postgresql://u:p@host/db</code></td>
                      </tr>
                      <tr class=" border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">mysql</code></td>
                        <td class="py-2 px-3 text-gray-500">Popular web database</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">mysql://u:p@host/db</code></td>
                      </tr>
                      <tr class=" bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">mssql</code></td>
                        <td class="py-2 px-3 text-gray-500">Microsoft SQL Server</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">mssql://u:p@host/db</code></td>
                      </tr>"""

NEW_TABLE_ROWS = """                      <tr class=" border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">mssql+pyodbc</code></td>
                        <td class="py-2 px-3 text-gray-500">Microsoft SQL Server</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">mssql+pyodbc://u:p@host/db</code></td>
                      </tr>
                      <tr class=" border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">oracle+oracledb</code></td>
                        <td class="py-2 px-3 text-gray-500">Oracle Database</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">oracle+oracledb://u:p@host/db</code></td>
                      </tr>
                      <tr class=" border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">snowflake</code></td>
                        <td class="py-2 px-3 text-gray-500">Snowflake cloud warehouse</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">snowflake://u:p@acct/db</code></td>
                      </tr>
                      <tr class=" bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">teradatasql</code></td>
                        <td class="py-2 px-3 text-gray-500">Teradata enterprise DW</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded text-[10px]">teradatasql://u:p@host/db</code></td>
                      </tr>"""

r(OLD_TABLE_ROWS, NEW_TABLE_ROWS, "KC-2 dialects table")

# KC Tab 2 — code block
r(
    '# SQLite — no install needed\n'
    'engine = create_engine("sqlite:///local.db")\n'
    '# PostgreSQL — pip install psycopg2-binary\n'
    'engine = create_engine("postgresql://admin:pw@localhost/sales")',

    '# SQL Server — pip install pyodbc\n'
    'engine = create_engine("mssql+pyodbc://admin:pw@sqlserver01/sales?driver=ODBC+Driver+18+for+SQL+Server")\n'
    '# Oracle — pip install oracledb\n'
    'engine = create_engine("oracle+oracledb://admin:pw@oracle01:1521/sales")',
    "KC-2 code block",
)

# KC Tab 2 — tip box
r(
    '<strong>Start with SQLite for learning.</strong> It needs no server, no password, and no extra install. Move to PostgreSQL when you need a shared database.',
    '<strong>SQL Server is the most common enterprise database.</strong> Install <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">pyodbc</code> and the ODBC driver, then use the same <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">create_engine()</code> pattern for any supported database.',
    "KC-2 tip box",
)

# ── 5. CE Tabs — connection strings (HTML entity quotes) ───────
# CE Tab 1 — connect_db.py
r(
    'conn_str = &quot;sqlite:///finance.db&quot;  # connection string',
    'conn_str = &quot;mssql+pyodbc://admin:pw@sqlserver01/finance?driver=ODBC+Driver+18+for+SQL+Server&quot;',
    "CE-1 conn_str",
)
r(
    'Engine(sqlite:///finance.db)',
    'Engine(mssql+pyodbc://admin:***@sqlserver01/finance)',
    "CE-1 terminal output",
)
r(
    'The connection string format changes for each database type &#8212; SQLite uses three slashes, PostgreSQL uses two.',
    'The connection string format changes for each database type &#8212; SQL Server uses <code class="text-xs font-mono px-1 rounded bg-gray-100">mssql+pyodbc://</code> and requires a <code class="text-xs font-mono px-1 rounded bg-gray-100">?driver=</code> parameter.',
    "CE-1 tip",
)

# CE Tab 2 — load_table.py
r(
    'engine = create_engine(&quot;sqlite:///inventory.db&quot;)  # connect',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/inventory?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "CE-2 conn_str",
)

# CE Tab 3 — safe_connect.py
r(
    'engine = create_engine(&quot;sqlite:///customers.db&quot;)  # connect',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/customers?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "CE-3 conn_str",
)

# CE Tab 4 — run_query.py
r(
    'engine = create_engine(&quot;sqlite:///shop.db&quot;)  # open database',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/shop?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "CE-4 conn_str",
)

# CE Tab 5 — safe_params.py
r(
    'engine = create_engine(&quot;sqlite:///orders.db&quot;)  # open database',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/orders?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "CE-5 conn_str",
)

# ── 6. Practice Exercises ───────────────────────────────────────
# PE Tab 1 pills & task
r(
    '>SQLite</span>',
    '>SQL Server</span>',
    "PE-1 pill label",
)
r(
    'Create a connection to a SQLite database called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">retail.db</code> using SQLAlchemy. Load the "products" table and print the row count.',
    'Create a connection to a SQL Server database called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">retail</code> using SQLAlchemy. Load the &quot;products&quot; table and print the row count.',
    "PE-1 task text",
)

# PE Tab 1 code
r(
    'engine = create_engine(&quot;sqlite:///retail.db&quot;)  # connect',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/retail?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "PE-1 code",
)

# PE Tab 1 tip
r(
    'The connection string tells SQLAlchemy which database engine and file to use &#8212; change "sqlite" to "postgresql" for a Postgres database.',
    'The connection string tells SQLAlchemy which database type to use &#8212; change <code class="text-xs font-mono px-1 rounded bg-gray-100">mssql+pyodbc</code> to <code class="text-xs font-mono px-1 rounded bg-gray-100">oracle+oracledb</code> for an Oracle database.',
    "PE-1 tip",
)

# PE Tab 2 code
r(
    'engine = create_engine(&quot;sqlite:///hr.db&quot;)       # connect',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/hr?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "PE-2 code",
)

# PE Tab 3 code
r(
    'engine = create_engine(&quot;sqlite:///logistics.db&quot;)',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/logistics?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "PE-3 code",
)

# PE Tab 4 code
r(
    'engine = create_engine(&quot;sqlite:///warehouse.db&quot;)',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/warehouse?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "PE-4 code",
)

# PE Tab 5 code
r(
    'engine = create_engine(&quot;sqlite:///clients.db&quot;)',
    'engine = create_engine(&quot;mssql+pyodbc://admin:pw@sqlserver01/clients?driver=ODBC+Driver+18+for+SQL+Server&quot;)',
    "PE-5 code",
)

# ── 7. Mistakes section ────────────────────────────────────────
# Mistake 1 — Wrong connection string format
r(
    'Each database type needs a specific URL prefix. SQLite uses <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">sqlite:///</code> (three slashes for relative path). PostgreSQL uses <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">postgresql://</code>. A wrong prefix triggers <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ArgumentError</code>.',
    'Each database type needs its own URL prefix and driver. SQL Server uses <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">mssql+pyodbc://</code> and requires a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">?driver=</code> parameter. Omitting the driver triggers <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ArgumentError</code>.',
    "Mistake-1 explanation",
)

# Mistake 1 label
r(
    'Wrong — wrong prefix',
    'Wrong — missing driver param',
    "Mistake-1 wrong label",
)

# Mistake 1 wrong code
r(
    'engine = create_engine("sqlite://data.db")\n# ArgumentError — missing a slash',
    'engine = create_engine("mssql+pyodbc://admin:pw@server/sales")\n# ArgumentError — missing ?driver= parameter',
    "Mistake-1 wrong code",
)

# Mistake 1 correct label
r(
    'Correct — correct prefix',
    'Correct — include driver',
    "Mistake-1 correct label",
)

# Mistake 1 correct code
r(
    'from sqlalchemy import create_engine              # import first\n'
    'engine = create_engine("sqlite:///data.db")       # three slashes\n'
    'print(engine)                                      # confirms connection',
    'from sqlalchemy import create_engine                               # import first\n'
    'engine = create_engine("mssql+pyodbc://admin:pw@server/sales"     # dialect + driver\n'
    '                       "?driver=ODBC+Driver+18+for+SQL+Server")   # driver param\n'
    'print(engine)                                                      # confirms connection',
    "Mistake-1 correct code",
)

# Mistake 1 amber tip
r(
    'Count the slashes: <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">sqlite:///</code> means "protocol + empty host + relative path". Two slashes is never enough for SQLite.',
    'Always add the <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">?driver=</code> parameter for SQL Server. Run <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">pyodbc.drivers()</code> in Python to see which drivers are installed on your machine.',
    "Mistake-1 amber tip",
)

# Mistake 3 — Missing driver package
r(
    'SQLAlchemy needs a separate driver for each database — <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">psycopg2</code> for PostgreSQL, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pymysql</code> for MySQL. Without the driver installed, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">create_engine()</code> fails.',
    'SQLAlchemy needs a separate driver for each database — <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pyodbc</code> for SQL Server, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">oracledb</code> for Oracle. Without the driver installed, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">create_engine()</code> fails.',
    "Mistake-3 explanation",
)

# Mistake 3 wrong code
r(
    'engine = create_engine("postgresql://user:pw@host/db")\n'
    '# ModuleNotFoundError: No module named psycopg2',
    'engine = create_engine("mssql+pyodbc://admin:pw@server/sales?driver=ODBC+Driver+18+for+SQL+Server")\n'
    '# ModuleNotFoundError: No module named pyodbc',
    "Mistake-3 wrong code",
)

# Mistake 3 correct code
r(
    '# first, in terminal: pip install psycopg2-binary\n'
    'from sqlalchemy import create_engine                 # import\n'
    'engine = create_engine("postgresql://user:pw@host/db") # works now',
    '# first, in terminal: pip install pyodbc\n'
    'from sqlalchemy import create_engine                                               # import\n'
    'engine = create_engine("mssql+pyodbc://admin:pw@server/sales"                     # connect\n'
    '                       "?driver=ODBC+Driver+18+for+SQL+Server")                   # works now',
    "Mistake-3 correct code",
)

# Mistake 3 amber tip
r(
    'Check the SQLAlchemy docs for your database type. Each has a recommended driver package you need to <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">pip install</code> once.',
    'Check the SQLAlchemy docs for your database type. SQL Server needs <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">pip install pyodbc</code>, Oracle needs <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">pip install oracledb</code>.',
    "Mistake-3 amber tip",
)


# ── WRITE ───────────────────────────────────────────────────────
TARGET.write_text(content, encoding="utf-8")

# Quick check for any remaining banned refs
import re
banned = re.findall(r'(?i)\b(?:sqlite|postgresql|postgres|mysql|pymysql|psycopg2)\b', content)
if banned:
    print(f"\n⚠️  {len(banned)} banned reference(s) still remain:")
    for w in sorted(set(banned)):
        print(f"   • {w}")
else:
    print("\n✅  No banned database references remain.")

print("\nDone.")
