"""
Remove #decision-flow, #comparison, and #real-world sections
from all lesson files in mod_06a_sql_foundation.
Also removes the matching TOC sidebar links.
"""

import re
from pathlib import Path

BASE = Path("c:/Users/nightwolf/Projects/Python-Learning/pages/mod_06a_sql_foundation")

TARGET_FILES = sorted([
    *BASE.glob("mod_05_sql_foundations/lesson*.html"),
    *BASE.glob("mod_06_advanced_sql_for_data_analysis/lesson*.html"),
])

SECTION_IDS = ["decision-flow", "comparison", "real-world"]

# TOC link patterns to remove (full <a> tag lines)
TOC_HREF_PATTERNS = [
    r'\n<a href="#decision-flow"[^>]*>.*?</a>',
    r'\n<a href="#comparison"[^>]*>.*?</a>',
    r'\n<a href="#real-world"[^>]*>.*?</a>',
]


def remove_section(html: str, section_id: str) -> str:
    """Remove a top-level <section id="SECTION_ID"> ... </section> block."""
    pattern = re.compile(
        r'\n?[ \t]*<section id="' + re.escape(section_id) + r'".*?</section>',
        re.DOTALL,
    )
    new_html, count = pattern.subn("", html)
    return new_html, count


def remove_toc_link(html: str, href: str) -> str:
    """Remove a TOC <a href="#HREF"> link line."""
    pattern = re.compile(
        r'\n[ \t]*<a href="#' + re.escape(href) + r'"[^>]*>.*?</a>',
        re.DOTALL,
    )
    new_html, count = pattern.subn("", html)
    return new_html, count


total_patched = 0

for fpath in TARGET_FILES:
    original = fpath.read_text(encoding="utf-8")
    html = original
    file_changes = 0

    # Remove sections
    for sid in SECTION_IDS:
        html, n = remove_section(html, sid)
        file_changes += n

    # Remove TOC links
    for sid in SECTION_IDS:
        html, n = remove_toc_link(html, sid)
        file_changes += n

    if file_changes > 0:
        fpath.write_text(html, encoding="utf-8")
        print(f"✅ {fpath.name} — {file_changes} removal(s)")
        total_patched += 1
    else:
        print(f"⚠️  {fpath.name} — nothing matched (already clean or different structure)")

print(f"\nDone. {total_patched}/{len(TARGET_FILES)} files updated.")
