# Module 9 — Professional Python Practices

# Lesson 2 — Writing Clean Python Code

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **clean code** means in Python  
• Python naming conventions and formatting standards  
• how to structure readable Python scripts  
• how clean code improves maintainability and collaboration  

Writing clean code is one of the most important habits for professional developers. Clean code allows others to **quickly understand, modify, and extend your work**.

---

# Overview

When learning Python, developers often focus on **making the code work**.

Example beginner script:

```python
import pandas as pd
df=pd.read_csv("sales.csv")
x=df[df["region"]=="West"]
print(x)
```

This script runs correctly, but it has several problems:

• variable names are unclear  
• spacing is inconsistent  
• logic is not organized  
• the code is difficult to read.

Professional Python code follows style guidelines that improve readability.

Example clean version:

```python
import pandas as pd

sales_data = pd.read_csv("sales.csv")

west_region_sales = sales_data[sales_data["region"] == "West"]

print(west_region_sales)
```

This version is easier to understand because:

• variable names are descriptive  
• formatting is consistent  
• logic is clearly separated.

Clean code helps developers quickly understand what a program is doing.

---

# Key Idea Cards (3 Cards)

### Clean Code Prioritizes Readability

Code should be written for humans to read, not just for computers to execute.

Example comparison:

```python
x=df[df["region"]=="West"]
```

vs

```python
west_region_sales = sales_data[sales_data["region"] == "West"]
```

The second example clearly explains the purpose of the variable.

---

### Consistent Style Improves Team Collaboration

When all developers follow the same coding style:

• codebases become easier to maintain  
• developers can switch between projects easily  
• bugs become easier to identify.

Python’s official style guide is called **PEP 8**.

---

### Small Functions Improve Clarity

Instead of writing large scripts, developers break logic into small functions.

Example:

```python
def load_data(file_path):
    return pd.read_csv(file_path)
```

Small functions make code easier to test and reuse.

---

# Key Concepts

## PEP 8 Style Guide

PEP 8 is the official Python style guide that defines conventions for writing readable code.

Examples include:

• naming conventions  
• indentation rules  
• spacing guidelines  
• line length limits.

Following these guidelines ensures consistent code across projects.

---

## Naming Conventions

Python typically uses **snake_case** for variable and function names.

Example:

```python
total_sales
customer_count
calculate_average
```

Avoid names like:

```python
TotalSales
x
data1
```

Descriptive names make code easier to understand.

---

## Indentation

Python uses indentation to define code blocks.

Standard indentation uses **4 spaces**.

Example:

```python
if region == "West":
    print("West region selected")
```

Incorrect indentation will cause Python errors.

---

## Line Length

PEP 8 recommends limiting lines to **79 characters**.

Long lines reduce readability.

Example:

```python
filtered_sales = sales_data[
    sales_data["region"] == "West"
]
```

Breaking lines improves clarity.

---

# Decision Flow

Developers often review code using this checklist:

```text
Is the variable name descriptive?
        ↓
Is the code easy to read?
        ↓
Is the logic organized into functions?
        ↓
Does the code follow PEP 8 style?
```

If the answer is yes to these questions, the code is likely well written.

---

# Code Examples

### Example 1 — Poor Naming

```python
import pandas as pd

df = pd.read_csv("sales.csv")

x = df[df["region"] == "West"]
```

Problems:

• variable names lack meaning  
• code intent is unclear.

---

### Example 2 — Improved Naming

```python
import pandas as pd

sales_data = pd.read_csv("sales.csv")

west_region_sales = sales_data[sales_data["region"] == "West"]
```

Clear naming immediately explains the code’s purpose.

---

### Example 3 — Breaking Code into Functions

Instead of writing one large script:

```python
import pandas as pd

data = pd.read_csv("sales.csv")
filtered = data[data["region"] == "West"]

print(filtered)
```

Create reusable functions.

```python
import pandas as pd

def load_sales_data(file_path):
    return pd.read_csv(file_path)

def filter_region(data, region):
    return data[data["region"] == region]

sales_data = load_sales_data("sales.csv")

west_sales = filter_region(sales_data, "West")

print(west_sales)
```

This approach improves readability and reuse.

---

### Example 4 — Proper Spacing

Incorrect spacing:

```python
total=df["sales"].sum()
```

Correct spacing:

```python
total = df["sales"].sum()
```

Spacing improves readability.

---

# SQL / Excel Comparison

Code organization principles also exist in SQL and Excel.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| naming clarity | descriptive variables | readable table aliases | named ranges |
| formatting | PEP 8 spacing | formatted queries | organized worksheets |
| modular logic | functions | stored procedures | reusable formulas |

Example SQL comparison:

Poor SQL:

```sql
SELECT * FROM sales WHERE region='West'
```

Better SQL:

```sql
SELECT order_id, sales_amount
FROM sales
WHERE region = 'West'
```

Clear formatting improves readability.

---

# Practice Exercises

### Exercise 1

Tags: print(), Lists, read_csv(), CSV

Rewrite the following code with better formatting.

```python
df=pd.read_csv("sales.csv")
x=df[df["region"]=="West"]
print(x)
```

---

### Exercise 2

Tags: Lists, read_csv(), CSV, Variables

Rename the variables to improve clarity.

```python
data = pd.read_csv("sales.csv")
filtered = data[data["region"] == "East"]
```

---

### Exercise 3

Tags: Functions, read_csv(), File I/O, Data I/O

Create a function that loads a dataset.

Example:

```python
def load_data(file_path):
    return pd.read_csv(file_path)
```

---

# Common Mistakes

### Ignoring Formatting

Messy formatting makes code difficult to read.

Always follow consistent spacing and indentation.

---

### Overly Long Scripts

Scripts with hundreds of lines become difficult to maintain.

Better approach:

```text
Break code into functions
```

---

### Using Vague Variable Names

Avoid variables like:

```python
x
data1
temp
```

Use descriptive names instead.

---

# Real-World Use

In professional environments, clean code allows teams to collaborate effectively.

Example development workflow:

```text
Developer A writes data pipeline
      ↓
Developer B adds new feature
      ↓
Developer C debugs issue
```

If the code is clean and well structured, each developer can quickly understand the system.

Clean code becomes essential for:

• data pipelines  
• analytics applications  
• machine learning systems  
• enterprise software.

---

# Lesson Recap

In this lesson you learned:

• what clean Python code looks like  
• how naming conventions improve readability  
• how PEP 8 defines Python coding style  
• how modular code improves maintainability.

Clean code is the foundation for **professional Python development**.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Python Project Structure

You will learn:

• how professional Python projects are organized  
• how folders and modules are structured  
• how to separate scripts, libraries, and configuration  
• how large Python projects are maintained.
