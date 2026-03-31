"""Rewrite #code-examples for every lesson in track_02 / mod_03."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_03_python_for_analysts")
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
            'tab': 'Automate a Calculation',
            'domain': 'Budgets',
            'title': 'Automate a Calculation',
            'pills': ['pandas', 'sum()'],
            'desc': 'This script loads a budget spreadsheet and calculates the total spend in one line. In Excel, you would need a SUM formula at the bottom of a column.',
            'filename': 'budget_total.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;budget.csv&quot;)  # load budget data\n'
                '\n'
                'total = df[&quot;amount&quot;].sum()  # add up the amount column\n'
                'print(&quot;Total spend:&quot;, total)   # display the result'
            ),
            'cmd': '$ python budget_total.py',
            'output': 'Total spend: 48750.0',
            'tip': 'One line of pandas replaces the manual SUM formula you would normally type at the bottom of a spreadsheet column.',
        },
        {
            'tab': 'Summarise by Category',
            'domain': 'Sales',
            'title': 'Summarise by Category',
            'pills': ['groupby()', 'pivot-table style'],
            'desc': 'This script groups rows by region and calculates the average &#8212; like a pivot table in Excel, but reusable and repeatable.',
            'filename': 'sales_summary.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;sales.csv&quot;)  # load sales data\n'
                '\n'
                'avg_by_region = df.groupby(&quot;region&quot;)[&quot;revenue&quot;].mean()  # average per region\n'
                'avg_by_region = avg_by_region.round(2)  # round to 2 decimal places\n'
                'print(avg_by_region)'
            ),
            'cmd': '$ python sales_summary.py',
            'output': 'region<br>East     1125.00<br>North     800.50<br>West     1275.25<br>Name: revenue, dtype: float64',
            'tip': 'Unlike a pivot table, this script gives you the same result every time you run it &#8212; no manual clicking required.',
        },
        {
            'tab': 'Use a Library',
            'domain': 'Reports',
            'title': 'Use a Library',
            'pills': ['import', 'library ecosystem'],
            'desc': 'This script uses <strong class="text-gray-800">pandas</strong> and <strong class="text-gray-800">datetime</strong> together. Libraries give you ready-made tools so you do not need to write everything from scratch.',
            'filename': 'report_date.py',
            'code': (
                'import pandas as pd              # data analysis\n'
                'from datetime import date         # today&apos;s date\n'
                '\n'
                'df = pd.read_csv(&quot;report.csv&quot;)   # load report data\n'
                'row_count = len(df)               # count rows\n'
                'today = date.today()              # get today&apos;s date\n'
                '\n'
                'print(f&quot;Report: {row_count} rows as of {today}&quot;)'
            ),
            'cmd': '$ python report_date.py',
            'output': 'Report: 340 rows as of 2026-03-31',
            'tip': 'Python has over 500,000 libraries &#8212; chances are someone has already built a tool for the task you are trying to automate.',
        },
    ]


def lesson02_examples():
    return [
        {
            'tab': 'Replicate VLOOKUP',
            'domain': 'Orders',
            'title': 'Replicate VLOOKUP',
            'pills': ['pd.merge()', 'VLOOKUP replacement'],
            'desc': 'This script joins two tables on a shared key, replicating what VLOOKUP does in Excel. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">merge()</code> function matches rows automatically.',
            'filename': 'vlookup_merge.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'orders = pd.read_csv(&quot;orders.csv&quot;)        # order rows\n'
                'products = pd.read_csv(&quot;products.csv&quot;)    # product details\n'
                '\n'
                'result = pd.merge(orders, products, on=&quot;product_id&quot;)  # match rows\n'
                'print(result[[&quot;order_id&quot;, &quot;product_name&quot;, &quot;price&quot;]].head())'
            ),
            'cmd': '$ python vlookup_merge.py',
            'output': '   order_id product_name  price<br>0     1001       Laptop  999.0<br>1     1002        Mouse   25.0',
            'tip': 'Unlike VLOOKUP, merge() handles multiple matches in both tables &#8212; no need for INDEX/MATCH workarounds.',
        },
        {
            'tab': 'Build a Pivot Table',
            'domain': 'Sales',
            'title': 'Build a Pivot Table',
            'pills': ['pivot_table()', 'aggfunc'],
            'desc': 'This script creates a pivot table that sums revenue by region and product &#8212; the same analysis you would build manually in Excel.',
            'filename': 'pivot_sales.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;sales.csv&quot;)  # load sales data\n'
                '\n'
                'pivot = df.pivot_table(values=&quot;revenue&quot;,     # values to sum\n'
                '                       index=&quot;region&quot;,       # row labels\n'
                '                       columns=&quot;product&quot;,    # column labels\n'
                '                       aggfunc=&quot;sum&quot;)        # aggregation\n'
                'print(pivot)'
            ),
            'cmd': '$ python pivot_sales.py',
            'output': 'product  Keyboard  Laptop  Mouse<br>region<br>East         750    2997    150<br>West         375    1998     75',
            'tip': 'Add fill_value=0 to replace blank cells with zero &#8212; this makes the pivot easier to read when some combinations have no data.',
        },
        {
            'tab': 'Multi-Sheet Excel Report',
            'domain': 'Finance',
            'title': 'Multi-Sheet Excel Report',
            'pills': ['ExcelWriter', 'multiple sheets'],
            'desc': 'This script writes two DataFrames to separate sheets in one Excel workbook. You can automate a multi-tab report that used to take manual copy-pasting.',
            'filename': 'multi_sheet.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;finance.csv&quot;)    # load all data\n'
                'summary = df.groupby(&quot;dept&quot;)[&quot;spend&quot;].sum().reset_index()  # totals\n'
                '\n'
                'with pd.ExcelWriter(&quot;report.xlsx&quot;) as writer:      # open workbook\n'
                '    df.to_excel(writer, sheet_name=&quot;Raw Data&quot;, index=False)\n'
                '    summary.to_excel(writer, sheet_name=&quot;Summary&quot;, index=False)\n'
                'print(&quot;Report saved with 2 sheets&quot;)'
            ),
            'cmd': '$ python multi_sheet.py',
            'output': 'Report saved with 2 sheets',
            'tip': 'ExcelWriter lets you add as many sheets as you need in one file &#8212; raw data, summaries, and charts can all live together.',
        },
    ]


def lesson03_examples():
    return [
        {
            'tab': 'Run a SQL Query',
            'domain': 'Products',
            'title': 'Run a SQL Query',
            'pills': ['pd.read_sql()', 'SELECT'],
            'desc': 'This script sends a SQL query to a database and loads the results directly into a DataFrame.',
            'filename': 'sql_query.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///shop.db&quot;)  # connect\n'
                '\n'
                'query = &quot;SELECT name, price FROM products WHERE price &gt; 50&quot;\n'
                'df = pd.read_sql(query, engine)  # run and load results\n'
                'print(df)'
            ),
            'cmd': '$ python sql_query.py',
            'output': '       name  price<br>0    Laptop  999.0<br>1   Monitor  350.0',
            'tip': 'Let SQL do heavy filtering with WHERE &#8212; it is faster to fetch fewer rows than to load everything into Python first.',
        },
        {
            'tab': 'Parameterised Query',
            'domain': 'Orders',
            'title': 'Parameterised Query',
            'pills': ['text()', 'params'],
            'desc': 'This script uses a placeholder instead of pasting a value directly into the SQL string. This prevents <strong class="text-gray-800">SQL injection</strong> and keeps your code safe.',
            'filename': 'param_query.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine, text\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///orders.db&quot;)\n'
                '\n'
                'query = text(&quot;SELECT * FROM orders WHERE total &gt; :min_val&quot;)\n'
                'df = pd.read_sql(query, engine, params={&quot;min_val&quot;: 200})\n'
                'print(df.head())'
            ),
            'cmd': '$ python param_query.py',
            'output': '   order_id  customer  total<br>0     1003     Alice    350',
            'tip': 'Never paste user input into a SQL string with f-strings &#8212; always use parameterised queries to keep your database safe.',
        },
        {
            'tab': 'SQL then Pandas',
            'domain': 'HR',
            'title': 'SQL then Pandas',
            'pills': ['combined workflow', 'groupby()'],
            'desc': 'This script fetches raw data with SQL and then summarises it with pandas. Combining both tools gives you the speed of SQL and the flexibility of Python.',
            'filename': 'sql_pandas.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///hr.db&quot;)\n'
                'df = pd.read_sql(&quot;SELECT dept, salary FROM staff&quot;, engine)\n'
                '\n'
                'avg_salary = df.groupby(&quot;dept&quot;)[&quot;salary&quot;].mean().round(2)\n'
                'print(avg_salary)'
            ),
            'cmd': '$ python sql_pandas.py',
            'output': 'dept<br>Engineering    92500.00<br>Marketing      68750.50<br>Name: salary, dtype: float64',
            'tip': 'Use SQL to pull and filter data, then use pandas to reshape and summarise &#8212; each tool does what it is best at.',
        },
    ]


def lesson04_examples():
    return [
        {
            'tab': 'Loop Over Files',
            'domain': 'Reports',
            'title': 'Loop Over Files',
            'pills': ['glob()', 'for loop'],
            'desc': 'This script finds all CSV files in a folder and reads each one in a loop. You process any number of files without writing a separate line for each.',
            'filename': 'loop_files.py',
            'code': (
                'import pandas as pd\n'
                'from pathlib import Path\n'
                '\n'
                'folder = Path(&quot;reports/&quot;)  # folder containing CSVs\n'
                '\n'
                'for file in folder.glob(&quot;*.csv&quot;):              # loop over CSV files\n'
                '    df = pd.read_csv(file)                      # read each file\n'
                '    print(f&quot;{file.name}: {len(df)} rows&quot;)      # show file name and size'
            ),
            'cmd': '$ python loop_files.py',
            'output': 'jan_report.csv: 120 rows<br>feb_report.csv: 145 rows',
            'tip': 'glob("*.csv") returns every CSV in the folder &#8212; add new files and the script picks them up automatically.',
        },
        {
            'tab': 'Combine and Summarise',
            'domain': 'Sales',
            'title': 'Combine and Summarise',
            'pills': ['pd.concat()', 'append results'],
            'desc': 'This script reads multiple files, stacks them into one DataFrame with <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">pd.concat()</code>, then calculates a grand total.',
            'filename': 'combine_files.py',
            'code': (
                'import pandas as pd\n'
                'from pathlib import Path\n'
                '\n'
                'frames = []  # empty list to collect DataFrames\n'
                'for file in Path(&quot;sales/&quot;).glob(&quot;*.csv&quot;):  # loop over files\n'
                '    frames.append(pd.read_csv(file))         # add each to the list\n'
                '\n'
                'all_sales = pd.concat(frames, ignore_index=True)  # stack together\n'
                'print(&quot;Total revenue:&quot;, all_sales[&quot;revenue&quot;].sum())'
            ),
            'cmd': '$ python combine_files.py',
            'output': 'Total revenue: 87450.0',
            'tip': 'Collect DataFrames in a list and concat once at the end &#8212; it is much faster than appending inside the loop.',
        },
        {
            'tab': 'Log the Results',
            'domain': 'ETL',
            'title': 'Log the Results',
            'pills': ['logging', 'automation'],
            'desc': 'This script processes files and writes a log message for each one. When the script runs unattended, logs tell you what happened.',
            'filename': 'log_results.py',
            'code': (
                'import pandas as pd\n'
                'import logging\n'
                '\n'
                'logging.basicConfig(filename=&quot;etl.log&quot;, level=logging.INFO)\n'
                '\n'
                'df = pd.read_csv(&quot;data.csv&quot;)      # load the data\n'
                'row_count = len(df)                 # count rows\n'
                'logging.info(f&quot;Processed {row_count} rows&quot;)  # write to log file'
            ),
            'cmd': '$ python log_results.py',
            'output': '',
            'tip': 'Logging writes to a file so you can check results later &#8212; print() output disappears as soon as the terminal closes.',
        },
    ]


def lesson05_examples():
    return [
        {
            'tab': 'Structure a Report',
            'domain': 'Finance',
            'title': 'Structure a Report',
            'pills': ['functions', 'clean flow'],
            'desc': 'This script organises a report into three clear steps: load, transform, and export. Each step is one function so the code reads like a recipe.',
            'filename': 'report_structure.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'def load_data():                               # step 1\n'
                '    return pd.read_csv(&quot;transactions.csv&quot;)\n'
                '\n'
                'def summarise(df):                             # step 2\n'
                '    return df.groupby(&quot;category&quot;)[&quot;amount&quot;].sum().reset_index()\n'
                '\n'
                'summary = summarise(load_data())  # run steps in order\n'
                'print(summary)'
            ),
            'cmd': '$ python report_structure.py',
            'output': '    category   amount<br>0   Supplies   4200.0<br>1     Travel   8750.0',
            'tip': 'Splitting your script into small functions makes each step easy to test and fix independently.',
        },
        {
            'tab': 'Format Numbers and Dates',
            'domain': 'Invoices',
            'title': 'Format Numbers and Dates',
            'pills': ['map()', 'strftime()'],
            'desc': 'This script formats money values with commas and dates in day-month-year order &#8212; ready for a report that people actually read.',
            'filename': 'format_output.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;invoices.csv&quot;, parse_dates=[&quot;date&quot;])  # load\n'
                '\n'
                'df[&quot;amount_fmt&quot;] = df[&quot;amount&quot;].map(&quot;${:,.2f}&quot;.format)  # $1,234.56\n'
                'df[&quot;date_fmt&quot;] = df[&quot;date&quot;].dt.strftime(&quot;%d %b %Y&quot;)    # 15 Mar 2026\n'
                '\n'
                'print(df[[&quot;date_fmt&quot;, &quot;amount_fmt&quot;]].head())'
            ),
            'cmd': '$ python format_output.py',
            'output': '     date_fmt  amount_fmt<br>0  15 Mar 2026  $4,200.00<br>1  22 Mar 2026  $1,875.50',
            'tip': 'Format numbers and dates last, just before exporting &#8212; formatted strings cannot be used for further calculations.',
        },
        {
            'tab': 'Export Multi-Sheet Report',
            'domain': 'HR',
            'title': 'Export Multi-Sheet Report',
            'pills': ['ExcelWriter', 'summary stats'],
            'desc': 'This script builds a report with raw data on one Excel sheet and summary statistics on another &#8212; ready to email.',
            'filename': 'export_report.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;staff.csv&quot;)  # load raw data\n'
                'summary = df.groupby(&quot;dept&quot;)[&quot;salary&quot;].agg([&quot;mean&quot;, &quot;count&quot;])\n'
                '\n'
                'with pd.ExcelWriter(&quot;hr_report.xlsx&quot;) as w:\n'
                '    df.to_excel(w, sheet_name=&quot;Raw Data&quot;, index=False)\n'
                '    summary.to_excel(w, sheet_name=&quot;Summary&quot;)\n'
                'print(&quot;Report saved&quot;)'
            ),
            'cmd': '$ python export_report.py',
            'output': 'Report saved',
            'tip': 'Always put the summary sheet first or second so stakeholders see the key numbers without scrolling through raw data.',
        },
    ]


def lesson06_examples():
    return [
        {
            'tab': 'Connect the Pipeline',
            'domain': 'Sales',
            'title': 'Connect the Pipeline',
            'pills': ['functions', 'end-to-end'],
            'desc': 'This script chains three functions into a complete pipeline: extract data, transform it, and export the result.',
            'filename': 'pipeline.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'def extract():                                 # step 1: get data\n'
                '    return pd.read_csv(&quot;sales.csv&quot;)\n'
                '\n'
                'def transform(df):                             # step 2: summarise\n'
                '    return df.groupby(&quot;region&quot;)[&quot;revenue&quot;].sum().reset_index()\n'
                '\n'
                'def export(df):                                # step 3: save\n'
                '    df.to_csv(&quot;summary.csv&quot;, index=False)\n'
                '\n'
                'export(transform(extract()))  # run all three steps'
            ),
            'cmd': '$ python pipeline.py',
            'output': '',
            'tip': 'Each function does one job &#8212; if the output looks wrong, you can test each step in isolation to find the problem.',
        },
        {
            'tab': 'Handle Errors',
            'domain': 'ETL',
            'title': 'Handle Errors',
            'pills': ['try/except', 'logging'],
            'desc': 'This script wraps each pipeline step in a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">try/except</code> block. If a step fails, the error is logged and the script continues.',
            'filename': 'error_handling.py',
            'code': (
                'import pandas as pd\n'
                'import logging\n'
                '\n'
                'logging.basicConfig(filename=&quot;pipeline.log&quot;, level=logging.INFO)\n'
                '\n'
                'try:\n'
                '    df = pd.read_csv(&quot;data.csv&quot;)           # attempt to load\n'
                '    logging.info(f&quot;Loaded {len(df)} rows&quot;)  # log success\n'
                'except FileNotFoundError as e:\n'
                '    logging.error(f&quot;File missing: {e}&quot;)     # log the error'
            ),
            'cmd': '$ python error_handling.py',
            'output': '',
            'tip': 'Wrap risky steps like file reads and database calls in try/except &#8212; the script logs the problem instead of crashing silently.',
        },
        {
            'tab': 'Schedule and Log',
            'domain': 'Reports',
            'title': 'Schedule and Log',
            'pills': ['main()', 'timestamps'],
            'desc': 'This script adds timestamps to every log message so you know exactly when each run started and finished.',
            'filename': 'scheduled_run.py',
            'code': (
                'import pandas as pd\n'
                'import logging\n'
                'from datetime import datetime\n'
                '\n'
                'logging.basicConfig(filename=&quot;runs.log&quot;, level=logging.INFO,\n'
                '                    format=&quot;%(asctime)s %(message)s&quot;)\n'
                '\n'
                'logging.info(&quot;Pipeline started&quot;)\n'
                'df = pd.read_csv(&quot;report.csv&quot;)\n'
                'logging.info(f&quot;Processed {len(df)} rows&quot;)'
            ),
            'cmd': '$ python scheduled_run.py',
            'output': '',
            'tip': 'Timestamped logs are essential for scheduled scripts &#8212; they let you trace exactly when a failure happened.',
        },
    ]


REGISTRY = {
    "lesson01_why_analysts_use_python.html": lesson01_examples,
    "lesson02_replacing_excel_workflows_with_python.html": lesson02_examples,
    "lesson03_using_python_with_sql_queries.html": lesson03_examples,
    "lesson04_automating_repetitive_data_tasks.html": lesson04_examples,
    "lesson05_building_a_simple_reporting_script.html": lesson05_examples,
    "lesson06_automating_reports_end_to_end.html": lesson06_examples,
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
