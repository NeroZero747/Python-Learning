"""Rewrite #knowledge-check for every lesson in track_02 / mod_02."""

import re, pathlib

ROOT = pathlib.Path(r"pages/track_02_data_analytics/mod_02_working_with_data_sources")
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
        ("When a CSV file uses a tab character as its separator, you can load it by passing sep='\\t' to pd.read_csv().", True),
        ("The only way to load specific columns from a CSV file is to read the entire file first and then drop the columns you do not need.", False),
        ("If a CSV file displays garbled characters after loading, changing the encoding parameter &#8212; such as encoding='latin-1' &#8212; usually fixes the issue.", True),
        ("Setting the dtype parameter in pd.read_csv() makes the file download faster from disk by compressing the data as it reads.", False),
    ]

def lesson02_questions():
    return [
        ("The pd.read_json() function can load a JSON file directly into a DataFrame when the data is structured as a list of records.", True),
        ("When a JSON file contains nested objects, pd.read_json() automatically flattens all nested levels into separate columns.", False),
        ("Calling df.to_json() converts a DataFrame into a JSON string, and passing a file path saves it directly to disk.", True),
        ("All JSON files follow the same structure &#8212; a single array of flat objects &#8212; so pd.read_json() works the same way every time.", False),
    ]

def lesson03_questions():
    return [
        ("A database connection string contains the database type, username, password, host, and database name &#8212; all in a single URL-format string.", True),
        ("You can pass a raw username and password directly to pd.read_sql() without creating a SQLAlchemy engine first.", False),
        ("The pd.read_sql_table() function loads an entire database table into a DataFrame using a SQLAlchemy engine connection.", True),
        ("Python automatically closes database connections when your script ends, so you never need to call .close() or use a context manager.", False),
    ]

def lesson04_questions():
    return [
        ("You can pass a SQL SELECT statement as a string to pd.read_sql() and receive the results as a pandas DataFrame.", True),
        ("The safest way to include user input in a SQL query is to use Python f-strings to insert the values directly into the SQL string.", False),
        ("Every call to pd.read_sql() returns a DataFrame, so you can immediately use pandas methods like .head() and .describe() on the result.", True),
        ("Pandas cannot join data from two SQL queries &#8212; you must write a single SQL query with a JOIN clause to combine tables.", False),
    ]

def lesson05_questions():
    return [
        ("The df.to_sql() method writes a DataFrame directly to a database table using a SQLAlchemy engine connection.", True),
        ("When you call df.to_sql() on an existing table, pandas automatically appends the new rows &#8212; it never overwrites the table.", False),
        ("If the target table does not exist in the database, df.to_sql() creates it automatically and infers column types from the DataFrame.", True),
        ("Pandas always converts DataFrame column types to match the database schema exactly, so type mismatch errors cannot occur with to_sql().", False),
    ]

def lesson06_questions():
    return [
        ("Hard-coding database passwords directly in your Python script creates a security risk because anyone who reads the file can see the credentials.", True),
        ("A .env file is encrypted by default, so it is safe to upload it to a public GitHub repository without any additional precautions.", False),
        ("The python-dotenv library provides a load_dotenv() function that reads key-value pairs from a .env file and makes them available as environment variables.", True),
        ("Adding your .env file to .gitignore only hides it from the directory listing &#8212; Git will still track and upload it when you push.", False),
    ]


REGISTRY = {
    "lesson01_reading_csv_files.html": lesson01_questions,
    "lesson02_working_with_json_files.html": lesson02_questions,
    "lesson03_connecting_to_databases.html": lesson03_questions,
    "lesson04_running_sql_in_python.html": lesson04_questions,
    "lesson05_writing_data_back_to_a_database.html": lesson05_questions,
    "lesson06_managing_credentials_env.html": lesson06_questions,
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
