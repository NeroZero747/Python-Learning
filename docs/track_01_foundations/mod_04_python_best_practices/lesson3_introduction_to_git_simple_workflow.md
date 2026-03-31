# Module 5 — Writing Cleaner Python Code

# Lesson 4 — Introduction to Git (Simple Workflow)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what version control is  
• why Git is used in professional development  
• the basic Git workflow  
• how Git helps manage code changes  

Version control systems like Git are essential because they allow developers and analysts to **track, manage, and collaborate on code safely**.

---

# Overview

When working on code projects, files change over time.

For example:

```text
analysis.py
analysis_v2.py
analysis_final.py
analysis_final2.py
analysis_final_REAL.py
```

Without version control, it becomes difficult to know:

• which version is correct  
• what changed  
• who made the change  
• how to revert mistakes  

Git solves this problem by tracking every change made to the code.

Instead of creating many versions of files, Git stores the **history of the project**.

Example Git history:

```text
Commit 1 — Initial analysis script
Commit 2 — Added data cleaning logic
Commit 3 — Fixed calculation bug
Commit 4 — Added export feature
```

This allows developers to move backward in time if needed.

Git is used by nearly every modern software team and is a core skill for analysts working in technical environments.

---

# Key Idea Cards (3 Cards)

## Git Tracks Code Changes

Git records every change made to the codebase.

Example commit history:

```text
Commit 1 → Initial script
Commit 2 → Added cleaning logic
Commit 3 → Fixed calculation bug
```

This makes it easy to understand how the code evolved.

---

## Git Enables Collaboration

Multiple developers can work on the same project without overwriting each other's work.

Example team workflow:

```text
Developer A → data cleaning
Developer B → dashboard logic
Developer C → export functions
```

Git merges their work together.

---

## Git Allows Reverting Mistakes

If something breaks, Git can restore a previous version.

Example:

```text
git checkout previous_version
```

This restores the code to a working state.

---

# Key Concepts

## Repository

A **repository (repo)** is a folder tracked by Git.

Example project folder:

```text
sales_project
│
├── main.py
├── modules
│   └── calculations.py
└── data
```

When Git tracks the folder, it becomes a repository.

---

## Commit

A **commit** records a snapshot of the project.

Example commit message:

```text
Added revenue calculation function
```

Each commit contains:

• code changes  
• author  
• timestamp  
• commit message  

---

## Version History

Git maintains a history of all commits.

Example timeline:

```text
Commit 1 — Initial project
Commit 2 — Added modules
Commit 3 — Fixed bug
Commit 4 — Improved performance
```

Developers can review or restore previous versions.

---

# Decision Flow

The basic Git workflow looks like this:

```text
Edit files
      ↓
Stage changes
      ↓
Commit changes
      ↓
Push changes to repository
```

Example workflow:

```text
Edit code → git add → git commit → git push
```

---

# Code Examples

## Example 1 — Initialize a Git Repository

```bash
git init
```

This converts the folder into a Git repository.

---

## Example 2 — Check File Status

```bash
git status
```

This shows which files have changed.

---

## Example 3 — Stage Changes

```bash
git add main.py
```

This prepares the file for commit.

---

## Example 4 — Commit Changes

```bash
git commit -m "Added revenue calculation"
```

This records the change in the project history.

---

# SQL / Excel Comparison

Version control concepts also exist informally in other tools.

| Concept | Python/Git | SQL | Excel |
|------|------|------|------|
| version control | Git repository | database backup | file versions |
| change history | commits | audit logs | version history |
| collaboration | Git branches | shared database | shared workbook |

Example Excel workflow:

```text
analysis_v1.xlsx
analysis_v2.xlsx
analysis_v3.xlsx
```

Git replaces this manual process with automated version tracking.

---

# Practice Exercises

## Exercise 1

Tags: Git, CI/CD

Initialize a Git repository.

```bash
git init
```

---

## Exercise 2

Tags: Git, CI/CD

Check file status.

```bash
git status
```

---

## Exercise 3

Tags: Transactions, Git, CI/CD, Scripts

Commit a file.

```bash
git add main.py
git commit -m "Initial script"
```

---

# Common Mistakes

## Forgetting Commit Messages

Poor commit message:

```text
git commit -m "update"
```

Better commit message:

```text
git commit -m "Added sales calculation function"
```

Clear messages improve collaboration.

---

## Committing Too Many Changes at Once

Large commits make it difficult to track changes.

Better practice:

```text
Commit small logical changes
```

---

## Tracking Data Files in Git

Large datasets should usually **not be stored in Git repositories**.

Instead store:

• scripts  
• modules  
• configuration files  

---

# Real-World Use

Git is used in nearly every professional development environment.

Example workflow for a data project:

```text
Edit Python script
      ↓
Commit change
      ↓
Push code to repository
      ↓
Team reviews change
```

Platforms such as:

• GitHub  
• GitLab  
• Bitbucket  

provide collaborative repositories for teams.

---

# Lesson Recap

In this lesson you learned:

• what Git is  
• how version control tracks code changes  
• the basic Git workflow  
• why Git is essential for collaboration  

Version control is a critical tool because it ensures that **code changes are tracked safely and transparently**.

---

# Next Lesson

Next we will learn:

# Lesson 5 — Git in VS Code

You will learn:

• how to use Git inside VS Code  
• how to stage and commit changes using the editor  
• how Git integrates into the development workflow  

This lesson will show how Git works inside a modern development environment.
