# Module 10 — Automation & CI/CD

# Lesson 1 — DevOps Concepts for Data & Analytics

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **DevOps** means in modern software development  
• how DevOps applies to **data and analytics workflows**  
• how automation improves reliability and productivity  
• how Python applications are deployed and maintained in production environments  

DevOps helps organizations **automate development, testing, deployment, and operations** so systems can run reliably at scale.

---

# Overview

Traditionally, software development and operations were separate processes.

Example traditional workflow:

```text
Developer writes code
        ↓
Code sent to operations team
        ↓
Operations deploy system
        ↓
Issues appear
        ↓
Developers investigate
```

This process often caused delays and communication problems.

DevOps improves this process by integrating development and operations.

Modern DevOps workflow:

```text
Write Code
   ↓
Automated Tests
   ↓
Automated Build
   ↓
Automated Deployment
   ↓
Monitoring
```

This approach allows software to be deployed **quickly, safely, and consistently**.

---

# Key Idea Cards (3 Cards)

### DevOps Connects Development and Operations

DevOps combines two traditionally separate roles:

```text
Development + Operations
```

Developers and operations teams collaborate to improve software delivery.

---

### Automation Reduces Human Error

Manual deployment processes often cause mistakes.

Automation ensures processes run the same way every time.

Example automation tasks:

```text
Running tests
Building applications
Deploying systems
Scheduling data pipelines
```

---

### Continuous Integration Improves Code Quality

Continuous Integration (CI) automatically tests code when changes are made.

Example workflow:

```text
Developer pushes code
      ↓
CI pipeline runs tests
      ↓
Code approved or rejected
```

This prevents broken code from entering production.

---

# Key Concepts

## DevOps

DevOps is a set of practices that combine **software development and IT operations**.

Goals include:

• faster development cycles  
• improved reliability  
• automated deployments  
• better collaboration.

---

## Continuous Integration (CI)

Continuous Integration automatically tests code whenever changes are pushed.

Example workflow:

```text
Developer pushes code
        ↓
CI system runs tests
        ↓
Code verified before merging
```

CI helps detect bugs early.

---

## Continuous Deployment (CD)

Continuous Deployment automatically deploys applications after tests pass.

Example workflow:

```text
Code committed
       ↓
Tests pass
       ↓
Application deployed
```

This allows systems to update frequently and reliably.

---

# Decision Flow

Organizations typically adopt DevOps using this approach:

```text
Manual processes slow development
        ↓
Introduce automation
        ↓
Add CI pipelines
        ↓
Enable automated deployment
```

Automation improves speed and reliability.

---

# Code Examples

### Example 1 — Manual Data Pipeline

```python
python process_data.py
python generate_report.py
```

This process must be run manually.

---

### Example 2 — Automated Script

```python
def run_pipeline():
    process_data()
    generate_report()

run_pipeline()
```

Automation reduces manual work.

---

### Example 3 — CI Pipeline Trigger

Example Git workflow:

```text
Developer commits code
        ↓
CI pipeline runs tests
        ↓
Pipeline reports results
```

CI ensures new code does not break the system.

---

### Example 4 — Automated Deployment

Example automated pipeline:

```text
Code pushed to repository
       ↓
Tests run automatically
       ↓
Application deployed
```

This reduces manual deployment work.

---

# SQL / Excel Comparison

DevOps concepts exist in data workflows as well.

| Concept | Python DevOps | SQL | Excel |
|------|------|------|------|
| automation | CI pipelines | scheduled jobs | macros |
| deployment | automated builds | database releases | workbook distribution |
| monitoring | logging systems | query monitoring | workbook validation |

Example SQL automation:

```text
Nightly ETL Job
```

Similarly, DevOps automates Python pipelines.

---

# Practice Exercises

### Exercise 1

Tags: CI/CD, Automation, Dashboards

Identify tasks in your workflow that could be automated.

Examples:

```text
Data processing
Report generation
Dashboard refresh
```

---

### Exercise 2

Tags: Functions, CI/CD, Scripts, Automation

Create a Python script that runs multiple steps automatically.

Example:

```python
def pipeline():
    extract_data()
    transform_data()
    load_data()
```

---

### Exercise 3

Tags: CI/CD, Automation

Research CI tools such as:

```text
GitHub Actions
GitLab CI
Jenkins
Azure DevOps
```

---

# Common Mistakes

### Relying on Manual Processes

Manual steps increase the risk of errors.

Automation improves reliability.

---

### Skipping Automated Testing

Deploying code without testing increases the chance of system failures.

Always integrate testing into pipelines.

---

### Ignoring Monitoring

Even automated systems must be monitored.

Logs and alerts help detect problems quickly.

---

# Real-World Use

DevOps is widely used in modern data platforms.

Example analytics workflow:

```text
Developer writes Python code
        ↓
Code pushed to Git repository
        ↓
CI pipeline runs automated tests
        ↓
Application deployed automatically
        ↓
Monitoring tracks system health
```

This approach is used in:

• data engineering pipelines  
• analytics platforms  
• machine learning systems  
• enterprise applications.

---

# Lesson Recap

In this lesson you learned:

• what DevOps is  
• how DevOps improves software development  
• how CI/CD pipelines automate development workflows  
• how automation improves reliability.

DevOps practices help organizations **build and deploy software faster and more reliably**.

---

# Next Lesson

Next we will learn:

# Lesson 2 — GitLab CI/CD Overview

You will learn:

• how CI/CD pipelines work  
• how GitLab CI automates workflows  
• how Python projects are tested and deployed using pipelines  
• how teams build reliable automation workflows.
