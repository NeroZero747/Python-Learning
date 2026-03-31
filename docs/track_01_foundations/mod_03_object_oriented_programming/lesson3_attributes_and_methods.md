# Module 6 — Object-Oriented Programming

# Lesson 3 — Attributes & Methods

---

# Lesson Objective

By the end of this lesson learners will understand:

• what attributes are in a class  
• what methods are in a class  
• how attributes store data for objects  
• how methods perform actions using that data  

Attributes and methods are important because they allow classes to **store information and perform operations on that information**.

This combination is what makes object-oriented programming powerful.

---

# Overview

In the previous lesson, you learned how to create a class and initialize it using the constructor `__init__`.

Example class:

```python
class Customer:

    def __init__(self, name, city):
        self.name = name
        self.city = city
```

Here the class stores attributes:

• name  
• city  

Attributes represent **data stored inside an object**.

Now we can add **methods**, which are functions that operate on that data.

Example:

```python
class Customer:

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def greet(self):
        return f"Hello {self.name}"
```

Now objects created from this class can run methods.

Example:

```python
customer = Customer("Alice", "Los Angeles")

print(customer.greet())
```

Output:

```text
Hello Alice
```

Attributes store information, while methods allow objects to **perform actions**.

---

# Key Idea Cards (3 Cards)

## Attributes Store Object Data

Attributes are variables that belong to an object.

Example:

```python
self.name
self.city
```

Each object stores its own values.

Example:

```python
customer1 = Customer("Alice", "LA")
customer2 = Customer("Bob", "Chicago")
```

Each object contains different data.

---

## Methods Define Object Behavior

Methods are functions inside a class.

Example:

```python
def greet(self):
    return f"Hello {self.name}"
```

Methods define actions the object can perform.

---

## Attributes and Methods Work Together

Methods often use attributes to perform logic.

Example:

```python
def describe(self):
    return f"{self.name} lives in {self.city}"
```

The method uses stored object data.

---

# Key Concepts

## Attribute

An attribute is a variable stored inside an object.

Example:

```python
self.price
self.quantity
```

These values belong to a specific object.

---

## Method

A method is a function defined inside a class.

Example:

```python
def calculate_total(self):
```

Methods allow objects to perform operations.

---

## self

The keyword `self` refers to the **current object**.

Example:

```python
self.name
```

This tells Python to access the object's attribute.

---

# Decision Flow

Creating and using attributes and methods usually follows this process:

```text
Define class
      ↓
Create attributes in constructor
      ↓
Create methods
      ↓
Create object
      ↓
Call methods
```

Example:

```python
customer = Customer("Alice", "LA")

customer.greet()
```

---

# Code Examples

## Example 1 — Class with Attributes

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
```

---

## Example 2 — Adding a Method

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"{self.name} costs {self.price}"
```

---

## Example 3 — Using Attributes and Methods

```python
product = Product("Laptop", 1200)

print(product.display())
```

Output:

```text
Laptop costs 1200
```

---

## Example 4 — Method with Calculations

```python
class Sale:

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity
```

Usage:

```python
sale = Sale(10, 5)

print(sale.total())
```

Output:

```text
50
```

---

# SQL / Excel Comparison

Attributes and methods can be compared to concepts in databases and spreadsheets.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| stored data | attributes | table columns | worksheet cells |
| behavior | methods | stored procedures | macros |
| object instance | record | row | row |

Example SQL table:

```sql
CREATE TABLE products (
    name VARCHAR(50),
    price INT
)
```

Each row represents a record with attributes.

Python objects behave similarly.

---

# Practice Exercises

## Exercise 1

Tags: Tuples, Functions, Classes, OOP

Create a class called `Student`.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## Exercise 2

Tags: String Formatting, Functions, OOP

Add a method that prints a greeting.

```python
def greet(self):
    return f"Hello {self.name}"
```

---

## Exercise 3

Tags: print(), OOP

Create an object and call the method.

```python
student = Student("Alice")

print(student.greet())
```

---

# Common Mistakes

## Forgetting self in Methods

Incorrect:

```python
def greet():
```

Correct:

```python
def greet(self):
```

Methods must include `self`.

---

## Accessing Attributes Incorrectly

Incorrect:

```python
return name
```

Correct:

```python
return self.name
```

Attributes must use `self`.

---

## Creating Methods Outside the Class

Methods must be defined inside the class indentation.

Incorrect:

```python
class Customer:
    pass

def greet(self):
```

Correct:

```python
class Customer:

    def greet(self):
        pass
```

---

# Real-World Use

Attributes and methods are used in many professional systems.

Examples include:

• machine learning models  
• data pipeline components  
• API request handlers  
• database connectors  

Example pipeline class:

```python
class DataPipeline:

    def __init__(self, dataset):
        self.dataset = dataset

    def load(self):
        print("Loading dataset")

    def clean(self):
        print("Cleaning dataset")
```

Usage:

```python
pipeline = DataPipeline("claims")

pipeline.load()
pipeline.clean()
```

Classes organize complex systems into logical components.

---

# Lesson Recap

In this lesson you learned:

• what attributes are  
• what methods are  
• how attributes store object data  
• how methods define object behavior  

Together, attributes and methods form the foundation of **object-oriented programming**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Refactoring a Script into a Class

You will learn:

• how to convert a traditional script into a class  
• how classes improve code organization  
• how object-oriented design helps large projects  

This lesson will demonstrate how to transform a simple script into a **structured Python system**.
