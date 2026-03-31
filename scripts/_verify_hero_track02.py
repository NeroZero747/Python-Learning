import glob, re, os

pattern = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics\**\*.html'
files = sorted(glob.glob(pattern, recursive=True))
fail = False

for fp in files:
    content = open(fp, encoding='utf-8').read()
    errs = []

    # Must contain hero-container section
    if '<section class="hero-container">' not in content:
        errs.append('missing hero-container')

    # Must have locked author name
    if 'Python Learning Hub' not in content:
        errs.append('missing author name')

    # Must have SVG hex
    if 'hexFill' not in content:
        errs.append('missing SVG hex')

    # Must have hero-abstract-card with correct style
    if 'padding:0.25rem;opacity:0.75;' not in content:
        errs.append('hero-abstract-card style wrong')

    # Difficulty dots must use inline style (not Tailwind)
    if 'style="width:6px;height:6px;border-radius:50%;background:' not in content:
        errs.append('difficulty dots missing inline style')

    # No forbidden shell tags
    for tag in ['<!DOCTYPE', '<html', '<head>', '<body>', '</body>', '</html>']:
        if tag in content:
            errs.append(f'contains {tag}')

    # id="hub-root" present
    if 'id="hub-root"' not in content:
        errs.append('missing id="hub-root"')

    if errs:
        fail = True
        print(f'❌  {os.path.basename(fp)}: {"; ".join(errs)}')
    else:
        # Print brief summary
        m_title = re.search(r'<h1[^>]*>(.*?)</h1>', content)
        m_diff  = re.search(r'>(Beginner|Intermediate|Advanced)<', content)
        m_prog  = re.search(r'<span class="font-extrabold">(\d+)<span class="font-bold opacity-50">/(\d+)', content)
        title   = m_title.group(1) if m_title else '?'
        diff    = m_diff.group(1) if m_diff else '?'
        prog    = f"{m_prog.group(1)}/{m_prog.group(2)}" if m_prog else '?/?'
        print(f'✅  {os.path.basename(fp)} [{diff} {prog}] — {title}')

print()
if not fail:
    print(f'All {len(files)} files passed verification.')
else:
    print('Some files FAILED — review errors above.')
