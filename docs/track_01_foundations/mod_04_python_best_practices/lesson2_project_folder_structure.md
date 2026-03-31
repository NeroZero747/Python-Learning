# Module 5 — Writing Cleaner Python Code

# Lesson 3 — Project Folder Structure

---

# Lesson Objective

By the end of this lesson learners will understand:

• why project folder structure matters  
• how to organize Python projects into logical folders  
• how separating scripts improves maintainability  
• what a typical analytics project structure looks like  

Organizing projects properly is important because real data projects often contain **many scripts, datasets, and configuration files**.

---

# Overview

When beginners start learning Python, they often place everything in one file.

Example:

```text
analysis.py
```

Inside this file might be:

• database connections  
• data cleaning logic  
• calculations  
• export logic  
• reporting code  

This works for small experiments, but as projects grow it becomes difficult to maintain.

A better approach is to organize projects into **folders and modules**.

Example organized project:

```text
project
│
├── main.py
├── data
│   └── sales.csv
├── modules
│   ├── cleaning.py
│   ├── calculations.py
│   └── exports.py
└── config
    └── settings.py
```

This structure separates responsibilities and keeps code easier to manage.

Benefits include:

• easier navigation  
• reusable components  
• better collaboration  
• easier debugging  

Professional Python projects almost always use **structured folders**.

---

# Key Idea Cards (3 Cards)

## Organized Projects Are Easier to Maintain

When projects grow large, organization becomes essential.

Example messy project:

```text
analysis_script_final_v3.py
analysis_script_final_v4.py
analysis_script_final_final.py
```

This quickly becomes confusing.

Structured folders solve this problem.

---

## Separate Responsibilities Into Different Files

Different types of code should live in different modules.

Example:

```text
cleaning.py
database.py
calculations.py
exports.py
```

Each module handles one responsibility.

---

## Clear Structure Improves Collaboration

When multiple analysts work on the same project, a clear structure helps everyone understand the codebase.

Example team structure:

```text
project
├── notebooks
├── scripts
├── modules
└── data
```

This helps teams navigate projects quickly.

---

# Key Concepts

## Project Root

The **project root** is the main folder containing the project.

Example:

```text
sales_analysis_project
```

Inside this folder are scripts, modules, and data.

---

## Modules Folder

Reusable code should live in a **modules** folder.

Example:

```text
modules
│
├── cleaning.py
├── calculations.py
└── exports.py
```

Each module contains reusable functions.

---

## Data Folder

Raw data should be stored separately from code.

Example:

```text
data
│
├── raw
└── processed
```

This keeps datasets organized.

---

# Decision Flow

Creating a project structure usually follows this process:

```text
Start new project
      ↓
Create project folder
      ↓
Create folders for modules and data
      ↓
Move reusable code into modules
      ↓
Run workflow from main script
```

Example:

```text
project
│
├── main.py
├── modules
└── data
```

---

# Code Examples

## Example 1 — Small Project Structure

```text
project
│
├── main.py
├── cleaning.py
└── calculations.py
```

---

## Example 2 — Organized Project Structure

```text
sales_project
│
├── main.py
├── modules
│   ├── cleaning.py
│   ├── calculations.py
│   └── exports.py
│
├── data
│   ├── raw
│   └── processed
│
└── config
    └── settings.py
```

---

## Example 3 — Using Modules from the Folder

```python
from modules.cleaning import clean_names
from modules.calculations import calculate_total
```

This imports functions from the module folder.

---

## Example 4 — Running the Main Script

```python
from modules.calculations import calculate_total

result = calculate_total(10, 5)

print(result)
```

The **main script controls the workflow**, while modules provide reusable logic.

---

# SQL / Excel Comparison

Project structure concepts also exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| project folder | project directory | database schema | workbook |
| modules | reusable scripts | stored procedures | macros |
| main script | pipeline script | scheduled job | macro runner |

Example SQL organization:

```sql
schema
│
├── procedures
├── tables
└── views
```

Python projects follow a similar organization approach.

---

# Practice Exercises

## Exercise 1

Tags: Best Practices, Code Quality

Create a project folder.

```text
sales_project
```

Inside create folders:

```text
modules
data
```

---

## Exercise 2

Tags: Scripts, Arithmetic

Create a module file.

```text
modules/calculations.py
```

Add a reusable function.

---

## Exercise 3

Tags: Imports, Scripts, Arithmetic

Import the module into the main script.

```python
from modules.calculations import calculate_total
```

Run the script.

---

# Common Mistakes

## Keeping Everything in One File

Example:

```text
analysis_script.py
```

This becomes difficult to maintain as the project grows.

---

## Mixing Data Files with Code

Incorrect structure:

```text
project
│
├── main.py
├── data.csv
├── script2.py
```

Better structure:

```text
project
│
├── data
│   └── data.csv
└── main.py
```

---

## Inconsistent Folder Naming

Example:

```text
Data
data_files
DATA
```

Consistency improves readability.

---

# Real-World Use

Most professional Python projects use structured folders.

Example analytics project:

```text
claims_analysis
│
├── main.py
├── modules
│   ├── claims_cleaning.py
│   ├── risk_calculations.py
│   └── exports.py
│
├── data
│   ├── raw_claims
│   └── processed_claims
│
└── config
    └── database_settings.py
```

This structure allows teams to scale projects easily.

---

# Lesson Recap

In this lesson you learned:

• why project folder structure is important  
• how Python projects organize code and data  
• how modules fit into project structure  
• how structured projects improve maintainability  

Good project organization is a key step toward **professional Python development**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Introduction to Git (Simple Workflow)

You will learn:

• what version control is  
• why Git is important for code management  
• how basic Git workflows work  

This is an important skill because nearly all modern development projects use **version control systems**.
