# Module 11 — Python Engineering Handbook

# Lesson 2 — Python Code Style Guide

---

# Lesson Objective

By the end of this lesson learners will understand:

• why **code style standards** are important in professional Python projects  
• what **PEP 8** is and how it guides Python formatting  
• how teams enforce consistent code style  
• tools used to automatically format Python code  

Consistent code style ensures that Python programs remain **readable, maintainable, and collaborative** when multiple developers work on the same project.

---

# Overview

When developers write Python code without any formatting standards, code can become inconsistent and difficult to read.

Example of poorly formatted code:

```python
def calc(a,b):return a+b
```

This code works but is difficult to read.

Better formatted version:

```python
def calculate_total(a, b):
    return a + b
```

Professional development teams follow **coding standards** to keep code consistent across projects.

The official Python style guide is called:

```text
PEP 8
```

PEP stands for **Python Enhancement Proposal**.

PEP 8 provides recommendations for:

• naming conventions  
• indentation  
• line length  
• spacing  
• file structure.

Following a consistent style improves collaboration and readability.

---

# Key Idea Cards (3 Cards)

### Code Readability Is Critical

Python emphasizes readability.

Example:

```python
total_sales = calculate_total(data)
```

Readable code helps developers understand logic quickly.

---

### Teams Use Coding Standards

Coding standards ensure all developers write code consistently.

Example standards:

```text
Function naming
Variable naming
File structure
Formatting
```

This prevents style inconsistencies.

---

### Formatting Tools Automate Style

Developers often use tools to automatically format code.

Common tools include:

```text
Black
Flake8
isort
```

These tools enforce coding standards automatically.

---

# Key Concepts

## PEP 8

PEP 8 is the official Python style guide.

It defines recommendations for writing Python code.

Example guidelines include:

```text
Use 4 spaces for indentation
Limit lines to ~79 characters
Use descriptive variable names
```

PEP 8 helps maintain consistency across Python projects.

---

## Naming Conventions

PEP 8 recommends using **snake_case** for functions and variables.

Example:

```python
total_sales
calculate_average
load_customer_data
```

Class names use **PascalCase**.

Example:

```python
SalesProcessor
CustomerAnalytics
```

---

## Line Length

PEP 8 recommends keeping lines under 79 characters.

Example:

Bad:

```python
result = calculate_total_sales_for_all_regions_and_customer_segments(data)
```

Better:

```python
result = calculate_total_sales(
    data
)
```

Breaking long lines improves readability.

---

# Decision Flow

Developers typically follow this workflow for maintaining code style:

```text
Write code
     ↓
Run formatter
     ↓
Run linter
     ↓
Commit code
```

Formatting tools automatically enforce standards.

---

# Code Examples

### Example 1 — Poor Formatting

```python
def calcSales(data):return sum(data)
```

Problems:

• unclear function name  
• missing spacing  
• poor readability.

---

### Example 2 — PEP 8 Formatting

```python
def calculate_sales(data):
    return sum(data)
```

This version is easier to read.

---

### Example 3 — Proper Naming Conventions

Variables:

```python
total_sales
average_price
customer_count
```

Functions:

```python
load_sales_data()
calculate_metrics()
generate_report()
```

Classes:

```python
SalesAnalyzer
CustomerReport
```

---

### Example 4 — Using Black Formatter

Install Black:

```bash
pip install black
```

Format a file:

```bash
black script.py
```

Black automatically formats the code according to consistent style rules.

---

# SQL / Excel Comparison

Code style principles exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| formatting | PEP 8 | SQL formatting standards | formula formatting |
| naming conventions | snake_case | table naming conventions | named ranges |
| code consistency | linters | SQL style guides | workbook conventions |

Example SQL formatting:

Bad:

```sql
select*from sales where region='west'
```

Better:

```sql
SELECT *
FROM sales
WHERE region = 'west'
```

Readable formatting improves maintainability.

---

# Practice Exercises

### Exercise 1

Tags: Tuples, Functions

Rewrite poorly formatted code:

```python
def calc(a,b):return a+b
```

Improve the formatting and naming.

---

### Exercise 2

Tags: Variables, Data Engineering

Rename variables using snake_case.

Example:

```python
TotalSales
```

Rewrite as:

```python
total_sales
```

---

### Exercise 3

Tags: pip install, Scripts, Code Quality

Install and run Black on a Python file.

```bash
pip install black
black script.py
```

---

### Exercise 4

Tags: Data Engineering, Python

Review your existing Python code and apply PEP 8 formatting guidelines.

---

# Common Mistakes

### Ignoring Code Style

Inconsistent formatting makes code difficult to read and maintain.

Teams should enforce style guidelines.

---

### Overly Complex Function Names

Names should be descriptive but not excessively long.

Example:

Bad:

```python
calculate_total_sales_for_all_regions_and_customers()
```

Better:

```python
calculate_total_sales()
```

---

### Mixing Naming Styles

Avoid mixing styles such as:

```python
totalSales
total_sales
TotalSales
```

Use consistent naming conventions.

---

# Real-World Use

Code style guidelines are essential in professional development environments.

Example team workflow:

```text
Developer writes code
       ↓
Formatter runs automatically
       ↓
Code review checks style
       ↓
Code merged into repository
```

Many organizations enforce formatting rules using CI pipelines.

Example tools used in production systems:

```text
Black
Flake8
Pre-commit hooks
```

These tools ensure code remains **clean, readable, and consistent**.

---

# Lesson Recap

In this lesson you learned:

• what the Python style guide (PEP 8) is  
• how consistent formatting improves readability  
• how naming conventions work  
• how formatting tools enforce coding standards.

Code style guidelines ensure Python programs remain **clear, maintainable, and collaborative**.

---

# Next Lesson

Next we will continue Module 11 with:

# Lesson 3 — Logging Standards

You will learn:

• how teams standardize logging practices  
• how logs are structured in production systems  
• how logging improves system observability  
• how to design effective logging strategies.
