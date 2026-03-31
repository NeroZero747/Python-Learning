"""
Replace the #code-examples body div in lesson03 (Git workflow).
4 examples — bash code, correct Style A structure, no traffic-light dots, terminal pane.
"""
import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

# ── Locate the old body div inside #code-examples ───────────────────────────
OLD_BODY_START = '    <div class="bg-white px-8 py-7 space-y-6">\n      <div class="flex items-center gap-2 mb-6" role="tablist"><button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">'

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Your First Commit</span>
        </button>
        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Stage the Right Files</span>
        </button>
        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Write a Clear Message</span>
        </button>
        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Push to GitLab</span>
        </button>
      </div>

      <!-- ── Panel 1 — Your First Commit ─────────────────────────────── -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Your First Commit</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git init, git add, git commit</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">These four commands turn a plain folder into a tracked project and save your first snapshot. <strong class="text-gray-800">git init</strong> creates the hidden <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">.git</code> folder that Git uses to remember every future change.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">first_commit.sh</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-bash">git init                               # turn this folder into a Git repository
git add report.py                      # tell Git to start tracking this file
git commit -m &quot;Add report script&quot;      # lock in the first snapshot with a label
git log --oneline                      # show the snapshot you just created</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ bash first_commit.sh</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">e4f5a12 Add report script</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">You only run <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git init</code> once per project — after that, every new snapshot needs only <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git add</code> and <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git commit</code>.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 2 — Stage the Right Files ─────────────────────────── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Stage the Right Files</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Analysis Scripts</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git status, git add</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This runs <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">git status</code> before and after staging so you can see exactly which files Git is tracking. Staging one file at a time gives you precise control over what goes into each snapshot.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">stage_files.sh</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-bash">git status                             # show all changed and untracked files
git add analysis.py                    # stage this one file only
git status                             # confirm the file is now in the staging area
git commit -m &quot;Add data analysis script&quot;  # save the staged snapshot</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ bash stage_files.sh</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">[main 9c3d2e1] Add data analysis script</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Run <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git status</code> before every commit — it shows exactly what Git has noticed so you never accidentally stage the wrong file.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 3 — Write a Clear Message ─────────────────────────── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Write a Clear Message</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Dashboards</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git commit -m, git log</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This commits one changed file with a descriptive message, then shows the history. A good commit message tells your team (and your future self) exactly what changed and why — not just that something was &ldquo;updated&rdquo;.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">commit_message.sh</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-bash">git add dashboard.py                         # stage the changed file
git commit -m &quot;Fix column total formula&quot;      # describe what changed, not what you did
git log --oneline                            # review the snapshot history</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ bash commit_message.sh</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">7a3b2c1 Fix column total formula<br>e4f5a12 Add report script</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Write your message to complete the sentence "If applied, this commit will…" — that forces you to describe the change rather than just say "misc fixes" or "updated file".</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 4 — Push to GitLab ────────────────────────────────── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Push to GitLab</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Team Projects</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git remote add, git push</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This runs the full stage &rarr; commit &rarr; push cycle and uploads your work to GitLab. <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">git push origin main</code> only uploads committed snapshots &mdash; you must run <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">git add</code> and <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">git commit</code> first.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">push_to_gitlab.sh</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-bash">git add .                                               # stage every changed file at once
git commit -m &quot;Add Q1 forecast model&quot;                   # save the snapshot locally
git remote add origin https://gitlab.com/you/project.git  # link to GitLab (one-time setup only)
git push origin main                                    # upload all commits to GitLab</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ bash push_to_gitlab.sh</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Branch &apos;main&apos; set up to track remote branch &apos;main&apos; from &apos;origin&apos;.</div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">You only need <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git remote add</code> once per project — after that, <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git push origin main</code> is all you need to share new commits with your team.</p>
            </div>
          </div>

        </div>
      </div>

    </div>'''


def find_ce_body(content):
    """Find start/end of the body div inside #code-examples."""
    sec_start = content.find('<section id="code-examples">')
    if sec_start == -1:
        return None, None
    sec_end = content.find('</section>', sec_start) + len('</section>')
    section = content[sec_start:sec_end]

    # Find the body div (directly after the section header closing div)
    body_marker = '    <div class="bg-white px-8 py-7 space-y-6">'
    body_start_rel = section.find(body_marker)
    if body_start_rel == -1:
        return None, None

    # Find its closing </div> — it's the outer wrapper, matched by counting divs
    body_start_abs = sec_start + body_start_rel
    depth = 0
    i = body_start_abs
    while i < sec_end:
        if content[i:i+4] == '<div':
            depth += 1
            i += 4
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                body_end_abs = i + 6
                return body_start_abs, body_end_abs
            i += 6
        else:
            i += 1
    return None, None


def main():
    content = TARGET.read_text(encoding="utf-8")

    start, end = find_ce_body(content)
    if start is None:
        print("❌ Could not locate #code-examples body div")
        return

    new_content = content[:start] + NEW_BODY + content[end:]
    TARGET.write_text(new_content, encoding="utf-8")
    print("✅ #code-examples body replaced")

    # Verification
    result = TARGET.read_text(encoding="utf-8")
    # Scope to #code-examples section for traffic-light check
    ce_start = result.find('<section id="code-examples">')
    ce_end   = result.find('</section>', ce_start) + len('</section>')
    section  = result[ce_start:ce_end]

    checks = [
        ('4 ce-step buttons',             section.count('class="ce-step') >= 4),
        ('4 ce-panels',                   section.count('class="ce-panel') >= 4),
        ('Panel 1 visible (no hidden)',   'ce-panel ce-panel-anim"' in section),
        ('Panels 2-4 hidden',             section.count('ce-panel ce-panel-anim hidden') == 3),
        ('No traffic-light dots',         'rounded-full bg-red-400' not in section),
        ('No .sql filenames',             '.sql' not in section),
        ('All 4 terminal panes',          section.count('bg-[#11111b]') == 4),
        ('All 4 amber tips',              section.count('bg-amber-tip') == 4),
        ('All 4 task-box descriptions',   section.count('task-box') == 4),
        ('Tab: Your First Commit',        'Your First Commit' in section),
        ('Tab: Stage the Right Files',    'Stage the Right Files' in section),
        ('Tab: Write a Clear Message',    'Write a Clear Message' in section),
        ('Tab: Push to GitLab',           'Push to GitLab' in section),
        ('Watermarks 01-04',              all(f'>{n:02d}<' in section for n in [1,2,3,4])),
        ('Filenames are .sh',             all(f in section for f in ['first_commit.sh','stage_files.sh','commit_message.sh','push_to_gitlab.sh'])),
    ]

    passed = failed = 0
    for label, ok in checks:
        status = "✅" if ok else "❌"
        (passed if ok else failed).__class__  # no-op
        if ok: passed += 1
        else:  failed += 1
        print(f"  {status} {label}")

    print(f"\n{'✅ All' if failed == 0 else '⚠️'} {passed}/{passed+failed} checks passed")


if __name__ == "__main__":
    main()
