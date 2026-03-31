# Module 2 — Programming Foundations

# Lesson 1 — What Is Programming?

## Lesson Objective

By the end of this lesson learners will understand:

• what programming means  
• how programs give instructions to computers  
• how programming automates tasks  
• how programming relates to tools like SQL and Excel  

This lesson introduces the **core idea behind programming before learning Python syntax**.

## Overview

Programming is the process of **writing instructions that tell a computer what to do**.

These instructions are written using a **programming language**, such as Python.

A program is simply a **series of instructions executed by a computer**.

For example, imagine the following task:

```text
Load sales data
Calculate total revenue
Calculate average sales
Export results
```

In Excel, you might do this manually using formulas and pivot tables.

In SQL, you might write queries.

In Python, you write a **program that performs the entire workflow automatically**.

Example Python program:

```python
sales = [120, 150, 90, 200]

total_sales = sum(sales)

print(total_sales)
```

Output:

```text
560
```

This program performs a calculation automatically.

Programming allows us to **automate tasks, analyze data, and build systems** that run without manual effort.

## Key Idea Cards (3 Cards)

### Programs Are Sets of Instructions

A computer program is a sequence of instructions executed by a computer.

Example program:

```python
print("Start")
print("Processing")
print("Done")
```

Each instruction runs **in order**.

### Programming Automates Work

Programming allows repetitive work to be automated.

Instead of performing steps manually, the program runs the process.

Example workflow automation:

```python
load_data()
clean_data()
calculate_metrics()
export_report()
```

Automation saves time and reduces errors.

### Programming Uses Logic

Programs often contain logic that controls behavior.

Example:

```python
sales = 120

if sales > 100:
    print("High sales")
```

Logic allows programs to make **decisions**.

## Key Concepts

### Instruction

An instruction is a command given to a computer.

Example:

```python
print("Hello")
```

The instruction tells Python to display a message.

Programs are built from **many instructions executed in sequence**.

### Program

A program is a collection of instructions.

Example program:

```python
print("Loading data")
print("Calculating results")
print("Process complete")
```

Programs run from **top to bottom unless logic changes the flow**.

### Programming Language

A programming language is the system used to write instructions.

Examples:

| Language | Common Use |
|------|------|
| Python | automation, analytics |
| SQL | querying databases |
| JavaScript | web development |
| R | statistical analysis |

Each language is designed for different purposes.

## Decision Flow

Programs normally execute instructions **in order**.

Example:

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

Execution flow:

```text
Program Starts
      ↓
Step 1
      ↓
Step 2
      ↓
Step 3
      ↓
Program Ends
```

Later lessons will introduce ways to control program flow:

• conditions  
• loops  
• functions  

## Code Examples

### Example 1 — Basic Program

```python
print("Starting program")
print("Processing data")
print("Program complete")
```

Output:

```text
Starting program
Processing data
Program complete
```

Python executes each instruction sequentially.

### Example 2 — Performing a Calculation

```python
price = 20
quantity = 5

total = price * quantity

print(total)
```

Output:

```text
100
```

This program calculates a total value.

### Example 3 — Program Using a List

```python
sales = [100, 150, 200]

total_sales = sum(sales)

print(total_sales)
```

Output:

```text
450
```

Programs can operate on collections of data.

## SQL / Excel Comparison

If you already use SQL or Excel, programming concepts will feel familiar.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| instruction | statement | query clause | formula |
| program | script | SQL script | workbook |
| automation | script execution | stored procedure | macro |

Example Excel formula:

```text
=A1 * B1
```

Equivalent Python:

```python
total = price * quantity
```

Both perform calculations automatically.

## Practice Exercises

### Exercise 1

Tags: print(), Data I/O

Write a program that prints three steps:

```text
Loading data
Analyzing data
Process complete
```

Example:

```python
print("Loading data")
print("Analyzing data")
print("Process complete")
```

### Exercise 2

Tags: print(), Arithmetic

Write a program that calculates the total of two numbers.

Example:

```python
a = 10
b = 15

print(a + b)
```

Run the program and observe the result.

### Exercise 3

Tags: print(), CI/CD, Automation

Create a small program that prints a message about learning Python.

Example:

```python
print("Python helps automate analytics workflows")
```

## Common Mistakes

### Thinking Programming Is Only for Engineers

Programming is widely used by:

• data analysts  
• scientists  
• researchers  
• finance professionals  

Many analysts use Python alongside SQL and Excel.

### Expecting Programs to Understand Natural Language

Incorrect:

```text
calculate total sales
```

Computers require **structured instructions**.

### Forgetting Programs Execute in Order

Code runs from top to bottom unless control logic changes the flow.

Example:

```python
print("A")
print("B")
print("C")
```

Output will always be:

```text
A
B
C
```

## Real-World Use

Programming is used in many real-world data workflows.

Examples:

• automating data pipelines  
• analyzing large datasets  
• generating automated reports  
• building dashboards  

Example data pipeline program:

```python
load_sales_data()
clean_data()
calculate_revenue()
generate_dashboard()
```

This automation replaces manual workflows.

## Lesson Recap

In this lesson you learned:

• programming is writing instructions for computers  
• programs execute instructions sequentially  
• programming allows automation of tasks  
• Python programs can perform calculations and analyze data  

These concepts form the **foundation for learning Python programming**.

## Next Lesson

Next we will learn:

**Lesson 2 — Variables & Data Types**

You will learn:

• how Python stores information  
• how variables work  
• common Python data types  

These concepts are used in **every Python program**.