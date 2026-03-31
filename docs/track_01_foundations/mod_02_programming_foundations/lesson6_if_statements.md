# Module 2 — Programming Foundations

# Lesson 6 — If Statements

## Lesson Objective

By the end of this lesson learners will understand:

• what conditional logic is  
• how `if` statements control program decisions  
• how to use `elif` and `else`  
• how conditions evaluate to True or False  

Conditional statements allow programs to **make decisions based on data**, which is essential in real-world programming.

## Overview

In many programs, different actions should occur depending on the data.

For example:

```text
If sales exceed the target → show success message
If sales are below the target → show warning
```

Programs handle these decisions using **conditional logic**.

In Python, conditional logic is written using an **if statement**.

Example:

```python
sales = 120

if sales > 100:
    print("Sales target reached")
```

Output:

```text
Sales target reached
```

Here’s what happens:

1. Python evaluates the condition  
2. If the condition is **True**, the code runs  
3. If the condition is **False**, Python skips the code  

This ability to **change behavior based on conditions** makes programs powerful.

## Key Idea Cards (3 Cards)

### If Statements Control Program Decisions

An `if` statement checks whether a condition is true.

Example:

```python
age = 18

if age >= 18:
    print("Adult")
```

If the condition is true, the code executes.

### Conditions Use Comparison Operators

`if` statements use comparison operators to evaluate conditions.

Example:

```python
score = 85

if score > 70:
    print("Pass")
```

The comparison produces a **True or False result**.

### Programs Can Have Multiple Conditions

Programs often need to check several possible conditions.

Example:

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

This allows programs to respond differently depending on the situation.

## Key Concepts

### If Statement

An `if` statement executes code when a condition is true.

Structure:

```python
if condition:
    action
```

Example:

```python
temperature = 30

if temperature > 25:
    print("Warm weather")
```

The code runs only if the condition is true.

### Else Statement

An `else` statement runs when the condition is false.

Example:

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

The `else` block handles the alternative case.

### Elif Statement

`elif` stands for **else if**.

It allows multiple conditions to be checked.

Example:

```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

Only one condition will execute.

## Decision Flow

Conditional statements control program flow.

Example:

```python
sales = 120

if sales > 100:
    print("Target reached")
```

Execution flow:

```text
Evaluate condition
      ↓
Is condition True?
      ↓
Yes → run code
No  → skip code
```

More complex logic may contain multiple branches.

## Code Examples

### Example 1 — Basic If Statement

```python
temperature = 30

if temperature > 25:
    print("Warm day")
```

Output:

```text
Warm day
```

The message appears only if the condition is true.

### Example 2 — If and Else

```python
score = 60

if score >= 70:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Fail
```

The program chooses one branch.

### Example 3 — Multiple Conditions

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```text
Grade B
```

Programs can evaluate multiple possible outcomes.

## SQL / Excel Comparison

Conditional logic exists in SQL and Excel as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| condition | if | CASE | IF |
| comparison | > | > | > |
| branch | elif | WHEN | nested IF |

Example Excel formula:

```text
=IF(A1>100,"High","Low")
```

Equivalent Python:

```python
if sales > 100:
    print("High")
else:
    print("Low")
```

Example SQL:

```sql
CASE
WHEN sales > 100 THEN 'High'
ELSE 'Low'
END
```

All three tools evaluate conditions.

## Practice Exercises

### Exercise 1

Tags: print(), Conditionals

Create a program that checks if a number is greater than 50.

Example:

```python
number = 75

if number > 50:
    print("Large number")
```

Run the program and observe the result.

### Exercise 2

Tags: print(), Conditionals

Create a program that checks if a person is eligible to vote.

Example:

```python
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

### Exercise 3

Tags: print(), Conditionals

Create a program that assigns grades.

Example:

```python
score = 92

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

Run the program with different scores.

## Common Mistakes

### Forgetting the Colon

Incorrect:

```python
if score > 80
```

Correct:

```python
if score > 80:
```

The colon is required.

### Incorrect Indentation

Python uses **indentation to define code blocks**.

Incorrect:

```python
if score > 80:
print("Good")
```

Correct:

```python
if score > 80:
    print("Good")
```

Indentation tells Python which code belongs to the condition.

### Using Assignment Instead of Comparison

Incorrect:

```python
if score = 80
```

Correct:

```python
if score == 80
```

`=` assigns a value.  
`==` compares values.

## Real-World Use

Conditional logic appears everywhere in real programs.

Examples include:

• filtering data  
• validating inputs  
• triggering alerts  
• controlling workflows  

Example business logic:

```python
revenue = 120000
expenses = 90000

profit = revenue - expenses

if profit > 0:
    print("Business profitable")
else:
    print("Business loss")
```

Programs frequently use conditions to **evaluate business metrics**.

## Lesson Recap

In this lesson you learned:

• `if` statements allow programs to make decisions  
• conditions evaluate to True or False  
• `elif` and `else` allow multiple branches  
• conditional logic controls program flow  

Conditional statements allow Python programs to **respond dynamically to data**.

## Next Lesson

Next we will learn:

**Lesson 7 — Loops**

You will learn:

• how programs repeat tasks automatically  
• how `for` loops iterate through data  
• how loops process lists and datasets  

Loops are essential for **processing large amounts of data efficiently**.