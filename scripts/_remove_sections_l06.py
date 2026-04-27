"""
Remove the full #comparison and #real-world sections from lesson06_shiny_for_python.html.
Also removes their TOC links.
"""
from pathlib import Path
import re

TARGET = Path(__file__).parent.parent / "pages/mod_05_data_application/lesson06_shiny_for_python.html"
html = TARGET.read_text(encoding="utf-8")
original_len = len(html)

def remove_section(content, section_id, next_section_id):
    """Remove from <section id="SECTION_ID"> up to (not including) <section id="NEXT_ID">"""
    start = content.find(f'\n<section id="{section_id}">')
    if start == -1:
        print(f"  ⚠️  #{section_id} not found")
        return content
    end = content.find(f'\n<section id="{next_section_id}">', start)
    if end == -1:
        print(f"  ⚠️  next section #{next_section_id} not found after #{section_id}")
        return content
    removed = len(content[start:end])
    content = content[:start] + content[end:]
    print(f"  ✅ Removed #{section_id} ({removed} chars)")
    return content

def remove_toc_link(content, href):
    """Remove a single <a href="#SECTION"> TOC link line."""
    pattern = re.compile(r'<a href="#' + re.escape(href) + r'"[^>]*>.*?</a>\n?', re.DOTALL)
    new, n = pattern.subn("", content, count=1)
    if n:
        print(f"  ✅ Removed TOC link #{href}")
    else:
        print(f"  ⚠️  TOC link #{href} not found")
    return new

# 1. Remove #comparison section (ends just before #practice)
html = remove_section(html, "comparison", "practice")

# 2. Remove #real-world section (ends just before #recap)
html = remove_section(html, "real-world", "recap")

# 3. Remove their TOC links
html = remove_toc_link(html, "comparison")
html = remove_toc_link(html, "real-world")

TARGET.write_text(html, encoding="utf-8")
print(f"\nFile size: {original_len} → {len(html)} chars (removed {original_len - len(html)} chars)")
