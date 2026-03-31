# Module 1 — Getting Started

## Lesson 1 — What is Python?

### Lesson Objective

By the end of this lesson learners will understand:

• what Python is  
• why Python is widely used in data and analytics  
• how Python compares to tools like SQL and Excel  
• what types of problems Python can solve  

This lesson introduces the **purpose and value of Python** before diving into programming concepts.

### Overview

Python is a **programming language** used to give instructions to a computer.

These instructions tell the computer how to perform tasks such as:

• analyzing data  
• automating repetitive work  
• processing files  
• connecting to databases  
• building dashboards or applications  

Python is known for being **easy to read and easy to learn**, which is why it is widely used in data science, data engineering, and analytics.

Unlike Excel or SQL, which are designed for specific tasks, Python is a **general-purpose language**. This means it can perform many different kinds of work.

For example, Python can:

```text
Load data from a database
Clean and transform the data
Perform calculations
Create visualizations
Export results
```

Instead of doing each step manually, Python allows you to **automate the entire workflow**.

Because of this, Python is widely used in industries such as:

• finance  
• healthcare  
• technology  
• scientific research  
• data analytics  

In many organizations, Python works **alongside SQL and Excel**, helping automate and scale data workflows.

### Key Idea Cards (Cards)

#### Python Is a Programming Language (Card 1)

Python is a language used to write instructions that computers can execute.

Example Python instruction:

```python
print("Hello World")
```

This command tells the computer to display the text **Hello World**.

A program is simply a collection of many such instructions.

#### Python Is Designed to Be Readable (Card 2)

Python was designed with readability in mind.

Example Python code:

```python
total = price * quantity
```

Even someone new to programming can understand what this line does.

This readability makes Python a popular choice for beginners and professionals alike.

#### Python Automates Work (Card 3)

One of Python’s biggest advantages is automation.

Instead of manually performing repetitive work, Python can run an automated process.

Example workflow automation:

```python
load_data()
clean_data()
calculate_metrics()
export_results()
```

This allows analysts to focus on **insights rather than manual tasks**.

### Key Concepts (Tabs)

#### Programming Language (Tab 1)

A programming language is a structured way of writing instructions for computers.

Examples of programming languages include:

| Language | Common Use |
|--------|-------------|
| Python | data analysis, automation |
| SQL | querying databases |
| JavaScript | web development |
| R | statistical analysis |

Python is widely used because it combines **simplicity with powerful capabilities**.

#### Script (Tab 2)

A script is a Python program that runs a sequence of instructions.

Example script:

```python
print("Starting process")
print("Loading data")
print("Process complete")
```

Each line is executed in order.

Scripts are commonly used for:

• data processing  
• automation tasks  
• system operations  

#### Libraries (Tab 3)

Python becomes extremely powerful through **libraries**.

Libraries are collections of pre-written code that add functionality.

Examples:

| Library | Purpose |
|-------|---------|
| Pandas | data analysis |
| NumPy | numerical computing |
| Requests | working with APIs |
| Matplotlib | data visualization |

Using libraries allows developers to **build powerful systems quickly**.

### Decision Flow

When a Python program runs, it executes instructions **line by line**.

Example:

```python
print("Start")
print("Processing")
print("Done")
```

Execution flow:

```text
Program Starts
      ↓
Execute first instruction
      ↓
Execute second instruction
      ↓
Execute third instruction
      ↓
Program Ends
```

Unless told otherwise, Python will always run instructions **in sequence**.

Later lessons will introduce concepts that change this flow, such as:

• conditions  
• loops  
• functions  

### Code Examples (Tabs)

#### Example 1 — Your First Python Program (Tab 1)

```python
print("Hello World")
```

Output:

```text
Hello World
```

This is traditionally the first program beginners run when learning a new language.

#### Example 2 — Multiple Instructions (Tab 2)

```python
print("Starting program")
print("Loading data")
print("Processing complete")
```

Output:

```text
Starting program
Loading data
Processing complete
```

Each line is an instruction executed by Python.

#### Example 3 — Using Python for Simple Calculations (Tab 3)

Python can also perform calculations.

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

This program calculates a total value.

### SQL / Excel Comparison

Many people learning Python already know SQL or Excel.

Understanding the similarities makes Python easier to learn.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| instruction | statement | query clause | formula |
| automation | script | stored procedure | macro |
| calculation | code expression | computed column | formula |

Example Excel formula:

```text
=A1 * B1
```

Equivalent Python code:

```python
total = price * quantity
```

Both perform the same calculation.

### Practice Exercises (Tabs)

#### Exercise 1 (Tab 1)

Tags: print(), Strings, Running Code

Run the following Python code:

```python
print("Learning Python")
```

Observe the output.

#### Exercise 2 (Tab 2)

Tags: print(), Multiple Statements

Modify the code to display three messages:

```text
Starting analysis
Loading dataset
Analysis complete
```

#### Exercise 3 (Tab 3)

Tags: print(), Strings, Creative Coding

Write a short program that prints a message about why you want to learn Python.

Example:

```python
print("Python helps automate data workflows")
```

### Common Mistakes (Tabs)

#### Forgetting quotation marks (Tab 1)

Incorrect:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

Strings must use quotation marks.

#### Misspelling Python commands (Tab 2)

Incorrect:

```python
pritn("Hello")
```

Correct:

```python
print("Hello")
```

Python commands must be spelled exactly.

#### Expecting Python to understand plain language (Tab 3)

Incorrect:

```text
show message hello
```

Python requires proper syntax.

### Real-World Use

Python is widely used in real-world data workflows.

Examples include:

• processing millions of rows of data  
• automating reporting pipelines  
• pulling data from APIs  
• analyzing datasets  
• building dashboards  

Example data workflow script:

```python
load_data()
clean_data()
calculate_metrics()
generate_report()
```

Instead of manually repeating tasks, Python performs the entire process automatically.

### Lesson Recap

In this lesson you learned:

• Python is a programming language used to give instructions to computers  
• Python is easy to read and widely used in data analytics  
• programs execute instructions step by step  
• Python can automate repetitive tasks  

Understanding what Python is and how it works sets the foundation for learning programming.

### Next Lesson

Next you will learn:

**Lesson 2 — How to Request Access & Software**

This lesson will cover:

• how to obtain Python access within your organization  
• installing Python and required tools  
• preparing your environment for development  

Setting up the correct environment ensures that your Python programs will run successfully.