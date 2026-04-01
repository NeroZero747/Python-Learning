"""Verify hero banners in all track_03 lesson files."""
import os, re

BASE = "pages/track_03_data_engineering"
HERO_OPEN = '<section class="hero-container">'
CHECKS = {
    "hero-container": r'<section class="hero-container">',
    "hero-dots": r'class="hero-dots"',
    "hex-SVG": r'<svg viewBox="0 0 280 324"',
    "badge-pills": r'class="hero-pill',
    "stat-goals": r'#objective.*?Goals',
    "stat-examples": r'#code-examples.*?Examples',
    "stat-exercises": r'#practice.*?Exercises',
    "stat-progress": r'Progress',
    "difficulty-dots": r'border-radius:50%',
    "author-line": r'Python Learning Hub',
    "pub-date": r'March 31, 2026',
    "title-h1": r'<h1 class="text-3xl md:text-4xl',
    "subtitle": r'text-white/80 text-sm md:text-base',
    "lesson-label": r'Lesson \d+',
    "module-badge": r'Module \d+',
    "PYTHON-text": r'>PYTHON<',
    "LEARNING-HUB": r'>LEARNING HUB<',
    "section-preserved-8+": None,  # special check
}

files = []
for root, dirs, fnames in os.walk(BASE):
    dirs.sort()
    for fn in sorted(fnames):
        if fn.endswith(".html"):
            files.append(os.path.join(root, fn))

pass_count = 0
fail_count = 0
for fp in files:
    content = open(fp, encoding="utf-8").read()
    rel = os.path.relpath(fp, BASE)
    issues = []

    for label, pat in CHECKS.items():
        if label == "section-preserved-8+":
            secs = re.findall(r'<section id="([^"]+)"', content)
            if len(secs) < 8:
                issues.append(f"{label} (only {len(secs)} sections)")
        else:
            if not re.search(pat, content, re.DOTALL):
                issues.append(label)

    if issues:
        print(f"  [FAIL] {rel}: missing {', '.join(issues)}")
        fail_count += 1
    else:
        pass_count += 1

print(f"\nVerified: {pass_count} passed, {fail_count} failed ({pass_count + fail_count} total)")
