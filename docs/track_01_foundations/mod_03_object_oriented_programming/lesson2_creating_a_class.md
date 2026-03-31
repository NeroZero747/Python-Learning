# Module 6 — Object-Oriented Programming

# Lesson 2 — Creating a Class

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to define a class in Python  
• what a constructor (`__init__`) is  
• how classes store data using attributes  
• how objects are created from classes  

Classes are useful because they allow programs to **store related data and behavior together in one structure**.

This is especially useful in data pipelines and analytics systems where objects represent **datasets, records, or processing steps**.

---

# Overview

In the previous lesson you learned that a **class is a blueprint** for creating objects.

Now we will learn how to **define classes that store information**.

In Python, classes usually include a special method called:

```python
__init__()
```

This method is called a **constructor**.

The constructor runs automatically when a new object is created.

Example:

```python
class Customer:

    def __init__(self, name, city):
        self.name = name
        self.city = city
```

Here the class stores two pieces of information:

• customer name  
• customer city  

Now we can create objects from the class.

Example:

```python
customer1 = Customer("Alice", "Los Angeles")
customer2 = Customer("Bob", "Chicago")
```

Each object stores its own data.

Example:

```python
print(customer1.name)
print(customer2.city)
```

Output:

```text
Alice
Chicago
```

This structure allows Python programs to **represent real-world entities inside code**.

---

# Key Idea Cards (3 Cards)

## Classes Store Data

Classes can store data using **attributes**.

Example:

```python
class Customer:

    def __init__(self, name, city):
        self.name = name
        self.city = city
```

The class now stores information about customers.

---

## Objects Are Instances of Classes

Objects are created from classes.

Example:

```python
customer = Customer("Alice", "Los Angeles")
```

Here the variable `customer` is an **object** created from the `Customer` class.

---

## The Constructor Initializes Objects

The `__init__` method runs when an object is created.

Example:

```python
def __init__(self, name, city):
```

This method sets up the object's attributes.

---

# Key Concepts

## Constructor (`__init__`)

The constructor initializes object data.

Example:

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
```

When an object is created, these values are stored.

---

## Attributes

Attributes are variables stored inside objects.

Example:

```python
product = Product("Laptop", 1200)

print(product.name)
```

Here `name` is an attribute.

---

## Instance

An **instance** is another word for an object created from a class.

Example:

```python
product = Product("Phone", 800)
```

The variable `product` is an instance of the class.

---

# Decision Flow

Creating and using a class usually follows this process:

```text
Define class
      ↓
Create constructor (__init__)
      ↓
Define attributes
      ↓
Create object
      ↓
Use object data
```

Example:

```python
product = Product("Laptop", 1200)
```

---

# Code Examples

## Example 1 — Basic Class with Constructor

```python
class Person:

    def __init__(self, name):
        self.name = name
```

---

## Example 2 — Creating Objects

```python
person1 = Person("Alice")
person2 = Person("Bob")

print(person1.name)
print(person2.name)
```

Output:

```text
Alice
Bob
```

---

## Example 3 — Class with Multiple Attributes

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
```

---

## Example 4 — Accessing Attributes

```python
product = Product("Laptop", 1200)

print(product.name)
print(product.price)
```

Output:

```text
Laptop
1200
```

---

# SQL / Excel Comparison

Object-oriented concepts can be compared to database structures.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| blueprint | class | table schema | workbook template |
| object | instance | record | row |
| attribute | object property | column | cell |

Example SQL table:

```sql
CREATE TABLE customers (
    name VARCHAR(50),
    city VARCHAR(50)
)
```

Each row in the table represents a record.

Similarly, each object created from a class represents a structured record.

---

# Practice Exercises

## Exercise 1

Tags: Tuples, Functions, Classes, OOP

Create a class called `Car`.

```python
class Car:

    def __init__(self, brand):
        self.brand = brand
```

---

## Exercise 2

Tags: OOP, Classes

Create two objects.

```python
car1 = Car("Toyota")
car2 = Car("Honda")
```

Print their attributes.

---

## Exercise 3

Tags: Tuples, Functions, Classes, OOP

Create a class with two attributes.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

Create an object and print the values.

---

# Common Mistakes

## Forgetting self

Incorrect:

```python
def __init__(name, city):
```

Correct:

```python
def __init__(self, name, city):
```

`self` refers to the current object.

---

## Not Using Attributes

Incorrect:

```python
def __init__(self, name):
    name = name
```

Correct:

```python
self.name = name
```

Attributes must use `self`.

---

## Confusing Classes with Functions

Classes create **objects with stored data**, while functions simply execute logic.

---

# Real-World Use

Classes are often used to represent structured data.

Examples include:

• customers  
• products  
• datasets  
• pipeline components  

Example analytics object:

```python
class Dataset:

    def __init__(self, name, rows):
        self.name = name
        self.rows = rows
```

Example usage:

```python
claims = Dataset("Claims Data", 100000)

print(claims.rows)
```

Output:

```text
100000
```

Classes help model structured information in Python systems.

---

# Lesson Recap

In this lesson you learned:

• how to create a class  
• how constructors initialize objects  
• how attributes store object data  
• how objects are created from classes  

This is the foundation for building **structured Python applications**.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Attributes & Methods

You will learn:

• how methods work inside classes  
• how objects perform actions  
• how attributes and methods work together  

This lesson will show how classes combine **data and behavior**.
