# Module 16 — Automation with Python  
## Lesson 4 — Automating Emails with Python

---

# Lesson Objective

By the end of this lesson you will understand:

- How Python can **send emails automatically**
- How to attach **reports or files to emails**
- How automation can distribute **daily or weekly reports**
- How Python integrates with **SMTP email systems**

This lesson introduces one of the most useful automation workflows:

**Automated reporting via email.**

---

# Overview

Many business processes rely on sending reports to stakeholders.

Example workflow:

1. Generate report
2. Save report file
3. Attach report to email
4. Send email to team

This process is often done **manually**.

Example:

- Run SQL query
- Export Excel report
- Open Outlook
- Write email
- Attach file
- Send email

Python can automate this entire workflow.

The automated process becomes:

```text
Run Python Script
       ↓
Generate Report
       ↓
Attach File
       ↓
Send Email
```

This is extremely common in:

- business reporting
- data pipelines
- analytics dashboards
- automated alerts

---

# Key Concepts

## SMTP

Most email systems use **SMTP (Simple Mail Transfer Protocol)**.

SMTP allows programs like Python to send email messages.

Example email servers:

| Provider | SMTP Server |
|------|------|
| Outlook | smtp.office365.com |
| Gmail | smtp.gmail.com |
| Yahoo | smtp.mail.yahoo.com |

Python connects to these servers to send email.

---

## Python Email Libraries

Python has built-in tools for sending emails.

Common modules:

| Module | Purpose |
|------|------|
| smtplib | Send emails |
| email.message | Create email messages |
| ssl | Secure connection |

These modules are part of the **Python standard library**.

---

## Automated Reporting Workflow

Typical automated reporting pipeline:

```text
Python Script
      ↓
Load Data
      ↓
Generate Report
      ↓
Save File
      ↓
Send Email
```

This allows entire reporting systems to run automatically.

---

# Decision Flow

Email automation is useful when:

```text
Do you send reports regularly?
        |
        Yes
        |
Is the email content predictable?
        |
        Yes
        |
Is the report generated automatically?
        |
        Yes
        |
Automate email delivery
```

Examples:

- Daily revenue reports
- Weekly KPI dashboards
- Alert notifications
- Data pipeline failures

---

# Code Examples

## Example 1 — Sending a Basic Email

```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "Daily Report"
msg["From"] = "your_email@example.com"
msg["To"] = "team@example.com"

msg.set_content("The daily report has been generated.")

with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login("your_email@example.com", "password")
    server.send_message(msg)

print("Email sent successfully")
```

This script:

1. Creates an email message
2. Connects to an SMTP server
3. Sends the email

---

## Example 2 — Sending an Email with an Attachment

Often automation scripts attach reports.

```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "Sales Report"
msg["From"] = "your_email@example.com"
msg["To"] = "manager@example.com"

msg.set_content("Attached is today's sales report.")

with open("sales_report.xlsx", "rb") as f:
    file_data = f.read()
    file_name = "sales_report.xlsx"

msg.add_attachment(file_data,
                   maintype="application",
                   subtype="octet-stream",
                   filename=file_name)

with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login("your_email@example.com", "password")
    server.send_message(msg)

print("Report emailed successfully")
```

This script:

1. Loads the Excel report
2. Attaches it to the email
3. Sends the message automatically

---

## Example 3 — Automated Reporting Pipeline

Combining report generation with email delivery.

```python
import pandas as pd
import smtplib
from email.message import EmailMessage

df = pd.read_csv("sales.csv")

summary = df.groupby("region")["sales"].sum()

summary_file = "sales_summary.xlsx"

summary.to_excel(summary_file)

msg = EmailMessage()

msg["Subject"] = "Daily Sales Report"
msg["From"] = "your_email@example.com"
msg["To"] = "team@example.com"

msg.set_content("Attached is the daily sales summary.")

with open(summary_file, "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="octet-stream",
        filename=summary_file
    )

with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login("your_email@example.com", "password")
    server.send_message(msg)

print("Automated report sent")
```

This script performs the entire workflow:

```text
Load Data
     ↓
Create Excel Report
     ↓
Send Email with Attachment
```

---

# SQL / Excel Comparison

### Manual Process

1. Run SQL query
2. Export results
3. Create Excel report
4. Write email
5. Attach file
6. Send email

Time: **30–60 minutes**

---

### Python Automation

```text
Run Python Script
       ↓
Report Generated
       ↓
Email Sent Automatically
```

Time: **seconds**

---

# Practice Exercises

## Exercise 1

Tags: Scripts, Automation, Notifications

Write a Python script that:

1. Sends an email message
2. Includes a subject and body

---

## Exercise 2

Tags: Scripts, Automation, Notifications

Modify the script to:

1. Attach a CSV file
2. Send the email automatically

---

## Exercise 3 (Real-World)

Tags: Excel, Scripts, Automation, Notifications

Create an automation script that:

1. Loads a dataset
2. Generates an Excel report
3. Sends the report via email

Imagine this script runs **every morning at 8 AM**.

---

# Common Mistakes

## Mistake 1 — Hardcoding Passwords

Bad practice:

```python
server.login("user@email.com", "mypassword")
```

Better approach:

Use **environment variables**.

Example:

```python
import os

password = os.getenv("EMAIL_PASSWORD")
```

---

## Mistake 2 — Forgetting TLS Security

Always secure SMTP connections.

Correct approach:

```python
server.starttls()
```

---

## Mistake 3 — Sending Large Attachments

Email servers may reject large files.

Better approach:

- compress files
- upload to shared storage
- include download link

---

# Real-World Use

Email automation is widely used in analytics and data engineering.

Examples include:

---

### Automated Business Reports

Python automatically sends:

- daily sales reports
- financial summaries
- operational dashboards

---

### Alert Systems

Automation scripts send alerts when:

- pipelines fail
- data is missing
- thresholds are exceeded

---

### Scheduled Notifications

Examples:

```text
Morning reports
Weekly executive dashboards
Monthly financial summaries
```

---

# Key Idea Cards

### Card 1

Python can **send emails automatically** using SMTP.

---

### Card 2

Automation scripts can **attach reports and distribute them automatically**.

---

### Card 3

Email automation is commonly used for **report distribution and alerting systems**.

---

# Lesson Recap

In this lesson you learned:

- How Python sends emails
- How to attach reports to emails
- How automated reporting systems distribute results

Combining **report generation + scheduling + email delivery** creates a fully automated reporting system.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 5: Automating File Management with Python**

You will learn how Python can:

- automatically organize files
- move and rename reports
- process folders of data files

This is extremely useful for **ETL workflows and reporting pipelines**.