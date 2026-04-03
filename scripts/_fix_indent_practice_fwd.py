"""
Re-indent the inner content of sections from #practice through #next-lesson
(plus bottom nav) in lesson10.

Strategy:
  - Read the file.
  - Isolate the block from line containing '<section id="practice">' through
    the '</section>      </main>' closing line.
  - Re-indent every HTML line by tracking open/close tag depth from the
    section boundary inward, using 2-space increments.
  - Preserve whitespace inside <pre> blocks verbatim.
  - Write the file back.
"""

import re, pathlib

FILE = pathlib.Path(
    r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_03_python_for_data_analysts"
    r"\lesson10_writing_to_databases_and_managing_credentials.html"
)

# ── helpers ──────────────────────────────────────────────────

VOID = {"br", "hr", "img", "input", "meta", "link", "col", "area", "base",
        "embed", "source", "track", "wbr", "param"}

def _count_opens(line):
    """Count opening tags (excluding self-closing and void)."""
    n = 0
    for m in re.finditer(r"<(\w[\w-]*)(?:\s[^>]*)?>", line):
        tag = m.group(1).lower()
        full = m.group(0)
        if tag in VOID:
            continue
        if full.endswith("/>"):
            continue
        n += 1
    return n

def _count_closes(line):
    """Count closing tags."""
    return len(re.findall(r"</(\w[\w-]*)>", line))


def reindent_block(lines, base_indent):
    """
    Re-indent a list of HTML lines starting at *base_indent* spaces.
    Returns a new list of strings (no trailing newlines).
    Preserves content inside <pre> verbatim.
    """
    out = []
    depth = 0          # nesting depth relative to base
    in_pre = False     # inside a <pre> block
    pre_collect = []   # raw lines inside <pre>

    for raw in lines:
        stripped = raw.strip()

        # ── handle <pre> blocks ──────────────────────────────
        if in_pre:
            pre_collect.append(raw.rstrip("\n"))
            if "</pre>" in stripped:
                # emit collected pre block with current indent on first/last
                # but preserve inner lines exactly
                for pl in pre_collect:
                    out.append(pl)
                pre_collect = []
                in_pre = False
            continue

        if "<pre" in stripped and "</pre>" not in stripped:
            # opening pre without close on same line
            indent = " " * (base_indent + depth * 2)
            out.append(indent + stripped)
            in_pre = True
            pre_collect = []
            continue

        if not stripped:
            out.append("")
            continue

        # ── compute depth change ─────────────────────────────
        opens = _count_opens(stripped)
        closes = _count_closes(stripped)

        # Lines that start with a closing tag get outdented first
        if stripped.startswith("</"):
            depth -= closes
            closes = 0           # already accounted for
            if depth < 0:
                depth = 0

        indent = " " * (base_indent + depth * 2)
        out.append(indent + stripped)

        depth += opens - closes
        if depth < 0:
            depth = 0

    return out


# ── main ─────────────────────────────────────────────────────

text = FILE.read_text(encoding="utf-8")
lines = text.split("\n")

# Find boundaries
start_idx = None   # index of '<section id="practice">' line
end_idx = None     # index of '</section>      </main>' line

for i, ln in enumerate(lines):
    if '<section id="practice">' in ln and start_idx is None:
        start_idx = i
    if "</section>" in ln and "</main>" in ln:
        end_idx = i

assert start_idx is not None, "Could not find #practice"
assert end_idx is not None, "Could not find </section></main>"

# The block to re-indent: from #practice through the </section></main> line.
# We will NOT include the </main> closing itself; split it out.
block = lines[start_idx : end_idx]  # excludes end_idx line
after = lines[end_idx:]              # includes end_idx line

# We re-indent the block.  Sections sit at 8 spaces (inside <main> at 6).
# But in this file the convention from #overview onward is 0-indent sections.
# Let's keep sections at 0 and indent their content at +2 per level.

reindented = reindent_block(block, base_indent=0)

# Reassemble
new_lines = lines[:start_idx] + reindented + after
new_text = "\n".join(new_lines)

FILE.write_text(new_text, encoding="utf-8")
print(f"✅  Re-indented lines {start_idx+1}–{end_idx} ({len(reindented)} lines)")
print(f"    Total file: {len(new_lines)} lines")
