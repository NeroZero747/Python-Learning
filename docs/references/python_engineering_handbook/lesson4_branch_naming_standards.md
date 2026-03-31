# Module 11 — Python Engineering Handbook

# Lesson 4 — Branch Naming Standards

---

# Lesson Objective

By the end of this lesson learners will understand:

• why teams define **branch naming standards**  
• how Git branches support collaborative development  
• how branch naming improves CI/CD workflows  
• common branch naming conventions used in professional environments  

Branch naming standards ensure that repositories remain **organized, understandable, and easy to manage** when multiple developers are working on the same project.

---

# Overview

When working with Git, developers create **branches** to isolate changes before merging them into the main codebase.

Example simple workflow:

```text
Main Branch
     ↓
Create Feature Branch
     ↓
Develop Feature
     ↓
Merge Feature Into Main
```

Without naming standards, branches might look like this:

```text
update
fix
stuff
new_code
test
```

These names do not clearly describe what the branch contains.

Professional teams define **branch naming conventions** to make branches easier to understand.

Example standardized naming:

```text
feature/add-user-authentication
bugfix/fix-login-error
hotfix/security-patch
```

This allows developers to quickly understand the purpose of each branch.

---

# Key Idea Cards (3 Cards)

### Branches Isolate Code Changes

Branches allow developers to work on changes without affecting the main codebase.

Example workflow:

```text
main
   ↓
feature/data-dashboard
```

Changes are merged once they are ready.

---

### Naming Standards Improve Collaboration

Clear naming conventions help developers understand the purpose of branches.

Example:

```text
feature/customer-report
bugfix/pipeline-error
```

This makes repositories easier to navigate.

---

### Branch Names Can Trigger CI/CD Workflows

Some CI/CD systems trigger different actions depending on branch names.

Example:

```text
main → production deployment
develop → staging deployment
feature/* → testing pipeline
```

Branch names can control deployment behavior.

---

# Key Concepts

## Branch Types

Most teams use several types of branches.

Common examples:

| Branch Type | Purpose |
|------|------|
| main | stable production code |
| develop | integration branch for new features |
| feature | new functionality |
| bugfix | fixes for bugs |
| hotfix | urgent production fixes |

This structure helps organize development workflows.

---

## Feature Branches

Feature branches are used to develop new functionality.

Example branch:

```text
feature/add-report-dashboard
```

Workflow:

```text
Create feature branch
        ↓
Develop feature
        ↓
Open pull request
        ↓
Merge into develop or main
```

---

## Bugfix Branches

Bugfix branches fix issues discovered in the code.

Example:

```text
bugfix/fix-data-processing-error
```

These branches isolate fixes before merging them.

---

# Decision Flow

Developers typically create branches using the following logic:

```text
New feature?
       ↓
Create feature branch

Bug found?
       ↓
Create bugfix branch

Urgent production issue?
       ↓
Create hotfix branch
```

Branch naming helps teams quickly identify the purpose of each change.

---

# Code Examples

### Example 1 — Creating a Branch

```bash
git checkout -b feature/customer-dashboard
```

This creates a new feature branch.

---

### Example 2 — Bugfix Branch

```bash
git checkout -b bugfix/pipeline-error
```

This branch isolates a bug fix.

---

### Example 3 — Hotfix Branch

```bash
git checkout -b hotfix/security-patch
```

Hotfix branches are used for urgent production issues.

---

### Example 4 — Branch Workflow

Example workflow:

```text
main
  ↓
feature/data-pipeline
  ↓
Pull Request
  ↓
Code Review
  ↓
Merge into main
```

This ensures changes are reviewed before merging.

---

# SQL / Excel Comparison

Branching concepts do not exist exactly in SQL or Excel, but similar version control ideas appear.

| Concept | Python / Git | SQL | Excel |
|------|------|------|------|
| version control | Git branches | database versioning | workbook versions |
| collaborative changes | pull requests | schema migrations | shared workbooks |
| controlled updates | merge process | release scripts | version history |

Example SQL release workflow:

```text
Develop schema change
      ↓
Test migration
      ↓
Deploy change
```

Branching serves a similar purpose in application development.

---

# Practice Exercises

### Exercise 1

Tags: Git, Dashboards, Git Workflow

Create a feature branch.

Example:

```bash
git checkout -b feature/new-dashboard
```

---

### Exercise 2

Tags: Git, Validation, Git Workflow

Create a bugfix branch.

Example:

```bash
git checkout -b bugfix/data-validation
```

---

### Exercise 3

Tags: Git, Git Workflow

Create a hotfix branch.

Example:

```bash
git checkout -b hotfix/security-fix
```

---

### Exercise 4

Tags: Git Workflow, Data Engineering

Write a branch naming guideline for your team.

Example rules:

```text
feature/
bugfix/
hotfix/
```

---

# Common Mistakes

### Vague Branch Names

Avoid unclear branch names.

Bad:

```text
update
changes
stuff
```

Better:

```text
feature/customer-report
bugfix/payment-processing
```

Clear naming improves repository organization.

---

### Long-Lived Feature Branches

Branches should be merged regularly.

Long-running branches can cause complex merge conflicts.

---

### Directly Committing to Main

Developers should avoid committing directly to the main branch.

Feature branches allow safe development and code review.

---

# Real-World Use

Branch naming standards are widely used in professional development teams.

Example workflow:

```text
Developer creates feature branch
        ↓
Developer implements changes
        ↓
Pull request created
        ↓
Code review performed
        ↓
Branch merged
```

Branch standards support:

• collaborative development  
• CI/CD pipelines  
• safe deployment workflows  
• structured release management.

Organizations often define **formal Git workflows** to ensure consistency across projects.
