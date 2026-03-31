# Module 11 — Python Engineering Handbook

# Lesson 1 — Python Project Template

---

# Lesson Objective

By the end of this lesson learners will understand:

• what a **Python project template** is  
• how professional Python projects are structured  
• how project templates improve maintainability  
• how teams standardize project organization  

Professional development teams use standardized project structures to ensure that projects remain **organized, maintainable, and scalable**.

---

# Overview

When beginners write Python programs, the project structure often looks like this:

```text
project/
│
├── script.py
├── data.csv
```

This works for small scripts but becomes difficult to manage as projects grow.

Example larger project:

```text
analytics_project/
│
├── main.py
├── process_data.py
├── utils.py
├── config.py
├── data/
│   └── sales.csv
```

Without organization, projects become difficult to maintain.

Professional teams use standardized project templates.

Example professional structure:

```text
analytics_project/
│
├── src/
│   ├── pipeline.py
│   ├── analytics.py
│   └── data_loader.py
│
├── tests/
│
├── config/
│
├── data/
│
├── requirements.txt
├── README.md
└── pyproject.toml
```

This structure separates different responsibilities within the project.

---

# Key Idea Cards (3 Cards)

### Project Structure Improves Organization

Well-structured projects are easier to maintain.

Example organization:

```text
src → application code
tests → automated tests
data → datasets
config → configuration
```

This separation makes projects easier to navigate.

---

### Templates Standardize Development

Project templates ensure that every project follows the same structure.

Benefits include:

• easier onboarding  
• consistent architecture  
• improved collaboration.

---

### Templates Reduce Setup Time

Instead of creating project structures from scratch, developers can reuse templates.

Example workflow:

```text
Create new project
      ↓
Copy project template
      ↓
Begin development
```

This accelerates development.

---

# Key Concepts

## Source Code Directory

Most professional Python projects store source code in a dedicated folder.

Example:

```text
src/
```

This prevents code from being mixed with configuration or data files.

---

## Tests Directory

Tests are stored in a dedicated folder.

Example:

```text
tests/
```

This keeps test code separate from application logic.

---

## Configuration Directory

Configuration files may be stored separately.

Example:

```text
config/
```

This directory may contain:

• environment configuration  
• pipeline settings  
• application configuration.

---

# Decision Flow

Developers typically organize projects using this logic:

```text
Is the project small?
        ↓
Maybe simple structure is OK
        ↓
Is project growing?
        ↓
Use standardized project template
```

Project templates become essential as projects scale.

---

# Code Examples

### Example 1 — Minimal Project Structure

```text
project/
│
├── main.py
└── requirements.txt
```

This works for small scripts.

---

### Example 2 — Professional Project Structure

```text
project/
│
├── src/
│   └── main.py
│
├── tests/
│
├── config/
│
├── requirements.txt
└── README.md
```

This structure supports larger projects.

---

### Example 3 — Example Source Code File

```python
# src/pipeline.py

def run_pipeline():
    print("Extract")
    print("Transform")
    print("Load")
```

---

### Example 4 — Running the Application

```python
from src.pipeline import run_pipeline

run_pipeline()
```

This imports the pipeline from the source directory.

---

# SQL / Excel Comparison

Project structure concepts also exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| project organization | directories | schema structure | workbook organization |
| reusable logic | modules | stored procedures | VBA modules |
| configuration | config files | database settings | workbook settings |

Example SQL project:

```text
database_project/
│
├── schema/
├── procedures/
└── queries/
```

Structured organization improves maintainability.

---

# Practice Exercises

### Exercise 1

Tags: Testing, Data Engineering

Create the following project structure:

```text
project/
│
├── src/
├── tests/
├── data/
├── config/
└── README.md
```

---

### Exercise 2

Tags: Scripts, Data Engineering

Create a simple Python script inside `src`.

---

### Exercise 3

Tags: Data Engineering, Python

Write a README describing the project.

---

### Exercise 4

Tags: Dependencies, Data Engineering

Add a `requirements.txt` file listing project dependencies.

---

# Common Mistakes

### Mixing Code and Data

Avoid storing data files directly alongside source code.

Better approach:

```text
data/
```

---

### No Documentation

Projects should always include:

```text
README.md
```

Documentation helps developers understand the project.

---

### Inconsistent Project Structures

Teams should standardize project templates to maintain consistency.

---

# Real-World Use

Project templates are widely used in professional software development.

Example data project:

```text
analytics_platform/
│
├── src/
├── tests/
├── pipelines/
├── config/
├── requirements.txt
└── README.md
```

Benefits include:

• consistent architecture  
• easier onboarding for new developers  
• improved maintainability.

Large organizations often maintain **internal project templates** that all teams use.

---

# Lesson Recap

In this lesson you learned:

• what Python project templates are  
• how projects are organized in professional environments  
• why standardized structures improve maintainability  
• how templates accelerate development.

Project templates help teams build **organized and scalable Python applications**.

---

# Next Lesson

Next we will continue Module 11 with:

# Lesson 2 — Python Code Style Guide

You will learn:

• how teams standardize Python code style  
• why readability matters in professional code  
• how formatting tools enforce coding standards  
• best practices for writing clean Python code.
