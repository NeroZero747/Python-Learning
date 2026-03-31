"""
Replace the #decision-flow body div in lesson03 with a Git workflow design.
Mirrors: Edit Files → Stage Changes → Commit Ready? → Save Snapshot → Push to Remote
"""
import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

OLD_BODY = '''    <div class="bg-white px-8 py-7 space-y-5">
      <div class="relative overflow-x-auto pb-2">
  <div class="flex items-center gap-0 min-w-[640px]"><div class="flex flex-col items-center shrink-0" style="width:120px;">
  <div class="w-16 h-16 rounded-full bg-gradient-to-br from-pink-500 to-rose-600 flex items-center justify-center shadow-lg ring-4 ring-pink-100">
    <span class="iconify text-white text-xl" data-icon="fa6-solid:play"></span>
  </div>
  <p class="text-xs font-bold text-gray-800 mt-2 text-center">Edit code → git add → git commit → git push</p>
</div>
</div>
</div>
      <p class="text-sm text-gray-600 leading-relaxed">The basic Git workflow looks like this:</p>
<p class="text-sm text-gray-600 leading-relaxed">Example workflow:</p>
    </div>'''

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Block 1: Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Every time you use Git, you follow the same repeatable path known as the <strong class="text-gray-800">stage &rarr; commit &rarr; push cycle</strong>: you edit files on your computer, tell Git exactly which changes to include, save a labeled snapshot, then upload it to GitHub &mdash; just like drafting a report, marking the sections worth keeping, printing a final version, and filing it away.</p>

      <!-- Block 2: Git workflow flowchart -->
      <div class="rounded-2xl border border-gray-100 bg-gray-50 px-5 pt-4 pb-6 overflow-x-auto">
        <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-4">How Git Saves Your Work &mdash; Step by Step</p>
        <div class="flex items-start gap-0 min-w-[640px]">

          <!-- Node 1: Edit Files (pink circle) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-full bg-gradient-to-br from-pink-500 to-rose-600 flex items-center justify-center shadow-lg ring-4 ring-pink-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:file-pen"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Edit<br>Files</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Your local working directory</p>
          </div>

          <!-- Arrow: pink → violet -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-pink-300 to-violet-300"></div>
            <span class="iconify text-violet-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 2: Stage Changes (violet rounded square) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center shadow-lg ring-4 ring-violet-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:layer-group"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Stage<br>Changes</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">git add &mdash; pick what to include</p>
          </div>

          <!-- Arrow: violet → blue -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-violet-300 to-blue-300"></div>
            <span class="iconify text-blue-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 3: Commit Ready? (blue diamond) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-12 h-12 rounded-xl rotate-45 bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-lg ring-4 ring-blue-100" style="margin-top:4px;">
              <span class="iconify text-white text-base -rotate-45" data-icon="fa6-solid:circle-question"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-3 text-center leading-tight">Commit<br>Ready?</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">git status &mdash; review staging</p>
          </div>

          <!-- Arrow: blue → emerald -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-blue-300 to-emerald-300"></div>
            <span class="iconify text-emerald-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 4: Save Snapshot (emerald rounded square) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg ring-4 ring-emerald-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:bookmark"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Save<br>Snapshot</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">git commit -m "message"</p>
          </div>

          <!-- Arrow: emerald → gray -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-emerald-300 to-gray-300"></div>
            <span class="iconify text-gray-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 5: Push to Remote (gray circle) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-full bg-gradient-to-br from-gray-400 to-gray-600 flex items-center justify-center shadow-lg ring-4 ring-gray-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:cloud-arrow-up"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Push to<br>Remote</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">GitHub receives your commits</p>
          </div>

        </div>
      </div>

      <!-- Block 3: Sub-heading + paragraph -->
      <div class="space-y-2">
        <p class="text-sm font-semibold text-gray-800">The Stage &rarr; Commit &rarr; Push Cycle &mdash; Every Time, In That Order</p>
        <p class="text-sm text-gray-600 leading-relaxed">After you edit a file, Git does not automatically save a version of your work. You must first run <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git add</code> to tell Git which changes to include, then <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git commit</code> to lock in a labeled snapshot, and finally <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git push</code> to upload that snapshot to GitHub. Skipping any step leaves your work either unsaved or unshared.</p>
      </div>

      <!-- Block 4: Code block (Style A — dark-chrome, no terminal pane) -->
      <div class="space-y-2">
        <p class="text-sm text-gray-600 leading-relaxed">Here is what the full cycle looks like in the terminal, starting from a folder that is already a Git repository:</p>
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">git_workflow.sh</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Step 1 — Check what files have changed
git status                       # shows modified and untracked files

# Step 2 — Stage the changes you want to include
git add report.py                # stage one specific file
git add .                        # or stage everything at once

# Step 3 — Save a snapshot with a clear, descriptive message
git commit -m "Add Q1 sales report script"   # locks in the snapshot

# Step 4 — Upload to GitHub so your team can access it
git push origin main             # sends all commits to the remote repository</code></pre>
          </div>
        </div>
      </div>

      <!-- Block 5: Three concept cards -->
      <div class="space-y-3">
        <p class="text-xs font-bold uppercase tracking-widest text-brand">The Three Commands That Drive the Git Cycle</p>
        <p class="text-sm text-gray-600 leading-relaxed">Each command plays a distinct role &mdash; swapping the order or skipping one will leave your work either unsaved or unshared with your team.</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <!-- Card 1: git add (blue) -->
          <div class="rounded-xl border border-blue-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-blue-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-blue-500 to-blue-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-blue-50 shrink-0">
                  <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:layer-group"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">git add</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">The staging area &mdash; what goes in?</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">Running <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git add</code> moves your changed files into the staging area &mdash; a holding zone where you decide which edits go into the next snapshot. Use <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git add .</code> to stage every change at once.</p>
            </div>
          </div>

          <!-- Card 2: git commit (emerald) -->
          <div class="rounded-xl border border-emerald-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-emerald-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-emerald-500 to-emerald-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-emerald-50 shrink-0">
                  <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:bookmark"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">git commit</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">The snapshot &mdash; locked in forever</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">Running <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git commit -m "message"</code> freezes everything in the staging area into a permanent, labeled snapshot. Write your message in the present tense and describe what changed, for example: <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">"Fix login form validation"</code>.</p>
            </div>
          </div>

          <!-- Card 3: git push (violet) -->
          <div class="rounded-xl border border-violet-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-violet-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-violet-500 to-violet-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-violet-50 shrink-0">
                  <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:cloud-arrow-up"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">git push</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">The upload &mdash; share your work</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">Running <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git push origin main</code> uploads your local commits to GitHub so your team can access them. Git only pushes committed snapshots &mdash; you must complete <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git add</code> and <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git commit</code> first.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- Block 6: Closing amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">The most common beginner mistake is editing files and then trying to jump straight to <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git push</code> without running <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git add</code> and <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git commit</code> first. Run <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git status</code> any time you are unsure where you are in the cycle &mdash; it tells you exactly what Git has noticed and what is still waiting to be staged or committed.</p>
      </div>

    </div>'''

def main():
    content = TARGET.read_text(encoding="utf-8")

    if OLD_BODY not in content:
        print("❌ OLD_BODY not found — check whitespace/indentation")
        # Show context around decision-flow to help debug
        idx = content.find('id="decision-flow"')
        if idx != -1:
            print("  Found section at char", idx)
            snippet = content[idx:idx+400]
            print("  Snippet:", repr(snippet[:200]))
        return

    new_content = content.replace(OLD_BODY, NEW_BODY, 1)
    TARGET.write_text(new_content, encoding="utf-8")
    print("✅ #decision-flow body replaced successfully")

    # Verification
    checks = [
        ('space-y-6 body wrapper',       'bg-white px-8 py-7 space-y-6'),
        ('flowchart container',           'How Git Saves Your Work'),
        ('node 1 — Edit Files',           'fa6-solid:file-pen'),
        ('node 2 — Stage (violet)',       'fa6-solid:layer-group'),
        ('node 3 — diamond decision',     'rotate-45'),
        ('node 4 — Save Snapshot',        'fa6-solid:bookmark'),
        ('node 5 — Push to Remote',       'fa6-solid:cloud-arrow-up'),
        ('section heading text',          'Stage &rarr; Commit &rarr; Push Cycle'),
        ('bash code block',               'language-bash'),
        ('git_workflow filename',         'git_workflow.sh'),
        ('card 1 — git add (blue)',       'border-blue-100'),
        ('card 2 — git commit (emerald)', 'border-emerald-100'),
        ('card 3 — git push (violet)',    'border-violet-100'),
        ('amber tip present',             'bg-amber-tip'),
        ('No traffic-light dots',         'w-2.5 h-2.5 rounded-full bg-red-400'),
    ]

    result = TARGET.read_text(encoding="utf-8")
    passed = failed = 0
    for label, needle in checks:
        if label == 'No traffic-light dots':
            # This check passes when the needle is NOT in the decision-flow section
            df_start = result.find('<section id="decision-flow">')
            df_end   = result.find('</section>', df_start) + len('</section>')
            section  = result[df_start:df_end]
            ok = needle not in section
        else:
            ok = needle in result
        status = "✅" if ok else "❌"
        if ok: passed += 1
        else:  failed += 1
        print(f"  {status} {label}")

    print(f"\n{'✅ All' if failed == 0 else '⚠️'} {passed}/{passed+failed} checks passed")

if __name__ == "__main__":
    main()
