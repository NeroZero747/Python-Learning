# Module 2 — Programming Foundations

# Lesson 8 — Functions

## Lesson Objective

By the end of this lesson learners will understand:

• what functions are and why they are useful  
• how to define a function in Python  
• how functions accept inputs (parameters)  
• how functions return results  

Functions allow developers to **organize code, avoid repetition, and build reusable logic**.

## Overview

As programs grow, repeating the same logic multiple times becomes inefficient.

For example:

```python
price = 10
quantity = 5
print(price * quantity)

price = 20
quantity = 3
print(price * quantity)
```

The same calculation appears multiple times.

Instead of repeating code, we can define a **function**.

A function is a reusable block of code that performs a specific task.

Example:

```python
def calculate_total(price, quantity):
    total = price * quantity
    print(total)
```

Now the program can reuse the function:

```python
calculate_total(10,5)
calculate_total(20,3)
```

Output:

```text
50
60
```

Functions allow programs to **reuse logic without rewriting code**.

They are commonly used in:

• data pipelines  
• analytics scripts  
• automation workflows  
• application development  

## Key Idea Cards (3 Cards)

### Functions Group Reusable Code

Functions allow developers to group related instructions together.

Example:

```python
def greet():
    print("Hello")
```

The function can be reused multiple times.

### Functions Accept Inputs

Functions often receive values called **parameters**.

Example:

```python
def add_numbers(a,b):
    print(a + b)
```

The function performs the calculation using the inputs.

### Functions Can Return Results

Functions can send results back to the program using `return`.

Example:

```python
def multiply(a,b):
    return a * b
```

The returned value can be stored in a variable.

## Key Concepts

### Function

A function is a **named block of reusable code**.

Structure:

```python
def function_name():
    instructions
```

Example:

```python
def greet():
    print("Hello World")
```

The function defines a reusable action.

### Function Call

A function must be **called** in order to run.

Example:

```python
greet()
```

Output:

```text
Hello World
```

The function executes when it is called.

### Parameters

Parameters are inputs passed to a function.

Example:

```python
def square(number):
    print(number * number)
```

Calling the function:

```python
square(4)
```

Output:

```text
16
```

Parameters allow functions to work with different values.

### Return Value

Functions can return results.

Example:

```python
def add(a,b):
    return a + b
```

Using the result:

```python
result = add(5,3)

print(result)
```

Output:

```text
8
```

The function sends the result back to the program.

## Decision Flow

Functions organize program execution.

Example:

```python
def calculate_total(price,quantity):
    return price * quantity

total = calculate_total(10,5)

print(total)
```

Execution flow:

```text
Define function
      ↓
Call function
      ↓
Execute instructions
      ↓
Return result
      ↓
Continue program
```

Functions break large programs into **manageable pieces**.

## Code Examples

### Example 1 — Simple Function

```python
def greet():
    print("Welcome to Python")

greet()
```

Output:

```text
Welcome to Python
```

The function runs when called.

### Example 2 — Function with Parameters

```python
def multiply(a,b):
    print(a * b)

multiply(4,5)
```

Output:

```text
20
```

The function uses input values.

### Example 3 — Function Returning Values

```python
def calculate_profit(revenue,expenses):
    return revenue - expenses

profit = calculate_profit(100000,60000)

print(profit)
```

Output:

```text
40000
```

Functions can return values to the program.

## SQL / Excel Comparison

Functions exist in SQL and Excel as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| reusable logic | function | stored procedure | custom formula |
| built-in logic | function | SQL function | Excel function |
| calculation | return value | computed column | formula |

Example Excel function:

```text
=SUM(A1:A5)
```

Equivalent Python concept:

```python
sum(numbers)
```

Both perform reusable calculations.

## Practice Exercises

### Exercise 1

Tags: print(), Functions

Create a function that prints a greeting.

Example:

```python
def hello():
    print("Hello Python")

hello()
```

### Exercise 2

Tags: print(), Tuples, Functions

Create a function that adds two numbers.

Example:

```python
def add(a,b):
    print(a+b)

add(5,10)
```

### Exercise 3

Tags: print(), Functions

Create a function that returns a result.

Example:

```python
def square(n):
    return n*n

result = square(6)

print(result)
```

## Common Mistakes

### Forgetting Parentheses When Calling a Function

Incorrect:

```python
greet
```

Correct:

```python
greet()
```

Parentheses execute the function.

### Incorrect Indentation

Incorrect:

```python
def greet():
print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

Python requires indentation inside functions.

### Forgetting Return When Needed

Incorrect:

```python
def add(a,b):
    a + b
```

Correct:

```python
def add(a,b):
    return a + b
```

Without `return`, the result is not sent back.

## Real-World Use

Functions are used heavily in real Python programs.

Examples include:

• data transformation functions  
• API request functions  
• validation functions  
• analytics calculations  

Example data processing function:

```python
def calculate_tax(price):
    return price * 0.08

tax = calculate_tax(100)

print(tax)
```

Functions help keep programs **organized and reusable**.

## Lesson Recap

In this lesson you learned:

• functions group reusable code  
• functions can accept inputs (parameters)  
• functions can return results  
• functions make programs easier to maintain  

Functions are essential for building **clean and scalable programs**.

## Next Lesson

Next we will learn:

**Lesson 9 — Reading & Understanding Errors**

You will learn:

• how Python error messages work  
• how to identify common errors  
• how to debug programs  

Understanding errors is a critical skill for **every programmer**.