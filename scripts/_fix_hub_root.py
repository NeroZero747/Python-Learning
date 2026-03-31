import os

LESSON_DIR = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started/'

# ── CSS block to inject (mirrors the #hub-root isolation approach from the reference template) ──
HUB_ROOT_CSS = """
<style>
  /* ============================================================
     CONFLUENCE ISOLATION — scoped to #hub-root
     All rules use !important to beat Confluence's element styles.
     ============================================================ */

  #hub-root,
  #hub-root * {
    font-family: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif !important;
    box-sizing: border-box !important;
  }

  #hub-root {
    font-size: 16px !important;
    line-height: 1.6 !important;
    color: #1f2937 !important;
  }

  /* ── Code elements keep monospace ── */
  #hub-root code,
  #hub-root pre,
  #hub-root [class*="language-"] {
    font-family: 'Fira Code', ui-monospace, 'Cascadia Code', monospace !important;
  }

  /* ── Headings ── */
  #hub-root h1, #hub-root h2, #hub-root h3,
  #hub-root h4, #hub-root h5, #hub-root h6 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
    padding: 0 !important;
    line-height: 1.3 !important;
  }
  #hub-root h1 { font-size: 1.75rem  !important; font-weight: 700 !important; }
  #hub-root h2 { font-size: 1.25rem  !important; font-weight: 700 !important; }
  #hub-root h3 { font-size: 1rem     !important; font-weight: 600 !important; }
  #hub-root h4 { font-size: 0.875rem !important; font-weight: 600 !important; }
  #hub-root h5, #hub-root h6 { font-size: 0.8rem !important; font-weight: 600 !important; }

  /* ── Font weights (Tailwind class overrides) ── */
  #hub-root .font-black     { font-weight: 900 !important; }
  #hub-root .font-extrabold { font-weight: 800 !important; }
  #hub-root .font-bold      { font-weight: 700 !important; }
  #hub-root .font-semibold  { font-weight: 600 !important; }
  #hub-root .font-medium    { font-weight: 500 !important; }

  /* ── Font sizes (Tailwind class overrides) ── */
  #hub-root .text-4xl  { font-size: 2.25rem  !important; line-height: 2.5rem  !important; }
  #hub-root .text-3xl  { font-size: 1.875rem !important; line-height: 2.25rem !important; }
  #hub-root .text-2xl  { font-size: 1.5rem   !important; line-height: 2rem    !important; }
  #hub-root .text-xl   { font-size: 1.25rem  !important; line-height: 1.75rem !important; }
  #hub-root .text-lg   { font-size: 1.125rem !important; line-height: 1.75rem !important; }
  #hub-root .text-base { font-size: 1rem     !important; line-height: 1.5rem  !important; }
  #hub-root .text-sm   { font-size: 0.875rem !important; line-height: 1.25rem !important; }
  #hub-root .text-xs   { font-size: 0.75rem  !important; line-height: 1rem    !important; }

  /* ── Text colours ── */
  #hub-root .text-white    { color: #ffffff !important; }
  #hub-root .text-gray-900 { color: #111827 !important; }
  #hub-root .text-gray-800 { color: #1f2937 !important; }
  #hub-root .text-gray-700 { color: #374151 !important; }
  #hub-root .text-gray-600 { color: #4b5563 !important; }
  #hub-root .text-gray-500 { color: #6b7280 !important; }
  #hub-root .text-gray-400 { color: #9ca3af !important; }
  #hub-root .text-gray-300 { color: #d1d5db !important; }

  /* ── Layout utilities ── */
  #hub-root .flex            { display: flex !important; }
  #hub-root .inline-flex     { display: inline-flex !important; }
  #hub-root .items-center    { align-items: center !important; }
  #hub-root .items-start     { align-items: flex-start !important; }
  #hub-root .justify-center  { justify-content: center !important; }
  #hub-root .justify-between { justify-content: space-between !important; }
  #hub-root .shrink-0        { flex-shrink: 0 !important; }
  #hub-root .min-w-0         { min-width: 0 !important; }
  #hub-root .flex-1          { flex: 1 1 0% !important; }
  #hub-root .flex-wrap       { flex-wrap: wrap !important; }
  #hub-root .gap-1  { gap: 0.25rem !important; }
  #hub-root .gap-2  { gap: 0.5rem  !important; }
  #hub-root .gap-3  { gap: 0.75rem !important; }
  #hub-root .gap-4  { gap: 1rem    !important; }
  #hub-root .gap-6  { gap: 1.5rem  !important; }
  #hub-root .gap-8  { gap: 2rem    !important; }
  #hub-root .gap-10 { gap: 2.5rem  !important; }
  #hub-root .ml-auto { margin-left: auto !important; }

  /* ── Links ── */
  #hub-root a       { text-decoration: none !important; }
  #hub-root a:hover { text-decoration: none !important; }

  /* ── Iconify icon alignment ── */
  #hub-root .iconify {
    vertical-align: middle !important;
    flex-shrink: 0 !important;
  }
  #hub-root :not(.block) > .iconify:not(.block) {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
  }

  /* ── Hero title override (hero uses very large text-3xl/text-4xl) ── */
  #hub-root .hero-title-main {
    font-size: 2.25rem !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
  }
  @media (min-width: 768px) {
    #hub-root .hero-title-main { font-size: 2.5rem !important; }
  }

  /* ── Section header card titles ── */
  #hub-root .text-xl.font-bold,
  #hub-root h2.text-xl { font-size: 1.25rem !important; font-weight: 700 !important; }
</style>
"""

OLD_OUTER = '<div class="bg-gray-50 min-h-screen">'
NEW_OUTER = '<div id="hub-root" class="bg-gray-50 min-h-screen">'

# The marker right before the outer wrapper (matches lesson01 pattern — lessons 02-06 have no scroll-progress before)
STYLE_END_MARKER = '</style>\n'

files = sorted(f for f in os.listdir(LESSON_DIR) if f.endswith('.html'))

for filename in files:
    filepath = os.path.join(LESSON_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Add #hub-root id to outer wrapper (only if not already there)
    if OLD_OUTER in content and 'id="hub-root"' not in content:
        content = content.replace(OLD_OUTER, NEW_OUTER, 1)
        changed = True

    # 2. Inject the hub-root CSS block after the first </style> (only once)
    if 'CONFLUENCE ISOLATION' not in content:
        # Find the first </style> occurrence
        idx = content.find('</style>\n')
        if idx != -1:
            insert_at = idx + len('</style>\n')
            content = content[:insert_at] + HUB_ROOT_CSS + content[insert_at:]
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("FIXED  " + filename)
    else:
        print("SKIP   " + filename)
