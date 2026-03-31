# Module 2 — Programming Foundations

# Lesson 5 — Operators

## Lesson Objective

By the end of this lesson learners will understand:

• what operators are in Python  
• how arithmetic operators perform calculations  
• how comparison operators evaluate conditions  
• how logical operators combine conditions  

Operators allow Python programs to **perform calculations and evaluate logic**, which are essential for data processing and decision-making.

## Overview

In programming, **operators are symbols that perform operations on values**.

For example, Python can perform mathematical operations such as addition and multiplication.

Example:

```python
result = 10 + 5
```

Here:

• `10` and `5` are values  
• `+` is the operator  

The operator tells Python **what action to perform**.

Python supports several types of operators:

| Operator Type | Purpose |
|------|------|
| Arithmetic | mathematical calculations |
| Comparison | compare values |
| Logical | combine conditions |

Operators are used constantly in programs for tasks such as:

• performing calculations  
• comparing values  
• controlling program decisions  

Understanding operators is essential before learning **conditional logic and loops**.

## Key Idea Cards (3 Cards)

### Operators Perform Actions on Values

Operators tell Python **how to combine or evaluate values**.

Example:

```python
total = 20 + 10
```

The `+` operator adds the two numbers.

Operators allow programs to perform calculations and comparisons.

### Comparison Operators Return True or False

Comparison operators compare values.

Example:

```python
sales = 120

print(sales > 100)
```

Output:

```text
True
```

The result is a **boolean value**.

### Logical Operators Combine Conditions

Logical operators allow programs to evaluate **multiple conditions**.

Example:

```python
sales = 120
customers = 10

print(sales > 100 and customers > 5)
```

Output:

```text
True
```

Logical operators help programs make decisions.

## Key Concepts

### Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning | Example |
|------|------|------|
| + | addition | 10 + 5 |
| - | subtraction | 10 - 5 |
| * | multiplication | 10 * 5 |
| / | division | 10 / 5 |
| % | remainder | 10 % 3 |

Example program:

```python
price = 20
quantity = 3

total = price * quantity

print(total)
```

Output:

```text
60
```

Arithmetic operators are commonly used in **financial and data calculations**.

### Comparison Operators

Comparison operators compare two values.

| Operator | Meaning |
|------|------|
| == | equal to |
| != | not equal |
| > | greater than |
| < | less than |
| >= | greater than or equal |
| <= | less than or equal |

Example:

```python
score = 85

print(score > 70)
```

Output:

```text
True
```

Comparison operators return **boolean values**.

### Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|------|------|
| and | both conditions must be true |
| or | one condition must be true |
| not | reverses a condition |

Example:

```python
age = 30
income = 60000

print(age > 25 and income > 50000)
```

Output:

```text
True
```

Logical operators allow complex decision logic.

## Decision Flow

Operators are frequently used in decision-making.

Example:

```python
sales = 120

print(sales > 100)
```

Execution flow:

```text
Store sales value
      ↓
Compare sales to 100
      ↓
Return True or False
```

Programs use these results to control behavior.

Later lessons will use operators inside **if statements**.

## Code Examples

### Example 1 — Arithmetic Calculation

```python
a = 10
b = 5

print(a + b)
print(a * b)
```

Output:

```text
15
50
```

Arithmetic operators perform mathematical calculations.

### Example 2 — Comparison Operators

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

The expression evaluates whether the value meets the condition.

### Example 3 — Logical Operators

```python
sales = 200
customers = 15

print(sales > 100 and customers > 10)
```

Output:

```text
True
```

Both conditions must be true.

## SQL / Excel Comparison

Operators behave similarly in SQL and Excel.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| addition | + | + | + |
| multiplication | * | * | * |
| comparison | > | > | > |
| logical | and | AND | AND |

Example Excel formula:

```text
=A1 > 100
```

Equivalent Python:

```python
sales > 100
```

Example SQL condition:

```sql
WHERE sales > 100
```

Operators work similarly across these tools.

## Practice Exercises

### Exercise 1

Tags: print(), Arithmetic

Perform arithmetic operations.

```python
a = 15
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Observe the results.

### Exercise 2

Tags: print(), Booleans

Use comparison operators.

```python
score = 75

print(score > 50)
print(score < 50)
```

Observe the boolean results.

### Exercise 3

Tags: print(), Python Basics

Use logical operators.

```python
age = 30
salary = 60000

print(age > 25 and salary > 50000)
```

Observe the result.

## Common Mistakes

### Using = Instead of ==

Incorrect:

```python
if score = 100
```

Correct:

```python
if score == 100
```

`=` assigns a value.  
`==` compares values.

### Confusing and / or Logic

Example:

```python
age > 18 and income > 50000
```

Both conditions must be true.

Example:

```python
age > 18 or income > 50000
```

Only one condition must be true.

### Forgetting Operator Precedence

Example:

```python
10 + 5 * 2
```

Multiplication happens first.

Result:

```text
20
```

Use parentheses if necessary.

## Real-World Use

Operators appear constantly in real programs.

Examples include:

• financial calculations  
• filtering data  
• evaluating conditions  
• controlling program flow  

Example data check:

```python
revenue = 100000
expenses = 60000

profit = revenue - expenses

print(profit > 0)
```

Output:

```text
True
```

Operators help determine business outcomes.

## Lesson Recap

In this lesson you learned:

• operators perform actions on values  
• arithmetic operators perform calculations  
• comparison operators evaluate conditions  
• logical operators combine multiple conditions  

Operators are essential because they allow programs to **calculate results and evaluate logic**.

## Next Lesson

Next we will learn:

**Lesson 6 — If Statements**

You will learn:

• how programs make decisions  
• how conditions control program behavior  
• how logic branches in Python  

This is where Python programs begin to **respond dynamically to data**.