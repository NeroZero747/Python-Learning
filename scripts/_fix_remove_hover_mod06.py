"""Remove all :hover effects from lesson*.html files in mod_06_sql_foundation,
except .lesson-nav-link:hover (bottom nav) and inline group-hover: classes."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_DIR = ROOT / "pages" / "mod_06_sql_foundation"
FILES = sorted(TARGET_DIR.glob("lesson*.html"))


def parse_css_blocks(css):
    blocks = []
    i, n = 0, len(css)
    while i < n:
        brace = css.find('{', i)
        if brace == -1:
            blocks.append(('tail', css[i:], '')); break
        sel = css[i:brace]
        depth, j = 1, brace + 1
        while j < n and depth > 0:
            if css[j] == '{': depth += 1
            elif css[j] == '}': depth -= 1
            j += 1
        blocks.append(('rule', sel, css[brace+1:j-1]))
        i = j
    return blocks


def strip_css_hover(css):
    out = []
    for kind, sel, body in parse_css_blocks(css):
        if kind == 'tail':
            out.append(sel); continue
        sel_stripped = sel.strip()
        if sel_stripped.startswith('@'):
            new_body = strip_css_hover(body)
            if new_body.strip():
                out.append(f"{sel}{{{new_body}}}")
            # else: drop empty @-rule
        elif ':hover' in sel:
            if 'lesson-nav-link' in sel:
                out.append(f"{sel}{{{body}}}")
            # else: drop
        else:
            out.append(f"{sel}{{{body}}}")
    return ''.join(out)


def clean_class_attr(m):
    val = m.group(1)
    if 'hover:' not in val:
        return m.group(0)
    val = re.sub(r'(?<!-)hover:\S+', '', val)
    val = re.sub(r' +', ' ', val).strip()
    return f'class="{val}"'


def process(text):
    # Op 1: strip CSS :hover rules inside <style> blocks
    def style_repl(m):
        return f"<style>{strip_css_hover(m.group(1))}</style>"
    text = re.sub(r'<style>([\s\S]*?)</style>', style_repl, text)

    # Op 2: strip inline Tailwind hover: classes
    text = re.sub(r'class="([^"]*)"', clean_class_attr, text)

    # Op 3: targeted removal of .obj-card:hover inside @media print
    text = text.replace(
        '      .obj-card:hover { transform: none; box-shadow: none; }\n',
        ''
    )
    text = re.sub(
        r'(\.hero-container \{ display: none; \})\s*\.obj-card:hover \{ transform: none; box-shadow: none; \}\s*(\})',
        r'\1 \2',
        text
    )

    # Op 4: collapse 3+ blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def main():
    for f in FILES:
        original = f.read_text(encoding='utf-8')
        new = process(original)
        if new == original:
            print(f"⚠️  {f.name}: no changes")
        else:
            f.write_text(new, encoding='utf-8')
            delta = len(new) - len(original)
            print(f"✅ {f.name} ({delta:+d} chars)")


if __name__ == '__main__':
    main()
