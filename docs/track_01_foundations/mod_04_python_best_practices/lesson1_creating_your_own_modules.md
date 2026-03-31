# Module 5 — Writing Cleaner Python Code

# Lesson 2 — Creating Your Own Modules

---

# Lesson Objective

By the end of this lesson learners will understand:

• what a Python module is  
• how to move reusable functions into separate files  
• how modules help organize larger programs  
• how to import functions from modules  

Modules are essential because they help transform simple scripts into **organized, scalable Python projects**.

---

# Overview

As Python scripts grow larger, putting everything in a single file becomes difficult to maintain.

Example large script:

```python
def clean_names(name):
    return name.strip().title()

def calculate_total(price, quantity):
    return price * quantity

def format_city(city):
    return city.upper()

# analysis code here
```

This works, but when projects grow to **hundreds or thousands of lines**, scripts become hard to read and maintain.

Python solves this problem using **modules**.

A **module** is simply a Python file that contains reusable code.

Example module file:

```text
utils.py
```

Inside the module:

```python
def clean_names(name):
    return name.strip().title()

def calculate_total(price, quantity):
    return price * quantity
```

Now the module can be imported into another script.

Example main script:

```python
import utils

print(utils.calculate_total(10, 5))
```

Output:

```text
50
```

Modules allow projects to be split into **logical components**, making code easier to maintain and reuse.

---

# Key Idea Cards (3 Cards)

## Modules Are Python Files

A module is simply a `.py` file that contains functions, variables, or classes.

Example file:

```text
math_utils.py
```

Inside:

```python
def calculate_total(price, quantity):
    return price * quantity
```

---

## Modules Help Organize Large Projects

Instead of putting everything in one script:

```text
main.py
```

We can organize code like this:

```text
main.py
data_cleaning.py
calculations.py
exports.py
```

Each file handles a different responsibility.

---

## Modules Enable Reusable Code Across Projects

Once a module exists, it can be reused across multiple scripts.

Example:

```python
import calculations
```

This allows the same logic to be shared across projects.

---

# Key Concepts

## Creating a Module

To create a module, simply create a Python file.

Example:

```text
math_utils.py
```

Inside the file:

```python
def multiply(a, b):
    return a * b
```

Now the module can be imported.

---

## Importing a Module

Example:

```python
import math_utils

result = math_utils.multiply(4, 5)

print(result)
```

Output:

```text
20
```

The module name acts like a namespace.

---

## Importing Specific Functions

Sometimes you only need one function from a module.

Example:

```python
from math_utils import multiply

print(multiply(4, 5))
```

This allows direct access to the function.

---

# Decision Flow

Organizing code with modules typically follows this pattern:

```text
Write reusable functions
      ↓
Move functions into module file
      ↓
Import module into main script
      ↓
Call module functions
```

Example:

```python
from math_utils import multiply

multiply(3, 4)
```

---

# Code Examples

## Example 1 — Single Script

```python
def calculate_total(price, quantity):
    return price * quantity

print(calculate_total(10, 5))
```

This works but becomes messy in larger scripts.

---

## Example 2 — Creating a Module

File: **sales_utils.py**

```python
def calculate_total(price, quantity):
    return price * quantity
```

---

## Example 3 — Importing the Module

Main script:

```python
import sales_utils

print(sales_utils.calculate_total(10, 5))
```

---

## Example 4 — Importing a Specific Function

```python
from sales_utils import calculate_total

print(calculate_total(10, 5))
```

---

# SQL / Excel Comparison

Modules are conceptually similar to reusable components in SQL or Excel.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| reusable logic | module | stored procedure | macro |
| reusable functions | function | user-defined function | custom formula |
| organization | module file | schema | workbook structure |

Example SQL reusable logic:

```sql
CREATE FUNCTION calculate_total(price, quantity)
RETURNS INT
```

Example Excel reusable macro:

```text
VBA Macro
```

Python modules provide a similar reusable structure.

---

# Practice Exercises

## Exercise 1

Tags: Tuples, Functions, Scripts

Create a module called:

```text
math_utils.py
```

Add this function:

```python
def add_numbers(a, b):
    return a + b
```

---

## Exercise 2

Tags: print(), Tuples, Imports, Scripts

Create a main script that imports the module.

```python
import math_utils

print(math_utils.add_numbers(5, 3))
```

---

## Exercise 3

Tags: print(), Tuples, Imports

Import the function directly.

```python
from math_utils import add_numbers

print(add_numbers(10, 7))
```

---

# Common Mistakes

## Naming Modules the Same as Built-in Libraries

Avoid naming files like:

```text
pandas.py
math.py
```

This can conflict with Python libraries.

---

## Forgetting the Module File Location

The module must be in the same directory as the script or installed in the environment.

Example structure:

```text
project
│
├── main.py
└── sales_utils.py
```

---

## Circular Imports

Sometimes two modules import each other, causing errors.

Example:

```text
moduleA imports moduleB
moduleB imports moduleA
```

This creates a circular dependency.

---

# Real-World Use

Modules are used in almost every professional Python project.

Example analytics project structure:

```text
project
│
├── main.py
├── data_cleaning.py
├── calculations.py
├── database.py
└── export.py
```

Example usage:

```python
import calculations

total = calculations.calculate_total(10, 5)
```

This structure makes the project easier to maintain and scale.

---

# Lesson Recap

In this lesson you learned:

• what Python modules are  
• how modules organize reusable code  
• how to import modules into scripts  
• how modules improve project structure  

Modules are a key step toward writing **clean, maintainable Python code**.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Project Folder Structure

You will learn:

• how to organize Python projects  
• how to structure folders for real data projects  
• best practices for scalable code organization  

This lesson will show how professional Python projects are structured.
