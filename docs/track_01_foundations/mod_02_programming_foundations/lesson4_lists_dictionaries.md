# Module 2 — Programming Foundations

# Lesson 4 — Lists & Dictionaries

## Lesson Objective

By the end of this lesson learners will understand:

• what lists are and how they store ordered collections of data  
• how dictionaries store data using key-value pairs  
• how to access values from lists and dictionaries  
• how these structures relate to SQL tables and Excel data  

Lists and dictionaries are two of the **most commonly used data structures in Python**, especially when working with datasets.

## Overview

In real programs, we rarely work with just a single value. Instead, programs often need to store **collections of data**.

Examples include:

```text
Sales numbers
Customer IDs
Product names
API responses
Rows from a dataset
```

Python provides several ways to store multiple values.

Two of the most important structures are:

| Structure | Purpose |
|------|------|
| List | ordered collection of values |
| Dictionary | key-value data structure |

Lists are useful when you have **multiple values in a sequence**.

Dictionaries are useful when you want to **associate keys with values**, similar to a lookup table.

These structures are fundamental to working with:

• datasets  
• APIs  
• JSON data  
• analytics pipelines  

## Key Idea Cards (3 Cards)

### Lists Store Ordered Collections

A list is an **ordered collection of values**.

Example:

```python
sales = [120, 150, 200]
```

Lists allow programs to store **multiple values in one variable**.

Values in lists maintain their order.

### Dictionaries Store Key-Value Pairs

A dictionary stores data using **keys and values**.

Example:

```python
customer = {
    "name": "Alice",
    "age": 30
}
```

Each key maps to a value.

Dictionaries are similar to **records in a database row**.

### Lists and Dictionaries Are Core Data Structures

Most Python programs working with data rely heavily on lists and dictionaries.

Examples include:

• rows of data  
• API responses  
• JSON files  
• grouped values  

Understanding these structures is essential for real-world programming.

## Key Concepts

### List

A list stores an **ordered collection of values**.

Example:

```python
numbers = [10, 20, 30]
```

Lists are surrounded by **square brackets**.

You can access values using an **index**.

Example:

```python
print(numbers[0])
```

Output:

```text
10
```

Indexing starts at **0**, not 1.

Example:

| Index | Value |
|------|------|
| 0 | 10 |
| 1 | 20 |
| 2 | 30 |

Lists can store different data types.

Example:

```python
data = [10, "Python", True]
```

### Dictionary

A dictionary stores values using **key-value pairs**.

Example:

```python
person = {
    "name": "John",
    "age": 28,
    "city": "Los Angeles"
}
```

Access values using the key.

Example:

```python
print(person["name"])
```

Output:

```text
John
```

Dictionaries are useful for representing **structured data records**.

### Key-Value Pair

A key-value pair is a way of associating a label with a value.

Example:

```python
"name": "Alice"
```

Here:

• `"name"` is the key  
• `"Alice"` is the value  

Dictionaries allow quick lookup using keys.

## Decision Flow

Programs often retrieve data from collections.

Example list program:

```python
sales = [100, 200, 150]

print(sales[1])
```

Execution flow:

```text
Store list
      ↓
Retrieve value at index 1
      ↓
Display result
```

Example dictionary program:

```python
user = {"name": "Maria"}

print(user["name"])
```

Execution flow:

```text
Store dictionary
      ↓
Lookup key "name"
      ↓
Display value
```

## Code Examples

### Example 1 — Creating a List

```python
sales = [100, 150, 200]

print(sales)
```

Output:

```text
[100, 150, 200]
```

### Example 2 — Accessing List Values

```python
sales = [100, 150, 200]

print(sales[0])
print(sales[2])
```

Output:

```text
100
200
```

Lists allow you to access values by position.

### Example 3 — Creating a Dictionary

```python
product = {
    "name": "Laptop",
    "price": 1200
}

print(product)
```

Output:

```text
{'name': 'Laptop', 'price': 1200}
```

### Example 4 — Accessing Dictionary Values

```python
product = {
    "name": "Laptop",
    "price": 1200
}

print(product["price"])
```

Output:

```text
1200
```

The key retrieves the value.

## SQL / Excel Comparison

Lists and dictionaries have similarities to structures in SQL and Excel.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| collection | list | table column | column |
| record | dictionary | row | row |
| lookup | dictionary key | WHERE clause | VLOOKUP |

Example Excel lookup:

```text
=VLOOKUP(A2, Table, 2)
```

Equivalent dictionary concept:

```python
prices = {"apple": 1.50}

print(prices["apple"])
```

Dictionaries behave like **lookup tables**.

## Practice Exercises

### Exercise 1

Tags: print(), Lists

Create a list of three numbers.

Example:

```python
numbers = [5, 10, 15]

print(numbers)
```

### Exercise 2

Tags: print(), Lists, Streamlit

Access the second item in a list.

Example:

```python
numbers = [5, 10, 15]

print(numbers[1])
```

### Exercise 3

Tags: print(), Lists, Dictionaries

Create a dictionary representing a product.

Example:

```python
product = {
    "name": "Phone",
    "price": 800
}

print(product["name"])
```

## Common Mistakes

### Using Parentheses Instead of Brackets

Incorrect list:

```python
numbers = (1,2,3)
```

This creates a **tuple**, not a list.

Correct:

```python
numbers = [1,2,3]
```

### Accessing a Dictionary Key That Doesn't Exist

Incorrect:

```python
user["email"]
```

If the key does not exist, Python raises an error.

### Forgetting That List Indexing Starts at 0

Example list:

```python
values = [10,20,30]
```

Indexes are:

```text
0 → 10
1 → 20
2 → 30
```

This can confuse beginners.

## Real-World Use

Lists and dictionaries appear constantly in data workflows.

Examples:

| Use Case | Structure |
|------|------|
| rows of data | dictionary |
| dataset column | list |
| API response | dictionary |
| JSON data | dictionary |

Example dataset record:

```python
customer = {
    "id": 101,
    "name": "Alice",
    "city": "Chicago"
}
```

Example dataset column:

```python
sales = [100, 200, 150]
```

These structures form the **foundation of data processing in Python**.

## Lesson Recap

In this lesson you learned:

• lists store ordered collections of values  
• dictionaries store key-value pairs  
• lists use indexes to access data  
• dictionaries use keys to retrieve values  

Lists and dictionaries are **core data structures used throughout Python programming**.

## Next Lesson

Next we will learn:

**Lesson 5 — Operators**

You will learn:

• arithmetic operators  
• comparison operators  
• logical operators  

Operators are essential because they allow Python programs to **perform calculations and evaluate conditions**.