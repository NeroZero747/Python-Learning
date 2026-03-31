"""
Replace the #comparison body div in lesson03 (Git workflow).
Topic: version control — git add/commit/push vs SQL COMMIT vs Excel Save/Track Changes.
"""
import pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-5">

      <!-- 1 · Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">If you already save multiple copies of an Excel file or rely on SQL backups to recover data, you already understand why version control matters. Git gives you the same safety net for your code &mdash; but automatically, with a clear history of every change and the author who made it.</p>

      <!-- 2 · Tool header cards -->
      <div class="grid grid-cols-3 gap-3">
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python / Git
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel
        </div>
      </div>

      <!-- 3 · Row 1 — track a change -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:hand-pointer"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">track a change</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python / Git</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">git add</code>
            <p class="text-xs text-gray-500 leading-relaxed">Marks specific files to include in the next snapshot — you choose exactly which changes to save.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">transaction log</code>
            <p class="text-xs text-gray-500 leading-relaxed">SQL records every change to a row in a system log that administrators can query to trace what happened.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Track Changes</code>
            <p class="text-xs text-gray-500 leading-relaxed">Excel's built-in tool highlights edits so you can accept or reject each one before saving the final copy.</p>
          </div>
        </div>
      </div>

      <!-- 3 · Row 2 — save a snapshot -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:bookmark"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">save a snapshot</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python / Git</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">git commit</code>
            <p class="text-xs text-gray-500 leading-relaxed">Locks your staged changes into a permanent, labeled snapshot you can return to at any time.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">COMMIT</code>
            <p class="text-xs text-gray-500 leading-relaxed">Finalises a database transaction and writes it permanently to disk, confirming the change is saved.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Save a Copy</code>
            <p class="text-xs text-gray-500 leading-relaxed">Saves a duplicate workbook with a new name, creating a manual version you keep in a folder.</p>
          </div>
        </div>
      </div>

      <!-- 3 · Row 3 — view history -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:clock-rotate-left"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">view history</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python / Git</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">git log</code>
            <p class="text-xs text-gray-500 leading-relaxed">Shows every commit ever made — newest first — with the author's name, date, and message.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">audit table</code>
            <p class="text-xs text-gray-500 leading-relaxed">A separate table where every INSERT, UPDATE, or DELETE is automatically logged by a trigger.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Version History</code>
            <p class="text-xs text-gray-500 leading-relaxed">The OneDrive panel that shows every auto-saved version of a shared workbook so you can restore any earlier state.</p>
          </div>
        </div>
      </div>

      <!-- 3 · Row 4 — share with the team -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:cloud-arrow-up"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">share with the team</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python / Git</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">git push</code>
            <p class="text-xs text-gray-500 leading-relaxed">Uploads your local commits to a remote repository on GitLab so teammates can see and download them.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">shared schema</code>
            <p class="text-xs text-gray-500 leading-relaxed">All team members query the same live database, so committed changes are immediately visible to everyone.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">OneDrive sync</code>
            <p class="text-xs text-gray-500 leading-relaxed">Saves the workbook to a shared cloud folder where colleagues open the same file in real time.</p>
          </div>
        </div>
      </div>

      <!-- 4 · Centered divider + side-by-side code blocks -->
      <div>
        <div class="flex items-center gap-3 mb-4">
          <span class="flex-1 h-px bg-gray-100"></span>
          <div class="flex items-center gap-2 shrink-0">
            <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
            </span>
            <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">Same snapshot save, three tools</p>
          </div>
          <span class="flex-1 h-px bg-gray-100"></span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 items-stretch">

          <!-- Git / Python column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Git commands</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                  <span class="text-xs font-semibold text-gray-400">Bash</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-bash">git add report.py
git commit -m "Add Q1 report"</code></pre>
            </div>
          </div>

          <!-- SQL column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">SQL query</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-orange-400" data-icon="fa6-solid:database"></span>
                  <span class="text-xs font-semibold text-gray-400">SQL</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-sql">BEGIN TRANSACTION;
UPDATE reports
  SET status = 'final';
COMMIT;</code></pre>
            </div>
          </div>

          <!-- Excel column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Excel formula</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-green-400" data-icon="fa6-solid:table"></span>
                  <span class="text-xs font-semibold text-gray-400">Excel</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-text">File &gt; Save a Copy
  &gt; report_v2.xlsx</code></pre>
            </div>
          </div>

        </div>
        <p class="text-xs text-gray-400 mt-2">All three save a permanent record of a change to a project — the same idea, just written in a different tool.</p>
      </div>

      <!-- 5 · Closing amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">The version control idea is the same whether you use Git, SQL, or Excel &mdash; you are always making deliberate, labeled saves so you can recover earlier states. Git just replaces manual file naming and copy-pasting with a single command that records who changed what and when.</p>
      </div>

    </div>'''


def find_comparison_body(content):
    """Find start/end of the body div inside #comparison using div-depth counting."""
    sec_start = content.find('<section id="comparison">')
    if sec_start == -1:
        return None, None
    sec_end = content.find('</section>', sec_start) + len('</section>')
    section = content[sec_start:sec_end]

    body_marker = '    <div class="bg-white px-8 py-7 space-y-5">'
    body_start_rel = section.find(body_marker)
    if body_start_rel == -1:
        return None, None

    body_start_abs = sec_start + body_start_rel
    depth = 0
    i = body_start_abs
    while i < sec_end + sec_start:
        if content[i:i+4] == '<div':
            depth += 1
            i += 4
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return body_start_abs, i + 6
            i += 6
        else:
            i += 1
    return None, None


def main():
    content = TARGET.read_text(encoding="utf-8")

    start, end = find_comparison_body(content)
    if start is None:
        print("❌ Could not locate #comparison body div")
        return

    new_content = content[:start] + NEW_BODY + content[end:]
    TARGET.write_text(new_content, encoding="utf-8")
    print("✅ #comparison body replaced")

    result = TARGET.read_text(encoding="utf-8")
    sec_start = result.find('<section id="comparison">')
    sec_end   = result.find('</section>', sec_start) + len('</section>')
    section   = result[sec_start:sec_end]

    checks = [
        ('Intro uses "If you already"',        'If you already' in section),
        ('Tool header — Python/Git',            'Python / Git' in section),
        ('Tool header — SQL (orange)',          'bg-orange-600' in section),
        ('Tool header — Excel (emerald)',       'bg-emerald-600' in section),
        ('Row 1 — track a change',             'track a change' in section),
        ('Row 2 — save a snapshot',            'save a snapshot' in section),
        ('Row 3 — view history',               'view history' in section),
        ('Row 4 — share with the team',        'share with the team' in section),
        ('4 icon badges on rows',              section.count('w-5 h-5 rounded bg-indigo-50') == 4),
        ('Chip colors: indigo Python',         'bg-indigo-50 text-indigo-700' in section),
        ('Chip colors: orange SQL',            'bg-orange-50 text-orange-700' in section),
        ('Chip colors: emerald Excel',         'bg-emerald-50 text-emerald-700' in section),
        ('Divider centered hairlines',         'flex-1 h-px bg-gray-100' in section),
        ('Divider label text',                 'Same snapshot save, three tools' in section),
        ('Divider icon code-compare',          'fa6-solid:code-compare' in section),
        ('No traffic-light dots',              'rounded-full bg-red-400' not in section),
        ('Git code block (bash)',              'language-bash' in section),
        ('SQL code block',                    'language-sql' in section),
        ('Excel code block (text)',           'language-text' in section),
        ('Caption starts with "All three"',   'All three' in section),
        ('amber tip present',                  'bg-amber-tip' in section),
    ]

    passed = failed = 0
    for label, ok in checks:
        status = "✅" if ok else "❌"
        if ok: passed += 1
        else:  failed += 1
        print(f"  {status} {label}")

    print(f"\n{'✅ All' if failed == 0 else '⚠️'} {passed}/{passed+failed} checks passed")


if __name__ == "__main__":
    main()
