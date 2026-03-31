# Module 16 — Automation with Python  
## Lesson 12 — Deploying Automation Scripts

---

# Lesson Objective

By the end of this lesson you will understand:

- What **deployment** means for automation scripts
- How to move Python automation from **local development to production**
- Where automation scripts are typically deployed
- How automated pipelines run reliably in real environments

Deployment is the final step that turns automation scripts into **real production systems**.

---

# Overview

When developing automation scripts, work often begins on a **local machine**.

Example workflow:

```text
Write script
Test locally
Fix bugs
Run script manually
```

However, real automation systems should run **without depending on a personal computer**.

Instead, scripts are deployed to environments like:

- servers
- cloud platforms
- automation runners
- scheduled pipeline systems

Example production workflow:

```text
Code Repository
        ↓
Deployment Environment
        ↓
Scheduled Job
        ↓
Automation Pipeline Runs
```

Deployment ensures automation runs **reliably and consistently**.

---

# Key Concepts

## Local vs Production

| Environment | Purpose |
|------|------|
| Local | Development and testing |
| Production | Real automated execution |

Example:

| Step | Environment |
|------|------|
| Write code | Local machine |
| Test automation | Local machine |
| Deploy pipeline | Server |
| Schedule jobs | Production system |

---

## Deployment Environments

Automation scripts can run in different environments.

Common environments include:

| Environment | Example |
|------|------|
| Local machine | Personal computer |
| Server | Linux server |
| Cloud platform | AWS, Azure |
| Automation runner | CI/CD system |

In many organizations, automation runs on **servers or pipeline runners**.

---

## Deployment Workflow

Typical deployment pipeline:

```text
Write Code
     ↓
Commit to Git
     ↓
Deploy to Server
     ↓
Schedule Automation Job
```

Once deployed, scripts run **automatically without manual intervention**.

---

# Decision Flow

Automation should be deployed when:

```text
Is the script stable?
        |
        Yes
        |
Does it need to run regularly?
        |
        Yes
        |
Should it run independently of your computer?
        |
        Yes
        |
Deploy the script
```

Deployment ensures automation works **reliably and continuously**.

---

# Code Examples

## Example 1 — Running a Script in Production

A deployed script may run like this:

```bash
python run_report.py
```

This command is executed by:

- a scheduler
- a pipeline runner
- a server automation job

---

## Example 2 — Typical Automation Project Structure

Example deployed automation project:

```text
automation_pipeline/

config/
    config.json

scripts/
    load_data.py
    process_data.py
    generate_report.py

logs/
    pipeline.log

main.py
```

This structure keeps production systems organized.

---

## Example 3 — Production Pipeline Execution

The main script orchestrates execution.

```python
def main():

    df = load_data()

    processed = process_data(df)

    report_file = generate_report(processed)

    send_email(report_file)

if __name__ == "__main__":

    main()
```

This script runs automatically in the deployed environment.

---

# SQL / Excel Comparison

### Manual Reporting

```text
Open Excel
Run SQL query
Create report
Email report
```

Requires a person every time.

---

### Automated Production Pipeline

```text
Server runs Python script
     ↓
Database query executed
     ↓
Report generated
     ↓
Email sent
```

No manual work required.

---

# Practice Exercises

## Exercise 1

Tags: Scripts, Automation, Deployment

Create a folder structure for a deployable automation project.

Example:

```text
automation_project/

config/
logs/
scripts/
main.py
```

---

## Exercise 2

Tags: Conditionals, Environment Variables, Scripts, Automation

Modify your automation script so it runs using:

```python
if __name__ == "__main__":
```

This ensures the script executes correctly in production environments.

---

## Exercise 3

Tags: CI/CD, Logging, Deployment

Add logging so deployment runs record activity.

Example log file:

```text
pipeline.log
```

---

## Exercise 4 (Real-World)

Tags: Git, CI/CD, Automation, Scheduling

Design a deployment workflow for a reporting pipeline.

Example process:

```text
Code stored in Git
     ↓
Pipeline deployed to server
     ↓
Scheduler runs job daily
     ↓
Report generated automatically
```

---

# Common Mistakes

## Mistake 1 — Running Automation Only on Personal Machines

If your computer shuts down, the automation stops.

Better approach:

Deploy scripts to **servers or pipeline runners**.

---

## Mistake 2 — Not Testing Before Deployment

Automation scripts should be **fully tested locally** before deployment.

---

## Mistake 3 — Missing Dependencies

Production environments must include all required packages.

Example:

```bash
pip install pandas
pip install openpyxl
```

---

# Real-World Use

Deployment is essential for large-scale automation systems.

Examples include:

---

### Data Engineering Pipelines

ETL pipelines are deployed to servers and run automatically.

Example workflow:

```text
Extract data
Transform records
Load data warehouse
```

---

### Reporting Systems

Production reporting pipelines generate:

- daily dashboards
- executive reports
- operational summaries

---

### CI/CD Automation

Modern organizations deploy automation using CI/CD systems that automatically run scripts when code changes.

---

# Key Idea Cards

### Card 1

Deployment moves automation scripts from **local machines to production environments**.

---

### Card 2

Production automation runs on **servers, cloud platforms, or pipeline systems**.

---

### Card 3

Deployment ensures automation runs **reliably without manual execution**.

---

# Lesson Recap

In this lesson you learned:

- what deployment means
- how automation scripts move to production environments
- how automation pipelines run on servers
- how deployment enables reliable automated workflows

Deployment is the final step that turns automation scripts into **real operational systems**.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 13: Building a Real-World Automation Project**

In this lesson you will:

- combine everything learned in Module 15
- design a complete automation project
- build a real-world reporting pipeline from start to finish.