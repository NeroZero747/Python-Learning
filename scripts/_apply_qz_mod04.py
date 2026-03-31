"""Rewrite #knowledge-check for every lesson in track_02 / mod_04."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_04_handling_large_data")
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
    pills = build_pill_tabs()
    panels = '\n'.join(build_panel(i, q[0], q[1]) for i, q in enumerate(questions))
    return f'{pills}\n{panels}'


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

def lesson02_questions():
    return [
        ("A DataFrame with one million rows can use far more memory than the original CSV file because pandas stores each value with a fixed-size data type.", True),
        ("The df.info() method only shows column names and data types &#8212; it cannot display how much memory each column uses.", False),
        ("Changing a column from int64 to int16 with pd.to_numeric(downcast='integer') reduces its memory usage when the values fit in the smaller type.", True),
        ("Converting a text column to the 'category' dtype always increases memory usage because pandas stores both the original strings and the category codes.", False),
    ]

def lesson03_questions():
    return [
        ("Reading a very large CSV file at once can crash Python because the entire file must fit into your computer's available RAM.", True),
        ("The chunksize parameter in pd.read_csv() splits the file into smaller CSV files on disk, which you then load one at a time.", False),
        ("When you iterate over chunks, each chunk is a regular DataFrame that you can filter, aggregate, or transform using normal pandas methods.", True),
        ("After processing each chunk separately, you must re-read the original file to combine the results &#8212; there is no way to merge chunk results in memory.", False),
    ]

def lesson04_questions():
    return [
        ("Operations that use a Python for-loop to process rows one at a time are typically much slower than vectorised pandas methods on large datasets.", True),
        ("Vectorised operations in pandas are just a shorthand for writing for-loops &#8212; they run at the same speed as looping through rows manually.", False),
        ("The np.select() function lets you apply multiple conditions to create a new column, similar to a chain of IF-ELSE statements in Excel.", True),
        ("You only need to benchmark your code when it is completely finished &#8212; profiling during development does not help you find bottlenecks.", False),
    ]

def lesson05_questions():
    return [
        ("In a columnar storage format, all values for a single column are stored together on disk, which makes reading individual columns much faster.", True),
        ("Row-based formats like CSV read individual columns faster than columnar formats because the data for each row is already grouped together.", False),
        ("When you query only three columns from a columnar file, the storage engine skips all other columns entirely &#8212; it never reads data you did not request.", True),
        ("Python can only read columnar files if you install a special database server &#8212; the Parquet format requires a running database instance.", False),
    ]

def lesson06_questions():
    return [
        ("Parquet is a binary columnar file format that stores data more efficiently than CSV by using compression and encoding for each column.", True),
        ("To save a DataFrame as a Parquet file, you first need to convert it to CSV format and then use a separate command-line tool to convert the CSV to Parquet.", False),
        ("When reading a Parquet file, you can pass a 'columns' parameter to load only the columns you need, which saves both time and memory.", True),
        ("Parquet files are always larger than the equivalent CSV file because Parquet adds metadata and schema information on top of the raw data.", False),
    ]

def lesson13_questions():
    return [
        ("Python's timeit module lets you measure how long a specific piece of code takes to run, helping you compare the speed of different approaches.", True),
        ("The best way to find the slowest part of your script is to add time.sleep() calls between sections and see which pause feels the longest.", False),
        ("The cProfile module shows you how many times each function was called and how much total time it consumed, making it easy to spot bottlenecks.", True),
        ("Once you identify a slow function, you should always optimise it immediately &#8212; the size of the performance improvement does not matter.", False),
    ]


REGISTRY = {
    "lesson02_memory_optimization.html": lesson02_questions,
    "lesson03_chunk_processing.html": lesson03_questions,
    "lesson04_processing_millions_of_rows.html": lesson04_questions,
    "lesson05_columnar_storage.html": lesson05_questions,
    "lesson06_parquet_files.html": lesson06_questions,
    "lesson13_performance_profiling.html": lesson13_questions,
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
