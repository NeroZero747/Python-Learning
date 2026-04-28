"""Enhance #join-diagrams section with richer design: hero intro, sample data tables,
   full-width JOIN cards with diagram + result table side-by-side."""

FILE = 'pages/mod_06a_sql_foundation/mod_05_sql_foundations/lesson07_joining_tables_join.html'

NEW_SECTION = '''<!-- ─── How JOINs Work — Visual Guide (Venn diagrams + worked example) ─── -->
<section id="join-diagrams" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:diagram-project"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">How JOINs Work</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A picture &mdash; and a worked example &mdash; for every JOIN type.</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-7">

      <!-- ─── Hero intro card with hook analogy ─── -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">∩</span>
        <div class="relative flex items-start gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
            <span class="iconify text-base" data-icon="fa6-solid:circle-nodes"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">Picture each table as a circle. Where the circles overlap, rows match on the shared key. The shaded area is exactly what each JOIN returns.</p>
        </div>
      </div>

      <!-- ─── Sample data setup ─── -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3 flex items-center gap-2">
          <span class="iconify text-brand" data-icon="fa6-solid:table"></span> The Sample Data
        </p>
        <p class="text-sm text-gray-600 leading-relaxed mb-3">All five examples below use these two tiny tables. Notice that <strong>customer 4 has no order</strong> and <strong>order 104 has no matching customer</strong> &mdash; that is what makes the differences between JOIN types visible.</p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

          <!-- customers table -->
          <div class="rounded-xl border border-gray-100 overflow-hidden">
            <div class="flex items-center gap-2 px-3 py-2 bg-gray-50 border-b border-gray-100">
              <span class="iconify text-gray-500 text-xs" data-icon="fa6-solid:user"></span>
              <p class="text-[11px] font-bold text-gray-700 font-mono">customers</p>
            </div>
            <table class="w-full text-xs border-collapse bg-white">
              <thead>
                <tr class="border-b border-gray-100 bg-gray-50/40">
                  <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[11px]">customer_id</th>
                  <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[11px]">name</th>
                </tr>
              </thead>
              <tbody class="font-mono text-[11px]">
                <tr class="border-b border-gray-50"><td class="py-2 px-3 text-gray-700">1</td><td class="py-2 px-3 text-gray-700">Alice</td></tr>
                <tr class="border-b border-gray-50"><td class="py-2 px-3 text-gray-700">2</td><td class="py-2 px-3 text-gray-700">Ben</td></tr>
                <tr class="border-b border-gray-50"><td class="py-2 px-3 text-gray-700">3</td><td class="py-2 px-3 text-gray-700">Chen</td></tr>
                <tr><td class="py-2 px-3 text-gray-700">4</td><td class="py-2 px-3 text-gray-700">Dana</td></tr>
              </tbody>
            </table>
          </div>

          <!-- orders table -->
          <div class="rounded-xl border border-gray-100 overflow-hidden">
            <div class="flex items-center gap-2 px-3 py-2 bg-gray-50 border-b border-gray-100">
              <span class="iconify text-gray-500 text-xs" data-icon="fa6-solid:receipt"></span>
              <p class="text-[11px] font-bold text-gray-700 font-mono">orders</p>
            </div>
            <table class="w-full text-xs border-collapse bg-white">
              <thead>
                <tr class="border-b border-gray-100 bg-gray-50/40">
                  <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[11px]">order_id</th>
                  <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[11px]">customer_id</th>
                  <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[11px]">amount</th>
                </tr>
              </thead>
              <tbody class="font-mono text-[11px]">
                <tr class="border-b border-gray-50"><td class="py-2 px-3 text-gray-700">101</td><td class="py-2 px-3 text-gray-700">1</td><td class="py-2 px-3 text-gray-700">$50</td></tr>
                <tr class="border-b border-gray-50"><td class="py-2 px-3 text-gray-700">102</td><td class="py-2 px-3 text-gray-700">2</td><td class="py-2 px-3 text-gray-700">$75</td></tr>
                <tr class="border-b border-gray-50"><td class="py-2 px-3 text-gray-700">103</td><td class="py-2 px-3 text-gray-700">2</td><td class="py-2 px-3 text-gray-700">$30</td></tr>
                <tr><td class="py-2 px-3 text-gray-700">104</td><td class="py-2 px-3 text-gray-700">9</td><td class="py-2 px-3 text-gray-700">$20</td></tr>
              </tbody>
            </table>
          </div>

        </div>
      </div>

      <!-- ─── 5 JOIN cards (full-width stack) ─── -->
      <div class="space-y-5">

        ##INNER##

        ##LEFT##

        ##RIGHT##

        ##FULL##

        ##CROSS##

      </div>

      <!-- ─── Closing memory aid ─── -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-5 py-3 flex items-center gap-2.5">
          <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-sm" data-icon="fa6-solid:brain"></span>
          </span>
          <p class="text-xs font-bold uppercase tracking-widest text-white">Read JOINs Out Loud</p>
        </div>
        <div class="bg-white px-5 py-4">
          <ul class="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-2 text-xs text-gray-600 leading-relaxed list-none pl-0">
            <li class="flex items-start gap-2"><span class="inline-block w-2 h-2 rounded-full bg-[#CB187D] mt-1.5 shrink-0"></span><span><strong class="text-[#CB187D]">INNER</strong> &rarr; just the overlap</span></li>
            <li class="flex items-start gap-2"><span class="inline-block w-2 h-2 rounded-full bg-violet-500 mt-1.5 shrink-0"></span><span><strong class="text-violet-700">LEFT</strong> &rarr; whole left circle</span></li>
            <li class="flex items-start gap-2"><span class="inline-block w-2 h-2 rounded-full bg-blue-500 mt-1.5 shrink-0"></span><span><strong class="text-blue-700">RIGHT</strong> &rarr; whole right circle</span></li>
            <li class="flex items-start gap-2"><span class="inline-block w-2 h-2 rounded-full bg-emerald-500 mt-1.5 shrink-0"></span><span><strong class="text-emerald-700">FULL OUTER</strong> &rarr; both whole circles</span></li>
            <li class="flex items-start gap-2 sm:col-span-2"><span class="inline-block w-2 h-2 rounded-full bg-amber-500 mt-1.5 shrink-0"></span><span><strong class="text-amber-700">CROSS</strong> &rarr; the odd one out: no overlap rule, just every possible pair</span></li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</section>'''


def join_card(*, title, icon, accent_text, accent_bg, accent_border, accent_dark, gradient_from, gradient_to, gradient_mid,
              soft_bg_class, summary, svg_inner, result_caption, result_rows, footer):
    """Build a full-width JOIN card."""
    rows_html = ''
    for kind, c, n, oid, amt in result_rows:
        # kind: 'match' | 'left-only' | 'right-only'
        if kind == 'match':
            rows_html += f'<tr class="border-b border-gray-50"><td class="py-2 px-3 text-gray-700">{c}</td><td class="py-2 px-3 text-gray-700">{n}</td><td class="py-2 px-3 text-gray-700">{oid}</td><td class="py-2 px-3 text-gray-700">{amt}</td></tr>'
        elif kind == 'left-only':
            rows_html += f'<tr class="border-b border-gray-50 bg-{accent_text}-50/30"><td class="py-2 px-3 text-gray-700">{c}</td><td class="py-2 px-3 text-gray-700">{n}</td><td class="py-2 px-3 text-gray-400 italic">NULL</td><td class="py-2 px-3 text-gray-400 italic">NULL</td></tr>'
        elif kind == 'right-only':
            rows_html += f'<tr class="border-b border-gray-50 bg-{accent_text}-50/30"><td class="py-2 px-3 text-gray-400 italic">NULL</td><td class="py-2 px-3 text-gray-400 italic">NULL</td><td class="py-2 px-3 text-gray-700">{oid}</td><td class="py-2 px-3 text-gray-700">{amt}</td></tr>'

    return f'''<div class="rounded-2xl border border-{accent_text}-100 overflow-hidden shadow-sm bg-white">
          <div class="h-1 bg-gradient-to-r {gradient_from} {gradient_mid} {gradient_to}"></div>
          <div class="px-6 py-5 space-y-4 {soft_bg_class}">

            <!-- Card header -->
            <div class="flex items-center justify-between flex-wrap gap-3">
              <div class="flex items-center gap-3">
                <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br {gradient_from.replace("from-", "from-")} {gradient_to.replace("to-", "to-")} shadow-md shrink-0">
                  <span class="iconify text-white text-base" data-icon="{icon}"></span>
                </span>
                <div>
                  <h3 class="text-base font-bold text-gray-900 leading-tight">{title}</h3>
                  <p class="text-xs text-gray-500 leading-snug mt-0.5">{summary}</p>
                </div>
              </div>
            </div>

            <!-- Two-column body: diagram | result table -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 items-center">

              <!-- Diagram -->
              <div class="flex justify-center items-center bg-white rounded-xl border border-{accent_text}-100 px-4 py-5">
                {svg_inner}
              </div>

              <!-- Result table -->
              <div class="rounded-xl overflow-hidden border border-{accent_text}-100 bg-white">
                <div class="flex items-center gap-2 px-3 py-2 bg-{accent_text}-50 border-b border-{accent_text}-100">
                  <span class="iconify text-{accent_text}-600 text-xs" data-icon="fa6-solid:arrow-right-long"></span>
                  <p class="text-[10px] font-bold uppercase tracking-widest text-{accent_text}-700">{result_caption}</p>
                </div>
                <table class="w-full text-xs border-collapse">
                  <thead>
                    <tr class="border-b border-{accent_text}-100 bg-{accent_text}-50/40">
                      <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[10px]">cust_id</th>
                      <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[10px]">name</th>
                      <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[10px]">order_id</th>
                      <th class="py-2 px-3 text-left font-semibold text-gray-500 font-mono text-[10px]">amount</th>
                    </tr>
                  </thead>
                  <tbody class="font-mono text-[11px]">
                    {rows_html}
                  </tbody>
                </table>
              </div>

            </div>

            <!-- Footer explanation -->
            <p class="text-xs text-gray-600 leading-relaxed">{footer}</p>

          </div>
        </div>'''


# ─── SVG diagrams ──────────────────────────────────────────────────────────
SVG_INNER = '''<svg viewBox="0 0 260 160" class="w-full max-w-[260px] h-auto" xmlns="http://www.w3.org/2000/svg" aria-label="INNER JOIN Venn diagram">
                  <defs>
                    <clipPath id="vd-inner-clip"><circle cx="100" cy="80" r="60"/></clipPath>
                    <linearGradient id="vd-inner-grad" x1="0" y1="0" x2="1" y2="1">
                      <stop offset="0%" stop-color="#CB187D"/><stop offset="100%" stop-color="#e84aad"/>
                    </linearGradient>
                  </defs>
                  <circle cx="160" cy="80" r="60" fill="url(#vd-inner-grad)" fill-opacity="0.92" clip-path="url(#vd-inner-clip)"/>
                  <circle cx="100" cy="80" r="60" fill="none" stroke="#9ca3af" stroke-width="1.5"/>
                  <circle cx="160" cy="80" r="60" fill="none" stroke="#9ca3af" stroke-width="1.5"/>
                  <text x="55"  y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">customers</text>
                  <text x="205" y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">orders</text>
                </svg>'''

SVG_LEFT = '''<svg viewBox="0 0 260 160" class="w-full max-w-[260px] h-auto" xmlns="http://www.w3.org/2000/svg" aria-label="LEFT JOIN Venn diagram">
                  <defs>
                    <linearGradient id="vd-left-grad" x1="0" y1="0" x2="1" y2="1">
                      <stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#a855f7"/>
                    </linearGradient>
                  </defs>
                  <circle cx="100" cy="80" r="60" fill="url(#vd-left-grad)" fill-opacity="0.92"/>
                  <circle cx="160" cy="80" r="60" fill="none" stroke="#9ca3af" stroke-width="1.5"/>
                  <circle cx="100" cy="80" r="60" fill="none" stroke="#ffffff" stroke-width="1.5"/>
                  <text x="55"  y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">customers</text>
                  <text x="205" y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">orders</text>
                </svg>'''

SVG_RIGHT = '''<svg viewBox="0 0 260 160" class="w-full max-w-[260px] h-auto" xmlns="http://www.w3.org/2000/svg" aria-label="RIGHT JOIN Venn diagram">
                  <defs>
                    <linearGradient id="vd-right-grad" x1="0" y1="0" x2="1" y2="1">
                      <stop offset="0%" stop-color="#2563eb"/><stop offset="100%" stop-color="#6366f1"/>
                    </linearGradient>
                  </defs>
                  <circle cx="160" cy="80" r="60" fill="url(#vd-right-grad)" fill-opacity="0.92"/>
                  <circle cx="100" cy="80" r="60" fill="none" stroke="#9ca3af" stroke-width="1.5"/>
                  <circle cx="160" cy="80" r="60" fill="none" stroke="#ffffff" stroke-width="1.5"/>
                  <text x="55"  y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">customers</text>
                  <text x="205" y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">orders</text>
                </svg>'''

SVG_FULL = '''<svg viewBox="0 0 260 160" class="w-full max-w-[260px] h-auto" xmlns="http://www.w3.org/2000/svg" aria-label="FULL OUTER JOIN Venn diagram">
                  <defs>
                    <linearGradient id="vd-full-grad" x1="0" y1="0" x2="1" y2="1">
                      <stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#14b8a6"/>
                    </linearGradient>
                  </defs>
                  <circle cx="100" cy="80" r="60" fill="url(#vd-full-grad)" fill-opacity="0.92"/>
                  <circle cx="160" cy="80" r="60" fill="url(#vd-full-grad)" fill-opacity="0.92"/>
                  <circle cx="100" cy="80" r="60" fill="none" stroke="#ffffff" stroke-width="1.5"/>
                  <circle cx="160" cy="80" r="60" fill="none" stroke="#ffffff" stroke-width="1.5"/>
                  <text x="55"  y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">customers</text>
                  <text x="205" y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">orders</text>
                </svg>'''

SVG_CROSS = '''<svg viewBox="0 0 260 160" class="w-full max-w-[260px] h-auto" xmlns="http://www.w3.org/2000/svg" aria-label="CROSS JOIN grid diagram">
                  <defs>
                    <linearGradient id="vd-cross-line" x1="0" y1="0" x2="1" y2="0">
                      <stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#f59e0b"/>
                    </linearGradient>
                  </defs>
                  <g stroke="url(#vd-cross-line)" stroke-width="1.2" stroke-opacity="0.55">
                    <line x1="50" y1="40" x2="210" y2="25"/>
                    <line x1="50" y1="40" x2="210" y2="60"/>
                    <line x1="50" y1="40" x2="210" y2="95"/>
                    <line x1="50" y1="40" x2="210" y2="130"/>
                    <line x1="50" y1="80" x2="210" y2="25"/>
                    <line x1="50" y1="80" x2="210" y2="60"/>
                    <line x1="50" y1="80" x2="210" y2="95"/>
                    <line x1="50" y1="80" x2="210" y2="130"/>
                    <line x1="50" y1="120" x2="210" y2="25"/>
                    <line x1="50" y1="120" x2="210" y2="60"/>
                    <line x1="50" y1="120" x2="210" y2="95"/>
                    <line x1="50" y1="120" x2="210" y2="130"/>
                  </g>
                  <circle cx="50"  cy="40"  r="8" fill="#d97706"/>
                  <circle cx="50"  cy="80"  r="8" fill="#d97706"/>
                  <circle cx="50"  cy="120" r="8" fill="#d97706"/>
                  <circle cx="210" cy="25"  r="8" fill="#f59e0b"/>
                  <circle cx="210" cy="60"  r="8" fill="#f59e0b"/>
                  <circle cx="210" cy="95"  r="8" fill="#f59e0b"/>
                  <circle cx="210" cy="130" r="8" fill="#f59e0b"/>
                  <text x="50"  y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">customers (3)</text>
                  <text x="210" y="155" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#6b7280">products (4)</text>
                </svg>'''


# ─── Build each JOIN card ──────────────────────────────────────────────────
INNER = join_card(
    title='INNER JOIN',
    icon='fa6-solid:link',
    accent_text='pink', accent_bg='pink-50', accent_border='pink-100', accent_dark='[#CB187D]',
    gradient_from='from-[#CB187D]', gradient_mid='via-pink-400', gradient_to='to-rose-300',
    soft_bg_class='bg-gradient-to-br from-pink-50/30 to-white',
    summary='Returns only rows that exist in BOTH tables &mdash; the overlap.',
    svg_inner=SVG_INNER,
    result_caption='3 rows returned',
    result_rows=[
        ('match', '1', 'Alice', '101', '$50'),
        ('match', '2', 'Ben',   '102', '$75'),
        ('match', '2', 'Ben',   '103', '$30'),
    ],
    footer='Customer 3 (Chen) and customer 4 (Dana) are dropped because they have no orders. Order 104 is dropped because customer 9 does not exist. Only the three rows that match on <code class="bg-pink-100 border border-pink-200 text-[#CB187D] px-1 rounded font-mono text-[11px]">customer_id</code> survive.'
)

LEFT = join_card(
    title='LEFT JOIN',
    icon='fa6-solid:code-compare',
    accent_text='violet', accent_bg='violet-50', accent_border='violet-100', accent_dark='violet-700',
    gradient_from='from-violet-500', gradient_mid='via-purple-400', gradient_to='to-fuchsia-300',
    soft_bg_class='bg-gradient-to-br from-violet-50/30 to-white',
    summary='Keeps every row from the LEFT table; right-side gaps become NULL.',
    svg_inner=SVG_LEFT,
    result_caption='5 rows returned',
    result_rows=[
        ('match',     '1', 'Alice', '101', '$50'),
        ('match',     '2', 'Ben',   '102', '$75'),
        ('match',     '2', 'Ben',   '103', '$30'),
        ('left-only', '3', 'Chen',  '',    ''),
        ('left-only', '4', 'Dana',  '',    ''),
    ],
    footer='Every customer is kept &mdash; even Chen and Dana, who have no orders. Their order columns return <code class="bg-violet-100 border border-violet-200 text-violet-700 px-1 rounded font-mono text-[11px]">NULL</code>. Order 104 is still dropped because customer 9 does not exist on the left side.'
)

RIGHT = join_card(
    title='RIGHT JOIN',
    icon='fa6-solid:arrow-right-to-bracket',
    accent_text='blue', accent_bg='blue-50', accent_border='blue-100', accent_dark='blue-700',
    gradient_from='from-blue-500', gradient_mid='via-cyan-400', gradient_to='to-teal-300',
    soft_bg_class='bg-gradient-to-br from-blue-50/30 to-white',
    summary='Keeps every row from the RIGHT table; left-side gaps become NULL.',
    svg_inner=SVG_RIGHT,
    result_caption='4 rows returned',
    result_rows=[
        ('match',      '1', 'Alice', '101', '$50'),
        ('match',      '2', 'Ben',   '102', '$75'),
        ('match',      '2', 'Ben',   '103', '$30'),
        ('right-only', '',  '',      '104', '$20'),
    ],
    footer='Every order is kept &mdash; even order 104, whose customer 9 does not exist. Its customer columns return <code class="bg-blue-100 border border-blue-200 text-blue-700 px-1 rounded font-mono text-[11px]">NULL</code>. Customers Chen and Dana are dropped because they have no orders on the right side.'
)

FULL = join_card(
    title='FULL OUTER JOIN',
    icon='fa6-solid:circle-dot',
    accent_text='emerald', accent_bg='emerald-50', accent_border='emerald-100', accent_dark='emerald-700',
    gradient_from='from-emerald-500', gradient_mid='via-teal-400', gradient_to='to-cyan-300',
    soft_bg_class='bg-gradient-to-br from-emerald-50/30 to-white',
    summary='Keeps every row from BOTH tables; unmatched columns on either side become NULL.',
    svg_inner=SVG_FULL,
    result_caption='6 rows returned',
    result_rows=[
        ('match',      '1', 'Alice', '101', '$50'),
        ('match',      '2', 'Ben',   '102', '$75'),
        ('match',      '2', 'Ben',   '103', '$30'),
        ('left-only',  '3', 'Chen',  '',    ''),
        ('left-only',  '4', 'Dana',  '',    ''),
        ('right-only', '',  '',      '104', '$20'),
    ],
    footer='Nothing is dropped. The result is the union of LEFT JOIN and RIGHT JOIN &mdash; matched rows in the middle, unmatched left rows with right-side <code class="bg-emerald-100 border border-emerald-200 text-emerald-700 px-1 rounded font-mono text-[11px]">NULL</code>s, and unmatched right rows with left-side <code class="bg-emerald-100 border border-emerald-200 text-emerald-700 px-1 rounded font-mono text-[11px]">NULL</code>s.'
)

CROSS = join_card(
    title='CROSS JOIN',
    icon='fa6-solid:xmark',
    accent_text='amber', accent_bg='amber-50', accent_border='amber-100', accent_dark='amber-700',
    gradient_from='from-amber-500', gradient_mid='via-orange-400', gradient_to='to-red-300',
    soft_bg_class='bg-gradient-to-br from-amber-50/30 to-white',
    summary='Pairs every row from one table with every row from the other &mdash; no ON clause.',
    svg_inner=SVG_CROSS,
    result_caption='3 &times; 4 = 12 rows returned',
    result_rows=[
        ('match', '1', 'Alice', 'P-A', 'Mug'),
        ('match', '1', 'Alice', 'P-B', 'Hat'),
        ('match', '1', 'Alice', '...', '...'),
        ('match', '2', 'Ben',   'P-A', 'Mug'),
        ('match', '2', 'Ben',   '...', '...'),
        ('match', '3', 'Chen',  '...', '...'),
    ],
    footer='Different example: 3 customers &times; 4 products = 12 combinations. There is no <code class="bg-amber-100 border border-amber-200 text-amber-700 px-1 rounded font-mono text-[11px]">ON</code> clause and no concept of matching &mdash; every left row is paired with every right row. Be careful: 1,000 &times; 1,000 = 1,000,000 rows.'
)

NEW_SECTION = (NEW_SECTION
               .replace('##INNER##', INNER)
               .replace('##LEFT##', LEFT)
               .replace('##RIGHT##', RIGHT)
               .replace('##FULL##', FULL)
               .replace('##CROSS##', CROSS))

# ─── Replace existing section ──────────────────────────────────────────────
with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- ─── How JOINs Work — Visual Guide'
start = content.find(start_marker)
if start == -1:
    # Fallback: find by section id
    start = content.find('<section id="join-diagrams"')

end = content.find('\n<section id="code-examples">', start)
if start == -1 or end == -1:
    print("ERROR: Could not find section boundaries")
    exit(1)

old_section = content[start:end]
print(f"Old section: {len(old_section)} chars")

new_content = content[:start] + NEW_SECTION + content[end:]

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
with open(FILE, 'r', encoding='utf-8') as f:
    verify = f.read()

js = verify[verify.find('<section id="join-diagrams"'):verify.find('\n<section id="code-examples">')]
print(f"\n✅ New section: {len(js)} chars")
print(f"   <svg> count: {js.count('<svg ')} (should be 5)")
needle = 'h3 class="text-base font-bold'
print(f"   JOIN cards: {js.count(needle)} (should be 5)")
print(f"   Result tables: {js.count('rows returned')} (should be 5)")
n1 = 'font-mono">customers'
n2 = 'font-mono">orders'
print(f"   Sample data tables found: {js.count(n1)+js.count(n2)} (should be >=2)")
