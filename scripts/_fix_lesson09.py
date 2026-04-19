"""
_fix_lesson09.py — Quality audit fixes for lesson09_pipeline_automation_deployment.html

Fixes applied:
  1. CSS:          Add obj-card-emerald:hover rule
  2. Overview:     Expand all 4 thin card explanations (text-xs -> text-xs with fuller text)
  3. Key Takeaways: Rewrite body — wrap cards in grid, fix px-6->px-5 + space-y-3 + bg-white,
                    fix text-xs->text-sm, add border to pills, add missing emerald card
  4. Key Concepts:  Rewrite section — add 2 new tabs + panels, fix header format,
                    add intro sentences + amber tips to all 5 panels
  5. TOC:           Add comparison link between code-examples and practice
  6. Comparison:    Insert full comparison section between code-examples and practice
  7. Knowledge Check: Add 4th question about monitoring
"""

from pathlib import Path

TARGET = Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson09_pipeline_automation_deployment.html")

text = TARGET.read_text(encoding="utf-8")
original = text  # keep for comparison


# ─── FIX 1: CSS — add obj-card-emerald:hover ─────────────────────────────────
OLD_CSS = '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }'
NEW_CSS = (
    '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }\n'
    '    .obj-card-emerald:hover { border-color: #059669; box-shadow: none; background-color: #ffffff; }'
)
assert OLD_CSS in text, "FIX 1: obj-card-blue:hover not found"
text = text.replace(OLD_CSS, NEW_CSS, 1)
print("✅ Fix 1: obj-card-emerald:hover added")


# ─── FIX 2: Overview card 1 — expand Scheduler explanation ───────────────────
OLD_OV1 = '    <p class="text-xs text-gray-500 leading-relaxed">Cron expressions define when jobs run. Every platform uses cron syntax.</p>'
NEW_OV1 = '    <p class="text-xs text-gray-500 leading-relaxed">A cron expression is a five-field string — minute, hour, day-of-month, month, day-of-week — that tells a scheduler exactly when to fire. Every cloud platform (Airflow, Kubernetes CronJob, GitHub Actions) uses this same syntax, so learning cron once works everywhere.</p>'
assert OLD_OV1 in text, "FIX 2a: overview card 1 text not found"
text = text.replace(OLD_OV1, NEW_OV1, 1)
print("✅ Fix 2a: Overview card 1 (Scheduler) expanded")

OLD_OV2 = '    <p class="text-xs text-gray-500 leading-relaxed">Automated test &rarr; build &rarr; deploy lifecycle triggered by git pushes.</p>'
NEW_OV2 = '    <p class="text-xs text-gray-500 leading-relaxed">Every time you push code, the CI server automatically runs your full test suite. If all tests pass, the CD step deploys the new version to the right environment — no manual copy-pasting, no forgotten steps, and a full git-history audit trail.</p>'
assert OLD_OV2 in text, "FIX 2b: overview card 2 text not found"
text = text.replace(OLD_OV2, NEW_OV2, 1)
print("✅ Fix 2b: Overview card 2 (CI/CD) expanded")

OLD_OV3 = '    <p class="text-xs text-gray-500 leading-relaxed">A copy of production where changes are tested safely before going live.</p>'
NEW_OV3 = '    <p class="text-xs text-gray-500 leading-relaxed">Staging uses the same code, database schema, and configuration as production but with separate data. You validate every change in staging before authorising it to go live — so a bad deploy never corrupts real records.</p>'
assert OLD_OV3 in text, "FIX 2c: overview card 3 text not found"
text = text.replace(OLD_OV3, NEW_OV3, 1)
print("✅ Fix 2c: Overview card 3 (Staging) expanded")

OLD_OV4 = '    <p class="text-xs text-gray-500 leading-relaxed">Structured logging, health checks, and alerts on failures or stale data.</p>'
NEW_OV4 = '    <p class="text-xs text-gray-500 leading-relaxed">Structured logs give you a timestamped, searchable record of every pipeline run, row count, and error. A health-check endpoint lets your monitoring system ask "did this job succeed?" on a schedule — and alert you the moment a run is late, empty, or failed.</p>'
assert OLD_OV4 in text, "FIX 2d: overview card 4 text not found"
text = text.replace(OLD_OV4, NEW_OV4, 1)
print("✅ Fix 2d: Overview card 4 (Monitoring) expanded")


# ─── FIX 3: Key Takeaways — full body replacement ────────────────────────────
OLD_KI_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">
<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:clock"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Cron Is the Universal Scheduler</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">0 2 * * * means &ldquo;at 02:00 every day.&rdquo; Every cloud platform and CI/CD tool uses cron syntax for scheduling.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border-pink-100">Cron</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border-pink-100">Schedule</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border-pink-100">0 2 * * *</span>
    </div>
  </div>
</div>
<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:code-branch"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">CI/CD Brings Engineering Discipline</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Push code &rarr; CI runs tests &rarr; CD deploys. You never manually copy code to production.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border-violet-100">Git push</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border-violet-100">CI tests</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border-violet-100">CD deploy</span>
    </div>
  </div>
</div>
<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:shield-halved"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Environments Separate Risk</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Staging is a safe copy of production. Changes go through staging first. Rolling back is a git revert, not a prayer.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border-blue-100">Staging</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border-blue-100">Production</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border-blue-100">Rollback</span>
    </div>
  </div>
</div>
    </div>
  </div>
</section>'''

NEW_KI_BODY = '''    <div class="bg-white px-8 py-7">
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:clock"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Cron Is the Universal Scheduler</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">A cron expression is a five-field string — minute, hour, day-of-month, month, day-of-week — that tells a scheduler exactly when to fire. Every cloud platform (Airflow, Kubernetes CronJob, GitHub Actions, GitLab CI) uses this same syntax, so cron is a skill you write once and use everywhere.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Cron</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Schedule</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">0 2 * * *</span>
    </div>
  </div>
</div>
<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:code-branch"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">CI/CD Brings Engineering Discipline</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Every git push to your main branch triggers the CI server to run your full test suite automatically. If all tests pass, the CD stage deploys the new version — no manual copying, no forgotten steps, and a full audit trail of exactly what changed and when.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Git push</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">CI tests</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">CD deploy</span>
    </div>
  </div>
</div>
<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:shield-halved"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Environments Separate Risk</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Staging is an exact mirror of production — same code, same database schema, different data — so you can validate a change works before it touches real records. If a deploy breaks production, a single <code>git revert</code> and push rolls it back in under a minute.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Staging</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Production</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Rollback</span>
    </div>
  </div>
</div>
<div class="obj-card obj-card-emerald rounded-2xl border border-emerald-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-line"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Monitoring Closes the Loop</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Structured logs give you a timestamped, searchable record of every pipeline run, row count, and error. A health-check endpoint lets your monitoring system poll "did the job succeed?" on a schedule — and send you an alert the moment a run is late, empty, or failed.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Logging</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Health checks</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Alerting</span>
    </div>
  </div>
</div>
</div>
    </div>
  </div>
</section>'''

assert OLD_KI_BODY in text, "FIX 3: key-ideas body not found"
text = text.replace(OLD_KI_BODY, NEW_KI_BODY, 1)
print("✅ Fix 3: Key Takeaways body rewritten (grid, fixes, emerald card added)")


# ─── FIX 4: Key Concepts — full section replacement ──────────────────────────
OLD_KC = '''<section id="key-concepts">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Core terms and definitions for this topic</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
<div class="flex flex-col md:flex-row gap-0">
  <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
    <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full bg-[#CB187D] transition-all duration-300" style="height:68px;"></div>
    <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-[#CB187D] text-white shadow-sm shadow-pink-200"><span class="iconify text-[11px]" data-icon="fa6-solid:clock"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Cron Syntax</span>
</button>
<button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:terminal"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Python Scheduler</span>
</button>
<button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:code-branch"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">CI/CD YAML</span>
</button>
  </div>
  <div class="flex-1 min-w-0 md:pl-5">
    <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
  <div class="rounded-2xl border border-pink-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
    <div class="bg-gradient-to-br from-pink-50/60 to-white p-5">
      <div class="mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">Cron Syntax</h3>
        <span class="text-[10px] font-bold text-#CB187D uppercase tracking-widest">Definition</span>
      </div>
      <div class="space-y-3">
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># minute hour day-of-month month day-of-week
0  2  *  *  *   # Every day at 02:00
0  */6 * *  *   # Every 6 hours
0  2  *  *  1   # Every Monday at 02:00
*/15 * * *  *   # Every 15 minutes</code></pre>
</div>
      </div>
    </div>
  </div>
</div>
<div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
  <div class="rounded-2xl border border-violet-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
    <div class="bg-gradient-to-br from-violet-50/60 to-white p-5">
      <div class="mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">APScheduler (Python)</h3>
        <span class="text-[10px] font-bold text-violet-500 uppercase tracking-widest">Definition</span>
      </div>
      <div class="space-y-3">
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Python</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-python">from apscheduler.schedulers.blocking import BlockingScheduler
import orders_pipeline

scheduler = BlockingScheduler()

@scheduler.scheduled_job(&quot;cron&quot;, hour=2, minute=0)
def run_nightly():
    orders_pipeline.run()

scheduler.start()</code></pre>
</div>
      </div>
    </div>
  </div>
</div>
<div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
  <div class="rounded-2xl border border-blue-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
    <div class="bg-gradient-to-br from-blue-50/60 to-white p-5">
      <div class="mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">GitLab CI/CD YAML</h3>
        <span class="text-[10px] font-bold text-blue-500 uppercase tracking-widest">Definition</span>
      </div>
      <div class="space-y-3">
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># .gitlab-ci.yml
stages: [test, deploy]

test-pipeline:
  stage: test
  script:
    - pip install -r requirements.txt
    - pytest tests/ -v

deploy-production:
  stage: deploy
  when: manual
  script:
    - python orders_pipeline.py
  variables:
    DB_URL: $PROD_DB_URL</code></pre>
</div>
      </div>
    </div>
  </div>
</div>
  </div>
</div>
    </div>
  </div>
</section>'''

NEW_KC = '''<section id="key-concepts">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Core terms and definitions for this topic</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
<div class="flex flex-col md:flex-row gap-0">
  <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
    <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full bg-[#CB187D] transition-all duration-300" style="height:68px;"></div>
    <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-[#CB187D] text-white shadow-sm shadow-pink-200"><span class="iconify text-[11px]" data-icon="fa6-solid:clock"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Cron Syntax</span>
</button>
<button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:terminal"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Python Scheduler</span>
</button>
<button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:code-branch"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">CI/CD YAML</span>
</button>
<button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:server"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Deployment Workflow</span>
</button>
<button onclick="switchKcTab(4)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:chart-line"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Monitoring &amp; Alerting</span>
</button>
  </div>
  <div class="flex-1 min-w-0 md:pl-5">
    <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
  <div class="rounded-2xl border border-pink-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
    <div class="bg-gradient-to-br from-pink-50/60 to-white p-5">
      <div class="flex items-center justify-between mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">Cron Syntax</h3>
        <span class="text-[10px] font-bold px-2 py-1 rounded-full bg-pink-50 text-[#CB187D] border border-pink-100 uppercase tracking-widest">Definition</span>
      </div>
      <div class="space-y-3">
        <p class="text-sm text-gray-600 leading-relaxed">A cron expression has five space-separated fields: <strong>minute &middot; hour &middot; day-of-month &middot; month &middot; day-of-week</strong>. An asterisk (<code>*</code>) means "every value"; a number means "only at this value"; <code>*/n</code> means "every n units". Mastering cron lets you schedule any pipeline on any platform.</p>
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># minute hour day-of-month month day-of-week
0  2  *  *  *   # Every day at 02:00
0  */6 * *  *   # Every 6 hours
0  2  *  *  1   # Every Monday at 02:00
*/15 * * *  *   # Every 15 minutes</code></pre>
</div>
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">Use an online cron expression validator to verify your schedules before deploying. They translate the expression into plain English so you can confirm it fires exactly when you intend — for example, <code>0 2 * * 1</code> means "Monday at 02:00", not "every minute on Monday".</p>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
  <div class="rounded-2xl border border-violet-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
    <div class="bg-gradient-to-br from-violet-50/60 to-white p-5">
      <div class="flex items-center justify-between mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">APScheduler (Python)</h3>
        <span class="text-[10px] font-bold px-2 py-1 rounded-full bg-violet-50 text-violet-600 border border-violet-100 uppercase tracking-widest">Library</span>
      </div>
      <div class="space-y-3">
        <p class="text-sm text-gray-600 leading-relaxed">APScheduler is a Python library that lets you schedule functions using cron-style rules directly in your application — no external cron daemon required. The <code>BlockingScheduler</code> keeps the process alive and fires <code>run_nightly()</code> at the specified time each day.</p>
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Python</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-python">from apscheduler.schedulers.blocking import BlockingScheduler
import orders_pipeline

scheduler = BlockingScheduler()

@scheduler.scheduled_job(&quot;cron&quot;, hour=2, minute=0)
def run_nightly():
    orders_pipeline.run()

scheduler.start()</code></pre>
</div>
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">For production pipelines on a server, the OS-level cron or a dedicated scheduler like Airflow is usually preferable. APScheduler is a great choice when you want scheduling logic bundled inside the Python application itself without a separate daemon process.</p>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
  <div class="rounded-2xl border border-blue-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
    <div class="bg-gradient-to-br from-blue-50/60 to-white p-5">
      <div class="flex items-center justify-between mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">GitLab CI/CD YAML</h3>
        <span class="text-[10px] font-bold px-2 py-1 rounded-full bg-blue-50 text-blue-600 border border-blue-100 uppercase tracking-widest">Config</span>
      </div>
      <div class="space-y-3">
        <p class="text-sm text-gray-600 leading-relaxed">A <code>.gitlab-ci.yml</code> file defines your pipeline stages in code. Each stage runs in a clean container, so "it worked on my machine" is never an excuse. The <code>when: manual</code> flag on the deploy stage adds a human approval gate before production changes go live.</p>
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># .gitlab-ci.yml
stages: [test, deploy]

test-pipeline:
  stage: test
  script:
    - pip install -r requirements.txt
    - pytest tests/ -v

deploy-production:
  stage: deploy
  when: manual
  script:
    - python orders_pipeline.py
  variables:
    DB_URL: $PROD_DB_URL</code></pre>
</div>
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">GitHub Actions uses an identical concept but stored in <code>.github/workflows/*.yml</code>. If you learn the GitLab YAML structure here, you can read and write GitHub Actions files with minimal adjustments — the concepts are the same, only the syntax differs slightly.</p>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
  <div class="rounded-2xl border border-emerald-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
    <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5">
      <div class="flex items-center justify-between mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">Deployment Workflow</h3>
        <span class="text-[10px] font-bold px-2 py-1 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-100 uppercase tracking-widest">Pattern</span>
      </div>
      <div class="space-y-3">
        <p class="text-sm text-gray-600 leading-relaxed">A safe deployment follows three steps: push to <code>develop</code> to trigger CI tests, merge to <code>main</code> which deploys to staging, then approve the promotion to production. If production breaks, <code>git revert HEAD</code> followed by a push rolls everything back in under a minute.</p>
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Bash</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># 1. Push to develop — CI tests run automatically
git add . &amp;&amp; git commit -m &quot;fix: handle null region&quot;
git push origin develop

# 2. After CI passes, merge to main &rarr; deploys to staging
# 3. After staging sign-off &rarr; promote to production

# If production breaks, revert in 30 seconds:
git revert HEAD --no-edit
git push origin main</code></pre>
</div>
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">Always deploy to staging first and let it run at least one full scheduled cycle before promoting to production. A silent data error caught in staging is far less damaging than one discovered after a production run has already written incorrect data to your dashboard.</p>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="kc-panel kc-panel-anim hidden" data-color="amber" role="tabpanel">
  <div class="rounded-2xl border border-amber-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-amber-500 via-orange-400 to-yellow-300"></div>
    <div class="bg-gradient-to-br from-amber-50/60 to-white p-5">
      <div class="flex items-center justify-between mb-3">
        <h3 class="text-sm font-bold text-gray-900 leading-tight">Monitoring &amp; Alerting</h3>
        <span class="text-[10px] font-bold px-2 py-1 rounded-full bg-amber-50 text-amber-600 border border-amber-100 uppercase tracking-widest">Pattern</span>
      </div>
      <div class="space-y-3">
        <p class="text-sm text-gray-600 leading-relaxed">After every pipeline run, write a status file with the result, row count, and timestamp. A <code>/health</code> endpoint reads this file and returns HTTP&nbsp;200 if the job succeeded within the last 25&nbsp;hours, or HTTP&nbsp;503 if it is stale or failed — which your monitoring platform can then alert on.</p>
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
    &quot;&quot;&quot;Write pipeline status for the health-check endpoint.&quot;&quot;&quot;
    with open(&quot;pipeline_status.json&quot;, &quot;w&quot;) as f:
        json.dump({
            &quot;status&quot;: status,       # &quot;success&quot; or &quot;failure&quot;
            &quot;rows_loaded&quot;: rows,
            &quot;last_run&quot;: datetime.now().isoformat()
        }, f)</code></pre>
</div>
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">Row-count monitoring is just as important as error monitoring. A pipeline that loads zero rows and exits with code 0 looks healthy to the scheduler but is silently broken. Always log and alert on unexpectedly low row counts alongside standard error conditions.</p>
        </div>
      </div>
    </div>
  </div>
</div>
  </div>
</div>
    </div>
  </div>
</section>'''

assert OLD_KC in text, "FIX 4: key-concepts section not found"
text = text.replace(OLD_KC, NEW_KC, 1)
print("✅ Fix 4: Key Concepts rewritten (5 tabs, intro sentences, amber tips, fixed headers)")


# ─── FIX 5: TOC — add comparison link after code-examples ────────────────────
OLD_TOC = '''<a href="#code-examples" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:code"></span> Code Examples
</a>
<a href="#practice" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">'''
NEW_TOC = '''<a href="#code-examples" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:code"></span> Code Examples
</a>
<a href="#comparison" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:scale-balanced"></span> Comparison
</a>
<a href="#practice" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">'''
assert OLD_TOC in text, "FIX 5: TOC code-examples->practice link not found"
text = text.replace(OLD_TOC, NEW_TOC, 1)
print("✅ Fix 5: TOC comparison link inserted")


# ─── FIX 6: Insert comparison section between code-examples and practice ─────
COMPARISON_SECTION = '''
<section id="comparison" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:scale-balanced"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Comparison</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Manual deployment vs CI/CD pipeline</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <p class="text-sm text-gray-600 leading-relaxed">Every data team eventually graduates from "I run it manually when I remember" to "it runs itself, guaranteed." The table below shows what that transition looks like in practice across the dimensions that matter most.</p>
      <div class="overflow-x-auto rounded-xl border border-gray-100">
        <table class="w-full text-sm">
          <thead>
            <tr class="border-b border-gray-100 bg-gray-50">
              <th class="text-left px-4 py-3 text-xs font-bold text-gray-500 uppercase tracking-widest w-1/4">Aspect</th>
              <th class="text-left px-4 py-3 text-xs font-bold text-red-400 uppercase tracking-widest">&#10007; Manual Deployment</th>
              <th class="text-left px-4 py-3 text-xs font-bold text-emerald-500 uppercase tracking-widest">&#10003; CI/CD Pipeline</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-50">
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-4 py-3 font-semibold text-gray-700 text-xs">Getting code to production</td>
              <td class="px-4 py-3 text-gray-500 text-xs">SSH into server, copy files, run the script by hand</td>
              <td class="px-4 py-3 text-emerald-700 text-xs">Git push triggers automated test &rarr; build &rarr; deploy</td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-4 py-3 font-semibold text-gray-700 text-xs">Test enforcement</td>
              <td class="px-4 py-3 text-gray-500 text-xs">Developer remembers to run tests &mdash; or doesn&rsquo;t</td>
              <td class="px-4 py-3 text-emerald-700 text-xs">Tests are mandatory; deploy is blocked if any fail</td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-4 py-3 font-semibold text-gray-700 text-xs">Audit trail</td>
              <td class="px-4 py-3 text-gray-500 text-xs">None &mdash; no record of who deployed what or when</td>
              <td class="px-4 py-3 text-emerald-700 text-xs">Full git history linked to every deployment event</td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-4 py-3 font-semibold text-gray-700 text-xs">Rollback</td>
              <td class="px-4 py-3 text-gray-500 text-xs">Re-copy old files manually &mdash; error-prone and slow</td>
              <td class="px-4 py-3 text-emerald-700 text-xs"><code>git revert HEAD &amp;&amp; git push</code> &mdash; under 30 seconds</td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-4 py-3 font-semibold text-gray-700 text-xs">Consistency</td>
              <td class="px-4 py-3 text-gray-500 text-xs">Every deploy is slightly different depending on who does it</td>
              <td class="px-4 py-3 text-emerald-700 text-xs">Identical automated steps every time, zero drift</td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
              <td class="px-4 py-3 font-semibold text-gray-700 text-xs">Runs while you sleep</td>
              <td class="px-4 py-3 text-gray-500 text-xs">No &mdash; someone must be available to trigger it manually</td>
              <td class="px-4 py-3 text-emerald-700 text-xs">Yes &mdash; the scheduler fires the job at 02:00 every day</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">You do not need to implement all of CI/CD on day one. Start with the scheduler (cron), add automated tests next, then automate the deploy step once the tests are reliable. Each improvement independently reduces your risk even before the full pipeline is in place.</p>
      </div>
    </div>
  </div>
</section>

'''

# Insert right before <section id="practice">
OLD_PRACTICE_ANCHOR = '\n<section id="practice">'
NEW_PRACTICE_ANCHOR = COMPARISON_SECTION + '<section id="practice">'
assert OLD_PRACTICE_ANCHOR in text, "FIX 6: practice section anchor not found"
text = text.replace(OLD_PRACTICE_ANCHOR, NEW_PRACTICE_ANCHOR, 1)
print("✅ Fix 6: Comparison section inserted before practice")


# ─── FIX 7: Knowledge Check — add 4th question ───────────────────────────────
OLD_QZ_TABS = '''<div class="flex items-center gap-2 mb-6" role="tablist"><button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 1</span></button>
<button onclick="switchQzTab(1)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 2</span></button>
<button onclick="switchQzTab(2)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 3</span></button></div>'''

NEW_QZ_TABS = '''<div class="flex items-center gap-2 mb-6" role="tablist"><button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 1</span></button>
<button onclick="switchQzTab(1)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 2</span></button>
<button onclick="switchQzTab(2)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 3</span></button>
<button onclick="switchQzTab(3)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 4</span></button></div>'''

assert OLD_QZ_TABS in text, "FIX 7a: quiz tab list not found"
text = text.replace(OLD_QZ_TABS, NEW_QZ_TABS, 1)

# Insert 4th panel before the closing </div> of the knowledge-check body
OLD_QZ_END = '''    </div>
  </div>
</section>

<section id="next-lesson"'''

NEW_QZ_END = '''<div class="qz-panel qz-panel-anim hidden" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q4</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Question 4</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q3">
        <p class="text-sm font-semibold text-gray-800 mb-4">Monitoring row counts is just as important as monitoring for errors, because a pipeline can load zero rows and still exit successfully. True or False?</p>
        <div class="flex gap-3">
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
            </button>
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
            </button>
        </div>
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>
    </div>
  </div>
</section>

<section id="next-lesson"'''

assert OLD_QZ_END in text, "FIX 7b: quiz end anchor not found"
text = text.replace(OLD_QZ_END, NEW_QZ_END, 1)
print("✅ Fix 7: Knowledge Check 4th question added")


# ─── Write output ─────────────────────────────────────────────────────────────
TARGET.write_text(text, encoding="utf-8")
print(f"\n✅ All fixes applied. File saved: {TARGET}")
print(f"   Original size: {len(original):,} chars")
print(f"   New size:      {len(text):,} chars")
print(f"   Delta:         +{len(text) - len(original):,} chars")
