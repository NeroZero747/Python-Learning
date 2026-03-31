"""Merge VS Code content from lesson04 into lesson03, then update navigation."""

L03 = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)
L05 = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson05_logging_basics.html"
)


def apply(html, old, new, label):
    count = html.count(old)
    if count == 0:
        print(f"  ❌ {label}: old string NOT found")
        return html
    if count > 1:
        print(f"  ⚠️  {label}: {count} matches — skipping")
        return html
    print(f"  ✅ {label}")
    return html.replace(old, new, 1)


# ════════════════════════════════════════════════════════════════════════
# KEY CONCEPTS — Tab 4 button (VS Code)
# ════════════════════════════════════════════════════════════════════════

KC_TAB_OLD = (
    '            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Remote / GitLab</span>\n'
    "          </button>\n\n"
    "        </div><!-- /sidebar -->"
)

KC_TAB_NEW = (
    '            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Remote / GitLab</span>\n'
    "          </button>\n\n"
    "          <!-- Tab 4 — VS Code (sky, inactive) -->\n"
    '          <button onclick="switchKcTab(4)"\n'
    '            class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200"\n'
    '            role="tab">\n'
    '            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af">'
    '<span class="iconify text-[11px]" data-icon="fa6-solid:display"></span></span>\n'
    '            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">VS Code</span>\n'
    "          </button>\n\n"
    "        </div><!-- /sidebar -->"
)

# ════════════════════════════════════════════════════════════════════════
# KEY CONCEPTS — Panel 4 (VS Code)
# ════════════════════════════════════════════════════════════════════════

KC_PANEL_OLD = "          </div><!-- /panel 3 -->\n\n        </div><!-- /panels -->"

KC_PANEL_NEW = (
    "          </div><!-- /panel 3 -->\n\n"
    "          <!-- ══════════════════════════════════════════════ -->\n"
    "          <!-- Panel 4 — VS Code (sky, INACTIVE)             -->\n"
    "          <!-- ══════════════════════════════════════════════ -->\n"
    '          <div class="kc-panel kc-panel-anim hidden" data-color="sky" role="tabpanel">\n'
    '            <div class="rounded-2xl border border-sky-100 overflow-hidden">\n'
    '              <div class="h-1 bg-gradient-to-r from-sky-500 via-blue-400 to-cyan-300"></div>\n'
    '              <div class="bg-gradient-to-br from-sky-50/60 to-white p-5 space-y-4">\n\n'
    "                <!-- Header row -->\n"
    '                <div class="flex items-center justify-between">\n'
    '                  <div class="flex items-center gap-3">\n'
    '                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-sky-500 to-blue-600 shadow-md shrink-0">\n'
    '                      <span class="iconify text-white text-sm" data-icon="fa6-solid:display"></span>\n'
    "                    </span>\n"
    "                    <div>\n"
    '                      <h3 class="text-sm font-bold text-gray-900 leading-tight">VS Code</h3>\n'
    '                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Version control without the terminal</p>\n'
    "                    </div>\n"
    "                  </div>\n"
    '                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-sky-100 to-blue-100 text-sky-600 border border-sky-200 shadow-sm">\n'
    '                    <span class="iconify text-[10px]" data-icon="fa6-brands:git-alt"></span> Source Control\n'
    "                  </span>\n"
    "                </div>\n\n"
    "                <!-- Definition -->\n"
    '                <p class="text-xs text-gray-600 leading-relaxed">VS Code has a <strong>built-in Source Control panel</strong> that maps directly to the Git commands you have already learned. Instead of typing in a terminal, you stage by clicking a <strong>+</strong> icon, commit by typing a message and clicking <strong>&#x2713;</strong>, and push by clicking <strong>Sync Changes</strong> &mdash; every action runs the same Git operation underneath.</p>\n\n'
    "                <!-- Widget: equivalents table -->\n"
    '                <div class="rounded-xl overflow-hidden border border-sky-100">\n'
    '                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-sky-50 to-blue-50 border-b border-sky-100">\n'
    '                    <span class="iconify text-sky-500 text-xs" data-icon="fa6-solid:arrows-left-right"></span>\n'
    '                    <p class="text-[10px] font-bold uppercase tracking-widest text-sky-500">VS Code UI &#x2194; Terminal Equivalent</p>\n'
    "                  </div>\n"
    '                  <table class="w-full text-xs border-collapse bg-white">\n'
    "                    <tbody>\n"
    '                      <tr class="border-b border-gray-50">\n'
    '                        <td class="py-2 px-3 font-semibold text-gray-700 w-1/2">Click <strong>+</strong> next to a file</td>\n'
    '                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-sky-100 text-sky-700 border border-sky-200 px-1.5 py-0.5 rounded-full text-[10px]">git add filename</code></td>\n'
    "                      </tr>\n"
    '                      <tr class="border-b border-gray-50 bg-gray-50/50">\n'
    '                        <td class="py-2 px-3 font-semibold text-gray-700">Type message &#x2192; click &#x2713;</td>\n'
    '                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-sky-100 text-sky-700 border border-sky-200 px-1.5 py-0.5 rounded-full text-[10px]">git commit -m "msg"</code></td>\n'
    "                      </tr>\n"
    '                      <tr class="border-b border-gray-50">\n'
    '                        <td class="py-2 px-3 font-semibold text-gray-700">Click <strong>Sync Changes</strong></td>\n'
    '                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-sky-100 text-sky-700 border border-sky-200 px-1.5 py-0.5 rounded-full text-[10px]">git push</code></td>\n'
    "                      </tr>\n"
    '                      <tr class="bg-gray-50/50">\n'
    '                        <td class="py-2 px-3 font-semibold text-gray-700">Click a changed file</td>\n'
    '                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-sky-100 text-sky-700 border border-sky-200 px-1.5 py-0.5 rounded-full text-[10px]">git diff filename</code></td>\n'
    "                      </tr>\n"
    "                    </tbody>\n"
    "                  </table>\n"
    "                </div>\n\n"
    "                <!-- Code block (bash) — Style B -->\n"
    '                <div class="rounded-xl overflow-hidden bg-code shadow-md">\n'
    '                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">\n'
    '                    <div class="flex items-center gap-2">\n'
    '                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>\n'
    '                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>\n'
    "                    </div>\n"
    '                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">\n'
    '                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy\n'
    "                    </button>\n"
    "                  </div>\n"
    '                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Open your project folder in VS Code\n'
    "code sales_project/\n\n"
    "# VS Code detects the .git folder and activates the Source Control panel\n"
    "# The Source Control icon (&#x238B;) in the sidebar shows a badge: number of changed files\n\n"
    "# Gutter indicators appear next to changed lines inside each file:\n"
    "#   M  &mdash; Modified  (yellow bar beside the line number)\n"
    "#   A  &mdash; Added     (green bar)\n"
    "#   D  &mdash; Deleted   (red triangle)</code></pre>\n"
    "                </div>\n\n"
    "                <!-- Tip -->\n"
    '                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-sky-50 border border-sky-100">\n'
    '                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-sky-500 shrink-0 mt-0.5">\n'
    '                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>\n'
    "                  </span>\n"
    '                  <p class="text-xs text-gray-600"><strong>You still need the terminal once per project</strong> to run <code class="font-mono bg-sky-200 text-sky-800 border border-sky-300 px-1 rounded">git init</code> and <code class="font-mono bg-sky-200 text-sky-800 border border-sky-300 px-1 rounded">git remote add origin</code>. After that initial setup, every commit, push, and diff can be done entirely inside VS Code without reopening a terminal.</p>\n'
    "                </div>\n\n"
    "              </div>\n"
    "            </div>\n"
    "          </div><!-- /panel 4 -->\n\n"
    "        </div><!-- /panels -->"
)

# ════════════════════════════════════════════════════════════════════════
# CODE EXAMPLES — Tab 4 button (VS Code Workflow)
# ════════════════════════════════════════════════════════════════════════

CE_TAB_OLD = (
    '          <span class="ce-step-label text-xs font-bold">Push to GitLab</span>\n'
    "        </button>\n"
    "      </div>"
)

CE_TAB_NEW = (
    '          <span class="ce-step-label text-xs font-bold">Push to GitLab</span>\n'
    "        </button>\n"
    '        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">\n'
    '          <span class="iconify text-[13px]" data-icon="fa6-solid:display"></span>\n'
    '          <span class="ce-step-label text-xs font-bold">VS Code Workflow</span>\n'
    "        </button>\n"
    "      </div>"
)

# ════════════════════════════════════════════════════════════════════════
# CODE EXAMPLES — Panel 4 (VS Code Workflow) — Style A
# Insert before section body closes (unique boundary: section id="comparison")
# ════════════════════════════════════════════════════════════════════════

CE_PANEL_OLD = (
    "        </div>\n"
    "      </div>\n\n"
    "    </div>\n"
    "  </div>\n"
    "</section>\n\n"
    '<section id="comparison">'
)

CE_PANEL_NEW = (
    "        </div>\n"
    "      </div>\n\n"
    "      <!-- &#x2500;&#x2500; Panel 5 &#x2014; VS Code Workflow &#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500; -->\n"
    '      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">\n'
    '        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n\n'
    '          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
    '            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>\n'
    '            <div class="relative flex items-center gap-3">\n'
    '              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">\n'
    '                <span class="iconify text-base" data-icon="fa6-solid:display"></span>\n'
    "              </span>\n"
    "              <div>\n"
    '                <h3 class="font-bold text-gray-800">VS Code Workflow</h3>\n'
    '                <div class="flex items-center gap-2 mt-1">\n'
    '                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">\n'
    '                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner\n'
    "                  </span>\n"
    '                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Team Projects</span>\n'
    '                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">VS Code, Source Control</span>\n'
    "                </div>\n"
    "              </div>\n"
    "            </div>\n"
    "          </div>\n\n"
    '          <div class="px-6 py-5 space-y-4">\n'
    '            <div class="flex items-start gap-3 rounded-xl p-4 task-box">\n'
    '              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>\n'
    "              <div>\n"
    '                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>\n'
    '                <p class="text-sm text-gray-600">VS Code\'s Source Control panel replaces every terminal command you have been using. The <strong class="text-gray-800">+</strong> icon stages a file (<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">git add</code>), the text box with &#x2713; saves the commit (<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">git commit -m</code>), and Sync Changes pushes to GitLab (<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">git push</code>).</p>\n'
    "              </div>\n"
    "            </div>\n\n"
    '            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">\n'
    '              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
    '                <div class="flex items-center gap-3">\n'
    '                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
    '                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>\n'
    '                    <span class="text-[11px] font-semibold text-gray-400">vs_code_workflow.sh</span>\n'
    "                  </div>\n"
    "                </div>\n"
    '                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
    "              </div>\n"
    '              <div class="bg-code">\n'
    '                <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Step 1 &mdash; open your project in VS Code (one-time per session)\n'
    "code sales_project/\n"
    "# VS Code detects .git and activates the Source Control panel automatically\n\n"
    "# Step 2 &mdash; edit main.py\n"
    "# A yellow  M  appears in the editor gutter next to every changed line\n"
    "# The Source Control icon shows a badge: 1 changed file\n\n"
    "# Step 3 &mdash; stage the file  (replaces: git add main.py)\n"
    "# Click the  +  icon next to main.py in the Source Control panel\n"
    '# The file moves from "Changes" to "Staged Changes"\n\n'
    "# Step 4 &mdash; commit  (replaces: git commit -m \"Update revenue calc for Q2\")\n"
    "# Type your message in the text box at the top of the Source Control panel\n"
    "# Click the  &#x2713;  checkmark to save the snapshot\n\n"
    "# Step 5 &mdash; push to GitLab  (replaces: git push origin main)\n"
    "# Click  Sync Changes  at the top of the Source Control panel\n\n"
    "# Verify &mdash; check the commit history\n"
    "git log --oneline</code></pre>\n"
    "              </div>\n"
    '              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">\n'
    '                <div class="flex items-center gap-2 mb-1.5">\n'
    '                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>\n'
    '                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>\n'
    '                  <span class="text-[10px] text-gray-600 font-mono">$ bash vs_code_workflow.sh</span>\n'
    "                </div>\n"
    '                <div class="font-mono text-xs text-emerald-400 leading-relaxed">a1b2c3d Update revenue calc for Q2<br>e4f5g6h Initial commit</div>\n'
    "              </div>\n"
    "            </div>\n\n"
    '            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
    '              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
    '              <p class="text-sm text-gray-600">You only need the terminal to run <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git init</code> and <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">git remote add origin</code> once per project. After that, every commit and push can be done entirely from the VS Code Source Control panel.</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    "        </div>\n"
    "      </div>\n\n"
    "    </div>\n"
    "  </div>\n"
    "</section>\n\n"
    '<section id="comparison">'
)

# ════════════════════════════════════════════════════════════════════════
# PRACTICE — Tab 3 button (VS Code Source Control)
# ════════════════════════════════════════════════════════════════════════

PE_TAB_OLD = (
    '          <span class="pe-step-label text-xs font-bold">Push to GitLab</span>\n'
    "        </button>\n\n"
    "      </div>"
)

PE_TAB_NEW = (
    '          <span class="pe-step-label text-xs font-bold">Push to GitLab</span>\n'
    "        </button>\n\n"
    '        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">\n'
    '          <span class="iconify text-[13px]" data-icon="fa6-solid:display"></span>\n'
    '          <span class="pe-step-label text-xs font-bold">VS Code Source Control</span>\n'
    "        </button>\n\n"
    "      </div>"
)

# ════════════════════════════════════════════════════════════════════════
# PRACTICE — Panel 3 (VS Code Source Control exercise) — Style A
# Insert before section body closes (unique boundary: section id="mistakes")
# ════════════════════════════════════════════════════════════════════════

PE_PANEL_OLD = (
    "        </div>\n"
    "      </div>\n"
    "    </div>\n"
    "  </div>\n"
    "</section>\n\n"
    '<section id="mistakes">'
)

PE_PANEL_NEW = (
    "        </div>\n"
    "      </div>\n\n"
    "      <!-- 4 &#xB7; Exercise 4 &#x2014;&#x2014; VS Code Source Control -->\n"
    '      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">\n'
    '        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n\n'
    '          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
    '            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>\n'
    '            <div class="relative flex items-center gap-3">\n'
    '              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">\n'
    '                <span class="iconify text-base" data-icon="fa6-solid:display"></span>\n'
    "              </span>\n"
    "              <div>\n"
    '                <h3 class="font-bold text-gray-800">VS Code Source Control</h3>\n'
    '                <div class="flex items-center gap-2 mt-1">\n'
    '                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">\n'
    '                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner\n'
    "                  </span>\n"
    '                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>\n'
    '                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">VS Code, Git</span>\n'
    "                </div>\n"
    "              </div>\n"
    "            </div>\n"
    "          </div>\n\n"
    '          <div class="px-6 py-5 space-y-4">\n'
    '            <div class="flex items-start gap-3 rounded-xl p-4 task-box">\n'
    '              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>\n'
    "              <div>\n"
    '                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
    '                <p class="text-sm text-gray-600">Open your Reports folder in VS Code. Modify one line in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">report.py</code>, then use the Source Control panel &mdash; <strong>not the terminal</strong> &mdash; to stage the file, write a clear commit message, and commit. The gutter should show a yellow <strong>M</strong> before you stage and disappear once the commit is saved.</p>\n'
    "              </div>\n"
    "            </div>\n\n"
    '            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">\n'
    '              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
    '                <div class="flex items-center gap-3">\n'
    '                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
    '                    <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>\n'
    '                    <span class="text-[11px] font-semibold text-gray-400">open_vs_code.sh</span>\n'
    "                  </div>\n"
    "                </div>\n"
    '                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
    "              </div>\n"
    '              <div class="bg-code">\n'
    '                <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Open your Reports project in VS Code\n'
    "code reports/\n\n"
    "# In VS Code, edit report.py &mdash; add or change one line\n"
    "# A yellow  M  appears in the editor gutter next to the changed line\n\n"
    "# In the Source Control panel (&#x238B; icon in the sidebar):\n"
    "#   1. Click  +  next to report.py to stage it\n"
    "#   2. Type a message:  Update Q2 revenue figures in report\n"
    "#   3. Click  &#x2713;  to commit\n\n"
    "# The yellow M disappears &mdash; the snapshot is saved</code></pre>\n"
    "              </div>\n"
    "            </div>\n\n"
    '            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
    '              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
    '              <p class="text-sm text-gray-600">If the Source Control panel shows a badge number but the file list appears empty, click the refresh icon at the top of the panel. This happens occasionally when VS Code and Git detect the change at slightly different times.</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    "        </div>\n"
    "      </div>\n"
    "    </div>\n"
    "  </div>\n"
    "</section>\n\n"
    '<section id="mistakes">'
)

# ════════════════════════════════════════════════════════════════════════
# MISTAKES — Tab 3 button (Ignoring VS Code Indicators)
# ════════════════════════════════════════════════════════════════════════

MK_TAB_OLD = (
    '          <span class="mk-step-label text-xs font-bold">Commit \u2260 Shared</span>\n'
    "        </button>\n"
    "      </div>"
)

MK_TAB_NEW = (
    '          <span class="mk-step-label text-xs font-bold">Commit \u2260 Shared</span>\n'
    "        </button>\n"
    '        <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">\n'
    '          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
    '          <span class="mk-step-label text-xs font-bold">Ignoring VS Code Indicators</span>\n'
    "        </button>\n"
    "      </div>"
)

# ════════════════════════════════════════════════════════════════════════
# MISTAKES — Panel 3 (Ignoring VS Code Indicators)
# Insert before section body closes (unique boundary: "commit alone is never enough")
# ════════════════════════════════════════════════════════════════════════

MK_PANEL_OLD = (
    "a commit alone is never enough to share your work.</p>\n"
    "          </div>\n\n"
    "        </div>\n"
    "      </div>\n"
    "    </div>\n"
    "  </div>\n"
    "</section>\n\n"
    '<section id="real-world">'
)

MK_PANEL_NEW = (
    "a commit alone is never enough to share your work.</p>\n"
    "          </div>\n\n"
    "        </div>\n"
    "      </div>\n\n"
    "      <!-- Mistake 4 &#x2014;&#x2014; Ignoring VS Code Indicators -->\n"
    '      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">\n'
    '        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">\n\n'
    "          <!-- Card header -->\n"
    '          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">\n'
    '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">\n'
    '              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>\n'
    "            </span>\n"
    "            <div>\n"
    '              <h3 class="text-sm font-bold text-gray-800">Committing Without Reviewing VS Code Indicators</h3>\n'
    '              <p class="text-xs text-gray-400 mt-0.5">Always check the Source Control panel before staging or committing</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    "          <!-- Split panel -->\n"
    '          <div class="grid grid-cols-1 md:grid-cols-[1fr_auto_1fr] items-stretch">\n'
    "            <!-- Wrong -->\n"
    '            <div class="px-5 py-5 bg-red-50/30">\n'
    '              <p class="text-[10px] font-bold uppercase tracking-widest text-red-500 mb-3 flex items-center gap-1.5">\n'
    '                <span class="iconify text-[12px]" data-icon="fa6-solid:xmark"></span> What people do\n'
    "              </p>\n"
    '              <div class="rounded-xl overflow-hidden bg-code">\n'
    '                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash"># In VS Code Source Control panel:\n'
    "# Click &quot;Commit All&quot; without reviewing the list\n"
    "# VS Code stages and commits every changed file &mdash;\n"
    "# including .env, large data files, or\n"
    "# half-finished work you didn't intend to include</code></pre>\n"
    "              </div>\n"
    '              <p class="text-xs text-gray-500 mt-3 leading-relaxed">Clicking <strong>Commit All</strong> stages and commits <em>everything</em> that changed &mdash; including sensitive files like <code class="font-mono">.env</code> or edits you were not ready to save.</p>\n'
    "            </div>\n\n"
    "            <!-- Arrow divider -->\n"
    '            <div class="flex items-center justify-center px-3 py-5 bg-gray-50">\n'
    '              <span class="iconify text-gray-300 text-xl" data-icon="fa6-solid:arrow-right"></span>\n'
    "            </div>\n\n"
    "            <!-- Correct -->\n"
    '            <div class="px-5 py-5 bg-emerald-50/30">\n'
    '              <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-600 mb-3 flex items-center gap-1.5">\n'
    '                <span class="iconify text-[12px]" data-icon="fa6-solid:check"></span> What to do instead\n'
    "              </p>\n"
    '              <div class="rounded-xl overflow-hidden bg-code">\n'
    '                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-bash"># In VS Code Source Control panel:\n'
    "# 1. Click each changed file to open the diff viewer\n"
    "#    Green lines = added, red lines = removed\n"
    "# 2. Stage only intended files with the  +  icon\n"
    "# 3. Type a clear message and click  &#x2713;  to commit</code></pre>\n"
    "              </div>\n"
    '              <p class="text-xs text-gray-500 mt-3 leading-relaxed">Click each changed file to review its diff first. Then click <strong>+</strong> to stage only the files you meant to include. This habit prevents accidentally committing sensitive or unfinished code.</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    "          <!-- Amber tip -->\n"
    '          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">\n'
    '            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>\n'
    '            <p class="text-xs text-gray-600 leading-relaxed">Add a <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">.gitignore</code> file to your project listing files Git should never track &mdash; such as <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">.env</code>, <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">__pycache__/</code>, and large data exports. Even with a <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">.gitignore</code>, reviewing the Source Control panel before committing is a valuable habit.</p>\n'
    "          </div>\n\n"
    "        </div>\n"
    "      </div>\n"
    "    </div>\n"
    "  </div>\n"
    "</section>\n\n"
    '<section id="real-world">'
)

# ════════════════════════════════════════════════════════════════════════
# RECAP — Card 5 (VS Code) + update "4 key concepts" → "5 key concepts"
# ════════════════════════════════════════════════════════════════════════

RECAP_OLD = "      <!-- Completion banner -->"

RECAP_NEW = (
    "      <!-- Recap card 5 — VS Code -->\n"
    '      <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">\n'
    '        <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">\n'
    '          <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>\n'
    '          <div class="relative flex items-start gap-3">\n'
    '            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">\n'
    '              <span class="iconify text-sm" data-icon="fa6-solid:display"></span>\n'
    "            </span>\n"
    '            <p class="text-sm text-gray-700 font-medium leading-relaxed">VS Code\'s Source Control panel lets you stage, commit, and push without leaving the editor &mdash; every action maps directly to a Git command you already know.</p>\n'
    "          </div>\n"
    "        </div>\n"
    "      </div>\n\n"
    "      <!-- Completion banner -->"
)

RECAP_COUNTER_OLD = "You&#39;ve covered 4 key concepts."
RECAP_COUNTER_NEW = "You&#39;ve covered 5 key concepts."

# ════════════════════════════════════════════════════════════════════════
# HERO PILLS — update counts
# ════════════════════════════════════════════════════════════════════════

HERO_EX_OLD = (
    '<span class="font-extrabold">4</span>\n'
    '            <span class="font-semibold opacity-55">Examples</span>'
)
HERO_EX_NEW = (
    '<span class="font-extrabold">5</span>\n'
    '            <span class="font-semibold opacity-55">Examples</span>'
)

HERO_PE_OLD = (
    '<span class="font-extrabold">3</span>\n'
    '            <span class="font-semibold opacity-55">Exercises</span>'
)
HERO_PE_NEW = (
    '<span class="font-extrabold">4</span>\n'
    '            <span class="font-semibold opacity-55">Exercises</span>'
)

HERO_PROG_OLD = (
    '<span class="font-extrabold">4'
    '<span class="font-bold opacity-50">/5</span></span>'
)
HERO_PROG_NEW = (
    '<span class="font-extrabold">3'
    '<span class="font-bold opacity-50">/4</span></span>'
)

# ════════════════════════════════════════════════════════════════════════
# NEXT-LESSON section body — update to Logging Basics
# ════════════════════════════════════════════════════════════════════════

NEXT_BADGE_OLD = (
    '          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 4 · Lesson 4</p>\n'
    '          <h3 class="text-base font-bold text-gray-800">Git in VS Code</h3>'
)
NEXT_BADGE_NEW = (
    '          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 4 · Lesson 4</p>\n'
    '          <h3 class="text-base font-bold text-gray-800">Logging Basics</h3>'
)

NEXT_CARDS_OLD = (
    '              <p class="text-sm font-semibold text-gray-700">The Source Control Panel in VS Code</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
    '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
    '              <span class="iconify text-white text-sm" data-icon="fa6-solid:code-branch"></span>\n'
    "            </span>\n"
    "            <div>\n"
    '              <p class="text-sm font-semibold text-gray-700">Staging &amp; Committing With a Few Clicks</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
    '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
    '              <span class="iconify text-white text-sm" data-icon="fa6-solid:rotate-left"></span>\n'
    "            </span>\n"
    "            <div>\n"
    '              <p class="text-sm font-semibold text-gray-700">Undoing &amp; Reviewing Changes in the Editor</p>'
)
NEXT_CARDS_NEW = (
    '              <p class="text-sm font-semibold text-gray-700">What Python Logging Is &amp; When to Use It</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
    '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
    '              <span class="iconify text-white text-sm" data-icon="fa6-solid:list-ul"></span>\n'
    "            </span>\n"
    "            <div>\n"
    '              <p class="text-sm font-semibold text-gray-700">Log Levels: DEBUG, INFO, WARNING, ERROR</p>\n'
    "            </div>\n"
    "          </div>\n\n"
    '          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">\n'
    '            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">\n'
    '              <span class="iconify text-white text-sm" data-icon="fa6-solid:code"></span>\n'
    "            </span>\n"
    "            <div>\n"
    '              <p class="text-sm font-semibold text-gray-700">Setting Up a Logger in Your Script</p>'
)

# Card 1 icon was fa6-brands:git-alt, need to update that too
NEXT_ICON_OLD = '              <span class="iconify text-white text-sm" data-icon="fa6-brands:git-alt"></span>\n'
NEXT_ICON_NEW = '              <span class="iconify text-white text-sm" data-icon="fa6-solid:scroll"></span>\n'

# Bottom nav next link
NEXT_NAV_OLD = (
    '    <a href="lesson04_git_in_vs_code.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">\n'
    "      <div class=\"min-w-0\">\n"
    '        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>\n'
    '        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Git in VS Code</p>\n'
    "      </div>"
)
NEXT_NAV_NEW = (
    '    <a href="lesson05_logging_basics.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">\n'
    "      <div class=\"min-w-0\">\n"
    '        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>\n'
    '        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Logging Basics</p>\n'
    "      </div>"
)

# ════════════════════════════════════════════════════════════════════════
# MODULE TOC in lesson03 — remove lesson04 entry
# ════════════════════════════════════════════════════════════════════════

L03_TOC_OLD = (
    '<a href="lesson04_git_in_vs_code.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    "  <span class=\"truncate\">4. Git in VS Code</span>\n"
    "</a>\n"
    '<a href="lesson05_logging_basics.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    "  <span class=\"truncate\">5. Logging Basics</span>\n"
    "</a>"
)

L03_TOC_NEW = (
    '<a href="lesson05_logging_basics.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    "  <span class=\"truncate\">4. Logging Basics</span>\n"
    "</a>"
)

# ════════════════════════════════════════════════════════════════════════
# MODULE TOC in lesson05 — remove lesson04 entry
# ════════════════════════════════════════════════════════════════════════

L05_TOC_OLD = (
    '<a href="lesson04_git_in_vs_code.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    "  <span class=\"truncate\">4. Git in VS Code</span>\n"
    "</a>\n"
    '<a href="lesson05_logging_basics.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span>\n'
    "  <span class=\"truncate\">5. Logging Basics</span>\n"
    "</a>"
)

L05_TOC_NEW = (
    '<a href="lesson05_logging_basics.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span>\n'
    "  <span class=\"truncate\">4. Logging Basics</span>\n"
    "</a>"
)


# ════════════════════════════════════════════════════════════════════════
# APPLY ALL CHANGES
# ════════════════════════════════════════════════════════════════════════

def main():
    # ── Lesson 03 ──────────────────────────────────────────────────────
    with open(L03, encoding="utf-8") as f:
        html = f.read()

    print("\n── Lesson 03 ──────────────────────────────────────────────")
    html = apply(html, KC_TAB_OLD, KC_TAB_NEW, "KC tab 4 button: VS Code")
    html = apply(html, KC_PANEL_OLD, KC_PANEL_NEW, "KC panel 4: VS Code")
    html = apply(html, CE_TAB_OLD, CE_TAB_NEW, "CE tab 4 button: VS Code Workflow")
    html = apply(html, CE_PANEL_OLD, CE_PANEL_NEW, "CE panel 4: VS Code Workflow")
    html = apply(html, PE_TAB_OLD, PE_TAB_NEW, "PE tab 3 button: VS Code Source Control")
    html = apply(html, PE_PANEL_OLD, PE_PANEL_NEW, "PE panel 3: VS Code Source Control")
    html = apply(html, MK_TAB_OLD, MK_TAB_NEW, "MK tab 3 button: Ignoring VS Code Indicators")
    html = apply(html, MK_PANEL_OLD, MK_PANEL_NEW, "MK panel 3: Ignoring VS Code Indicators")
    html = apply(html, RECAP_OLD, RECAP_NEW, "Recap: card 5 (VS Code)")
    html = apply(html, RECAP_COUNTER_OLD, RECAP_COUNTER_NEW, "Recap: 4→5 key concepts")
    html = apply(html, HERO_EX_OLD, HERO_EX_NEW, "Hero: 4→5 Examples")
    html = apply(html, HERO_PE_OLD, HERO_PE_NEW, "Hero: 3→4 Exercises")
    html = apply(html, HERO_PROG_OLD, HERO_PROG_NEW, "Hero: 4/5→3/4 Progress")
    html = apply(html, NEXT_BADGE_OLD, NEXT_BADGE_NEW, "#next-lesson: badge title Logging Basics")
    html = apply(html, NEXT_ICON_OLD, NEXT_ICON_NEW, "#next-lesson: card 1 icon → scroll")
    html = apply(html, NEXT_CARDS_OLD, NEXT_CARDS_NEW, "#next-lesson: card titles → logging topics")
    html = apply(html, NEXT_NAV_OLD, NEXT_NAV_NEW, "Bottom nav next: lesson05_logging_basics")
    html = apply(html, L03_TOC_OLD, L03_TOC_NEW, "Module TOC: remove lesson04 entry")

    with open(L03, "w", encoding="utf-8") as f:
        f.write(html)

    # ── Lesson 05 ──────────────────────────────────────────────────────
    with open(L05, encoding="utf-8") as f:
        html = f.read()

    print("\n── Lesson 05 ──────────────────────────────────────────────")
    html = apply(html, L05_TOC_OLD, L05_TOC_NEW, "Module TOC: remove lesson04 entry")

    with open(L05, "w", encoding="utf-8") as f:
        f.write(html)

    # ── Quick verification ──────────────────────────────────────────────
    with open(L03, encoding="utf-8") as f:
        final = f.read()

    print("\n── Verification ───────────────────────────────────────────")
    checks = [
        ("KC has 5 tab buttons (switchKcTab 0-4)",   final.count("switchKcTab") == 5),
        ("KC has VS Code panel",                      'data-color="sky"' in final),
        ("CE has 5 tab buttons (switchCeTab 0-4)",   final.count("switchCeTab") == 5),
        ("CE has vs_code_workflow.sh",               "vs_code_workflow.sh" in final),
        ("PE has 4 tab buttons (switchPeTab 0-3)",   final.count("switchPeTab") == 4),
        ("PE has open_vs_code.sh",                   "open_vs_code.sh" in final),
        ("MK has 4 tab buttons (switchMkTab 0-3)",   final.count("switchMkTab") == 4),
        ("MK has VS Code indicator mistake",         "Ignoring VS Code Indicators" in final),
        ("Recap has 5 watermark cards",              ">05<" in final),
        ("Recap says 5 key concepts",                "covered 5 key concepts" in final),
        ("Hero shows 5 Examples",                    ">5</span>\n            <span class=\"font-semibold opacity-55\">Examples</span>" in final),
        ("Hero shows 4 Exercises",                   ">4</span>\n            <span class=\"font-semibold opacity-55\">Exercises</span>" in final),
        ("Next-lesson points to lesson05",           "lesson05_logging_basics.html" in final),
        ("Next-lesson title is Logging Basics",      "Logging Basics" in final),
        ("Module TOC has 4 entries (no lesson04)",   "lesson04_git_in_vs_code.html" not in final),
        ("Bottom nav Next points to lesson05",       'href="lesson05_logging_basics.html"' in final),
    ]

    with open(L05, encoding="utf-8") as f:
        l05 = f.read()
    checks.append(("L05 TOC has no lesson04 entry", "lesson04_git_in_vs_code.html" not in l05))
    checks.append(("L05 TOC shows lesson05 as #4",  "4. Logging Basics" in l05))

    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  {'✅' if ok else '❌'} {label}")
    print(f"\n{'✅' if passed == len(checks) else '⚠️'} {passed}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
