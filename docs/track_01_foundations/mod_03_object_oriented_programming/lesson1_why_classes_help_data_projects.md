# Module 6 — Object-Oriented Programming

# Lesson 1 — Why Classes Help Data Projects

---

# Lesson Objective

By the end of this lesson learners will understand:

• what object-oriented programming (OOP) is  
• what a class represents in Python  
• why classes help organize larger programs  
• how classes are useful in analytics and data engineering projects  

Classes are important because they allow developers to **group related data and behavior together into a structured unit**.

This helps turn scripts into **organized, maintainable systems**.

---

# Overview

As Python projects grow, scripts can become increasingly complex.

Example script:

```python
def clean_names(name):
    return name.strip().title()

def calculate_total(price, quantity):
    return price * quantity

def export_data(df):
    df.to_csv("output.csv")
```

This works, but in larger projects we often want to group related logic together.

For example, imagine building a data processing pipeline that performs:

• loading data  
• cleaning data  
• calculating metrics  
• exporting results  

Instead of many separate functions, we can group these operations into a **class**.

Example:

```python
class SalesPipeline:

    def clean_names(self, name):
        return name.strip().title()

    def calculate_total(self, price, quantity):
        return price * quantity
```

A class acts like a **blueprint** for creating structured objects that contain both:

• data  
• behavior (functions)

This approach helps organize complex systems.

Classes are widely used in:

• data engineering pipelines  
• APIs  
• analytics frameworks  
• machine learning systems  

---

# Key Idea Cards (3 Cards)

## Classes Organize Related Logic

Classes group related functions and data together.

Example:

```python
class SalesCalculator:
    def calculate_total(self, price, quantity):
        return price * quantity
```

This keeps related logic in one place.

---

## Classes Create Reusable Objects

A class defines a blueprint for creating objects.

Example:

```python
calculator = SalesCalculator()
```

Now the object can run methods from the class.

---

## Classes Help Scale Large Projects

Large projects often contain many components.

Classes help structure them into logical units.

Example system:

```text
DataPipeline
│
├── load_data()
├── clean_data()
├── calculate_metrics()
└── export_results()
```

This structure makes systems easier to maintain.

---

# Key Concepts

## Class

A **class** is a blueprint used to create objects.

Example:

```python
class Customer:
    pass
```

This defines a class named `Customer`.

---

## Object

An **object** is an instance of a class.

Example:

```python
customer = Customer()
```

Here, `customer` is an object created from the class.

---

## Methods

Methods are functions defined inside a class.

Example:

```python
class Calculator:

    def add(self, a, b):
        return a + b
```

Methods describe the behavior of the class.

---

# Decision Flow

Using classes typically follows this workflow:

```text
Identify related functionality
      ↓
Create a class
      ↓
Define methods inside the class
      ↓
Create an object from the class
      ↓
Use the object to run methods
```

Example:

```python
calculator = Calculator()
calculator.add(5, 3)
```

---

# Code Examples

## Example 1 — Simple Class

```python
class Dog:
    pass
```

This defines a class but does not yet include behavior.

---

## Example 2 — Class with a Method

```python
class Calculator:

    def add(self, a, b):
        return a + b
```

---

## Example 3 — Creating an Object

```python
calculator = Calculator()

result = calculator.add(5, 3)

print(result)
```

Output:

```text
8
```

---

## Example 4 — Data Processing Class

```python
class DataProcessor:

    def clean_name(self, name):
        return name.strip().title()

processor = DataProcessor()

print(processor.clean_name(" alice "))
```

Output:

```text
Alice
```

---

# SQL / Excel Comparison

OOP concepts have parallels in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| blueprint | class | table schema | workbook template |
| instance | object | table record | worksheet copy |
| behavior | method | stored procedure | macro |

Example SQL structure:

```sql
CREATE TABLE customers (
    id INT,
    name VARCHAR(50)
)
```

Python classes provide similar structural organization.

---

# Practice Exercises

## Exercise 1

Tags: Classes, OOP

Create a class named `Person`.

```python
class Person:
    pass
```

---

## Exercise 2

Tags: String Formatting, Tuples, Functions, Classes

Add a method to greet someone.

```python
class Person:

    def greet(self, name):
        return f"Hello {name}"
```

---

## Exercise 3

Tags: print(), OOP

Create an object and call the method.

```python
p = Person()

print(p.greet("Alice"))
```

---

# Common Mistakes

## Forgetting the self Parameter

Incorrect:

```python
def add(a, b):
```

Correct:

```python
def add(self, a, b):
```

Methods inside classes must include `self`.

---

## Using Classes for Very Small Scripts

For simple scripts, classes may not be necessary.

They are most useful in **larger systems**.

---

## Confusing Classes and Objects

Incorrect thinking:

```text
Class = object
```

Correct understanding:

```text
Class = blueprint
Object = instance created from blueprint
```

---

# Real-World Use

Classes are used heavily in professional Python projects.

Examples include:

• web frameworks (Django, FastAPI)  
• machine learning models  
• ETL pipelines  
• database connectors  

Example pipeline class:

```python
class DataPipeline:

    def load_data(self):
        pass

    def clean_data(self):
        pass

    def export_data(self):
        pass
```

This design organizes the entire pipeline inside a structured system.

---

# Lesson Recap

In this lesson you learned:

• what object-oriented programming is  
• what classes represent in Python  
• how classes organize logic  
• why classes help scale larger systems  

Classes are the foundation of **structured Python software development**.

---

# Next Lesson

Next we will learn:

# Lesson 2 — Creating a Class

You will learn:

• how to define attributes inside classes  
• how constructors work (`__init__`)  
• how objects store data  

This lesson will show how classes can **store and manage data** inside Python programs.
