# Module 9 — Professional Python Practices

# Lesson 1 — Why Code Quality Matters

---

# Lesson Objective

By the end of this lesson learners will understand:

• why code quality matters in professional environments  
• the risks of poorly written scripts  
• how maintainable code improves collaboration  
• the principles that guide professional Python development

Code quality becomes extremely important when Python scripts move from **personal experimentation** to **production systems used by teams**.

---

# Overview

When people first learn Python, they often write small scripts like this:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df = df[df["region"] == "West"]

print(df)
```

For learning purposes, this works fine.

However, problems appear when scripts become larger.

Example real-world workflow:

```text
Data Pipeline
    ↓
Processing Script
    ↓
Analytics Dashboard
    ↓
Business Users
```

If the code is messy or poorly structured:

• bugs are harder to find  
• new developers cannot understand the code  
• changes break existing functionality  
• systems become difficult to maintain.

Professional software development focuses heavily on **code quality** because well-written code:

• is easier to understand  
• is easier to maintain  
• reduces bugs  
• improves team productivity.

---

# Key Idea Cards (3 Cards)

### Code Is Read More Than It Is Written

Developers spend far more time **reading code** than writing it.

Example workflow:

```text
Write code once
Read code many times
```

Clear code makes future work easier.

---

### Maintainable Code Saves Time

When code is easy to understand, teams can quickly:

• add new features  
• fix bugs  
• extend functionality.

Poor code slows development dramatically.

---

### Code Quality Enables Collaboration

When multiple developers work on the same project, consistency becomes essential.

Good practices include:

• consistent naming  
• modular code structure  
• clear documentation.

These practices allow teams to collaborate effectively.

---

# Key Concepts

## Readability

Readable code is easy for other developers to understand.

Example:

Poor readability:

```python
a=df[df["region"]=="West"]
```

Better readability:

```python
west_region_sales = df[df["region"] == "West"]
```

Clear variable names improve understanding.

---

## Maintainability

Maintainable code can be updated or extended without major rewrites.

Example improvements:

• modular functions  
• organized project structure  
• separation of responsibilities.

---

## Reusability

Reusable code can be used in multiple programs.

Example:

Instead of copying logic across scripts, developers create reusable functions.

```python
def filter_region(data, region):
    return data[data["region"] == region]
```

This function can be reused anywhere.

---

# Decision Flow

Developers often evaluate code quality with this simple logic:

```text
Can another developer understand this code quickly?
        ↓
       YES
        ↓
Good code quality

        NO
        ↓
Needs improvement
```

If the code requires significant explanation, it may need refactoring.

---

# Code Examples

### Example 1 — Poorly Structured Code

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df = df[df["region"] == "West"]

df["tax"] = df["sales"] * 0.08

print(df)
```

Problems:

• no function structure  
• hardcoded logic  
• difficult to reuse.

---

### Example 2 — Improved Structure

```python
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def filter_region(data, region):
    return data[data["region"] == region]

def calculate_tax(data):
    data["tax"] = data["sales"] * 0.08
    return data

sales_data = load_data("sales.csv")
west_sales = filter_region(sales_data, "West")
result = calculate_tax(west_sales)

print(result)
```

This version is easier to read and maintain.

---

### Example 3 — Clear Naming

Poor variable naming:

```python
d = pd.read_csv("sales.csv")
```

Better naming:

```python
sales_data = pd.read_csv("sales.csv")
```

Descriptive names improve clarity.

---

### Example 4 — Adding Comments

```python
# Load sales dataset
sales_data = pd.read_csv("sales.csv")

# Filter west region records
west_sales = sales_data[sales_data["region"] == "West"]
```

Comments help explain code intent.

---

# SQL / Excel Comparison

Code quality concepts exist in other tools as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| structure | functions/modules | stored procedures | workbook organization |
| readability | clear variable names | readable queries | named ranges |
| reuse | functions | views | formulas/templates |

Example SQL comparison:

Poor SQL:

```sql
SELECT * FROM orders WHERE region='West'
```

Better SQL:

```sql
SELECT order_id, sales_amount
FROM orders
WHERE region = 'West'
```

Readable code improves maintainability in any language.

---

# Practice Exercises

### Exercise 1

Tags: Lists, read_csv(), CSV, Variables

Rewrite the following code using clearer variable names:

```python
df = pd.read_csv("sales.csv")
x = df[df["region"]=="West"]
```

---

### Exercise 2

Tags: Lists, Code Quality

Convert the following logic into a reusable function:

```python
df = df[df["region"] == "East"]
```

---

### Exercise 3

Tags: Scripts, Code Quality

Add comments explaining the purpose of each step in a script.

---

# Common Mistakes

### Writing Extremely Long Scripts

Large scripts become difficult to maintain.

Better approach:

```text
Break logic into functions
```

---

### Using Vague Variable Names

Avoid names like:

```python
x
data1
temp
```

Use descriptive names instead.

---

### Copying Code Instead of Reusing It

Repeated code increases maintenance cost.

Better approach:

```text
Create reusable functions
```

---

# Real-World Use

In professional environments, code quality matters because systems grow quickly.

Example data workflow:

```text
Raw Data
   ↓
ETL Scripts
   ↓
Data Warehouse
   ↓
Dashboards
   ↓
Business Decisions
```

If ETL code is poorly written:

• data pipelines break easily  
• debugging takes longer  
• system reliability decreases.

High-quality code helps teams maintain complex systems.

---

# Lesson Recap

In this lesson you learned:

• why code quality matters  
• how readability improves collaboration  
• how modular code improves maintainability  
• how professional developers structure Python code.

These principles form the foundation of **professional Python development**.

---

# Next Lesson

Next we will learn:

# Lesson 2 — Writing Clean Python Code

You will learn:

• Python style guidelines  
• naming conventions  
• organizing functions and logic  
• how developers write production-quality Python code.
