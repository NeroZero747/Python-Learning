"""Rewrite #knowledge-check for every lesson in track_02 / mod_03."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_03_python_for_analysts")
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

def lesson01_questions():
    return [
        ("Python lets analysts automate repetitive tasks that would otherwise require manual work in spreadsheets, such as reformatting data or generating reports.", True),
        ("Python has only a handful of data-related libraries, so analysts need to write most analysis code from scratch without any third-party help.", False),
        ("In a typical analyst workflow, Python sits between the data source and the final report &#8212; pulling data in, transforming it, and exporting results.", True),
        ("Python should replace Excel for every task, including quick one-off calculations and simple data lookups that take under a minute in a spreadsheet.", False),
    ]

def lesson02_questions():
    return [
        ("The pandas merge() function can replicate Excel's VLOOKUP by joining two DataFrames on a shared key column.", True),
        ("Pandas cannot create pivot tables &#8212; you need to export your data back to Excel and build the pivot table there.", False),
        ("Using pd.ExcelWriter(), you can write multiple DataFrames to separate sheets within a single Excel workbook.", True),
        ("A Python script that automates an Excel workflow must be rewritten from scratch every time the input file has a different name.", False),
    ]

def lesson03_questions():
    return [
        ("Using parameterised queries with placeholders protects your code from SQL injection by keeping user input separate from the SQL statement.", True),
        ("You should always pull the entire database table into pandas first and then filter in Python, because SQL WHERE clauses are slower than pandas filtering.", False),
        ("Storing long SQL queries in separate variables or triple-quoted strings keeps your Python code readable and easier to maintain.", True),
        ("If a SQL query runs slowly through pandas, the bottleneck is always in the pd.read_sql() function &#8212; the database server itself is never the cause.", False),
    ]

def lesson04_questions():
    return [
        ("Tasks that involve the same steps on different files each week &#8212; like reformatting and summarising &#8212; are strong candidates for automation with Python.", True),
        ("To process ten CSV files in a folder, you need to write ten separate pd.read_csv() calls &#8212; there is no way to loop over files automatically.", False),
        ("On Windows, you can use Task Scheduler to run a Python script automatically at a set time without manually opening the file.", True),
        ("Adding logging to an automated script is unnecessary extra work because Python automatically saves a log of every print() statement to a file.", False),
    ]

def lesson05_questions():
    return [
        ("A well-structured reporting script follows a clear sequence: load data, transform it, calculate summaries, and export the final output.", True),
        ("Pandas automatically formats numbers with thousand separators and dates in your local format when exporting to Excel &#8212; no extra code is needed.", False),
        ("Using pd.ExcelWriter with multiple to_excel() calls lets you place raw data, summaries, and charts on separate sheets in one workbook.", True),
        ("The only way to add a totals row to the bottom of a DataFrame is to calculate the sum manually and append it using a for loop.", False),
    ]

def lesson06_questions():
    return [
        ("An end-to-end reporting pipeline connects data extraction, transformation, summarisation, and export into a single script that runs without manual steps.", True),
        ("If one step in your pipeline fails, the entire script should crash immediately &#8212; adding try/except blocks hides bugs and makes debugging harder.", False),
        ("Python's smtplib library lets your script send an email with the finished report attached, so stakeholders receive it automatically.", True),
        ("Once a script is scheduled to run daily, you no longer need logging because the scheduler keeps a complete record of every output the script produces.", False),
    ]


REGISTRY = {
    "lesson01_why_analysts_use_python.html": lesson01_questions,
    "lesson02_replacing_excel_workflows_with_python.html": lesson02_questions,
    "lesson03_using_python_with_sql_queries.html": lesson03_questions,
    "lesson04_automating_repetitive_data_tasks.html": lesson04_questions,
    "lesson05_building_a_simple_reporting_script.html": lesson05_questions,
    "lesson06_automating_reports_end_to_end.html": lesson06_questions,
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
