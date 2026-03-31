"""Replace the #mistakes section body in lesson03 with proper Git-specific mistake panels."""

TARGET = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

NEW_BODY = '''\
      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Vague Commit Message</span>
        </button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Adding Everything</span>
        </button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Commit ≠ Shared</span>
        </button>
      </div>

      <!-- Mistake 1 — Vague Commit Message -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Using a Vague Message Like "update" or "fix"</h4>
              <p class="text-xs text-gray-500 mt-0.5">Git records your message forever — a vague message makes it impossible to understand what changed weeks later.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git commit -m "update"</code> creates a permanent snapshot with no useful information — your future self and your teammates cannot tell what actually changed. Replace the message with a short imperative phrase that names the specific change, such as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"Add Q1 sales aggregation step"</code>.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — vague message
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash">git commit -m "update"</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — specific imperative phrase
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash">git commit -m "Add Q1 sales aggregation step"  # names the exact change</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of a commit message like the subject line of an email — you can open the commit to see the full diff, but a subject of <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">"stuff"</code> makes the history impossible to scan. Aim for a message that tells you what changed without having to open it.</p>
          </div>

        </div>
      </div>

      <!-- Mistake 2 — Adding Everything -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Running git add . Without Checking What Will Be Staged</h4>
              <p class="text-xs text-gray-500 mt-0.5"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git add .</code> stages every changed file — including scratch files, credentials, and large data exports you never meant to commit.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git add .</code> stages all modified files at once — including temporary files, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> files containing API keys, or multi-gigabyte data exports. Run <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git status</code> first to review which files are modified, then stage only the files you intend to commit using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git add FILENAME</code>.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — stage everything blindly
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash">git add .                   # stages all files — including secrets
git commit -m "Add changes"</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — check then stage selectively
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash">git status                            # review what has changed
git add sales_report.sh               # stage only the intended file
git commit -m "Add Q1 sales summary"  # save just that change</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">git add .</code> like forwarding an entire email thread — you might accidentally share something in the history that was meant to stay private. Use targeted <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">git add FILENAME</code> to keep each commit clean and intentional.</p>
          </div>

        </div>
      </div>

      <!-- Mistake 3 — Commit ≠ Shared -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Treating a Local Commit as if the Team Can Already See It</h4>
              <p class="text-xs text-gray-500 mt-0.5"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git commit</code> saves a snapshot on your machine only — teammates see nothing on GitLab until you run <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git push</code>.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git commit</code> writes a snapshot to your local repository and does not contact the remote server at all — teammates checking GitLab will still see the old version. Run <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">git push</code> after committing to upload your snapshots so the team can see them.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — commit but never push
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash">git add analysis.sh
git commit -m "Add cleaning step"
# team still sees the old version on GitLab</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — commit then push
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash">git add analysis.sh
git commit -m "Add cleaning step"  # save snapshot locally
git push origin main               # upload so teammates can see it</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">git commit</code> as saving a document to your own hard drive and <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">git push</code> as uploading it to a shared folder. Your colleagues can only open the file after the upload — a commit alone is never enough to share your work.</p>
          </div>

        </div>
      </div>
'''


def find_mistakes_body(html: str):
    """Find start/end indices of the body div inside #mistakes."""
    section_pos = html.find('<section id="mistakes">')
    if section_pos == -1:
        return None, None

    marker = '<div class="bg-white px-8 py-7 space-y-6">'
    body_start = html.find(marker, section_pos)
    if body_start == -1:
        return None, None

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

    start, end = find_mistakes_body(html)
    if start is None:
        print("❌ Could not locate #mistakes body div")
        return

    new_html = html[:start] + "\n" + NEW_BODY + "    " + html[end:]

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)

    print("✅ #mistakes body replaced")

    # Scope for verification — just the mistakes section
    mk_section = new_html[new_html.find('<section id="mistakes">'):
                           new_html.find('<section id="real-world">')]

    checks = [
        # Tab labels — descriptive, not "Mistake N"
        ("Tab: Vague Commit Message",           "Vague Commit Message" in mk_section),
        ("Tab: Adding Everything",              "Adding Everything" in mk_section),
        ("Tab: Commit ≠ Shared",                "Commit ≠ Shared" in mk_section),
        ("No 'Mistake 1/2/3' labels",           "Mistake 1</span>" not in mk_section and
                                                "Mistake 2</span>" not in mk_section and
                                                "Mistake 3</span>" not in mk_section),
        # Panel visibility
        ("Panel 1 not hidden",                  'class="mk-panel mk-panel-anim"' in mk_section),
        ("Panel 2 hidden",                      mk_section.count('class="mk-panel mk-panel-anim hidden"') >= 2),
        # Split panel structure
        ("Red panel bg present (x3)",           mk_section.count("bg-red-50/30") >= 3),
        ("Emerald panel bg present (x3)",       mk_section.count("bg-emerald-50/30") >= 3),
        ("Arrow divider present (x3)",          mk_section.count("fa6-solid:arrow-right") >= 3),
        # No traffic-light dots
        ("No traffic-light dots",               "rounded-full bg-red-400/80" not in mk_section),
        # No style-A dark chrome header
        ("No dark-chrome header (bg-[#181825])","bg-[#181825]" not in mk_section),
        # Correct code class
        ("language-bash used",                  'class="language-bash"' in mk_section),
        # Content checks
        ("git commit -m present",               'git commit -m' in mk_section),
        ("git add . explained",                 "git add ." in mk_section),
        ("git push present",                    "git push" in mk_section),
        # Amber tips
        ("Amber tips present (3)",              mk_section.count("bg-amber-50/40") >= 3),
        # switchMkTab indices
        ("switchMkTab(0) present",              "switchMkTab(0)" in mk_section),
        ("switchMkTab(1) present",              "switchMkTab(1)" in mk_section),
        ("switchMkTab(2) present",              "switchMkTab(2)" in mk_section),
        # Section shell intact
        ("Section id unchanged",                'id="mistakes"' in mk_section),
        ("Header icon unchanged",               "fa6-solid:triangle-exclamation" in mk_section),
        ("Header title unchanged",              "Common Mistakes" in mk_section),
    ]

    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  {'✅' if ok else '❌'} {label}")
    print(f"\n{'✅' if passed == len(checks) else '⚠️'} {passed}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
