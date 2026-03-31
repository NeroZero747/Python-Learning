# Module 10 — Automation & CI/CD

# Lesson 5 — Deployment Workflow

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **software deployment** means  
• how applications move from development to production  
• how CI/CD pipelines automate deployment  
• common deployment workflows used by development teams  

Deployment is the process of **releasing software so it can run in a production environment** where users and systems can access it.

For data applications, deployment might include:

• running a data pipeline  
• deploying an analytics dashboard  
• updating a data processing service  
• releasing a machine learning model.

---

# Overview

During development, developers write and test code on their local machines.

Example workflow:

```text
Developer writes Python code
        ↓
Tests code locally
        ↓
Commits code to repository
```

However, users cannot access applications running on a developer’s laptop.

The application must be **deployed to a server or platform**.

Example deployment workflow:

```text
Developer commits code
        ↓
CI pipeline runs tests
        ↓
Build process prepares application
        ↓
Application deployed to server
```

Once deployed, the application becomes available to users or other systems.

---

# Key Idea Cards (3 Cards)

### Deployment Moves Code to Production

Deployment makes an application available to users.

Example environments:

```text
Development
Testing
Production
```

Production is the environment where real users interact with the system.

---

### CI/CD Pipelines Automate Deployment

Modern systems deploy applications automatically using pipelines.

Example pipeline:

```text
Code pushed to repository
        ↓
Tests run automatically
        ↓
Application deployed
```

Automation reduces deployment errors.

---

### Multiple Environments Improve Safety

Most systems use several environments before deployment.

Example:

```text
Development → Testing → Production
```

This ensures code is validated before reaching production.

---

# Key Concepts

## Deployment Environments

Software typically moves through several environments.

| Environment | Purpose |
|------|------|
| Development | developers build and test code |
| Testing | automated tests run |
| Staging | production-like testing |
| Production | real users access system |

This staged process reduces risk.

---

## Build Process

Before deployment, code may be packaged or prepared.

Example build tasks:

```text
install dependencies
compile assets
prepare configuration
package application
```

Build steps ensure the application runs properly.

---

## Automated Deployment

CI/CD pipelines automate the deployment process.

Example pipeline:

```text
Test Stage
      ↓
Build Stage
      ↓
Deploy Stage
```

Automation ensures consistent deployment.

---

# Decision Flow

Deployment workflows usually follow this process:

```text
Code updated
      ↓
Tests run
      ↓
Build application
      ↓
Deploy to environment
```

If tests fail, deployment stops.

---

# Code Examples

### Example 1 — Simple Deployment Script

```python
def deploy_application():
    install_dependencies()
    run_tests()
    start_application()

deploy_application()
```

This script performs deployment tasks.

---

### Example 2 — GitLab CI Deployment Stage

Example `.gitlab-ci.yml` configuration:

```yaml
stages:
  - test
  - deploy

deploy_app:
  stage: deploy
  script:
    - python deploy.py
```

This pipeline deploys the application after tests pass.

---

### Example 3 — Deploying a Python Application

Example deployment script:

```python
import subprocess

subprocess.run(["pip", "install", "-r", "requirements.txt"])
subprocess.run(["python", "app.py"])
```

This installs dependencies and starts the application.

---

### Example 4 — Deployment Workflow

Example deployment process:

```text
Developer pushes code
        ↓
Pipeline runs tests
        ↓
Application built
        ↓
Application deployed
```

This ensures reliable releases.

---

# SQL / Excel Comparison

Deployment concepts exist in other data tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| deployment | application release | database migration | workbook distribution |
| environments | dev/test/prod | dev/test/prod databases | shared workbooks |
| automation | CI/CD pipelines | deployment scripts | macros |

Example SQL deployment:

```text
Run migration scripts
Update stored procedures
Deploy database schema
```

These steps are similar to deploying Python applications.

---

# Practice Exercises

### Exercise 1

Tags: print(), Functions, CI/CD, Scripts

Create a simple deployment script.

Example:

```python
def deploy():
    print("Installing dependencies")
    print("Starting application")
```

---

### Exercise 2

Tags: CI/CD, Testing, Deployment

Design a deployment pipeline.

Example stages:

```text
test
build
deploy
```

---

### Exercise 3

Tags: File I/O, CI/CD, YAML, Deployment

Write a `.gitlab-ci.yml` file with a deployment stage.

---

### Exercise 4

Tags: WHERE, Docker, CI/CD, Deployment

Research platforms where Python applications are deployed.

Examples:

```text
AWS
Azure
Google Cloud
Docker
Posit Connect
```

---

# Common Mistakes

### Deploying Without Testing

Skipping tests increases the risk of production failures.

Testing should always occur before deployment.

---

### Deploying Directly to Production

Code should first pass through staging environments.

This reduces risk.

---

### Ignoring Rollback Strategies

Deployments may fail.

Teams should have a rollback strategy to restore previous versions.

---

# Real-World Use

Deployment workflows are used in almost every modern software system.

Example analytics deployment:

```text
Developer updates dashboard code
        ↓
Pipeline runs tests
        ↓
Application deployed
        ↓
Users access updated dashboard
```

Deployment automation is used in:

• web applications  
• data pipelines  
• analytics platforms  
• machine learning services.

Automated deployment allows teams to **deliver software quickly and reliably**.

---

# Lesson Recap

In this lesson you learned:

• what deployment means in software development  
• how applications move from development to production  
• how CI/CD pipelines automate deployment  
• how environments reduce deployment risk.

Deployment workflows ensure applications are **released safely and consistently**.

---

# Module 10 Complete

In this module you learned:

• DevOps concepts  
• CI/CD pipelines  
• GitLab CI workflows  
• scheduling automated jobs  
• secrets management  
• deployment workflows.

These practices enable teams to build **fully automated and reliable software systems**.
