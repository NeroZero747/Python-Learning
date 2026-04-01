#!/usr/bin/env python3
"""
Rewrite <section id="mistakes"> for all 11 lessons in
track_03 / mod_04_data_pipelines_and_orchestration.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_03_data_engineering" / "mod_04_data_pipelines_and_orchestration"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

LESSONS = {
    # ── Lesson 01: What Is a Data Pipeline ──
    "lesson01_what_is_a_data_pipeline.html": {
        "topic": "data pipeline concepts",
        "mistakes": [
            {
                "tab": "Manual Steps in a Pipeline",
                "title": "Mixing Manual Steps Into an Automated Pipeline",
                "subtitle": "A pipeline that needs a human in the middle is not truly automated.",
                "explanation": 'The point of a data pipeline is end-to-end automation. If you email a CSV manually between the extract and load steps, the pipeline is fragile and depends on someone being available. Automate every stage so the pipeline runs unattended.',
                "wrong_label": "manual handoff",
                "wrong_code": 'df = pd.read_csv("sales.csv")        # extract\ndf.to_csv("to_send.csv", index=False)\n# email CSV to analyst → analyst loads it manually',
                "correct_label": "fully automated",
                "correct_code": 'df = pd.read_csv("sales.csv")        # extract\ndf["total"] = df["price"] * df["qty"] # transform\ndf.to_sql("sales", engine, if_exists="replace")  # load',
                "tip": "If any pipeline step requires opening an email or clicking a button, it belongs in the script, not in a human\u2019s inbox.",
            },
            {
                "tab": "No Logging",
                "title": "Running a Pipeline Without Any Logging",
                "subtitle": "When the pipeline fails overnight, you have no record of what happened.",
                "explanation": 'Print statements vanish when a script runs as a scheduled job. Python\u2019s <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">logging</code> module writes timestamped messages to a file so you can diagnose failures the next morning.',
                "wrong_label": "no logging",
                "wrong_code": 'df = pd.read_csv("sales.csv")\ndf.to_sql("sales", engine)\n# fails at 3 AM — no trace of what went wrong',
                "correct_label": "add logging",
                "correct_code": 'import logging\nlogging.basicConfig(filename="pipeline.log", level=logging.INFO)\ndf = pd.read_csv("sales.csv")\nlogging.info(f"Extracted {len(df)} rows")\ndf.to_sql("sales", engine, if_exists="replace")\nlogging.info("Load complete")',
                "tip": "Log the row count after every stage. A sudden zero or a drastic drop tells you exactly where the pipeline broke.",
            },
            {
                "tab": "Skipping Validation",
                "title": "Loading Data Without Checking It First",
                "subtitle": "Null values, wrong types, and duplicates slip into your database unnoticed.",
                "explanation": 'A pipeline that loads raw data without validation lets bad records corrupt downstream reports and dashboards. Add basic checks — null counts, duplicate keys, type assertions — before writing output.',
                "wrong_label": "no validation",
                "wrong_code": 'df = pd.read_csv("orders.csv")\ndf.to_sql("orders", engine, if_exists="replace")\n# nulls and dupes now in the table',
                "correct_label": "validate before loading",
                "correct_code": 'df = pd.read_csv("orders.csv")\nassert df["order_id"].notnull().all(), "Null IDs found"\nassert df["order_id"].is_unique, "Duplicate IDs found"\ndf.to_sql("orders", engine, if_exists="replace", index=False)',
                "tip": "Two assert lines take seconds to write but catch errors that would otherwise hide in your data for weeks.",
            },
        ],
    },

    # ── Lesson 02: ETL vs ELT ──
    "lesson02_etl_vs_elt.html": {
        "topic": "ETL and ELT patterns",
        "mistakes": [
            {
                "tab": "Transform Before Full Extract",
                "title": "Transforming Data Before the Extract Stage Is Complete",
                "subtitle": "Operating on a partial extract drops rows that arrive later.",
                "explanation": 'Both ETL and ELT begin with a full extract. Transforming a half-loaded DataFrame means late-arriving data is missing from the output. Always finish extracting before you start transforming.',
                "wrong_label": "partial extract",
                "wrong_code": 'chunk = pd.read_csv("sales.csv", nrows=100)  # partial\nchunk["total"] = chunk["price"] * chunk["qty"]\nchunk.to_csv("warehouse.csv", index=False)',
                "correct_label": "full extract first",
                "correct_code": 'df = pd.read_csv("sales.csv")              # full extract\ndf["total"] = df["price"] * df["qty"]      # transform\ndf.to_csv("warehouse.csv", index=False)     # load',
                "tip": "Extract is the foundation. Cutting it short is like photocopying only half a document and then trying to summarise the full report.",
            },
            {
                "tab": "Overwriting Raw Data",
                "title": "Transforming Data In Place and Overwriting the Source File",
                "subtitle": "Destroying the raw copy makes re-processing and auditing impossible.",
                "explanation": 'ELT preserves raw data in the warehouse so you can rerun transforms later. If you overwrite the only copy, there is no way to recover if the transform logic changes or has a bug.',
                "wrong_label": "overwrite source",
                "wrong_code": 'df = pd.read_csv("sales.csv")\ndf["total"] = df["price"] * df["qty"]\ndf.to_csv("sales.csv", index=False)  # raw data gone',
                "correct_label": "preserve raw, write processed",
                "correct_code": 'df = pd.read_csv("sales.csv")\ndf.to_csv("raw_sales.csv", index=False)    # keep raw\ndf["total"] = df["price"] * df["qty"]\ndf.to_csv("processed_sales.csv", index=False)',
                "tip": "Raw data is your safety net. Overwriting it is like shredding the original receipt after writing the expense report.",
            },
            {
                "tab": "Wrong Pattern Choice",
                "title": "Choosing ETL When the Warehouse Can Transform Faster",
                "subtitle": "Heavy Python transforms waste time when SQL handles the aggregation natively.",
                "explanation": 'If your target database supports SQL, loading raw data and transforming there (ELT) is often faster for large datasets. Reserve ETL for cases where the destination cannot run transforms — like flat files or simple databases.',
                "wrong_label": "heavy Python transforms",
                "wrong_code": 'df = pd.read_csv("events.csv")       # 50 million rows\ndf = df.groupby("user_id").sum()      # slow in pandas\ndf.to_sql("events", engine)',
                "correct_label": "load raw, transform in SQL",
                "correct_code": 'df = pd.read_csv("events.csv")       # extract\ndf.to_sql("raw_events", engine)       # load raw\n# SQL: SELECT user_id, SUM(amount)\n#      FROM raw_events GROUP BY user_id',
                "tip": "Databases are built for aggregation. Let the warehouse do the heavy lifting instead of making pandas churn through millions of rows.",
            },
        ],
    },

    # ── Lesson 03: Pipeline Design Patterns ──
    "lesson03_pipeline_design_patterns.html": {
        "topic": "pipeline design patterns",
        "mistakes": [
            {
                "tab": "Monolithic Script",
                "title": "Writing the Entire Pipeline as One Long Script Without Functions",
                "subtitle": "A single block is impossible to test, debug, or reuse.",
                "explanation": 'When extract, transform, and load live in one continuous block, a bug anywhere forces you to rerun everything from scratch. Splitting into separate functions lets you test each stage independently and swap implementations without touching the rest.',
                "wrong_label": "one big script",
                "wrong_code": 'df = pd.read_csv("orders.csv")\ndf["total"] = df["price"] * df["qty"]\ndf = df.dropna()\ndf.to_csv("output.csv", index=False)',
                "correct_label": "modular functions",
                "correct_code": 'def extract():\n    return pd.read_csv("orders.csv")\ndef transform(df):\n    df["total"] = df["price"] * df["qty"]\n    return df.dropna()\ndef load(df):\n    df.to_csv("output.csv", index=False)\n\nload(transform(extract()))',
                "tip": "If you cannot describe what a function does in one sentence, it is doing too much. Split until each function has one clear job.",
            },
            {
                "tab": "Non-Idempotent Steps",
                "title": "Writing Steps That Produce Different Results When Rerun",
                "subtitle": "Rerunning the pipeline duplicates rows or corrupts the output.",
                "explanation": 'An idempotent step produces the same result whether you run it once or ten times. Appending to a file without deduplication is the most common violation. Use overwrite or upsert logic to guarantee consistent output.',
                "wrong_label": "appends duplicates",
                "wrong_code": 'df.to_csv("output.csv", mode="a", header=False)\n# each run adds another copy of the data',
                "correct_label": "overwrite safely",
                "correct_code": 'df.to_csv("output.csv", index=False)\n# same result every run — idempotent',
                "tip": "Ask yourself: \"If this step runs twice, do I get the same file?\" If the answer is no, fix it before deploying.",
            },
            {
                "tab": "No Error Recovery",
                "title": "Ignoring Errors Instead of Catching and Recovering",
                "subtitle": "A silent failure in one stage corrupts every stage that follows.",
                "explanation": 'Without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">try/except</code>, a missing file or bad record crashes the entire pipeline with no record of what happened. Wrap each stage, log the error, and decide whether to skip or abort.',
                "wrong_label": "no error handling",
                "wrong_code": 'df = pd.read_csv("orders.csv")  # FileNotFoundError\ndf.to_csv("output.csv")',
                "correct_label": "catch and log",
                "correct_code": 'import logging\ntry:\n    df = pd.read_csv("orders.csv")\n    df.to_csv("output.csv", index=False)\nexcept Exception as err:\n    logging.error(f"Pipeline failed: {err}")',
                "tip": "A pipeline that crashes loudly is better than one that crashes silently. Good error handling turns a mystery into a diagnosis.",
            },
        ],
    },

    # ── Lesson 04: Working With Large Data Files ──
    "lesson04_working_with_large_data_files.html": {
        "topic": "large data file processing",
        "mistakes": [
            {
                "tab": "Loading Everything at Once",
                "title": "Reading an Entire Large File Into Memory at Once",
                "subtitle": "Python raises a MemoryError when the file exceeds available RAM.",
                "explanation": 'Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.read_csv()</code> without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">chunksize</code> loads the whole file. For multi-gigabyte files, this exhausts memory and freezes or crashes the process.',
                "wrong_label": "load everything",
                "wrong_code": 'df = pd.read_csv("large_file.csv")  # 8 GB → MemoryError',
                "correct_label": "read in chunks",
                "correct_code": 'for chunk in pd.read_csv("large_file.csv",\n                         chunksize=50000):\n    process(chunk)  # manageable 50 K rows at a time',
                "tip": "Chunked reading is like drinking from a glass instead of a fire hose. Your computer can only swallow so much data at once.",
            },
            {
                "tab": "Loading All Columns",
                "title": "Loading Every Column When You Only Need a Few",
                "subtitle": "Unused columns waste memory and slow down every operation.",
                "explanation": 'A 20-column CSV uses five times the memory of the four columns you actually need. Pass <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">usecols</code> to skip the rest.',
                "wrong_label": "all columns",
                "wrong_code": 'df = pd.read_csv("orders.csv")  # loads all 20 columns',
                "correct_label": "select columns",
                "correct_code": 'cols = ["order_id", "price", "quantity", "date"]\ndf = pd.read_csv("orders.csv", usecols=cols)',
                "tip": "List the columns your code actually uses before loading. If a column never appears in your script, do not load it.",
            },
            {
                "tab": "Default Data Types",
                "title": "Leaving Default int64 and float64 on Large Numeric Columns",
                "subtitle": "Pandas defaults to 8-byte types when 1 or 2 bytes would hold the same values.",
                "explanation": 'A column of small integers (0\u2013255) stored as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int64</code> uses 8 bytes per value. Downcasting to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">int8</code> uses 1 byte. Multiply that saving across millions of rows and you free gigabytes of RAM.',
                "wrong_label": "default types",
                "wrong_code": 'df = pd.read_csv("orders.csv")\nprint(df["quantity"].dtype)  # int64 — 8 bytes each',
                "correct_label": "downcast types",
                "correct_code": 'df = pd.read_csv("orders.csv")\ndf["quantity"] = pd.to_numeric(\n    df["quantity"], downcast="integer")  # int8 or int16',
                "tip": "Downcasting is free performance. The numbers stay the same — only the storage shrinks.",
            },
        ],
    },

    # ── Lesson 05: Data Validation in Pipelines ──
    "lesson05_data_validation_in_pipelines.html": {
        "topic": "data validation in pipelines",
        "mistakes": [
            {
                "tab": "Validating After Loading",
                "title": "Checking Data Quality After It Has Already Been Loaded Into the Database",
                "subtitle": "Bad records are already in the table by the time you discover them.",
                "explanation": 'Validation should happen before the load step, not after. Once invalid data reaches the database, downstream dashboards and reports consume it immediately. Validate first, then load only the clean records.',
                "wrong_label": "validate after load",
                "wrong_code": 'df.to_sql("orders", engine, if_exists="append")\n# now check for issues\nassert df["amount"].notnull().all()  # too late',
                "correct_label": "validate before load",
                "correct_code": 'assert df["amount"].notnull().all(), "Nulls found"\nassert (df["amount"] >= 0).all(), "Negatives found"\ndf.to_sql("orders", engine, if_exists="append", index=False)',
                "tip": "Think of validation as the gate before the warehouse. Bad data should be stopped at the gate, not discovered after it is already on the shelves.",
            },
            {
                "tab": "Dropping All Bad Rows Silently",
                "title": "Dropping Invalid Rows Without Logging or Saving Them",
                "subtitle": "You lose visibility into how much data is being discarded and why.",
                "explanation": 'Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">df.dropna()</code> silently removes rows. If 40% of your data is bad, you should know — otherwise your reports look fine but are based on a fraction of the records. Log the count and save rejected rows.',
                "wrong_label": "silent drop",
                "wrong_code": 'df = df.dropna()  # how many rows were dropped? unknown',
                "correct_label": "log and quarantine",
                "correct_code": 'mask = df["email"].notna()\nbad = df[~mask]\nbad.to_csv("quarantine.csv", index=False)\nlogging.warning(f"Quarantined {len(bad)} bad rows")\ndf = df[mask]',
                "tip": "Quarantined rows are an audit trail. If stakeholders ask why a report looks low, you can point to the quarantine file and explain exactly what was filtered out.",
            },
            {
                "tab": "Hardcoded Thresholds",
                "title": "Hardcoding Validation Thresholds Instead of Making Them Configurable",
                "subtitle": "Business rules change — hardcoded numbers require code edits to update.",
                "explanation": 'Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">assert amount > 10</code> directly in the code means changing the threshold requires a code change and a redeployment. Store thresholds in a config file or dictionary so they can be updated without touching the script.',
                "wrong_label": "hardcoded threshold",
                "wrong_code": 'assert (df["amount"] > 10).all()  # magic number',
                "correct_label": "configurable threshold",
                "correct_code": 'config = {"min_amount": 10}  # from config file\nassert (df["amount"] > config["min_amount"]).all()',
                "tip": "Store validation rules in a config dict or YAML file. When the business changes the minimum order amount, you update the config — not the pipeline code.",
            },
        ],
    },

    # ── Lesson 09: Scheduling Pipelines ──
    "lesson09_scheduling_pipelines.html": {
        "topic": "scheduling pipelines",
        "mistakes": [
            {
                "tab": "No Overlap Protection",
                "title": "Scheduling a Pipeline Without Checking if the Previous Run Is Still Going",
                "subtitle": "Two overlapping runs process the same data and create duplicates or lock conflicts.",
                "explanation": 'If a pipeline takes 45 minutes but is scheduled every 30 minutes, two instances run at the same time. Use a lock file or a database flag to ensure only one instance runs at a time.',
                "wrong_label": "no lock",
                "wrong_code": '# Cron: */30 * * * * python pipeline.py\n# Pipeline takes 45 min → two instances run together',
                "correct_label": "lock file prevents overlap",
                "correct_code": 'import os, sys\nLOCK = "pipeline.lock"\nif os.path.exists(LOCK):\n    print("Already running"); sys.exit(0)\nopen(LOCK, "w").close()\ntry:\n    run_pipeline()\nfinally:\n    os.remove(LOCK)',
                "tip": "A lock file is the simplest overlap guard. For production systems, consider database-level advisory locks or a task queue.",
            },
            {
                "tab": "Wrong Cron Syntax",
                "title": "Using Incorrect Cron Expressions and Not Testing Them",
                "subtitle": "A wrong cron expression runs the pipeline at the wrong time — or not at all.",
                "explanation": 'Cron syntax has five fields: minute, hour, day, month, weekday. Swapping minute and hour is a common mistake. Always test your cron expression with an online parser before deploying.',
                "wrong_label": "swapped fields",
                "wrong_code": '# Intended: 6:00 AM daily\n# Wrong: runs at minute 6 of every hour\n6 * * * * python pipeline.py',
                "correct_label": "correct cron expression",
                "correct_code": '# Correct: 6:00 AM daily\n0 6 * * * python /full/path/to/pipeline.py',
                "tip": "Use an online cron expression validator (like crontab.guru) to check your schedule before deploying. A one-field mistake can mean 24 extra runs per day.",
            },
            {
                "tab": "No Monitoring",
                "title": "Scheduling a Pipeline Without Any Monitoring or Alerts",
                "subtitle": "The pipeline can fail for days before anyone notices.",
                "explanation": 'A scheduled pipeline that fails silently is worse than one that never ran. At minimum, send a notification (email, Slack, log entry) when the pipeline finishes or fails, so someone can investigate.',
                "wrong_label": "no monitoring",
                "wrong_code": '# Pipeline runs at 2 AM\n# Fails for a week — nobody knows\nrun_pipeline()',
                "correct_label": "notify on completion or failure",
                "correct_code": 'import logging\ntry:\n    run_pipeline()\n    logging.info("Pipeline completed successfully")\nexcept Exception as err:\n    logging.error(f"Pipeline FAILED: {err}")\n    # send_alert(err)  # email or Slack notification',
                "tip": "Start with a simple log message. Once that works, add an email or Slack alert for failures. Monitoring does not have to be complex to be effective.",
            },
        ],
    },

    # ── Lesson 10: Building a Simple Python Pipeline ──
    "lesson10_building_a_simple_python_pipeline.html": {
        "topic": "building a simple Python pipeline",
        "mistakes": [
            {
                "tab": "All Code in One Block",
                "title": "Writing Extract, Transform, and Load as One Continuous Block",
                "subtitle": "You cannot test or rerun individual stages without executing the entire script.",
                "explanation": 'A monolithic script means a transform bug forces you to re-extract from source. Separate each stage into its own function so you can call and test them independently.',
                "wrong_label": "monolithic block",
                "wrong_code": 'df = pd.read_csv("raw.csv")\ndf = df.dropna()\ndf["total"] = df["price"] * df["qty"]\ndf.to_sql("clean", engine)',
                "correct_label": "separate functions",
                "correct_code": 'def extract():\n    return pd.read_csv("raw.csv")\ndef transform(df):\n    df = df.dropna()\n    df["total"] = df["price"] * df["qty"]\n    return df\ndef load(df):\n    df.to_sql("clean", engine, if_exists="replace")',
                "tip": "Save intermediate results to CSV after extract. That way, when you iterate on transform, you do not re-read the source every time.",
            },
            {
                "tab": "Hardcoded File Paths",
                "title": "Hardcoding Absolute File Paths in Pipeline Functions",
                "subtitle": "The pipeline breaks on any machine where the folder structure differs.",
                "explanation": 'An absolute path like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">C:/Users/me/data.csv</code> only works on one computer. Use relative paths or environment variables so the same code runs on your laptop and the production server.',
                "wrong_label": "absolute path",
                "wrong_code": 'df = pd.read_csv("C:/Users/me/data/raw.csv")',
                "correct_label": "configurable path",
                "correct_code": 'import os\ndata_dir = os.getenv("DATA_DIR", "data")\ndf = pd.read_csv(f"{data_dir}/raw.csv")',
                "tip": "Store folder paths in environment variables or a config file. Your laptop and the server will never share the same folder tree.",
            },
            {
                "tab": "No Row Count Checks",
                "title": "Not Checking Row Counts Between Stages",
                "subtitle": "A silent drop from 10,000 to 0 rows goes unnoticed until reports are wrong.",
                "explanation": 'After each pipeline stage, log the row count. A sudden zero or a large drop means a bug was introduced in that stage. Catching it immediately is far easier than debugging the final output.',
                "wrong_label": "no checks",
                "wrong_code": 'df = extract()\ndf = transform(df)\nload(df)  # how many rows? who knows',
                "correct_label": "log row counts",
                "correct_code": 'df = extract()\nprint(f"Extracted: {len(df)} rows")\ndf = transform(df)\nprint(f"Transformed: {len(df)} rows")\nassert len(df) > 0, "No rows after transform"\nload(df)',
                "tip": "A one-line print after every stage costs nothing and saves hours of debugging. Make it a habit.",
            },
        ],
    },

    # ── Lesson 11: Pipeline Project — Automating Data Ingestion ──
    "lesson11_pipeline_project_automating_data_ingestion.html": {
        "topic": "automating data ingestion",
        "mistakes": [
            {
                "tab": "Re-Ingesting All Data",
                "title": "Re-Ingesting the Entire Dataset Instead of Only New Records",
                "subtitle": "Processing everything every time wastes compute and slows the pipeline.",
                "explanation": 'A well-designed ingestion pipeline tracks a high-water mark (the latest ID or timestamp already loaded) and fetches only new records. Without it, every run reprocesses millions of rows you have already loaded.',
                "wrong_label": "full re-ingest",
                "wrong_code": 'df = pd.read_csv("all_orders.csv")     # 5 million rows\ndf.to_sql("orders", engine, if_exists="replace")',
                "correct_label": "incremental ingest",
                "correct_code": 'last_id = get_watermark()               # e.g. 4_999_000\nnew = pd.read_csv("all_orders.csv")\nnew = new[new["id"] > last_id]          # only new rows\nnew.to_sql("orders", engine, if_exists="append")\nupdate_watermark(new["id"].max())',
                "tip": "Store the high-water mark in a small database table or a JSON file. It turns a 30-minute full reload into a 30-second incremental update.",
            },
            {
                "tab": "No Validation on Arrival",
                "title": "Loading Incoming Data Without Any Validation",
                "subtitle": "Corrupt or unexpected data propagates to downstream tables and reports.",
                "explanation": 'New data arriving from external sources is inherently untrustworthy. Validate format, check for nulls in key columns, and reject records that fail before writing to the database.',
                "wrong_label": "trust incoming data",
                "wrong_code": 'new = fetch_new_records()\ndf = pd.DataFrame(new)\ndf.to_sql("orders", engine, if_exists="append")',
                "correct_label": "validate before loading",
                "correct_code": 'new = fetch_new_records()\ndf = pd.DataFrame(new)\nassert df["id"].notnull().all(), "Null IDs"\nassert (df["amount"] >= 0).all(), "Negative amounts"\ndf.to_sql("orders", engine, if_exists="append", index=False)',
                "tip": "External data is guilty until proven innocent. Two assert lines are enough to catch the most common data problems on arrival.",
            },
            {
                "tab": "No Step Logging",
                "title": "Not Logging Each Step of the Ingestion Pipeline",
                "subtitle": "When the pipeline fails, you cannot tell which step caused the failure.",
                "explanation": 'Log the start and end of every stage — fetch, validate, load — with row counts and timestamps. Without logs, you are diagnosing failures blind.',
                "wrong_label": "no logging",
                "wrong_code": 'data = fetch()\ndf = validate(data)\nload(df)\n# which step failed? unknown',
                "correct_label": "log every step",
                "correct_code": 'import logging\ndata = fetch()\nlogging.info(f"Fetched {len(data)} records")\ndf = validate(data)\nlogging.info(f"Validated — {len(df)} clean rows")\nload(df)\nlogging.info("Load complete")',
                "tip": "Timestamped logs are your pipeline\u2019s black box. When something breaks, the log tells you what, when, and where.",
            },
        ],
    },

    # ── Lesson 12: Pipeline Project — Data Quality Checks ──
    "lesson12_pipeline_project_data_quality_checks.html": {
        "topic": "data quality checks in pipelines",
        "mistakes": [
            {
                "tab": "Checking Only Nulls",
                "title": "Only Checking for Null Values and Ignoring Other Quality Issues",
                "subtitle": "Data can be non-null but still invalid — duplicates, out-of-range values, wrong formats.",
                "explanation": 'Null checks are the first line of defence, but they are not enough. Duplicate keys, negative prices, and future dates are all non-null values that should still be rejected. Build a multi-check validation pipeline.',
                "wrong_label": "null check only",
                "wrong_code": 'df = df.dropna()\n# duplicates, negatives, bad dates all pass through',
                "correct_label": "multi-rule validation",
                "correct_code": 'df = df.dropna(subset=["id", "amount"])\ndf = df.drop_duplicates(subset=["id"])\ndf = df[df["amount"] >= 0]\ndf = df[df["date"] <= pd.Timestamp.today()]',
                "tip": "Build a checklist of quality rules: nulls, duplicates, range checks, format checks. Run all of them in sequence so nothing slips through.",
            },
            {
                "tab": "Discarding Without Quarantine",
                "title": "Dropping Bad Records Without Saving Them for Review",
                "subtitle": "You lose visibility into how much data is being rejected and why.",
                "explanation": 'Simply dropping rows makes the problem invisible. Save rejected records to a quarantine file so you can review them, fix the source, and reprocess if needed.',
                "wrong_label": "silent discard",
                "wrong_code": 'df = df[df["amount"] >= 0]  # negatives disappear',
                "correct_label": "quarantine bad records",
                "correct_code": 'mask = df["amount"] >= 0\nbad = df[~mask]\nbad.to_csv("quarantine.csv", index=False)\nlogging.warning(f"Quarantined {len(bad)} rows")\ndf = df[mask]',
                "tip": "A quarantine file is your audit trail. When stakeholders ask why the numbers look low, you can point to exactly which records were filtered and why.",
            },
            {
                "tab": "No Quality Metrics",
                "title": "Not Tracking Quality Metrics Over Time",
                "subtitle": "You cannot spot trends — like rising null rates — without historical data.",
                "explanation": 'Recording the percentage of nulls, duplicates, and rejected rows for each run lets you see whether data quality is improving or degrading. Without metrics, a slow decline goes unnoticed until reports break.',
                "wrong_label": "no metrics",
                "wrong_code": 'clean = df.dropna()\nclean.to_sql("orders", engine)',
                "correct_label": "log quality metrics",
                "correct_code": 'total = len(df)\nnulls = df["email"].isnull().sum()\ndupes = df["id"].duplicated().sum()\nlogging.info(\n    f"Total: {total}, Nulls: {nulls}, Dupes: {dupes}")',
                "tip": "Store quality metrics in a separate log table or CSV. A weekly review of null and duplicate rates catches problems before they reach stakeholders.",
            },
        ],
    },

    # ── Lesson 13: Pipeline Project — Database Loading ──
    "lesson13_pipeline_project_database_loading.html": {
        "topic": "database loading in pipelines",
        "mistakes": [
            {
                "tab": "Blind Append",
                "title": "Appending Data Without Checking for Duplicate Records",
                "subtitle": "Rerunning the pipeline creates duplicate rows in the table.",
                "explanation": 'Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">if_exists="append"</code> without deduplication means every run adds another copy of existing records. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">replace</code> for small tables or implement an upsert pattern for large ones.',
                "wrong_label": "blind append",
                "wrong_code": 'df.to_sql("orders", engine, if_exists="append")\n# second run → every row appears twice',
                "correct_label": "deduplicate or replace",
                "correct_code": 'df = df.drop_duplicates(subset=["order_id"])\ndf.to_sql("orders", engine, if_exists="replace", index=False)',
                "tip": "For small datasets, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">if_exists=\"replace\"</code> is simplest. For large tables, use a staging table and a SQL MERGE statement to upsert.",
            },
            {
                "tab": "No Post-Load Verification",
                "title": "Not Verifying the Row Count After Loading Into the Database",
                "subtitle": "You assume the load succeeded but have no proof.",
                "explanation": 'A successful <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_sql()</code> call does not guarantee all rows made it. Compare the DataFrame row count to the database table count to confirm a complete load.',
                "wrong_label": "no verification",
                "wrong_code": 'df.to_sql("orders", engine, if_exists="replace")\n# how many rows in the table? unchecked',
                "correct_label": "verify after load",
                "correct_code": 'df.to_sql("orders", engine, if_exists="replace", index=False)\ndb_count = pd.read_sql("SELECT COUNT(*) FROM orders", engine)\nassert db_count.iloc[0, 0] == len(df), "Row count mismatch"',
                "tip": "A post-load row count check takes one query and catches silent data loss. Add it to every load step.",
            },
            {
                "tab": "No Transaction Wrapping",
                "title": "Loading Data Outside a Transaction So Partial Writes Persist on Error",
                "subtitle": "A half-loaded table leaves your database in an inconsistent state.",
                "explanation": 'If the load step fails halfway, some rows are in the table and some are not. Wrapping the load in a database transaction ensures either all rows are committed or none are — no partial writes.',
                "wrong_label": "no transaction",
                "wrong_code": 'df.to_sql("orders", engine, if_exists="append")\n# crash at row 5,000 — first 5,000 already committed',
                "correct_label": "wrap in a transaction",
                "correct_code": 'with engine.begin() as conn:\n    df.to_sql("orders", conn,\n              if_exists="append", index=False)\n    # all-or-nothing: rollback on error',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">engine.begin()</code> instead of raw <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">engine.connect()</code>. It wraps the block in a transaction that rolls back automatically on failure.",
            },
        ],
    },

    # ── Lesson 14: Production Pipeline Architecture ──
    "lesson14_production_pipeline_architecture.html": {
        "topic": "production pipeline architecture",
        "mistakes": [
            {
                "tab": "Hardcoded Config",
                "title": "Hardcoding Database URLs and File Paths in Production Code",
                "subtitle": "Deploying to a new environment means editing the script instead of the config.",
                "explanation": 'Production, staging, and development environments have different database URLs and file paths. Hardcoding any of them means a code change for every deployment. Use environment variables or a config file.',
                "wrong_label": "hardcoded config",
                "wrong_code": 'engine = create_engine("postgresql://admin:pass@prod-db/orders")\ndf = pd.read_csv("/data/prod/sales.csv")',
                "correct_label": "environment-driven config",
                "correct_code": 'import os\ndb_url = os.getenv("DATABASE_URL")\ndata_path = os.getenv("DATA_PATH", "data/sales.csv")\nengine = create_engine(db_url)\ndf = pd.read_csv(data_path)',
                "tip": "Follow the twelve-factor app pattern: store config in the environment, not in the code. One codebase, many deployments.",
            },
            {
                "tab": "No Graceful Failure",
                "title": "Letting the Pipeline Crash Without Cleanup or Notification",
                "subtitle": "A crash leaves lock files, partial writes, and no one knows it happened.",
                "explanation": 'Production pipelines must fail gracefully: roll back partial writes, remove lock files, and send an alert. An unhandled crash leaves the system in an unknown state that requires manual intervention.',
                "wrong_label": "crash and burn",
                "wrong_code": 'df.to_sql("orders", engine)  # crash → partial data, no alert',
                "correct_label": "graceful failure",
                "correct_code": 'try:\n    with engine.begin() as conn:\n        df.to_sql("orders", conn, if_exists="append", index=False)\nexcept Exception as err:\n    logging.error(f"Pipeline failed: {err}")\n    # send_alert(err)  # notify the team\n    raise',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">try/finally</code> for cleanup (lock files, temp files) and <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">try/except</code> for logging and alerts. Then re-raise so the scheduler knows the job failed.",
            },
            {
                "tab": "No Monitoring",
                "title": "Running a Production Pipeline Without Monitoring or Alerting",
                "subtitle": "The pipeline can break for days before anyone notices.",
                "explanation": 'Production systems need monitoring: run status, row counts, execution time, and error rates. Without it, a silent failure means stale data in dashboards and reports, and nobody knows until a stakeholder complains.',
                "wrong_label": "no monitoring",
                "wrong_code": 'run_pipeline()  # silent — succeeds or fails unseen',
                "correct_label": "log metrics and alert",
                "correct_code": 'import time, logging\nstart = time.time()\ntry:\n    run_pipeline()\n    elapsed = time.time() - start\n    logging.info(f"Pipeline OK in {elapsed:.1f}s")\nexcept Exception as err:\n    logging.error(f"FAILED: {err}")\n    # send_alert(err)',
                "tip": "Start with logging execution time and success/failure status. Once that works, add alerts for anomalies like zero-row outputs or runs that take twice as long as usual.",
            },
        ],
    },
}


# ── HTML builders ──────────────────────────────────────────────────────

def _tab_btn(index: int, label: str, *, active: bool) -> str:
    if active:
        cls = (
            'mk-step mk-step-active flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
            'text-white shadow-lg shadow-pink-200/50 transition-all duration-250'
        )
    else:
        cls = (
            'mk-step flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gray-800 text-gray-400 transition-all duration-250'
        )
    return (
        f'<button onclick="switchMkTab({index})" '
        f'class="{cls}" role="tab">\n'
        f'  <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
        f'  <span class="mk-step-label text-xs font-bold">{label}</span>\n'
        f'</button>'
    )


def _panel(mk: dict, *, hidden: bool) -> str:
    hide = " hidden" if hidden else ""
    return f'''\
<div class="mk-panel mk-panel-anim{hide}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

    <!-- Card header -->
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["subtitle"]}</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>

    <!-- Explanation paragraph -->
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">{mk["explanation"]}</p>
    </div>

    <!-- Wrong / Correct split panel -->
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong \u2014 {mk["wrong_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["wrong_code"]}</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct \u2014 {mk["correct_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["correct_code"]}</code></pre>
        </div>
      </div>
    </div>

    <!-- Amber tip footer -->
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["tip"]}</p>
    </div>

  </div>
</div>'''


def build_section(topic: str, mistakes: list[dict]) -> str:
    tabs = "\n".join(
        _tab_btn(i, m["tab"], active=(i == 0))
        for i, m in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{tabs}\n</div>'

    panels = "\n\n".join(
        _panel(m, hidden=(i > 0))
        for i, m in enumerate(mistakes)
    )

    body = f'{tab_row}\n\n{panels}'

    return f'''\
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with {topic}</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

{body}

    </div>
  </div>
</section>'''


# ── Main ───────────────────────────────────────────────────────────────

ok = fail = 0
for filename, lesson in LESSONS.items():
    path = MOD / filename
    if not path.exists():
        print(f"\u274c NOT FOUND  {filename}")
        fail += 1
        continue

    text = path.read_text(encoding="utf-8")
    replacement = build_section(lesson["topic"], lesson["mistakes"])
    new_text, n = SECTION_RE.subn(replacement, text, count=1)

    if n == 0:
        print(f"\u274c NO MATCH   {filename}")
        fail += 1
        continue

    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {filename}")
    ok += 1

print(f"\n{ok}/{ok + fail} mistakes sections rewritten")
