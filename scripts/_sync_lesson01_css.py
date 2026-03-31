#!/usr/bin/env python3
"""
Sync lesson01_what_is_python.html CSS and HTML to match
the docs/new_lesson_template.html architecture.

17 targeted replacements — content (lesson text, section data) untouched.
"""

TARGET = "pages/track_01/mod_01_getting_started/lesson01_what_is_python.html"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

original = content
errors = []

def apply(label, old, new):
    global content
    if old not in content:
        errors.append(f"❌ NOT FOUND: {label}")
        return
    count = content.count(old)
    if count > 1:
        errors.append(f"⚠️  AMBIGUOUS ({count} matches): {label}")
        return
    content = content.replace(old, new)
    print(f"✅ {label}")

# ──────────────────────────────────────────────────────────────
# BROWSER CSS CHANGES
# ──────────────────────────────────────────────────────────────

# 1. bg-amber-tip: border-color → border shorthand
apply(
    "1. bg-amber-tip border",
    ".bg-amber-tip    { background: #fff7ed; border-color: #fed7aa; }",
    ".bg-amber-tip    { background: #fff7ed; border: 1px solid #fed7aa; }",
)

# 2. Tab CSS block — restructure from fragmented to combined template style
#    Replaces from "/* ── Key Concepts sidebar tabs */" through "/* ── Accordion */"
#    (the Accordion section comment itself is the anchor that stays in place)
apply(
    "2. Tab CSS block restructure",
    """    /* ── Key Concepts sidebar tabs  (.kc-tab / .kc-tab-active) ─── */
    .kc-tab-active { background: #fdf0f7; }
    .kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }
    .kc-panel-anim { animation: kcFadeIn 0.25s ease-out; }
    @keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* ── Code Examples pill tabs   (.ce-step / .ce-step-active) ── */
    .ce-step:not(.ce-step-active):hover { background: #374151; color: #ffffff; }
    .ce-panel-anim { animation: kcFadeIn 0.25s ease-out; }

    /* ── Common Mistakes pill tabs (.mk-step / .mk-step-active) ── */
    .mk-step:not(.mk-step-active):hover { background: #374151; color: #ffffff; }
    .mk-panel-anim { animation: kcFadeIn 0.25s ease-out; }

    /* ── Knowledge Check quiz tabs (.qz-step / .qz-step-active) ── */
    .qz-step:not(.qz-step-active):hover { background: #374151; color: #ffffff; }
    .qz-panel-anim { animation: kcFadeIn 0.25s ease-out; }

    /* Practice Exercises */
    .task-box { background: #fdf0f7; border: 1px solid #f5c6e0; }

    /* ── Accordion — used in Overview & Key Ideas sections ─────── */""",
    """    /* ─── Tab Systems ──────────────────────────────────────────── */

    /* Keyframe used by all tab panel fade-in animations */
    @keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* All panel animations share one keyframe */
    .kc-panel-anim,
    .ce-panel-anim,
    .mk-panel-anim,
    .qz-panel-anim,
    .pe-panel-anim { animation: kcFadeIn 0.25s ease-out; }

    /* ── Code Examples pill tabs   (.ce-step / .ce-step-active) ── */
    .ce-step:not(.ce-step-active):hover,
    /* ── Common Mistakes pill tabs (.mk-step / .mk-step-active) ── */
    .mk-step:not(.mk-step-active):hover,
    /* ── Knowledge Check quiz tabs (.qz-step / .qz-step-active) ── */
    .qz-step:not(.qz-step-active):hover,
    /* ── Practice Exercise tabs    (.pe-step / .pe-step-active) ── */
    .pe-step:not(.pe-step-active):hover { background: #374151; color: #ffffff; }

    /* Inactive pill tab base state (standalone browser without Tailwind) */
    .ce-step:not(.ce-step-active),
    .mk-step:not(.mk-step-active),
    .qz-step:not(.qz-step-active),
    .pe-step:not(.pe-step-active) { background: #1f2937; color: #ffffff; box-shadow: none; }

    /* Active pill tab base state */
    .ce-step-active,
    .mk-step-active,
    .qz-step-active,
    .pe-step-active {
      background: linear-gradient(to right, #CB187D, #e84aad);
      color: #ffffff;
      box-shadow: 0 10px 25px -5px rgba(203, 24, 125, 0.3);
    }

    /* Pill tab base layout (shared by all step tab buttons) */
    .pill-tab {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      border: none;
      cursor: pointer;
      font-size: 0.75rem;
      font-weight: 700;
      line-height: 1.2;
      transition: all 0.25s;
    }
    .pill-tab .iconify { font-size: 13px; }

    /* ─── Step tab consistent sizing ── */
    .ce-step, .mk-step, .qz-step, .pe-step {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      border: none;
      cursor: pointer;
      font-size: 0.75rem;
      font-weight: 700;
      line-height: 1.2;
      white-space: nowrap;
    }

    /* ── Key Concepts sidebar tabs  (.kc-tab / .kc-tab-active) ─── */
    .kc-tab-active { background: #fdf0f7; }
    .kc-indicator { height: 68px; }
    .kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }

    /* Task description box inside practice/example panels */
    .task-box { background: #fdf0f7; border: 1px solid #f5c6e0; }

    /* ── Accordion — used in Overview & Key Ideas sections ─────── */""",
)

# 3. Remove redundant pe-step block that sat after the accordion
#    (now incorporated into the combined tab block above)
apply(
    "3. Remove redundant pe-step after accordion",
    """    /* ── Practice Exercise tabs    (.pe-step / .pe-step-active) ── */
    .pe-step:not(.pe-step-active):hover { background: #374151; color: #ffffff; }
    .pe-panel-anim { animation: kcFadeIn 0.25s ease-out; }

    /* ═══════════════════════════════════════════════════════
       HERO — Static Gradient + Abstract Design
       ═══════════════════════════════════════════════════════ */""",
    """    /* ═══════════════════════════════════════════════════════
       HERO — Static Gradient + Abstract Design
       ═══════════════════════════════════════════════════════ */""",
)

# 4. scroll-progress — add width: 0;
apply(
    "4. scroll-progress width: 0",
    """    .scroll-progress {
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;""",
    """    .scroll-progress {
      position: fixed;
      top: 0;
      left: 0;
      width: 0;
      height: 3px;""",
)

# 5. lesson-layout / lesson-toc-sidebar — convert float to flex
apply(
    "5. lesson-layout flex (remove float)",
    """    /* ── Page layout — two-column: TOC sidebar + main content ──── */
    .lesson-layout { display: block; }
    .lesson-layout > main { overflow: hidden; }

    /* TOC Sidebar */
    .lesson-toc-sidebar { float: left; width: 240px; margin-right: 1.75rem; margin-bottom: 1rem; position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem); overflow-y: auto; transition: width 0.25s ease, opacity 0.25s ease; }""",
    """    /* ── Page layout — two-column: TOC sidebar + main content ──── */
    .lesson-layout { display: flex; gap: 1.75rem; align-items: flex-start; }
    .lesson-toc-sidebar {
      width: 240px; flex-shrink: 0;
      position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem);
      overflow-y: auto; transition: width 0.25s ease, opacity 0.25s ease;
    }""",
)

# 6. hero-abstract-card — fix padding + add opacity
apply(
    "6. hero-abstract-card padding + opacity",
    """    .hero-abstract-card {
      position: relative;
      border-radius: 1rem;
      overflow: hidden;
      padding: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }""",
    """    .hero-abstract-card {
      position: relative;
      border-radius: 1rem;
      overflow: hidden;
      padding: 0.25rem;
      opacity: 0.75;
      display: flex;
      align-items: center;
      justify-content: center;
    }""",
)

# 7. obj-card:hover — add background-color
apply(
    "7. obj-card:hover background-color",
    """    .obj-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 32px -6px rgba(203, 24, 125, 0.18), 0 6px 12px -2px rgba(203, 24, 125, 0.1);
      border-color: #CB187D;
    }""",
    """    .obj-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 32px -6px rgba(203, 24, 125, 0.18), 0 6px 12px -2px rgba(203, 24, 125, 0.1);
      border-color: #CB187D;
      background-color: #fdf0f7;
    }""",
)

# 8. Add section-header / skill-dot / hero-py-icon blocks before Generic outline tab buttons
apply(
    "8. Add section-header + skill-dot + hero-py-icon + rename generic tabs comment",
    "    /* ── Generic outline tab buttons (.tab-btn / .tab-panel) ───── */",
    """    /* ─── Section Headers ──────────────────────────────────────── */
    .section-header {
      display: flex; align-items: center; gap: 1rem;
      padding: 1.25rem 2rem 1.25rem 1rem;
      background: #ffffff; border-bottom: 1px solid #f3f4f6; border-left: 4px solid #CB187D;
    }
    .section-icon {
      display: inline-flex; align-items: center; justify-content: center;
      width: 2.75rem; height: 2.75rem; border-radius: 0.75rem; background: #CB187D; flex-shrink: 0;
    }
    .section-body { min-width: 0; }
    .section-title { font-size: 1.25rem; font-weight: 700; color: #111827; line-height: 1.3; margin: 0; }
    .section-subtitle { font-size: 0.875rem; color: #9ca3af; line-height: 1.4; margin-top: 0.125rem; margin-bottom: 0; }

    /* ─── Skill-level indicator dots ──────────────────────────── */
    .skill-dot { width: 6px; height: 6px; border-radius: 50%; background: #d1d5db; display: inline-block; }
    .skill-dot-active { background: #22c55e; }

    /* ─── Hero SVG illustration ────────────────────────────────── */
    .hero-svg { max-height: 320px; }
    .hero-py-icon-wrap { display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; }
    .hero-py-icon { font-size: 70px; filter: drop-shadow(0 0 14px rgba(255, 212, 59, 0.25)); }

    /* ── Generic outline tab buttons (.tab-btn / .tab-panel) ───── */""",
)

# 9. Mobile breakpoint — remove float: none
apply(
    "9. Mobile breakpoint remove float: none",
    "      .lesson-toc-sidebar { float: none; display: none; }",
    "      .lesson-toc-sidebar { display: none; }",
)

# ──────────────────────────────────────────────────────────────
# #hub-root BLOCK CHANGES
# ──────────────────────────────────────────────────────────────

# 10. Font family: hardcoded Inter → var(--font-body)
apply(
    "10. hub-root font-family → var(--font-body)",
    """  #hub-root,
  #hub-root * {
    font-family: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif !important;
    box-sizing: border-box !important;
  }""",
    """  #hub-root,
  #hub-root * {
    font-family: var(--font-body) !important;
    box-sizing: border-box !important;
  }""",
)

# 11. Mono font: hardcoded Fira Code → var(--font-mono)
apply(
    "11. hub-root code font-family → var(--font-mono)",
    "    font-family: 'Fira Code', ui-monospace, 'Cascadia Code', monospace !important;",
    "    font-family: var(--font-mono) !important;",
)

# 12. hero-title-main — add margin-bottom: 2rem
apply(
    "12. hero-title-main margin-bottom",
    """  /* ── Hero title override (hero uses very large text-3xl/text-4xl) ── */
  #hub-root .hero-title-main {
    font-size: 2.25rem !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
  }""",
    """  /* ── Hero title override ── */
  #hub-root .hero-title-main {
    font-size: 2.25rem !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
    margin-bottom: 2rem !important;
  }""",
)

# 13. Replace old section-header rule + dark-pill block anchor
#     with full template section-header + pill-tab + step-sizing + skill-dot + hero-svg + bg-amber-tip
apply(
    "13. Replace text-xl.font-bold rule with full section-header block + extras",
    """  /* ── Section header card titles ── */
  #hub-root .text-xl.font-bold,
  #hub-root h2.text-xl { font-size: 1.25rem !important; font-weight: 700 !important; }
  /* ── Dark pill tabs — dark bg, white text ── */""",
    """  /* ── Section header components ── */
  #hub-root .section-header {
    display: flex !important; align-items: center !important; gap: 1rem !important;
    padding: 1.25rem 2rem 1.25rem 1rem !important; background: #ffffff !important;
    border-bottom: 1px solid #f3f4f6 !important; border-left: 4px solid #CB187D !important;
  }
  #hub-root .section-icon {
    display: inline-flex !important; align-items: center !important;
    justify-content: center !important; width: 2.75rem !important; height: 2.75rem !important;
    border-radius: 0.75rem !important; background: #CB187D !important; flex-shrink: 0 !important;
  }
  #hub-root .section-body { min-width: 0 !important; }
  #hub-root .section-title {
    font-size: 1.25rem !important; font-weight: 700 !important;
    color: #111827 !important; line-height: 1.3 !important; margin: 0 !important;
  }
  #hub-root .section-subtitle {
    font-size: 0.875rem !important; color: #9ca3af !important;
    line-height: 1.4 !important; margin-top: 0.125rem !important; margin-bottom: 0 !important;
  }

  /* ── Pill tab base layout ── */
  #hub-root .pill-tab {
    display: inline-flex !important; align-items: center !important; gap: 0.5rem !important;
    padding: 0.5rem 1rem !important; border-radius: 9999px !important; border: none !important;
    cursor: pointer !important; font-size: 0.75rem !important; font-weight: 700 !important;
    line-height: 1.2 !important; transition: all 0.25s !important;
  }
  #hub-root .pill-tab .iconify { font-size: 13px !important; }

  /* ── Skill dots ── */
  #hub-root .skill-dot {
    width: 6px !important; height: 6px !important; border-radius: 50% !important;
    background: #d1d5db !important; display: inline-block !important;
  }
  #hub-root .skill-dot-active { background: #22c55e !important; }

  /* ── Hero SVG / Python icon ── */
  #hub-root .hero-svg { max-height: 320px !important; }
  #hub-root .hero-py-icon-wrap {
    display: flex !important; align-items: center !important;
    justify-content: center !important; width: 100% !important; height: 100% !important;
  }
  #hub-root .hero-py-icon {
    font-size: 70px !important;
    filter: drop-shadow(0 0 14px rgba(255, 212, 59, 0.25)) !important;
  }

  /* ── Tip / info boxes ── */
  #hub-root .bg-amber-tip { background: #fff7ed !important; border: 1px solid #fed7aa !important; }

  /* ── Dark pill tabs — inactive (dark bg, white text) ── */""",
)

# 14. Fix inactive tabs block — add box-shadow: none
apply(
    "14. Inactive tabs box-shadow: none",
    """  #hub-root .ce-step:not(.ce-step-active),
  #hub-root .mk-step:not(.mk-step-active),
  #hub-root .qz-step:not(.qz-step-active),
  #hub-root .pe-step:not(.pe-step-active) {
    background-color: #1f2937 !important;
    color: #ffffff !important;
  }""",
    """  #hub-root .ce-step:not(.ce-step-active),
  #hub-root .mk-step:not(.mk-step-active),
  #hub-root .qz-step:not(.qz-step-active),
  #hub-root .pe-step:not(.pe-step-active) {
    background-color: #1f2937 !important;
    color: #ffffff !important;
    box-shadow: none !important;
  }""",
)

# 15. Fix active tab box-shadow (4px 12px → 10px 25px -5px)
apply(
    "15. Active tab box-shadow",
    "    box-shadow: 0 4px 12px rgba(203,24,125,0.35) !important;",
    "    box-shadow: 0 10px 25px -5px rgba(203,24,125,0.3) !important;",
)

# 16. Fix Confluence Tailwind fix block — padding 0.375rem → 0.5rem + rename comment
apply(
    "16. Confluence step sizing padding 0.375rem → 0.5rem",
    """  /* -- Pill tab consistent sizing (Confluence Tailwind fix) -- */
  #hub-root .ce-step, #hub-root .mk-step,
  #hub-root .qz-step, #hub-root .pe-step {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    padding: 0.375rem 1rem !important;
    border-radius: 9999px !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
    border: none !important;
    cursor: pointer !important;
  }""",
    """  /* ── Step tab consistent sizing — semantic class beats Confluence button rules ── */
  #hub-root .ce-step,
  #hub-root .mk-step,
  #hub-root .qz-step,
  #hub-root .pe-step {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    padding: 0.5rem 1rem !important;
    border-radius: 9999px !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
    border: none !important;
    cursor: pointer !important;
  }""",
)

# 17. hero-pill .iconify opacity: 1 → 0.5
apply(
    "17. hero-pill iconify opacity 1 → 0.5",
    "  #hub-root .hero-pill .iconify { opacity: 1 !important; }",
    "  #hub-root .hero-pill .iconify { opacity: 0.5 !important; }",
)

# ──────────────────────────────────────────────────────────────
# HERO HTML CHANGES
# ──────────────────────────────────────────────────────────────

# 18. Skill dots — inline style → CSS classes
apply(
    "18. Skill dots inline style → CSS classes",
    """              <span class="inline-flex items-center gap-1">
                  <span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span>
                  <span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>
                  <span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>
                </span>""",
    """              <span class="inline-flex items-center gap-1">
                  <span class="skill-dot skill-dot-active"></span>
                  <span class="skill-dot"></span>
                  <span class="skill-dot"></span>
                </span>""",
)

# 19. Scroll progress bar — remove inline style="width: 0%;"
apply(
    "19. Scroll progress bar remove inline style",
    '<div class="scroll-progress" id="scroll-progress" style="width: 0%;"></div>',
    '<div class="scroll-progress" id="scroll-progress"></div>',
)

# 20. h1 mb-5 → mb-8 (template standard spacing)
apply(
    "20. h1 mb-5 → mb-8",
    'class="hero-title-main text-3xl md:text-4xl font-extrabold text-white mb-5 leading-[1.15] tracking-tight"',
    'class="hero-title-main text-3xl md:text-4xl font-extrabold text-white mb-8 leading-[1.15] tracking-tight"',
)

# 21. hero-abstract-card: remove inline style (now handled by CSS)
apply(
    "21. hero-abstract-card remove inline style (padding+opacity now in CSS)",
    '<div class="hero-abstract-card" style="padding:0.25rem;opacity:0.75;">',
    '<div class="hero-abstract-card">',
)

# ──────────────────────────────────────────────────────────────
# Write result
# ──────────────────────────────────────────────────────────────

if errors:
    print("\n── ERRORS ─────────────────────────────────")
    for e in errors:
        print(e)
    print("\nFile NOT written due to errors.")
else:
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(content)
    diff = len(content) - len(original)
    print(f"\n✅ All {sum(1 for _ in range(21))} replacements applied. File updated ({diff:+d} chars).")
