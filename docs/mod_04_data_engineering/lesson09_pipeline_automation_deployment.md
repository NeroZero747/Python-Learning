# Lesson 09 — Pipeline Automation & Deployment

**Track:** Data Engineering for Analysts  
**Module:** Module 4 — Production Engineering  
**Difficulty:** Intermediate → Advanced | **Duration:** 14 min  
**Sources:** M4-L04 (Working with Large Data Files) · M4-L05 (Data Validation — covered in L08) · M4-L09 (Scheduling) · M4-L10 (Building a Simple Python Pipeline) · M4-L11 (Automating Ingestion) · M4-L12 (Data Quality Checks — in L08) · M4-L13 (Database Loading) · M4-L14 (Production Architecture — trimmed) · M6-L01 (DevOps Concepts) · M6-L02 (GitLab CI/CD Overview) · M6-L03 (Scheduling Data Jobs) · M6-L05 (Deployment Workflow)

---

## Learning Objectives

1. **Schedule pipelines** — Use cron syntax and Python schedulers to run pipelines automatically.
2. **CI/CD basics** — Understand what a pipeline YAML does and how to add a basic data pipeline to a CI/CD workflow.
3. **Deployment workflow** — Move a pipeline from local development through staging to production with proper environment isolation.
4. **Monitoring & alerting** — Log structured metrics, set up a basic health check, and understand what to alert on.

> By the end of this lesson you'll be able to take the pipeline you built and turn it into a production-grade automated job.

---

## Overview

### Hook
Writing a pipeline that works on your laptop is step one. Making it run reliably every night — without you touching it — is the real engineering challenge. Automation, deployment, and monitoring are where data analysts who move into DE spend most of their new-found time.

### Analogy: The Newspaper Printing Press
Think of a production pipeline like running a daily newspaper. The journalists (your data sources) deliver stories by a deadline. The press (your pipeline) runs automatically at the same time every night, typesetting and printing the morning edition. The press doesn't wait for someone to push a button — it runs on schedule. If a machine jams (a job fails), an alarm sounds and the night editor investigates. The morning papers must be delivered on time regardless.

| Production Concept | Newspaper Analogy |
|-------------------|------------------|
| **Scheduler (cron)** | The clock that starts the press at exactly 2 AM every night |
| **CI/CD pipeline** | The quality control process before a story goes to print |
| **Staging environment** | The proof copy checked before the full print run |
| **Production** | The actual 100,000 copies delivered to front doors |
| **Monitoring/alerting** | The night editor's phone — rings only when something breaks |

> **Key takeaway:** Automation takes a pipeline from "I run it manually when I remember" to "it runs itself, and I hear about it only if something goes wrong." That transition is the core of production data engineering.

---

## Key Takeaways

### 1. Cron Is the Universal Scheduler
Cron is a Unix scheduling system that runs commands at defined times. A cron expression defines when a job runs: `0 2 * * *` means "at 02:00 every day." Every cloud platform, workflow orchestrator, and CI/CD tool uses cron syntax for scheduling.  
**Keywords:** Cron · Schedule · Automation · 0 2 * * *

### 2. CI/CD Brings Software Engineering Discipline to Pipelines
CI/CD (Continuous Integration / Continuous Deployment) automates the test → build → deploy lifecycle. For a data pipeline, this means: push code to git → CI runs tests automatically → on merge, CD deploys the new version. You never manually copy code to production.  
**Keywords:** Git push · CI pipeline · Test automation · CD deploy

### 3. Environments Separate Risk from Reality
Production data is real and irreversible. A deployment workflow uses at least two environments: **staging** (a copy of production with real-ish data, where you test changes safely) and **production** (the live system). Changes go through staging first. Rolling back is a git revert, not a prayer.  
**Keywords:** Staging · Production · Environment variables · Rollback

---

## Key Concepts

### Cron Syntax
```
┌──── minute (0-59)
│  ┌──── hour (0-23)
│  │  ┌──── day of month (1-31)
│  │  │  ┌──── month (1-12)
│  │  │  │  ┌──── day of week (0-6, 0=Sunday)
│  │  │  │  │
*  *  *  *  *   command to run

Examples:
0  2  *  *  *   → Every day at 02:00
0  */6 * *  *   → Every 6 hours
0  2  *  *  1   → Every Monday at 02:00
*/15 * * *  *   → Every 15 minutes
```

### Running a Python script on a cron schedule (Linux/Mac)
```bash
# Open crontab editor
crontab -e

# Add this line to run your pipeline at 2 AM daily
0 2 * * * /usr/bin/python3 /home/user/pipelines/orders_pipeline.py >> /logs/pipeline.log 2>&1
```

### Python APScheduler (pure Python scheduler)
```python
from apscheduler.schedulers.blocking import BlockingScheduler
import orders_pipeline

scheduler = BlockingScheduler()

@scheduler.scheduled_job("cron", hour=2, minute=0)
def run_nightly():
    print("Starting nightly pipeline...")
    orders_pipeline.run()

scheduler.start()  # keeps running until you stop it
```

---

## Code Examples

### Example 1: A production-ready pipeline with logging and error handling
```python
# orders_pipeline.py
import logging, sys, os
from datetime import datetime
import pandas as pd
import sqlalchemy

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    handlers=[
        logging.FileHandler(f"logs/pipeline_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("orders_pipeline")

def run():
    log.info("=== Pipeline started ===")
    try:
        raw    = extract()
        valid  = validate(raw)
        clean  = transform(valid)
        load(clean)
        log.info(f"=== Pipeline complete: {len(clean):,} rows loaded ===")
    except Exception as e:
        log.error(f"Pipeline FAILED: {e}", exc_info=True)
        sys.exit(1)   # non-zero exit code signals failure to the scheduler

if __name__ == "__main__":
    run()
```

### Example 2: GitLab CI/CD pipeline YAML for a data job
```yaml
# .gitlab-ci.yml
stages:
  - test
  - deploy

variables:
  PYTHON_VERSION: "3.11"

# Stage 1: Run tests on every push
test-pipeline:
  stage: test
  image: python:3.11-slim
  script:
    - pip install -r requirements.txt
    - pytest tests/ -v
  rules:
    - when: always   # run tests on every commit

# Stage 2: Deploy to STAGING on merge to develop branch
deploy-staging:
  stage: deploy
  environment: staging
  script:
    - pip install -r requirements.txt
    - python orders_pipeline.py
  variables:
    DB_URL: $STAGING_DB_URL          # environment-specific secret from GitLab CI
    API_KEY: $STAGING_API_KEY
  rules:
    - if: '$CI_COMMIT_BRANCH == "develop"'

# Stage 3: Deploy to PRODUCTION on merge to main branch (with manual approval)
deploy-production:
  stage: deploy
  environment: production
  when: manual      # requires a human to click "Deploy" in GitLab — safety gate
  script:
    - pip install -r requirements.txt
    - python orders_pipeline.py
  variables:
    DB_URL: $PROD_DB_URL
    API_KEY: $PROD_API_KEY
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

### Example 3: Environment isolation with environment variables
```python
# config.py — reads different settings per environment
import os

ENV = os.environ.get("ENV", "development")

CONFIG = {
    "development": {
        "db_url":  "sqlite:///local.db",
        "api_url": "https://sandbox.api.example.com",
        "log_level": "DEBUG"
    },
    "staging": {
        "db_url":  os.environ.get("DB_URL", ""),
        "api_url": "https://staging.api.example.com",
        "log_level": "INFO"
    },
    "production": {
        "db_url":  os.environ.get("DB_URL", ""),
        "api_url": "https://api.example.com",
        "log_level": "WARNING"
    }
}[ENV]
```

### Example 4: Basic monitoring — pipeline health check endpoint
```python
# health_check.py — a simple HTTP endpoint that shows pipeline status
from flask import Flask, jsonify
import json, os
from datetime import datetime, timedelta

app = Flask(__name__)
STATUS_FILE = "pipeline_status.json"

def update_status(status: str, rows_loaded: int = 0, error: str = None):
    """Write pipeline status to a file after each run."""
    with open(STATUS_FILE, "w") as f:
        json.dump({
            "status": status,
            "last_run": datetime.now().isoformat(),
            "rows_loaded": rows_loaded,
            "error": error
        }, f)

@app.route("/health")
def health():
    """Return pipeline health — call this from monitoring tools."""
    if not os.path.exists(STATUS_FILE):
        return jsonify({"healthy": False, "reason": "No pipeline run recorded"}), 503

    with open(STATUS_FILE) as f:
        status = json.load(f)

    last_run = datetime.fromisoformat(status["last_run"])
    stale    = last_run < datetime.now() - timedelta(hours=25)

    healthy = status["status"] == "success" and not stale
    code    = 200 if healthy else 503

    return jsonify({
        "healthy": healthy,
        "last_run": status["last_run"],
        "rows_loaded": status["rows_loaded"],
        "error": status["error"],
        "stale": stale
    }), code
```

### Example 5: Deployment workflow with rollback plan
```bash
# Deployment workflow for a production pipeline
# Step 1: Push code to git
git add . && git commit -m "fix: handle null region in transform step"
git push origin develop   # → CI tests run automatically

# Step 2: Review CI test results in GitLab → green
# Step 3: Merge develop → main (triggers manual production gate)

# If production breaks — rollback in 30 seconds:
git revert HEAD --no-edit
git push origin main      # CI/CD redeploys the previous version automatically

# OR pin to a previous release tag
git checkout v1.4.2
git push origin main -f   # force-push previous stable version
```

---

## Common Mistakes

### Mistake 1: Using local paths in scheduled jobs
```python
# WRONG — works on your laptop, breaks when the scheduler runs it as a different user
df = pd.read_csv("data/orders.csv")

# RIGHT — use absolute paths or environment-relative paths
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "data", "orders.csv"))
```

### Mistake 2: No exit code on failure (scheduler thinks it succeeded)
```python
# WRONG — scheduler sees exit code 0 (success) even when pipeline crashed
try:
    run_pipeline()
except Exception as e:
    print(f"Error: {e}")   # scheduler doesn't know this failed

# RIGHT — signal failure with a non-zero exit code
import sys
try:
    run_pipeline()
except Exception as e:
    log.error(e)
    sys.exit(1)   # exit code 1 = failure — scheduler will alert
```

### Mistake 3: Deploying directly to production without staging
```
WRONG: Edit pipeline code → save → run in production
RISK:  A bug corrupts live production data with no easy rollback

RIGHT: Edit → commit → CI tests → deploy to staging → test against staging data
       → manual approval → deploy to production
```

---

## Practice Exercises

### Exercise 1 — Write a cron expression
Write cron expressions for each of the following schedules:
1. Every day at 6:30 AM
2. Every Monday and Wednesday at midnight
3. Every 30 minutes
4. The first day of every month at 3 AM

**Answers:** 1. `30 6 * * *`  2. `0 0 * * 1,3`  3. `*/30 * * * *`  4. `0 3 1 * *`

### Exercise 2 — Add production logging to a pipeline
```python
# TODO: Take this minimal pipeline and add:
# 1. Logging at INFO level for each step (extract, validate, transform, load)
# 2. Log row counts at each stage
# 3. A try/except that logs the error and calls sys.exit(1) on failure
# 4. A final log message with total rows loaded and elapsed time

def run():
    raw   = extract()
    clean = transform(raw)
    load(clean)
```

### Exercise 3 — Environment configuration
```python
# TODO: Write a config.py that:
# 1. Reads an ENV environment variable (default: "development")
# 2. Returns different DB URLs and API base URLs for dev/staging/prod
# 3. Reads sensitive values (passwords, API keys) from environment variables
# 4. Raises a clear error if a required environment variable is missing
```

---

## Lesson Recap

1. **Cron** (`0 2 * * *` syntax) is the universal way to schedule pipeline runs — learn 5 cron patterns and you can schedule anything.
2. **CI/CD** automates test → build → deploy so you never manually push code to production; a `.gitlab-ci.yml` defines the pipeline as code.
3. **Environment isolation** (development → staging → production) separates risk from real data — always test on staging before touching production.
4. **Monitoring** means knowing before your users do when something breaks — structured logging, non-zero exit codes on failure, and a health check endpoint are the minimum viable monitoring stack.

---

## Knowledge Check

**Q1.** What does the cron expression `0 */4 * * *` mean?  
**Answer:** Run at minute 0 of every 4th hour — i.e. at 00:00, 04:00, 08:00, 12:00, 16:00, and 20:00 every day. Six times per day, every 4 hours.

**Q2.** Why is `sys.exit(1)` important in a scheduled pipeline script?  
**Answer:** A non-zero exit code signals to the scheduler (cron, CI/CD, orchestrator) that the job failed. If the script exits with code 0 (the default on no error), the scheduler assumes success and won't trigger alerts — even if your pipeline loaded 0 rows due to an exception it silently swallowed.

**Q3.** What is the purpose of a staging environment?  
**Answer:** Staging is a copy of the production environment (same database schema, similar data, same pipeline code) where you test changes before they go live. It lets you catch bugs and integration issues on non-critical data before they can cause irreversible damage to production.

---

## Next Lesson
**Lesson 10 — Performance at Scale**  
Your pipeline is running automatically and reliably. Now let's make it faster. In the final lesson you'll learn to profile where time and memory go, use parallel processing to use all your CPU cores, and build the habits that keep large-data pipelines performant over time.
