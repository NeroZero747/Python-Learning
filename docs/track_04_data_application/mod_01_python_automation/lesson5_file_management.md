# Module 16 — Automation with Python  
## Lesson 5 — Automating File Management with Python

---

# Lesson Objective

By the end of this lesson you will understand:

- How Python can **manage files automatically**
- How to **move, rename, copy, and delete files**
- How to **process folders of files automatically**
- How file automation is used in **ETL pipelines and reporting workflows**

This lesson focuses on automating one of the most common real-world problems:

**handling large numbers of files.**

---

# Overview

Many business workflows involve managing files.

Examples:

- Downloading reports into a folder
- Renaming files
- Moving reports into archive folders
- Processing hundreds of CSV files
- Cleaning up old files

Manual workflow example:

1. Download files
2. Rename them
3. Move them into folders
4. Open each file for processing

Python can automate all of this.

Instead of manually managing files, Python can:

```text
Scan Folder
     ↓
Identify Files
     ↓
Process Files
     ↓
Move or Rename Files
```

This is extremely common in:

- reporting automation
- data engineering pipelines
- data ingestion systems

---

# Key Concepts

## File Paths

Every file has a **path** that describes its location.

Example:

```text
data/sales_report.csv
```

Or on Windows:

```text
C:/reports/sales_report.csv
```

Python uses file paths to locate files.

---

## The `os` Module

Python includes the **os module** for working with files and directories.

Common operations:

| Operation | Function |
|------|------|
| List files | `os.listdir()` |
| Rename file | `os.rename()` |
| Delete file | `os.remove()` |
| Create folder | `os.mkdir()` |

---

## The `shutil` Module

The **shutil module** is used for file operations like copying and moving files.

Examples:

| Operation | Function |
|------|------|
| Copy file | `shutil.copy()` |
| Move file | `shutil.move()` |
| Delete folder | `shutil.rmtree()` |

---

# Decision Flow

File automation is useful when:

```text
Do you regularly process multiple files?
        |
        Yes
        |
Do the files follow a predictable format?
        |
        Yes
        |
Do they arrive in a folder?
        |
        Yes
        |
Automate the file workflow
```

Examples:

- processing daily CSV downloads
- organizing monthly reports
- archiving completed files

---

# Code Examples

## Example 1 — Listing Files in a Folder

Python can read all files in a directory.

```python
import os

files = os.listdir("data")

for file in files:
    print(file)
```

Example output:

```text
sales_january.csv
sales_february.csv
sales_march.csv
```

This allows Python to automatically detect files.

---

## Example 2 — Renaming Files

Python can rename files automatically.

```python
import os

os.rename("report.csv", "sales_report.csv")

print("File renamed successfully")
```

This is useful for standardizing file names.

---

## Example 3 — Moving Files

Using `shutil`:

```python
import shutil

shutil.move("report.csv", "archive/report.csv")

print("File moved to archive")
```

Example workflow:

```text
Reports Folder
      ↓
Processed
      ↓
Moved to Archive Folder
```

---

## Example 4 — Processing Multiple Files

Python can process every file in a folder.

```python
import os
import pandas as pd

folder = "data"

files = os.listdir(folder)

for file in files:

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print(file, "rows:", len(df))
```

This script:

1. Scans a folder
2. Identifies CSV files
3. Processes each file

This pattern is very common in **ETL pipelines**.

---

## Example 5 — Automatically Archiving Processed Files

```python
import os
import shutil

source = "data"
archive = "archive"

files = os.listdir(source)

for file in files:

    if file.endswith(".csv"):

        src_path = os.path.join(source, file)
        dest_path = os.path.join(archive, file)

        shutil.move(src_path, dest_path)

print("Files archived successfully")
```

This script:

1. Detects CSV files
2. Moves them to an archive folder
3. Keeps the main directory clean

---

# SQL / Excel Comparison

### Manual File Workflow

1. Download files
2. Open folder
3. Rename files
4. Move them to correct location
5. Process data

Time: **15–30 minutes**

---

### Python Automation

```text
Run Python Script
      ↓
Files Detected
      ↓
Files Processed
      ↓
Files Archived
```

Time: **seconds**

---

# Practice Exercises

## Exercise 1

Tags: Scripts, Automation

Write a script that:

1. Lists all files in a folder
2. Prints the file names.

---

## Exercise 2

Tags: File I/O, Scripts

Write a script that:

1. Reads all CSV files in a folder
2. Prints the number of rows in each file.

---

## Exercise 3

Tags: Scripts, Automation

Create a script that:

1. Moves processed files into an **archive folder**.

Folder structure:

```text
data/
archive/
```

---

## Exercise 4 (Real-World)

Tags: CI/CD, Scripts, ETL, Automation

Create an automation script that:

1. Detects new CSV files
2. Processes them
3. Moves them into an archive folder

This is a simplified **ETL ingestion pipeline**.

---

# Common Mistakes

## Mistake 1 — Hardcoding Paths

Bad practice:

```python
df = pd.read_csv("C:/Users/name/Desktop/data.csv")
```

Better approach:

```python
import os

base = os.getcwd()

file_path = os.path.join(base, "data", "data.csv")
```

---

## Mistake 2 — Not Checking File Types

Scripts should filter files.

Example:

```python
if file.endswith(".csv"):
```

Otherwise Python might try to read non-data files.

---

## Mistake 3 — Not Handling Missing Folders

Scripts may fail if folders do not exist.

Better approach:

```python
os.makedirs("archive", exist_ok=True)
```

---

# Real-World Use

File automation is heavily used in data workflows.

Examples include:

---

### Data Ingestion

ETL pipelines automatically:

```text
Detect new files
     ↓
Load data
     ↓
Process records
     ↓
Archive source files
```

---

### Reporting Pipelines

Python scripts:

- detect daily reports
- process them
- move them to reporting folders

---

### Data Lake Ingestion

Large systems automatically move data files into:

```text
raw/
processed/
archive/
```

This keeps data pipelines organized.

---

# Key Idea Cards

### Card 1

Python can automatically **detect and process files in folders**.

---

### Card 2

Modules like **os and shutil** manage file operations.

---

### Card 3

File automation is a core building block of **data pipelines and ETL systems**.

---

# Lesson Recap

In this lesson you learned:

- How Python manages files
- How to process folders of files
- How to move and rename files automatically
- How file automation supports data pipelines

You now understand how Python can automate **file-based workflows**.

---

# Next Lesson

In the next lesson you will learn:

**Module 15 — Lesson 6: Building a Complete Automated Reporting Pipeline**

You will combine everything learned so far:

- data loading
- report generation
- file management
- email automation
- scheduling

to build a **complete automated reporting system**.