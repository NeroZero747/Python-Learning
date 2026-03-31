"""Rewrite #code-examples for every lesson in track_02 / mod_01."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_01_data_analysis_with_pandas")
SECTION_RE = re.compile(
    r'(<section id="code-examples"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── HTML builder helpers ─────────────────────────────────────────

def pill_tabs(tabs):
    """tabs = [(label, ...), ...]"""
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
    """ex = dict with keys: tab, domain, title, pills, desc, filename, code, cmd, output, tip"""
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
            'tab': 'Create a DataFrame',
            'domain': 'Products',
            'title': 'Create a DataFrame',
            'pills': ['pd.DataFrame()', 'dict'],
            'desc': 'This script builds a <strong class="text-gray-800">DataFrame</strong> from a Python dictionary. Each key becomes a column name and each list becomes the column values.',
            'filename': 'create_df.py',
            'code': (
                'import pandas as pd  # load the pandas library\n'
                '\n'
                'products = {&quot;name&quot;: [&quot;Laptop&quot;, &quot;Mouse&quot;, &quot;Keyboard&quot;],  # column 1\n'
                '            &quot;price&quot;: [999, 25, 75]}                 # column 2\n'
                '\n'
                'df = pd.DataFrame(products)  # convert dict to a DataFrame\n'
                'print(df)                     # display the table'
            ),
            'cmd': '$ python create_df.py',
            'output': '       name  price<br>0    Laptop    999<br>1     Mouse     25<br>2  Keyboard     75',
            'tip': 'A DataFrame is just a table &#8212; if you can picture rows and columns in a spreadsheet, you already understand it.',
        },
        {
            'tab': 'Read a CSV File',
            'domain': 'Orders',
            'title': 'Read a CSV File',
            'pills': ['pd.read_csv()', 'head()'],
            'desc': 'This script reads a CSV file into a DataFrame using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">pd.read_csv()</code> and prints the first few rows.',
            'filename': 'read_orders.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;orders.csv&quot;)  # read the CSV file\n'
                'print(df.head())                  # show first 5 rows'
            ),
            'cmd': '$ python read_orders.py',
            'output': '   order_id  product  quantity<br>0      1001   Laptop         1<br>1      1002    Mouse         3',
            'tip': 'You can load thousands of rows in one line &#8212; no more opening files manually in Excel.',
        },
        {
            'tab': 'Inspect a DataFrame',
            'domain': 'Students',
            'title': 'Inspect a DataFrame',
            'pills': ['shape', 'dtypes', 'describe()'],
            'desc': 'This script loads data and checks its size, column types, and summary statistics. These three checks help you understand your data before you start working with it.',
            'filename': 'inspect_students.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;students.csv&quot;)  # load student data\n'
                '\n'
                'print(df.shape)       # count rows and columns\n'
                'print(df.dtypes)      # check each column&apos;s data type\n'
                'print(df.describe())  # get summary statistics'
            ),
            'cmd': '$ python inspect_students.py',
            'output': '(150, 4)<br>name     object<br>age       int64<br>grade   float64',
            'tip': 'Always run shape and dtypes first &#8212; they tell you how much data you have and whether each column loaded correctly.',
        },
    ]


def lesson02_examples():
    return [
        {
            'tab': 'Build from a Dictionary',
            'domain': 'Books',
            'title': 'Build from a Dictionary',
            'pills': ['pd.DataFrame()', 'dict'],
            'desc': 'This script creates a <strong class="text-gray-800">DataFrame</strong> from a dictionary. Each key becomes a column and each list becomes the values.',
            'filename': 'books_df.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'books = {&quot;title&quot;: [&quot;Python 101&quot;, &quot;Data Basics&quot;],  # column 1\n'
                '         &quot;pages&quot;: [250, 180]}                       # column 2\n'
                '\n'
                'df = pd.DataFrame(books)  # build the table\n'
                'print(df)                 # display it'
            ),
            'cmd': '$ python books_df.py',
            'output': '         title  pages<br>0   Python 101    250<br>1  Data Basics    180',
            'tip': 'A dictionary is the quickest way to create a small DataFrame for testing or prototyping.',
        },
        {
            'tab': 'Check Index and Columns',
            'domain': 'Employees',
            'title': 'Check Index and Columns',
            'pills': ['index', 'columns', 'shape'],
            'desc': 'This script shows how to inspect a DataFrame&apos;s <strong class="text-gray-800">index</strong>, column names, and overall dimensions.',
            'filename': 'check_structure.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;employees.csv&quot;)  # load employee data\n'
                '\n'
                'print(df.index)    # show the row labels\n'
                'print(df.columns)  # list all column names\n'
                'print(df.shape)    # count (rows, columns)'
            ),
            'cmd': '$ python check_structure.py',
            'output': "RangeIndex(start=0, stop=50, step=1)<br>Index(['name', 'department', 'salary'], dtype='object')<br>(50, 3)",
            'tip': 'The index is the row label &#8212; pandas creates one automatically starting at zero unless you specify your own.',
        },
        {
            'tab': 'Check Data Types',
            'domain': 'Products',
            'title': 'Check Data Types',
            'pills': ['dtypes', 'info()'],
            'desc': 'This script uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">dtypes</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">info()</code> to check what type of data each column holds &#8212; text, whole numbers, or decimals.',
            'filename': 'check_types.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;products.csv&quot;)  # load product data\n'
                '\n'
                'print(df.dtypes)  # show type of each column\n'
                'print(df.info())  # show types plus memory usage'
            ),
            'cmd': '$ python check_types.py',
            'output': "name      object<br>price    float64<br>stock      int64",
            'tip': 'If a number column shows as "object", the file probably has text mixed in &#8212; fix that before doing any calculations.',
        },
    ]


def lesson03_examples():
    return [
        {
            'tab': 'Load a CSV',
            'domain': 'Sales',
            'title': 'Load a CSV',
            'pills': ['pd.read_csv()', 'head()'],
            'desc': 'This script reads a CSV file into a DataFrame and prints the first five rows to confirm the data loaded correctly.',
            'filename': 'load_sales.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;sales.csv&quot;)  # read the CSV file\n'
                '\n'
                'print(df.head())  # show the first 5 rows'
            ),
            'cmd': '$ python load_sales.py',
            'output': '   date        product  amount<br>0  2025-01-01  Widget     150',
            'tip': 'Always call head() right after loading &#8212; it catches problems like wrong separators or missing headers instantly.',
        },
        {
            'tab': 'Read an Excel File',
            'domain': 'Inventory',
            'title': 'Read an Excel File',
            'pills': ['read_excel()', 'sheet_name'],
            'desc': 'This script loads a specific sheet from an Excel workbook using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">pd.read_excel()</code> and the <strong class="text-gray-800">sheet_name</strong> parameter.',
            'filename': 'load_inventory.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_excel(&quot;stock.xlsx&quot;,          # path to the workbook\n'
                '                   sheet_name=&quot;Sheet1&quot;)  # which sheet to read\n'
                '\n'
                'print(df.head())  # show first rows'
            ),
            'cmd': '$ python load_inventory.py',
            'output': '   item_code  item_name  qty_on_hand<br>0       A100     Widget          320',
            'tip': 'If the sheet name has spaces, wrap it in quotes exactly as it appears in Excel &#8212; spelling must match.',
        },
        {
            'tab': 'Fix a Load Error',
            'domain': 'Transactions',
            'title': 'Fix a Load Error',
            'pills': ['sep', 'encoding', 'error handling'],
            'desc': 'This script fixes two common load problems at once: a semicolon separator and a non-standard text encoding.',
            'filename': 'fix_load.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;transactions.csv&quot;,   # file path\n'
                '                 sep=&quot;;&quot;,               # semicolon separator\n'
                '                 encoding=&quot;latin-1&quot;)   # fix special characters\n'
                '\n'
                'print(df.head())   # check rows loaded correctly\n'
                'print(df.shape)    # confirm row and column count'
            ),
            'cmd': '$ python fix_load.py',
            'output': '   trans_id  merchant    amount<br>0     5001   CaféShop   42.50<br>(1200, 3)',
            'tip': 'European CSV files often use semicolons and latin-1 encoding &#8212; try these two parameters first when a file looks broken.',
        },
    ]


def lesson04_examples():
    return [
        {
            'tab': 'Select One Column',
            'domain': 'Employees',
            'title': 'Select One Column',
            'pills': ['df["col"]', 'Series'],
            'desc': 'This script picks a single column from a DataFrame using square brackets. The result is a <strong class="text-gray-800">Series</strong> &#8212; a one-column list of values.',
            'filename': 'select_one.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;employees.csv&quot;)  # load data\n'
                '\n'
                'names = df[&quot;name&quot;]  # select the name column\n'
                'print(names)         # display the Series'
            ),
            'cmd': '$ python select_one.py',
            'output': '0      Alice<br>1        Bob<br>2    Charlie<br>Name: name, dtype: object',
            'tip': 'The column name inside the brackets must match exactly &#8212; including uppercase, lowercase, and spaces.',
        },
        {
            'tab': 'Select Multiple Columns',
            'domain': 'Products',
            'title': 'Select Multiple Columns',
            'pills': ['df[["a","b"]]', 'DataFrame'],
            'desc': 'This script selects two columns at once by passing a list of column names. The result stays as a DataFrame.',
            'filename': 'select_multi.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;products.csv&quot;)  # load data\n'
                '\n'
                'subset = df[[&quot;name&quot;, &quot;price&quot;]]  # pick two columns\n'
                'print(subset.head())              # show first rows'
            ),
            'cmd': '$ python select_multi.py',
            'output': '       name  price<br>0    Laptop    999<br>1     Mouse     25',
            'tip': 'Notice the double brackets &#8212; the inner list tells pandas which columns you want, and the outer brackets do the selection.',
        },
        {
            'tab': 'Rename Columns',
            'domain': 'Orders',
            'title': 'Rename Columns',
            'pills': ['rename()', 'columns'],
            'desc': 'This script renames columns using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">rename()</code> and lists all column names before and after the change.',
            'filename': 'rename_cols.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;orders.csv&quot;)  # load data\n'
                'print(df.columns.tolist())       # show original names\n'
                '\n'
                'df = df.rename(columns={&quot;qty&quot;: &quot;quantity&quot;})  # rename one column\n'
                'print(df.columns.tolist())                     # confirm the change'
            ),
            'cmd': '$ python rename_cols.py',
            'output': "['order_id', 'product', 'qty']<br>['order_id', 'product', 'quantity']",
            'tip': 'rename() returns a new DataFrame by default &#8212; assign it back to df or the original stays unchanged.',
        },
    ]


def lesson05_examples():
    return [
        {
            'tab': 'Filter by Condition',
            'domain': 'Products',
            'title': 'Filter by Condition',
            'pills': ['boolean mask', 'comparison'],
            'desc': 'This script filters rows where the price is above 50. The condition inside the brackets creates a true/false mask that keeps only matching rows.',
            'filename': 'filter_price.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;products.csv&quot;)  # load product data\n'
                '\n'
                'expensive = df[df[&quot;price&quot;] &gt; 50]  # keep rows where price &gt; 50\n'
                'print(expensive)                     # show filtered result'
            ),
            'cmd': '$ python filter_price.py',
            'output': '     name  price<br>0  Laptop    999<br>2  Monitor   350',
            'tip': 'The condition inside the brackets is evaluated row by row &#8212; only rows that return True survive.',
        },
        {
            'tab': 'Combine Conditions',
            'domain': 'Orders',
            'title': 'Combine Conditions',
            'pills': ['&amp; operator', 'multiple filters'],
            'desc': 'This script applies two filters at once using the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">&amp;</code> operator. Each condition is wrapped in parentheses.',
            'filename': 'filter_combined.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;orders.csv&quot;)  # load order data\n'
                '\n'
                'result = df[(df[&quot;quantity&quot;] &gt; 2) &amp;   # more than 2 items\n'
                '            (df[&quot;total&quot;] &gt; 100)]      # AND total over 100\n'
                '\n'
                'print(result)  # show matching orders'
            ),
            'cmd': '$ python filter_combined.py',
            'output': '   order_id  product  quantity  total<br>3     1004   Keyboard       5    375',
            'tip': 'Always wrap each condition in parentheses when combining with &amp; or | &#8212; without them, Python will throw an error.',
        },
        {
            'tab': 'Filter with a List',
            'domain': 'Students',
            'title': 'Filter with a List',
            'pills': ['isin()', 'dropna()'],
            'desc': 'This script filters rows where a column value matches any item in a list, then removes rows with missing data.',
            'filename': 'filter_list.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;students.csv&quot;)  # load student data\n'
                '\n'
                'target = [&quot;Maths&quot;, &quot;Science&quot;]          # subjects to keep\n'
                'filtered = df[df[&quot;subject&quot;].isin(target)]  # keep matching rows\n'
                'clean = filtered.dropna()                    # remove missing values\n'
                'print(clean)'
            ),
            'cmd': '$ python filter_list.py',
            'output': '     name  subject  score<br>0   Alice    Maths   88.0<br>2  Charlie  Science   72.0',
            'tip': 'isin() is the pandas version of SQL&apos;s IN clause &#8212; use it whenever you need to match against a set of values.',
        },
    ]


def lesson06_examples():
    return [
        {
            'tab': 'Add a Column',
            'domain': 'Products',
            'title': 'Add a Column',
            'pills': ['arithmetic', 'new column'],
            'desc': 'This script creates a new column by multiplying two existing columns together. Pandas applies the calculation to every row at once.',
            'filename': 'add_column.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;products.csv&quot;)  # load product data\n'
                '\n'
                'df[&quot;total&quot;] = df[&quot;price&quot;] * df[&quot;quantity&quot;]  # multiply two columns\n'
                'print(df)                                     # show the result'
            ),
            'cmd': '$ python add_column.py',
            'output': '       name  price  quantity  total<br>0    Laptop    999         1    999<br>1     Mouse     25         4    100',
            'tip': 'You can use +, -, *, / between columns &#8212; pandas calculates every row in one step, no loops needed.',
        },
        {
            'tab': 'Conditional Values',
            'domain': 'Orders',
            'title': 'Conditional Values',
            'pills': ['np.where()', 'condition'],
            'desc': 'This script uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">np.where()</code> to set a column value based on a condition &#8212; one value when true, another when false.',
            'filename': 'conditional_col.py',
            'code': (
                'import pandas as pd    # load pandas\n'
                'import numpy as np     # load numpy for np.where\n'
                '\n'
                'df = pd.read_csv(&quot;orders.csv&quot;)  # load order data\n'
                '\n'
                'df[&quot;size&quot;] = np.where(df[&quot;total&quot;] &gt; 100,  # condition\n'
                '                       &quot;Large&quot;, &quot;Small&quot;)    # true / false values\n'
                'print(df[[&quot;order_id&quot;, &quot;total&quot;, &quot;size&quot;]])'
            ),
            'cmd': '$ python conditional_col.py',
            'output': '   order_id  total   size<br>0     1001    250  Large<br>1     1002     45  Small',
            'tip': 'np.where() works like an IF function in Excel &#8212; condition first, then the value-if-true, then value-if-false.',
        },
        {
            'tab': 'Drop a Column',
            'domain': 'Employees',
            'title': 'Drop a Column',
            'pills': ['drop()', 'axis=1'],
            'desc': 'This script removes an unwanted column using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">drop()</code> and confirms it is gone by printing the remaining column names.',
            'filename': 'drop_column.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;employees.csv&quot;)  # load data\n'
                'print(df.columns.tolist())           # before: all columns\n'
                '\n'
                'df = df.drop(columns=[&quot;temp_id&quot;])  # remove the column\n'
                'print(df.columns.tolist())           # after: column is gone'
            ),
            'cmd': '$ python drop_column.py',
            'output': "['name', 'department', 'salary', 'temp_id']<br>['name', 'department', 'salary']",
            'tip': 'Use columns= instead of axis=1 &#8212; it makes the code easier to read and harder to get wrong.',
        },
    ]


def lesson07_examples():
    return [
        {
            'tab': 'Group and Sum',
            'domain': 'Sales',
            'title': 'Group and Sum',
            'pills': ['groupby()', 'sum()'],
            'desc': 'This script groups rows by category and calculates the total for each group &#8212; like a SUM formula in a pivot table.',
            'filename': 'group_sum.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;sales.csv&quot;)  # load sales data\n'
                '\n'
                'totals = df.groupby(&quot;region&quot;)[&quot;revenue&quot;].sum()  # sum by region\n'
                'print(totals)  # show the result'
            ),
            'cmd': '$ python group_sum.py',
            'output': 'region<br>East     4500<br>North    3200<br>West     5100<br>Name: revenue, dtype: int64',
            'tip': 'groupby() splits your data into groups, then the aggregation function (sum, mean, count) does the maths on each group.',
        },
        {
            'tab': 'Multiple Aggregations',
            'domain': 'Orders',
            'title': 'Multiple Aggregations',
            'pills': ['agg()', 'multiple functions'],
            'desc': 'This script calculates several statistics for each group at once using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">.agg()</code>.',
            'filename': 'multi_agg.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;orders.csv&quot;)  # load order data\n'
                '\n'
                'summary = df.groupby(&quot;product&quot;)[&quot;total&quot;].agg(  # group and aggregate\n'
                '    [&quot;sum&quot;, &quot;mean&quot;, &quot;count&quot;])                       # three functions\n'
                '\n'
                'print(summary)  # show grouped stats'
            ),
            'cmd': '$ python multi_agg.py',
            'output': '           sum   mean  count<br>product<br>Keyboard  1500  375.0      4<br>Mouse      600  150.0      4',
            'tip': 'Pass a list of function names as strings to agg() &#8212; you get one column for each function in the result.',
        },
        {
            'tab': 'Reset the Index',
            'domain': 'Employees',
            'title': 'Reset the Index',
            'pills': ['reset_index()', 'clean output'],
            'desc': 'After groupby, the grouped column becomes the index. This script uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">reset_index()</code> to turn it back into a regular column.',
            'filename': 'reset_idx.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;employees.csv&quot;)  # load data\n'
                '\n'
                'avg_sal = df.groupby(&quot;department&quot;)[&quot;salary&quot;].mean()  # average salary\n'
                'avg_sal = avg_sal.reset_index()  # move department back to a column\n'
                'avg_sal.columns = [&quot;department&quot;, &quot;avg_salary&quot;]  # rename for clarity\n'
                'print(avg_sal)'
            ),
            'cmd': '$ python reset_idx.py',
            'output': '  department  avg_salary<br>0  Engineering     85000.0<br>1    Marketing     72000.0',
            'tip': 'Call reset_index() whenever you want to save or merge your grouped results &#8212; most pandas operations expect a clean numeric index.',
        },
    ]


def lesson08_examples():
    return [
        {
            'tab': 'Merge Two Tables',
            'domain': 'Orders',
            'title': 'Merge Two Tables',
            'pills': ['pd.merge()', 'on'],
            'desc': 'This script joins two DataFrames on a shared column using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">pd.merge()</code>. Matching rows are combined into a single table.',
            'filename': 'merge_basic.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'orders = pd.read_csv(&quot;orders.csv&quot;)        # order details\n'
                'customers = pd.read_csv(&quot;customers.csv&quot;)  # customer details\n'
                '\n'
                'merged = pd.merge(orders, customers, on=&quot;customer_id&quot;)  # join on key\n'
                'print(merged.head())  # show combined table'
            ),
            'cmd': '$ python merge_basic.py',
            'output': '   order_id  customer_id  total customer_name<br>0     1001          101    250         Alice',
            'tip': 'The on= column must exist in both DataFrames with the same name &#8212; check spelling and case before merging.',
        },
        {
            'tab': 'Left Join',
            'domain': 'Products',
            'title': 'Left Join',
            'pills': ['how="left"', 'NaN matches'],
            'desc': 'This script uses a left join to keep every row from the left table. Rows with no match in the right table get NaN values.',
            'filename': 'left_join.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'products = pd.read_csv(&quot;products.csv&quot;)      # all products\n'
                'suppliers = pd.read_csv(&quot;suppliers.csv&quot;)    # supplier info\n'
                '\n'
                'result = pd.merge(products, suppliers,\n'
                '                  on=&quot;supplier_id&quot;, how=&quot;left&quot;)  # keep all products\n'
                'print(result.head())'
            ),
            'cmd': '$ python left_join.py',
            'output': '     name  supplier_id supplier_name<br>0  Laptop          101     TechCorp<br>1   Mouse          NaN           NaN',
            'tip': 'A left join never drops rows from your main table &#8212; use it when you want to add extra columns without losing data.',
        },
        {
            'tab': 'Join on Multiple Keys',
            'domain': 'Sales',
            'title': 'Join on Multiple Keys',
            'pills': ['on=[list]', 'composite key'],
            'desc': 'This script merges on two columns at once &#8212; both must match for rows to join. Use this when a single column is not unique enough.',
            'filename': 'multi_key.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'sales = pd.read_csv(&quot;sales.csv&quot;)      # monthly sales\n'
                'targets = pd.read_csv(&quot;targets.csv&quot;)  # monthly targets\n'
                '\n'
                'combined = pd.merge(sales, targets,\n'
                '                    on=[&quot;region&quot;, &quot;month&quot;])  # match on two columns\n'
                'print(combined.head())'
            ),
            'cmd': '$ python multi_key.py',
            'output': '  region  month  revenue  target<br>0   East    Jan     4500    4000',
            'tip': 'If you merge on a single column and get duplicate rows, you probably need to add a second key to make each match unique.',
        },
    ]


def lesson09_examples():
    return [
        {
            'tab': 'Detect Missing Values',
            'domain': 'Survey',
            'title': 'Detect Missing Values',
            'pills': ['isna()', 'sum()'],
            'desc': 'This script counts how many missing values each column has. A count of zero means the column is complete.',
            'filename': 'detect_missing.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;survey.csv&quot;)  # load survey responses\n'
                '\n'
                'missing = df.isna().sum()  # count NaN per column\n'
                'print(missing)             # show the counts'
            ),
            'cmd': '$ python detect_missing.py',
            'output': 'name       0<br>age        3<br>rating     5<br>dtype: int64',
            'tip': 'Run isna().sum() right after loading any file &#8212; it tells you exactly which columns need attention.',
        },
        {
            'tab': 'Drop Missing Rows',
            'domain': 'Patients',
            'title': 'Drop Missing Rows',
            'pills': ['dropna()', 'subset'],
            'desc': 'This script removes rows that have missing values in specific columns using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">dropna(subset=)</code>.',
            'filename': 'drop_missing.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;patients.csv&quot;)  # load patient data\n'
                'print(df.shape)                    # before: row count\n'
                '\n'
                'df = df.dropna(subset=[&quot;age&quot;, &quot;diagnosis&quot;])  # drop if age or diagnosis missing\n'
                'print(df.shape)  # after: fewer rows'
            ),
            'cmd': '$ python drop_missing.py',
            'output': '(200, 5)<br>(187, 5)',
            'tip': 'Use subset= to target only the critical columns &#8212; dropping every row with any NaN could remove too much data.',
        },
        {
            'tab': 'Fill Missing Values',
            'domain': 'Scores',
            'title': 'Fill Missing Values',
            'pills': ['fillna()', 'mean()'],
            'desc': 'This script replaces missing values with the column&apos;s average using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">fillna()</code>. This is useful when dropping rows would lose too much data.',
            'filename': 'fill_missing.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;scores.csv&quot;)  # load test scores\n'
                '\n'
                'avg_score = df[&quot;score&quot;].mean()         # calculate the average\n'
                'df[&quot;score&quot;] = df[&quot;score&quot;].fillna(avg_score)  # replace NaN with average\n'
                '\n'
                'print(df[&quot;score&quot;].isna().sum())  # confirm: should be 0'
            ),
            'cmd': '$ python fill_missing.py',
            'output': '0',
            'tip': 'Filling with the mean works well for normally distributed numbers &#8212; for skewed data, consider using the median instead.',
        },
    ]


def lesson10_examples():
    return [
        {
            'tab': 'Save to CSV',
            'domain': 'Reports',
            'title': 'Save to CSV',
            'pills': ['to_csv()', 'index=False'],
            'desc': 'This script saves a DataFrame to a CSV file. Setting <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">index=False</code> prevents pandas from adding an extra index column.',
            'filename': 'save_csv.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;cleaned_data.csv&quot;)  # load processed data\n'
                '\n'
                'df.to_csv(&quot;output.csv&quot;, index=False)  # save without index column\n'
                'print(&quot;Saved&quot;, len(df), &quot;rows to output.csv&quot;)  # confirm'
            ),
            'cmd': '$ python save_csv.py',
            'output': 'Saved 500 rows to output.csv',
            'tip': 'Always set index=False unless you specifically need the row numbers &#8212; most people opening the file in Excel will not want them.',
        },
        {
            'tab': 'Write to Excel',
            'domain': 'Budgets',
            'title': 'Write to Excel',
            'pills': ['to_excel()', 'ExcelWriter'],
            'desc': 'This script writes a DataFrame to an Excel file. It uses <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">to_excel()</code> to create a workbook with named sheets.',
            'filename': 'save_excel.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;budget.csv&quot;)  # load budget data\n'
                '\n'
                'df.to_excel(&quot;budget_report.xlsx&quot;,     # output file name\n'
                '            sheet_name=&quot;Summary&quot;,     # name the sheet\n'
                '            index=False)               # skip the index\n'
                'print(&quot;Excel file saved&quot;)'
            ),
            'cmd': '$ python save_excel.py',
            'output': 'Excel file saved',
            'tip': 'You need the openpyxl package installed to write Excel files &#8212; run pip install openpyxl if you get an import error.',
        },
        {
            'tab': 'Export Selected Columns',
            'domain': 'Customers',
            'title': 'Export Selected Columns',
            'pills': ['columns filter', 'to_csv()'],
            'desc': 'This script picks only the columns you need, then exports them. This keeps the output file small and focused.',
            'filename': 'export_cols.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;customers.csv&quot;)  # load full dataset\n'
                '\n'
                'keep = [&quot;name&quot;, &quot;email&quot;, &quot;city&quot;]  # columns to export\n'
                'df[keep].to_csv(&quot;contacts.csv&quot;, index=False)  # save subset\n'
                '\n'
                'print(&quot;Exported&quot;, len(keep), &quot;columns&quot;)  # confirm'
            ),
            'cmd': '$ python export_cols.py',
            'output': 'Exported 3 columns',
            'tip': 'Select your columns before exporting &#8212; sending a 20-column file when people only need three wastes everyone&apos;s time.',
        },
    ]


REGISTRY = {
    "lesson01_introduction_to_pandas.html": lesson01_examples,
    "lesson02_dataframes_explained.html": lesson02_examples,
    "lesson03_reading_data_csv_excel.html": lesson03_examples,
    "lesson04_selecting_columns.html": lesson04_examples,
    "lesson05_filtering_rows.html": lesson05_examples,
    "lesson06_creating_calculated_columns.html": lesson06_examples,
    "lesson07_aggregations_group_by.html": lesson07_examples,
    "lesson08_joining_data_merge.html": lesson08_examples,
    "lesson09_handling_missing_data.html": lesson09_examples,
    "lesson10_exporting_data.html": lesson10_examples,
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
