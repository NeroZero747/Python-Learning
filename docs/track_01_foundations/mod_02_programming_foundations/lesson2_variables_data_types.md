# Module 2 — Programming Foundations

# Lesson 2 — Variables & Data Types

## Lesson Objective

By the end of this lesson learners will understand:

• what a variable is  
• how Python stores information in variables  
• the most common Python data types  
• how to check the data type of a value  

These concepts are fundamental because **almost every Python program stores and manipulates data**.

## Overview

In programming, information must be stored so that it can be used later in a program.

Python stores information using **variables**.

A variable is simply a **name that refers to a value stored in memory**.

You can think of a variable as a **labeled container that holds data**.

Example:

```python
name = "Johnny"
```

In this example:

• `name` is the variable  
• `"Johnny"` is the value stored inside it  

Once a value is stored in a variable, the program can **reuse that value throughout the program**.

For example:

```python
name = "Johnny"

print(name)
```

Output:

```text
Johnny
```

Python programs constantly store values such as:

• numbers  
• text  
• lists of values  
• true/false conditions  

Each value belongs to a **data type**.

Understanding data types is important because Python treats different types of data in different ways.

The most common data types you will see are:

| Data Type | Example | Description |
|------|------|------|
| String | `"Hello"` | Text |
| Integer | `10` | Whole numbers |
| Float | `19.99` | Decimal numbers |
| Boolean | `True` | True/False values |

Python automatically determines the correct data type for most values.

## Key Idea Cards (3 Cards)

### Variables Store Information

Variables allow Python programs to store information so it can be reused later.

Example:

```python
age = 30
```

The program can now use the value `30` whenever the variable `age` is referenced.

### Data Types Describe Values

Every value in Python has a **data type**.

Examples:

```text
"Python"   → string  
10         → integer  
10.5       → float  
True       → boolean  
```

The data type tells Python **how the value should behave**.

For example:

Numbers can be added.

Text values can be combined.

### Python Automatically Detects Data Types

Unlike some programming languages, Python does not require you to declare types manually.

Example:

```python
name = "Python"
count = 5
price = 19.99
```

Python automatically determines the type of each value.

This feature makes Python easier to learn and write.

## Key Concepts

### Variable

A variable is a **named container that stores a value**.

Example:

```python
city = "Los Angeles"
```

The variable `city` now stores the value `"Los Angeles"`.

Variables allow programs to reuse information without repeating values.

Example:

```python
price = 20
quantity = 3

total = price * quantity
```

The variables store values used in the calculation.

### String

A string is **text surrounded by quotation marks**.

Example:

```python
name = "Python"
```

Strings are commonly used for:

• names  
• labels  
• messages  
• text data  

Example program:

```python
message = "Hello World"

print(message)
```

### Integer

An integer is a **whole number without a decimal**.

Example:

```python
users = 100
```

Integers are commonly used for:

• counts  
• IDs  
• quantities  
• indexes  

Example:

```python
orders = 25

print(orders)
```

### Float

A float is a **decimal number**.

Example:

```python
price = 19.99
```

Floats are used for:

• prices  
• percentages  
• measurements  
• averages  

Example:

```python
average_score = 92.5
```

### Boolean

A boolean represents **True or False**.

Example:

```python
is_active = True
```

Booleans are commonly used in program logic.

Example:

```python
is_logged_in = True
```

Later lessons will show how booleans control program behavior.

## Decision Flow

Variables store values that programs can use in calculations or decisions.

Example program:

```python
price = 20
quantity = 3

total = price * quantity

print(total)
```

Execution flow:

```text
Store price
      ↓
Store quantity
      ↓
Calculate total
      ↓
Display result
```

Variables allow programs to store intermediate results.

## Code Examples

### Example 1 — Creating Variables

```python
name = "Python"
year_created = 1991
is_popular = True

print(name)
print(year_created)
print(is_popular)
```

Output:

```text
Python
1991
True
```

This program creates three variables and prints them.

### Example 2 — Different Data Types

Python supports many types, but these four are used frequently.

```python
language = "Python"
users = 1000000
rating = 4.8
is_open_source = True

print(language)
print(users)
print(rating)
print(is_open_source)
```

This example shows:

• a string  
• an integer  
• a float  
• a boolean  

### Example 3 — Checking a Data Type

Python provides a function called `type()` to check a variable’s data type.

```python
name = "Python"
count = 5
price = 19.99
is_ready = True

print(type(name))
print(type(count))
print(type(price))
print(type(is_ready))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

This tells you what type of value each variable contains.

## SQL / Excel Comparison

If you already work with SQL or Excel, variables and data types will feel familiar.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| variable | variable | column value | cell |
| text | string | VARCHAR | text |
| number | integer/float | numeric | number |
| boolean | True/False | boolean | TRUE/FALSE |

Example Excel formula:

```text
=A1 * B1
```

Equivalent Python:

```python
total = price * quantity
```

Both perform the same calculation.

## Practice Exercises

### Exercise 1

Tags: print(), Loops, Variables

Create variables for:

• your name  
• your age  
• your favorite number  

Example:

```python
name = "Alex"
age = 28
favorite_number = 7

print(name)
print(age)
print(favorite_number)
```

### Exercise 2

Tags: print(), Variables

Create variables representing a product sale.

Example:

```python
price = 15
quantity = 4

total = price * quantity

print(total)
```

Run the program and observe the result.

### Exercise 3

Tags: print(), type(), Booleans, Variables

Check the type of several values.

Example:

```python
print(type("Hello"))
print(type(10))
print(type(3.14))
print(type(True))
```

Observe the types displayed.

## Common Mistakes

### Forgetting Quotes Around Strings

Incorrect:

```python
name = Python
```

Correct:

```python
name = "Python"
```

Strings must use quotation marks.

### Mixing Numbers and Text Incorrectly

Incorrect:

```python
age = "30"
```

Correct:

```python
age = 30
```

If quotes are used, Python treats the value as text.

### Incorrect Boolean Capitalization

Incorrect:

```python
is_ready = true
```

Correct:

```python
is_ready = True
```

Python booleans must begin with a capital letter.

## Real-World Use

Variables and data types are used in every Python program.

Examples:

• storing dataset values  
• storing calculation results  
• storing configuration settings  
• storing API responses  

Example data analysis program:

```python
revenue = 120000
expenses = 45000

profit = revenue - expenses

print(profit)
```

Variables allow programs to store and manipulate business data.

## Lesson Recap

In this lesson you learned:

• variables store values in Python  
• Python supports multiple data types  
• common types include strings, integers, floats, and booleans  
• Python automatically determines data types  
• the `type()` function can reveal a value’s type  

Understanding variables and data types is essential for writing Python programs.

## Next Lesson

Next we will learn:

**Lesson 3 — Additional Python Data Types**

This lesson will introduce:

• tuples  
• sets  
• the `None` type  

These data types are commonly used when working with structured data in Python.