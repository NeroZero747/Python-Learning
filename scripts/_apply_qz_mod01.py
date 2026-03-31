"""Rewrite #knowledge-check for every lesson in track_02 / mod_01."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_01_data_analysis_with_pandas")
SECTION_RE = re.compile(
    r'(<section id="knowledge-check"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── builder helpers ──────────────────────────────────────────────

def build_pill_tabs():
    tabs = []
    for i in range(4):
        n = i + 1
        if i == 0:
            cls = ('qz-step qz-step-active flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
                   'text-white shadow-lg shadow-pink-200/50 transition-all duration-250')
        else:
            cls = ('qz-step flex items-center gap-2 px-4 py-2 '
                   'rounded-full bg-gray-800 text-gray-400 transition-all duration-250')
        tabs.append(
            f'<button onclick="switchQzTab({i})" class="{cls}" role="tab">'
            f'<span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>'
            f'<span class="qz-step-label text-xs font-bold">Question {n}</span>'
            f'</button>'
        )
    return '<div class="flex items-center gap-2 flex-wrap" role="tablist">\n' + \
           '\n'.join(tabs) + '\n</div>'


def build_panel(idx, statement, answer_is_true):
    qid = f"quiz-q{idx}"
    watermark = f"Q{idx+1}"
    hidden = ' hidden' if idx > 0 else ''
    true_bool = 'true' if answer_is_true else 'false'
    false_bool = 'false' if answer_is_true else 'true'
    return f'''<div class="qz-panel qz-panel-anim{hidden}" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{watermark}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">True or False</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="{qid}">
        <p class="text-sm font-semibold text-gray-800 mb-4">{statement}</p>
        <div class="flex gap-3">
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, {true_bool})">
            <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, {false_bool})">
            <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
          </button>
        </div>
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>'''


def build_section(questions):
    """questions = [(statement, answer_is_true), ...] — exactly 4."""
    pills = build_pill_tabs()
    panels = '\n'.join(build_panel(i, q[0], q[1]) for i, q in enumerate(questions))
    body = f'''{pills}
{panels}'''
    return body


def make_section_html(questions):
    body = build_section(questions)
    return (
        '<section id="knowledge-check">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:brain"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Knowledge Check</h2>\n'
        '        <p class="text-sm text-gray-400 leading-snug mt-0.5">Test your understanding before moving on</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-6">\n'
        f'{body}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── question data per lesson ─────────────────────────────────────

def lesson01_questions():
    return [
        ("Pandas is a Python library specifically designed for working with structured data like tables, spreadsheets, and databases.", True),
        ("Pandas is only useful for small datasets &#8212; for anything over a few hundred rows, you need a dedicated database.", False),
        ("A DataFrame organises data into labelled rows and columns, similar to an Excel spreadsheet or a database table.", True),
        ("Pandas replaces SQL entirely &#8212; once you learn pandas, you no longer need to write SQL queries.", False),
    ]

def lesson02_questions():
    return [
        ("A DataFrame is a two-dimensional data structure where every column can hold a different data type, such as text, integers, or dates.", True),
        ("The index of a DataFrame is always a sequence of numbers starting from 1, and it cannot be changed after creation.", False),
        ("You can create a DataFrame by passing a Python dictionary to pd.DataFrame(), where each key becomes a column name.", True),
        ("Calling df.shape returns a list of all column names in the DataFrame.", False),
    ]

def lesson03_questions():
    return [
        ("The pd.read_csv() function loads a CSV file into a DataFrame with a single line of code.", True),
        ("pd.read_csv() can open both CSV and Excel files &#8212; there is no separate function for Excel.", False),
        ("After loading a file, calling df.head() shows you the first five rows so you can quickly check whether the data loaded correctly.", True),
        ("If a CSV file uses semicolons instead of commas, pd.read_csv() will automatically detect and handle the separator.", False),
    ]

def lesson04_questions():
    return [
        ("You can select a single column from a DataFrame using square-bracket notation, such as df['column_name'], which returns a Series.", True),
        ("To select several columns at once, you pass each column name as a separate argument to df.select(), such as df.select('Name', 'Age').", False),
        ("The df.rename() method lets you change column names by passing a dictionary that maps old names to new names.", True),
        ("The only way to see all column names in a DataFrame is to print the first row using df.head(1).", False),
    ]

def lesson05_questions():
    return [
        ("You can filter a DataFrame by writing a condition inside square brackets, such as df[df['price'] &gt; 100], to get only the rows that match.", True),
        ("When combining two filter conditions in pandas, you use the Python keywords 'and' and 'or' between them, just like in a regular if statement.", False),
        ("The .isin() method lets you filter rows where a column value matches any item in a list, similar to SQL's IN operator.", True),
        ("Calling df.dropna() permanently deletes missing rows from your original DataFrame, even if you do not assign the result to a variable.", False),
    ]

def lesson06_questions():
    return [
        ("You can create a new column by assigning a calculation to a new column name, such as df['total'] = df['price'] * df['quantity'].", True),
        ("Pandas arithmetic operations work one row at a time using an internal loop, so adding a calculated column is slow on large datasets.", False),
        ("The np.where() function lets you set column values based on a condition, choosing one value when true and another when false.", True),
        ("To remove a column from a DataFrame, you must create a new DataFrame without that column &#8212; there is no method that drops a column directly.", False),
    ]

def lesson07_questions():
    return [
        ("The df.groupby() method splits a DataFrame into groups based on the unique values in a column, similar to GROUP BY in SQL.", True),
        ("After calling groupby(), the result is immediately a new DataFrame containing the totals &#8212; you do not need to apply an aggregation function.", False),
        ("The .agg() method lets you apply several functions at once, such as 'sum', 'mean', and 'count', to grouped data in a single step.", True),
        ("After a groupby operation, the grouped column automatically becomes a regular column &#8212; there is no need to call reset_index().", False),
    ]

def lesson08_questions():
    return [
        ("The pd.merge() function combines two DataFrames by matching rows that share the same value in a specified key column.", True),
        ("An inner merge keeps all rows from both DataFrames, filling in blanks with NaN wherever a key does not match.", False),
        ("You can merge on more than one column by passing a list of column names to the 'on' parameter, such as on=['year', 'region'].", True),
        ("If the key columns in two DataFrames have different names, pd.merge() will still match them automatically without specifying left_on and right_on.", False),
    ]

def lesson09_questions():
    return [
        ("You can detect missing values in a DataFrame by calling df.isna(), which returns True for every cell that contains NaN.", True),
        ("Calling df.dropna() removes only columns that contain missing values &#8212; it never drops rows.", False),
        ("The df.fillna() method replaces all NaN values with a value you specify, such as zero or a column mean.", True),
        ("Filling missing numerical values with zero is always the safest strategy because it does not add any bias to calculations.", False),
    ]

def lesson10_questions():
    return [
        ("Calling df.to_csv('output.csv', index=False) saves a DataFrame to a CSV file without writing the index as an extra column.", True),
        ("To write a DataFrame to an Excel file, you call df.to_csv() with a .xlsx file extension &#8212; pandas detects the format automatically.", False),
        ("You can choose which columns to export by passing a 'columns' parameter to to_csv() or to_excel() with a list of column names.", True),
        ("Calling df.to_csv('data.csv') a second time will automatically append new rows to the existing file instead of overwriting it.", False),
    ]


REGISTRY = {
    "lesson01_introduction_to_pandas.html": lesson01_questions,
    "lesson02_dataframes_explained.html": lesson02_questions,
    "lesson03_reading_data_csv_excel.html": lesson03_questions,
    "lesson04_selecting_columns.html": lesson04_questions,
    "lesson05_filtering_rows.html": lesson05_questions,
    "lesson06_creating_calculated_columns.html": lesson06_questions,
    "lesson07_aggregations_group_by.html": lesson07_questions,
    "lesson08_joining_data_merge.html": lesson08_questions,
    "lesson09_handling_missing_data.html": lesson09_questions,
    "lesson10_exporting_data.html": lesson10_questions,
}


def main():
    for fname, qfn in REGISTRY.items():
        fpath = ROOT / fname
        if not fpath.exists():
            print(f"  SKIP  {fname} (file not found)")
            continue
        html = fpath.read_text(encoding="utf-8")
        questions = qfn()
        new_section = make_section_html(questions)
        new_html, count = SECTION_RE.subn(new_section, html)
        if count == 0:
            print(f"  WARN  {fname} (no #knowledge-check section found)")
            continue
        fpath.write_text(new_html, encoding="utf-8")
        print(f"  OK    {fname} ({len(questions)} questions)")
    print("\nDone.")


if __name__ == "__main__":
    main()
