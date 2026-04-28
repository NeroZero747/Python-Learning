"""Redesign the #join-diagrams section in lesson10 with a polished layout."""
from pathlib import Path
import re

TARGET = Path(r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations\lesson10_advanced_joins.html')

# --- SVG diagrams ----------------------------------------------------------
# Each SVG is 240x140, with shared <defs> placed inline (unique IDs per diagram).

def venn(uid, mode):
    """Polished Venn with gradient pink fill on the surviving regions."""
    GRAY = '#e5e7eb'
    GRAY_STROKE = '#cbd5e1'
    # Region fills: 'L' = left only, 'R' = right only, 'X' = intersection
    regions = {'L': GRAY, 'R': GRAY, 'X': GRAY}
    if mode == 'inner':
        regions['X'] = f'url(#g-{uid})'
    elif mode == 'left':
        regions['L'] = f'url(#g-{uid})'
        regions['X'] = f'url(#g-{uid})'
    elif mode == 'right':
        regions['R'] = f'url(#g-{uid})'
        regions['X'] = f'url(#g-{uid})'
    elif mode == 'full':
        regions['L'] = f'url(#g-{uid})'
        regions['R'] = f'url(#g-{uid})'
        regions['X'] = f'url(#g-{uid})'

    return f'''<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" class="w-full h-40" role="img" aria-label="Venn diagram for {mode} join">
  <defs>
    <linearGradient id="g-{uid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#CB187D"/>
      <stop offset="100%" stop-color="#e84aad"/>
    </linearGradient>
    <filter id="s-{uid}" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.08"/>
    </filter>
    <clipPath id="cl-{uid}-L"><circle cx="92"  cy="70" r="50"/></clipPath>
    <clipPath id="cl-{uid}-R"><circle cx="148" cy="70" r="50"/></clipPath>
  </defs>
  <g filter="url(#s-{uid})">
    <!-- Base fills: full L and R as gray, then overlay region fills -->
    <circle cx="92"  cy="70" r="50" fill="{GRAY}" stroke="{GRAY_STROKE}" stroke-width="1.5"/>
    <circle cx="148" cy="70" r="50" fill="{GRAY}" stroke="{GRAY_STROKE}" stroke-width="1.5"/>
    <!-- Left-only region (left circle minus right circle) -->
    <g clip-path="url(#cl-{uid}-L)">
      <rect x="0" y="0" width="240" height="140" fill="{regions['L']}"/>
      <circle cx="148" cy="70" r="50" fill="{GRAY}"/>
    </g>
    <!-- Right-only region -->
    <g clip-path="url(#cl-{uid}-R)">
      <rect x="0" y="0" width="240" height="140" fill="{regions['R']}"/>
      <circle cx="92" cy="70" r="50" fill="{GRAY}"/>
    </g>
    <!-- Intersection -->
    <g clip-path="url(#cl-{uid}-L)">
      <circle cx="148" cy="70" r="50" fill="{regions['X']}"/>
    </g>
    <!-- Outlines on top -->
    <circle cx="92"  cy="70" r="50" fill="none" stroke="{GRAY_STROKE}" stroke-width="1.5"/>
    <circle cx="148" cy="70" r="50" fill="none" stroke="{GRAY_STROKE}" stroke-width="1.5"/>
  </g>
  <!-- Labels -->
  <text x="60"  y="74" font-family="Inter, sans-serif" font-size="14" font-weight="800" fill="#374151" text-anchor="middle">A</text>
  <text x="180" y="74" font-family="Inter, sans-serif" font-size="14" font-weight="800" fill="#374151" text-anchor="middle">B</text>
  <text x="60"  y="135" font-family="Inter, sans-serif" font-size="9"  font-weight="600" fill="#9ca3af" text-anchor="middle">left table</text>
  <text x="180" y="135" font-family="Inter, sans-serif" font-size="9"  font-weight="600" fill="#9ca3af" text-anchor="middle">right table</text>
</svg>'''

SELF_SVG = '''<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" class="w-full h-40" role="img" aria-label="Self join diagram">
  <defs>
    <linearGradient id="g-self" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#CB187D"/>
      <stop offset="100%" stop-color="#e84aad"/>
    </linearGradient>
    <marker id="arrow-self" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#CB187D"/>
    </marker>
    <filter id="s-self" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.1"/>
    </filter>
  </defs>
  <g filter="url(#s-self)">
    <rect x="80" y="50" width="80" height="44" rx="10" fill="url(#g-self)"/>
  </g>
  <text x="120" y="77" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">employees</text>
  <!-- Loop arrow -->
  <path d="M 158 56 C 210 30, 210 114, 158 88" fill="none" stroke="#CB187D" stroke-width="2.5" marker-end="url(#arrow-self)"/>
  <!-- Alias pills -->
  <rect x="40" y="44" width="34" height="18" rx="9" fill="#fdf0f7" stroke="#f5c6e0"/>
  <text x="57" y="57" font-family="Fira Code, monospace" font-size="11" font-weight="700" fill="#CB187D" text-anchor="middle">e</text>
  <rect x="40" y="82" width="34" height="18" rx="9" fill="#fdf0f7" stroke="#f5c6e0"/>
  <text x="57" y="95" font-family="Fira Code, monospace" font-size="11" font-weight="700" fill="#CB187D" text-anchor="middle">m</text>
  <text x="120" y="20" font-family="Inter, sans-serif" font-size="10" font-weight="700" fill="#9ca3af" text-anchor="middle">one table, two aliases</text>
  <text x="200" y="74" font-family="Fira Code, monospace" font-size="10" font-weight="700" fill="#CB187D" text-anchor="middle">e \u2194 m</text>
</svg>'''

CROSS_SVG = '''<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg" class="w-full h-40" role="img" aria-label="Cross join diagram">
  <defs>
    <linearGradient id="g-cross" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#CB187D"/>
      <stop offset="100%" stop-color="#e84aad"/>
    </linearGradient>
  </defs>
  <!-- A column -->
  <text x="50" y="22" font-family="Inter, sans-serif" font-size="11" font-weight="800" fill="#374151" text-anchor="middle">A</text>
  <circle cx="50" cy="50" r="9" fill="url(#g-cross)"/>
  <circle cx="50" cy="80" r="9" fill="url(#g-cross)"/>
  <circle cx="50" cy="110" r="9" fill="url(#g-cross)"/>
  <!-- B column -->
  <text x="190" y="22" font-family="Inter, sans-serif" font-size="11" font-weight="800" fill="#374151" text-anchor="middle">B</text>
  <circle cx="190" cy="50" r="9" fill="#7F004C"/>
  <circle cx="190" cy="80" r="9" fill="#7F004C"/>
  <circle cx="190" cy="110" r="9" fill="#7F004C"/>
  <!-- All-with-all connection lines -->
  <g stroke="#CB187D" stroke-width="1" opacity="0.4">
    <line x1="50" y1="50"  x2="190" y2="50"/>
    <line x1="50" y1="50"  x2="190" y2="80"/>
    <line x1="50" y1="50"  x2="190" y2="110"/>
    <line x1="50" y1="80"  x2="190" y2="50"/>
    <line x1="50" y1="80"  x2="190" y2="80"/>
    <line x1="50" y1="80"  x2="190" y2="110"/>
    <line x1="50" y1="110" x2="190" y2="50"/>
    <line x1="50" y1="110" x2="190" y2="80"/>
    <line x1="50" y1="110" x2="190" y2="110"/>
  </g>
  <!-- Result badge -->
  <rect x="92" y="64" width="56" height="22" rx="11" fill="#ffffff" stroke="#f5c6e0" stroke-width="1.5"/>
  <text x="120" y="79" font-family="Fira Code, monospace" font-size="10" font-weight="700" fill="#CB187D" text-anchor="middle">3 \u00d7 3 = 9</text>
  <text x="120" y="135" font-family="Inter, sans-serif" font-size="9"  font-weight="600" fill="#9ca3af" text-anchor="middle">every row paired with every row</text>
</svg>'''

# --- Card data -------------------------------------------------------------
CARDS = [
    {
        'num': '01', 'name': 'INNER JOIN', 'tag': 'Intersection only',
        'syntax': 'INNER JOIN  \u2022  ON a.id = b.id',
        'result': 'Only rows that exist in <strong>both</strong> tables',
        'desc'  : 'Returns rows where the join key matches on both sides. Any row without a counterpart in the other table is dropped from the result.',
        'svg'   : venn('inner', 'inner'),
    },
    {
        'num': '02', 'name': 'LEFT JOIN', 'tag': 'Everything on the left',
        'syntax': 'LEFT JOIN  \u2022  ON a.id = b.id',
        'result': '<strong>Every row</strong> from A; matched columns from B',
        'desc'  : 'Keeps every row from the left table. When the right table has no match, its columns are filled with <code class="text-[11px] font-mono px-1 rounded bg-gray-100">NULL</code>.',
        'svg'   : venn('left', 'left'),
    },
    {
        'num': '03', 'name': 'RIGHT JOIN', 'tag': 'Everything on the right',
        'syntax': 'RIGHT JOIN  \u2022  ON a.id = b.id',
        'result': '<strong>Every row</strong> from B; matched columns from A',
        'desc'  : 'The mirror image of LEFT JOIN. Keeps every row from the right table; left-table columns become <code class="text-[11px] font-mono px-1 rounded bg-gray-100">NULL</code> when no match exists.',
        'svg'   : venn('right', 'right'),
    },
    {
        'num': '04', 'name': 'FULL OUTER JOIN', 'tag': 'Everything on both sides',
        'syntax': 'FULL OUTER JOIN  \u2022  ON a.id = b.id',
        'result': '<strong>Every row</strong> from both tables',
        'desc'  : 'Returns the union of LEFT and RIGHT JOIN. Unmatched cells on either side become <code class="text-[11px] font-mono px-1 rounded bg-gray-100">NULL</code> \u2014 ideal for full reconciliation work.',
        'svg'   : venn('full', 'full'),
    },
    {
        'num': '05', 'name': 'SELF JOIN', 'tag': 'A table joined to itself',
        'syntax': 'JOIN employees m  \u2022  ON e.manager_id = m.id',
        'result': 'Rows of one table matched against <strong>other rows</strong> of the same table',
        'desc'  : 'Not a separate join type \u2014 it is any join where the same table appears twice with different aliases. Used for hierarchies, comparisons, and pair-finding.',
        'svg'   : SELF_SVG,
    },
    {
        'num': '06', 'name': 'CROSS JOIN', 'tag': 'Every row paired with every row',
        'syntax': 'CROSS JOIN  \u2022  no ON clause',
        'result': 'The <strong>Cartesian product</strong> \u2014 every combination',
        'desc'  : 'No join key. Every row from A is paired with every row from B. Useful for grids, calendars, and seed data \u2014 dangerous on large tables.',
        'svg'   : CROSS_SVG,
    },
]

cards_html = []
for c in CARDS:
    cards_html.append(f'''        <div class="group relative rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm hover:shadow-lg hover:border-[#f5c6e0] hover:-translate-y-0.5 transition-all duration-300">
          <!-- Top accent strip -->
          <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>

          <!-- Card header -->
          <div class="relative px-5 pt-5 pb-3 overflow-hidden">
            <span class="absolute -right-2 -top-3 text-[4.5rem] font-black text-[#CB187D]/[0.05] leading-none select-none pointer-events-none">{c['num']}</span>
            <div class="relative">
              <p class="text-[10px] font-bold uppercase tracking-widest text-brand mb-1">{c['tag']}</p>
              <h3 class="text-base font-bold text-gray-900 leading-tight">{c['name']}</h3>
            </div>
          </div>

          <!-- Diagram -->
          <div class="px-5 py-3 flex items-center justify-center bg-gradient-to-b from-white to-gray-50/40">
            {c['svg']}
          </div>

          <!-- Syntax pill -->
          <div class="px-5 pt-2 pb-1">
            <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-[#1e1e2e] text-[10.5px] font-mono font-semibold text-pink-200 shadow-sm">
              <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span>
              {c['syntax']}
            </div>
          </div>

          <!-- Description -->
          <div class="px-5 pt-3 pb-4">
            <p class="text-xs text-gray-600 leading-relaxed">{c['desc']}</p>
          </div>

          <!-- Result footer -->
          <div class="flex items-start gap-2.5 px-5 py-3 border-t border-gray-100 bg-[#fdf0f7]/40">
            <span class="iconify text-brand text-sm shrink-0 mt-0.5" data-icon="fa6-solid:circle-check"></span>
            <p class="text-[11px] text-gray-700 leading-snug"><span class="font-semibold text-brand uppercase tracking-wider text-[10px]">Result &middot;</span> {c['result']}</p>
          </div>
        </div>''')

NEW_SECTION = '''<section id="join-diagrams" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
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

      <!-- Intro + legend banner -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-4 -top-6 text-[7rem] font-black text-[#CB187D]/[0.05] leading-none select-none pointer-events-none">\u2229</span>
        <div class="relative flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div class="flex items-start gap-4">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
              <span class="iconify text-base" data-icon="fa6-solid:circle-info"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-900">How to read these diagrams</p>
              <p class="text-xs text-gray-600 mt-1 leading-relaxed">Two tables \u2014 <strong>A</strong> on the left and <strong>B</strong> on the right. The shaded region is what the join <strong>keeps</strong>.</p>
            </div>
          </div>
          <div class="flex items-center gap-4 shrink-0 pl-14 sm:pl-0">
            <div class="flex items-center gap-2">
              <span class="inline-block w-4 h-4 rounded-full bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-sm"></span>
              <span class="text-[11px] font-semibold text-gray-700">Kept</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="inline-block w-4 h-4 rounded-full bg-gray-200 border border-gray-300"></span>
              <span class="text-[11px] font-semibold text-gray-500">Dropped</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Diagram grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
''' + '\n'.join(cards_html) + '''
      </div>

      <!-- Closing tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:lightbulb"></span>
        <p class="text-sm text-gray-600">Bookmark this page \u2014 most analysts revisit a chart like this for months until the join shapes are second nature. Pick the join whose <strong>kept</strong> region matches the rows you actually need in your output.</p>
      </div>

    </div>
  </div>
</section>'''

# --- Apply -----------------------------------------------------------------
content = TARGET.read_text(encoding='utf-8')
original_size = len(content)

# Replace the entire existing #join-diagrams section
pattern = re.compile(r'<section id="join-diagrams"[\s\S]*?</section>', re.MULTILINE)
matches = pattern.findall(content)
if len(matches) != 1:
    raise RuntimeError(f"Expected exactly 1 #join-diagrams section, found {len(matches)}")
content = pattern.sub(NEW_SECTION, content, count=1)

TARGET.write_text(content, encoding='utf-8')
print(f"Original: {original_size}")
print(f"New:      {len(content)}  ({len(content)-original_size:+d})")

# Validate
s1 = content.find('<section id="join-diagrams"')
s2 = content.find('</section>', s1) + len('</section>')
sec = content[s1:s2]
print(f"join-diagrams: {sec.count('<div')} open / {sec.count('</div>')} close")
print(f"join-diagrams: {sec.count('<svg')} svg blocks (expect 6)")
print(f"join-diagrams: {sec.count('group relative rounded-2xl')} cards (expect 6)")
