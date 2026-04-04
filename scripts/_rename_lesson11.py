"""
Rename lesson11 file and update all mod_03 references:
- Old filename: lesson11_parquet_and_performance_profiling.html
- New filename: lesson11_working_with_parquet_files.html
- Old TOC label: "11. Parquet &amp; Performance Profiling"
- New TOC label: "11. Working with Parquet Files"
"""
import os, glob

MOD_DIR = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_03_python_for_data_analysts"
OLD_NAME = "lesson11_parquet_and_performance_profiling.html"
NEW_NAME = "lesson11_working_with_parquet_files.html"
OLD_LABEL = "11. Parquet &amp; Performance Profiling"
NEW_LABEL = "11. Working with Parquet Files"

# Rename the file
old_path = os.path.join(MOD_DIR, OLD_NAME)
new_path = os.path.join(MOD_DIR, NEW_NAME)
os.rename(old_path, new_path)
print(f"Renamed: {OLD_NAME} -> {NEW_NAME}")

# Update references in all lesson files
files = sorted(glob.glob(os.path.join(MOD_DIR, "lesson*.html")))
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    original = content

    # Replace filename references (hrefs)
    content = content.replace(OLD_NAME, NEW_NAME)

    # Replace TOC label text
    content = content.replace(OLD_LABEL, NEW_LABEL)

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        fname = os.path.basename(f)
        changes = []
        if OLD_NAME in original:
            changes.append("href")
        if OLD_LABEL in original:
            changes.append("label")
        print(f"  Updated {fname}: {', '.join(changes)}")
    else:
        print(f"  Skipped {os.path.basename(f)}: no changes needed")

# Verify no old references remain
print("\nVerification:")
for f in files:
    content = open(f, encoding='utf-8').read()
    fname = os.path.basename(f)
    if OLD_NAME in content:
        print(f"  WARNING: {fname} still has old filename ref")
    if OLD_LABEL in content:
        print(f"  WARNING: {fname} still has old label ref")
print("  All files checked.")
