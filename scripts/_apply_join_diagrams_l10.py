"""Insert #join-diagrams section between #key-concepts and #code-examples."""
from pathlib import Path

TARGET = Path(r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson10_advanced_joins.html')

# Reusable SVG diagram builders -------------------------------------------------
# Two overlapping circles (Venn). `mode` controls which regions are filled with brand pink.
#   - 'inner'    : intersection only
#   - 'left'     : left circle entire (intersection + left-only)
#   - 'right'    : right circle entire
#   - 'full'     : both circles entire
#   - 'left_excl': left circle only, intersection NOT filled (LEFT EXCLUSIVE — for completeness; not used here)
def venn(mode: str) -> str:
    PINK = "#CB187D"
    GRAY_FILL = "#f3f4f6"
    GRAY_STROKE = "#d1d5db"
    # Default: both circles unfilled (light gray)
    left_fill = GRAY_FILL
    right_fill = GRAY_FILL
    # Intersection is rendered as a clipped pink overlay on top
    intersection_pink = False
    if mode == 'inner':
        intersection_pink = True
    elif mode == 'left':
        left_fill = PINK
        intersection_pink = True  # whole left circle filled, including overlap
    elif mode == 'right':
        right_fill = PINK
        intersection_pink = True
    elif mode == 'full':
        left_fill = PINK
        right_fill = PINK
        intersection_pink = True
    # Build SVG
    overlay = ''
    if intersection_pink:
        # The intersection is the lens between cx=70,r=42 and cx=110,r=42 in viewBox 180x100
        # We clip a pink circle (right one) to the area inside left circle
        overlay = (
            '<defs><clipPath id="clip-{m}-l"><circle cx="70" cy="50" r="42"/></clipPath></defs>'
            '<circle cx="110" cy="50" r="42" fill="{p}" clip-path="url(#clip-{m}-l)" opacity="0.95"/>'
        ).format(m=mode, p=PINK)
    return (
        '<svg viewBox="0 0 180 100" xmlns="http://www.w3.org/2000/svg" class="w-full h-32">'
        f'<circle cx="70"  cy="50" r="42" fill="{left_fill}"  fill-opacity="0.85" stroke="{GRAY_STROKE}" stroke-width="1.5"/>'
        f'<circle cx="110" cy="50" r="42" fill="{right_fill}" fill-opacity="0.85" stroke="{GRAY_STROKE}" stroke-width="1.5"/>'
        f'{overlay}'
        '<text x="40"  y="95" font-family="Inter, sans-serif" font-size="9" font-weight="700" fill="#6b7280" text-anchor="middle">A (left)</text>'
        '<text x="140" y="95" font-family="Inter, sans-serif" font-size="9" font-weight="700" fill="#6b7280" text-anchor="middle">B (right)</text>'
        '</svg>'
    )

# SELF JOIN: single table with arrow looping back to itself
SELF_SVG = '''<svg viewBox="0 0 180 100" xmlns="http://www.w3.org/2000/svg" class="w-full h-32">
  <defs>
    <marker id="arrow-self" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#CB187D"/>
    </marker>
  </defs>
  <rect x="60" y="32" width="60" height="36" rx="6" fill="#CB187D" fill-opacity="0.85" stroke="#7F004C" stroke-width="1.5"/>
  <text x="90" y="55" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">employees</text>
  <path d="M 120 36 C 160 20, 160 80, 120 64" fill="none" stroke="#CB187D" stroke-width="2" marker-end="url(#arrow-self)"/>
  <text x="155" y="50" font-family="Inter, sans-serif" font-size="8" font-weight="600" fill="#6b7280" text-anchor="middle">e \u2194 m</text>
  <text x="90" y="92" font-family="Inter, sans-serif" font-size="9" font-weight="700" fill="#6b7280" text-anchor="middle">one table, two aliases</text>
</svg>'''

# CROSS JOIN: 3x3 grid of dots showing every-with-every pairing
CROSS_SVG = '''<svg viewBox="0 0 180 100" xmlns="http://www.w3.org/2000/svg" class="w-full h-32">
  <!-- left column dots (A) -->
  <circle cx="30" cy="30" r="6" fill="#CB187D"/>
  <circle cx="30" cy="55" r="6" fill="#CB187D"/>
  <circle cx="30" cy="80" r="6" fill="#CB187D"/>
  <!-- right column dots (B) -->
  <circle cx="150" cy="30" r="6" fill="#7F004C"/>
  <circle cx="150" cy="55" r="6" fill="#7F004C"/>
  <circle cx="150" cy="80" r="6" fill="#7F004C"/>
  <!-- every-with-every connections -->
  <g stroke="#CB187D" stroke-width="0.8" opacity="0.45">
    <line x1="30" y1="30" x2="150" y2="30"/>
    <line x1="30" y1="30" x2="150" y2="55"/>
    <line x1="30" y1="30" x2="150" y2="80"/>
    <line x1="30" y1="55" x2="150" y2="30"/>
    <line x1="30" y1="55" x2="150" y2="55"/>
    <line x1="30" y1="55" x2="150" y2="80"/>
    <line x1="30" y1="80" x2="150" y2="30"/>
    <line x1="30" y1="80" x2="150" y2="55"/>
    <line x1="30" y1="80" x2="150" y2="80"/>
  </g>
  <text x="30"  y="98" font-family="Inter, sans-serif" font-size="9" font-weight="700" fill="#6b7280" text-anchor="middle">A (3 rows)</text>
  <text x="150" y="98" font-family="Inter, sans-serif" font-size="9" font-weight="700" fill="#6b7280" text-anchor="middle">B (3 rows)</text>
  <text x="90"  y="18" font-family="Inter, sans-serif" font-size="10" font-weight="700" fill="#CB187D" text-anchor="middle">3 \u00d7 3 = 9 pairs</text>
</svg>'''

DIAGRAMS = [
    ('INNER JOIN',       'Only matched rows',   'Returns rows where the join key exists in <strong>both</strong> tables. Unmatched rows from either side are dropped.', venn('inner')),
    ('LEFT JOIN',        'Everything on the left', 'Returns every row from the <strong>left</strong> table, plus matched rows from the right. Unmatched right-side columns become <code class="text-[11px] font-mono px-1 rounded bg-gray-100">NULL</code>.', venn('left')),
    ('RIGHT JOIN',       'Everything on the right', 'Returns every row from the <strong>right</strong> table, plus matched rows from the left. The mirror image of LEFT JOIN.', venn('right')),
    ('FULL OUTER JOIN',  'Everything on both sides', 'Returns every row from both tables. Unmatched cells are filled with <code class="text-[11px] font-mono px-1 rounded bg-gray-100">NULL</code> on whichever side has no match.', venn('full')),
    ('SELF JOIN',        'A table joined to itself', 'A regular join where one table is given two aliases (e.g. <code class="text-[11px] font-mono px-1 rounded bg-gray-100">e</code> and <code class="text-[11px] font-mono px-1 rounded bg-gray-100">m</code>) so rows can be matched against other rows in the same table.', SELF_SVG),
    ('CROSS JOIN',       'Every row paired with every row', 'No <code class="text-[11px] font-mono px-1 rounded bg-gray-100">ON</code> clause. Returns the Cartesian product \u2014 every row in A paired with every row in B.', CROSS_SVG),
]

cards_html = []
for title, subtitle, body, svg in DIAGRAMS:
    cards_html.append(f'''        <div class="rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="px-5 pt-5 pb-3 bg-gradient-to-br from-[#fdf0f7]/40 via-white to-white border-b border-gray-100">
            <div class="flex items-center gap-2 mb-1">
              <span class="text-sm font-bold text-gray-900">{title}</span>
            </div>
            <p class="text-[11px] font-semibold uppercase tracking-widest text-brand">{subtitle}</p>
          </div>
          <div class="px-5 py-4 flex items-center justify-center bg-white">
            {svg}
          </div>
          <div class="px-5 pb-5">
            <p class="text-xs text-gray-600 leading-relaxed">{body}</p>
          </div>
        </div>''')

NEW_SECTION = '''

<section id="join-diagrams" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:diagram-project"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Join Diagrams</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A visual reference for how each join shapes the result set</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <p class="text-sm text-gray-600 leading-relaxed">Each diagram below shows two tables \u2014 <strong>A</strong> on the left and <strong>B</strong> on the right \u2014 and shades the area each join keeps. Use this as a quick reference whenever you are deciding which join type to reach for.</p>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
''' + '\n'.join(cards_html) + '''
      </div>

      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">The pink area shows what <strong>survives</strong> the join. Anything outside the pink is dropped from the result.</p>
      </div>

    </div>
  </div>
</section>

'''

content = TARGET.read_text(encoding='utf-8')
original_size = len(content)

# Insert NEW_SECTION just before <section id="code-examples">
anchor = '\n\n<section id="code-examples">'
if anchor not in content:
    raise RuntimeError("anchor not found")
if '<section id="join-diagrams"' in content:
    raise RuntimeError("section already exists")
content = content.replace(anchor, NEW_SECTION + '<section id="code-examples">', 1)

TARGET.write_text(content, encoding='utf-8')
print(f"Original: {original_size}")
print(f"New:      {len(content)}  (+{len(content)-original_size})")

# Validate div balance for new section
s1 = content.find('<section id="join-diagrams"')
s2 = content.find('</section>', s1) + len('</section>')
sec = content[s1:s2]
print(f"join-diagrams: {sec.count('<div')} open / {sec.count('</div>')} close")
print(f"join-diagrams: {sec.count('<svg')} svg blocks (expect 6)")
