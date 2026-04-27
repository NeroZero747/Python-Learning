"""
Rebuild lesson05_deploying_data_applications.html from scratch.
Fixes every audit issue found in the original file.
"""
import os, re, html as htmlmod

TARGET = os.path.join("pages", "mod_05_data_application", "lesson05_deploying_data_applications.html")

# ── Lesson metadata ───────────────────────────────────────
LESSON_NUM   = 5
LESSON_TITLE = "Deploying Data Applications"
MODULE_NUM   = 5
MODULE_TITLE = "Building Data Applications"
TRACK_LABEL  = "Data Applications Track"
PROGRESS     = "5/7"
PREV_LESSON  = ("lesson04_exporting_data.html", "Exporting Data")
NEXT_LESSON  = ("lesson06_shiny_for_python.html", "Shiny for Python")

# ── 5 Objectives ──────────────────────────────────────────
objectives = [
    ("fa6-solid:cloud-arrow-up", "Understand application hosting",       "Explain what it means to deploy a Streamlit app so other people can reach it through a URL"),
    ("fa6-solid:file-lines",     "Create a requirements file",           "Write a requirements.txt that lists every Python package your app needs to run on a remote server"),
    ("fa6-solid:server",         "Compare deployment environments",      "Distinguish between Streamlit Community Cloud, Docker containers, and internal company servers"),
    ("fa6-solid:arrows-spin",    "Describe a CI/CD pipeline",            "Outline how automated testing and deployment push code from your laptop to a live server safely"),
    ("fa6-solid:lock",           "Manage secrets and environment variables", "Store sensitive values like API keys outside your code so they stay safe in production"),
]

# ── Overview — restaurant analogy ─────────────────────────
HOOK_QUOTE = "Deploying an application means putting your finished Streamlit dashboard on a server so that anyone with the link can open it in their browser, without needing Python installed on their own machine."
ANALOGY_INTRO = "Think of deployment like opening a restaurant: you have been perfecting recipes in your home kitchen (your laptop), and now you need a real restaurant space, a supply chain for ingredients, a menu that lists every dish, and a way to keep the kitchen running smoothly every day. Each deployment concept maps to one part of that restaurant."
overview_cards = [
    ("fa6-solid:cloud-arrow-up", "Application Hosting",    "The restaurant building &mdash; a public space customers can walk into",
     "Hosting means placing your app on a computer (a server) that is always on and connected to the internet. When you deploy to Streamlit Community Cloud, you are renting a small restaurant space for free &mdash; anyone with the URL can visit and use your dashboard."),
    ("fa6-solid:file-lines",     "Requirements File",      "The supply list &mdash; every ingredient the kitchen needs to open",
     "A requirements.txt file tells the server exactly which Python packages to install. Without it the server has no idea what libraries your code imports, just like a kitchen that opens without stocking its pantry. Each line names one package and optionally pins a version."),
    ("fa6-solid:server",         "Deployment Environments","The franchise model &mdash; different locations with different rules",
     "Streamlit Community Cloud is a small free location, a Docker container is a portable food truck you can park anywhere, and an internal company server is a private cafeteria behind a badge door. Each environment has its own trade-offs in cost, control, and security."),
    ("fa6-solid:arrows-spin",    "CI/CD Pipelines",        "The daily delivery truck &mdash; automated restocking without closing the kitchen",
     "Continuous Integration and Continuous Deployment (CI/CD) means that every time you push code to GitHub, automated tests run and, if they pass, the new version goes live automatically. You never have to manually log in and restart the server."),
    ("fa6-solid:lock",           "Secrets Management",     "The safe in the back office &mdash; keeps cash and keys away from the dining room",
     "API keys, database passwords, and tokens must never appear in your source code. Secrets management stores them as environment variables that your app reads at runtime. If someone sees your code on GitHub, they see variable names but not the actual values."),
]
OVERVIEW_TIP = "Even if you are not a DevOps engineer, understanding deployment basics lets you hand off your work cleanly &mdash; or ship a quick prototype yourself on Streamlit Community Cloud in under five minutes."

# ── Key Takeaways ─────────────────────────────────────────
takeaways = [
    ("pink", "fa6-solid:cloud-arrow-up", "Hosting Makes Your App Public",
     "Running streamlit run app.py on your laptop only works for you. Deploying to a server gives your app a permanent URL that anyone on the internet (or your company network) can open in a browser without installing Python.",
     ["server", "URL", "public access"]),
    ("violet", "fa6-solid:file-lines", "requirements.txt Is Mandatory",
     "Every remote server starts with a bare Python installation. Your requirements.txt file tells it which packages to install. If a package is missing from the list, your app crashes on the server even though it runs perfectly on your laptop.",
     ["requirements.txt", "pip freeze", "version pinning"]),
    ("blue", "fa6-solid:server", "Choose the Right Environment",
     "Streamlit Community Cloud is free and beginner-friendly but limited in resources. Docker containers give you full control and portability. Internal company servers offer security but require IT support. Pick the one that matches your audience and budget.",
     ["Streamlit Cloud", "Docker", "on-premise"]),
    ("emerald", "fa6-solid:arrows-spin", "CI/CD Removes Manual Steps",
     "Without CI/CD, deploying means manually copying files, restarting servers, and hoping nothing breaks. A CI/CD pipeline runs your tests automatically on every push and only deploys the new version if all tests pass &mdash; no human intervention needed.",
     ["GitHub Actions", "automated tests", "push to deploy"]),
    ("amber", "fa6-solid:lock", "Never Hard-Code Secrets",
     "Pasting an API key directly into your Python file means anyone who reads the code can steal it. Environment variables and platform secret stores keep credentials out of your source code and out of version control.",
     ["env variables", "st.secrets", ".gitignore"]),
]

# ── Key Concepts (5 tabs) ─────────────────────────────────
kc_tabs = [
    {
        "label": "Streamlit Cloud Deploy",
        "icon": "fa6-solid:cloud-arrow-up",
        "color": "pink",
        "badge": "Free Tier",
        "intro": "Streamlit Community Cloud connects directly to your GitHub repository. When you push a commit, the platform pulls the latest code, installs the packages listed in requirements.txt, and starts the app at a public URL. You do not need to configure a server or write any deployment scripts.",
        "code": """# 1. Push your project to GitHub with these files:
#    app.py              ← your Streamlit code
#    requirements.txt    ← package list
#
# 2. Go to share.streamlit.io
# 3. Click "New app" → pick your repo, branch, and file
# 4. Click "Deploy" — Streamlit builds and launches the app
#
# Your app is now live at:
#   https://YOUR-USERNAME-YOUR-REPO.streamlit.app""",
        "params": [
            ("Repository",  "GitHub URL",  "The public or private repo that contains app.py"),
            ("Branch",      "string",      "The Git branch to deploy from (usually main)"),
            ("Main file",   "path",        "The entry-point Python file (e.g. app.py)"),
        ],
        "tip": "Streamlit Community Cloud watches your repo. Every time you push to the selected branch, the app redeploys automatically &mdash; no manual restart needed."
    },
    {
        "label": "requirements.txt",
        "icon": "fa6-solid:file-lines",
        "color": "violet",
        "badge": "Essential",
        "intro": "A requirements.txt file is a plain-text list of Python packages your app needs. The server reads this file during deployment and runs pip install for every line. Pinning versions (e.g. pandas==2.2.0) prevents surprise breakages when a library releases a new version.",
        "code": """# requirements.txt — one package per line
streamlit==1.45.0
pandas==2.2.0
openpyxl==3.1.2
plotly==5.22.0
python-dotenv==1.1.0

# Generate automatically from your environment:
# pip freeze > requirements.txt
#
# Or list only the packages you actually import:
# pip install pipreqs
# pipreqs . --force""",
        "params": [
            ("package==version", "pinned",   "Installs exactly that version &mdash; safest for production"),
            ("package>=version", "minimum",  "Installs that version or newer &mdash; allows updates"),
            ("package",          "unpinned", "Installs the latest version &mdash; convenient but risky"),
        ],
        "tip": "Run pip freeze > requirements.txt to capture every package in your current environment, but review the list and remove packages your app does not actually import."
    },
    {
        "label": "Docker Basics",
        "icon": "fa6-solid:box-open",
        "color": "blue",
        "badge": "Portable",
        "intro": "A Docker container packages your app, its dependencies, and a lightweight operating system into a single image that runs identically on any machine. You write a Dockerfile that describes the build steps, then anyone with Docker installed can start your app with one command.",
        "code": """# Dockerfile — build instructions for the container
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (Docker caches this layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files
COPY . .

# Expose the port Streamlit uses
EXPOSE 8501

# Start the app when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8501"]""",
        "params": [
            ("FROM",    "image",   "The base image to start from (e.g. python:3.12-slim)"),
            ("WORKDIR", "path",    "The directory inside the container where commands run"),
            ("COPY",    "src dest","Copies files from your machine into the container"),
            ("RUN",     "command", "Executes a shell command during the build (e.g. pip install)"),
            ("CMD",     "command", "The default command that runs when the container starts"),
        ],
        "tip": "Docker containers are the standard way to deploy apps in large companies. Even if you start on Streamlit Cloud, learning Docker prepares you for enterprise deployment."
    },
    {
        "label": "CI/CD with GitHub Actions",
        "icon": "fa6-solid:arrows-spin",
        "color": "emerald",
        "badge": "Automation",
        "intro": "GitHub Actions lets you define workflows that run automatically when you push code. A typical CI/CD workflow has two stages: first it installs dependencies and runs tests, then &mdash; if the tests pass &mdash; it deploys the new version. The workflow is defined in a YAML file inside your repository.",
        "code": """# .github/workflows/deploy.yml
name: Test and Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/

  deploy:
    needs: test            # Only runs if tests pass
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying to production server..."
      # Add your deployment commands here""",
        "params": [
            ("on: push",     "trigger",  "Runs the workflow every time code is pushed to the branch"),
            ("jobs: test",   "job",      "Installs dependencies and runs pytest to catch bugs early"),
            ("needs: test",  "depends",  "The deploy job waits for the test job to succeed first"),
        ],
        "tip": "You do not need CI/CD for a personal prototype, but any app that multiple people rely on should have automated tests that run before every deployment."
    },
    {
        "label": "Secrets & Env Variables",
        "icon": "fa6-solid:lock",
        "color": "orange",
        "badge": "Security",
        "intro": "Sensitive values like API keys and database passwords must never appear in your source code. Instead, store them as environment variables or in a platform-specific secrets manager. Your Python code reads these values at runtime using os.environ or st.secrets, so the actual credentials stay hidden.",
        "code": """import os
import streamlit as st

# ── Option 1: os.environ (works everywhere) ──────────
api_key = os.environ.get("API_KEY")
if not api_key:
    st.error("API_KEY environment variable is not set.")
    st.stop()

# ── Option 2: st.secrets (Streamlit Cloud only) ──────
# Create a file at .streamlit/secrets.toml:
#   API_KEY = "your-key-here"
#   DB_HOST = "db.example.com"
#
# Then read it in Python:
api_key = st.secrets["API_KEY"]
db_host = st.secrets["DB_HOST"]

# ── Keep secrets out of Git ──────────────────────────
# Add these lines to .gitignore:
#   .streamlit/secrets.toml
#   .env""",
        "params": [
            ("os.environ",   "dict-like", "Reads environment variables set on the server or in a .env file"),
            ("st.secrets",   "dict-like", "Reads from .streamlit/secrets.toml or the Streamlit Cloud secrets UI"),
            (".gitignore",   "file",      "Tells Git to never track files that contain secrets"),
        ],
        "tip": "Before every git push, search your code for hard-coded strings that look like keys or passwords. If you find one, move it to an environment variable immediately."
    },
]

# ── Code Examples (5 tabs) ────────────────────────────────
code_examples = [
    {
        "title": "Deploy to Streamlit Cloud",
        "desc": "This example shows the minimal file structure you need to deploy a Streamlit app to the free Community Cloud. The key is having a requirements.txt alongside your app.py so the server knows which packages to install.",
        "code": """# app.py — a minimal Streamlit dashboard
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard")

# Load data from a CSV bundled with the repo
df = pd.read_csv("data/sales.csv")

# Show a summary metric
total = df["revenue"].sum()
st.metric("Total Revenue", f"${total:,.0f}")

# Display an interactive table
st.dataframe(df, use_container_width=True)""",
        "terminal_cmd": "streamlit run app.py",
        "terminal_out": "You can now view your Streamlit app in your browser.\nLocal URL: http://localhost:8501\nNetwork URL: http://192.168.1.10:8501",
        "tip": "After confirming the app works locally, push the entire folder to GitHub and connect it on share.streamlit.io. The cloud version uses the exact same command under the hood."
    },
    {
        "title": "Write requirements.txt",
        "desc": "This example demonstrates two ways to generate a requirements.txt file: the quick-and-dirty pip freeze approach and the cleaner pipreqs approach that only lists packages your code actually imports.",
        "code": """# Method 1 — capture everything in the environment
# (includes packages you may not need)
# Run in your terminal:
# pip freeze > requirements.txt

# Method 2 — scan imports and list only what you use
# pip install pipreqs
# pipreqs . --force

# Method 3 — write it by hand (most control)
# requirements.txt contents:
# streamlit==1.45.0
# pandas==2.2.0
# openpyxl==3.1.2
# plotly==5.22.0

# Verify the file works by installing into a fresh env:
import subprocess, sys

def test_requirements():
    \"\"\"Install requirements in the current env to verify.\"\"\"
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install",
         "-r", "requirements.txt", "--dry-run"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print("All packages resolved successfully.")
    else:
        print("Error:", result.stderr)

test_requirements()""",
        "terminal_cmd": "python verify_requirements.py",
        "terminal_out": "All packages resolved successfully.",
        "tip": "Pin exact versions (pandas==2.2.0) for production apps. Use >= only when you intentionally want automatic updates."
    },
    {
        "title": "Build a Docker Image",
        "desc": "This example walks through creating a Dockerfile for a Streamlit app and building it into a container image. Once built, the image can run on any machine that has Docker installed &mdash; no Python setup required.",
        "code": """# Dockerfile — place this in your project root
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies first (cached by Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Health check — verify the app responds
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Launch the app
CMD ["streamlit", "run", "app.py", \\
     "--server.port=8501", \\
     "--server.address=0.0.0.0"]""",
        "terminal_cmd": "docker build -t sales-dashboard . && docker run -p 8501:8501 sales-dashboard",
        "terminal_out": "Successfully built a]3f2e1d\nSuccessfully tagged sales-dashboard:latest\n\n  You can now view your Streamlit app in your browser.\n  URL: http://0.0.0.0:8501",
        "tip": "The --server.address=0.0.0.0 flag is critical. Without it, Streamlit only listens on localhost inside the container, so the port mapping cannot reach it."
    },
    {
        "title": "GitHub Actions Workflow",
        "desc": "This example creates a CI/CD pipeline that automatically tests your code on every push to the main branch. If the tests pass, a second job runs your deployment commands. The file lives at .github/workflows/deploy.yml inside your repository.",
        "code": """# .github/workflows/deploy.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python -m pytest tests/ -v

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Deploy to server
        env:
          DEPLOY_KEY: ${{ "secrets.DEPLOY_KEY" }}
        run: |
          echo "Deploying to production..."
          # Replace with your actual deploy command""",
        "terminal_cmd": "git push origin main",
        "terminal_out": "remote: CI/CD Pipeline #42 — test: ✓ passed (3 tests)\nremote: CI/CD Pipeline #42 — deploy: ✓ deployed to production\nTo github.com:user/sales-dashboard.git\n   a1b2c3d..d4e5f6g  main -> main",
        "tip": "Store deployment credentials in GitHub Settings → Secrets → Actions. The workflow reads them as environment variables without ever printing them in logs."
    },
    {
        "title": "Read Secrets at Runtime",
        "desc": "This example shows how to read sensitive configuration values from environment variables and from Streamlit's built-in secrets manager. Both approaches keep credentials out of your source code and out of version control.",
        "code": """import os
import streamlit as st

# ── Read secrets from environment variables ──────────
# Set these on your server or in a .env file
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    st.error("Missing API_KEY — set it as an env variable.")
    st.stop()

st.success(f"Connected to {DB_HOST}:{DB_PORT}")

# ── Streamlit secrets (Cloud or local .toml file) ────
# .streamlit/secrets.toml:
#   [database]
#   host = "db.example.com"
#   port = 5432
#   password = "s3cur3-p@ss"

db = st.secrets["database"]
st.write(f"Database host: {db['host']}")

# ── .gitignore — keep secrets out of Git ─────────────
# Add these lines to .gitignore:
#   .env
#   .streamlit/secrets.toml""",
        "terminal_cmd": "API_KEY=abc123 streamlit run app.py",
        "terminal_out": "  You can now view your Streamlit app in your browser.\n  Local URL: http://localhost:8501\n  ✅ Connected to localhost:5432",
        "tip": "On Streamlit Community Cloud, paste your secrets into the app settings UI instead of uploading a secrets.toml file. The platform encrypts them at rest."
    },
]

# ── Comparison rows (Python vs SQL vs Excel) ─────────────
comparison_rows = [
    ("fa6-solid:cloud-arrow-up", "Application Hosting",
     "streamlit run app.py",               "Starts a local server you can share via a public URL after deployment",
     "N/A",                                "SQL databases are always running on a server &mdash; no separate deploy step",
     "File &rarr; Share &rarr; OneDrive",  "Excel files are shared via cloud storage links, not deployed as apps"),
    ("fa6-solid:file-lines", "Dependency List",
     "pip freeze &gt; requirements.txt",   "Captures every Python package and version into a text file",
     "N/A",                                "SQL has no package manager &mdash; the database engine provides all functions",
     "N/A",                                "Excel has no external dependencies &mdash; all features are built in"),
    ("fa6-solid:box-open", "Containerization",
     "docker build -t app .",              "Packages the app + OS + packages into a portable image",
     "docker pull postgres:16",            "Database servers also run in containers in production",
     "N/A",                                "Excel is a desktop application that cannot be containerized"),
    ("fa6-solid:arrows-spin", "Automated Deploy",
     "git push &rarr; GitHub Actions",     "CI/CD pipelines test code and deploy automatically on every push",
     "Flyway / Liquibase",                 "SQL migration tools version-control and auto-apply schema changes",
     "Power Automate",                     "Excel workflows can be automated with Microsoft Power Automate"),
    ("fa6-solid:lock", "Secrets Management",
     "os.environ[&quot;KEY&quot;]",        "Reads credentials from environment variables at runtime",
     "pg_hba.conf / IAM roles",           "Database access is controlled by config files or cloud IAM policies",
     "File &rarr; Protect Workbook",       "Excel offers password protection but not environment-variable secrets"),
]

# ── Practice Exercises (5 tabs) ───────────────────────────
practice_exercises = [
    {
        "title": "Create requirements.txt",
        "tasks": [
            "Create a new file called <code>requirements.txt</code> in your project root.",
            "List the four packages your app imports: <code>streamlit</code>, <code>pandas</code>, <code>openpyxl</code>, and <code>plotly</code>.",
            "Pin each package to an exact version using the <code>==</code> syntax.",
            "Run <code>pip install -r requirements.txt --dry-run</code> to verify all packages resolve."
        ],
        "solution": """# requirements.txt
streamlit==1.45.0
pandas==2.2.0
openpyxl==3.1.2
plotly==5.22.0

# Verify in your terminal:
# pip install -r requirements.txt --dry-run""",
        "why": "Pinning exact versions ensures the server installs the same packages you tested locally. A missing or mismatched version is the number-one cause of &ldquo;works on my machine&rdquo; deployment failures."
    },
    {
        "title": "Write a Dockerfile",
        "tasks": [
            "Create a file called <code>Dockerfile</code> (no extension) in your project root.",
            "Use <code>python:3.12-slim</code> as the base image.",
            "Copy <code>requirements.txt</code> first and run <code>pip install</code> before copying the rest of the code.",
            "Expose port <code>8501</code> and set the CMD to launch <code>streamlit run app.py</code>."
        ],
        "solution": """# Dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]""",
        "why": "Copying requirements.txt separately lets Docker cache the pip install layer. If you only change app.py, Docker skips the install step entirely &mdash; builds finish in seconds instead of minutes."
    },
    {
        "title": "Add a GitHub Actions Workflow",
        "tasks": [
            "Create the folder <code>.github/workflows/</code> in your project.",
            "Create a file called <code>ci.yml</code> inside that folder.",
            "Define a <code>test</code> job that installs dependencies and runs <code>pytest</code>.",
            "Trigger the workflow on every push to the <code>main</code> branch."
        ],
        "solution": """# .github/workflows/ci.yml
name: Run Tests

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/ -v""",
        "why": "Automated tests catch bugs before they reach production. If a test fails, the workflow stops and the broken code never gets deployed."
    },
    {
        "title": "Store Secrets Safely",
        "tasks": [
            "Create a <code>.streamlit/secrets.toml</code> file with a fake API key.",
            "Read the key in your app using <code>st.secrets[\"API_KEY\"]</code>.",
            "Add <code>.streamlit/secrets.toml</code> to your <code>.gitignore</code> file.",
            "Verify that <code>git status</code> does not list the secrets file."
        ],
        "solution": """# .streamlit/secrets.toml
API_KEY = "sk-test-abc123def456"

# app.py
import streamlit as st

api_key = st.secrets["API_KEY"]
st.write(f"Key loaded: {api_key[:8]}...")  # Show only a prefix

# .gitignore — add this line:
# .streamlit/secrets.toml""",
        "why": "Adding the secrets file to .gitignore prevents it from being committed to Git. Even if you accidentally run git add, Git will skip ignored files."
    },
    {
        "title": "Deploy on Streamlit Cloud",
        "tasks": [
            "Push your project (app.py + requirements.txt + data/) to a public GitHub repository.",
            "Go to <a href='https://share.streamlit.io' class='text-brand font-semibold'>share.streamlit.io</a> and sign in with GitHub.",
            "Click <strong>New app</strong>, select your repo, branch, and main file.",
            "Wait for the build to finish and open the public URL in a new tab."
        ],
        "solution": """# Step-by-step commands to push to GitHub:

# 1. Initialize a Git repo (skip if already done)
# git init

# 2. Add all project files
# git add app.py requirements.txt data/

# 3. Commit
# git commit -m "Initial deploy"

# 4. Create a GitHub repo and push
# git remote add origin https://github.com/YOUR-USER/YOUR-REPO.git
# git push -u origin main

# 5. Go to share.streamlit.io → New app → Deploy
# Your app is live at:
#   https://YOUR-USER-YOUR-REPO.streamlit.app""",
        "why": "Streamlit Community Cloud is the fastest way to share a dashboard publicly. The entire deploy process takes under five minutes and costs nothing."
    },
]

# ── Mistakes (5 tabs) ─────────────────────────────────────
mistakes = [
    {
        "title": "Forgetting requirements.txt",
        "why_happens": "The app runs locally because packages are already installed, so the developer forgets the server needs a list.",
        "wrong": """# Project structure — missing requirements.txt
# my_app/
#   app.py
#   data/sales.csv
#
# Deploy to Streamlit Cloud → ERROR:
# ModuleNotFoundError: No module named 'plotly'""",
        "correct": """# Project structure — with requirements.txt
# my_app/
#   app.py
#   requirements.txt   ← lists all packages
#   data/sales.csv
#
# requirements.txt:
# streamlit==1.45.0
# pandas==2.2.0
# plotly==5.22.0""",
        "fix": "Always create a requirements.txt before deploying. Run pip freeze > requirements.txt or use pipreqs to scan your imports."
    },
    {
        "title": "Hard-coding API keys in source code",
        "why_happens": "During development it is quick to paste a key directly into the script, and the developer forgets to remove it before pushing to GitHub.",
        "wrong": """import requests

# Secret is visible to anyone who reads the code
API_KEY = "sk-live-abc123def456ghi789"
response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {API_KEY}"}
)""",
        "correct": """import os
import requests

# Secret is read from the environment at runtime
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise SystemExit("Set the API_KEY env variable.")

response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {API_KEY}"}
)""",
        "fix": "Store secrets in environment variables or in .streamlit/secrets.toml and add those files to .gitignore so they never enter version control."
    },
    {
        "title": "Using pip freeze without review",
        "why_happens": "pip freeze lists every package in the environment, including ones unrelated to the project, making the file bloated and fragile.",
        "wrong": """# requirements.txt generated by pip freeze
# Contains 87 packages including unrelated ones:
streamlit==1.45.0
pandas==2.2.0
black==24.3.0          # ← code formatter, not needed at runtime
mypy==1.9.0            # ← type checker, not needed at runtime
jupyter==1.0.0         # ← notebook, not needed at runtime
# ... 82 more lines""",
        "correct": """# requirements.txt — only packages the app imports
streamlit==1.45.0
pandas==2.2.0
openpyxl==3.1.2
plotly==5.22.0
python-dotenv==1.1.0""",
        "fix": "Use pipreqs to scan your code and list only imported packages, or write the file by hand. Fewer packages mean faster builds and fewer version conflicts."
    },
    {
        "title": "Not exposing the correct port in Docker",
        "why_happens": "The developer forgets that Streamlit defaults to port 8501 and either omits the EXPOSE line or maps the wrong port.",
        "wrong": """# Dockerfile — wrong port
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000   # ← Streamlit does not use 5000
CMD ["streamlit", "run", "app.py"]""",
        "correct": """# Dockerfile — correct port
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", \\
     "--server.port=8501", \\
     "--server.address=0.0.0.0"]""",
        "fix": "Always EXPOSE 8501 and pass --server.port=8501 --server.address=0.0.0.0 in the CMD. The address flag ensures the container accepts connections from outside."
    },
    {
        "title": "Skipping tests in the CI/CD pipeline",
        "why_happens": "Adding a test step feels like extra work, so the developer deploys directly on every push without validation.",
        "wrong": """# .github/workflows/deploy.yml — no tests
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying..."
      # Deploys broken code if a bug slipped in""",
        "correct": """# .github/workflows/deploy.yml — with tests
name: Deploy
on:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/ -v
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying..."
      # Only runs if all tests pass""",
        "fix": "Always add a test job before the deploy job and use needs: test so deployment is blocked when tests fail."
    },
]

# ── Real-World Applications ──────────────────────────────
real_world = [
    ("fa6-solid:chart-line",     "Sales Dashboards",         "Deploy a Streamlit dashboard that shows live revenue metrics so the entire sales team can check numbers from any browser."),
    ("fa6-solid:hospital",       "Healthcare Monitoring",    "Host a patient data dashboard on an internal server behind a VPN so clinicians can view trends without installing Python."),
    ("fa6-solid:graduation-cap", "Academic Research",        "Share interactive visualizations of research data via Streamlit Cloud so peer reviewers can explore results directly."),
    ("fa6-solid:building",       "Corporate Reporting",      "Run a weekly KPI dashboard inside a Docker container on the company Kubernetes cluster for enterprise-grade reliability."),
    ("fa6-solid:robot",          "ML Model Demos",           "Deploy a machine-learning inference app so stakeholders can upload data and see predictions live in a web browser."),
    ("fa6-solid:earth-americas", "Open Data Portals",        "Publish a public Streamlit app that lets anyone explore government or NGO datasets without downloading raw files."),
]

# ── Quiz (5 questions) ────────────────────────────────────
quiz = [
    {
        "type": "tf",
        "stem": "A requirements.txt file is optional when deploying to Streamlit Community Cloud.",
        "answer": False,
        "fb_correct": "Correct! Without requirements.txt the server cannot install your packages and the app will crash.",
        "fb_wrong": "Not quite — requirements.txt is mandatory. Without it the server has no way to know which packages to install.",
    },
    {
        "type": "mc",
        "stem": "Which command generates a requirements.txt that lists only the packages your code actually imports?",
        "options": [
            ("pip freeze > requirements.txt", False),
            ("pipreqs . --force", True),
            ("pip list > requirements.txt", False),
            ("python -m pip export", False),
        ],
        "fb_correct": "Correct! pipreqs scans your import statements and lists only the packages you use.",
        "fb_wrong": "Not quite — pip freeze captures every package in the environment, not just the ones your code imports. pipreqs . --force scans imports only.",
    },
    {
        "type": "tf",
        "stem": "In a Dockerfile, the EXPOSE instruction automatically makes the port accessible from outside the container.",
        "answer": False,
        "fb_correct": "Correct! EXPOSE is documentation only. You still need -p 8501:8501 in the docker run command to map the port.",
        "fb_wrong": "Not quite — EXPOSE is a hint for documentation. You must use -p 8501:8501 when running the container to actually map the port.",
    },
    {
        "type": "mc",
        "stem": "Where should you store API keys for a Streamlit app deployed to Streamlit Community Cloud?",
        "options": [
            ("Directly in the Python source code", False),
            ("In a public GitHub repository README", False),
            ("In the Streamlit Cloud secrets manager", True),
            ("In a comment inside requirements.txt", False),
        ],
        "fb_correct": "Correct! Streamlit Cloud encrypts secrets and makes them available via st.secrets at runtime.",
        "fb_wrong": "Not quite — secrets should go in the Streamlit Cloud secrets manager, never in source code or public files.",
    },
    {
        "type": "mc",
        "stem": "In a GitHub Actions workflow, what does <code>needs: test</code> do on the deploy job?",
        "options": [
            ("It runs the deploy and test jobs at the same time", False),
            ("It skips the test job entirely", False),
            ("It ensures the deploy job only runs after the test job passes", True),
            ("It merges the test and deploy jobs into one step", False),
        ],
        "fb_correct": "Correct! The needs keyword creates a dependency — deploy waits for test to succeed before starting.",
        "fb_wrong": "Not quite — needs: test means the deploy job will not start until the test job finishes successfully.",
    },
]

# ── Next lesson preview ──────────────────────────────────
next_preview = [
    ("fa6-solid:leaf",       "Shiny for Python Basics"),
    ("fa6-solid:sliders",    "Reactive UI Components"),
    ("fa6-solid:code-compare","Shiny vs Streamlit Architecture"),
]

# ── Sidebar lessons ──────────────────────────────────────
sidebar_lessons = [
    ("lesson01_why_build_data_apps.html",           "1. Why Build Data Apps?"),
    ("lesson02_introduction_to_streamlit.html",      "2. Introduction to Streamlit"),
    ("lesson03_interactive_filters.html",             "3. Interactive Filters"),
    ("lesson04_exporting_data.html",                  "4. Exporting Data"),
    ("lesson05_deploying_data_applications.html",     "5. Deploying Data Applications"),
    ("lesson06_shiny_for_python.html",                "6. Shiny for Python"),
    ("lesson07_streamlit_vs_shiny.html",              "7. Streamlit vs Shiny"),
]

# ═══════════════════════════════════════════════════════════
# BUILDER
# ═══════════════════════════════════════════════════════════

def e(text):
    """HTML-escape helper — pass-through for pre-escaped content."""
    return text

def indent(html, n=0):
    pad = "  " * n
    return "\n".join(pad + line for line in html.strip().split("\n"))

# ── CSS ────────────────────────────────────────────────────
CSS = r"""<style>
/* ── CSS Variables — font tokens (:root) ──────────────────── */
:root { --font-body: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif; --font-mono: 'Fira Code', monospace; }

/* ── Global reset — smooth scroll ─────────────────────────── */
* { scroll-behavior: smooth; }

/* ── Prism.js — syntax highlighted code blocks ────────────── */
pre[class*="language-"] { border-radius: 0.75rem; font-family: var(--font-mono); font-size: 0.875rem; margin: 0; padding: 1.25rem 1.5rem; }
code[class*="language-"], pre[class*="language-"] { background: #1e1e2e; }

/* ── Heading resets — strip Confluence default margins ────── */
h1, h2, h3, h4, h5, h6 { margin-top: 0; margin-bottom: 0; padding: 0; line-height: 1.3; }

/* ── Brand utility classes ────────────────────────────────── */
.text-brand { color: #CB187D; }
.bg-brand   { background: #CB187D; }
.bg-brand-soft { background: #fdf0f7; }
.brand-soft-panel { background: #fdf0f7; border-color: #f5c6e0; }
.bg-amber-tip { background: #fff7ed; border-color: #fed7aa; }
.bg-code { background: #1e1e2e; }
.border-code-sep { border-color: rgba(255,255,255,0.08); }
.pre-reset { margin: 0; border-radius: 0; background: transparent; }

/* ── Key Concepts sidebar tabs (.kc-tab / .kc-tab-active) ── */
.kc-tab-active { background: #fdf0f7; }
.kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }
.kc-panel-anim { animation: kcFadeIn 0.25s ease-out; }
@keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

/* ── Code Examples pill tabs (.ce-step / .ce-step-active) ── */
.ce-step:not(.ce-step-active):hover { background: #374151; color: #d1d5db; }
.ce-panel-anim { animation: kcFadeIn 0.25s ease-out; }

/* ── Common Mistakes pill tabs (.mk-step / .mk-step-active) */
.mk-step:not(.mk-step-active):hover { background: #374151; color: #d1d5db; }
.mk-panel-anim { animation: kcFadeIn 0.25s ease-out; }

/* ── Knowledge Check quiz tabs (.qz-step / .qz-step-active) */
.qz-step:not(.qz-step-active):hover { background: #374151; color: #d1d5db; }
.qz-panel-anim { animation: kcFadeIn 0.25s ease-out; }

/* ── Practice Exercise tabs (.pe-step / .pe-step-active) ── */
.pe-step:not(.pe-step-active):hover { background: #374151; color: #d1d5db; }
.pe-panel-anim { animation: kcFadeIn 0.25s ease-out; }
.task-box { background: #fdf0f7; border: 1px solid #f5c6e0; }

/* ── Accordion — used in Overview & Key Ideas sections ──── */
.accordion-body { display: none !important; }
.accordion-body.open { display: block !important; }
.accordion-toggle { display:flex !important; align-items:center !important; gap:8px !important; width:100% !important; padding:10px 16px !important; border-radius:10px !important; font-size:0.8rem !important; font-weight:600 !important; cursor:pointer !important; border:2px dashed #f5c6e0 !important; background:#fdf0f7 !important; color:#7F004C !important; line-height:1.2 !important; text-decoration:none !important; transition:background 0.15s, border-color 0.15s !important; }
.accordion-toggle:hover { background:#f9d9ee !important; border-color:#CB187D !important; }
.accordion-toggle.open { background:#fdf0f7 !important; border-color:#CB187D !important; border-style:solid !important; }
.accordion-chevron { margin-left:auto !important; transition:transform 0.2s !important; }
.accordion-toggle.open .accordion-chevron { transform:rotate(180deg) !important; }

/* ── Hero banner — full-width gradient header ─────────────── */
.hero-container { position:relative; border-radius:1.25rem; overflow:hidden; min-height:380px; background:linear-gradient(135deg,#CB187D 0%,#CB187D 40%,#a31268 65%,#7F004C 100%); }
.hero-dots { position:absolute; inset:0; opacity:0.06; background-image:radial-gradient(circle,rgba(255,255,255,0.7) 1px,transparent 1px); background-size:24px 24px; }
.hero-glow { position:absolute; border-radius:50%; pointer-events:none; filter:blur(70px); }
.hero-pill { pointer-events:none; cursor:default; background:#ffffff; border:none; color:#7F004C; font-weight:700; }

/* ── Scroll progress bar — fixed top-of-page indicator ───── */
.scroll-progress { position:fixed; top:0; left:0; height:3px; background:linear-gradient(90deg,#CB187D,#6366f1,#CB187D); background-size:200% 100%; animation:scrollGradient 3s linear infinite; z-index:9999; transition:width 0.15s; }
@keyframes scrollGradient { 0%{background-position:0% 0%} 100%{background-position:200% 0%} }

/* ── Page layout — two-column: TOC sidebar + main content ── */
.lesson-layout { display:flex; gap:1.75rem; align-items:flex-start; }
.lesson-toc-sidebar { width:240px; flex-shrink:0; position:sticky; top:1.5rem; max-height:calc(100vh - 2rem); overflow-y:auto; transition:width 0.25s ease, opacity 0.25s ease; }
.lesson-toc-sidebar.toc-collapsed { width:44px; overflow:hidden; }
.lesson-toc-sidebar.toc-collapsed .toc-body { display:none; }
.lesson-toc-sidebar.toc-collapsed .toc-header-label { display:none; }
.lesson-toc-sidebar.toc-collapsed .toc-module-list { display:none; }
.toc-toggle-btn { background:none; border:none; cursor:pointer; padding:2px; color:#CB187D; display:flex; align-items:center; justify-content:center; position:absolute; right:8px; top:50%; transform:translateY(-50%); border-radius:6px; transition:background 0.15s; }
.toc-toggle-btn:hover { background:#fdf0f7; }
.toc-link { transition: color 0.15s, padding-left 0.15s; }
.toc-link:hover { color:#CB187D; padding-left:4px; }
.toc-link.active { color:#CB187D; font-weight:600; border-left:3px solid #CB187D; padding-left:8px; }

/* ── Objective cards (.obj-card) ──────────────────────────── */
.obj-card { transition: box-shadow 0.22s cubic-bezier(.4,0,.2,1), border-color 0.22s ease, background-color 0.22s ease; }
.obj-card:hover { box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); border-color: #f5c6e0; background-color: #ffffff; }
.obj-card .obj-icon { transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease; }
.obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
.obj-card:hover .obj-icon .iconify { color: white !important; }
#key-ideas .obj-card:hover { border-color: #f3f4f6; background-color: #ffffff; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); }
#key-ideas .obj-card:hover .obj-icon { transform: scale(1.1); background-color: revert; }

/* ── Generic outline tab buttons (.tab-btn / .tab-panel) ── */
.tab-btn { display:inline-flex; align-items:center; gap:6px; padding:7px 18px; font-size:0.82rem; font-weight:600; cursor:pointer; border:1.5px solid #e5e7eb; border-radius:999px; color:#6b7280; background:#fff; line-height:1.2; transition:color 0.15s, background 0.15s, border-color 0.15s; }
.tab-btn:hover { color:#CB187D; border-color:#CB187D; background:#fdf0f7; }
.tab-btn.active { color:#fff; background:#CB187D; border-color:#CB187D; }
.tab-panel { display:none; } .tab-panel.active { display:block; }

/* ── Code block copy button (.copy-btn) ───────────────────── */
.copy-btn { position:absolute; top:10px; right:12px; display:inline-flex; align-items:center; background:rgba(203,24,125,0.15); border:1px solid rgba(203,24,125,0.3); color:#CB187D; border-radius:6px; padding:3px 8px; font-size:0.65rem; font-weight:600; cursor:pointer; transition:background 0.2s; white-space:nowrap; }
.copy-btn:hover { background:rgba(203,24,125,0.3); }
.copy-btn-light { position:static; color:#fff; border-color:rgba(255,255,255,0.25); background:rgba(255,255,255,0.1); }
.copy-btn-light:hover { background:rgba(255,255,255,0.2); }

/* ── Bottom lesson navigation — Previous / All Lessons / Next */
.lesson-nav-link:hover p, .lesson-nav-link:hover span, .lesson-nav-link:hover svg { color:#CB187D; transition:color 0.15s; }

/* ── Back-to-top floating button ──────────────────────────── */
.back-to-top { position:fixed; bottom:2rem; right:2rem; width:44px; height:44px; border-radius:50%; background:#CB187D; color:white; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(203,24,125,0.3); cursor:pointer; opacity:0; transform:translateY(10px); transition:opacity 0.3s, transform 0.3s; z-index:50; border:none; }
.back-to-top.visible { opacity:1; transform:translateY(0); }
.back-to-top:hover { background:#7F004C; }

/* ── Quiz answer feedback buttons (.quiz-btn.correct / .incorrect) */
.quiz-btn.correct { background:#f0fdf4; border-color:#22c55e; color:#16a34a; }
.quiz-btn.incorrect { background:#fef2f2; border-color:#ef4444; color:#dc2626; }

/* ── Card hover animations — Mistake, Flow, Recap, Overview cards */
.mistake-card { transition: transform 0.18s ease, box-shadow 0.18s ease; }
.mistake-card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px -5px rgba(0,0,0,0.08); }

/* ── Responsive — mobile breakpoint (<768px) ──────────────── */
@media (max-width: 767px) { .lesson-toc-sidebar { display:none; } .lesson-layout { display:block; } .hero-container { min-height:auto; } .hero-split { flex-direction:column !important; } }

/* ── Print styles — hide interactive chrome when printing ─── */
@media print { .lesson-toc-sidebar, .back-to-top, .scroll-progress, .copy-btn, .hero-container { display:none; } .obj-card:hover { transform:none; box-shadow:none; } }

/* ── Iconify icon alignment utility ───────────────────────── */
.iconify { vertical-align: middle; flex-shrink: 0; }

/* ═══ Confluence Hub-Root Isolation Block ═══════════════════ */
#hub-root a.hero-pill { color: #CB187D !important; }
#hub-root .hero-pill .opacity-55 { opacity: 1 !important; }
#hub-root .hero-pill .opacity-50 { opacity: 1 !important; }
#hub-root .toc-link:hover { color: #CB187D !important; }
#hub-root .toc-link.active { color: #CB187D !important; font-weight: 600 !important; border-left: 3px solid #CB187D !important; padding-left: 8px !important; background-color: #fdf0f7 !important; }
#hub-root .mod-lesson-active { background-color: #fdf0f7 !important; border-color: #CB187D !important; color: #CB187D !important; }
#hub-root .mod-lesson-active .lesson-dot { background-color: #CB187D !important; }
#hub-root .ce-step, #hub-root .mk-step, #hub-root .qz-step, #hub-root .pe-step { display:inline-flex !important; align-items:center !important; gap:0.5rem !important; padding:0.375rem 1rem !important; border-radius:9999px !important; font-size:0.75rem !important; font-weight:700 !important; line-height:1.2 !important; white-space:nowrap !important; border:none !important; cursor:pointer !important; }
#hub-root .ce-step:not(.ce-step-active), #hub-root .mk-step:not(.mk-step-active), #hub-root .qz-step:not(.qz-step-active), #hub-root .pe-step:not(.pe-step-active) { background-color:#1f2937 !important; color:#ffffff !important; box-shadow:none !important; }
#hub-root .ce-step-active, #hub-root .mk-step-active, #hub-root .qz-step-active, #hub-root .pe-step-active { background:linear-gradient(to right,#CB187D,#e84aad) !important; color:#ffffff !important; box-shadow:0 10px 25px -5px rgba(203,24,125,0.3) !important; }
#hub-root .obj-card:hover { border-color: #f5c6e0 !important; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important; background-color: #ffffff !important; }
#hub-root .obj-card:hover .obj-icon { background: #CB187D !important; }
#hub-root .obj-card:hover .obj-icon .iconify { color: #ffffff !important; }
/* ── Key Takeaway cards — keep border gray and icon gradient on hover ── */
#hub-root #key-ideas .obj-card:hover { border-color: #f3f4f6 !important; background-color: #ffffff !important; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important; }
#hub-root #key-ideas .obj-card:hover .obj-icon { background: revert !important; }
#hub-root .section-header { display:flex !important; align-items:center !important; gap:1rem !important; padding:1.25rem 2rem 1.25rem 1rem !important; background:#ffffff !important; border-bottom:1px solid #f3f4f6 !important; border-left:4px solid #CB187D !important; }
#hub-root .section-icon { display:inline-flex !important; align-items:center !important; justify-content:center !important; width:2.75rem !important; height:2.75rem !important; border-radius:0.75rem !important; background:#CB187D !important; flex-shrink:0 !important; }
#hub-root .section-title { font-size:1.25rem !important; font-weight:700 !important; color:#111827 !important; }
#hub-root .section-subtitle { font-size:0.875rem !important; color:#9ca3af !important; }
#hub-root .lesson-nav-link:hover p, #hub-root .lesson-nav-link:hover span, #hub-root .lesson-nav-link:hover svg { color: #CB187D !important; transition: color 0.15s !important; }
</style>"""

# ── HERO SVG ──────────────────────────────────────────────
HERO_SVG = """<svg viewBox="0 0 280 324" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" style="max-height:320px;" aria-hidden="true">
  <defs>
    <linearGradient id="hexFill" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a0a12"/><stop offset="45%" stop-color="#2d0a1e"/><stop offset="100%" stop-color="#0d0610"/></linearGradient>
    <linearGradient id="hexBorder" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#CB187D"/><stop offset="50%" stop-color="#e84aad"/><stop offset="100%" stop-color="#CB187D"/></linearGradient>
    <radialGradient id="hexGlow" cx="50%" cy="38%" r="45%"><stop offset="0%" stop-color="#CB187D" stop-opacity="0.18"/><stop offset="100%" stop-color="#CB187D" stop-opacity="0"/></radialGradient>
    <radialGradient id="pyGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFD43B" stop-opacity="0.12"/><stop offset="100%" stop-color="#FFD43B" stop-opacity="0"/></radialGradient>
    <clipPath id="hexClip"><polygon points="140,14 268,88 268,236 140,310 12,236 12,88"/></clipPath>
  </defs>
  <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexFill)"/>
  <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexGlow)"/>
  <g clip-path="url(#hexClip)" opacity="1">
    <g opacity="0.06"><circle cx="40" cy="100" r="1.2" fill="white"/><circle cx="60" cy="100" r="1.2" fill="white"/><circle cx="80" cy="100" r="1.2" fill="white"/><circle cx="100" cy="100" r="1.2" fill="white"/><circle cx="120" cy="100" r="1.2" fill="white"/><circle cx="160" cy="100" r="1.2" fill="white"/><circle cx="180" cy="100" r="1.2" fill="white"/><circle cx="200" cy="100" r="1.2" fill="white"/><circle cx="220" cy="100" r="1.2" fill="white"/><circle cx="240" cy="100" r="1.2" fill="white"/></g>
    <g opacity="0.08" fill="white" font-family="'Fira Code',monospace" font-size="7"><text x="42" y="145">&gt;&gt;&gt; import pandas</text><text x="185" y="92">def main():</text><text x="38" y="92">class Data:</text></g>
    <g opacity="0.15" stroke="#FFD43B" stroke-width="1.5" fill="none" stroke-linecap="round"><polyline points="52,72 42,72 42,85"/><polyline points="228,72 238,72 238,85"/><polyline points="52,252 42,252 42,239"/><polyline points="228,252 238,252 238,239"/></g>
    <circle cx="140" cy="145" r="55" fill="url(#pyGlow)"/>
  </g>
  <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="none" stroke="url(#hexBorder)" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="95" y="85" width="90" height="90"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;width:100%;height:100%;"><span class="iconify" data-icon="logos:python" style="font-size:70px;filter:drop-shadow(0 0 14px rgba(255,212,59,0.25));"></span></div></foreignObject>
  <text x="140" y="205" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="800" font-size="30" letter-spacing="4" opacity="0.95">PYTHON</text>
  <text x="140" y="230" text-anchor="middle" fill="#f5c6e0" font-family="Inter,sans-serif" font-weight="600" font-size="14" letter-spacing="5" opacity="0.8">LEARNING HUB</text>
  <line x1="85" y1="185" x2="195" y2="185" stroke="#CB187D" stroke-width="1" stroke-opacity="0.35" stroke-linecap="round"/>
</svg>"""

# ═══════════════════════════════════════════════════════════
# HTML generation helpers
# ═══════════════════════════════════════════════════════════

def section_header(icon, title, subtitle):
    return f"""<div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
  <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
    <span class="iconify text-white text-base" data-icon="{icon}"></span>
  </span>
  <div class="min-w-0">
    <h2 class="text-xl font-bold text-gray-900 leading-tight">{title}</h2>
    <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">{subtitle}</p>
  </div>
</div>"""

def amber_tip(text):
    return f"""<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">{text}</p>
</div>"""

def style_a_code(filename, code, terminal_cmd=None, terminal_out=None):
    """Style A dark-chrome code block with optional terminal pane."""
    lang = "bash" if filename.endswith(".sh") else "python"
    if filename.endswith(".yml") or filename.endswith(".yaml"):
        lang = "python"  # Prism fallback — YAML close enough for highlighting
    icon = "fa6-solid:terminal" if lang == "bash" else "logos:python"
    terminal_html = ""
    if terminal_cmd and terminal_out:
        terminal_html = f"""
  <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
    <div class="flex items-center gap-2 mb-1.5">
      <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
      <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
      <span class="text-[10px] text-gray-600 font-mono">$ {terminal_cmd}</span>
    </div>
    <div class="font-mono text-xs text-emerald-400 leading-relaxed">{terminal_out}</div>
  </div>"""
    return f"""<div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
        <span class="iconify text-yellow-400 text-xs" data-icon="{icon}" data-width="12" data-height="12"></span>
        <span class="text-[11px] font-semibold text-gray-400">{filename}</span>
      </div>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <div class="bg-code">
    <pre class="overflow-x-auto pre-reset"><code class="language-{lang}">{htmlmod.escape(code)}</code></pre>
  </div>{terminal_html}
</div>"""

def style_b_code(label, code, lang="python"):
    """Style B simple-dark code block — for #key-concepts."""
    icon = "fa6-solid:terminal" if lang == "bash" else "logos:python"
    display = "Bash" if lang == "bash" else "Python"
    return f"""<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="{icon}" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">{display}</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-{lang}">{htmlmod.escape(code)}</code></pre>
</div>"""

# ═══════════════════════════════════════════════════════════
# BUILD SECTIONS
# ═══════════════════════════════════════════════════════════

# ── TOC links (12 canonical sections, no decision-flow) ───
toc_sections = [
    ("objective",       "fa6-solid:bullseye",          "Lesson Objective"),
    ("overview",        "fa6-solid:binoculars",        "Overview"),
    ("key-ideas",       "fa6-solid:lightbulb",         "Key Takeaways"),
    ("key-concepts",    "fa6-solid:book-open",         "Key Concepts"),
    ("code-examples",   "fa6-solid:code",              "Code Examples"),
    ("comparison",      "fa6-solid:scale-balanced",    "SQL / Excel Comparison"),
    ("practice",        "fa6-solid:pencil",            "Practice Exercises"),
    ("mistakes",        "fa6-solid:triangle-exclamation","Common Mistakes"),
    ("real-world",      "fa6-solid:briefcase",         "Real-World Use"),
    ("recap",           "fa6-solid:list-check",        "Lesson Recap"),
    ("knowledge-check", "fa6-solid:brain",             "Knowledge Check"),
    ("next-lesson",     "fa6-solid:circle-arrow-right","Next Lesson"),
]

def build_toc_links():
    lines = []
    for sid, icon, label in toc_sections:
        lines.append(f'<a href="#{sid}" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="{icon}"></span> {label}</a>')
    return "\n".join(lines)

def build_sidebar_lessons():
    lines = []
    for href, label in sidebar_lessons:
        is_active = (f"lesson{LESSON_NUM:02d}_" in href)
        if is_active:
            lines.append(f'<a href="{href}" class="mod-lesson-active flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors"><span class="lesson-dot w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span><span class="truncate">{label}</span></a>')
        else:
            lines.append(f'<a href="{href}" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors"><span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span><span class="truncate">{label}</span></a>')
    return "\n".join(lines)

# ── Objective section ─────────────────────────────────────
def build_objective():
    cards = []
    for icon, title, desc in objectives:
        cards.append(f"""<div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
  <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
    <span class="iconify text-brand text-lg" data-icon="{icon}"></span>
  </span>
  <div>
    <p class="text-sm font-semibold text-gray-800">{title}</p>
    <p class="text-xs text-gray-500 mt-0.5">{desc}</p>
  </div>
</div>""")
    n = len(objectives)
    return f"""<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:bullseye", "Lesson Objective", "The goal and expected outcome of this lesson")}
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {"".join(cards)}
      </div>
      <div class="mt-5">
        {amber_tip(f'This lesson covers <strong>{n} key concepts</strong> for deploying data applications &mdash; hosting, requirements files, deployment environments, CI/CD pipelines, and secrets management.')}
      </div>
    </div>
  </div>
</section>"""

# ── Overview section ──────────────────────────────────────
def build_overview():
    cards = []
    for icon, title, subtitle, desc in overview_cards:
        cards.append(f"""<div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
  <div class="flex items-center gap-3 mb-2.5">
    <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
      <span class="iconify text-brand text-base" data-icon="{icon}"></span>
    </span>
    <div>
      <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>
      <p class="text-[10px] text-gray-400 italic leading-tight">{subtitle}</p>
    </div>
  </div>
  <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>
</div>""")
    return f"""<section id="overview">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:binoculars", "Overview", "A high-level introduction to deploying data applications")}
    <div class="bg-white px-8 py-7 space-y-5">
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-start gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">{HOOK_QUOTE}</p>
        </div>
      </div>
      <p class="text-sm text-gray-600 leading-relaxed">{ANALOGY_INTRO}</p>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {"".join(cards)}
      </div>
      {amber_tip(OVERVIEW_TIP)}
    </div>
  </div>
</section>"""

# ── Key Takeaways ─────────────────────────────────────────
KT_COLORS = {
    "pink":    {"border": "border-pink-100",   "bar": "from-[#CB187D] to-[#e84aad]", "icon": "from-[#CB187D] to-[#e84aad]", "pill_bg": "bg-pink-50",    "pill_text": "text-[#CB187D]",   "pill_border": "border-pink-100"},
    "violet":  {"border": "border-violet-100", "bar": "from-violet-500 to-purple-400","icon": "from-violet-500 to-purple-600","pill_bg": "bg-violet-50",  "pill_text": "text-violet-600",  "pill_border": "border-violet-100"},
    "blue":    {"border": "border-blue-100",   "bar": "from-blue-500 to-indigo-400",  "icon": "from-blue-500 to-indigo-600",  "pill_bg": "bg-blue-50",    "pill_text": "text-blue-600",    "pill_border": "border-blue-100"},
    "emerald": {"border": "border-emerald-100","bar": "from-emerald-500 to-teal-400", "icon": "from-emerald-500 to-teal-600", "pill_bg": "bg-emerald-50", "pill_text": "text-emerald-600", "pill_border": "border-emerald-100"},
    "amber":   {"border": "border-amber-100",  "bar": "from-amber-500 to-orange-400", "icon": "from-amber-500 to-orange-600", "pill_bg": "bg-amber-50",   "pill_text": "text-amber-600",   "pill_border": "border-amber-100"},
}

def build_key_ideas():
    cards = []
    for color, icon, heading, explanation, keywords in takeaways:
        c = KT_COLORS[color]
        pills = "".join(f'<span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold {c["pill_bg"]} {c["pill_text"]} border {c["pill_border"]}">{kw}</span>' for kw in keywords)
        cards.append(f"""<div class="obj-card rounded-2xl border {c["border"]} bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r {c["bar"]}"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br {c["icon"]} shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="{icon}"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">{heading}</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">{explanation}</p>
    <div class="flex flex-wrap gap-2">{pills}</div>
  </div>
</div>""")
    return f"""<section id="key-ideas">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:lightbulb", "Key Takeaways", "The most important ideas to remember")}
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {"".join(cards)}
      </div>
    </div>
  </div>
</section>"""

# ── Key Concepts (KC tabs) ────────────────────────────────
KC_COLORS_MAP = [
    {"name":"pink",    "border":"pink-100",   "bar":"from-[#CB187D] via-pink-400 to-rose-300",        "bg":"from-pink-50/60",    "icon":"from-[#CB187D] to-[#e84aad]", "badge_from":"from-pink-100","badge_to":"to-rose-100","badge_text":"text-[#CB187D]","table_bg":"bg-pink-50","table_text":"text-[#CB187D]","code_bg":"bg-pink-50","code_text":"text-pink-700"},
    {"name":"violet",  "border":"violet-100", "bar":"from-violet-500 via-purple-400 to-fuchsia-300",  "bg":"from-violet-50/60",  "icon":"from-violet-500 to-purple-600","badge_from":"from-violet-100","badge_to":"to-purple-100","badge_text":"text-violet-600","table_bg":"bg-violet-50","table_text":"text-violet-600","code_bg":"bg-violet-50","code_text":"text-violet-700"},
    {"name":"blue",    "border":"blue-100",   "bar":"from-blue-500 via-cyan-400 to-teal-300",          "bg":"from-blue-50/60",    "icon":"from-blue-500 to-indigo-600",  "badge_from":"from-blue-100","badge_to":"to-indigo-100","badge_text":"text-blue-600","table_bg":"bg-blue-50","table_text":"text-blue-600","code_bg":"bg-blue-50","code_text":"text-blue-700"},
    {"name":"emerald", "border":"emerald-100","bar":"from-emerald-500 via-teal-400 to-cyan-300",       "bg":"from-emerald-50/60", "icon":"from-emerald-500 to-teal-600", "badge_from":"from-emerald-100","badge_to":"to-teal-100","badge_text":"text-emerald-600","table_bg":"bg-emerald-50","table_text":"text-emerald-600","code_bg":"bg-emerald-50","code_text":"text-emerald-700"},
    {"name":"orange",  "border":"orange-100", "bar":"from-orange-500 via-amber-400 to-yellow-300",     "bg":"from-orange-50/60",  "icon":"from-orange-500 to-red-600",   "badge_from":"from-orange-100","badge_to":"to-amber-100","badge_text":"text-orange-600","table_bg":"bg-orange-50","table_text":"text-orange-600","code_bg":"bg-orange-50","code_text":"text-orange-700"},
]

def build_key_concepts():
    tabs_html = []
    panels_html = []
    for i, kc in enumerate(kc_tabs):
        c = KC_COLORS_MAP[i]
        active_cls = " kc-tab-active" if i == 0 else ""
        hidden_cls = "" if i == 0 else " hidden"
        # Tab button
        tabs_html.append(f"""<button onclick="switchKcTab({i})" class="kc-tab{active_cls} group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 {'bg-[#CB187D] text-white shadow-sm shadow-pink-200' if i==0 else 'bg-gray-100 text-gray-400'}"><span class="iconify text-[11px]" data-icon="{kc['icon']}"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight {'text-gray-900' if i==0 else 'text-gray-400'}">{kc['label']}</span>
</button>""")
        # Panel
        params_html = ""
        if kc.get("params"):
            rows = "".join(f'<tr class="border-t border-gray-100"><td class="py-2 pr-3 align-top"><code class="text-xs font-mono font-semibold px-1.5 py-0.5 rounded {c["code_bg"]} {c["code_text"]}">{p[0]}</code></td><td class="py-2 pr-3 align-top text-[11px] text-gray-400 font-mono">{p[1]}</td><td class="py-2 align-top text-xs text-gray-600">{p[2]}</td></tr>' for p in kc["params"])
            params_html = f"""<table class="w-full text-left mt-3"><thead><tr class="{c['table_bg']}"><th class="py-1.5 px-2 text-[11px] font-bold uppercase tracking-wider {c['table_text']} rounded-tl-lg">Parameter</th><th class="py-1.5 px-2 text-[11px] font-bold uppercase tracking-wider {c['table_text']}">Type</th><th class="py-1.5 px-2 text-[11px] font-bold uppercase tracking-wider {c['table_text']} rounded-tr-lg">Description</th></tr></thead><tbody>{rows}</tbody></table>"""
        tip_html = amber_tip(kc["tip"]) if kc.get("tip") else ""
        panels_html.append(f"""<div class="kc-panel kc-panel-anim{hidden_cls}" data-color="{c['name']}" role="tabpanel">
  <div class="rounded-2xl border border-{c['border']} overflow-hidden">
    <div class="h-1 bg-gradient-to-r {c['bar']}"></div>
    <div class="bg-gradient-to-br {c['bg']} to-white p-5 space-y-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br {c['icon']} shrink-0 shadow-md">
            <span class="iconify text-white text-sm" data-icon="{kc['icon']}"></span>
          </span>
          <div>
            <h3 class="text-sm font-bold text-gray-900 leading-tight">{kc['label']}</h3>
            <p class="text-[10px] text-gray-400 mt-0.5">Concept {i+1} of {len(kc_tabs)}</p>
          </div>
        </div>
        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r {c['badge_from']} {c['badge_to']} {c['badge_text']}">{kc['badge']}</span>
      </div>
      <p class="text-sm text-gray-600 leading-relaxed">{kc['intro']}</p>
      {style_b_code(kc['label'], kc['code'])}
      {params_html}
      {tip_html}
    </div>
  </div>
</div>""")
    return f"""<section id="key-concepts">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:book-open", "Key Concepts", "Core terms and definitions for this topic")}
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full bg-[#CB187D] transition-all duration-300" style="height:68px;"></div>
          {"".join(tabs_html)}
        </div>
        <div class="flex-1 min-w-0 md:pl-5">
          {"".join(panels_html)}
        </div>
      </div>
    </div>
  </div>
</section>"""

# ── Code Examples ─────────────────────────────────────────
def build_code_examples():
    n = len(code_examples)
    tab_buttons = []
    panels = []
    for i, ce in enumerate(code_examples):
        active = "ce-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchCeTab({i})" class="ce-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">{ce["title"]}</span></button>')
        hidden = "" if i == 0 else " hidden"
        fname = ce["title"].lower().replace(" ", "_").replace("'","").replace("/","_") + ".py"
        term_out = ce.get("terminal_out","").replace("\n", "<br>")
        panels.append(f"""<div class="ce-panel ce-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{i+1:02d}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Example {i+1} &mdash; {ce["title"]}</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <p class="text-sm text-gray-600 leading-relaxed">{ce["desc"]}</p>
      {style_a_code(fname, ce["code"], ce.get("terminal_cmd"), ce.get("terminal_out"))}
      {amber_tip(ce["tip"])}
    </div>
  </div>
</div>""")
    return f"""<section id="code-examples">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:code", "Code Examples", "Hands-on code snippets to explore the concepts")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Comparison ────────────────────────────────────────────
def build_comparison():
    rows_html = []
    for i, (icon, label, py_code, py_desc, sql_code, sql_desc, xl_code, xl_desc) in enumerate(comparison_rows):
        if i > 0:
            rows_html.append("""<div class="flex items-center gap-3 mb-4">
  <span class="flex-1 h-px bg-gray-100"></span>
  <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
    <span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span>
  </span>
  <span class="flex-1 h-px bg-gray-100"></span>
</div>""")
        rows_html.append(f"""<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
    <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
      <span class="iconify text-indigo-400 text-[11px]" data-icon="{icon}"></span>
    </span>
    <span class="text-xs font-bold uppercase tracking-widest text-gray-400">{label}</span>
  </div>
  <div class="grid grid-cols-3 divide-x divide-gray-100">
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Python</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">{py_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{py_desc}</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">SQL</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">{sql_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{sql_desc}</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Excel</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">{xl_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{xl_desc}</p>
    </div>
  </div>
</div>""")
    return f"""<section id="comparison">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:scale-balanced", "SQL / Excel Comparison", "How deployment compares across Python, SQL, and Excel")}
    <div class="bg-white px-8 py-7 space-y-5">
      {"".join(rows_html)}
    </div>
  </div>
</section>"""

# ── Practice ──────────────────────────────────────────────
def build_practice():
    n = len(practice_exercises)
    tab_buttons = []
    panels = []
    for i, pe in enumerate(practice_exercises):
        active = "pe-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchPeTab({i})" class="pe-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">{pe["title"]}</span></button>')
        hidden = "" if i == 0 else " hidden"
        task_items = "".join(f'<li class="text-sm text-gray-600">{t}</li>' for t in pe["tasks"])
        fname = f"solution_{i+1}.py"
        panels.append(f"""<div class="pe-panel pe-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{i+1:02d}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Exercise {i+1} &mdash; {pe["title"]}</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
          <ol class="list-decimal list-inside space-y-1">{task_items}</ol>
        </div>
      </div>
      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Solution
        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        {style_a_code(fname, pe["solution"])}
        <div class="mt-3">{amber_tip(pe["why"])}</div>
      </div>
    </div>
  </div>
</div>""")
    return f"""<section id="practice">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:pencil", "Practice Exercises", "Guided exercises to reinforce your learning")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Mistakes ──────────────────────────────────────────────
def build_mistakes():
    n = len(mistakes)
    tab_buttons = []
    panels = []
    for i, mk in enumerate(mistakes):
        active = "mk-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchMkTab({i})" class="mk-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">{mk["title"]}</span></button>')
        hidden = "" if i == 0 else " hidden"
        panels.append(f"""<div class="mk-panel mk-panel-anim{hidden}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["why_happens"]}</p>
      </div>
    </div>
    <div class="px-6 py-5 space-y-3">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div>
          <p class="text-xs font-bold text-red-500 mb-2 flex items-center gap-1"><span class="iconify" data-icon="fa6-solid:xmark"></span> Wrong</p>
          <div class="rounded-xl overflow-hidden bg-code">
            <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{htmlmod.escape(mk["wrong"])}</code></pre>
          </div>
        </div>
        <div>
          <p class="text-xs font-bold text-emerald-500 mb-2 flex items-center gap-1"><span class="iconify" data-icon="fa6-solid:check"></span> Correct</p>
          <div class="rounded-xl overflow-hidden bg-code">
            <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{htmlmod.escape(mk["correct"])}</code></pre>
          </div>
        </div>
      </div>
    </div>
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["fix"]}</p>
    </div>
  </div>
</div>""")
    return f"""<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:triangle-exclamation", "Common Mistakes", "Frequent errors and how to avoid them")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Real-World ────────────────────────────────────────────
def build_real_world():
    cards = []
    for icon, title, desc in real_world:
        cards.append(f"""<div class="group flex items-start gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
  <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]">
    <span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="{icon}"></span>
  </div>
  <div>
    <p class="text-sm font-semibold text-gray-700">{title}</p>
    <p class="text-xs text-gray-500 mt-0.5 leading-relaxed">{desc}</p>
  </div>
</div>""")
    return f"""<section id="real-world">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:briefcase", "Real-World Use", "Practical applications in real-world workflows")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="rounded-xl p-5 flex items-start gap-4 border border-[#f5c6e0] bg-[#fdf0f7]">
        <span class="iconify mt-0.5 shrink-0 text-xl text-[#CB187D]" data-icon="fa6-solid:earth-americas"></span>
        <p class="text-sm text-gray-700 leading-relaxed">Deployment is the bridge between building a dashboard on your laptop and sharing it with the world &mdash; every data app that reaches an audience beyond one person goes through some form of deployment.</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {"".join(cards)}
      </div>
    </div>
  </div>
</section>"""

# ── Recap ─────────────────────────────────────────────────
recap_items = [
    ("fa6-solid:cloud-arrow-up", "Application Hosting",  "You learned that deploying means placing your app on an always-on server so anyone with the URL can use it without installing Python."),
    ("fa6-solid:file-lines",     "Requirements File",    "You learned that requirements.txt lists every package your app needs and that the server runs pip install from this file during deployment."),
    ("fa6-solid:server",         "Deployment Options",   "You learned the trade-offs between Streamlit Community Cloud, Docker containers, and internal company servers."),
    ("fa6-solid:arrows-spin",    "CI/CD Pipelines",      "You learned that CI/CD automates testing and deployment so broken code never reaches production."),
    ("fa6-solid:lock",           "Secrets Management",   "You learned to store API keys and passwords in environment variables or st.secrets instead of hard-coding them in your source code."),
]

def build_recap():
    cards = []
    for i, (icon, title, desc) in enumerate(recap_items):
        cards.append(f"""<div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{i+1:02d}</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="{icon}"></span>
      </span>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">{title}</p>
        <p class="text-[11px] text-gray-600 leading-snug">{desc}</p>
      </div>
    </div>
  </div>
</div>""")
    n = len(recap_items)
    return f"""<section id="recap">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:list-check", "Lesson Recap", "A quick summary of what you learned")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {"".join(cards)}
      </div>
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered {n} key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

# ── Knowledge Check ───────────────────────────────────────
def build_knowledge_check():
    n = len(quiz)
    tab_buttons = []
    panels = []
    for i, q in enumerate(quiz):
        active = "qz-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchQzTab({i})" class="qz-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question {i+1}</span></button>')
        hidden = "" if i == 0 else " hidden"
        if q["type"] == "tf":
            answers_html = f"""<div class="flex gap-3">
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, {str(q['answer']).lower()})"><span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True</button>
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, {str(not q['answer']).lower()})"><span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False</button>
          </div>"""
            q_type_label = "True or False"
        else:
            opts = []
            for label, correct in q["options"]:
                hover_cls = "hover:border-[#CB187D] hover:bg-[#fdf0f7]" if correct else "hover:border-gray-300 hover:bg-gray-50"
                opts.append(f'<button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 {hover_cls} transition-colors" onclick="checkQuiz(this, {str(correct).lower()})">{htmlmod.escape(label)}</button>')
            answers_html = f'<div class="grid gap-2">{"".join(opts)}</div>'
            q_type_label = "Multiple Choice"
        panels.append(f"""<div class="qz-panel qz-panel-anim{hidden}" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q{i+1}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{q_type_label}</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q{i}" data-fb-correct="{q['fb_correct']}" data-fb-wrong="{q['fb_wrong']}">
        <p class="text-sm font-semibold text-gray-800 mb-4">{q['stem']}</p>
        {answers_html}
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>""")
    return f"""<section id="knowledge-check">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:brain", "Knowledge Check", "Test your understanding before moving on")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Next Lesson ───────────────────────────────────────────
def build_next_lesson():
    preview_cards = []
    for icon, text in next_preview:
        preview_cards.append(f"""<div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
  <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="{icon}"></span></span>
  <div><p class="text-sm font-semibold text-gray-700">{text}</p></div>
</div>""")
    next_num = LESSON_NUM + 1
    return f"""<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:circle-arrow-right", "Next Lesson", "Preview of what comes next")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">{next_num}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module {MODULE_NUM} &middot; Lesson {next_num}</p>
          <h3 class="text-base font-bold text-gray-800">{NEXT_LESSON[1]}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {"".join(preview_cards)}
        </div>
      </div>
    </div>
  </div>
</section>"""

# ── Bottom Nav ────────────────────────────────────────────
def build_bottom_nav():
    prev_html = f"""<a href="{PREV_LESSON[0]}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{PREV_LESSON[1]}</p>
      </div>
    </a>"""
    next_html = f"""<a href="{NEXT_LESSON[0]}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{NEXT_LESSON[1]}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>"""
    return f"""<section>
  <div class="flex flex-col sm:flex-row gap-3">
    {prev_html}
    <a href="../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>
    {next_html}
  </div>
</section>"""

# ── JavaScript ────────────────────────────────────────────
SCRIPT = r"""<script>
function toggleToc(){const s=document.querySelector('.lesson-toc-sidebar'),i=document.getElementById('toc-toggle-icon'),c=s.classList.toggle('toc-collapsed');i.setAttribute('data-icon',c?'fa6-solid:angles-right':'fa6-solid:angles-left');if(window.Iconify)Iconify.scan();}
const tocLinks=document.querySelectorAll('.toc-link');const sections=[...tocLinks].map(l=>document.getElementById(l.getAttribute('href').replace('#',''))).filter(Boolean);
function updateScrollSpy(){let id='';sections.forEach(s=>{if(window.scrollY>=s.offsetTop-120)id=s.id;});tocLinks.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+id));}
function updateScrollProgress(){const w=document.documentElement.scrollTop||document.body.scrollTop;const h=document.documentElement.scrollHeight-document.documentElement.clientHeight;document.getElementById('scroll-progress').style.width=(h>0?(w/h)*100:0)+'%';}
function updateBackToTop(){document.getElementById('back-to-top').classList.toggle('visible',window.scrollY>400);}
window.addEventListener('scroll',()=>{updateScrollSpy();updateScrollProgress();updateBackToTop();});
function copyCode(btn){const c=btn.closest('.relative')||btn.parentElement.closest('div');const pre=c?c.querySelector('pre'):null;const text=pre?pre.innerText:'';function fb(){const o=btn.innerHTML;btn.innerHTML='<span class="iconify mr-1" data-icon="fa6-solid:check"></span>Copied!';btn.style.background='rgba(34,197,94,0.2)';btn.style.borderColor='rgba(34,197,94,0.5)';btn.style.color='#4ade80';setTimeout(()=>{btn.innerHTML=o;btn.style.background='';btn.style.borderColor='';btn.style.color='';},2000);}function fc(){const t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();try{document.execCommand('copy');}catch(e){}document.body.removeChild(t);fb();}if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(fb).catch(fc);}else{fc();}}
function toggleAccordion(btn){const b=btn.nextElementSibling;const o=b.classList.contains('open');btn.classList.toggle('open',!o);b.classList.toggle('open',!o);if(!o&&window.Prism)Prism.highlightAllUnder(b);}
const kcColors=[{num:'#CB187D',numShadow:'rgba(203,24,125,0.25)',activeBg:'#fdf0f7'},{num:'#7c3aed',numShadow:'rgba(124,58,237,0.25)',activeBg:'#f5f3ff'},{num:'#2563eb',numShadow:'rgba(37,99,235,0.25)',activeBg:'#eff6ff'},{num:'#059669',numShadow:'rgba(5,150,105,0.25)',activeBg:'#ecfdf5'},{num:'#c74905',numShadow:'rgba(199,73,5,0.25)',activeBg:'#ffddb3'}];
function switchKcTab(idx){const c=kcColors[idx%kcColors.length];const tabs=document.querySelectorAll('.kc-tab');const panels=document.querySelectorAll('.kc-panel');const ind=document.querySelector('.kc-indicator');tabs.forEach((t,i)=>{const n=t.querySelector('.kc-tab-num'),l=t.querySelector('.kc-tab-label');if(i===idx){t.classList.add('kc-tab-active');t.style.background=c.activeBg;if(n){n.style.background=c.num;n.style.color='#fff';n.style.boxShadow='0 2px 8px '+c.numShadow;}if(l)l.style.color='#111827';}else{t.classList.remove('kc-tab-active');t.style.background='';if(n){n.style.background='#f3f4f6';n.style.color='#9ca3af';n.style.boxShadow='none';}if(l)l.style.color='#9ca3af';}});if(ind&&tabs[idx]){ind.style.top=tabs[idx].offsetTop+'px';ind.style.height=tabs[idx].offsetHeight+'px';ind.style.background=c.num;}panels.forEach((p,i)=>{if(i===idx){p.classList.remove('hidden');p.classList.remove('kc-panel-anim');void p.offsetWidth;p.classList.add('kc-panel-anim');}else{p.classList.add('hidden');}});const v=panels[idx];if(v&&window.Prism)Prism.highlightAllUnder(v);}
function _switchDarkPills(pfx,idx){document.querySelectorAll('.'+pfx+'-step').forEach((s,i)=>{if(i===idx){s.classList.add(pfx+'-step-active');s.style.background='linear-gradient(to right,#CB187D,#e84aad)';s.style.color='#fff';s.style.boxShadow='0 10px 25px -5px rgba(203,24,125,0.3)';}else{s.classList.remove(pfx+'-step-active');s.style.background='#1f2937';s.style.color='#9ca3af';s.style.boxShadow='none';}});document.querySelectorAll('.'+pfx+'-panel').forEach((p,i)=>{if(i===idx){p.classList.remove('hidden');p.classList.remove(pfx+'-panel-anim');void p.offsetWidth;p.classList.add(pfx+'-panel-anim');}else{p.classList.add('hidden');}});const v=document.querySelectorAll('.'+pfx+'-panel:not(.hidden)')[0];if(v&&window.Prism)Prism.highlightAllUnder(v);}
function switchCeTab(i){_switchDarkPills('ce',i);}
function switchMkTab(i){_switchDarkPills('mk',i);}
function switchPeTab(i){_switchDarkPills('pe',i);}
function switchQzTab(i){_switchDarkPills('qz',i);}
function checkQuiz(btn,answer){const q=btn.closest('.quiz-question');const fb=q.querySelector('.quiz-feedback');const btns=q.querySelectorAll('.quiz-btn');const fbC=q.getAttribute('data-fb-correct');const fbW=q.getAttribute('data-fb-wrong');btns.forEach(b=>{b.disabled=true;b.style.opacity='0.6';});if(answer===true){btn.classList.add('correct');btn.style.opacity='1';fb.textContent=fbC||'\u2713 Correct!';fb.className='quiz-feedback mt-2 text-sm font-medium text-green-600';}else{btn.classList.add('incorrect');btn.style.opacity='1';fb.textContent=fbW||'\u2717 Not quite \u2014 review the lesson above.';fb.className='quiz-feedback mt-2 text-sm font-medium text-red-500';}}
document.addEventListener('DOMContentLoaded',()=>{if(window.Prism)Prism.highlightAll();});
</script>"""

# ═══════════════════════════════════════════════════════════
# ASSEMBLE FULL FILE
# ═══════════════════════════════════════════════════════════

NUM_OBJ = len(objectives)

HTML = f"""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap">
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" crossorigin="anonymous">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js" crossorigin="anonymous"></script>

{CSS}

<div class="scroll-progress" id="scroll-progress" style="width:0%;"></div>
<button class="back-to-top" id="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
  <span class="iconify text-lg" data-icon="fa6-solid:arrow-up"></span>
</button>

<div id="hub-root" class="bg-gray-50 min-h-screen">

<!-- HERO -->
<div class="max-w-[1280px] mx-auto px-4 pt-5 pb-0">
  <section class="hero-container">
    <div class="hero-dots"></div>
    <div class="hero-glow" style="width:350px;height:350px;top:-80px;right:0;background:rgba(255,255,255,0.12);"></div>
    <div class="hero-glow" style="width:280px;height:280px;bottom:-50px;left:5%;background:rgba(127,0,76,0.35);"></div>
    <div style="position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent 0%,#f5c6e0 30%,#CB187D 50%,#f5c6e0 70%,transparent 100%);opacity:0.7;"></div>
    <div class="relative z-10 px-8 py-8 md:px-12 md:py-10">
      <div class="hero-split flex flex-col md:flex-row items-center gap-6 md:gap-10">
        <div class="flex-1 min-w-0">
          <div class="flex flex-wrap items-center gap-2 mb-4">
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="iconify text-[10px]" data-icon="fa6-solid:window-maximize"></span> Module {MODULE_NUM}</span>
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="inline-flex items-center gap-1"><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span><span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span></span> Intermediate</span>
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> 5 min read</span>
          </div>
          <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson {LESSON_NUM:02d}</p>
          <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">{LESSON_TITLE}</h1>
          <p class="text-white/80 text-sm md:text-base leading-relaxed mb-4 max-w-lg">{MODULE_TITLE} &middot; {TRACK_LABEL}</p>
          <div class="flex items-center gap-4 mb-5 text-sm">
            <div class="flex items-center gap-2">
              <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
                <span class="iconify text-white text-[10px]" data-icon="fa6-solid:user"></span>
              </span>
              <span class="text-white/85 font-medium text-xs">Python Learning Hub</span>
            </div>
          </div>
          <div class="flex items-center gap-2 flex-wrap">
            <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span><span class="font-extrabold">{NUM_OBJ}</span><span class="font-semibold opacity-55">Goals</span></a>
            <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span><span class="font-extrabold">{len(code_examples)}</span><span class="font-semibold opacity-55">Examples</span></a>
            <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span><span class="font-extrabold">{len(practice_exercises)}</span><span class="font-semibold opacity-55">Exercises</span></a>
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span><span class="font-extrabold">{PROGRESS}</span><span class="font-semibold opacity-55">Progress</span></span>
          </div>
        </div>
        <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
          <div style="padding:0.25rem;opacity:0.75;">
            {HERO_SVG}
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- MAIN LAYOUT -->
<div class="max-w-[1280px] mx-auto px-4 pt-8 pb-12">
  <div class="lesson-layout">
    <aside class="lesson-toc-sidebar">
      <div class="rounded-2xl border border-gray-100 shadow-sm overflow-hidden bg-white">
        <div class="toc-header relative flex items-center gap-2 px-4 py-3 border-b border-gray-100">
          <span class="toc-header-label text-xs font-bold uppercase tracking-widest text-brand">On This Page</span>
          <button class="toc-toggle-btn" onclick="toggleToc()" title="Toggle navigation">
            <span class="iconify text-sm" id="toc-toggle-icon" data-icon="fa6-solid:angles-left"></span>
          </button>
        </div>
        <nav class="toc-body px-2 py-2 border-b border-gray-100" aria-label="Page sections">
          {build_toc_links()}
        </nav>
        <div class="toc-module-list px-3 py-3">
          <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2 px-1">Module Lessons</p>
          <div class="space-y-1">
            {build_sidebar_lessons()}
          </div>
        </div>
      </div>
    </aside>

    <main class="min-w-0 flex-1 space-y-10">

{build_objective()}

{build_overview()}

{build_key_ideas()}

{build_key_concepts()}

{build_code_examples()}

{build_comparison()}

{build_practice()}

{build_mistakes()}

{build_real_world()}

{build_recap()}

{build_knowledge_check()}

{build_next_lesson()}

{build_bottom_nav()}

    </main>
  </div>
</div>

</div>

{SCRIPT}"""

# ═══════════════════════════════════════════════════════════
# WRITE & VERIFY
# ═══════════════════════════════════════════════════════════
os.makedirs(os.path.dirname(TARGET), exist_ok=True)
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(HTML)

lines = HTML.split("\n")
print(f"✅ Wrote {TARGET} ({len(lines)} lines)")

# Div balance
opens = sum(l.count("<div") for l in lines)
closes = sum(l.count("</div>") for l in lines)
print(f"   Div balance: {opens - closes} (opens={opens}, closes={closes})")

# Tab / panel counts
import re as _re
for prefix, label in [("ce","CE"), ("kc","KC"), ("pe","PE"), ("mk","MK"), ("qz","QZ")]:
    tabs_count = len(_re.findall(rf'class="[^"]*{prefix}-step[ "]', HTML))
    panels_count = len(_re.findall(rf'class="[^"]*{prefix}-panel[ "]', HTML))
    print(f"   {label} tabs={tabs_count}, panels={panels_count}")

# Section balance
for sid in ["objective","overview","key-ideas","key-concepts","code-examples","comparison","practice","mistakes","real-world","recap","knowledge-check","next-lesson"]:
    pattern = rf'<section id="{sid}"[^>]*>(.*?)</section>'
    m = _re.search(pattern, HTML, _re.DOTALL)
    if m:
        block = m.group(1)
        o = block.count("<div")
        c = block.count("</div>")
        status = "✅" if o == c else f"❌ ({o-c})"
        print(f"   #{sid}: div balance {status}")
    else:
        print(f"   #{sid}: NOT FOUND ❌")
