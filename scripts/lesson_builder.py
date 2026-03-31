"""
Python Learning Hub — Lesson Builder
=====================================
Extracts boilerplate (CSS, JS, hero SVG) from docs/new_lesson_template.html at
runtime so generator scripts only need to define lesson-specific content.

Usage in a generator script:
    from scripts.lesson_builder import *   # or adjust sys.path as needed
    # … define section HTML strings …
    write_lesson(OUTPUT, [cdn_head(), style_block(), fixed_chrome(),
                          hub_root_open(), build_hero(…), layout_open(),
                          build_toc(…), main_open(),
                          obj_html, overview_html, …,  # content sections
                          main_close(), layout_close(), hub_root_close(),
                          script_block()])
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATE = ROOT / "docs" / "new_lesson_template.html"


# ── Template extraction ────────────────────────────────────────────────────────

def _t() -> str:
    return TEMPLATE.read_text(encoding="utf-8")


def cdn_head() -> str:
    """CDN <link>/<script> tags from the template header (before <style>)."""
    html = _t()
    m = re.search(r'(<!--\n  ╔.*?╝\n-->.*?)\s*\n\s*<style>', html, re.DOTALL)
    if m:
        return m.group(1).strip()
    # fallback: grab from first <link> up to <style>
    m = re.search(r'(<link rel="preconnect".*?)\s*\n\s*<style>', html, re.DOTALL)
    return m.group(1).strip() if m else ""


def style_block() -> str:
    """Complete <style>…</style> block from the template."""
    m = re.search(r'(<style>.*?</style>)', _t(), re.DOTALL)
    return m.group(1) if m else ""


def script_block() -> str:
    """The final <script>…</script> from the template footer (all JS functions)."""
    matches = list(re.finditer(r'(<script>.*?</script>)', _t(), re.DOTALL))
    return matches[-1].group(1) if matches else ""


def hero_svg() -> str:
    """The full hero <svg> element from the template."""
    m = re.search(r'(<svg viewBox="0 0 280 324".*?</svg>)', _t(), re.DOTALL)
    return m.group(1) if m else ""


# ── Fixed structural chrome ────────────────────────────────────────────────────

def fixed_chrome() -> str:
    """Scroll-progress bar + back-to-top button (always identical)."""
    return (
        '\n<!-- Scroll progress bar -->\n'
        '<div class="scroll-progress" id="scroll-progress"></div>\n\n'
        '<!-- Back to top -->\n'
        '<button class="back-to-top" id="back-to-top" '
        'onclick="window.scrollTo({top:0,behavior:\'smooth\'})">\n'
        '  <span class="iconify text-lg" data-icon="fa6-solid:arrow-up"></span>\n'
        '</button>\n'
    )


def hub_root_open() -> str:
    return '\n<div id="hub-root" class="bg-gray-50 min-h-screen">\n'


def hub_root_close() -> str:
    return '\n</div>\n'


def layout_open() -> str:
    return (
        '\n  <!-- ═══ MAIN LAYOUT ═══ -->\n'
        '  <div class="max-w-[1280px] mx-auto px-4 pt-8 pb-12">\n'
        '    <div class="lesson-layout">\n'
    )


def layout_close() -> str:
    return '    </div>\n  </div>\n'


def main_open() -> str:
    return (
        '\n      <!-- ═══ MAIN CONTENT ═══ -->\n'
        '      <main class="min-w-0 flex-1 space-y-10">\n'
    )


def main_close() -> str:
    return '      </main>\n'


# ── Hero banner builder ────────────────────────────────────────────────────────

def build_hero(
    lesson_num: str,        # e.g. "02"
    title: str,
    subtitle: str,
    module_label: str,      # e.g. "Module 2"
    difficulty: str,        # "Beginner" | "Intermediate" | "Advanced"
    n_goals: int = 4,
    n_examples: int = 3,
    n_exercises: int = 3,
    progress: str = "2/9",  # shown as "2/9" in the pill
) -> str:
    dots = {
        "Beginner": (
            '<span class="skill-dot skill-dot-active"></span>'
            '<span class="skill-dot"></span>'
            '<span class="skill-dot"></span>'
        ),
        "Intermediate": (
            '<span class="skill-dot skill-dot-active"></span>'
            '<span class="skill-dot skill-dot-active"></span>'
            '<span class="skill-dot"></span>'
        ),
        "Advanced": (
            '<span class="skill-dot skill-dot-active"></span>'
            '<span class="skill-dot skill-dot-active"></span>'
            '<span class="skill-dot skill-dot-active"></span>'
        ),
    }.get(difficulty, '<span class="skill-dot skill-dot-active"></span>'
                      '<span class="skill-dot"></span>'
                      '<span class="skill-dot"></span>')

    prog_num, prog_total = (progress.split("/") + ["?"])[:2]
    svg = hero_svg()

    return f"""
  <!-- ═══ HERO BANNER ═══ -->
  <div class="max-w-[1280px] mx-auto px-4 pt-5 pb-0">
    <section class="hero-container">
      <div class="hero-dots"></div>
      <div class="hero-glow hero-glow-1"></div>
      <div class="hero-glow hero-glow-2"></div>
      <div class="hero-glow-line"></div>
      <div class="relative z-10 px-8 py-8 md:px-12 md:py-10">
        <div class="hero-split flex flex-col md:flex-row items-center gap-6 md:gap-10">
          <div class="flex-1 min-w-0">
            <div class="flex flex-wrap items-center gap-2 mb-4">
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-solid:rocket"></span> {module_label}
              </span>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="inline-flex items-center gap-1">{dots}</span> {difficulty}
              </span>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> 6 min read
              </span>
            </div>
            <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson {lesson_num}</p>
            <h1 class="hero-title-main text-3xl md:text-4xl font-extrabold text-white mb-8 leading-[1.15] tracking-tight">
              {title}
            </h1>
            <p class="text-white/80 text-sm md:text-base leading-relaxed mb-4 max-w-lg">
              {subtitle}
            </p>
            <div class="flex items-center gap-4 mb-5 text-sm">
              <div class="flex items-center gap-2">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
                  <span class="iconify text-white text-[10px]" data-icon="fa6-solid:user"></span>
                </span>
                <span class="text-white/85 font-medium text-xs">Python Learning Hub</span>
              </div>
              <span class="text-white/30">|</span>
              <div class="flex items-center gap-2">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
                  <span class="iconify text-white text-[10px]" data-icon="fa6-regular:calendar"></span>
                </span>
                <span class="text-white/85 font-medium text-xs">March 24, 2026</span>
              </div>
            </div>
            <div class="flex items-center gap-2 flex-wrap mb-0">
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-solid:bullseye"></span>
                <span class="font-extrabold">{n_goals}</span>
                <span class="font-semibold opacity-55">Goals</span>
              </span>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span>
                <span class="font-extrabold">{n_examples}</span>
                <span class="font-semibold opacity-55">Examples</span>
              </span>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell"></span>
                <span class="font-extrabold">{n_exercises}</span>
                <span class="font-semibold opacity-55">Exercises</span>
              </span>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-solid:layer-group"></span>
                <span class="font-extrabold">{prog_num}<span class="font-bold opacity-50">/{prog_total}</span></span>
                <span class="font-semibold opacity-55">Progress</span>
              </span>
            </div>
          </div>
          <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
            <div class="hero-abstract-card">
              {svg}
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
"""


# ── TOC sidebar builder ────────────────────────────────────────────────────────

def build_toc(
    toc_items: list,        # [(href, iconify_icon, label), …]
    module_lessons: list,   # [(href, display_label), …]
    current_lesson_idx: int,
) -> str:
    """
    toc_items        — list of (href, icon, label) for 'On This Page' links.
    module_lessons   — list of (href, label) for all lessons in the module.
    current_lesson_idx — 0-based index of the page being generated.
    """
    toc_links_html = "\n            ".join(
        f'<a href="{href}" class="toc-link flex items-center gap-2 text-xs '
        f'text-gray-600 py-1.5 px-2 rounded-lg no-underline">'
        f'<span class="iconify text-brand shrink-0" data-icon="{icon}"></span> {label}</a>'
        for href, icon, label in toc_items
    )

    lesson_links_html = ""
    for i, (href, label) in enumerate(module_lessons):
        if i == current_lesson_idx:
            lesson_links_html += (
                f'<a href="{href}" class="mod-lesson-active flex items-center gap-2 px-3 py-2 '
                f'rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] '
                f'text-xs font-medium no-underline transition-colors">'
                f'<span class="w-2 h-2 rounded-full bg-[#CB187D] shrink-0 lesson-dot"></span>'
                f'<span class="truncate">{label}</span></a>\n              '
            )
        else:
            lesson_links_html += (
                f'<a href="{href}" class="flex items-center gap-2 px-3 py-2 rounded-lg border '
                f'bg-white border-gray-100 text-gray-600 hover:border-gray-200 '
                f'text-xs font-medium no-underline transition-colors">'
                f'<span class="w-2 h-2 rounded-full bg-gray-300 shrink-0 lesson-dot"></span>'
                f'<span class="truncate">{label}</span></a>\n              '
            )

    return f"""
      <!-- ═══ TOC SIDEBAR ═══ -->
      <aside class="lesson-toc-sidebar">
        <div class="rounded-2xl border border-gray-100 shadow-sm overflow-hidden bg-white">
          <div class="toc-header relative flex items-center gap-2 px-4 py-3 border-b border-gray-100">
            <span class="toc-header-label text-xs font-bold uppercase tracking-widest text-brand">On This Page</span>
            <button class="toc-toggle-btn" onclick="toggleToc()" title="Toggle navigation">
              <span class="iconify text-sm" id="toc-toggle-icon" data-icon="fa6-solid:angles-left"></span>
            </button>
          </div>
          <nav class="toc-body px-2 py-2 border-b border-gray-100" aria-label="Page sections">
            {toc_links_html}
          </nav>
          <div class="toc-module-list px-3 py-3">
            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2 px-1">Module Lessons</p>
            <div class="space-y-1">
              {lesson_links_html}
            </div>
          </div>
        </div>
      </aside>
"""


# ── Shared section helpers ─────────────────────────────────────────────────────

def section_wrap(section_id: str, header_html: str, body_html: str) -> str:
    """Wrap a section header + body in the standard card shell."""
    return (
        f'\n        <!-- ═══ {section_id.upper()} ═══ -->\n'
        f'        <section id="{section_id}" class="scroll-mt-24">\n'
        f'          <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        f'{header_html}\n'
        f'            <div class="bg-white px-8 py-7 space-y-6">\n'
        f'{body_html}\n'
        f'            </div>\n'
        f'          </div>\n'
        f'        </section>\n'
    )


def section_header(icon: str, title: str, subtitle: str) -> str:
    return (
        f'            <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white '
        f'border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        f'              <span class="inline-flex items-center justify-center w-11 h-11 '
        f'rounded-xl bg-[#CB187D] shrink-0">\n'
        f'                <span class="iconify text-white text-base" data-icon="{icon}"></span>\n'
        f'              </span>\n'
        f'              <div class="min-w-0">\n'
        f'                <h2 class="text-xl font-bold text-gray-900 leading-tight">{title}</h2>\n'
        f'                <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">{subtitle}</p>\n'
        f'              </div>\n'
        f'            </div>'
    )


def code_block(code: str, language: str = "python") -> str:
    """Return a Prism-highlighted code block with a copy button."""
    return (
        f'<div class="relative rounded-xl overflow-hidden">\n'
        f'  <button class="copy-btn" onclick="copyCode(this)">'
        f'<span class="iconify" data-icon="fa6-regular:copy"></span><span>Copy</span></button>\n'
        f'  <pre class="pre-reset"><code class="language-{language}">{code}</code></pre>\n'
        f'</div>'
    )


def pill_tabs(tabs: list, tab_class: str, active_class: str,
              switch_fn: str) -> str:
    """
    tabs: list of (icon, label) tuples.
    Returns the <div> row of pill tab buttons.
    """
    buttons = []
    for i, (icon, label) in enumerate(tabs):
        is_active = (i == 0)
        cls = f"{tab_class} {active_class}" if is_active else tab_class
        extra = ""
        if is_active:
            extra = (
                ' bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white '
                'shadow-lg shadow-pink-200/50'
            )
        else:
            extra = ' bg-gray-800 text-gray-400'
        buttons.append(
            f'<button onclick="{switch_fn}({i})" class="{cls}{extra} '
            f'flex items-center gap-2 px-4 py-2 rounded-full transition-all duration-250" '
            f'role="tab">'
            f'<span class="iconify text-[13px]" data-icon="{icon}"></span>'
            f'<span class="text-xs font-bold">{label}</span></button>'
        )
    return (
        '<div class="flex flex-wrap items-center gap-2 mb-6" role="tablist">\n  '
        + "\n  ".join(buttons)
        + "\n</div>"
    )


# ── Bottom navigation ──────────────────────────────────────────────────────────

def bottom_nav(
    prev_filename: str,   # relative filename, or "none"
    prev_title: str,
    next_filename: str,   # relative filename, or "none"
    next_title: str,
) -> str:
    hub_link = (
        '<a href="../../../hub_home_page.html" class="lesson-nav-link group flex '
        'items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 '
        'transition-all sm:w-auto w-full">'
        '<span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] '
        'transition-colors" data-icon="fa6-solid:table-cells-large"></span>'
        '<span class="text-xs font-semibold uppercase tracking-widest text-gray-400 '
        'group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>'
        '</a>'
    )

    prev_html = (
        f'<a href="{prev_filename}" class="lesson-nav-link group flex-1 flex items-center '
        f'gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">'
        f'<span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] '
        f'transition-colors" data-icon="fa6-solid:arrow-left"></span>'
        f'<div class="min-w-0">'
        f'<p class="text-xs font-semibold uppercase tracking-widest text-gray-400 '
        f'group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>'
        f'<p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] '
        f'transition-colors truncate">{prev_title}</p>'
        f'</div></a>'
        if prev_filename.lower() != "none"
        else '<div class="flex-1"></div>'
    )

    next_html = (
        f'<a href="{next_filename}" class="lesson-nav-link group flex-1 flex items-center '
        f'justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">'
        f'<div class="min-w-0">'
        f'<p class="text-xs font-semibold uppercase tracking-widest text-gray-400 '
        f'group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>'
        f'<p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] '
        f'transition-colors truncate">{next_title}</p>'
        f'</div>'
        f'<span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] '
        f'transition-colors" data-icon="fa6-solid:arrow-right"></span>'
        f'</a>'
        if next_filename.lower() != "none"
        else ""
    )

    return (
        '\n        <!-- Bottom nav -->\n'
        '        <section>\n'
        '          <div class="flex flex-col sm:flex-row gap-3">\n'
        f'            {prev_html}\n'
        f'            {hub_link}\n'
        f'            {next_html}\n'
        '          </div>\n'
        '        </section>\n'
    )


# ── Final assembly ─────────────────────────────────────────────────────────────

def write_lesson(output_path: str, parts: list) -> None:
    """Join all HTML parts and write to the output path."""
    html = "\n".join(str(p) for p in parts)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"✅  Written → {out}")


# ── Quick self-test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("lesson_builder.py self-test")
    print(f"  Template : {TEMPLATE} ({'found' if TEMPLATE.exists() else 'NOT FOUND'})")
    print(f"  cdn_head length    : {len(cdn_head())} chars")
    print(f"  style_block length : {len(style_block())} chars")
    print(f"  script_block length: {len(script_block())} chars")
    print(f"  hero_svg length    : {len(hero_svg())} chars")
    print("  All OK — builder is ready.")
