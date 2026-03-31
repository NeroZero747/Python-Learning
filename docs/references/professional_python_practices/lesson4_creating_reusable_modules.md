# Module 9 — Professional Python Practices

# Lesson 4 — Creating Reusable Modules

---

# Lesson Objective

By the end of this lesson learners will understand:

• what a **reusable module** is  
• how to design modules that can be reused across multiple programs  
• how to organize functions inside modules  
• how modules reduce duplicated code in large projects  

Reusable modules are one of the most important tools in professional Python development because they allow developers to **write code once and reuse it across many scripts or applications**.

---

# Overview

When beginners write Python scripts, they often repeat the same logic multiple times.

Example:

```python
import pandas as pd

data = pd.read_csv("sales.csv")
west = data[data["region"] == "West"]

print(west)
```

Later they may write another script that performs similar logic.

```python
import pandas as pd

data = pd.read_csv("orders.csv")
east = data[data["region"] == "East"]

print(east)
```

This approach leads to **duplicated code**.

Problems with duplicated code include:

• harder maintenance  
• inconsistent logic  
• bugs that must be fixed in multiple places.

Instead, developers create **reusable modules** that centralize shared logic.

Example reusable module:

```python
def filter_region(data, region):
    return data[data["region"] == region]
```

Now this function can be used anywhere in the project.

---

# Key Idea Cards (3 Cards)

### Modules Reduce Duplicate Code

Instead of rewriting logic repeatedly, developers place common functions into modules.

Example:

```text
filter_region()
load_data()
calculate_metrics()
```

These functions can be reused across multiple scripts.

---

### Modules Improve Code Organization

Modules group related functionality together.

Example:

```text
data_loader.py
analytics.py
visualization.py
```

Each module has a clear purpose.

---

### Modules Make Projects Scalable

As projects grow, modules allow developers to add new features without creating large, unmanageable scripts.

Example growth path:

```text
Small Script
     ↓
Multiple Modules
     ↓
Large Application
```

This approach allows Python systems to scale effectively.

---

# Key Concepts

## What Is a Module?

A **module** is a Python file containing reusable functions, classes, or variables.

Example module file:

```text
analytics.py
```

Example code inside the module:

```python
def calculate_total_sales(data):
    return data["sales"].sum()
```

Other scripts can import and use this function.

---

## Importing Modules

Python allows importing functions from modules.

Example:

```python
from analytics import calculate_total_sales
```

This makes the function available in the script.

---

## Organizing Module Functions

Modules often group related functionality.

Example analytics module:

```python
def filter_region(data, region):
    return data[data["region"] == region]

def calculate_total_sales(data):
    return data["sales"].sum()
```

These functions all relate to analytics operations.

---

# Decision Flow

Developers often decide whether to create a module using this logic:

```text
Will this logic be reused?
        ↓
       YES
        ↓
Create a reusable module
```

Reusable modules prevent code duplication.

---

# Code Examples

### Example 1 — Script Without Modules

```python
import pandas as pd

data = pd.read_csv("sales.csv")

west_sales = data[data["region"] == "West"]

total_sales = west_sales["sales"].sum()

print(total_sales)
```

If this logic is used in multiple scripts, duplication occurs.

---

### Example 2 — Creating a Module

**analytics.py**

```python
def filter_region(data, region):
    return data[data["region"] == region]

def calculate_total_sales(data):
    return data["sales"].sum()
```

---

### Example 3 — Using the Module

**app.py**

```python
import pandas as pd
from analytics import filter_region, calculate_total_sales

data = pd.read_csv("sales.csv")

west_sales = filter_region(data, "West")

total = calculate_total_sales(west_sales)

print(total)
```

Now the logic is centralized.

---

### Example 4 — Creating a Data Loader Module

**data_loader.py**

```python
import pandas as pd

def load_sales_data(file_path):
    return pd.read_csv(file_path)
```

Usage:

```python
from data_loader import load_sales_data

data = load_sales_data("sales.csv")
```

This makes data loading reusable across scripts.

---

# SQL / Excel Comparison

Reusable modules have equivalents in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| reusable logic | modules/functions | stored procedures | VBA modules |
| shared calculations | functions | views | formulas |
| code organization | project structure | database objects | workbook modules |

Example SQL stored procedure:

```sql
CREATE PROCEDURE get_west_sales
AS
SELECT *
FROM sales
WHERE region = 'West';
```

This provides reusable query logic similar to Python modules.

---

# Practice Exercises

### Exercise 1

Tags: Lists, Tuples, Functions, Scripts

Create a module called **analytics.py**.

Add a function:

```python
def filter_region(data, region):
    return data[data["region"] == region]
```

---

### Exercise 2

Tags: Lists, Functions, Aggregations, Arithmetic

Create a function to calculate total sales.

```python
def calculate_total_sales(data):
    return data["sales"].sum()
```

---

### Exercise 3

Tags: Imports, Scripts

Import your module into a script.

```python
from analytics import filter_region
```

Use the function to filter a dataset.

---

# Common Mistakes

### Copying Code Instead of Creating Modules

Repeated code leads to maintenance problems.

Better approach:

```text
Create reusable modules
```

---

### Creating Modules That Are Too Large

Modules should focus on a single responsibility.

Example structure:

```text
data_loader.py
analytics.py
visualization.py
```

Avoid placing all functions in a single large module.

---

### Poor Module Naming

Modules should clearly describe their purpose.

Examples:

```text
data_loader.py
analytics.py
metrics.py
```

Avoid vague names like:

```text
helpers.py
misc.py
stuff.py
```

---

# Real-World Use

Reusable modules are essential in professional Python systems.

Example analytics project structure:

```text
analytics_project/
│
├── app.py
├── src/
│   ├── data_loader.py
│   ├── analytics.py
│   ├── metrics.py
│   └── visualization.py
└── data/
    └── sales.csv
```

Benefits:

• reusable logic  
• easier debugging  
• faster development  
• better collaboration.

Modules are heavily used in:

• data engineering pipelines  
• machine learning systems  
• analytics platforms  
• production software applications.

---

# Lesson Recap

In this lesson you learned:

• what reusable modules are  
• how modules reduce duplicate code  
• how modules organize project logic  
• how functions inside modules can be reused across scripts.

Reusable modules allow developers to **build scalable and maintainable Python systems**.

---

# Next Lesson

Next we will learn:

# Lesson 5 — Dependency Management

You will learn:

• how Python projects manage external libraries  
• how **requirements.txt** works  
• how virtual environments isolate dependencies  
• how teams ensure consistent environments across machines.
