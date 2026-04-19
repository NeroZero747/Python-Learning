"""
_fix_lesson09_kc.py — Full rewrite of #key-concepts per lesson-key-concepts.prompt.md

Changes vs current file:
  - Section shell: px-6 py-7 (not px-8 py-7 space-y-6), scroll-mt-24 on <section>
  - kc-indicator: background via inline style (Confluence-safe)
  - Tab nums: inline style= only (not Tailwind bg/text/shadow classes)
  - Inactive tabs: inline style= only
  - Panel body: p-5 space-y-4 (not p-5 wrapping a space-y-3 div)
  - Header row: full spec pattern (icon chip + subtitle + type badge chip with gradient)
  - Definition: text-xs (not text-sm), bare <p> no wrapper div
  - Widget added to every panel
  - Tips: color-matched chip pattern (not amber bg-amber-tip)
  - Code pills: correct tier (-100 bg, -200 border in definition/widget; -200 bg, -300 border in tip)
  - kc-tab-num: rounded-full (already correct, maintaining)
  - CSS/JS: already present, left unchanged
"""

from pathlib import Path

TARGET = Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson09_pipeline_automation_deployment.html")
text = TARGET.read_text(encoding="utf-8")

# ─── Find section boundaries ──────────────────────────────────────────────────
START = '<section id="key-concepts">'
# Find end = closing </section> after the section start
start_idx = text.index(START)
# Find the matching </section> — it's the first one after the section starts
end_marker = '</section>'
# We need the </section> that closes key-concepts specifically.
# Scan for it after the section start position.
search_from = start_idx + len(START)
# Count nested <section> tags isn't needed — key-concepts has no nested sections.
# Find first </section> after start.
end_idx = text.index(end_marker, search_from) + len(end_marker)

OLD_KC = text[start_idx:end_idx]

NEW_KC = '''<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Cron syntax, Python scheduling, CI/CD config, deployment workflow, and monitoring.</p>
      </div>
    </div>

    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — active -->
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:clock"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Cron Syntax</span>
          </button>

          <!-- Tab 1 — inactive -->
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:terminal"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Python Scheduler</span>
          </button>

          <!-- Tab 2 — inactive -->
          <button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:code-branch"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">CI/CD YAML</span>
          </button>

          <!-- Tab 3 — inactive -->
          <button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:server"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Deployment Workflow</span>
          </button>

          <!-- Tab 4 — inactive -->
          <button onclick="switchKcTab(4)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:chart-line"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Monitoring &amp; Alerting</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- ── Panel 0 — Cron Syntax (pink) ── -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:clock"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Cron Syntax</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Five fields that define when a job fires</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:clock"></span> Syntax
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>cron expression</strong> is a five-field string that tells the scheduler exactly when to run a job. The fields are, in order: <code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">minute</code> <code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">hour</code> <code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">day-of-month</code> <code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">month</code> <code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">day-of-week</code>. Every cloud scheduler — Airflow, Kubernetes, GitHub Actions — reads this exact format.</p>

                <!-- Widget: rules-table — cron field reference -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:table-list"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">Common Cron Patterns</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/3"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">0 2 * * *</code></td>
                        <td class="py-2 px-3 text-gray-500">Every day at 02:00</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">0 */6 * * *</code></td>
                        <td class="py-2 px-3 text-gray-500">Every 6 hours</td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">0 2 * * 1</code></td>
                        <td class="py-2 px-3 text-gray-500">Every Monday at 02:00</td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded">*/15 * * * *</code></td>
                        <td class="py-2 px-3 text-gray-500">Every 15 minutes</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block (Style B) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Cron format: minute hour day-of-month month day-of-week
0  2  *  *  *   # Run at 02:00 every night
0  2  *  *  1   # Run at 02:00 on Monday only
*/30 * * * *    # Run every 30 minutes</code></pre>
                </div>

                <!-- Tip (pink) -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Always validate your cron expression</strong> before deploying. Use an online cron validator — it translates the expression into plain English so you can confirm it fires at the right time. <code class="font-mono bg-pink-200 text-pink-800 border border-pink-300 px-1 rounded">0 2 * * 1</code> means Monday at 02:00, not every minute on Monday.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- ── Panel 1 — Python Scheduler (violet) ── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:terminal"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Python Scheduler</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Schedule Python functions with APScheduler</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:cube"></span> Library
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><strong>APScheduler</strong> is a Python library that lets you schedule functions inside your application. It uses the same cron syntax you already know. The <code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1 rounded">BlockingScheduler</code> keeps the process running and fires your function at the scheduled time every day.</p>

                <!-- Widget: comparison-table — APScheduler vs OS cron -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-purple-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">APScheduler vs OS Cron</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-violet-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-violet-100 text-violet-700 border border-violet-200 text-[10px] font-bold">APScheduler</span></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-gray-100 text-gray-600 border border-gray-200 text-[10px] font-bold">OS Cron</span></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Lives in</td>
                        <td class="py-2 px-3 text-gray-500">Your Python app</td>
                        <td class="py-2 px-3 text-gray-500">The server OS</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Separate daemon?</td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">✗</span> <span class="text-gray-400">Not needed</span></td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">✓</span> <span class="text-gray-400">Yes, crond</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Best for</td>
                        <td class="py-2 px-3 text-gray-500">Bundled scheduling logic</td>
                        <td class="py-2 px-3 text-gray-500">Server-level tasks</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block (Style B) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">from apscheduler.schedulers.blocking import BlockingScheduler
import orders_pipeline                       # your pipeline module

scheduler = BlockingScheduler()

@scheduler.scheduled_job("cron", hour=2, minute=0)
def run_nightly():
    orders_pipeline.run()                    # runs every night at 02:00

scheduler.start()                            # keeps the process alive</code></pre>
                </div>

                <!-- Tip (violet) -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>APScheduler is great for short pipelines on a single server.</strong> For longer-running or multi-step workflows, consider a dedicated orchestrator like Apache Airflow. Both use <code class="font-mono bg-violet-200 text-violet-800 border border-violet-300 px-1 rounded">cron</code> syntax, so everything you learned here still applies.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- ── Panel 2 — CI/CD YAML (blue) ── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:code-branch"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">CI/CD YAML</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Pipeline-as-code using GitLab CI</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:file-code"></span> Config
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>CI/CD YAML file</strong> describes your pipeline stages in code stored alongside your source. Every <code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1 rounded">git push</code> triggers the file automatically. The <code class="font-mono bg-blue-100 text-blue-800 border border-blue-200 px-1 rounded">when: manual</code> flag adds a human approval step before production changes go live.</p>

                <!-- Widget: comparison-strip — GitLab CI vs GitHub Actions -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:arrows-left-right"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">GitLab CI vs GitHub Actions</p>
                  </div>
                  <div class="flex gap-0 bg-white">
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-blue-50">
                      <code class="text-sm font-mono font-bold text-blue-700 bg-blue-100 border border-blue-200 px-2 py-0.5 rounded mb-1">.gitlab-ci.yml</code>
                      <span class="text-[10px] font-semibold text-blue-600 bg-blue-100 border border-blue-200 px-2 py-0.5 rounded-full">GitLab CI</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-blue-300 text-base font-black">=</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-blue-50">
                      <code class="text-sm font-mono font-bold text-blue-700 bg-blue-100 border border-blue-200 px-2 py-0.5 rounded mb-1">.github/workflows/*.yml</code>
                      <span class="text-[10px] font-semibold text-blue-600 bg-blue-100 border border-blue-200 px-2 py-0.5 rounded-full">GitHub Actions</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-blue-300 text-base font-black">&rarr;</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3">
                      <span class="iconify text-xl text-green-500 mb-1" data-icon="fa6-solid:circle-check"></span>
                      <span class="text-[10px] font-bold text-green-700 bg-green-100 border border-green-200 px-2 py-0.5 rounded-full">Same concept</span>
                    </div>
                  </div>
                </div>

                <!-- Code block (Style B — Bash for YAML) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># .gitlab-ci.yml — stored at the root of your repo
stages: [test, deploy]

test-pipeline:
  stage: test                     # runs on every push
  script:
    - pip install -r requirements.txt
    - pytest tests/ -v            # blocks deploy if any test fails

deploy-production:
  stage: deploy
  when: manual                    # requires a click to promote to prod
  script:
    - python orders_pipeline.py
  variables:
    DB_URL: $PROD_DB_URL          # secret injected by CI/CD settings</code></pre>
                </div>

                <!-- Tip (blue) -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Never put secrets in your YAML file.</strong> Store database passwords and API keys as CI/CD variables in your platform's settings panel. Reference them in your YAML as <code class="font-mono bg-blue-200 text-blue-800 border border-blue-300 px-1 rounded">$VARIABLE_NAME</code>. The CI runner injects them at runtime — they never appear in your code history.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- ── Panel 3 — Deployment Workflow (emerald) ── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:server"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Deployment Workflow</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">develop → staging → production</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:diagram-project"></span> Pattern
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>deployment workflow</strong> is a fixed sequence of steps that every code change must pass through before reaching production. You push to <code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded">develop</code>, CI tests run, then the change promotes to <code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded">staging</code>, and only after sign-off does it go to <code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded">production</code>. This keeps bad code away from live data.</p>

                <!-- Widget: rules-table — workflow stages -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">Deployment Stages</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/3"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded">develop</code></td>
                        <td class="py-2 px-3 text-gray-500">Push here — triggers CI tests automatically</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded">staging</code></td>
                        <td class="py-2 px-3 text-gray-500">Runs full pipeline on copy of production data</td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded">production</code></td>
                        <td class="py-2 px-3 text-gray-500">Promoted manually after staging sign-off</td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded">git revert</code></td>
                        <td class="py-2 px-3 text-gray-500">Rolls back production in under 30 seconds</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block (Style B — Bash) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Step 1: push to develop — CI runs tests automatically
git add . &amp;&amp; git commit -m "fix: handle null region"
git push origin develop

# Step 2: after CI passes, merge to main (deploys to staging)
# Step 3: validate on staging, then approve production deploy

# If production breaks — rollback in 30 seconds:
git revert HEAD --no-edit &amp;&amp; git push origin main</code></pre>
                </div>

                <!-- Tip (emerald) -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Let staging run at least one full scheduled cycle</strong> before you promote to production. A silent data error caught in staging is far cheaper to fix than one discovered after a production run has written wrong data to your dashboards. One day of delay saves hours of cleanup.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

          <!-- ── Panel 4 — Monitoring & Alerting (amber) ── -->
          <div class="kc-panel kc-panel-anim hidden" data-color="amber" role="tabpanel">
            <div class="rounded-2xl border border-amber-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-amber-500 via-orange-400 to-red-300"></div>
              <div class="bg-gradient-to-br from-amber-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-line"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Monitoring &amp; Alerting</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Log runs, check health, alert on failure</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-amber-100 to-orange-100 text-amber-600 border border-amber-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:bell"></span> Pattern
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><strong>Monitoring</strong> is how you know your pipeline ran, succeeded, and loaded the expected number of rows. You write a status file after every run. A <code class="font-mono bg-amber-100 text-amber-800 border border-amber-200 px-1 rounded">/health</code> endpoint reads that file and returns <code class="font-mono bg-amber-100 text-amber-800 border border-amber-200 px-1 rounded">200 OK</code> or <code class="font-mono bg-amber-100 text-amber-800 border border-amber-200 px-1 rounded">503</code> depending on whether the last run was recent and successful.</p>

                <!-- Widget: rules-table — monitoring checklist -->
                <div class="rounded-xl overflow-hidden border border-amber-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-amber-50 to-orange-50 border-b border-amber-100">
                    <span class="iconify text-amber-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-amber-500">Monitoring Checklist</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Structured logging</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">timestamp + level + message</code>
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Row-count check</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">alert if rows == 0</code>
                        </td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Exit code</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">sys.exit(0)</code> success &nbsp;
                          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">sys.exit(1)</code> failure
                        </td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Stale check</td>
                        <td class="py-2 px-3 text-gray-500">
                          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">alert if last_run &gt; 25 h ago</code>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block (Style B — Python) -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import json
from datetime import datetime

def write_status(status: str, rows: int) -&gt; None:
    with open("pipeline_status.json", "w") as f:
        json.dump({
            "status":      status,                   # "success" or "failure"
            "rows_loaded": rows,                     # alert if this is 0
            "last_run":    datetime.now().isoformat() # used by /health endpoint
        }, f)</code></pre>
                </div>

                <!-- Tip (amber) -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-amber-50 border border-amber-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-amber-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Row-count monitoring is just as important as error monitoring.</strong> A pipeline that loads zero rows and exits with <code class="font-mono bg-amber-200 text-amber-800 border border-amber-300 px-1 rounded">sys.exit(0)</code> looks healthy to the scheduler but is silently broken. Always alert on unexpectedly low row counts, not only on exceptions.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 4 -->

        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>'''

assert OLD_KC in text, "Target KC section not found — check boundaries"
text = text.replace(OLD_KC, NEW_KC, 1)

TARGET.write_text(text, encoding="utf-8")
print("✅ #key-concepts rewritten per lesson-key-concepts.prompt.md spec")

# Verify div balance
opens  = text.count('<div')
closes = text.count('</div>')
print(f"   <div balance: {opens - closes} (should be 0)")

# Spot checks
import re
checks = [
    ('scroll-mt-24', 'section scroll-mt-24'),
    ('px-6 py-7', 'section body px-6 py-7'),
    ('style="height:68px;background:#CB187D;"', 'kc-indicator inline style'),
    ('style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"', 'active tab num inline style'),
    ('style="background:#f3f4f6;color:#9ca3af"', 'inactive tab inline style'),
    ('p-5 space-y-4', 'panel body p-5 space-y-4'),
    ('text-xs text-gray-600 leading-relaxed', 'definition text-xs'),
    ('bg-pink-200 text-pink-800 border border-pink-300', 'pink tip code pill -200/-300'),
    ('bg-violet-200 text-violet-800 border border-violet-300', 'violet tip code pill'),
    ('bg-blue-200 text-blue-800 border border-blue-300', 'blue tip code pill'),
    ('bg-amber-200 text-amber-800 border border-amber-300', 'amber tip code pill'),
    ('Common Cron Patterns', 'panel 0 widget'),
    ('APScheduler vs OS Cron', 'panel 1 widget'),
    ('GitLab CI vs GitHub Actions', 'panel 2 widget'),
    ('Deployment Stages', 'panel 3 widget'),
    ('Monitoring Checklist', 'panel 4 widget'),
    ('from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200', 'pink badge gradient'),
    ('from-violet-100 to-purple-100 text-violet-600 border border-violet-200', 'violet badge gradient'),
    ('from-blue-100 to-indigo-100 text-blue-600 border border-blue-200', 'blue badge gradient'),
    ('from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200', 'emerald badge gradient'),
    ('from-amber-100 to-orange-100 text-amber-600 border border-amber-200', 'amber badge gradient'),
]
all_pass = True
for needle, label in checks:
    found = needle in text
    status = '✅' if found else '❌'
    if not found:
        all_pass = False
    print(f"  {status} {label}")

if all_pass:
    print("\n✅ All spec checks passed.")
else:
    print("\n⚠️  Some checks failed — review above.")
