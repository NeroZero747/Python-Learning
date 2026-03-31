"""Replace the #key-concepts section in lesson03 with the new 4-tab template structure."""

import re

TARGET = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01_python_foundation/mod_04_python_best_practices/lesson03_introduction_to_git_simple_workflow.html"

NEW_SECTION = '''<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Repository, commit, staging area, and remote — the four building blocks of Git.</p>
      </div>
    </div>

    <!-- Two-column layout: sidebar left, panel right -->
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar tabs ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <!-- Active indicator bar (desktop only) -->
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — Repository (pink, active) -->
          <button onclick="switchKcTab(0)"
            class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:book"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Repository</span>
          </button>

          <!-- Tab 1 — Commit (violet, inactive) -->
          <button onclick="switchKcTab(1)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:bookmark"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Commit</span>
          </button>

          <!-- Tab 2 — Staging Area (blue, inactive) -->
          <button onclick="switchKcTab(2)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:layer-group"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Staging Area</span>
          </button>

          <!-- Tab 3 — Remote / GitHub (emerald, inactive) -->
          <button onclick="switchKcTab(3)"
            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"
            role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:cloud-arrow-up"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Remote / GitHub</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Content panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ══════════════════════════════════════════════ -->
          <!-- Panel 0 — Repository (pink, ACTIVE)           -->
          <!-- ══════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:book"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Repository</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Your project's tracked home folder</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:folder-open"></span> repo
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>repository is the folder where Git watches your project</strong>. Run <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">git init</code> once inside your project folder and Git creates a hidden <code class="font-mono bg-pink-100 text-[#CB187D] border border-pink-200 px-1 rounded">.git</code> folder that records every change you make from that moment on.</p>

                <!-- Widget: rules-table — Repository conventions -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">Repository Rules</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">One repo per project</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">sales_project/</code>
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">web_app/</code> ✓
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Never commit secrets</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">.env</code> ✗ →
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">.gitignore</code>
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Use lowercase names</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">my-project</code> over
                          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">My Project</code>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block (bash) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Create a new folder for your project
mkdir my_project

# Move into that folder
cd my_project

# Tell Git to start tracking this folder
git init</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Run <code class="font-mono bg-pink-200 text-[#CB187D] border border-pink-300 px-1 rounded">git init</code> only once per project.</strong> A hidden <code class="font-mono bg-pink-200 text-[#CB187D] border border-pink-300 px-1 rounded">.git</code> folder will appear — this is where Git stores its entire history. Never delete it or you will lose all your saved snapshots.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ═══════════════════════════════════════════════ -->
          <!-- Panel 1 — Commit (violet, INACTIVE)            -->
          <!-- ═══════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:bookmark"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Commit</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">A saved snapshot of your project</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:camera"></span> snapshot
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>commit is a permanent snapshot of all your files</strong> at one moment in time. Every commit records what changed, who changed it, and when — like a dated entry in a project diary you can always return to.</p>

                <!-- Widget: operators-table — Git commit commands -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:terminal"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Commit Commands</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-violet-50">
                        <th class="py-2 px-3 text-left font-bold text-violet-600 w-36">Command</th>
                        <th class="py-2 px-3 text-left font-bold text-violet-600">What it does</th>
                        <th class="py-2 px-3 text-left font-bold text-violet-600">Result</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">git add .</code></td>
                        <td class="py-2 px-3 text-gray-500">Stage all changes</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">files ready to save</code></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">git commit -m</code></td>
                        <td class="py-2 px-3 text-gray-500">Save a snapshot</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">new entry in history</code></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">git log</code></td>
                        <td class="py-2 px-3 text-gray-500">View past commits</td>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-50 text-violet-700 border border-violet-200 px-1.5 py-0.5 rounded text-[10px]">list of snapshots</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block (bash) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Stage all changed files — prepare them to be saved
git add .

# Save a snapshot with a message describing what changed
git commit -m "Add revenue calculation function"

# View the list of commits you have made so far
git log --oneline</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Write commit messages in plain English.</strong> A good message finishes the sentence "This commit will…" — for example, <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">git commit -m "Fix total price rounding error"</code> tells your future self exactly what changed and why.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ═══════════════════════════════════════════════ -->
          <!-- Panel 2 — Staging Area (blue, INACTIVE)        -->
          <!-- ═══════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:layer-group"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Staging Area</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">The waiting room before a commit</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:box-archive"></span> stage
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <strong>staging area is a preparation zone between your files and a commit</strong>. You place files there with <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">git add</code>. Only staged files are included in your next commit, so you stay in full control of exactly what gets saved.</p>

                <!-- Widget: comparison-table — unstaged vs staged -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">Unstaged vs Staged</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-blue-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-gray-100 text-gray-700 border border-gray-200 text-[10px] font-bold">Unstaged</span>
                        </th>
                        <th class="py-2 px-3 text-left">
                          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">Staged</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Git sees it?</td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">✓</span> <span class="text-gray-400">Yes</span></td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">✓</span> <span class="text-gray-400">Yes</span></td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">In next commit?</td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">✗</span> <span class="text-gray-400">No</span></td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">✓</span> <span class="text-gray-400">Yes</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">How to get here</td>
                        <td class="py-2 px-3 text-gray-500">(edit a file)</td>
                        <td class="py-2 px-3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">git add</code></td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block (bash) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Check which files have changed since your last commit
git status

# Stage one specific file — only this file will be saved
git add analysis.py

# Stage every changed file at once
git add .</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong><code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">git add .</code> stages everything.</strong> If you only want to save one file, use <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">git add filename.py</code> instead — this keeps unfinished work out of your commit and makes your history easier to read.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ═══════════════════════════════════════════════ -->
          <!-- Panel 3 — Remote / GitHub (emerald, INACTIVE)  -->
          <!-- ═══════════════════════════════════════════════ -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:cloud-arrow-up"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Remote / GitHub</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Sharing your commits online</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:cloud"></span> remote
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>remote is an online copy of your repository</strong>, usually hosted on GitHub. After you commit locally, you use <code class="font-mono bg-emerald-100 text-emerald-700 border border-emerald-200 px-1 rounded">git push</code> to upload those commits so teammates can see and download your work.</p>

                <!-- Widget: comparison-strip — Local → git push → GitHub -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:arrows-left-right"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">Local to Remote</p>
                  </div>
                  <div class="flex gap-0 bg-white">
                    <!-- Local repo -->
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-emerald-50">
                      <code class="text-sm font-mono font-bold text-emerald-700 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded mb-1">Local Repo</code>
                      <span class="text-[10px] font-semibold text-emerald-600 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded-full">Your machine</span>
                    </div>
                    <!-- Separator -->
                    <div class="flex items-center justify-center px-3 text-emerald-300 text-base font-black">→</div>
                    <!-- git push -->
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-emerald-50">
                      <code class="text-sm font-mono font-bold text-emerald-700 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded mb-1">git push</code>
                      <span class="text-[10px] font-semibold text-emerald-600 bg-emerald-100 border border-emerald-200 px-2 py-0.5 rounded-full">Upload commits</span>
                    </div>
                    <!-- Separator -->
                    <div class="flex items-center justify-center px-3 text-emerald-300 text-base font-black">→</div>
                    <!-- GitHub result -->
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3">
                      <span class="iconify text-xl text-green-500 mb-1" data-icon="fa6-solid:cloud"></span>
                      <span class="text-[10px] font-bold text-green-700 bg-green-100 border border-green-200 px-2 py-0.5 rounded-full">GitHub ✓</span>
                    </div>
                  </div>
                </div>

                <!-- Code block (bash) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Link your local repo to a GitHub repository (one-time setup)
git remote add origin https://github.com/you/my_project.git

# Upload your commits to GitHub for the first time
git push -u origin main

# Upload subsequent commits after the first push
git push</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong><code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">git push</code> only uploads commits.</strong> Unsaved file edits stay on your machine until you run <code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">git add</code> and <code class="font-mono bg-emerald-200 text-emerald-800 border border-emerald-300 px-1 rounded">git commit</code> first — then push to share your work on GitHub.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->

      </div><!-- /flex row -->
    </div><!-- /section body -->

  </div>
</section>'''

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

# Match from <section id="key-concepts"> to the </section> that closes it.
# Use a regex that finds the section block non-greedily.
pattern = re.compile(
    r'<section id="key-concepts">.*?</section>',
    re.DOTALL
)

matches = list(pattern.finditer(content))
if len(matches) != 1:
    print(f'❌ Expected 1 match, found {len(matches)}')
    raise SystemExit(1)

new_content = pattern.sub(NEW_SECTION, content, count=1)

if new_content == content:
    print('⚠️  No change made — pattern may not have matched.')
    raise SystemExit(1)

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('✅ #key-concepts section replaced successfully.')

# Quick verification
with open(TARGET, 'r', encoding='utf-8') as f:
    verify = f.read()

checks = [
    ('4 kc-tab buttons', verify.count('class="kc-tab ') + verify.count('class="kc-tab\n') + verify.count('"kc-tab kc-tab-active') >= 4),
    ('Repository panel', 'Repository Rules' in verify),
    ('Commit panel (violet)', 'Commit Commands' in verify),
    ('Staging Area panel (blue)', 'Unstaged vs Staged' in verify),
    ('Remote panel (emerald)', 'Local to Remote' in verify),
    ('4 kc-panels', verify.count('class="kc-panel') >= 4),
    ('scroll-mt-24 on section', 'id="key-concepts" class="scroll-mt-24"' in verify),
    ('kc-indicator uses inline style', 'kc-indicator' in verify and 'background:#CB187D' in verify),
    ('inline style on active tab-num', 'style="background:#CB187D;color:#fff' in verify),
]

all_ok = True
for label, result in checks:
    icon = '✅' if result else '❌'
    if not result:
        all_ok = False
    print(f'  {icon} {label}')

if all_ok:
    print('\n✅ All verification checks passed.')
else:
    print('\n❌ Some checks failed — review the output above.')
