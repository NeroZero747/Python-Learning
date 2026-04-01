"""Audit key-concepts sections in all track_03 lesson files."""
import re, pathlib

BASE = pathlib.Path('pages/track_03_data_engineering')
results = []

for f in sorted(BASE.rglob('*.html')):
    text = f.read_text(encoding='utf-8')
    rel = str(f.relative_to(BASE))

    # Extract hero title
    hero_match = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
    hero_title = re.sub(r'<[^>]+>', '', hero_match.group(1)).strip() if hero_match else 'NOT FOUND'

    # Count kc-tab buttons using a pattern that matches class attributes containing kc-tab
    kc_tab_buttons = re.findall(r'class="[^"]*\bkc-tab\b[^"]*"', text)
    kc_tab_count = len(kc_tab_buttons)

    # Extract kc-tab labels
    kc_labels = re.findall(r'kc-tab-label[^>]*>(.*?)</span>', text, re.DOTALL)
    kc_labels = [re.sub(r'<[^>]+>', '', l).strip() for l in kc_labels]

    # Check if key-concepts section exists
    has_kc_section = 'id="key-concepts"' in text

    # Find key-concepts section and check for bg-code
    kc_section_match = re.search(
        r'(<section[^>]*id="key-concepts".*?)(?=<section[^>]*id=|$)', text, re.DOTALL
    )
    has_code_in_kc = False
    if kc_section_match:
        kc_section = kc_section_match.group(1)
        has_code_in_kc = 'bg-code' in kc_section

    # Extract objective text for topic understanding
    obj_match = re.search(
        r'<section[^>]*id="objective"(.*?)(?=<section[^>]*id=)', text, re.DOTALL
    )
    obj_text = ''
    if obj_match:
        obj_text = re.sub(r'<[^>]+>', ' ', obj_match.group(1))
        obj_text = re.sub(r'\s+', ' ', obj_text).strip()[:400]

    # Extract overview hook quote
    hook_match = re.search(r'fa6-solid:quote-left.*?<p[^>]*>(.*?)</p>', text, re.DOTALL)
    hook_text = ''
    if hook_match:
        hook_text = re.sub(r'<[^>]+>', '', hook_match.group(1)).strip()[:200]

    results.append({
        'file': rel,
        'hero': hero_title,
        'kc_count': kc_tab_count,
        'kc_labels': kc_labels,
        'has_kc_section': has_kc_section,
        'has_code_in_kc': has_code_in_kc,
        'obj_summary': obj_text,
        'hook': hook_text,
    })

# Print organized by module
current_mod = ''
for r in results:
    mod = r['file'].split('/')[0] if '/' in r['file'] else r['file'].split('\\')[0]
    if mod != current_mod:
        current_mod = mod
        print(f"\n{'='*80}")
        print(f"  MODULE: {mod}")
        print(f"{'='*80}")

    print(f"\n--- {r['file']} ---")
    print(f"  Hero:       {r['hero']}")
    print(f"  KC Section: {r['has_kc_section']}")
    print(f"  KC Tabs:    {r['kc_count']}")
    if r['kc_labels']:
        for i, lab in enumerate(r['kc_labels'], 1):
            print(f"    Tab {i}: {lab}")
    else:
        print(f"    (no tab labels found)")
    print(f"  Code (bg-code): {r['has_code_in_kc']}")
    print(f"  Hook: {r['hook'][:120]}..." if len(r['hook']) > 120 else f"  Hook: {r['hook']}")
    print(f"  Obj:  {r['obj_summary'][:200]}..." if len(r['obj_summary']) > 200 else f"  Obj:  {r['obj_summary']}")

print(f"\n\nTOTAL FILES: {len(results)}")
print(f"Files with KC section: {sum(1 for r in results if r['has_kc_section'])}")
print(f"Files with code in KC: {sum(1 for r in results if r['has_code_in_kc'])}")
