"""Rewrite #practice for every lesson in track_02 / mod_03."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_03_python_for_analysts")
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
    """Why Analysts Use Python"""
    return [
        {
            'tab': 'Sum a Column',
            'title': 'Sum a Column',
            'domain': 'Donations',
            'badges': ['sum()', 'pandas'],
            'task': 'A charity tracks donations in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">donations.csv</code> with an <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">amount</code> column. Load the file and print the total amount donated.',
            'filename': 'total_donations.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;donations.csv&quot;)  # load donation data\n'
                '\n'
                'total = df[&quot;amount&quot;].sum()  # add up all donations\n'
                'print(f&quot;Total donated: ${total:,.2f}&quot;)'
            ),
            'cmd': '$ python total_donations.py',
            'output': 'Total donated: $34,750.00',
            'tip': 'One line of pandas replaces a manual SUM formula in a spreadsheet &#8212; and you can rerun it any time new data arrives.',
        },
        {
            'tab': 'Count by Category',
            'title': 'Count by Category',
            'domain': 'Tickets',
            'badges': ['groupby()', 'count'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">support_tickets.csv</code>. Group by <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">priority</code> and count how many tickets belong to each level. Print the result.',
            'filename': 'ticket_counts.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;support_tickets.csv&quot;)  # load tickets\n'
                '\n'
                'counts = df.groupby(&quot;priority&quot;)[&quot;ticket_id&quot;].count()  # count per group\n'
                'print(counts)'
            ),
            'cmd': '$ python ticket_counts.py',
            'output': 'priority<br>High       42<br>Low       118<br>Medium     86<br>Name: ticket_id, dtype: int64',
            'tip': 'groupby() plus count() is the pandas equivalent of a COUNTIF pivot table in Excel.',
        },
        {
            'tab': 'Add Today\'s Date',
            'title': 'Add Today\'s Date',
            'domain': 'Inventory',
            'badges': ['datetime', 'import'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">stock.csv</code> and print a message showing the row count and today\'s date. Use the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">datetime</code> library to get the date.',
            'filename': 'stock_report.py',
            'code': (
                'import pandas as pd\n'
                'from datetime import date\n'
                '\n'
                'df = pd.read_csv(&quot;stock.csv&quot;)   # load inventory\n'
                'today = date.today()              # get today&apos;s date\n'
                '\n'
                'print(f&quot;Stock report: {len(df)} items as of {today}&quot;)'
            ),
            'cmd': '$ python stock_report.py',
            'output': 'Stock report: 87 items as of 2026-03-31',
            'tip': 'Combining two libraries in one script is a core Python strength &#8212; each library handles one job.',
        },
    ]


def lesson02():
    """Replacing Excel Workflows with Python"""
    return [
        {
            'tab': 'Merge Two Tables',
            'title': 'Merge Two Tables',
            'domain': 'Suppliers',
            'badges': ['pd.merge()', 'VLOOKUP'],
            'task': 'You have <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">parts.csv</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">suppliers.csv</code>. Both share a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">supplier_id</code> column. Merge them and print the first three rows to see part names next to supplier details.',
            'filename': 'merge_parts.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'parts = pd.read_csv(&quot;parts.csv&quot;)            # part records\n'
                'suppliers = pd.read_csv(&quot;suppliers.csv&quot;)    # supplier details\n'
                '\n'
                'merged = pd.merge(parts, suppliers, on=&quot;supplier_id&quot;)  # join\n'
                'print(merged.head(3))'
            ),
            'cmd': '$ python merge_parts.py',
            'output': '   part_name  supplier_id supplier_name    city<br>0     Bolt-A          201     Acme Inc  London<br>1     Gear-B          202    Beta Corp   Tokyo<br>2    Valve-C          201     Acme Inc  London',
            'tip': 'Unlike VLOOKUP, merge() handles multiple matches automatically &#8212; no need for INDEX/MATCH workarounds.',
        },
        {
            'tab': 'Build a Pivot',
            'title': 'Build a Pivot',
            'domain': 'Expenses',
            'badges': ['pivot_table()', 'aggfunc'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">expenses.csv</code> with columns department, month, and amount. Create a pivot table that sums the amount by department (rows) and month (columns). Print the result.',
            'filename': 'expense_pivot.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;expenses.csv&quot;)  # load expense data\n'
                '\n'
                'pivot = df.pivot_table(values=&quot;amount&quot;,\n'
                '                       index=&quot;department&quot;,\n'
                '                       columns=&quot;month&quot;,\n'
                '                       aggfunc=&quot;sum&quot;, fill_value=0)\n'
                'print(pivot)'
            ),
            'cmd': '$ python expense_pivot.py',
            'output': 'month        Jan    Feb    Mar<br>department<br>Marketing   4500   3800   5100<br>Operations  6200   5900   6400',
            'tip': 'This pivot table is fully reproducible &#8212; run the same script next month and the new data updates automatically.',
        },
        {
            'tab': 'Two-Sheet Report',
            'title': 'Two-Sheet Report',
            'domain': 'Projects',
            'badges': ['ExcelWriter', 'multi-sheet'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">projects.csv</code> and create a summary grouped by status. Save raw data to a "Details" sheet and the summary to a "Summary" sheet in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">project_report.xlsx</code>.',
            'filename': 'two_sheet.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;projects.csv&quot;)  # raw data\n'
                'summary = df.groupby(&quot;status&quot;)[&quot;budget&quot;].sum().reset_index()\n'
                '\n'
                'with pd.ExcelWriter(&quot;project_report.xlsx&quot;) as w:\n'
                '    df.to_excel(w, sheet_name=&quot;Details&quot;, index=False)\n'
                '    summary.to_excel(w, sheet_name=&quot;Summary&quot;, index=False)\n'
                'print(&quot;Report saved with 2 sheets&quot;)'
            ),
            'cmd': '$ python two_sheet.py',
            'output': 'Report saved with 2 sheets',
            'tip': 'Putting the summary on a separate sheet means stakeholders see the headlines first without scrolling through raw data.',
        },
    ]


def lesson03():
    """Using Python with SQL Queries"""
    return [
        {
            'tab': 'Fetch Client Data',
            'title': 'Fetch Client Data',
            'domain': 'Clients',
            'badges': ['read_sql()', 'SELECT'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">crm.db</code> and run a query to fetch all clients where <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">active = 1</code>. Print the number of active clients.',
            'filename': 'active_clients.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///crm.db&quot;)  # connect\n'
                '\n'
                'df = pd.read_sql(&quot;SELECT * FROM clients WHERE active = 1&quot;, engine)\n'
                'print(f&quot;Active clients: {len(df)}&quot;)'
            ),
            'cmd': '$ python active_clients.py',
            'output': 'Active clients: 142',
            'tip': 'Filter with SQL WHERE instead of loading everything into Python &#8212; the database is optimised for this kind of work.',
        },
        {
            'tab': 'Safe Filtering',
            'title': 'Safe Filtering',
            'domain': 'Invoices',
            'badges': ['text()', 'params'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">billing.db</code>. Use a parameterised query to find invoices with a total above a threshold stored in a variable. Print the matching rows.',
            'filename': 'safe_filter.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine, text\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///billing.db&quot;)\n'
                'min_total = 500  # threshold variable\n'
                '\n'
                'query = text(&quot;SELECT invoice_id, total FROM invoices WHERE total &gt; :amt&quot;)\n'
                'df = pd.read_sql(query, engine, params={&quot;amt&quot;: min_total})\n'
                'print(df)'
            ),
            'cmd': '$ python safe_filter.py',
            'output': '   invoice_id   total<br>0       INV-12   750.0<br>1       INV-34  1200.0',
            'tip': 'Parameterised queries prevent SQL injection. Never paste a variable directly into a SQL string with f-strings.',
        },
        {
            'tab': 'SQL then Summarise',
            'title': 'SQL then Summarise',
            'domain': 'Payroll',
            'badges': ['SQL + pandas', 'groupby()'],
            'task': 'Connect to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">company.db</code>, fetch all rows from the "payroll" table, then use pandas to calculate the average salary by department. Print the result.',
            'filename': 'sql_summarise.py',
            'code': (
                'import pandas as pd\n'
                'from sqlalchemy import create_engine\n'
                '\n'
                'engine = create_engine(&quot;sqlite:///company.db&quot;)\n'
                'df = pd.read_sql(&quot;SELECT dept, salary FROM payroll&quot;, engine)\n'
                '\n'
                'avg = df.groupby(&quot;dept&quot;)[&quot;salary&quot;].mean().round(2)\n'
                'print(avg)'
            ),
            'cmd': '$ python sql_summarise.py',
            'output': 'dept<br>Finance       72500.00<br>Marketing     61250.50<br>Name: salary, dtype: float64',
            'tip': 'Use SQL to pull and filter, then use pandas to reshape &#8212; each tool does what it is best at.',
        },
    ]


def lesson04():
    """Automating Repetitive Data Tasks"""
    return [
        {
            'tab': 'Process Survey Files',
            'title': 'Process Survey Files',
            'domain': 'Surveys',
            'badges': ['glob()', 'for loop'],
            'task': 'A folder called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">surveys/</code> contains multiple CSV files. Write a script that loops through every CSV and prints each filename with its row count.',
            'filename': 'process_surveys.py',
            'code': (
                'import pandas as pd\n'
                'from pathlib import Path\n'
                '\n'
                'folder = Path(&quot;surveys/&quot;)  # survey folder\n'
                '\n'
                'for file in folder.glob(&quot;*.csv&quot;):          # each CSV\n'
                '    df = pd.read_csv(file)                  # load it\n'
                '    print(f&quot;{file.name}: {len(df)} rows&quot;)  # report'
            ),
            'cmd': '$ python process_surveys.py',
            'output': 'jan_survey.csv: 95 rows<br>feb_survey.csv: 110 rows',
            'tip': 'glob("*.csv") finds every CSV in the folder automatically &#8212; add a new file and the script picks it up on the next run.',
        },
        {
            'tab': 'Stack and Total',
            'title': 'Stack and Total',
            'domain': 'Receipts',
            'badges': ['pd.concat()', 'sum()'],
            'task': 'Read all CSV files in a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">receipts/</code> folder, stack them into one DataFrame, and print the grand total of the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">amount</code> column.',
            'filename': 'stack_receipts.py',
            'code': (
                'import pandas as pd\n'
                'from pathlib import Path\n'
                '\n'
                'frames = []  # collect DataFrames\n'
                'for file in Path(&quot;receipts/&quot;).glob(&quot;*.csv&quot;):\n'
                '    frames.append(pd.read_csv(file))  # add each file\n'
                '\n'
                'all_data = pd.concat(frames, ignore_index=True)  # stack\n'
                'print(f&quot;Grand total: ${all_data[&apos;amount&apos;].sum():,.2f}&quot;)'
            ),
            'cmd': '$ python stack_receipts.py',
            'output': 'Grand total: $12,480.50',
            'tip': 'Collect frames in a list and concat once at the end &#8212; it is much faster than appending row by row inside the loop.',
        },
        {
            'tab': 'Log Each Step',
            'title': 'Log Each Step',
            'domain': 'Backups',
            'badges': ['logging', 'automation'],
            'task': 'Write a script that processes <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">backup.csv</code> and logs a success message to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">backup.log</code>. If the file is missing, log an error instead.',
            'filename': 'log_backup.py',
            'code': (
                'import pandas as pd\n'
                'import logging\n'
                '\n'
                'logging.basicConfig(filename=&quot;backup.log&quot;, level=logging.INFO)\n'
                '\n'
                'try:\n'
                '    df = pd.read_csv(&quot;backup.csv&quot;)                # load\n'
                '    logging.info(f&quot;Backed up {len(df)} rows&quot;)     # success\n'
                'except FileNotFoundError:\n'
                '    logging.error(&quot;backup.csv not found&quot;)          # failure'
            ),
            'cmd': '$ python log_backup.py',
            'output': '',
            'tip': 'Logging writes to a file so you can check results later &#8212; print() output disappears as soon as the terminal closes.',
        },
    ]


def lesson05():
    """Building a Simple Reporting Script"""
    return [
        {
            'tab': 'Define Helper Functions',
            'title': 'Define Helper Functions',
            'domain': 'Billing',
            'badges': ['functions', 'structure'],
            'task': 'Write a reporting script with two functions: one that loads <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">billing.csv</code> and one that summarises totals by client. Call both and print the summary.',
            'filename': 'billing_report.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'def load_data():                                # step 1\n'
                '    return pd.read_csv(&quot;billing.csv&quot;)\n'
                '\n'
                'def summarise(df):                              # step 2\n'
                '    return df.groupby(&quot;client&quot;)[&quot;total&quot;].sum().reset_index()\n'
                '\n'
                'print(summarise(load_data()))'
            ),
            'cmd': '$ python billing_report.py',
            'output': '    client   total<br>0  Acme Inc  8400.0<br>1  Beta Ltd  5200.0',
            'tip': 'Splitting logic into small functions makes each step easy to test and fix independently.',
        },
        {
            'tab': 'Format Currency',
            'title': 'Format Currency',
            'domain': 'Transactions',
            'badges': ['map()', 'formatting'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">transactions.csv</code> and add a column called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">amount_fmt</code> that shows amounts with a dollar sign and two decimal places. Print the first three rows.',
            'filename': 'format_money.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;transactions.csv&quot;)  # load data\n'
                '\n'
                'df[&quot;amount_fmt&quot;] = df[&quot;amount&quot;].map(&quot;${:,.2f}&quot;.format)  # format\n'
                'print(df[[&quot;description&quot;, &quot;amount_fmt&quot;]].head(3))'
            ),
            'cmd': '$ python format_money.py',
            'output': '     description amount_fmt<br>0  Office Rent  $4,200.00<br>1    Software    $899.00<br>2      Travel  $1,350.50',
            'tip': 'Format numbers last, just before exporting &#8212; formatted strings are text, so pandas cannot do maths on them.',
        },
        {
            'tab': 'Save a Summary Sheet',
            'title': 'Save a Summary Sheet',
            'domain': 'Staff',
            'badges': ['ExcelWriter', 'export'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">staff.csv</code> and create a headcount summary by department. Save raw data and the summary to separate sheets in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">staff_report.xlsx</code>.',
            'filename': 'staff_report.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;staff.csv&quot;)  # raw data\n'
                'headcount = df[&quot;department&quot;].value_counts().reset_index()\n'
                '\n'
                'with pd.ExcelWriter(&quot;staff_report.xlsx&quot;) as w:\n'
                '    df.to_excel(w, sheet_name=&quot;Full List&quot;, index=False)\n'
                '    headcount.to_excel(w, sheet_name=&quot;Headcount&quot;, index=False)\n'
                'print(&quot;Staff report saved&quot;)'
            ),
            'cmd': '$ python staff_report.py',
            'output': 'Staff report saved',
            'tip': 'Always put the summary sheet first or second so stakeholders see the key numbers without searching through tabs.',
        },
    ]


def lesson06():
    """Automating Reports End to End"""
    return [
        {
            'tab': 'Chain Three Steps',
            'title': 'Chain Three Steps',
            'domain': 'Revenue',
            'badges': ['functions', 'pipeline'],
            'task': 'Write a pipeline script with three functions: extract loads <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">revenue.csv</code>, transform groups by quarter, and export saves to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">quarterly.csv</code>. Call them in order.',
            'filename': 'revenue_pipeline.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'def extract():                                  # step 1\n'
                '    return pd.read_csv(&quot;revenue.csv&quot;)\n'
                '\n'
                'def transform(df):                              # step 2\n'
                '    return df.groupby(&quot;quarter&quot;)[&quot;amount&quot;].sum().reset_index()\n'
                '\n'
                'def export(df):                                 # step 3\n'
                '    df.to_csv(&quot;quarterly.csv&quot;, index=False)\n'
                '\n'
                'export(transform(extract()))'
            ),
            'cmd': '$ python revenue_pipeline.py',
            'output': '',
            'tip': 'Each function does one job. If the output looks wrong, you can test each step in isolation to find the problem.',
        },
        {
            'tab': 'Catch File Errors',
            'title': 'Catch File Errors',
            'domain': 'Downloads',
            'badges': ['try/except', 'logging'],
            'task': 'Write a script that tries to load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">downloads.csv</code>. If the file is missing, log the error to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">pipeline.log</code> instead of crashing.',
            'filename': 'catch_errors.py',
            'code': (
                'import pandas as pd\n'
                'import logging\n'
                '\n'
                'logging.basicConfig(filename=&quot;pipeline.log&quot;, level=logging.INFO)\n'
                '\n'
                'try:\n'
                '    df = pd.read_csv(&quot;downloads.csv&quot;)           # load\n'
                '    logging.info(f&quot;Loaded {len(df)} rows&quot;)      # success\n'
                'except FileNotFoundError as e:\n'
                '    logging.error(f&quot;Missing file: {e}&quot;)         # log error'
            ),
            'cmd': '$ python catch_errors.py',
            'output': '',
            'tip': 'Wrap risky steps like file reads in try/except &#8212; the script logs the problem instead of crashing silently.',
        },
        {
            'tab': 'Add Timestamps',
            'title': 'Add Timestamps',
            'domain': 'Audit',
            'badges': ['asctime', 'log format'],
            'task': 'Write a script that loads <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">audit.csv</code> and logs a timestamped message to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">audit.log</code> showing how many rows were processed.',
            'filename': 'timestamped_log.py',
            'code': (
                'import pandas as pd\n'
                'import logging\n'
                '\n'
                'logging.basicConfig(filename=&quot;audit.log&quot;, level=logging.INFO,\n'
                '                    format=&quot;%(asctime)s %(message)s&quot;)\n'
                '\n'
                'df = pd.read_csv(&quot;audit.csv&quot;)                    # load data\n'
                'logging.info(f&quot;Processed {len(df)} audit records&quot;)'
            ),
            'cmd': '$ python timestamped_log.py',
            'output': '',
            'tip': 'Timestamped logs are essential for scheduled scripts &#8212; they let you trace exactly when each run happened.',
        },
    ]


REGISTRY = {
    "lesson01_why_analysts_use_python.html": lesson01,
    "lesson02_replacing_excel_workflows_with_python.html": lesson02,
    "lesson03_using_python_with_sql_queries.html": lesson03,
    "lesson04_automating_repetitive_data_tasks.html": lesson04,
    "lesson05_building_a_simple_reporting_script.html": lesson05,
    "lesson06_automating_reports_end_to_end.html": lesson06,
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
