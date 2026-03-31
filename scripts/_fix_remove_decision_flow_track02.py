import re
import glob
import os

TARGET_PATTERN = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics\**\*.html'

files = glob.glob(TARGET_PATTERN, recursive=True)

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove TOC link (3-line block)
    content = re.sub(
        r'\n<a href="#decision-flow"[^>]+>\n  <span[^>]+>[^<]*</span> Decision Flow\n</a>',
        '',
        content
    )

    # 2. Remove the entire <section id="decision-flow"> block
    # The section ends at </section> followed by a blank line + next section
    content = re.sub(
        r'\n<section id="decision-flow">.*?</section>(?=\n)',
        '',
        content,
        flags=re.DOTALL
    )

    if content == original:
        print(f'⚠️  No changes — {os.path.basename(filepath)}')
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅  Patched — {os.path.basename(filepath)}')
