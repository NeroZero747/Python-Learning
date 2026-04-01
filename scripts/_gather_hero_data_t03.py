import pathlib, re

root = pathlib.Path(r"pages/track_03_data_engineering")
ce_re = re.compile(r'ce-step-label')
pe_re = re.compile(r'pe-step-label')
h1_re = re.compile(r'<h1[^>]*>(.*?)</h1>', re.DOTALL)
hero_re = re.compile(r'<section class="hero-container">')

for f in sorted(root.rglob("lesson*.html")):
    html = f.read_text(encoding="utf-8")
    ce = len(ce_re.findall(html))
    pe = len(pe_re.findall(html))
    h1_match = h1_re.search(html)
    title = h1_match.group(1).strip() if h1_match else "NO H1"
    has_hero = bool(hero_re.search(html))
    rel = f.relative_to(root)
    # Clean HTML from title
    title = re.sub(r'<[^>]+>', '', title).strip()
    print(f"{rel}|ce={ce}|pe={pe}|hero={has_hero}|title={title}")
