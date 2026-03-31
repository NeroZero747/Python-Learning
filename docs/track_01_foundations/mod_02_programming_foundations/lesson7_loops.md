# Module 2 — Programming Foundations

# Lesson 7 — Loops

## Lesson Objective

By the end of this lesson learners will understand:

• what loops are and why they are used  
• how `for` loops repeat actions automatically  
• how loops process lists of data  
• how loops help automate repetitive tasks  

Loops allow programs to **repeat tasks automatically**, which is essential when working with datasets.

## Overview

Many programming tasks require repeating the same action multiple times.

For example:

```text
Calculate revenue for each product
Print each customer name
Process every row in a dataset
```

Without loops, you would need to write repetitive code like this:

```python
print(customer1)
print(customer2)
print(customer3)
print(customer4)
```

This approach does not scale.

Instead, Python provides **loops**, which allow programs to repeat instructions automatically.

Example:

```python
customers = ["Alice", "Bob", "Maria"]

for customer in customers:
    print(customer)
```

Output:

```text
Alice
Bob
Maria
```

The loop processes each item automatically.

Loops are essential for working with:

• datasets  
• lists of values  
• files  
• API results  

Without loops, most data processing tasks would be impossible.

## Key Idea Cards (3 Cards)

### Loops Repeat Instructions

Loops allow programs to repeat instructions automatically.

Example:

```python
for i in range(3):
    print("Processing")
```

Output:

```text
Processing
Processing
Processing
```

The loop repeats the instruction multiple times.

### For Loops Process Collections of Data

A `for` loop processes each item in a collection.

Example:

```python
sales = [100, 200, 150]

for value in sales:
    print(value)
```

The loop processes each value in the list.

### Loops Automate Data Processing

Loops allow programs to process datasets automatically.

Example:

```python
sales = [100, 200, 150]

total = 0

for value in sales:
    total = total + value

print(total)
```

Output:

```text
450
```

Loops make it possible to analyze large datasets efficiently.

## Key Concepts

### Loop

A loop repeats a block of code multiple times.

Example:

```python
for i in range(3):
    print("Hello")
```

The loop executes the code **three times**.

Loops allow programs to handle repetitive tasks automatically.

### For Loop

A `for` loop iterates through a collection of values.

Structure:

```python
for item in collection:
    action
```

Example:

```python
numbers = [1,2,3]

for number in numbers:
    print(number)
```

Each item is processed one at a time.

### Range Function

The `range()` function generates a sequence of numbers.

Example:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

`range()` is often used when repeating actions a fixed number of times.

## Decision Flow

Loops repeat code until all values are processed.

Example:

```python
sales = [100,200,150]

for value in sales:
    print(value)
```

Execution flow:

```text
Start loop
      ↓
Retrieve first value
      ↓
Run code
      ↓
Retrieve next value
      ↓
Repeat until finished
```

The loop stops once all values have been processed.

## Code Examples

### Example 1 — Simple Loop

```python
for i in range(3):
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
```

The loop repeats the instruction three times.

### Example 2 — Loop Through a List

```python
names = ["Alice","Bob","Maria"]

for name in names:
    print(name)
```

Output:

```text
Alice
Bob
Maria
```

The loop processes each value in the list.

### Example 3 — Summing Values

```python
numbers = [10,20,30]

total = 0

for n in numbers:
    total = total + n

print(total)
```

Output:

```text
60
```

The loop processes the dataset and accumulates results.

## SQL / Excel Comparison

Loops perform similar tasks to operations in SQL and Excel.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| iterate rows | for loop | row processing | drag formula |
| dataset operation | loop calculation | GROUP BY | pivot table |
| repeated action | loop | stored procedure | macro |

Example Excel formula copied down a column:

```text
=A1 * 2
```

Equivalent Python concept:

```python
values = [1,2,3]

for v in values:
    print(v * 2)
```

Loops apply operations across datasets.

## Practice Exercises

### Exercise 1

Tags: print(), range(), Tuples, Loops

Write a loop that prints numbers from 1 to 5.

Example:

```python
for i in range(1,6):
    print(i)
```

### Exercise 2

Tags: print(), Lists, Loops, Iteration

Loop through a list of cities.

Example:

```python
cities = ["NY","LA","Chicago"]

for city in cities:
    print(city)
```

### Exercise 3

Tags: print(), Lists, Loops, Iteration

Calculate the total sales.

Example:

```python
sales = [100,150,200]

total = 0

for s in sales:
    total += s

print(total)
```

## Common Mistakes

### Incorrect Indentation

Incorrect:

```python
for i in range(3):
print(i)
```

Correct:

```python
for i in range(3):
    print(i)
```

Python requires proper indentation.

### Forgetting the Colon

Incorrect:

```python
for i in range(5)
```

Correct:

```python
for i in range(5):
```

The colon is required.

### Modifying Lists Incorrectly

Beginners sometimes modify a list while looping through it.

This can produce unexpected results.

## Real-World Use

Loops are used everywhere in real programs.

Examples include:

• processing rows in a dataset  
• applying calculations to columns  
• validating records  
• generating reports  

Example data processing loop:

```python
sales = [120, 150, 200]

for s in sales:
    revenue = s * 1.1
    print(revenue)
```

Loops allow programs to process **entire datasets efficiently**.

## Lesson Recap

In this lesson you learned:

• loops repeat instructions automatically  
• `for` loops iterate through collections  
• loops process datasets efficiently  
• loops allow automation of repetitive tasks  

Loops are essential for analyzing and transforming data.

## Next Lesson

Next we will learn:

**Lesson 8 — Functions**

You will learn:

• how functions organize code  
• how functions make programs reusable  
• how functions simplify complex programs  

Functions are essential for writing **clean and maintainable Python code**.