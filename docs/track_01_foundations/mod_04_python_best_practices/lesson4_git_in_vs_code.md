# Module 5 — Writing Cleaner Python Code

# Lesson 5 — Git in VS Code

---

# Lesson Objective

By the end of this lesson learners will understand:

• how Git integrates with Visual Studio Code  
• how to stage and commit changes using the VS Code interface  
• how to view file changes and version history  
• how Git improves the development workflow inside an editor  

VS Code makes Git easier to use because it provides a **visual interface for version control**, allowing developers to manage commits without always using the command line.

---

# Overview

While Git can be used through the command line, most developers interact with Git through their code editor.

Visual Studio Code has **built-in Git support**, which allows users to:

• track file changes  
• stage files  
• create commits  
• view differences between versions  
• push code to repositories  

When a folder contains a Git repository, VS Code automatically detects it.

Example project:

```text
sales_project
│
├── main.py
├── modules
│   └── calculations.py
└── data
```

When files are modified, VS Code highlights the changes.

Example indicators:

• **green** — new lines added  
• **red** — lines removed  
• **yellow** — modified lines  

These visual indicators help developers quickly understand what changed in the code.

---

# Key Idea Cards (3 Cards)

## VS Code Detects Git Repositories Automatically

When you open a folder that contains a Git repository, VS Code activates Git features automatically.

Example workflow:

```text
Open project folder → VS Code detects Git → Source Control panel becomes active
```

This allows developers to manage version control directly in the editor.

---

## The Source Control Panel Manages Commits

VS Code provides a **Source Control panel** that displays modified files.

Example workflow:

```text
Edit file → open Source Control → stage file → commit change
```

This replaces many command-line steps with a graphical interface.

---

## VS Code Shows File Differences

VS Code can display the difference between file versions.

Example comparison:

```text
Old version → New version
```

Added lines appear in **green**, removed lines appear in **red**.

This makes reviewing changes easier.

---

# Key Concepts

## Source Control Panel

The **Source Control panel** displays files that have changed.

In VS Code, this panel shows:

• modified files  
• staged changes  
• commit history  

Access it using the sidebar icon.

Example indicator:

```text
M main.py
```

This means the file has been modified.

---

## Staging Files

Before committing changes, files must be **staged**.

Staging tells Git which changes should be included in the commit.

Example staging workflow:

```text
Edit file
      ↓
Stage file
      ↓
Commit changes
```

In VS Code, staging can be done by clicking the **+ icon** next to the file.

---

## Commit Messages

After staging files, a commit message describes the change.

Example commit message:

```text
Added revenue calculation function
```

The message should clearly explain the purpose of the change.

---

# Decision Flow

Using Git in VS Code typically follows this workflow:

```text
Edit file
      ↓
View changes in Source Control
      ↓
Stage file
      ↓
Write commit message
      ↓
Commit changes
```

Example:

```text
Edit code → Stage → Commit
```

---

# Code Examples

## Example 1 — Initialize Repository

Command line equivalent:

```bash
git init
```

This creates the Git repository.

---

## Example 2 — Stage Files

Command line equivalent:

```bash
git add main.py
```

In VS Code, this is done by clicking the **stage icon**.

---

## Example 3 — Commit Changes

Command line equivalent:

```bash
git commit -m "Added cleaning function"
```

In VS Code, the commit message is entered in the Source Control panel.

---

## Example 4 — View Differences

Command line equivalent:

```bash
git diff
```

VS Code visually displays the file changes.

---

# SQL / Excel Comparison

Version control tools provide structured change tracking.

| Concept | Python/Git | SQL | Excel |
|------|------|------|------|
| change tracking | commit history | audit logs | version history |
| reviewing changes | diff | query history | compare workbook |
| collaboration | Git repo | shared database | shared workbook |

Example Excel workflow:

```text
report_v1.xlsx
report_v2.xlsx
report_v3.xlsx
```

Git replaces this with structured version control.

---

# Practice Exercises

## Exercise 1

Tags: Git, Best Practices

Open a Python project folder in VS Code.

Verify that the **Source Control panel** is active.

---

## Exercise 2

Tags: Git, Scripts

Modify a file such as:

```text
main.py
```

Observe how VS Code marks the change.

---

## Exercise 3

Tags: Transactions, Git, Git Workflow

Stage and commit the change.

Example commit message:

```text
Added data cleaning logic
```

---

# Common Mistakes

## Forgetting to Stage Files

Changes must be staged before committing.

Example workflow:

```text
Edit → Stage → Commit
```

Skipping staging prevents the commit from including the file.

---

## Poor Commit Messages

Example bad message:

```text
update
```

Better message:

```text
Added function to calculate monthly revenue
```

Clear messages help teams understand changes.

---

## Ignoring Git Indicators

VS Code highlights changed lines.

Ignoring these indicators may lead to committing unintended changes.

Always review changes before committing.

---

# Real-World Use

Most development teams use Git through an editor like VS Code.

Example workflow for a data project:

```text
Edit Python code
      ↓
VS Code detects change
      ↓
Stage change
      ↓
Commit change
      ↓
Push to Git repository
```

This workflow integrates development and version control into a single environment.

---

# Lesson Recap

In this lesson you learned:

• how Git integrates with VS Code  
• how to stage and commit changes using the Source Control panel  
• how VS Code displays file differences  
• how Git workflows operate inside an editor  

Using Git inside VS Code simplifies version control and makes it easier to manage code changes.

---

# Next Lesson

Next we will learn:

# Lesson 6 — Logging Basics

You will learn:

• what logging is  
• why logging is important for debugging and monitoring  
• how to implement logging in Python scripts  

Logging is essential for **tracking program behavior and diagnosing issues in production systems**.
