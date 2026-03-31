"""Rewrite #practice for every lesson in track_02 / mod_01."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_01_data_analysis_with_pandas")
SECTION_RE = re.compile(
    r'(<section id="practice"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── HTML builder helpers ─────────────────────────────────────────

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
    """Introduction to Pandas"""
    return [
        {
            'tab': 'Build an Inventory',
            'title': 'Build an Inventory',
            'domain': 'Bookshop',
            'badges': ['pd.DataFrame', 'dict'],
            'task': 'A bookshop owner wants a quick list of three books with their prices. Create a DataFrame from a dictionary with columns <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">title</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">price</code>. Print the full table.',
            'filename': 'book_inventory.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'books = {&quot;title&quot;: [&quot;Python Basics&quot;, &quot;Data Science&quot;, &quot;SQL Guide&quot;],  # book titles\n'
                '         &quot;price&quot;: [29.99, 39.99, 24.99]}                        # prices\n'
                '\n'
                'df = pd.DataFrame(books)  # create the DataFrame\n'
                'print(df)                  # display the table'
            ),
            'cmd': '$ python book_inventory.py',
            'output': '            title  price<br>0   Python Basics  29.99<br>1   Data Science  39.99<br>2      SQL Guide  24.99',
            'tip': 'A DataFrame is just a table with labelled rows and columns &#8212; think of it as a spreadsheet you can control with code.',
        },
        {
            'tab': 'Load a Dataset',
            'title': 'Load a Dataset',
            'domain': 'Movies',
            'badges': ['read_csv()', 'head()'],
            'task': 'You have a CSV file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">movies.csv</code> with columns for title, genre, and rating. Load the file and display the first three rows.',
            'filename': 'load_movies.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;movies.csv&quot;)  # load the CSV file\n'
                'print(df.head(3))               # show the first 3 rows'
            ),
            'cmd': '$ python load_movies.py',
            'output': '           title   genre  rating<br>0   The Matrix  Action     8.7<br>1     Frozen  Family     7.4<br>2  Inception  Sci-Fi     8.8',
            'tip': 'The head() method is a quick way to peek at your data without printing thousands of rows.',
        },
        {
            'tab': 'Count the Rows',
            'title': 'Count the Rows',
            'domain': 'Restaurants',
            'badges': ['shape', 'columns'],
            'task': 'A food inspector has a file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">restaurants.csv</code>. Load it, print the number of rows and columns, then print the column names.',
            'filename': 'inspect_restaurants.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;restaurants.csv&quot;)  # load the file\n'
                '\n'
                'print(&quot;Rows:&quot;, df.shape[0])    # number of rows\n'
                'print(&quot;Columns:&quot;, df.shape[1])  # number of columns\n'
                'print(df.columns.tolist())      # list column names'
            ),
            'cmd': '$ python inspect_restaurants.py',
            'output': 'Rows: 85<br>Columns: 4<br>[&apos;name&apos;, &apos;cuisine&apos;, &apos;rating&apos;, &apos;city&apos;]',
            'tip': 'Always check shape and column names first &#8212; knowing how big your data is and what columns exist saves time later.',
        },
    ]


def lesson02():
    """DataFrames Explained"""
    return [
        {
            'tab': 'Create from Scratch',
            'title': 'Create from Scratch',
            'domain': 'Weather',
            'badges': ['pd.DataFrame', 'dict'],
            'task': 'Build a DataFrame of three cities with their average temperatures: London 15, Tokyo 22, Sydney 25. Print the full table.',
            'filename': 'city_temps.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'data = {&quot;city&quot;: [&quot;London&quot;, &quot;Tokyo&quot;, &quot;Sydney&quot;],  # city names\n'
                '        &quot;avg_temp&quot;: [15, 22, 25]}                 # temperatures\n'
                '\n'
                'df = pd.DataFrame(data)  # build the table\n'
                'print(df)                 # display it'
            ),
            'cmd': '$ python city_temps.py',
            'output': '     city  avg_temp<br>0  London        15<br>1   Tokyo        22<br>2  Sydney        25',
            'tip': 'Every dictionary key becomes a column name. Keep names short and lowercase &#8212; you will type them often.',
        },
        {
            'tab': 'List the Columns',
            'title': 'List the Columns',
            'domain': 'Fitness',
            'badges': ['columns', 'dtypes'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">workouts.csv</code> and print the column names on one line, then print the data type of each column.',
            'filename': 'workout_columns.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;workouts.csv&quot;)  # load workout log\n'
                '\n'
                'print(df.columns.tolist())  # column names\n'
                'print(df.dtypes)            # data type per column'
            ),
            'cmd': '$ python workout_columns.py',
            'output': '[&apos;date&apos;, &apos;exercise&apos;, &apos;duration_min&apos;, &apos;calories&apos;]<br>date            object<br>exercise        object<br>duration_min     int64<br>calories         int64',
            'tip': 'Checking dtypes early catches problems like numbers stored as text &#8212; pandas cannot do maths on text columns.',
        },
        {
            'tab': 'Check the Shape',
            'title': 'Check the Shape',
            'domain': 'Recipes',
            'badges': ['shape', 'index'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">recipes.csv</code> and print the row count, the column count, and the first five index values.',
            'filename': 'recipe_shape.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;recipes.csv&quot;)  # load recipes\n'
                '\n'
                'print(&quot;Rows:&quot;, df.shape[0])       # row count\n'
                'print(&quot;Cols:&quot;, df.shape[1])       # column count\n'
                'print(df.index[:5].tolist())     # first five index values'
            ),
            'cmd': '$ python recipe_shape.py',
            'output': 'Rows: 120<br>Cols: 5<br>[0, 1, 2, 3, 4]',
            'tip': 'The default index is a simple counter starting at 0. It changes only if you set a different column as the index.',
        },
    ]


def lesson03():
    """Reading Data — CSV & Excel"""
    return [
        {
            'tab': 'Load Event Data',
            'title': 'Load Event Data',
            'domain': 'Events',
            'badges': ['read_csv()', 'head()'],
            'task': 'A conference organiser has a file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">events.csv</code>. Load it and print the first four rows to confirm the file loaded correctly.',
            'filename': 'load_events.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;events.csv&quot;)  # load event data\n'
                'print(df.head(4))               # show the first 4 rows'
            ),
            'cmd': '$ python load_events.py',
            'output': '          event       date  attendees<br>0     Keynote  2026-03-01        500<br>1    Workshop  2026-03-02        120<br>2       Panel  2026-03-02         80<br>3  Networking  2026-03-03        200',
            'tip': 'Always preview your data with head() straight after loading &#8212; it catches column misalignment and encoding issues immediately.',
        },
        {
            'tab': 'Read an Excel Sheet',
            'title': 'Read an Excel Sheet',
            'domain': 'Subscriptions',
            'badges': ['read_excel()', 'sheet_name'],
            'task': 'A subscription manager stores monthly data in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">subs.xlsx</code>. The March data is on a sheet named "Mar". Load only that sheet and print the row count.',
            'filename': 'read_subs.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_excel(&quot;subs.xlsx&quot;, sheet_name=&quot;Mar&quot;)  # load March sheet\n'
                '\n'
                'print(f&quot;Rows: {len(df)}&quot;)  # show row count'
            ),
            'cmd': '$ python read_subs.py',
            'output': 'Rows: 245',
            'tip': 'Without sheet_name, pandas loads only the first sheet. Always specify the sheet when an Excel file has multiple tabs.',
        },
        {
            'tab': 'Handle a Load Error',
            'title': 'Handle a Load Error',
            'domain': 'Expenses',
            'badges': ['try/except', 'FileNotFoundError'],
            'task': 'Write a script that tries to load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">expenses.csv</code>. If the file is missing, print a friendly error message instead of crashing.',
            'filename': 'safe_load.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'try:\n'
                '    df = pd.read_csv(&quot;expenses.csv&quot;)     # attempt load\n'
                '    print(f&quot;Loaded {len(df)} rows&quot;)       # success message\n'
                'except FileNotFoundError:\n'
                '    print(&quot;Error: expenses.csv not found&quot;)  # friendly error'
            ),
            'cmd': '$ python safe_load.py',
            'output': 'Error: expenses.csv not found',
            'tip': 'Wrapping file loads in try/except means your script logs a clear message instead of a scary traceback.',
        },
    ]


def lesson04():
    """Selecting Columns"""
    return [
        {
            'tab': 'Pick One Column',
            'title': 'Pick One Column',
            'domain': 'Library',
            'badges': ['df["col"]', 'Series'],
            'task': 'A library has a file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">catalogue.csv</code> with columns for title, author, and genre. Select only the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">title</code> column and print the first five values.',
            'filename': 'pick_title.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;catalogue.csv&quot;)  # load library data\n'
                '\n'
                'titles = df[&quot;title&quot;]   # select the title column\n'
                'print(titles.head())   # show first 5 values'
            ),
            'cmd': '$ python pick_title.py',
            'output': '0    The Great Gatsby<br>1        1984<br>2    To Kill a Mockingbird<br>Name: title, dtype: object',
            'tip': 'Selecting one column with df["col"] returns a Series &#8212; a single column of data with its own index.',
        },
        {
            'tab': 'Pick Three Columns',
            'title': 'Pick Three Columns',
            'domain': 'Movies',
            'badges': ['df[["a","b"]]', 'subset'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">movies.csv</code> and select only the title, genre, and rating columns. Print the first three rows of the smaller table.',
            'filename': 'pick_columns.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;movies.csv&quot;)  # load movie data\n'
                '\n'
                'subset = df[[&quot;title&quot;, &quot;genre&quot;, &quot;rating&quot;]]  # pick 3 columns\n'
                'print(subset.head(3))                        # show first 3 rows'
            ),
            'cmd': '$ python pick_columns.py',
            'output': '           title   genre  rating<br>0   The Matrix  Action     8.7<br>1     Frozen  Family     7.4<br>2  Inception  Sci-Fi     8.8',
            'tip': 'Double brackets df[["a","b"]] return a DataFrame. Single brackets df["a"] return a Series.',
        },
        {
            'tab': 'Rename a Column',
            'title': 'Rename a Column',
            'domain': 'Warehouse',
            'badges': ['rename()', 'columns={}'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">warehouse.csv</code>. The column <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">qty</code> is not clear enough. Rename it to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">quantity</code> and print the column names to confirm.',
            'filename': 'rename_col.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;warehouse.csv&quot;)  # load warehouse data\n'
                '\n'
                'df = df.rename(columns={&quot;qty&quot;: &quot;quantity&quot;})  # clearer name\n'
                'print(df.columns.tolist())                     # confirm the change'
            ),
            'cmd': '$ python rename_col.py',
            'output': '[&apos;product&apos;, &apos;quantity&apos;, &apos;location&apos;]',
            'tip': 'Clear column names save time later &#8212; you will type them in every filter, groupby, and merge for the rest of the analysis.',
        },
    ]


def lesson05():
    """Filtering Rows"""
    return [
        {
            'tab': 'Filter by Price',
            'title': 'Filter by Price',
            'domain': 'Groceries',
            'badges': ['boolean mask', 'comparison'],
            'task': 'A grocery shop has a file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">groceries.csv</code> with columns name and price. Filter the rows where the price is above $5 and print how many items match.',
            'filename': 'filter_price.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;groceries.csv&quot;)  # load grocery data\n'
                '\n'
                'expensive = df[df[&quot;price&quot;] &gt; 5]  # keep rows over $5\n'
                'print(f&quot;Items over $5: {len(expensive)}&quot;)  # count matches'
            ),
            'cmd': '$ python filter_price.py',
            'output': 'Items over $5: 18',
            'tip': 'The condition inside the brackets creates a True/False mask. Only rows where the mask is True are kept.',
        },
        {
            'tab': 'Two Conditions',
            'title': 'Two Conditions',
            'domain': 'Staff',
            'badges': ['&amp; operator', 'combined filter'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">staff.csv</code> with columns name, department, and salary. Find employees in the "Engineering" department who earn more than 70,000. Print the matching names.',
            'filename': 'two_filters.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;staff.csv&quot;)  # load staff data\n'
                '\n'
                'match = df[(df[&quot;department&quot;] == &quot;Engineering&quot;) &amp;  # dept filter\n'
                '           (df[&quot;salary&quot;] &gt; 70000)]                 # salary filter\n'
                'print(match[&quot;name&quot;].tolist())  # print matching names'
            ),
            'cmd': '$ python two_filters.py',
            'output': '[&apos;Alice&apos;, &apos;Carlos&apos;]',
            'tip': 'Wrap each condition in parentheses when using &amp; &#8212; without them, Python reads the expression in the wrong order.',
        },
        {
            'tab': 'Filter with a List',
            'title': 'Filter with a List',
            'domain': 'Shipments',
            'badges': ['isin()', 'list filter'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">shipments.csv</code>. Keep only rows where the status is "Delivered" or "In Transit". Print the number of matching rows.',
            'filename': 'filter_isin.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;shipments.csv&quot;)  # load shipment data\n'
                '\n'
                'keep = [&quot;Delivered&quot;, &quot;In Transit&quot;]          # statuses to keep\n'
                'result = df[df[&quot;status&quot;].isin(keep)]       # filter rows\n'
                'print(f&quot;Matching rows: {len(result)}&quot;)  # count'
            ),
            'cmd': '$ python filter_isin.py',
            'output': 'Matching rows: 64',
            'tip': 'Use isin() when you need to match several values at once &#8212; it is cleaner than chaining multiple == checks with the | operator.',
        },
    ]


def lesson06():
    """Creating Calculated Columns"""
    return [
        {
            'tab': 'Add a Tax Column',
            'title': 'Add a Tax Column',
            'domain': 'Invoices',
            'badges': ['new column', 'arithmetic'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">invoices.csv</code> with a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">subtotal</code> column. Add a new column called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">tax</code> that is 10% of the subtotal. Print the first three rows.',
            'filename': 'add_tax.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;invoices.csv&quot;)  # load invoice data\n'
                '\n'
                'df[&quot;tax&quot;] = df[&quot;subtotal&quot;] * 0.10  # 10% tax\n'
                'print(df[[&quot;subtotal&quot;, &quot;tax&quot;]].head(3))  # preview'
            ),
            'cmd': '$ python add_tax.py',
            'output': '   subtotal    tax<br>0    200.00  20.00<br>1    150.00  15.00<br>2     75.00   7.50',
            'tip': 'Pandas applies the calculation to every row at once &#8212; no loop needed, even with millions of rows.',
        },
        {
            'tab': 'Label Pass or Fail',
            'title': 'Label Pass or Fail',
            'domain': 'Students',
            'badges': ['np.where()', 'conditional'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">grades.csv</code> with a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">score</code> column. Add a column called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">result</code> that says "Pass" for scores of 50 or above and "Fail" for the rest. Print the first four rows.',
            'filename': 'pass_fail.py',
            'code': (
                'import pandas as pd   # load pandas\n'
                'import numpy as np    # for np.where\n'
                '\n'
                'df = pd.read_csv(&quot;grades.csv&quot;)  # load student scores\n'
                '\n'
                'df[&quot;result&quot;] = np.where(df[&quot;score&quot;] &gt;= 50, &quot;Pass&quot;, &quot;Fail&quot;)  # label\n'
                'print(df[[&quot;student&quot;, &quot;score&quot;, &quot;result&quot;]].head(4))'
            ),
            'cmd': '$ python pass_fail.py',
            'output': '  student  score result<br>0   Alice     72   Pass<br>1     Bob     45   Fail<br>2   Carol     88   Pass<br>3   David     33   Fail',
            'tip': 'np.where() handles simple if/else logic across an entire column. Use np.select() when you need more than two categories.',
        },
        {
            'tab': 'Drop a Column',
            'title': 'Drop a Column',
            'domain': 'Vehicles',
            'badges': ['drop()', 'axis=1'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">vehicles.csv</code>. The column <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">internal_id</code> is not needed for analysis. Drop it and print the remaining column names.',
            'filename': 'drop_col.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;vehicles.csv&quot;)  # load vehicle data\n'
                '\n'
                'df = df.drop(columns=[&quot;internal_id&quot;])  # remove column\n'
                'print(df.columns.tolist())                # confirm'
            ),
            'cmd': '$ python drop_col.py',
            'output': '[&apos;make&apos;, &apos;model&apos;, &apos;year&apos;, &apos;price&apos;]',
            'tip': 'Drop unneeded columns early &#8212; smaller DataFrames are faster to process and easier to read.',
        },
    ]


def lesson07():
    """Aggregations — Group By"""
    return [
        {
            'tab': 'Sum by Category',
            'title': 'Sum by Category',
            'domain': 'Donations',
            'badges': ['groupby()', 'sum()'],
            'task': 'A charity tracks donations in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">donations.csv</code> with columns donor, campaign, and amount. Group by campaign and print the total amount per campaign.',
            'filename': 'donation_totals.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;donations.csv&quot;)  # load donation data\n'
                '\n'
                'totals = df.groupby(&quot;campaign&quot;)[&quot;amount&quot;].sum()  # total per campaign\n'
                'print(totals)'
            ),
            'cmd': '$ python donation_totals.py',
            'output': 'campaign<br>Education     12500<br>Health        18700<br>Wildlife       9300<br>Name: amount, dtype: int64',
            'tip': 'groupby() splits the data into groups, applies the aggregation, and combines the results &#8212; all in one line.',
        },
        {
            'tab': 'Multiple Aggregations',
            'title': 'Multiple Aggregations',
            'domain': 'Tickets',
            'badges': ['agg()', 'dict'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">tickets.csv</code> with columns priority and resolution_hours. Group by priority and calculate both the mean and maximum resolution time. Print the result.',
            'filename': 'ticket_agg.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;tickets.csv&quot;)  # load support tickets\n'
                '\n'
                'stats = df.groupby(&quot;priority&quot;)[&quot;resolution_hours&quot;].agg(\n'
                '    [&quot;mean&quot;, &quot;max&quot;]  # average and worst case\n'
                ')\n'
                'print(stats.round(1))'
            ),
            'cmd': '$ python ticket_agg.py',
            'output': '          mean   max<br>priority<br>High       2.4   8.0<br>Low       12.1  48.0<br>Medium     6.3  24.0',
            'tip': 'Pass a list of function names to agg() when you need more than one statistic per group.',
        },
        {
            'tab': 'Count by Value',
            'title': 'Count by Value',
            'domain': 'Retail',
            'badges': ['value_counts()', 'frequency'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">transactions.csv</code>. Count how many transactions belong to each payment_method. Print the counts sorted from most to least common.',
            'filename': 'payment_counts.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;transactions.csv&quot;)  # load data\n'
                '\n'
                'counts = df[&quot;payment_method&quot;].value_counts()  # count each type\n'
                'print(counts)'
            ),
            'cmd': '$ python payment_counts.py',
            'output': 'payment_method<br>Card      245<br>Cash      180<br>Digital    75<br>Name: count, dtype: int64',
            'tip': 'value_counts() sorts from most to least common by default &#8212; the top item in the output is the most frequent.',
        },
    ]


def lesson08():
    """Joining Data — Merge"""
    return [
        {
            'tab': 'Merge Two Tables',
            'title': 'Merge Two Tables',
            'domain': 'Clients',
            'badges': ['pd.merge()', 'inner join'],
            'task': 'You have <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">clients.csv</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">orders.csv</code>. Both share a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">client_id</code> column. Merge them and print the first three rows to see client names next to their orders.',
            'filename': 'merge_clients.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'clients = pd.read_csv(&quot;clients.csv&quot;)   # client details\n'
                'orders = pd.read_csv(&quot;orders.csv&quot;)     # order records\n'
                '\n'
                'merged = pd.merge(clients, orders, on=&quot;client_id&quot;)  # join\n'
                'print(merged.head(3))'
            ),
            'cmd': '$ python merge_clients.py',
            'output': '   client_id     name  order_id  total<br>0        101    Alice      5001  120.0<br>1        102      Bob      5002   85.0<br>2        103    Carol      5003  210.0',
            'tip': 'An inner merge keeps only rows where the key exists in both tables &#8212; unmatched rows are silently dropped.',
        },
        {
            'tab': 'Keep All Students',
            'title': 'Keep All Students',
            'domain': 'Courses',
            'badges': ['left join', 'how="left"'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">students.csv</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">enrollments.csv</code>. Use a left join on <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">student_id</code> so every student appears, even if they have not enrolled in a course yet. Print the row count.',
            'filename': 'left_join.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'students = pd.read_csv(&quot;students.csv&quot;)        # all students\n'
                'enrollments = pd.read_csv(&quot;enrollments.csv&quot;)  # enrollments\n'
                '\n'
                'result = pd.merge(students, enrollments,\n'
                '                  on=&quot;student_id&quot;, how=&quot;left&quot;)  # keep all students\n'
                'print(f&quot;Rows: {len(result)}&quot;)'
            ),
            'cmd': '$ python left_join.py',
            'output': 'Rows: 52',
            'tip': 'A left join never drops rows from the left table. If a student has no enrolment, the course columns show NaN.',
        },
        {
            'tab': 'Join on Two Keys',
            'title': 'Join on Two Keys',
            'domain': 'Payroll',
            'badges': ['on=[a,b]', 'composite key'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">hours.csv</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">rates.csv</code>. Both have <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">dept</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">month</code> columns. Merge on both keys and print the first three rows.',
            'filename': 'multi_key.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'hours = pd.read_csv(&quot;hours.csv&quot;)  # hours worked\n'
                'rates = pd.read_csv(&quot;rates.csv&quot;)  # pay rates\n'
                '\n'
                'merged = pd.merge(hours, rates, on=[&quot;dept&quot;, &quot;month&quot;])  # two keys\n'
                'print(merged.head(3))'
            ),
            'cmd': '$ python multi_key.py',
            'output': '         dept    month  hours  rate<br>0  Marketing  January    160    35<br>1  Marketing  February   152    35<br>2    Finance  January    168    42',
            'tip': 'Use a list of column names in the on= parameter when a single column does not uniquely identify each row.',
        },
    ]


def lesson09():
    """Handling Missing Data"""
    return [
        {
            'tab': 'Find Missing Values',
            'title': 'Find Missing Values',
            'domain': 'Feedback',
            'badges': ['isnull()', 'sum()'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">feedback.csv</code>. Some respondents left fields blank. Print the number of missing values in each column.',
            'filename': 'find_nulls.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;feedback.csv&quot;)  # load feedback data\n'
                '\n'
                'missing = df.isnull().sum()  # count nulls per column\n'
                'print(missing)'
            ),
            'cmd': '$ python find_nulls.py',
            'output': 'name        0<br>email       3<br>comment    12<br>rating      5<br>dtype: int64',
            'tip': 'Run isnull().sum() first to see which columns have gaps &#8212; then decide whether to drop or fill.',
        },
        {
            'tab': 'Drop Incomplete Rows',
            'title': 'Drop Incomplete Rows',
            'domain': 'Weather',
            'badges': ['dropna()', 'subset'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">weather.csv</code>. Drop any rows where the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">temperature</code> reading is missing. Print the row count before and after.',
            'filename': 'drop_missing.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;weather.csv&quot;)  # load weather data\n'
                'print(f&quot;Before: {len(df)} rows&quot;)  # original count\n'
                '\n'
                'df = df.dropna(subset=[&quot;temperature&quot;])  # drop rows with no temp\n'
                'print(f&quot;After: {len(df)} rows&quot;)           # new count'
            ),
            'cmd': '$ python drop_missing.py',
            'output': 'Before: 365 rows<br>After: 358 rows',
            'tip': 'Use the subset parameter to drop rows only when a specific important column is blank &#8212; other missing values are preserved.',
        },
        {
            'tab': 'Fill the Gaps',
            'title': 'Fill the Gaps',
            'domain': 'Stock',
            'badges': ['fillna()', 'default value'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">stock.csv</code>. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">quantity</code> column has some blanks. Fill them with 0 and print the first five rows.',
            'filename': 'fill_nulls.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;stock.csv&quot;)  # load stock data\n'
                '\n'
                'df[&quot;quantity&quot;] = df[&quot;quantity&quot;].fillna(0)  # replace NaN with 0\n'
                'print(df.head())'
            ),
            'cmd': '$ python fill_nulls.py',
            'output': '    product  quantity<br>0   Widget      12.0<br>1   Gadget       0.0<br>2   Gizmo       25.0<br>3   Doohickey    0.0<br>4   Thingamajig  8.0',
            'tip': 'fillna(0) is safe for quantities and counts. For prices or measurements, the column median is often a better default.',
        },
    ]


def lesson10():
    """Exporting Data"""
    return [
        {
            'tab': 'Save to CSV',
            'title': 'Save to CSV',
            'domain': 'Grades',
            'badges': ['to_csv()', 'index=False'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">grades.csv</code>, filter for students who scored above 80, and save the result to a new file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">top_students.csv</code>.',
            'filename': 'save_csv.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;grades.csv&quot;)            # load grade data\n'
                'top = df[df[&quot;score&quot;] &gt; 80]                # filter top students\n'
                '\n'
                'top.to_csv(&quot;top_students.csv&quot;, index=False)  # save without index\n'
                'print(f&quot;Saved {len(top)} rows&quot;)'
            ),
            'cmd': '$ python save_csv.py',
            'output': 'Saved 14 rows',
            'tip': 'Always set index=False when saving &#8212; without it, pandas adds an extra numbered column that clutters the output file.',
        },
        {
            'tab': 'Export to Excel',
            'title': 'Export to Excel',
            'domain': 'Projects',
            'badges': ['to_excel()', 'sheet_name'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">projects.csv</code> and save it to an Excel file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">projects.xlsx</code> on a sheet named "Active".',
            'filename': 'save_excel.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;projects.csv&quot;)  # load project data\n'
                '\n'
                'df.to_excel(&quot;projects.xlsx&quot;, sheet_name=&quot;Active&quot;, index=False)\n'
                'print(&quot;Saved to projects.xlsx&quot;)'
            ),
            'cmd': '$ python save_excel.py',
            'output': 'Saved to projects.xlsx',
            'tip': 'Give the sheet a meaningful name &#8212; stakeholders who open the Excel file will see it straight away.',
        },
        {
            'tab': 'Export a Subset',
            'title': 'Export a Subset',
            'domain': 'Suppliers',
            'badges': ['select + save', 'workflow'],
            'task': 'Load <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">suppliers.csv</code>. Select only the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">name</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">email</code> columns and save them to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">contacts.csv</code>.',
            'filename': 'export_subset.py',
            'code': (
                'import pandas as pd  # load pandas\n'
                '\n'
                'df = pd.read_csv(&quot;suppliers.csv&quot;)          # load supplier data\n'
                'contacts = df[[&quot;name&quot;, &quot;email&quot;]]           # pick 2 columns\n'
                '\n'
                'contacts.to_csv(&quot;contacts.csv&quot;, index=False)  # save subset\n'
                'print(f&quot;Exported {len(contacts)} contacts&quot;)'
            ),
            'cmd': '$ python export_subset.py',
            'output': 'Exported 38 contacts',
            'tip': 'Select the columns you need before saving &#8212; this keeps exported files small and avoids sharing unnecessary data.',
        },
    ]


REGISTRY = {
    "lesson01_introduction_to_pandas.html": lesson01,
    "lesson02_dataframes_explained.html": lesson02,
    "lesson03_reading_data_csv_excel.html": lesson03,
    "lesson04_selecting_columns.html": lesson04,
    "lesson05_filtering_rows.html": lesson05,
    "lesson06_creating_calculated_columns.html": lesson06,
    "lesson07_aggregations_group_by.html": lesson07,
    "lesson08_joining_data_merge.html": lesson08,
    "lesson09_handling_missing_data.html": lesson09,
    "lesson10_exporting_data.html": lesson10,
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
