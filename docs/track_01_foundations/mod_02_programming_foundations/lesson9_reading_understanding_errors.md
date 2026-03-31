# Module 2 — Programming Foundations

# Lesson 9 — Reading & Understanding Errors

## Lesson Objective

By the end of this lesson learners will understand:

• how Python displays error messages  
• how to identify the location of an error  
• common types of Python errors  
• basic strategies for debugging code  

Understanding errors is an essential programming skill because **every developer encounters errors while writing code**.

## Overview

When Python encounters a problem in a program, it displays an **error message**.

These messages are designed to help developers understand:

• what went wrong  
• where the error occurred  
• why Python could not execute the code  

Example program with an error:

```python
print("Hello
```

Output:

```text
SyntaxError: unterminated string literal
```

The error message tells us that the string was not closed properly.

Python error messages may look intimidating at first, but they contain useful information that helps identify the problem.

Most Python errors include:

```text
Error type
Location of the error
Description of the problem
```

Learning to interpret these messages is a key step toward becoming comfortable with programming.

## Key Idea Cards (3 Cards)

### Errors Are Normal in Programming

Every programmer encounters errors.

Errors are part of the development process and help identify problems in the code.

The goal is not to avoid errors completely, but to **learn how to understand and fix them quickly**.

### Python Error Messages Provide Clues

Python error messages include useful details such as:

• the line number where the error occurred  
• the type of error  
• a description of the problem  

Example error message:

```text
NameError: name 'value' is not defined
```

This tells us the variable `value` was used before being defined.

### Debugging Is the Process of Fixing Errors

Debugging is the process of identifying and correcting problems in code.

Developers typically debug by:

• reading error messages  
• checking the line indicated by Python  
• reviewing the surrounding code  

Debugging is a skill that improves with practice.

## Key Concepts

### Syntax Error

A syntax error occurs when Python code **does not follow the correct structure**.

Example:

```python
print("Hello"
```

Error message:

```text
SyntaxError: '(' was never closed
```

The parentheses were not closed.

Syntax errors prevent the program from running.

### Name Error

A name error occurs when a variable is used before it is defined.

Example:

```python
print(total)
```

Error:

```text
NameError: name 'total' is not defined
```

Python cannot find the variable.

### Type Error

A type error occurs when an operation is performed on incompatible data types.

Example:

```python
print("Age: " + 25)
```

Error:

```text
TypeError: can only concatenate str (not "int") to str
```

Python cannot combine text and numbers directly.

Correct version:

```python
print("Age:", 25)
```

## Decision Flow

When Python encounters an error, the program stops execution.

Example program:

```python
x = 10
y = "5"

print(x + y)
```

Execution flow:

```text
Run program
      ↓
Evaluate expression
      ↓
Detect incompatible types
      ↓
Display error message
      ↓
Program stops
```

The developer must correct the code before running it again.

## Code Examples

### Example 1 — Syntax Error

Incorrect code:

```python
if x > 5
    print("High")
```

Error:

```text
SyntaxError: invalid syntax
```

Correct code:

```python
if x > 5:
    print("High")
```

The colon was missing.

### Example 2 — Name Error

Incorrect code:

```python
print(price)
```

Error:

```text
NameError: name 'price' is not defined
```

Correct code:

```python
price = 10
print(price)
```

The variable must be defined first.

### Example 3 — Type Error

Incorrect code:

```python
print("Total: " + 100)
```

Error:

```text
TypeError
```

Correct code:

```python
print("Total:", 100)
```

Python cannot combine incompatible data types.

## SQL / Excel Comparison

Errors occur in SQL and Excel as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| syntax error | invalid syntax | query error | formula error |
| missing value | NameError | column not found | #NAME? |
| invalid operation | TypeError | data type mismatch | #VALUE! |

Example Excel error:

```text
#VALUE!
```

Example SQL error:

```sql
column not found
```

All programming tools produce errors when instructions are incorrect.

## Practice Exercises

### Exercise 1

Tags: print(), Python Basics

Create a program with a syntax error.

Example:

```python
print("Hello"
```

Run the program and read the error message.

### Exercise 2

Tags: print(), Variables

Create a program with a name error.

Example:

```python
print(total)
```

Then fix the error by defining the variable.

### Exercise 3

Tags: print(), Arithmetic

Create a type error.

Example:

```python
print("Score: " + 100)
```

Correct the program so it runs successfully.

## Common Mistakes

### Ignoring the Line Number

Python tells you exactly where the error occurs.

Example error:

```text
File "script.py", line 5
```

Always check that line first.

### Fixing the Wrong Line

Sometimes the actual mistake occurs **above the line shown in the error**.

Example:

```python
print("Hello"
print("World")
```

The missing parenthesis affects the next line.

### Guessing Instead of Reading the Error

Beginners sometimes try random fixes.

Instead, carefully read the message.

Error messages usually explain the problem.

## Real-World Use

Debugging is part of everyday programming work.

Developers often debug code when:

• scripts fail to run  
• data pipelines break  
• API responses change  
• calculations produce incorrect results  

Example debugging process:

```text
Run program
      ↓
Read error message
      ↓
Locate error line
      ↓
Fix code
      ↓
Run program again
```

Experienced developers spend significant time debugging.

## Lesson Recap

In this lesson you learned:

• Python displays error messages when code fails  
• error messages include the type and location of the problem  
• common errors include syntax, name, and type errors  
• debugging is the process of identifying and fixing problems  

Learning to read error messages is one of the most important skills in programming.

## Next Lesson

Next we will begin **Module 3 — Data Analysis with Pandas**.

You will learn:

• how Pandas works  
• what DataFrames are  
• how Python analyzes datasets  

This module will introduce the **core tools used for data analysis in Python**.