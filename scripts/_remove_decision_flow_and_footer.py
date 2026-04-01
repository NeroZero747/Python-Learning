"""
Remove <section id="decision-flow">...</section>, 
its TOC sidebar link, and <footer>...</footer> from all track_03 lessons.
"""
import re, os, glob

BASE = os.path.join(os.path.dirname(__file__), "..",
                    "pages", "track_03_data_engineering")

files = sorted(glob.glob(os.path.join(BASE, "**", "lesson*.html"), recursive=True))
print(f"Found {len(files)} lesson files\n")

df_removed = 0
df_skipped = 0
toc_removed = 0
footer_removed = 0
footer_skipped = 0

for fpath in files:
    fname = os.path.relpath(fpath, BASE)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content

    # 1. Remove <section id="decision-flow">...</section> (greedy within section)
    new_content, n = re.subn(
        r'\n*<section id="decision-flow">.*?</section>\s*',
        '\n\n',
        content,
        flags=re.DOTALL,
    )
    if n > 0:
        df_removed += 1
        print(f"  ✅ {fname}: decision-flow removed")
    else:
        df_skipped += 1
        print(f"  ⏭️  {fname}: no decision-flow found")
    content = new_content

    # 2. Remove TOC sidebar link to #decision-flow (3-line <a> block)
    new_content, n = re.subn(
        r'\s*<a href="#decision-flow"[^>]*>.*?</a>',
        '',
        content,
        flags=re.DOTALL,
    )
    if n > 0:
        toc_removed += 1
    content = new_content

    # 3. Remove <footer ...>...</footer>
    new_content, n = re.subn(
        r'\s*<footer\b[^>]*>.*?</footer>',
        '',
        content,
        flags=re.DOTALL,
    )
    if n > 0:
        footer_removed += 1
        print(f"  ✅ {fname}: footer removed")
    else:
        footer_skipped += 1
        print(f"  ⏭️  {fname}: no footer found")
    content = new_content

    # Write only if changed
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

print(f"\n{'='*60}")
print(f"Decision-flow: {df_removed} removed, {df_skipped} skipped")
print(f"TOC links:     {toc_removed} removed")
print(f"Footers:       {footer_removed} removed, {footer_skipped} skipped")
print(f"Total files:   {len(files)}")
