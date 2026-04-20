"""
Normalize #practice section format across all mod_04_data_engineering lessons.

Fixes applied (within practice section only):
  1. Tab container: remove flex-wrap
  2. Tab button icons → fa6-solid:pencil
  3. Panel header icons → fa6-solid:pencil
  4. Old accordion button → canonical simple button
  5. accordion-body: remove mt-3 class
  6. Code block inside accordion: remove mt-1 / mt-3
  7. "Why this matters" italic/strong tip → amber bg-amber-tip block
  8. Task label: "Your Tasks" → "Your Task", mb-3 → mb-1
  9. Remove w-full from task inner div
 10. Inline code in task box: gray → pink canonical style
 11. Keyword tags in panel header: add pill bg if missing
"""

import re, os, sys

LESSON_DIR = os.path.join(os.path.dirname(__file__), "..", "pages", "mod_04_data_engineering")
LESSONS = sorted(f for f in os.listdir(LESSON_DIR) if f.startswith("lesson") and f.endswith(".html"))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_practice(content):
    """Return (start, end, section_text) for the practice section."""
    m = re.search(r'<section\s+id="practice"[^>]*>', content)
    if not m:
        return None, None, None
    start = m.start()
    # Find the matching </section> — since HTML sections don't nest,
    # just find the first </section> after the opening tag.
    end_tag = '</section>'
    end = content.index(end_tag, m.end()) + len(end_tag)
    return start, end, content[start:end]


# ---------------------------------------------------------------------------
# Fix 1: Remove flex-wrap from tab container
# ---------------------------------------------------------------------------

def fix_tab_container(section):
    count = 0
    def _replace(m):
        nonlocal count
        count += 1
        return m.group(0).replace('flex flex-wrap items-center', 'flex items-center')
    result = re.sub(
        r'<div\s+class="flex flex-wrap items-center gap-2 mb-6"\s+role="tablist">',
        _replace, section
    )
    return result, count


# ---------------------------------------------------------------------------
# Fix 2: Tab button icons → fa6-solid:pencil
# ---------------------------------------------------------------------------

def fix_tab_icons(section):
    # Find the tablist region
    m = re.search(r'(role="tablist">)(.*?)(</div>)', section, re.DOTALL)
    if not m:
        return section, 0

    tablist = m.group(2)
    count = 0

    def _replace_icon(match):
        nonlocal count
        icon = match.group(1)
        if icon != 'fa6-solid:pencil':
            count += 1
            return 'data-icon="fa6-solid:pencil"'
        return match.group(0)

    # Only replace data-icon on text-[13px] spans inside tab buttons
    new_tablist = re.sub(
        r'(?<=text-\[13px\]" )data-icon="([^"]+)"',
        _replace_icon, tablist
    )
    return section[:m.start(2)] + new_tablist + section[m.end(2):], count


# ---------------------------------------------------------------------------
# Fix 3: Panel header icons → fa6-solid:pencil
# ---------------------------------------------------------------------------

def fix_panel_header_icons(section):
    count = 0

    def _replace(m):
        nonlocal count
        old_icon = m.group(1)
        if old_icon != 'fa6-solid:pencil':
            count += 1
            return m.group(0).replace(f'data-icon="{old_icon}"', 'data-icon="fa6-solid:pencil"')
        return m.group(0)

    # Match the icon inside panel header gradient boxes
    # Pattern: w-10 h-10 ... bg-gradient-to-br from-[#CB187D] ... <span ... data-icon="ICON">
    result = re.sub(
        r'w-10 h-10 rounded-xl bg-gradient-to-br from-\[#CB187D\] to-\[#e84aad\][^>]*>[\s\n]*<span class="iconify text-base" data-icon="([^"]+)"',
        _replace, section
    )
    return result, count


# ---------------------------------------------------------------------------
# Fix 4: Old accordion button → canonical simple button
# ---------------------------------------------------------------------------

def fix_accordion_buttons(section):
    """Replace old verbose accordion buttons that use 'Show Solution' with
    the canonical simple button format."""
    count = 0

    def _replace(m):
        nonlocal count
        count += 1
        # Detect indentation from the first line
        leading = m.group(1) or '      '
        # Normalize indentation (use detected leading whitespace)
        return (
            f'{leading}<button class="accordion-toggle w-full" onclick="toggleAccordion(this)">\n'
            f'{leading}  <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer\n'
            f'{leading}  <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>\n'
            f'{leading}</button>'
        )

    # Match any accordion-toggle button containing "Show Solution"
    # Handles all variants: different classes, different onclick, different icons
    result = re.sub(
        r'(\s*)<button\s+class="accordion-toggle[^"]*"[^>]*onclick="this\.nextElementSibling\.classList\.toggle\(\'open\'\)"[^>]*>.*?</button>',
        _replace, section, flags=re.DOTALL
    )
    return result, count


# ---------------------------------------------------------------------------
# Fix 5: accordion-body — remove mt-3 from class
# ---------------------------------------------------------------------------

def fix_accordion_body_mt(section):
    old = 'class="accordion-body mt-3"'
    new = 'class="accordion-body"'
    count = section.count(old)
    return section.replace(old, new), count


# ---------------------------------------------------------------------------
# Fix 6: Code block inside accordion — remove mt-1 / mt-3
# ---------------------------------------------------------------------------

def fix_code_block_mt(section):
    count = 0

    def _replace(m):
        nonlocal count
        count += 1
        return m.group(0).replace(m.group(1), '')

    # Remove mt-N from code blocks inside accordion bodies
    # Pattern: shadow-lg mt-N" inside accordion-body context
    result = re.sub(
        r'shadow-lg( mt-\d+)"',
        _replace, section
    )
    return result, count


# ---------------------------------------------------------------------------
# Fix 7: "Why this matters" tip → amber tip block
# ---------------------------------------------------------------------------

def fix_tip_paragraphs(section):
    count = 0

    def _replace(m):
        nonlocal count
        count += 1
        indent = m.group(1) or '        '
        text = m.group(2).strip()
        # Clean up: remove "Why this matters:" prefix and <strong> tags
        text = re.sub(r'^<strong[^>]*>Why this matters:?</strong>\s*', '', text)
        text = re.sub(r'^Why this matters:\s*', '', text, flags=re.IGNORECASE)
        # Capitalize first letter
        if text and text[0].islower():
            text = text[0].upper() + text[1:]
        return (
            f'{indent}<div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
            f'{indent}  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
            f'{indent}  <p class="text-sm text-gray-600">{text}</p>\n'
            f'{indent}</div>'
        )

    # Match various tip paragraph patterns:
    # 1. <p class="... italic">Why this matters: TEXT</p>
    # 2. <p class="..."><strong>Why this matters:</strong> TEXT</p>
    # 3. <p class="... text-gray-500 ...">Why this matters: TEXT</p>
    result = re.sub(
        r'(\s*)<p\s+class="[^"]*text-(?:xs|sm)[^"]*text-gray-(?:400|500|600)[^"]*"[^>]*>\s*(?:<strong[^>]*>)?\s*(?:Why this matters:?\s*)\s*(?:</strong>)?\s*(.*?)\s*</p>',
        _replace, section, flags=re.DOTALL
    )
    return result, count


# ---------------------------------------------------------------------------
# Fix 8: Task label — "Your Tasks" → "Your Task", mb-3 → mb-1
# ---------------------------------------------------------------------------

def fix_task_label(section):
    count = 0
    result = section

    # Fix label text
    tasks_plural = '>Your Tasks<'
    task_singular = '>Your Task<'
    c1 = result.count(tasks_plural)
    result = result.replace(tasks_plural, task_singular)
    count += c1

    # Fix margin on task label: mb-3 text-brand → mb-1 text-brand
    # (Only within task-box context — look for the specific pattern)
    old_margin = 'uppercase tracking-widest mb-3 text-brand'
    new_margin = 'uppercase tracking-widest mb-1 text-brand'
    c2 = result.count(old_margin)
    result = result.replace(old_margin, new_margin)
    count += c2

    return result, count


# ---------------------------------------------------------------------------
# Fix 9: Remove w-full from task inner div
# ---------------------------------------------------------------------------

def fix_task_wrapper(section):
    old = '<div class="w-full">'
    new = '<div>'
    count = section.count(old)
    return section.replace(old, new), count


# ---------------------------------------------------------------------------
# Fix 10: Inline code in task box — gray → pink canonical
# ---------------------------------------------------------------------------

def fix_inline_code_style(section):
    count = 0

    # Target inline <code> elements inside task-box areas
    # Various old patterns:
    #   font-mono text-xs bg-white px-1 py-0.5 rounded border border-gray-200
    #   font-mono bg-gray-100 px-1 rounded text-[11px]
    #   text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700
    #   font-mono text-xs bg-gray-100 px-1.5 py-0.5 rounded border border-gray-200

    canonical = 'font-mono text-[11px] bg-pink-50 text-[#CB187D] border border-pink-100 px-1 rounded'

    # Find task-box regions and fix code inside them
    # Strategy: find each task-box div, then fix <code> inside it

    def _fix_codes_in_taskbox(m):
        nonlocal count
        taskbox = m.group(0)

        def _fix_code_class(cm):
            nonlocal count
            old_class = cm.group(1)
            # Skip if already canonical
            if 'bg-pink-50' in old_class and 'text-[#CB187D]' in old_class:
                return cm.group(0)
            # Only replace if it's a styling class (has bg- or font-mono)
            if 'font-mono' in old_class or 'bg-' in old_class:
                count += 1
                return f'<code class="{canonical}">'
            return cm.group(0)

        return re.sub(r'<code class="([^"]+)">', _fix_code_class, taskbox)

    # Find task-box regions
    result = re.sub(
        r'<div[^>]*class="[^"]*task-box[^"]*"[^>]*>.*?</div>\s*</div>',
        _fix_codes_in_taskbox, section, flags=re.DOTALL
    )
    return result, count


# ---------------------------------------------------------------------------
# Fix 11: Remove wrapper <div> around accordion (L01, L10 pattern)
# ---------------------------------------------------------------------------

def fix_accordion_wrapper(section):
    """Remove the bare <div> wrapper around accordion button + body.
    Pattern: <div>\\n...button...\\n...accordion-body...\\n</div>
    Replace with just the button + accordion-body (unwrapped)."""
    count = 0

    # This pattern appears in L01, L10:
    # <div>
    #   <button class="accordion-toggle ...">...</button>
    #   <div class="accordion-body">...</div>
    # </div>
    #
    # We need to be careful to only remove the wrapper around accordions,
    # not other functional divs.
    #
    # Strategy: find a bare <div> followed by an accordion-toggle button
    # The bare <div> has no class attribute.

    def _replace(m):
        nonlocal count
        count += 1
        indent = m.group(1)
        inner = m.group(2)
        # Remove one level of indentation from inner content
        lines = inner.split('\n')
        dedented = []
        for line in lines:
            # Remove 2 spaces of indentation if present
            if line.startswith(indent + '  '):
                dedented.append(indent + line[len(indent) + 2:])
            else:
                dedented.append(line)
        return '\n'.join(dedented)

    result = re.sub(
        r'(\s*)<div>\s*\n((?:\s*<button class="accordion-toggle.*?</button>\s*\n)(?:\s*<div class="accordion-body.*?</div>\s*\n))\s*</div>',
        _replace, section, flags=re.DOTALL
    )
    return result, count


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_lesson(filepath):
    """Apply all fixes to a single lesson's practice section."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start, end, section = extract_practice(content)
    if section is None:
        return {'file': os.path.basename(filepath), 'status': 'NO_PRACTICE', 'fixes': {}}

    original = section
    fixes = {}

    # Apply fixes in order
    section, n = fix_tab_container(section);   fixes['tab_container_flex_wrap'] = n
    section, n = fix_tab_icons(section);        fixes['tab_icons'] = n
    section, n = fix_panel_header_icons(section); fixes['panel_header_icons'] = n
    section, n = fix_accordion_buttons(section); fixes['accordion_buttons'] = n
    section, n = fix_accordion_body_mt(section); fixes['accordion_body_mt'] = n
    section, n = fix_code_block_mt(section);    fixes['code_block_mt'] = n
    section, n = fix_tip_paragraphs(section);   fixes['tip_paragraphs'] = n
    section, n = fix_task_label(section);       fixes['task_label'] = n
    section, n = fix_task_wrapper(section);     fixes['task_wrapper'] = n
    section, n = fix_inline_code_style(section); fixes['inline_code'] = n

    total = sum(fixes.values())
    if total == 0:
        return {'file': os.path.basename(filepath), 'status': 'NO_CHANGES', 'fixes': fixes}

    # Replace practice section in content
    new_content = content[:start] + section + content[end:]

    # Validate div balance
    old_divs = len(re.findall(r'<div[\s>]', content)) - content.count('</div>')
    new_divs = len(re.findall(r'<div[\s>]', new_content)) - new_content.count('</div>')
    if old_divs != new_divs:
        return {
            'file': os.path.basename(filepath),
            'status': f'DIV_IMBALANCE (was {old_divs}, now {new_divs})',
            'fixes': fixes
        }

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return {'file': os.path.basename(filepath), 'status': 'PATCHED', 'fixes': fixes}


def main():
    print('=' * 80)
    print('PRACTICE SECTION FORMAT NORMALIZER — mod_04_data_engineering')
    print('=' * 80)

    results = []
    for lesson in LESSONS:
        filepath = os.path.join(LESSON_DIR, lesson)
        result = process_lesson(filepath)
        results.append(result)

    # Print results
    for r in results:
        status = r['status']
        icon = '✅' if status == 'PATCHED' else ('⏭️' if status == 'NO_CHANGES' else '⚠️')
        print(f"\n{icon} {r['file']}  [{status}]")
        if r['fixes']:
            active_fixes = {k: v for k, v in r['fixes'].items() if v > 0}
            if active_fixes:
                for fix_name, count in active_fixes.items():
                    print(f"   {fix_name}: {count}")

    # Summary
    patched = sum(1 for r in results if r['status'] == 'PATCHED')
    no_change = sum(1 for r in results if r['status'] == 'NO_CHANGES')
    errors = sum(1 for r in results if r['status'] not in ('PATCHED', 'NO_CHANGES', 'NO_PRACTICE'))

    print(f'\n{"=" * 80}')
    print(f'SUMMARY: {patched} patched, {no_change} unchanged, {errors} errors')
    print('=' * 80)


if __name__ == '__main__':
    main()
