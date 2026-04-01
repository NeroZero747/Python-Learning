#!/usr/bin/env python3
"""
Rewrite <section id="mistakes"> for all 4 lessons in
track_03 / mod_06_automation_and_ci_cd.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_03_data_engineering" / "mod_06_automation_and_ci_cd"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

LESSONS = {
    # ── Lesson 01: DevOps Concepts ──
    "lesson01_devops_concepts_for_data_analytics.html": {
        "topic": "DevOps concepts for data teams",
        "mistakes": [
            {
                "tab": "Manual Deployment Steps",
                "title": "Deploying by Manually Copying Files to the Server",
                "subtitle": "Manual steps are slow, error-prone, and impossible to reproduce reliably.",
                "explanation": 'Copying scripts to a server via FTP or drag-and-drop skips version control, testing, and logging. If something goes wrong, there is no record of what changed. Automate deployments through a CI/CD pipeline so every change is versioned, tested, and traceable.',
                "wrong_label": "manual copy",
                "wrong_code": '# SCP the script to the server by hand\n# scp pipeline.py user@server:/opt/scripts/\n# no test, no version, no rollback',
                "correct_label": "automated pipeline",
                "correct_code": '# .gitlab-ci.yml\ndeploy:\n  stage: deploy\n  script:\n    - scp pipeline.py user@server:/opt/scripts/\n  only:\n    - main  # runs only after tests pass on main',
                "tip": "If you are typing the same deployment commands more than once, wrap them in a CI/CD pipeline. Automation removes the chance of human error.",
            },
            {
                "tab": "Skipping Tests in CI",
                "title": "Setting Up a Pipeline Without an Automated Test Stage",
                "subtitle": "A pipeline that only deploys without testing pushes bugs straight to production.",
                "explanation": 'The whole point of CI/CD is the automated safety net. A pipeline that runs <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">deploy</code> without a preceding <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">test</code> stage is just automated risk. Always include a test job that must pass before deployment.',
                "wrong_label": "deploy-only pipeline",
                "wrong_code": '# .gitlab-ci.yml\nstages:\n  - deploy          # no test stage!\ndeploy:\n  stage: deploy\n  script:\n    - python deploy.py',
                "correct_label": "test then deploy",
                "correct_code": '# .gitlab-ci.yml\nstages:\n  - test\n  - deploy\ntest:\n  stage: test\n  script:\n    - pytest tests/\ndeploy:\n  stage: deploy\n  script:\n    - python deploy.py',
                "tip": "Even one basic test is better than none. A test stage that runs <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pytest</code> catches import errors, syntax mistakes, and assertion failures before deployment.",
            },
            {
                "tab": "No Version Control",
                "title": "Running Data Scripts Without Keeping Them in Version Control",
                "subtitle": "Without Git, you cannot track changes, roll back, or collaborate safely.",
                "explanation": 'Scripts saved only on a local machine or a shared drive have no history. If a change breaks the pipeline, you cannot see what changed or revert to the working version. Store all code in a Git repository from day one.',
                "wrong_label": "no Git",
                "wrong_code": '# pipeline.py saved on desktop\n# edited directly → old version lost\n# no way to see what changed yesterday',
                "correct_label": "Git-tracked",
                "correct_code": '# git init → git add → git commit\ngit add pipeline.py\ngit commit -m "Add daily sales pipeline"\n# full history preserved and shareable',
                "tip": "Version control is the foundation of DevOps. Every other practice — CI/CD, testing, code review — depends on having code in a Git repository.",
            },
        ],
    },

    # ── Lesson 02: GitLab CI/CD Overview ──
    "lesson02_gitlab_ci_cd_overview.html": {
        "topic": "GitLab CI/CD pipelines",
        "mistakes": [
            {
                "tab": "Wrong YAML Indentation",
                "title": "Using Tabs or Incorrect Indentation in .gitlab-ci.yml",
                "subtitle": "YAML is indentation-sensitive — tabs cause parse errors and the pipeline fails to start.",
                "explanation": 'YAML requires spaces (not tabs) and consistent indentation levels. A single misplaced space or tab causes <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">yaml.scanner.ScannerError</code> and the entire pipeline refuses to run. Use your editor\'s YAML mode to catch issues before pushing.',
                "wrong_label": "mixed indentation",
                "wrong_code": "stages:\n  - test\n  - deploy\ntest:\n\tstage: test        # tab instead of spaces!\n\tscript:\n\t\t- pytest tests/",
                "correct_label": "consistent 2-space indent",
                "correct_code": "stages:\n  - test\n  - deploy\ntest:\n  stage: test\n  script:\n    - pytest tests/",
                "tip": "Configure your editor to insert spaces when you press Tab in YAML files. Most editors have a per-language setting for this.",
            },
            {
                "tab": "Missing Stage Declaration",
                "title": "Defining a Job Without Declaring Its Stage in the stages List",
                "subtitle": "GitLab ignores jobs whose stage is not in the top-level stages list.",
                "explanation": 'Every <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">stage:</code> value used by a job must appear in the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">stages:</code> list at the top of the file. If you define a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">deploy</code> job but forget to list <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">deploy</code> in <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">stages:</code>, the job is skipped silently.',
                "wrong_label": "missing stage",
                "wrong_code": "stages:\n  - test\n  # deploy not listed!\ndeploy:\n  stage: deploy      # skipped silently\n  script:\n    - python deploy.py",
                "correct_label": "all stages listed",
                "correct_code": "stages:\n  - test\n  - deploy          # now listed\ndeploy:\n  stage: deploy\n  script:\n    - python deploy.py",
                "tip": "After adding a new job, check that its <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">stage:</code> value appears in the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">stages:</code> list. A quick Ctrl+F saves debugging time.",
            },
            {
                "tab": "Secrets in the YAML File",
                "title": "Hardcoding Passwords or API Keys Directly in .gitlab-ci.yml",
                "subtitle": "The YAML file is committed to Git — anyone with repo access can see the secrets.",
                "explanation": 'Credentials in a committed file are exposed to every developer and remain in the Git history even after deletion. Use GitLab CI/CD Variables (Settings → CI/CD → Variables) to pass secrets securely at runtime.',
                "wrong_label": "hardcoded secret",
                "wrong_code": "deploy:\n  stage: deploy\n  script:\n    - export DB_PASS=\"s3cret!\"   # visible in Git history\n    - python deploy.py",
                "correct_label": "CI/CD variable",
                "correct_code": "# DB_PASS set in GitLab Settings → CI/CD → Variables\ndeploy:\n  stage: deploy\n  script:\n    - python deploy.py   # reads $DB_PASS at runtime",
                "tip": "Never commit secrets to Git — even in private repositories. Use CI/CD variables with the \"Masked\" and \"Protected\" flags enabled.",
            },
        ],
    },

    # ── Lesson 03: Scheduling Data Jobs ──
    "lesson03_scheduling_data_jobs.html": {
        "topic": "scheduling data jobs",
        "mistakes": [
            {
                "tab": "Wrong Cron Syntax",
                "title": "Writing an Invalid Cron Expression That Never Fires",
                "subtitle": "A typo in a cron field means the job silently never runs.",
                "explanation": 'Cron expressions have five fields: minute, hour, day-of-month, month, day-of-week. Mixing up the order or using invalid values (e.g. <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">60</code> for minutes) means the job is registered but never triggered. Validate your expression with an online cron tool before deploying.',
                "wrong_label": "invalid cron",
                "wrong_code": '# crontab\n60 8 * * *  python /opt/pipeline.py\n# 60 is not a valid minute — job never fires',
                "correct_label": "valid cron",
                "correct_code": '# crontab\n0 8 * * *  python /opt/pipeline.py\n# runs at 08:00 every day',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">crontab.guru</code> to validate your cron expression before deploying. It shows you exactly when the next run will be.",
            },
            {
                "tab": "No Logging",
                "title": "Running Scheduled Jobs Without Capturing Output or Logs",
                "subtitle": "When the job fails at 3 AM, there is no record of what went wrong.",
                "explanation": 'Scheduled jobs run unattended. Without logging, a failure produces no evidence. Redirect output to a log file and include timestamps so you can diagnose issues the next morning.',
                "wrong_label": "no logging",
                "wrong_code": '# crontab\n0 8 * * *  python /opt/pipeline.py\n# output goes nowhere — errors are lost',
                "correct_label": "log output",
                "correct_code": '# crontab\n0 8 * * *  python /opt/pipeline.py >> /var/log/pipeline.log 2>&1',
                "tip": "Always redirect both stdout and stderr (<code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">2>&1</code>) to a log file. Add timestamps inside your Python script with <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">logging</code>.",
            },
            {
                "tab": "Overlapping Runs",
                "title": "Scheduling a Job More Frequently Than It Takes to Complete",
                "subtitle": "Two copies of the same job running simultaneously can corrupt data.",
                "explanation": 'If your pipeline takes 45 minutes but runs every 30 minutes, the second run starts before the first finishes. Both write to the same tables or files, causing duplicate rows or lock conflicts. Either increase the interval or add a lock mechanism.',
                "wrong_label": "overlapping schedule",
                "wrong_code": '# crontab — runs every 30 min, but job takes 45 min\n*/30 * * * *  python /opt/pipeline.py\n# two copies running simultaneously',
                "correct_label": "safe interval",
                "correct_code": '# crontab — runs every 60 min (> 45 min runtime)\n0 * * * *  python /opt/pipeline.py',
                "tip": "Time your job on real data to find out how long it takes. Set the schedule interval to at least 1.5 times the worst-case runtime.",
            },
        ],
    },

    # ── Lesson 05: Deployment Workflow ──
    "lesson05_deployment_workflow.html": {
        "topic": "deployment workflows",
        "mistakes": [
            {
                "tab": "Skipping Staging",
                "title": "Deploying Directly to Production Without a Staging Environment",
                "subtitle": "Bugs appear in production instead of being caught in a safe test environment.",
                "explanation": 'A staging environment mirrors production but has no real users. Deploying there first lets you catch configuration errors, missing environment variables, and data issues before they affect anyone. Skipping staging means your users are your testers.',
                "wrong_label": "straight to production",
                "wrong_code": '# .gitlab-ci.yml\ndeploy:\n  stage: deploy\n  script:\n    - python deploy.py --env production\n  # no staging step — bugs go live',
                "correct_label": "staging first",
                "correct_code": '# .gitlab-ci.yml\nstaging:\n  stage: staging\n  script:\n    - python deploy.py --env staging\nproduction:\n  stage: deploy\n  script:\n    - python deploy.py --env production\n  when: manual   # requires approval',
                "tip": "Even a minimal staging environment — a separate database and server — catches 90% of deployment issues. Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">when: manual</code> for the production stage so it requires explicit approval.",
            },
            {
                "tab": "No Rollback Plan",
                "title": "Deploying Without a Plan to Revert if Something Goes Wrong",
                "subtitle": "A failed deployment with no rollback means downtime until the bug is fixed.",
                "explanation": 'Every deployment should have a rollback plan: a way to return to the last working version in minutes. Tag your releases in Git so you can redeploy any previous version. Without tags, you are debugging under pressure with users waiting.',
                "wrong_label": "no rollback",
                "wrong_code": '# deploy new version → it breaks\n# "which commit was the last working one?"\n# scramble to find and fix the bug',
                "correct_label": "tagged releases",
                "correct_code": '# tag before deploying\ngit tag v2.1.0\ngit push origin v2.1.0\n# if v2.1.0 fails → redeploy v2.0.0\ngit checkout v2.0.0\npython deploy.py',
                "tip": "Tag every release with a version number. If the deployment fails, redeploying the previous tag is a one-command operation.",
            },
            {
                "tab": "Env Variables Missing",
                "title": "Forgetting to Set Environment Variables in the Target Environment",
                "subtitle": "The code works locally but crashes in production because a variable is not set.",
                "explanation": 'Environment variables like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">DATABASE_URL</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">API_KEY</code> are set on your laptop but not on the server. The script starts, fails immediately with a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">KeyError</code>, and the pipeline breaks. Check for required variables at startup.',
                "wrong_label": "no env check",
                "wrong_code": 'import os\ndb_url = os.environ["DATABASE_URL"]  # KeyError in production\n# script crashes before doing any work',
                "correct_label": "check at startup",
                "correct_code": 'import os, sys\nrequired = ["DATABASE_URL", "API_KEY"]\nmissing = [v for v in required if v not in os.environ]\nif missing:\n    print(f"Missing env vars: {missing}")\n    sys.exit(1)',
                "tip": "Add a startup check that validates all required environment variables before any real work begins. A clear error message beats a cryptic <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">KeyError</code> traceback.",
            },
        ],
    },
}


# ── HTML builders ──────────────────────────────────────────────────────

def _tab_btn(index: int, label: str, *, active: bool) -> str:
    if active:
        cls = (
            'mk-step mk-step-active flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
            'text-white shadow-lg shadow-pink-200/50 transition-all duration-250'
        )
    else:
        cls = (
            'mk-step flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gray-800 text-gray-400 transition-all duration-250'
        )
    return (
        f'<button onclick="switchMkTab({index})" '
        f'class="{cls}" role="tab">\n'
        f'  <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
        f'  <span class="mk-step-label text-xs font-bold">{label}</span>\n'
        f'</button>'
    )


def _panel(mk: dict, *, hidden: bool) -> str:
    hide = " hidden" if hidden else ""
    return f'''\
<div class="mk-panel mk-panel-anim{hide}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

    <!-- Card header -->
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["subtitle"]}</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>

    <!-- Explanation paragraph -->
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">{mk["explanation"]}</p>
    </div>

    <!-- Wrong / Correct split panel -->
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong \u2014 {mk["wrong_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["wrong_code"]}</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct \u2014 {mk["correct_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["correct_code"]}</code></pre>
        </div>
      </div>
    </div>

    <!-- Amber tip footer -->
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["tip"]}</p>
    </div>

  </div>
</div>'''


def build_section(topic: str, mistakes: list[dict]) -> str:
    tabs = "\n".join(
        _tab_btn(i, m["tab"], active=(i == 0))
        for i, m in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{tabs}\n</div>'

    panels = "\n\n".join(
        _panel(m, hidden=(i > 0))
        for i, m in enumerate(mistakes)
    )

    body = f'{tab_row}\n\n{panels}'

    return f'''\
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with {topic}</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

{body}

    </div>
  </div>
</section>'''


# ── Main ───────────────────────────────────────────────────────────────

ok = fail = 0
for filename, lesson in LESSONS.items():
    path = MOD / filename
    if not path.exists():
        print(f"\u274c NOT FOUND  {filename}")
        fail += 1
        continue

    text = path.read_text(encoding="utf-8")
    replacement = build_section(lesson["topic"], lesson["mistakes"])
    new_text, n = SECTION_RE.subn(replacement, text, count=1)

    if n == 0:
        print(f"\u274c NO MATCH   {filename}")
        fail += 1
        continue

    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {filename}")
    ok += 1

print(f"\n{ok}/{ok + fail} mistakes sections rewritten")
