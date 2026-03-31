"""Replace the #practice section body in lesson03 with proper Git bash exercises."""

TARGET = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

NEW_BODY = '''\
      <!-- 1 · Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Save Your First Commit</span>
        </button>

        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Stage One File</span>
        </button>

        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Push to GitLab</span>
        </button>

      </div>

      <!-- 2 · Exercise 1 — Save Your First Commit -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Save Your First Commit</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git init</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git commit</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You have just written a quarterly sales report and saved it as <code>q1_report.md</code>. Initialise a Git repository in the project folder, stage the file, and commit it with a clear message. Run <code>git log --oneline</code> at the end to confirm Git recorded your snapshot.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block — Style A (bash, no traffic-light dots) -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">first_commit.sh</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash">git init                                   # create a new Git repository in this folder
git add q1_report.md                       # stage the report so Git will include it
git commit -m "Add Q1 report first draft"  # save a permanent snapshot with a message
git log --oneline                          # confirm the commit appears in the history</code></pre>
                </div>
                <!-- Terminal pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ bash first_commit.sh</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">[main (root-commit) a1b2c3d] Add Q1 report first draft<br>a1b2c3d Add Q1 report first draft</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Running <code>git log --oneline</code> after each commit confirms Git saved your work. Every line in the log is a permanent record — if you need to undo a change later, this list tells you exactly where to go back to.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- 3 · Exercise 2 — Stage One File -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Stage One File</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Analysis Scripts</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git add</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git status</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You edited two scripts today — <code>clean_data.sh</code> and <code>explore_data.sh</code> — but only <code>clean_data.sh</code> is ready to save. Stage just that one file and commit it with a clear message. Use <code>git status</code> before and after staging to see exactly which files Git is tracking.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block — Style A (bash, no traffic-light dots) -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">stage_one.sh</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash">git status                                        # check which files have changed
git add clean_data.sh                             # stage only the data-cleaning script
git status                                        # confirm only one file is staged
git commit -m "Clean null values in source data"  # save the staged file as a snapshot</code></pre>
                </div>
                <!-- Terminal pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ bash stage_one.sh</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Changes to be committed: clean_data.sh<br>[main 4f5e6d7] Clean null values in source data</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Staging files individually keeps each commit focused on one change. Your team can read the history later and understand exactly what changed and why — without digging through unrelated edits bundled into the same snapshot.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- 4 · Exercise 3 — Push to GitLab -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Push to GitLab</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Team Projects</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git push</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">git remote</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You have committed a sales pipeline script locally and need to share it with your team on GitLab. Stage and commit the file, link your local repository to a remote GitLab project, and push your commits. Your teammates can then pull your changes and continue the work.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block — Style A (bash, no traffic-light dots) -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">push_to_gitlab.sh</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash">git add sales_pipeline.sh                                    # stage the updated pipeline script
git commit -m "Add monthly sales aggregation step"           # save the snapshot locally
git remote add origin https://gitlab.com/team/pipeline.git   # link this repo to GitLab
git push -u origin main                                      # upload all commits to GitLab</code></pre>
                </div>
                <!-- Terminal pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ bash push_to_gitlab.sh</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Branch &apos;main&apos; set up to track origin/main.<br>* [new branch]      main -&gt; main</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">The <code>-u</code> flag in <code>git push -u origin main</code> sets GitLab as the default destination. After the first push, typing just <code>git push</code> is enough — Git remembers where to send your commits every time.</p>
              </div>

            </div>
          </div>

        </div>
      </div>
'''


def find_practice_body(html: str):
    """Find start/end indices of the body div inside #practice."""
    # Find the section anchor
    section_pos = html.find('<section id="practice">')
    if section_pos == -1:
        return None, None

    # Find the body div that immediately follows the section header
    marker = '<div class="bg-white px-8 py-7 space-y-6">'
    body_start = html.find(marker, section_pos)
    if body_start == -1:
        return None, None

    # Walk forward counting div depth to find the matching closing tag
    content_start = body_start + len(marker)
    depth = 1
    pos = content_start
    while pos < len(html) and depth > 0:
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return content_start, next_close
            pos = next_close + 6
    return None, None


def main():
    with open(TARGET, encoding="utf-8") as f:
        html = f.read()

    start, end = find_practice_body(html)
    if start is None:
        print("❌ Could not locate #practice body div")
        return

    new_html = html[:start] + "\n" + NEW_BODY + "    " + html[end:]

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)

    print("✅ #practice body replaced")

    # ── Verification ──────────────────────────────────────────────
    checks = [
        # Tab labels
        ("Tab: Save Your First Commit",   "Save Your First Commit" in new_html),
        ("Tab: Stage One File",           "Stage One File" in new_html),
        ("Tab: Push to GitLab",           "Push to GitLab" in new_html),
        ("No 'Exercise 1/2/3' labels",    "Exercise 1</span>" not in new_html and
                                          "Exercise 2</span>" not in new_html and
                                          "Exercise 3</span>" not in new_html),
        # Watermarks
        ("Watermark 01 present",          ">01<" in new_html),
        ("Watermark 02 present",          ">02<" in new_html),
        ("Watermark 03 present",          ">03<" in new_html),
        # Domains
        ("Domain: Reports badge",         ">Reports<" in new_html),
        ("Domain: Analysis Scripts badge","Analysis Scripts" in new_html),
        ("Domain: Team Projects badge",   "Team Projects" in new_html),
        # Filenames
        ("File: first_commit.sh",         "first_commit.sh" in new_html),
        ("File: stage_one.sh",            "stage_one.sh" in new_html),
        ("File: push_to_gitlab.sh",       "push_to_gitlab.sh" in new_html),
        # No traffic-light dots
        ("No traffic-light dots",         "rounded-full bg-red-400/80" not in
                                          new_html[new_html.find('<section id="practice">'):
                                                   new_html.find('<section id="mistakes">')]),
        # Correct language
        ("language-bash class",           new_html.count('class="language-bash"') >= 3),
        # Terminal panes present
        ("Terminal pane in each panel",   new_html.count("$ bash ") >= 3),
        # Amber tips
        ("Amber tips present (3+)",       new_html.count("bg-amber-tip") >= 3),
        # Panels hidden correctly
        ("Panel 1 not hidden",            'class="pe-panel pe-panel-anim"' in new_html),
        ("Panel 2 hidden",                'class="pe-panel pe-panel-anim hidden"' in new_html),
        # git terminology
        ("git commit present",            "git commit" in new_html),
        ("git push present",              "git push" in new_html),
        ("GitLab URL present",            "gitlab.com" in new_html),
    ]

    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  {'✅' if ok else '❌'} {label}")
    print(f"\n{'✅' if passed == len(checks) else '⚠️'} {passed}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
