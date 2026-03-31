# Module 10 — Automation & CI/CD

# Lesson 2 — GitLab CI/CD Overview

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **CI/CD pipelines** are  
• how **GitLab CI/CD** works  
• how automation pipelines run tests and deployments  
• how Python projects can be integrated into CI/CD workflows  

Continuous Integration and Continuous Deployment (CI/CD) are essential tools for modern development teams because they allow software to be **automatically built, tested, and deployed**.

---

# Overview

When teams collaborate on software projects, multiple developers contribute code changes regularly.

Without automation, the workflow might look like this:

```text
Developer writes code
        ↓
Developer manually runs tests
        ↓
Developer deploys application
        ↓
Errors appear in production
```

This approach is risky because:

• tests may be skipped  
• deployments may be inconsistent  
• bugs may reach production systems.

CI/CD pipelines solve this problem by automating the process.

Modern CI/CD workflow:

```text
Developer pushes code to Git repository
        ↓
CI pipeline automatically runs
        ↓
Automated tests execute
        ↓
Application is built
        ↓
Application is deployed
```

GitLab provides a built-in CI/CD system that allows teams to define pipelines using a configuration file.

---

# Key Idea Cards (3 Cards)

### CI/CD Automates Software Workflows

CI/CD pipelines automate repetitive tasks such as:

```text
running tests
building applications
deploying software
```

Automation improves consistency and reliability.

---

### Pipelines Run When Code Changes

CI/CD pipelines are typically triggered when developers push changes.

Example trigger:

```text
git push
```

This automatically starts the pipeline process.

---

### Pipeline Steps Are Defined in Configuration Files

GitLab pipelines are configured using a file called:

```text
.gitlab-ci.yml
```

This file defines the stages and tasks in the pipeline.

---

# Key Concepts

## CI Pipeline

A **Continuous Integration pipeline** automatically builds and tests code whenever changes are committed.

Example process:

```text
Developer commits code
        ↓
Pipeline runs tests
        ↓
Results reported to developer
```

If tests fail, developers must fix the issue before merging code.

---

## CD Pipeline

A **Continuous Deployment pipeline** automatically deploys applications after tests pass.

Example workflow:

```text
Tests pass
       ↓
Application packaged
       ↓
Application deployed
```

This ensures software updates can be delivered quickly.

---

## GitLab CI/CD Configuration

GitLab pipelines are defined in a YAML configuration file.

Example file:

```text
.gitlab-ci.yml
```

This file defines:

• pipeline stages  
• jobs to execute  
• scripts to run  
• environment settings.

---

# Decision Flow

Developers typically implement CI/CD pipelines using this workflow:

```text
Write code
      ↓
Push code to repository
      ↓
Pipeline runs automatically
      ↓
Tests verify code
      ↓
Deploy application
```

This ensures code quality and reliable deployment.

---

# Code Examples

### Example 1 — Simple GitLab CI Pipeline

Example `.gitlab-ci.yml` file:

```yaml
stages:
  - test

test_job:
  stage: test
  script:
    - echo "Running tests"
```

This pipeline runs a simple test stage.

---

### Example 2 — Python Test Pipeline

```yaml
stages:
  - test

test_python:
  stage: test
  script:
    - pip install pytest
    - pytest
```

This pipeline installs pytest and runs automated tests.

---

### Example 3 — Multi-Stage Pipeline

```yaml
stages:
  - test
  - build
  - deploy
```

Example pipeline flow:

```text
Test Stage
     ↓
Build Stage
     ↓
Deploy Stage
```

Each stage runs in sequence.

---

### Example 4 — Python Script in Pipeline

```yaml
process_data:
  stage: build
  script:
    - python process_data.py
```

This pipeline runs a Python script automatically.

---

# SQL / Excel Comparison

CI/CD automation concepts exist in data workflows as well.

| Concept | Python CI/CD | SQL | Excel |
|------|------|------|------|
| automation | CI pipelines | scheduled jobs | macros |
| deployment | automated builds | database release scripts | workbook distribution |
| validation | automated tests | data validation queries | formula checks |

Example SQL automation:

```text
Nightly ETL Job
```

CI pipelines perform similar automation tasks for code.

---

# Practice Exercises

### Exercise 1

Tags: CI/CD, YAML, Scripts, Testing

Create a simple `.gitlab-ci.yml` file:

```yaml
stages:
  - test

test_job:
  stage: test
  script:
    - echo "Pipeline working"
```

---

### Exercise 2

Tags: YAML, Scripts, Testing

Add a Python test stage:

```yaml
script:
  - pytest
```

---

### Exercise 3

Tags: CI/CD, Testing, Deployment

Add additional pipeline stages.

Example:

```text
test
build
deploy
```

---

# Common Mistakes

### Not Testing Code Before Deployment

Skipping automated tests can allow bugs into production.

CI pipelines should always run tests.

---

### Overly Complex Pipelines

Pipelines should start simple and grow as needed.

Begin with basic testing before adding complex stages.

---

### Ignoring Pipeline Failures

Developers must investigate and fix pipeline failures quickly.

Ignoring failures reduces CI/CD effectiveness.

---

# Real-World Use

CI/CD pipelines are widely used in modern development teams.

Example workflow:

```text
Developer pushes code
        ↓
GitLab pipeline runs
        ↓
Tests execute
        ↓
Application builds
        ↓
Deployment occurs
```

This approach is commonly used in:

• data engineering pipelines  
• analytics platforms  
• machine learning systems  
• enterprise applications.

CI/CD allows teams to **deploy software faster and with fewer errors**.

---

# Lesson Recap

In this lesson you learned:

• what CI/CD pipelines are  
• how GitLab CI/CD automates workflows  
• how pipelines run tests and deployments  
• how Python applications integrate with CI pipelines.

CI/CD is a key component of **modern software automation and DevOps practices**.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Scheduling Data Jobs

You will learn:

• how automated jobs run on schedules  
• how data pipelines are scheduled  
• how Python scripts can run automatically  
• how organizations automate recurring data processes.
