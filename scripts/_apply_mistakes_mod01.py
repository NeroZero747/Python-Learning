"""
Rewrite <section id="mistakes"> for all 10 lessons in
track_02 / mod_01_data_analysis_with_pandas.

Uses the prompt spec from lesson-common-mistakes.prompt.md:
- Descriptive tab labels (never "Mistake N")
- Explanation paragraph above the split panel
- Style B-lite code blocks (px-4 py-3 on <pre>, no header)
- Wrong — label / Correct — label
- Amber tip on every card
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_02_data_analytics" / "mod_01_data_analysis_with_pandas"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

# ── Content definitions ────────────────────────────────────────────────

LESSONS = {
    # ── Lesson 01: Introduction to Pandas ──
    "lesson01_introduction_to_pandas.html": {
        "topic": "Pandas basics",
        "mistakes": [
            {
                "tab": "Missing Import",
                "title": "Using Pandas Without Importing It",
                "subtitle": "Python raises a NameError because it does not know what pd means.",
                "explanation": 'Python cannot find <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd</code> unless you import Pandas first. Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_csv()</code> without the import line raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">NameError</code>. Add <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">import pandas as pd</code> at the top of your file.',
                "wrong_label": "no import",
                "wrong_code": 'df = pd.read_csv("sales.csv")\nprint(df.head())',
                "correct_label": "import first",
                "correct_code": 'import pandas as pd              # load the library\ndf = pd.read_csv("sales.csv")    # now pd is recognised\nprint(df.head())                  # show first five rows',
                "tip": "Think of importing as opening a toolbox — you cannot use the tools until you open the lid.",
            },
            {
                "tab": "Wrong Alias",
                "title": "Importing Without the Standard Alias",
                "subtitle": "Code that references pd will fail if you imported pandas under a different name.",
                "explanation": 'The community standard is <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">import pandas as pd</code>. If you write <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">import pandas</code> alone, every call must spell out <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pandas.read_csv()</code> instead of <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_csv()</code>.',
                "wrong_label": "no alias",
                "wrong_code": 'import pandas\ndf = pandas.read_csv("sales.csv")',
                "correct_label": "use pd alias",
                "correct_code": 'import pandas as pd              # standard alias\ndf = pd.read_csv("sales.csv")    # shorter and universal',
                "tip": "Every tutorial, blog post, and colleague uses <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pd</code>. Matching the convention makes your code instantly readable to others.",
            },
            {
                "tab": "List-Style Index",
                "title": "Accessing Columns With a Numeric Index",
                "subtitle": "DataFrames use column names, not positional numbers like a list.",
                "explanation": 'Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df[0]</code> raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">KeyError</code> because Pandas looks for a column named <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">0</code>. Use the column\'s actual label inside quotes.',
                "wrong_label": "numeric index",
                "wrong_code": "first_column = df[0]",
                "correct_label": "column name",
                "correct_code": 'first_column = df["Name"]   # use the column label',
                "tip": "DataFrames are labelled shelves, not numbered slots. Always reach for the label, not the position.",
            },
        ],
    },

    # ── Lesson 02: DataFrames Explained ──
    "lesson02_dataframes_explained.html": {
        "topic": "DataFrames",
        "mistakes": [
            {
                "tab": "Mismatched Lengths",
                "title": "Creating a DataFrame With Unequal Lists",
                "subtitle": "Pandas raises a ValueError when the lists have different lengths.",
                "explanation": 'Each key in the dictionary must map to a list of the same length. A mismatch like three names and two ages triggers <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ValueError: All arrays must be of the same length</code>.',
                "wrong_label": "unequal lists",
                "wrong_code": 'data = {"Name": ["Alice", "Bob", "Carla"],\n        "Age": [30, 28]}       # only 2 items\ndf = pd.DataFrame(data)',
                "correct_label": "equal lists",
                "correct_code": 'data = {"Name": ["Alice", "Bob", "Carla"],  # 3 items\n        "Age": [30, 28, 35]}               # 3 items\ndf = pd.DataFrame(data)                     # works',
                "tip": "Count your items before building the dictionary. Every column must have the same number of values, like rows in a spreadsheet.",
            },
            {
                "tab": "Index vs Column",
                "title": "Confusing the Index With a Column",
                "subtitle": "The index is a row label, not a data column you can select with brackets.",
                "explanation": 'The index appears on the left of every printout, but <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["index"]</code> looks for a column named index — not the row labels. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.index</code> to access row labels.',
                "wrong_label": "bracket lookup",
                "wrong_code": 'row_labels = df["index"]    # KeyError',
                "correct_label": "use .index",
                "correct_code": 'row_labels = df.index       # access the row labels\nprint(row_labels)            # RangeIndex(start=0, ...)',
                "tip": "The index is part of the frame's structure, not its data. Access it through the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.index</code> attribute, not the bracket operator.",
            },
            {
                "tab": "Wrong dtype",
                "title": "Assuming Column Types Without Checking",
                "subtitle": "A column that looks numeric may be stored as text, causing silent calculation errors.",
                "explanation": 'CSV files often load numbers as strings. Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.sum()</code> on a text column concatenates strings instead of adding numbers. Always check types with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.dtypes</code> first.',
                "wrong_label": "skip type check",
                "wrong_code": 'total = df["Price"].sum()   # may concatenate strings\nprint(total)                 # &quot;1020&quot; instead of 30',
                "correct_label": "verify dtypes",
                "correct_code": 'print(df.dtypes)                        # check types first\ndf["Price"] = pd.to_numeric(df["Price"]) # convert to number\ntotal = df["Price"].sum()                # now adds correctly',
                "tip": "Run <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">df.dtypes</code> right after loading data. It takes one second and prevents hours of debugging wrong calculations.",
            },
        ],
    },

    # ── Lesson 03: Reading Data (CSV & Excel) ──
    "lesson03_reading_data_csv_excel.html": {
        "topic": "reading CSV and Excel files",
        "mistakes": [
            {
                "tab": "Wrong File Path",
                "title": "Passing an Incorrect Path to read_csv()",
                "subtitle": "Python raises a FileNotFoundError because the file cannot be located.",
                "explanation": 'If the path does not match the actual file location, Pandas raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">FileNotFoundError</code>. Double-check the folder, filename, and extension before running.',
                "wrong_label": "wrong path",
                "wrong_code": 'df = pd.read_csv("data/Sale.csv")   # typo in name',
                "correct_label": "correct path",
                "correct_code": 'df = pd.read_csv("data/sales.csv")  # exact filename match\nprint(df.head())                     # confirm it loaded',
                "tip": "Copy the filename directly from your file explorer. A single wrong letter — capital or lowercase — is enough to trigger the error.",
            },
            {
                "tab": "Wrong Function",
                "title": "Using read_csv() to Open an Excel File",
                "subtitle": "Pandas cannot parse .xlsx bytes as CSV text and raises a ParserError.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read_csv()</code> expects plain text delimited by commas. Passing an <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.xlsx</code> file produces garbled output or a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ParserError</code>. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read_excel()</code> for Excel files.',
                "wrong_label": "read_csv for xlsx",
                "wrong_code": 'df = pd.read_csv("report.xlsx")     # wrong function',
                "correct_label": "use read_excel",
                "correct_code": 'df = pd.read_excel("report.xlsx")   # matches the format\nprint(df.shape)                      # confirm rows/columns',
                "tip": "Match the function to the file extension: <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.csv</code> → <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">read_csv()</code>, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.xlsx</code> → <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">read_excel()</code>.",
            },
            {
                "tab": "Encoding Error",
                "title": "Loading a CSV With the Wrong Encoding",
                "subtitle": "Special characters appear garbled or Python raises a UnicodeDecodeError.",
                "explanation": 'Files created on different systems may use encodings other than UTF-8. When characters look broken, add the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">encoding</code> parameter to match the file\'s actual encoding.',
                "wrong_label": "default encoding",
                "wrong_code": 'df = pd.read_csv("clients.csv")     # garbled names',
                "correct_label": "specify encoding",
                "correct_code": 'df = pd.read_csv("clients.csv",\n                  encoding="latin-1") # match source\nprint(df.head())                      # names display correctly',
                "tip": "If names or addresses look like <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">Ã©</code> instead of <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">é</code>, try <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">encoding=\"latin-1\"</code> or <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">encoding=\"cp1252\"</code>.",
            },
        ],
    },

    # ── Lesson 04: Selecting Columns ──
    "lesson04_selecting_columns.html": {
        "topic": "selecting columns",
        "mistakes": [
            {
                "tab": "Single Brackets",
                "title": "Using Single Brackets for Multiple Columns",
                "subtitle": "Pandas raises a KeyError because it treats the tuple as one column name.",
                "explanation": 'Selecting multiple columns requires double brackets: <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df[["A", "B"]]</code>. Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["A", "B"]</code> with single brackets makes Pandas look for a single column named <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">("A", "B")</code>.',
                "wrong_label": "single brackets",
                "wrong_code": 'subset = df["Name", "Age"]   # KeyError',
                "correct_label": "double brackets",
                "correct_code": 'subset = df[["Name", "Age"]]  # pass a list of names\nprint(subset.head())           # shows both columns',
                "tip": "The outer brackets select from the DataFrame. The inner brackets create the list of column names. Two layers, two jobs.",
            },
            {
                "tab": "Misspelt Name",
                "title": "Misspelling a Column Name",
                "subtitle": "Pandas raises a KeyError because the exact string does not exist in the columns.",
                "explanation": 'Column names are case-sensitive strings. <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["name"]</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["Name"]</code> are different lookups. Print <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.columns.tolist()</code> to see the exact names.',
                "wrong_label": "wrong spelling",
                "wrong_code": 'ages = df["age"]              # KeyError — wrong case',
                "correct_label": "exact name",
                "correct_code": 'print(df.columns.tolist())    # check exact names first\nages = df["Age"]               # matches the real column',
                "tip": "Run <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">df.columns.tolist()</code> once after loading. Copy-paste the column name from the output — never retype it from memory.",
            },
            {
                "tab": "Dot Notation Trap",
                "title": "Using Dot Notation With Spaces or Special Characters",
                "subtitle": "Python raises a SyntaxError or AttributeError when the column name is not a valid identifier.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.First Name</code> fails because Python sees a space as a statement break. Bracket notation works with any column name. Use dots only for simple, space-free names.',
                "wrong_label": "dot with space",
                "wrong_code": 'name = df.First Name     # SyntaxError',
                "correct_label": "bracket notation",
                "correct_code": 'name = df["First Name"]  # works with any name\nprint(name.head())        # displays the column',
                "tip": "Bracket notation always works. Dot notation is a shortcut that breaks the moment a column name has a space, hyphen, or number at the start.",
            },
        ],
    },

    # ── Lesson 05: Filtering Rows ──
    "lesson05_filtering_rows.html": {
        "topic": "filtering rows",
        "mistakes": [
            {
                "tab": "Missing Parentheses",
                "title": "Combining Conditions Without Parentheses",
                "subtitle": "Python raises a ValueError because the & operator binds before the comparison.",
                "explanation": 'The <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">&amp;</code> operator has higher precedence than <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">==</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">&gt;</code>. Without parentheses, Python evaluates <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["Age"] &amp; df["City"]</code> first, which is meaningless. Wrap each condition in parentheses.',
                "wrong_label": "no parentheses",
                "wrong_code": 'filtered_rows = df[df["Age"] &gt; 30 &amp; df["City"] == "London"]',
                "correct_label": "add parentheses",
                "correct_code": 'mask = (df["Age"] &gt; 30) &amp; (df["City"] == "London")  # each wrapped\nfiltered_rows = df[mask]                               # apply filter\nprint(filtered_rows.shape)                             # check count',
                "tip": "Always wrap each individual condition in its own parentheses before joining them with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">&amp;</code> or <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">|</code>.",
            },
            {
                "tab": 'Using "and"',
                "title": "Writing and Instead of the & Operator",
                "subtitle": "Pandas raises a ValueError because and cannot evaluate a Series of booleans.",
                "explanation": 'Python\'s <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">and</code> keyword works on single True/False values. Pandas filters produce a Series of booleans, which requires the element-wise <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">&amp;</code> operator.',
                "wrong_label": "and keyword",
                "wrong_code": 'filtered_rows = df[(df["Age"] &gt; 30) and (df["City"] == "London")]',
                "correct_label": "use &amp;",
                "correct_code": 'filtered_rows = df[(df["Age"] &gt; 30) &amp; (df["City"] == "London")]  # &amp; works\nprint(filtered_rows)                                               # filtered rows',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">&amp;</code> for AND and <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">|</code> for OR when filtering DataFrames. The English words <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">and</code> / <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">or</code> only work on single values.",
            },
            {
                "tab": "Single Equals",
                "title": "Using = Instead of == in a Condition",
                "subtitle": "Python raises a SyntaxError because = is assignment, not comparison.",
                "explanation": 'A single <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">=</code> assigns a value. A double <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">==</code> compares two values. Filters always need <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">==</code>.',
                "wrong_label": "single =",
                "wrong_code": 'london_rows = df[df["City"] = "London"]    # SyntaxError',
                "correct_label": "double ==",
                "correct_code": 'london_rows = df[df["City"] == "London"]   # comparison, not assignment\nprint(london_rows.head())                   # matching rows',
                "tip": "Read <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">=</code> as \"store this value\" and <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">==</code> as \"is this equal?\". Filters always ask a question, so they always use the double form.",
            },
        ],
    },

    # ── Lesson 06: Creating Calculated Columns ──
    "lesson06_creating_calculated_columns.html": {
        "topic": "calculated columns",
        "mistakes": [
            {
                "tab": "Misspelt Column",
                "title": "Referencing a Column Name That Does Not Exist",
                "subtitle": "Pandas raises a KeyError because the string does not match any column.",
                "explanation": 'A single typo in a column name causes a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">KeyError</code>. The name must match exactly — including capitalisation. Check with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.columns.tolist()</code> before writing formulas.',
                "wrong_label": "typo in name",
                "wrong_code": 'df["Total"] = df["Prce"] * df["Qty"]  # KeyError',
                "correct_label": "exact name",
                "correct_code": 'print(df.columns.tolist())               # verify names\ndf["Total"] = df["Price"] * df["Qty"]   # correct spelling',
                "tip": "Copy-paste column names from <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">df.columns.tolist()</code> output. Your fingers will misspell it; your clipboard will not.",
            },
            {
                "tab": "String vs Number",
                "title": "Adding a Number to a Text Column",
                "subtitle": "Python raises a TypeError or silently concatenates strings instead of adding.",
                "explanation": 'If a column holds text, the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">+</code> operator concatenates instead of adding. Convert the column to a number first with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.to_numeric()</code>.',
                "wrong_label": "add to text",
                "wrong_code": 'df["Total"] = df["Price"] + df["Tax"]    # concatenates strings\n# result: &quot;1005&quot; instead of 15',
                "correct_label": "convert first",
                "correct_code": 'df["Price"] = pd.to_numeric(df["Price"])  # ensure numeric\ndf["Tax"] = pd.to_numeric(df["Tax"])      # ensure numeric\ndf["Total"] = df["Price"] + df["Tax"]      # now adds correctly',
                "tip": "Run <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">df.dtypes</code> before any arithmetic. If it says <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">object</code>, the column is text and needs conversion.",
            },
            {
                "tab": "Overwriting Data",
                "title": "Overwriting an Existing Column by Accident",
                "subtitle": "The original data is permanently replaced and cannot be recovered.",
                "explanation": 'Assigning to an existing column name overwrites it. If you write <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["Price"] = df["Price"] * 1.1</code>, the original prices are gone. Store the result in a new column instead.',
                "wrong_label": "overwrite original",
                "wrong_code": 'df["Price"] = df["Price"] * 1.1    # original prices lost',
                "correct_label": "new column",
                "correct_code": 'df["Price_With_Tax"] = df["Price"] * 1.1  # original untouched\nprint(df[["Price", "Price_With_Tax"]])      # both columns visible',
                "tip": "Give calculated results a new column name. It is like saving a document with \"Save As\" instead of overwriting the original file.",
            },
        ],
    },

    # ── Lesson 07: Aggregations & Group By ──
    "lesson07_aggregations_group_by.html": {
        "topic": "aggregations and GroupBy",
        "mistakes": [
            {
                "tab": "No Aggregation",
                "title": "Printing a GroupBy Object Without Aggregating",
                "subtitle": "Python prints a memory address instead of the grouped data.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.groupby("Region")</code> creates a lazy GroupBy object, not a table. You must call an aggregation like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.sum()</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.mean()</code> to produce actual results.',
                "wrong_label": "no aggregation",
                "wrong_code": 'result = df.groupby("Region")\nprint(result)   # &lt;DataFrameGroupBy object&gt;',
                "correct_label": "add .sum()",
                "correct_code": 'result = df.groupby("Region")["Sales"].sum()  # aggregate\nprint(result)                                  # numbers per region',
                "tip": "Think of <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">groupby()</code> as sorting items into labelled bins. The aggregation is the step where you actually count or total what is inside each bin.",
            },
            {
                "tab": "Sum on Text",
                "title": "Aggregating a Non-Numeric Column",
                "subtitle": "Calling .sum() on text silently concatenates strings instead of adding numbers.",
                "explanation": 'If you run <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.sum()</code> on a column that holds text, Pandas joins the strings together. Select only the numeric column before aggregating.',
                "wrong_label": "all columns",
                "wrong_code": 'total = df.groupby("Region").sum()\n# Name column: &quot;AliceBobCarla&quot;',
                "correct_label": "select numeric",
                "correct_code": 'total = df.groupby("Region")["Sales"].sum()  # numeric only\nprint(total)                                   # clean numbers',
                "tip": "Always name the column you want between the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">groupby()</code> and the aggregation. It prevents surprise concatenation of text columns.",
            },
            {
                "tab": "Lost Columns",
                "title": "Expecting All Columns After GroupBy",
                "subtitle": "GroupBy returns only the grouping key and the aggregated column.",
                "explanation": 'After <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">groupby().sum()</code>, the result has fewer columns than the original. The grouped column becomes the index. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.reset_index()</code> to turn it back into a regular column.',
                "wrong_label": "missing columns",
                "wrong_code": 'summary = df.groupby("Region")["Sales"].sum()\nprint(summary["Region"])   # KeyError — it is the index',
                "correct_label": "reset index",
                "correct_code": 'summary = df.groupby("Region")["Sales"].sum()  # grouped\nsummary = summary.reset_index()                  # Region is a column\nprint(summary.columns.tolist())                   # [Region, Sales]',
                "tip": "If you plan to keep working with the result, add <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.reset_index()</code> immediately. It turns the grouped key back into a normal column you can select and filter.",
            },
        ],
    },

    # ── Lesson 08: Joining Data (Merge) ──
    "lesson08_joining_data_merge.html": {
        "topic": "merging DataFrames",
        "mistakes": [
            {
                "tab": "Wrong Join Key",
                "title": "Merging on a Column That Does Not Match",
                "subtitle": "The result contains zero rows or many NaN values because no keys aligned.",
                "explanation": 'If the join key has different names in each DataFrame, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">merge()</code> finds no matches. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">left_on</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">right_on</code> when the column names differ.',
                "wrong_label": "no match found",
                "wrong_code": 'merged = orders.merge(clients, on="ID")\n# KeyError — orders has "CustomerID", not "ID"',
                "correct_label": "specify both keys",
                "correct_code": 'merged = orders.merge(clients,\n                      left_on="CustomerID",   # left DataFrame\n                      right_on="ID")           # right DataFrame\nprint(merged.shape)                             # confirm match count',
                "tip": "Print the columns of both DataFrames before merging. If the names differ, spell each one out with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">left_on</code> and <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">right_on</code>.",
            },
            {
                "tab": "Wrong Join Type",
                "title": "Using the Default Inner Join When You Need All Rows",
                "subtitle": "Rows without a match are silently dropped from the result.",
                "explanation": 'The default <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">how="inner"</code> keeps only rows that match in both DataFrames. If you need all rows from the left table, use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">how="left"</code>.',
                "wrong_label": "inner drops rows",
                "wrong_code": 'merged = orders.merge(clients, on="CustomerID")\n# rows with no matching client are gone',
                "correct_label": "use left join",
                "correct_code": 'merged = orders.merge(clients,\n                      on="CustomerID",\n                      how="left")       # keep all orders\nprint(merged.shape)                      # same row count as orders',
                "tip": "Ask yourself: \"Do I need every row from my main table, even if there is no match?\" If yes, set <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">how=\"left\"</code>.",
            },
            {
                "tab": "Duplicate Rows",
                "title": "Getting Unexpected Duplicate Rows After Merge",
                "subtitle": "A one-to-many relationship multiplies rows in the result.",
                "explanation": 'If the right table has multiple rows per key, each left row is duplicated for every match. Check for duplicates in the join key with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.duplicated()</code> before merging.',
                "wrong_label": "duplicates appear",
                "wrong_code": '# clients has 2 rows for CustomerID 101\nmerged = orders.merge(clients, on="CustomerID")\n# order row is now duplicated',
                "correct_label": "check first",
                "correct_code": '# verify no duplicates in the join key\ndupes = clients["CustomerID"].duplicated().sum()  # count dupes\nprint(f"Duplicates: {dupes}")                      # should be 0\nmerged = orders.merge(clients, on="CustomerID")    # safe merge',
                "tip": "Always check <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">df[\"key\"].duplicated().sum()</code> on the right table before merging. Unexpected duplicates are the number-one cause of inflated row counts.",
            },
        ],
    },

    # ── Lesson 09: Handling Missing Data ──
    "lesson09_handling_missing_data.html": {
        "topic": "missing data",
        "mistakes": [
            {
                "tab": "Using == None",
                "title": "Comparing to None With the == Operator",
                "subtitle": "The comparison always returns False because NaN is not equal to anything, including itself.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">NaN == NaN</code> returns <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">False</code> in Python. Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df["Age"] == None</code> finds nothing. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.isnull()</code> instead.',
                "wrong_label": "== None",
                "wrong_code": 'missing = df[df["Age"] == None]   # finds nothing\nprint(len(missing))                # 0 — even if NaNs exist',
                "correct_label": "use .isnull()",
                "correct_code": 'missing = df[df["Age"].isnull()]  # detects NaN correctly\nprint(len(missing))                # actual count of blanks',
                "tip": "NaN is a special value that is not equal to anything — not even itself. Always use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.isnull()</code> or <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.isna()</code> to find missing values.",
            },
            {
                "tab": "Dropping Too Much",
                "title": "Using dropna() Without Specifying a Column",
                "subtitle": "Rows are dropped even if only one irrelevant column has a missing value.",
                "explanation": 'Bare <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.dropna()</code> drops every row that has a blank in any column. If only one column matters, pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">subset=["column"]</code> to keep the rest.',
                "wrong_label": "drop all blanks",
                "wrong_code": 'clean = df.dropna()       # drops rows with ANY blank\nprint(clean.shape)         # far fewer rows than expected',
                "correct_label": "target one column",
                "correct_code": 'clean = df.dropna(subset=["Age"])  # only drop if Age is blank\nprint(clean.shape)                  # keeps most of the data',
                "tip": "Think of <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">dropna()</code> without a subset as throwing away an entire form because one optional field is blank. Target the column that actually matters.",
            },
            {
                "tab": "fillna() Not Saved",
                "title": "Calling fillna() Without Saving the Result",
                "subtitle": "The original DataFrame still contains NaN because fillna() returns a new copy.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">fillna()</code> does not change the DataFrame in place by default. Assign the result back to the column or pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">inplace=True</code>.',
                "wrong_label": "result discarded",
                "wrong_code": 'df["Age"].fillna(0)      # returns a copy — original unchanged\nprint(df["Age"].isnull().sum())   # still has NaN',
                "correct_label": "assign back",
                "correct_code": 'df["Age"] = df["Age"].fillna(0)   # save the filled version\nprint(df["Age"].isnull().sum())    # 0 — no more blanks',
                "tip": "Most Pandas methods return a new object. If you do not assign the result, the change is lost — like editing a document without pressing Save.",
            },
        ],
    },

    # ── Lesson 10: Exporting Data ──
    "lesson10_exporting_data.html": {
        "topic": "exporting data",
        "mistakes": [
            {
                "tab": "Extra Index Column",
                "title": "Exporting With an Unwanted Index Column",
                "subtitle": "The output file contains a nameless extra column of row numbers.",
                "explanation": 'By default, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_csv()</code> writes the DataFrame index as the first column. Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">index=False</code> to exclude it.',
                "wrong_label": "index included",
                "wrong_code": 'df.to_csv("output.csv")   # adds 0, 1, 2… as first column',
                "correct_label": "no index",
                "correct_code": 'df.to_csv("output.csv", index=False)  # clean output\nprint("Saved without index column")    # confirm',
                "tip": "Unless your index carries meaning (like dates), always add <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">index=False</code>. Recipients of the file rarely want a mystery column of numbers.",
            },
            {
                "tab": "Silent Overwrite",
                "title": "Overwriting an Existing File Without Warning",
                "subtitle": "to_csv() silently replaces the old file with no confirmation prompt.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_csv()</code> overwrites the target file instantly. There is no undo. Check if the file exists before writing, or include a date in the filename.',
                "wrong_label": "overwrites old file",
                "wrong_code": 'df.to_csv("report.csv", index=False)  # old report is gone',
                "correct_label": "timestamped name",
                "correct_code": 'from datetime import date                        # date helper\nfilename = f"report_{date.today()}.csv"           # unique name\ndf.to_csv(filename, index=False)                   # safe export\nprint(f"Saved to {filename}")                      # confirm path',
                "tip": "Adding today's date to the filename is like version-numbering a document. You can always go back to yesterday's export if something goes wrong.",
            },
            {
                "tab": "Wrong Extension",
                "title": "Using to_csv() When You Need an Excel File",
                "subtitle": "The recipient cannot open the .csv properly in Excel with formatting intact.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_csv()</code> creates plain text. If your recipient expects an <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.xlsx</code> file with multiple sheets or formatting, use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_excel()</code> instead.',
                "wrong_label": "csv for Excel user",
                "wrong_code": 'df.to_csv("report.xlsx", index=False)  # not real Excel format',
                "correct_label": "use to_excel",
                "correct_code": 'df.to_excel("report.xlsx",\n            index=False,\n            sheet_name="Sales")  # proper Excel file\nprint("Excel file saved")        # confirm',
                "tip": "Match the function to your audience: <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">to_csv()</code> for data pipelines, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">to_excel()</code> for colleagues who live in Excel.",
            },
        ],
    },
}


# ── HTML builders ──────────────────────────────────────────────────────

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
    # Tab pills
    pills = "\n".join(
        build_tab_pill(i, mk["tab"], i == 0)
        for i, mk in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{pills}\n</div>'

    # Panels
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


# ── Apply to files ─────────────────────────────────────────────────────

def main():
    updated = 0
    for filename, content in LESSONS.items():
        path = MOD / filename
        if not path.exists():
            print(f"  ❌ {filename} — file not found")
            continue

        html = path.read_text(encoding="utf-8")

        new_section = build_section(content["topic"], content["mistakes"])

        new_html, count = SECTION_RE.subn(new_section, html)
        if count == 0:
            print(f"  ⚠️  {filename} — <section id=\"mistakes\"> not found")
            continue

        path.write_text(new_html, encoding="utf-8")
        print(f"  ✅ {filename}")
        updated += 1

    print(f"\n  Done: {updated}/{len(LESSONS)} files updated.")


if __name__ == "__main__":
    main()
