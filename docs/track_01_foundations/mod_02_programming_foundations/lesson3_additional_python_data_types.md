# Module 2 — Programming Foundations

# Lesson 3 — Additional Python Data Types

## Lesson Objective

By the end of this lesson learners will understand:

• what tuples are  
• what sets are  
• what the `None` data type represents  
• when these data types are useful in Python programs  

These types are commonly used when working with **structured data, collections of values, and missing data**.

## Overview

In the previous lesson you learned about the most common Python data types:

• strings  
• integers  
• floats  
• booleans  

Python also includes several **additional data types** that help organize and manage data.

Three important types are:

| Data Type | Purpose |
|------|------|
| Tuple | ordered collection that cannot change |
| Set | collection of unique values |
| None | represents absence of a value |

These types are frequently used in real-world data workflows.

For example:

• storing fixed data structures  
• removing duplicate values  
• representing missing data  

Understanding these types will make it easier to work with **datasets and data transformations** later.

## Key Idea Cards (3 Cards)

### Tuples Store Ordered Data That Cannot Change

A tuple is an **ordered collection of values that cannot be modified**.

Example:

```python
coordinates = (34.05, -118.24)
```

Tuples are useful when data **should not change**, such as:

• geographic coordinates  
• database records  
• configuration settings  

Once created, tuple values cannot be altered.

### Sets Store Unique Values

A set is a collection that automatically **removes duplicate values**.

Example:

```python
numbers = {1, 2, 2, 3, 3, 3}
```

Result:

```text
{1, 2, 3}
```

Sets are commonly used for:

• removing duplicates  
• comparing datasets  
• performing membership checks  

### None Represents No Value

`None` represents the **absence of a value**.

Example:

```python
result = None
```

This is different from:

• `0`
• `False`
• empty string `""`

`None` is often used to represent **missing or unknown data**.

## Key Concepts

### Tuple

A tuple is an **immutable ordered collection of values**.

Example:

```python
point = (10, 20)
```

Accessing tuple values:

```python
print(point[0])
```

Output:

```text
10
```

Tuples are similar to lists, but **they cannot be modified**.

Example (invalid):

```python
point[0] = 5
```

This will produce an error.

Tuples are useful when values should remain constant.

### Set

A set is an **unordered collection of unique values**.

Example:

```python
values = {1, 2, 3}
```

If duplicates are added:

```python
values = {1, 2, 2, 3, 3}
```

Result:

```text
{1, 2, 3}
```

Sets automatically remove duplicates.

Sets are often used for:

• data cleaning  
• identifying unique records  
• comparing datasets  

### None

`None` is a special Python value that represents **no value or missing data**.

Example:

```python
value = None
```

Programs often use `None` as a placeholder.

Example:

```python
result = None

if result is None:
    print("No result available")
```

This is common when:

• a value has not been calculated yet  
• data is missing  
• a function returns nothing  

## Decision Flow

Programs often check whether a value exists.

Example:

```python
result = None

if result is None:
    print("Data not available")
```

Execution flow:

```text
Assign result = None
      ↓
Check if result is None
      ↓
Display message
```

This allows programs to handle missing values safely.

## Code Examples

### Example 1 — Tuple

```python
coordinates = (34.05, -118.24)

print(coordinates)
```

Output:

```text
(34.05, -118.24)
```

Tuples store values in a fixed structure.

### Example 2 — Set

```python
numbers = {1, 2, 2, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

Duplicate values are removed automatically.

### Example 3 — Using None

```python
result = None

print(result)
```

Output:

```text
None
```

`None` indicates that a value is not currently available.

## SQL / Excel Comparison

These Python types have similarities with concepts in SQL and Excel.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| tuple | fixed row structure | row | row |
| set | unique values | DISTINCT | Remove duplicates |
| None | missing value | NULL | blank cell |

Example SQL:

```sql
SELECT DISTINCT city
FROM customers;
```

Equivalent Python concept:

```python
cities = {"LA", "NY", "LA"}
```

Result:

```text
{"LA", "NY"}
```

Sets remove duplicates automatically.

## Practice Exercises

### Exercise 1

Tags: print(), Tuples

Create a tuple representing coordinates.

Example:

```python
location = (40.71, -74.00)

print(location)
```

### Exercise 2

Tags: print(), Sets

Create a set that removes duplicates.

Example:

```python
numbers = {1,2,2,3,3,4}

print(numbers)
```

Observe how duplicates are removed.

### Exercise 3

Tags: print(), None, Variables

Create a variable with no value using `None`.

Example:

```python
data = None

print(data)
```

## Common Mistakes

### Trying to Modify a Tuple

Incorrect:

```python
coordinates = (10,20)
coordinates[0] = 5
```

Tuples cannot be modified.

### Expecting Sets to Maintain Order

Sets do not guarantee order.

Example:

```python
numbers = {5,1,3}
```

Output order may vary.

### Confusing None With Zero or Empty Values

These values are different:

```python
0
False
""
None
```

`None` specifically means **no value exists**.

## Real-World Use

These data types appear frequently in data processing workflows.

Examples:

| Use Case | Data Type |
|------|------|
| coordinates | tuple |
| unique IDs | set |
| missing API response | None |

Example dataset cleaning:

```python
ids = {101, 102, 102, 103}

print(ids)
```

Result:

```text
{101,102,103}
```

Sets quickly remove duplicates.

## Lesson Recap

In this lesson you learned:

• tuples store fixed ordered data  
• sets store unique values  
• `None` represents missing data  
• these data types are useful for structured and cleaned data  

These types are frequently used in data processing workflows.

## Next Lesson

Next we will learn:

**Lesson 4 — Lists & Dictionaries**

You will learn:

• how Python stores collections of values  
• how lists store ordered data  
• how dictionaries store key-value pairs  

These are **two of the most important data structures in Python**.