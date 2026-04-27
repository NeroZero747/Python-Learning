"""
Complete rebuild of lesson02_introduction_to_streamlit.html
Fixes ALL audit issues: broken HTML, thin content, wrong patterns, missing sections.
"""
import os

TARGET = os.path.join('pages', 'mod_05_data_application', 'lesson02_introduction_to_streamlit.html')

# ── Read the existing file to extract the hero SVG and sidebar ─────────────
existing = open(TARGET, encoding='utf-8').read()

# Extract hero SVG (reuse the existing hexagon artwork)
svg_start = existing.find('<svg viewBox="0 0 280 324"')
svg_end = existing.find('</svg>', svg_start) + len('</svg>')
HERO_SVG = existing[svg_start:svg_end]

# ── Sidebar HTML (already verified correct) ────────────────────────────────
SIDEBAR_LINKS = """<a href="lesson01_why_build_data_apps.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">1. Why Build Data Apps?</span>
</a>
<a href="lesson02_introduction_to_streamlit.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span>
  <span class="truncate">2. Introduction to Streamlit</span>
</a>
<a href="lesson03_interactive_filters.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">3. Interactive Filters</span>
</a>
<a href="lesson04_exporting_data.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">4. Exporting Data</span>
</a>
<a href="lesson05_deploying_data_applications.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">5. Deploying Data Applications</span>
</a>
<a href="lesson06_shiny_for_python.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">6. Shiny for Python</span>
</a>
<a href="lesson07_streamlit_vs_shiny.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">7. Streamlit vs Shiny</span>
</a>"""

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lesson 2 &mdash; Introduction to Streamlit | Python Learning Hub</title>
  <meta name="description" content="Learn Introduction to Streamlit in Python. Part of the Building Data Applications module — Track 4: Data Applications — Python Learning Hub.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" crossorigin="anonymous">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js" crossorigin="anonymous"></script>
  <style>
    /* ── CSS Variables — font tokens (:root) ──────────────────────────────── */
    :root {{ --font-body: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif; --font-mono: 'Fira Code', monospace; }}
    /* ── Global reset — smooth scroll ──────────────────────────────── */
    * {{ scroll-behavior: smooth; }}
    /* ── Prism.js — syntax highlighted code blocks ──────────────────────────────── */
    pre[class*="language-"] {{ border-radius: 0.75rem; font-family: var(--font-mono); font-size: 0.875rem; margin: 0; padding: 1.25rem 1.5rem; }}
    code[class*="language-"], pre[class*="language-"] {{ background: #1e1e2e; }}
    /* ── Heading resets — strip Confluence default margins ──────────────────────────────── */
    body {{ font-family: var(--font-body); background: #f9fafb; color: #1f2937; line-height: 1.6; margin: 0; padding: 0; }}
    h1, h2, h3, h4, h5, h6 {{ margin-top: 0; margin-bottom: 0; padding: 0; line-height: 1.3; }}
    h2 {{ font-size: 1.25rem; font-weight: 700; }}
    h3 {{ font-size: 1rem; font-weight: 600; }}
    /* ── Brand utility classes ──────────────────────────────── */
    .text-brand {{ color: #CB187D; }}
    .text-brand-dark {{ color: #7F004C; }}
    .bg-brand {{ background: #CB187D; }}
    .bg-brand-soft {{ background: #fdf0f7; }}
    .brand-soft-panel {{ background: #fdf0f7; border-color: #f5c6e0; }}
    .bg-amber-tip {{ background: #fff7ed; border-color: #fed7aa; }}
    .bg-code {{ background: #1e1e2e; }}
    .border-code-sep {{ border-color: rgba(255, 255, 255, 0.08); }}
    .pre-reset {{ margin: 0; border-radius: 0; background: transparent; }}
    /* ── Key Concepts sidebar tabs (.kc-tab / .kc-tab-active) ──────────────────────────────── */
    .kc-tab-active {{ background: #fdf0f7; }}
    .kc-tab:not(.kc-tab-active):hover {{ background: #f9fafb; }}
    .kc-panel-anim {{ animation: kcFadeIn 0.25s ease-out; }}
    @keyframes kcFadeIn {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    /* ── Code Examples pill tabs (.ce-step / .ce-step-active) ──────────────────────────────── */
    .ce-step:not(.ce-step-active):hover {{ background: #374151; color: #d1d5db; }}
    .ce-panel-anim {{ animation: kcFadeIn 0.25s ease-out; }}
    /* ── Common Mistakes pill tabs (.mk-step / .mk-step-active) ──────────────────────────────── */
    .mk-step:not(.mk-step-active):hover {{ background: #374151; color: #d1d5db; }}
    .mk-panel-anim {{ animation: kcFadeIn 0.25s ease-out; }}
    /* ── Knowledge Check quiz tabs (.qz-step / .qz-step-active) ──────────────────────────────── */
    .qz-step:not(.qz-step-active):hover {{ background: #374151; color: #d1d5db; }}
    .qz-panel-anim {{ animation: kcFadeIn 0.25s ease-out; }}
    /* ── Practice Exercise tabs (.pe-step / .pe-step-active) ──────────────────────────────── */
    .pe-step:not(.pe-step-active):hover {{ background: #374151; color: #d1d5db; }}
    .pe-panel-anim {{ animation: kcFadeIn 0.25s ease-out; }}
    .task-box {{ background: #fdf0f7; border: 1px solid #f5c6e0; }}
    /* ── Accordion — used in Overview & Key Ideas sections ──────────────────────────────── */
    .accordion-body {{ display: none !important; }}
    .accordion-body.open {{ display: block !important; }}
    .accordion-toggle {{ display: flex !important; align-items: center !important; gap: 8px !important; width: 100% !important; padding: 10px 16px !important; border-radius: 10px !important; font-size: 0.8rem !important; font-weight: 600 !important; cursor: pointer !important; border: 2px dashed #f5c6e0 !important; background: #fdf0f7 !important; color: #7F004C !important; line-height: 1.2 !important; text-decoration: none !important; transition: background 0.15s, border-color 0.15s !important; }}
    .accordion-toggle:hover {{ background: #f9d9ee !important; border-color: #CB187D !important; }}
    .accordion-toggle.open {{ background: #fdf0f7 !important; border-color: #CB187D !important; border-style: solid !important; }}
    .accordion-chevron {{ margin-left: auto !important; transition: transform 0.2s !important; }}
    .accordion-toggle.open .accordion-chevron {{ transform: rotate(180deg) !important; }}
    /* ── Hero banner — full-width gradient header ──────────────────────────────── */
    .hero-container {{ position: relative; border-radius: 1.25rem; overflow: hidden; min-height: 380px; background: linear-gradient(135deg, #CB187D 0%, #CB187D 40%, #a31268 65%, #7F004C 100%); }}
    .hero-dots {{ position: absolute; inset: 0; opacity: 0.06; background-image: radial-gradient(circle, rgba(255,255,255,0.7) 1px, transparent 1px); background-size: 24px 24px; }}
    .hero-glow {{ position: absolute; border-radius: 50%; pointer-events: none; filter: blur(70px); }}
    .hero-glow-1 {{ width: 350px; height: 350px; top: -80px; right: 0; background: rgba(255, 255, 255, 0.12); }}
    .hero-glow-2 {{ width: 280px; height: 280px; bottom: -50px; left: 5%; background: rgba(127, 0, 76, 0.35); }}
    .hero-glow-line {{ position: absolute; bottom: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent 0%, #f5c6e0 30%, #CB187D 50%, #f5c6e0 70%, transparent 100%); opacity: 0.7; }}
    .hero-pill {{ background: #ffffff; border: none; color: #7F004C; font-weight: 700; transition: transform 0.2s ease; pointer-events: none; cursor: default; }}
    .hero-pill:hover {{ transform: translateY(-1px); }}
    /* ── Scroll progress bar — fixed top-of-page indicator ──────────────────────────────── */
    .scroll-progress {{ position: fixed; top: 0; left: 0; height: 3px; background: linear-gradient(90deg, #CB187D, #6366f1, #CB187D); background-size: 200% 100%; animation: scrollGradient 3s linear infinite; z-index: 9999; transition: width 0.15s; }}
    @keyframes scrollGradient {{ 0% {{ background-position: 0% 0%; }} 100% {{ background-position: 200% 0%; }} }}
    /* ── Page layout — two-column: TOC sidebar + main content ──────────────────────────────── */
    .lesson-layout {{ display: flex; gap: 1.75rem; align-items: flex-start; }}
    .lesson-toc-sidebar {{ width: 240px; flex-shrink: 0; position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem); overflow-y: auto; transition: width 0.25s ease, opacity 0.25s ease; }}
    .lesson-toc-sidebar.toc-collapsed {{ width: 44px; overflow: hidden; }}
    .lesson-toc-sidebar.toc-collapsed .toc-body {{ display: none; }}
    .lesson-toc-sidebar.toc-collapsed .toc-header-label {{ display: none; }}
    .lesson-toc-sidebar.toc-collapsed .toc-module-list {{ display: none; }}
    .toc-toggle-btn {{ background: none; border: none; cursor: pointer; padding: 2px; color: #CB187D; display: flex; align-items: center; justify-content: center; position: absolute; right: 8px; top: 50%; transform: translateY(-50%); border-radius: 6px; transition: background 0.15s; }}
    .toc-toggle-btn:hover {{ background: #fdf0f7; }}
    .toc-link {{ transition: color 0.15s, padding-left 0.15s; }}
    .toc-link:hover {{ color: #CB187D; padding-left: 4px; }}
    .toc-link.active {{ color: #CB187D; font-weight: 600; border-left: 3px solid #CB187D; padding-left: 8px; }}
    /* ── Objective cards (.obj-card) ──────────────────────────────── */
    .obj-card {{ transition: box-shadow 0.22s cubic-bezier(.4,0,.2,1), border-color 0.22s ease, background-color 0.22s ease; }}
    .obj-card:hover {{ box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); border-color: #f5c6e0; background-color: #ffffff; }}
    .obj-card .obj-icon {{ transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease; }}
    .obj-card:hover .obj-icon {{ transform: scale(1.1); background-color: #CB187D; }}
    .obj-card:hover .obj-icon .iconify {{ color: white !important; }}
    #key-ideas .obj-card:hover {{ border-color: #f3f4f6; background-color: #ffffff; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); }}
    #key-ideas .obj-card:hover .obj-icon {{ transform: scale(1.1); background-color: revert; }}
    /* ── Generic outline tab buttons (.tab-btn / .tab-panel) ──────────────────────────────── */
    .tab-btn {{ display: inline-flex; align-items: center; gap: 6px; padding: 7px 18px; font-size: 0.82rem; font-weight: 600; cursor: pointer; border: 1.5px solid #e5e7eb; border-radius: 999px; color: #6b7280; background: #fff; line-height: 1.2; transition: color 0.15s, background 0.15s, border-color 0.15s; }}
    .tab-btn:hover {{ color: #CB187D; border-color: #CB187D; background: #fdf0f7; }}
    .tab-btn.active {{ color: #fff; background: #CB187D; border-color: #CB187D; }}
    .tab-panel {{ display: none; }}
    .tab-panel.active {{ display: block; }}
    /* ── Code block copy button (.copy-btn) ──────────────────────────────── */
    .copy-btn {{ position: absolute; top: 10px; right: 12px; display: inline-flex; align-items: center; background: rgba(203, 24, 125, 0.15); border: 1px solid rgba(203, 24, 125, 0.3); color: #CB187D; border-radius: 6px; padding: 3px 8px; font-size: 0.65rem; font-weight: 600; cursor: pointer; transition: background 0.2s; white-space: nowrap; }}
    .copy-btn:hover {{ background: rgba(203, 24, 125, 0.3); }}
    .copy-btn-light {{ position: static; color: #fff; border-color: rgba(255, 255, 255, 0.25); background: rgba(255, 255, 255, 0.1); }}
    .copy-btn-light:hover {{ background: rgba(255, 255, 255, 0.2); }}
    /* ── Bottom lesson navigation — Previous / All Lessons / Next ──────────────────────────────── */
    .lesson-nav-link:hover p, .lesson-nav-link:hover span, .lesson-nav-link:hover svg {{ color: #CB187D; transition: color 0.15s; }}
    /* ── Back-to-top floating button ──────────────────────────────── */
    .back-to-top {{ position: fixed; bottom: 2rem; right: 2rem; width: 44px; height: 44px; border-radius: 50%; background: #CB187D; color: white; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(203, 24, 125, 0.3); cursor: pointer; opacity: 0; transform: translateY(10px); transition: opacity 0.3s, transform 0.3s; z-index: 50; border: none; }}
    .back-to-top.visible {{ opacity: 1; transform: translateY(0); }}
    .back-to-top:hover {{ background: #7F004C; }}
    /* ── Quiz answer feedback buttons (.quiz-btn.correct / .incorrect) ──────────────────────────────── */
    .quiz-btn.correct {{ background: #f0fdf4; border-color: #22c55e; color: #16a34a; }}
    .quiz-btn.incorrect {{ background: #fef2f2; border-color: #ef4444; color: #dc2626; }}
    /* ── Card hover animations — Mistake, Flow, Recap, Overview cards ──────────────────────────────── */
    .mistake-card {{ transition: transform 0.18s ease, box-shadow 0.18s ease; }}
    .mistake-card:hover {{ transform: translateY(-2px); box-shadow: 0 8px 25px -5px rgba(0, 0, 0, 0.08); }}
    .flow-stepper .flow-step {{ transition: transform 0.15s ease; }}
    .flow-stepper .flow-step:hover {{ transform: translateX(4px); }}
    .recap-item {{ transition: transform 0.15s ease, box-shadow 0.15s ease; }}
    .recap-item:hover {{ transform: translateX(4px); box-shadow: -4px 0 0 0 #10b981; }}
    .overview-card {{ transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease; }}
    .overview-card:hover {{ transform: translateY(-3px); box-shadow: 0 12px 30px -6px rgba(203, 24, 125, 0.12); border-color: rgba(203, 24, 125, 0.3); }}
    /* ── Responsive — mobile breakpoint (<768px) ──────────────────────────────── */
    @media (max-width: 767px) {{ .lesson-toc-sidebar {{ display: none; }} .lesson-layout {{ display: block; }} #lesson-nav {{ display: block; }} .hero-container {{ min-height: auto; }} .hero-split {{ flex-direction: column !important; }} .hero-abstract-card {{ margin-top: 1.5rem; }} }}
    /* ── Print styles — hide interactive chrome when printing ──────────────────────────────── */
    @media print {{ .lesson-toc-sidebar, .back-to-top, .scroll-progress, .copy-btn, .hero-container {{ display: none; }} .obj-card:hover {{ transform: none; box-shadow: none; }} }}
    /* ── Iconify icon alignment utility ──────────────────────────────── */
    .iconify {{ vertical-align: middle; flex-shrink: 0; }}
  </style>
</head>
<body>

<div class="scroll-progress" id="scroll-progress" style="width: 0%;"></div>
<button class="back-to-top" id="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
  <span class="iconify text-lg" data-icon="fa6-solid:arrow-up"></span>
</button>

<div class="bg-gray-50 min-h-screen">

  <!-- ── HERO ──────────────────────────────── -->
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
                <span class="iconify text-[10px]" data-icon="fa6-solid:window-maximize"></span> Module 5
              </span>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="inline-flex items-center gap-1"><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span><span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span></span> Intermediate
              </span>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> 8 min read
              </span>
            </div>
            <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson 02</p>
            <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">Introduction to Streamlit</h1>
            <p class="text-white/80 text-sm md:text-base leading-relaxed mb-4 max-w-lg">Building Data Applications &middot; Data Applications Track</p>
            <div class="flex items-center gap-4 mb-5 text-sm">
              <div class="flex items-center gap-2">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
                  <span class="iconify text-white text-[10px]" data-icon="fa6-solid:user"></span>
                </span>
                <span class="text-white/85 font-medium text-xs">Python Learning Hub</span>
              </div>
            </div>
            <div class="flex items-center gap-2 flex-wrap">
              <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span><span class="font-extrabold">5</span><span class="font-semibold opacity-55">Goals</span></a>
              <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span><span class="font-extrabold">5</span><span class="font-semibold opacity-55">Examples</span></a>
              <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span><span class="font-extrabold">5</span><span class="font-semibold opacity-55">Exercises</span></a>
              <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
                <span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span>
                <span class="font-extrabold">2<span class="font-bold opacity-50">/7</span></span>
                <span class="font-semibold opacity-55">Progress</span>
              </span>
            </div>
          </div>
          <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
            <div class="hero-abstract-card" style="padding:0.25rem;opacity:0.75;">
              {HERO_SVG}
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <!-- ── MAIN LAYOUT ──────────────────────────────── -->
  <div class="max-w-[1280px] mx-auto px-4 pt-8 pb-12">
    <div class="lesson-layout">
      <aside class="lesson-toc-sidebar">
        <div class="rounded-2xl border border-gray-100 shadow-sm overflow-hidden bg-white">
          <div class="toc-header relative flex items-center gap-2 px-4 py-3 border-b border-gray-100">
            <span class="toc-header-label text-xs font-bold uppercase tracking-widest text-brand">On This Page</span>
            <button class="toc-toggle-btn" onclick="toggleToc()" title="Toggle navigation">
              <span class="iconify text-sm" id="toc-toggle-icon" data-icon="fa6-solid:angles-left"></span>
            </button>
          </div>
          <nav class="toc-body px-2 py-2 border-b border-gray-100" aria-label="Page sections">
            <a href="#objective" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:bullseye"></span> Lesson Objective</a>
            <a href="#overview" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:binoculars"></span> Overview</a>
            <a href="#key-ideas" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:lightbulb"></span> Key Takeaways</a>
            <a href="#key-concepts" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:book-open"></span> Key Concepts</a>
            <a href="#code-examples" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:code"></span> Code Examples</a>
            <a href="#comparison" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:table-columns"></span> SQL / Excel Comparison</a>
            <a href="#practice" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:dumbbell"></span> Practice Exercises</a>
            <a href="#mistakes" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:triangle-exclamation"></span> Common Mistakes</a>
            <a href="#real-world" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:briefcase"></span> Real-World Use</a>
            <a href="#recap" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:list-check"></span> Lesson Recap</a>
            <a href="#knowledge-check" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:brain"></span> Knowledge Check</a>
            <a href="#next-lesson" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:circle-arrow-right"></span> Next Lesson</a>
          </nav>
          <div class="toc-module-list px-3 py-3">
            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2 px-1">Module Lessons</p>
            <div class="space-y-1">{SIDEBAR_LINKS}</div>
          </div>
        </div>
      </aside>

      <main class="min-w-0 flex-1 space-y-10">

<!-- ═══════════════════ OBJECTIVE ═══════════════════ -->
<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Objective</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">What you will be able to do after this lesson</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:lightbulb"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Explain what Streamlit is</p>
            <p class="text-xs text-gray-500 mt-0.5">Describe what Streamlit does and why data analysts use it instead of traditional web frameworks</p>
          </div>
        </div>
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:terminal"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Install and run a Streamlit app</p>
            <p class="text-xs text-gray-500 mt-0.5">Use pip to install Streamlit and launch your first app with the <code class="font-mono">streamlit run</code> command</p>
          </div>
        </div>
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:sliders"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Use core display and input components</p>
            <p class="text-xs text-gray-500 mt-0.5">Display text, tables, and capture user input with <code class="font-mono">st.write()</code>, <code class="font-mono">st.selectbox()</code>, and <code class="font-mono">st.slider()</code></p>
          </div>
        </div>
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:chart-column"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Create charts and visualizations</p>
            <p class="text-xs text-gray-500 mt-0.5">Render bar charts, line charts, and metrics cards directly from pandas DataFrames</p>
          </div>
        </div>
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 sm:col-span-2">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:gauge-high"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Build a simple interactive dashboard</p>
            <p class="text-xs text-gray-500 mt-0.5">Combine data loading, filters, charts, and metrics into a single working Streamlit dashboard</p>
          </div>
        </div>
      </div>
      <div class="mt-5 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">This lesson introduces <strong>Streamlit</strong> from installation through building your first interactive dashboard, covering all the core components you will use daily.</p>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ OVERVIEW ═══════════════════ -->
<section id="overview">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:binoculars"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Overview</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A high-level introduction before diving into the details</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-5">
      <!-- Hook quote -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-start gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">Streamlit is an open-source Python library that turns ordinary Python scripts into interactive web applications without requiring any knowledge of HTML, CSS, or JavaScript.</p>
        </div>
      </div>
      <!-- Analogy intro -->
      <p class="text-sm text-gray-600 leading-relaxed">Think of Streamlit like a <strong>food truck kitchen</strong>: you bring the ingredients (your data and Python code), and the truck already has the counter, the menu board, the serving window, and the payment system built in &mdash; you just cook and serve.</p>
      <!-- Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:lightbulb"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">What Streamlit Is</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The food truck itself &mdash; everything is built in</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Streamlit is a Python library that handles the entire web layer for you &mdash; routing, layout, and live reloading &mdash; so you only write Python and your app appears in the browser instantly.</p>
        </div>
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:terminal"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Install &amp; Run</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The ignition key &mdash; one command starts everything</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">You install Streamlit with <code class="font-mono text-[11px]">pip install streamlit</code> and launch any app with <code class="font-mono text-[11px]">streamlit run app.py</code>, which starts a local web server and opens your browser automatically.</p>
        </div>
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:sliders"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Display &amp; Input Components</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The counter and menu board &mdash; ready-made UI</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Streamlit provides dozens of built-in widgets like <code class="font-mono text-[11px]">st.write()</code>, <code class="font-mono text-[11px]">st.selectbox()</code>, and <code class="font-mono text-[11px]">st.slider()</code> that render as professional UI elements without you writing any frontend code.</p>
        </div>
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:chart-column"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Charts &amp; Visualizations</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The display board &mdash; shows today's specials</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">You can render bar charts, line charts, and metric cards by passing a pandas DataFrame directly to functions like <code class="font-mono text-[11px]">st.bar_chart()</code> or <code class="font-mono text-[11px]">st.metric()</code> &mdash; no chart library configuration needed.</p>
        </div>
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors sm:col-span-2">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:gauge-high"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Interactive Dashboard</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The full meal &mdash; ingredients combined into a dish</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">When you combine data loading, filters, and charts in a single script, Streamlit reruns the entire file every time a user changes a widget, which means your dashboard updates in real time without any extra code for event handling or callbacks.</p>
        </div>
      </div>
      <!-- Closing tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Streamlit is one of the fastest ways for data analysts to share their work as a live, interactive tool that non-technical stakeholders can use without installing Python themselves.</p>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ KEY TAKEAWAYS ═══════════════════ -->
<section id="key-ideas">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:lightbulb"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Takeaways</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The most important ideas to remember</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <!-- Pink card -->
        <div class="obj-card rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:bolt"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Zero Frontend Knowledge Required</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">Streamlit eliminates the need to learn HTML, CSS, or JavaScript, which means a data analyst who only knows Python can ship a working dashboard in minutes. If you try to build the same dashboard with Flask or Django, you will spend more time on templates and routing than on the actual analysis.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Python-only</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">No templates</span>
            </div>
          </div>
        </div>
        <!-- Violet card -->
        <div class="obj-card rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:terminal"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">One Command Launches Everything</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed"><code class="font-mono text-xs bg-violet-50 px-1 rounded">streamlit run app.py</code> starts a local server and opens the browser in one step. If you accidentally run your script with <code class="font-mono text-xs bg-violet-50 px-1 rounded">python app.py</code> instead, nothing will appear because Streamlit&rsquo;s server never starts.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">streamlit run</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Hot reload</span>
            </div>
          </div>
        </div>
        <!-- Blue card -->
        <div class="obj-card rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:sliders"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Widgets Return Values Directly</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">Every Streamlit widget returns the user&rsquo;s current selection as a plain Python variable, so <code class="font-mono text-xs bg-blue-50 px-1 rounded">region = st.selectbox("Region", options)</code> gives you a string you can immediately use to filter a DataFrame. There is no callback system or event listener to learn.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">st.selectbox()</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">st.slider()</span>
            </div>
          </div>
        </div>
        <!-- Emerald card -->
        <div class="obj-card rounded-2xl border border-emerald-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-column"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Charts Accept DataFrames Directly</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed"><code class="font-mono text-xs bg-emerald-50 px-1 rounded">st.bar_chart(df)</code> renders instantly from a pandas DataFrame without any Matplotlib or Plotly configuration. This means you can go from raw data to a visible chart in a single line, which makes prototyping dramatically faster than building visualizations manually.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">st.bar_chart()</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">st.metric()</span>
            </div>
          </div>
        </div>
        <!-- Amber card -->
        <div class="obj-card rounded-2xl border border-amber-100 bg-white overflow-hidden shadow-sm sm:col-span-2">
          <div class="h-1 bg-gradient-to-r from-amber-500 to-orange-400"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-amber-500 to-orange-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:rotate"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">The Entire Script Reruns on Every Interaction</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">Streamlit&rsquo;s execution model reruns your entire Python file top-to-bottom every time a user changes any widget. This is powerful because your dashboard always shows fresh results, but it also means expensive operations like loading a large CSV will run repeatedly unless you wrap them in <code class="font-mono text-xs bg-amber-50 px-1 rounded">@st.cache_data</code>.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-600 border border-amber-100">Rerun model</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-600 border border-amber-100">@st.cache_data</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ KEY CONCEPTS ═══════════════════ -->
<section id="key-concepts">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Core terms, syntax, and mechanics explained in depth</p>
      </div>
    </div>
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full bg-[#CB187D] transition-all duration-300" style="height:68px;"></div>
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-[#CB187D] text-white shadow-sm shadow-pink-200"><span class="iconify text-[11px]" data-icon="fa6-solid:lightbulb"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">What Is Streamlit?</span>
          </button>
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:terminal"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Install &amp; Run</span>
          </button>
          <button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:sliders"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Display &amp; Input</span>
          </button>
          <button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:chart-column"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Charts &amp; Metrics</span>
          </button>
          <button onclick="switchKcTab(4)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:gauge-high"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Dashboard Layout</span>
          </button>
        </div>
        <div class="flex-1 min-w-0 md:pl-5">
          <!-- KC Panel 0 — What Is Streamlit? (pink) -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md"><span class="iconify text-white text-sm" data-icon="fa6-solid:lightbulb"></span></span>
                    <div><h3 class="text-sm font-bold text-gray-900">What Is Streamlit?</h3><p class="text-[10px] text-gray-400">Open-source Python framework</p></div>
                  </div>
                  <span class="inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D]">Core</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">Streamlit is an open-source Python framework designed specifically for data scientists and analysts who want to create interactive web applications without learning frontend technologies. You write a standard <code class="font-mono text-xs bg-pink-50 text-[#CB187D] px-1 rounded">.py</code> file, and Streamlit converts it into a fully functional web app that runs in the browser.</p>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2"><span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span><span class="text-[11px] font-semibold text-gray-400">Python</span></div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st          # import the library

st.title("Sales Dashboard")     # renders an h1 heading
st.write("Welcome to the app")  # renders text or data</code></pre>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Every <code class="font-mono text-xs">st.</code> call adds a visible element to the page in the order it appears in your script &mdash; there is no separate layout file.</p>
                </div>
              </div>
            </div>
          </div>
          <!-- KC Panel 1 — Install & Run (violet) -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md"><span class="iconify text-white text-sm" data-icon="fa6-solid:terminal"></span></span>
                    <div><h3 class="text-sm font-bold text-gray-900">Install &amp; Run</h3><p class="text-[10px] text-gray-400">Getting started in two commands</p></div>
                  </div>
                  <span class="inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600">Setup</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">Installing Streamlit is a single <code class="font-mono text-xs bg-violet-50 text-violet-700 px-1 rounded">pip install</code> command. After installation, you launch any Streamlit app by running <code class="font-mono text-xs bg-violet-50 text-violet-700 px-1 rounded">streamlit run filename.py</code> in your terminal, which starts a local development server on port 8501 and opens it in your default browser.</p>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2"><span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span><span class="text-[11px] font-semibold text-gray-400">Bash</span></div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-bash"># Step 1: install Streamlit into your virtual environment
pip install streamlit

# Step 2: run your app (opens http://localhost:8501)
streamlit run app.py</code></pre>
                </div>
                <div class="overflow-x-auto rounded-xl border border-violet-100">
                  <table class="w-full text-sm">
                    <thead><tr class="bg-violet-50"><th class="px-4 py-2 text-left font-semibold text-violet-600 text-xs uppercase tracking-wider">Command</th><th class="px-4 py-2 text-left font-semibold text-violet-600 text-xs uppercase tracking-wider">Purpose</th></tr></thead>
                    <tbody>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 text-gray-600 font-mono text-xs">pip install streamlit</td><td class="px-4 py-2 text-gray-600 text-xs">Downloads and installs the library</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 text-gray-600 font-mono text-xs">streamlit run app.py</td><td class="px-4 py-2 text-gray-600 text-xs">Starts local server + opens browser</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 text-gray-600 font-mono text-xs">streamlit hello</td><td class="px-4 py-2 text-gray-600 text-xs">Runs built-in demo app</td></tr>
                    </tbody>
                  </table>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Always use <code class="font-mono text-xs">streamlit run</code>, not <code class="font-mono text-xs">python</code>. Running <code class="font-mono text-xs">python app.py</code> executes the script but never starts the web server, so you will see no output in the browser.</p>
                </div>
              </div>
            </div>
          </div>
          <!-- KC Panel 2 — Display & Input (blue) -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md"><span class="iconify text-white text-sm" data-icon="fa6-solid:sliders"></span></span>
                    <div><h3 class="text-sm font-bold text-gray-900">Display &amp; Input Components</h3><p class="text-[10px] text-gray-400">Built-in widgets for UI</p></div>
                  </div>
                  <span class="inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600">Widgets</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">Streamlit ships with dozens of pre-built widgets that cover the most common dashboard needs. Display functions like <code class="font-mono text-xs bg-blue-50 text-blue-700 px-1 rounded">st.write()</code> and <code class="font-mono text-xs bg-blue-50 text-blue-700 px-1 rounded">st.dataframe()</code> render text and tables, while input functions like <code class="font-mono text-xs bg-blue-50 text-blue-700 px-1 rounded">st.selectbox()</code> and <code class="font-mono text-xs bg-blue-50 text-blue-700 px-1 rounded">st.slider()</code> return the user&rsquo;s current selection as a normal Python variable.</p>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2"><span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span><span class="text-[11px] font-semibold text-gray-400">Python</span></div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st
import pandas as pd

df = pd.read_csv("sales.csv")   # load the dataset

st.title("Sales Explorer")      # page heading
st.dataframe(df)                 # interactive table

# selectbox returns the chosen string
region = st.selectbox("Region", df["region"].unique())

# slider returns the chosen number
min_sales = st.slider("Min Sales", 0, 10000, 1000)</code></pre>
                </div>
                <div class="overflow-x-auto rounded-xl border border-blue-100">
                  <table class="w-full text-sm">
                    <thead><tr class="bg-blue-50"><th class="px-4 py-2 text-left font-semibold text-blue-600 text-xs uppercase tracking-wider">Function</th><th class="px-4 py-2 text-left font-semibold text-blue-600 text-xs uppercase tracking-wider">Returns</th><th class="px-4 py-2 text-left font-semibold text-blue-600 text-xs uppercase tracking-wider">Use For</th></tr></thead>
                    <tbody>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-mono text-xs text-gray-600">st.write()</td><td class="px-4 py-2 text-xs text-gray-600">None</td><td class="px-4 py-2 text-xs text-gray-600">Text, DataFrames, charts</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-mono text-xs text-gray-600">st.selectbox()</td><td class="px-4 py-2 text-xs text-gray-600">str</td><td class="px-4 py-2 text-xs text-gray-600">Dropdown menus</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-mono text-xs text-gray-600">st.slider()</td><td class="px-4 py-2 text-xs text-gray-600">int / float</td><td class="px-4 py-2 text-xs text-gray-600">Numeric ranges</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-mono text-xs text-gray-600">st.dataframe()</td><td class="px-4 py-2 text-xs text-gray-600">None</td><td class="px-4 py-2 text-xs text-gray-600">Scrollable tables</td></tr>
                    </tbody>
                  </table>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Use <code class="font-mono text-xs">st.dataframe()</code> instead of <code class="font-mono text-xs">st.write()</code> for large tables &mdash; <code class="font-mono text-xs">st.dataframe()</code> adds sorting, searching, and column resizing out of the box.</p>
                </div>
              </div>
            </div>
          </div>
          <!-- KC Panel 3 — Charts & Metrics (emerald) -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md"><span class="iconify text-white text-sm" data-icon="fa6-solid:chart-column"></span></span>
                    <div><h3 class="text-sm font-bold text-gray-900">Charts &amp; Metrics</h3><p class="text-[10px] text-gray-400">Built-in visualization functions</p></div>
                  </div>
                  <span class="inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600">Visual</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">Streamlit includes built-in chart functions that accept pandas DataFrames directly. <code class="font-mono text-xs bg-emerald-50 text-emerald-700 px-1 rounded">st.bar_chart()</code> and <code class="font-mono text-xs bg-emerald-50 text-emerald-700 px-1 rounded">st.line_chart()</code> create responsive charts in one line, while <code class="font-mono text-xs bg-emerald-50 text-emerald-700 px-1 rounded">st.metric()</code> displays a KPI card with an optional delta indicator showing the change from a previous value.</p>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2"><span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span><span class="text-[11px] font-semibold text-gray-400">Python</span></div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># bar chart — pass a DataFrame column directly
st.bar_chart(df.set_index("region")["sales"])

# line chart — shows trends over time
st.line_chart(df.set_index("month")["revenue"])

# metric card — shows a KPI with change indicator
st.metric(
    label="Total Revenue",       # card title
    value="$1.2M",               # main number
    delta="+12%"                  # green/red change badge
)</code></pre>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">For more advanced charts, you can also pass Matplotlib, Plotly, or Altair figures to <code class="font-mono text-xs">st.pyplot()</code>, <code class="font-mono text-xs">st.plotly_chart()</code>, or <code class="font-mono text-xs">st.altair_chart()</code>.</p>
                </div>
              </div>
            </div>
          </div>
          <!-- KC Panel 4 — Dashboard Layout (orange) -->
          <div class="kc-panel kc-panel-anim hidden" data-color="orange" role="tabpanel">
            <div class="rounded-2xl border border-orange-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-orange-500 via-amber-400 to-yellow-300"></div>
              <div class="bg-gradient-to-br from-orange-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-orange-500 to-amber-600 shrink-0 shadow-md"><span class="iconify text-white text-sm" data-icon="fa6-solid:gauge-high"></span></span>
                    <div><h3 class="text-sm font-bold text-gray-900">Dashboard Layout</h3><p class="text-[10px] text-gray-400">Columns, sidebar, and structure</p></div>
                  </div>
                  <span class="inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-orange-100 to-amber-100 text-orange-600">Layout</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">Streamlit renders components top-to-bottom by default, but you can arrange them side-by-side using <code class="font-mono text-xs bg-orange-50 text-orange-700 px-1 rounded">st.columns()</code> and move filters into a collapsible sidebar using <code class="font-mono text-xs bg-orange-50 text-orange-700 px-1 rounded">st.sidebar</code>. This lets you build professional two-column or sidebar-based dashboard layouts with just a few lines of Python.</p>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2"><span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span><span class="text-[11px] font-semibold text-gray-400">Python</span></div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># sidebar — put filters in a collapsible panel
region = st.sidebar.selectbox("Region", df["region"].unique())

# columns — arrange KPIs side by side
col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$1.2M", "+12%")
col2.metric("Orders", "3,421", "+8%")
col3.metric("Avg Order", "$351", "-2%")</code></pre>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Use <code class="font-mono text-xs">st.sidebar</code> for all your filters and controls &mdash; this keeps the main area clean for charts and tables, and users can collapse the sidebar when they do not need it.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ CODE EXAMPLES ═══════════════════ -->
<section id="code-examples">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:code"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Code Examples</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Hands-on code snippets to explore the concepts</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Hello Streamlit</span></button>
        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Display Data</span></button>
        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">User Input</span></button>
        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Charts &amp; Metrics</span></button>
        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Full Dashboard</span></button>
      </div>'''

# ── CE panels (Style A with terminal pane) ──────────────────────────────
ce_panels = [
    {
        "idx": "01", "title": "Hello Streamlit", "desc": "Create and launch your very first Streamlit app",
        "file": "hello_streamlit.py",
        "code": '''import streamlit as st          # import the library

st.title("My First App")       # large heading at top
st.write("Hello, Streamlit!")   # display a line of text
st.write("This app was built with **only Python**.")''',
        "terminal_cmd": "streamlit run hello_streamlit.py",
        "terminal_out": '''  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.42:8501''',
        "tip": "Streamlit watches your file for changes. When you save, the browser reloads automatically &mdash; no need to restart the server."
    },
    {
        "idx": "02", "title": "Display Data", "desc": "Load a CSV and show it as an interactive table",
        "file": "display_data.py",
        "code": '''import streamlit as st
import pandas as pd

# load the dataset from a CSV file
df = pd.read_csv("sales.csv")

st.title("Sales Data Viewer")   # page heading
st.write(f"Rows: {{len(df)}}")     # show row count

# render an interactive, sortable table
st.dataframe(df)''',
        "terminal_cmd": "streamlit run display_data.py",
        "terminal_out": '''  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501''',
        "tip": "<code class='font-mono text-xs'>st.dataframe()</code> is better than <code class='font-mono text-xs'>st.write()</code> for tables because it adds sorting, column resizing, and search built in."
    },
    {
        "idx": "03", "title": "User Input", "desc": "Add a dropdown filter that updates the displayed data",
        "file": "user_input.py",
        "code": '''import streamlit as st
import pandas as pd

df = pd.read_csv("sales.csv")

st.title("Filtered Sales")

# selectbox returns the user's chosen string
region = st.selectbox(
    "Select a Region",                 # label shown above the dropdown
    df["region"].unique()              # list of options
)

# filter the DataFrame to the selected region
filtered = df[df["region"] == region]

st.write(f"Showing {{len(filtered)}} rows for **{{region}}**")
st.dataframe(filtered)''',
        "terminal_cmd": "streamlit run user_input.py",
        "terminal_out": '''  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501''',
        "tip": "Every time the user picks a different region, Streamlit reruns the entire script from top to bottom with the new value. You do not need to write any event-listener code."
    },
    {
        "idx": "04", "title": "Charts &amp; Metrics", "desc": "Visualize data with built-in chart and metric components",
        "file": "charts_metrics.py",
        "code": '''import streamlit as st
import pandas as pd

df = pd.read_csv("sales.csv")

st.title("Sales Performance")

# three metric cards in a row
col1, col2, col3 = st.columns(3)      # create 3 columns
col1.metric("Total Revenue", "$1.2M", "+12%")
col2.metric("Total Orders", "3,421", "+8%")
col3.metric("Avg Order Value", "$351", "-2%")

# bar chart from a DataFrame column
st.subheader("Revenue by Region")
chart_data = df.groupby("region")["sales"].sum()
st.bar_chart(chart_data)''',
        "terminal_cmd": "streamlit run charts_metrics.py",
        "terminal_out": '''  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501''',
        "tip": "<code class='font-mono text-xs'>st.metric()</code> accepts a <code class='font-mono text-xs'>delta</code> parameter that shows green (positive) or red (negative) badges &mdash; perfect for KPI dashboards."
    },
    {
        "idx": "05", "title": "Full Dashboard", "desc": "Combine sidebar filters, metrics, and charts into one app",
        "file": "full_dashboard.py",
        "code": '''import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

@st.cache_data                         # cache the file read
def load_data():
    return pd.read_csv("sales.csv")

df = load_data()

st.title("Sales Dashboard")

# sidebar filters
region = st.sidebar.selectbox("Region", ["All"] + list(df["region"].unique()))
min_sales = st.sidebar.slider("Min Sales", 0, int(df["sales"].max()), 0)

# apply filters
filtered = df.copy()
if region != "All":
    filtered = filtered[filtered["region"] == region]
filtered = filtered[filtered["sales"] >= min_sales]

# metrics row
col1, col2, col3 = st.columns(3)
col1.metric("Rows", f"{{len(filtered):,}}")
col2.metric("Total Sales", f"${{filtered['sales'].sum():,.0f}}")
col3.metric("Avg Sale", f"${{filtered['sales'].mean():,.0f}}")

# chart
st.bar_chart(filtered.groupby("region")["sales"].sum())

# data table
st.dataframe(filtered)''',
        "terminal_cmd": "streamlit run full_dashboard.py",
        "terminal_out": '''  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501''',
        "tip": "The <code class='font-mono text-xs'>@st.cache_data</code> decorator prevents the CSV from being re-read on every interaction. Without it, large files will slow down your dashboard significantly."
    }
]

for i, ce in enumerate(ce_panels):
    hidden = " hidden" if i > 0 else ""
    html += f'''
      <div class="ce-panel ce-panel-anim{hidden}" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{ce["idx"]}</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:code"></span></span>
              <div>
                <h3 class="font-bold text-gray-800">{ce["title"]}</h3>
                <p class="text-xs text-gray-500 mt-0.5">{ce["desc"]}</p>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">{ce["file"]}</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">{ce["code"]}</code></pre></div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ {ce["terminal_cmd"]}</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed whitespace-pre">{ce["terminal_out"]}</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">{ce["tip"]}</p>
            </div>
          </div>
        </div>
      </div>'''

html += '''
    </div>
  </div>
</section>

<!-- ═══════════════════ COMPARISON ═══════════════════ -->
<section id="comparison">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:scale-balanced"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">SQL / Excel Comparison</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How Streamlit concepts map to tools you already know</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-5">
      <div class="grid grid-cols-3 gap-3 mb-4">
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white"><span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python / Streamlit</div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white"><span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL</div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white"><span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel</div>
      </div>'''

# Comparison rows
comp_rows = [
    {"label": "Display Data", "icon": "fa6-solid:table", "py": "st.dataframe(df)", "py_desc": "Renders an interactive sortable table in the browser.", "sql": "SELECT * FROM sales", "sql_desc": "Returns all rows from the sales table.", "xl": "Open file → View sheet", "xl_desc": "Data appears in a grid when you open the file."},
    {"label": "Filter Rows", "icon": "fa6-solid:filter", "py": "st.selectbox() + boolean mask", "py_desc": "User picks a value from a dropdown; the DataFrame filters reactively.", "sql": "WHERE region = 'West'", "sql_desc": "Filters rows in the query itself.", "xl": "Data → Filter → Column dropdown", "xl_desc": "Excel's AutoFilter narrows visible rows to the selected value."},
    {"label": "Bar Chart", "icon": "fa6-solid:chart-column", "py": "st.bar_chart(df)", "py_desc": "One-line call that renders a responsive bar chart from a DataFrame.", "sql": "BI tool (Tableau, Power BI)", "sql_desc": "SQL itself does not render charts; a BI layer is needed.", "xl": "Insert → Chart → Bar", "xl_desc": "Select data range and insert a bar chart."},
    {"label": "KPI Summary", "icon": "fa6-solid:gauge-high", "py": 'st.metric("Revenue", "$1.2M", "+12%")', "py_desc": "Displays a metric card with value and delta indicator.", "sql": "SELECT SUM(sales) FROM ...", "sql_desc": "Aggregation query returns a number but no visual card.", "xl": "Cell with SUM() formula", "xl_desc": "A cell formula calculates the total; formatting is manual."},
    {"label": "Multi-Column Layout", "icon": "fa6-solid:columns", "py": "st.columns(3)", "py_desc": "Arranges widgets side-by-side in a flexible column grid.", "sql": "n/a", "sql_desc": "SQL has no layout concept; the BI tool handles positioning.", "xl": "Drag charts / cells", "xl_desc": "You manually position charts and cells on the sheet."},
]

for j, row in enumerate(comp_rows):
    if j > 0:
        html += '''
      <div class="flex items-center gap-3 my-4">
        <span class="flex-1 h-px bg-gray-100"></span>
        <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0"><span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span></span>
        <span class="flex-1 h-px bg-gray-100"></span>
      </div>'''
    html += f'''
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="{row["icon"]}"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">{row["label"]}</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">{row["py"]}</code>
            <p class="text-xs text-gray-500 leading-relaxed">{row["py_desc"]}</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">{row["sql"]}</code>
            <p class="text-xs text-gray-500 leading-relaxed">{row["sql_desc"]}</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">{row["xl"]}</code>
            <p class="text-xs text-gray-500 leading-relaxed">{row["xl_desc"]}</p>
          </div>
        </div>
      </div>'''

html += '''
    </div>
  </div>
</section>

<!-- ═══════════════════ PRACTICE ═══════════════════ -->
<section id="practice">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Guided exercises to reinforce your learning</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Your First App</span></button>
        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Load &amp; Display</span></button>
        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Add a Filter</span></button>
        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Add a Chart</span></button>
        <button onclick="switchPeTab(4)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Mini Dashboard</span></button>
      </div>'''

pe_panels = [
    {"idx":"01","title":"Your First App","tasks":["1. Create a new file called <code class='font-mono'>my_app.py</code>","2. Import Streamlit and add a title with your name","3. Add a <code class='font-mono'>st.write()</code> call that displays today's date","4. Run the app with <code class='font-mono'>streamlit run my_app.py</code>"],
     "code":"import streamlit as st\nfrom datetime import date\n\nst.title(\"My App — Jane\")            # your name here\nst.write(f\"Today is {date.today()}\")  # display the date","why":"This confirms your Streamlit installation works and teaches the basic write-and-run cycle you will use for every project."},
    {"idx":"02","title":"Load &amp; Display","tasks":["1. Import pandas and load <code class='font-mono'>sales.csv</code>","2. Display the DataFrame shape using <code class='font-mono'>st.write()</code>","3. Show the full table with <code class='font-mono'>st.dataframe()</code>","4. Verify you can sort columns by clicking the headers"],
     "code":"import streamlit as st\nimport pandas as pd\n\ndf = pd.read_csv(\"sales.csv\")\nst.title(\"Sales Data\")\nst.write(f\"Shape: {df.shape[0]} rows × {df.shape[1]} columns\")\nst.dataframe(df)","why":"Loading and displaying data is the first step of every analytics dashboard — you need to see the data before you can filter or chart it."},
    {"idx":"03","title":"Add a Filter","tasks":["1. Add a <code class='font-mono'>st.selectbox()</code> for the region column","2. Filter the DataFrame to the selected region","3. Display the filtered row count with <code class='font-mono'>st.write()</code>","4. Show the filtered DataFrame with <code class='font-mono'>st.dataframe()</code>"],
     "code":"import streamlit as st\nimport pandas as pd\n\ndf = pd.read_csv(\"sales.csv\")\nst.title(\"Filtered Sales\")\n\nregion = st.selectbox(\"Region\", df[\"region\"].unique())\nfiltered = df[df[\"region\"] == region]\n\nst.write(f\"Showing {len(filtered)} rows\")\nst.dataframe(filtered)","why":"Interactive filters are what distinguish a dashboard from a static report — they let stakeholders explore the data themselves."},
    {"idx":"04","title":"Add a Chart","tasks":["1. Group sales by region and compute the sum","2. Display the result as a bar chart with <code class='font-mono'>st.bar_chart()</code>","3. Add a <code class='font-mono'>st.metric()</code> card showing total sales"],
     "code":"import streamlit as st\nimport pandas as pd\n\ndf = pd.read_csv(\"sales.csv\")\nst.title(\"Sales Charts\")\n\nst.metric(\"Total Sales\", f\"${df['sales'].sum():,.0f}\")\nst.bar_chart(df.groupby(\"region\")[\"sales\"].sum())","why":"Visualizations make patterns visible at a glance — a bar chart reveals which region leads in seconds, while a raw table takes minutes to scan."},
    {"idx":"05","title":"Mini Dashboard","tasks":["1. Put a selectbox and slider in <code class='font-mono'>st.sidebar</code>","2. Filter the DataFrame by both the dropdown and slider values","3. Display three <code class='font-mono'>st.metric()</code> cards in a <code class='font-mono'>st.columns(3)</code> row","4. Show a bar chart of the filtered data below the metrics"],
     "code":"import streamlit as st\nimport pandas as pd\n\ndf = pd.read_csv(\"sales.csv\")\nst.title(\"Mini Dashboard\")\n\nregion = st.sidebar.selectbox(\"Region\", [\"All\"] + list(df[\"region\"].unique()))\nmin_sales = st.sidebar.slider(\"Min Sales\", 0, int(df[\"sales\"].max()), 0)\n\ndata = df.copy()\nif region != \"All\":\n    data = data[data[\"region\"] == region]\ndata = data[data[\"sales\"] >= min_sales]\n\nc1, c2, c3 = st.columns(3)\nc1.metric(\"Rows\", f\"{len(data):,}\")\nc2.metric(\"Total\", f\"${data['sales'].sum():,.0f}\")\nc3.metric(\"Avg\", f\"${data['sales'].mean():,.0f}\")\n\nst.bar_chart(data.groupby(\"region\")[\"sales\"].sum())","why":"Combining sidebar filters, metric cards, and charts into one file is the core pattern for every Streamlit dashboard you will build in your career."},
]

for i, pe in enumerate(pe_panels):
    hidden = " hidden" if i > 0 else ""
    tasks_html = "\n".join(f'        <p class="text-sm text-gray-600">{t}</p>' for t in pe["tasks"])
    html += f'''
      <div class="pe-panel pe-panel-anim{hidden}" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{pe["idx"]}</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:pencil"></span></span>
              <div><h3 class="font-bold text-gray-800">{pe["title"]}</h3></div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Your Task</p>
{tasks_html}
              </div>
            </div>
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Solution
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>
            <div class="accordion-body">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">solution_{pe["idx"]}.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">{pe["code"]}</code></pre></div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600"><strong>Why this matters:</strong> {pe["why"]}</p>
              </div>
            </div>
          </div>
        </div>
      </div>'''

html += '''
    </div>
  </div>
</section>

<!-- ═══════════════════ MISTAKES ═══════════════════ -->
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Frequent errors and how to avoid them</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">python vs streamlit run</span></button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">Missing import</span></button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">No cache on load</span></button>
        <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">Filtering original df</span></button>
        <button onclick="switchMkTab(4)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">Widget key collisions</span></button>
      </div>'''

mk_panels = [
    {"title":"Running with python instead of streamlit run","why":"Beginners instinctively type <code class='font-mono text-xs'>python app.py</code> because that is how they have always run scripts. But Streamlit needs its own server to render the UI.","wrong":"python app.py","correct":"streamlit run app.py","lang":"bash","fix":"Always use <code class='font-mono text-xs'>streamlit run</code> to launch Streamlit apps. The <code class='font-mono text-xs'>python</code> command executes the file but never starts the web server, so nothing appears in the browser."},
    {"title":"Forgetting to import streamlit","why":"If you jump straight into writing <code class='font-mono text-xs'>st.title()</code> without the import, Python raises a <code class='font-mono text-xs'>NameError</code> because <code class='font-mono text-xs'>st</code> is undefined.","wrong":"st.title(\"Dashboard\")  # NameError!","correct":"import streamlit as st\nst.title(\"Dashboard\")","lang":"python","fix":"Always start your Streamlit files with <code class='font-mono text-xs'>import streamlit as st</code> on the very first line. It is the most common first-line import in any Streamlit project."},
    {"title":"Loading data without @st.cache_data","why":"Streamlit reruns the entire script on every interaction, so a <code class='font-mono text-xs'>pd.read_csv()</code> call at the top level will re-read the file every time a user changes a widget &mdash; this is invisible until the file is large.","wrong":"df = pd.read_csv(\"big_data.csv\")\nst.selectbox(\"Filter\", df[\"col\"].unique())","correct":"@st.cache_data\ndef load():\n    return pd.read_csv(\"big_data.csv\")\n\ndf = load()\nst.selectbox(\"Filter\", df[\"col\"].unique())","lang":"python","fix":"Wrap any expensive operation (file reads, API calls, heavy computations) in a function decorated with <code class='font-mono text-xs'>@st.cache_data</code>. Streamlit will cache the result and skip the function on reruns."},
    {"title":"Filtering the original DataFrame instead of a copy","why":"If you write <code class='font-mono text-xs'>df = df[df[\"region\"] == region]</code>, you permanently shrink <code class='font-mono text-xs'>df</code> on every rerun. With caching, the original data still exists, but without caching the filtered result carries forward and you lose rows.","wrong":"df = df[df[\"region\"] == region]\nst.dataframe(df)","correct":"filtered = df[df[\"region\"] == region]\nst.dataframe(filtered)","lang":"python","fix":"Always assign filtered results to a <strong>new variable</strong> like <code class='font-mono text-xs'>filtered</code> instead of overwriting <code class='font-mono text-xs'>df</code>. This keeps the original DataFrame intact for the next rerun."},
    {"title":"Duplicate widget keys when reusing components","why":"If you create two <code class='font-mono text-xs'>st.selectbox()</code> calls with the same label, Streamlit raises a <code class='font-mono text-xs'>DuplicateWidgetID</code> error because it cannot tell them apart.","wrong":"a = st.selectbox(\"Pick\", [1,2,3])\nb = st.selectbox(\"Pick\", [4,5,6])","correct":"a = st.selectbox(\"Pick\", [1,2,3], key=\"pick_a\")\nb = st.selectbox(\"Pick\", [4,5,6], key=\"pick_b\")","lang":"python","fix":"Add a unique <code class='font-mono text-xs'>key=</code> parameter to any widget that shares a label with another widget. The key string must be unique across your entire app."},
]

for i, mk in enumerate(mk_panels):
    hidden = " hidden" if i > 0 else ""
    html += f'''
      <div class="mk-panel mk-panel-anim{hidden}" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0"><span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span></span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
              <p class="text-xs text-gray-500 mt-0.5">{mk["why"]}</p>
            </div>
          </div>
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong</p>
              <div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-{mk["lang"]}">{mk["wrong"]}</code></pre></div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200"><span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span></span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct</p>
              <div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-{mk["lang"]}">{mk["correct"]}</code></pre></div>
            </div>
          </div>
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">{mk["fix"]}</p>
          </div>
        </div>
      </div>'''

html += '''
    </div>
  </div>
</section>

<!-- ═══════════════════ REAL-WORLD ═══════════════════ -->
<section id="real-world">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:briefcase"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Real-World Use</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How teams use Streamlit in practice</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="rounded-xl p-5 flex items-start gap-4 border border-[#f5c6e0] bg-[#fdf0f7]">
        <span class="iconify mt-0.5 shrink-0 text-xl text-[#CB187D]" data-icon="fa6-solid:earth-americas"></span>
        <p class="text-sm text-gray-700 leading-relaxed">Streamlit is used by thousands of data teams worldwide to replace ad-hoc email reports with live, self-service dashboards that stakeholders can explore without writing code.</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        <div class="group flex items-center gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
          <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]"><span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="fa6-solid:chart-line"></span></div>
          <span class="text-sm text-gray-700">Sales performance dashboards</span>
        </div>
        <div class="group flex items-center gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
          <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]"><span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="fa6-solid:robot"></span></div>
          <span class="text-sm text-gray-700">Machine learning model demos</span>
        </div>
        <div class="group flex items-center gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
          <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]"><span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="fa6-solid:magnifying-glass-chart"></span></div>
          <span class="text-sm text-gray-700">Data quality monitoring tools</span>
        </div>
        <div class="group flex items-center gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
          <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]"><span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="fa6-solid:building"></span></div>
          <span class="text-sm text-gray-700">Internal analytics portals</span>
        </div>
        <div class="group flex items-center gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
          <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]"><span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="fa6-solid:flask"></span></div>
          <span class="text-sm text-gray-700">Experiment tracking interfaces</span>
        </div>
        <div class="group flex items-center gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
          <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]"><span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="fa6-solid:file-invoice"></span></div>
          <span class="text-sm text-gray-700">Automated report generators</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ RECAP ═══════════════════ -->
<section id="recap">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:list-check"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Recap</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A quick summary of what you learned</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">'''

recap_items = [
    ("01", "fa6-solid:check", "What Streamlit Is", "You learned that Streamlit is an open-source Python library that converts plain <code class='font-mono'>*.py</code> scripts into interactive web apps without any frontend code."),
    ("02", "fa6-solid:check", "Install &amp; Run", "You learned to install Streamlit with <code class='font-mono'>pip install streamlit</code> and launch apps with <code class='font-mono'>streamlit run app.py</code>."),
    ("03", "fa6-solid:check", "Display &amp; Input", "You learned to display data with <code class='font-mono'>st.write()</code> and <code class='font-mono'>st.dataframe()</code>, and capture user input with <code class='font-mono'>st.selectbox()</code> and <code class='font-mono'>st.slider()</code>."),
    ("04", "fa6-solid:check", "Charts &amp; Metrics", "You learned to create bar charts, line charts, and metric KPI cards by passing DataFrames directly to Streamlit&rsquo;s built-in chart functions."),
    ("05", "fa6-solid:check", "Interactive Dashboard", "You learned to combine sidebar filters, metric columns, and charts into a complete, reactive dashboard that updates on every user interaction."),
]

for num, icon, title, desc in recap_items:
    html += f'''
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num}</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5"><span class="iconify text-sm" data-icon="{icon}"></span></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">{title}</p>
                <p class="text-[11px] text-gray-600 leading-snug">{desc}</p>
              </div>
            </div>
          </div>
        </div>'''

html += '''
      </div>
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0"><span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span></span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 5 key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ KNOWLEDGE CHECK ═══════════════════ -->
<section id="knowledge-check">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:brain"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Knowledge Check</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5">Test your understanding before moving on</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 1</span></button>
        <button onclick="switchQzTab(1)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 2</span></button>
        <button onclick="switchQzTab(2)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 3</span></button>
        <button onclick="switchQzTab(3)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 4</span></button>
        <button onclick="switchQzTab(4)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 5</span></button>
      </div>'''

qz_panels = [
    {"num":"Q1","type":"Multiple Choice","q":"Which command correctly launches a Streamlit app in the browser?",
     "opts":[("python app.py",False),("streamlit run app.py",True),("flask run app.py",False),("pip run app.py",False)],
     "fb_correct":"Correct! <code class='font-mono text-xs'>streamlit run</code> starts both the server and opens the browser.",
     "fb_wrong":"Not quite — <code class='font-mono text-xs'>streamlit run app.py</code> is the correct command. <code class='font-mono text-xs'>python app.py</code> runs the script but does not start the web server."},
    {"num":"Q2","type":"True or False","q":"Streamlit requires you to write HTML and CSS to build the user interface. True or False?",
     "opts":[("True",False),("False",True)],
     "fb_correct":"Correct! Streamlit generates the entire UI from Python code — no HTML or CSS needed.",
     "fb_wrong":"Not quite — Streamlit generates all HTML and CSS automatically from your Python code."},
    {"num":"Q3","type":"Multiple Choice","q":"What does <code class='font-mono'>st.selectbox(\"Region\", options)</code> return?",
     "opts":[("A Streamlit widget object",False),("The selected string value",True),("A list of all options",False),("None",False)],
     "fb_correct":"Correct! Streamlit widgets return the user's current selection as a plain Python value.",
     "fb_wrong":"Not quite — <code class='font-mono text-xs'>st.selectbox()</code> returns the selected value as a string, not a widget object."},
    {"num":"Q4","type":"Multiple Choice","q":"Your dashboard loads a 500 MB CSV and feels slow after every click. Which fix is most appropriate?",
     "opts":[("Use st.write() instead of st.dataframe()",False),("Add @st.cache_data to the load function",True),("Remove the selectbox widget",False),("Switch from pandas to a list",False)],
     "fb_correct":"Correct! <code class='font-mono text-xs'>@st.cache_data</code> caches the result so the file is only read once, not on every rerun.",
     "fb_wrong":"Not quite — the best fix is to decorate the data-loading function with <code class='font-mono text-xs'>@st.cache_data</code> so it runs only once."},
    {"num":"Q5","type":"True or False","q":"When a user changes a slider value, Streamlit only reruns the code related to that slider. True or False?",
     "opts":[("True",False),("False",True)],
     "fb_correct":"Correct! Streamlit reruns the <strong>entire script</strong> from top to bottom on every interaction, not just the changed widget.",
     "fb_wrong":"Not quite — Streamlit reruns the entire Python script from top to bottom on every interaction."},
]

for i, qz in enumerate(qz_panels):
    hidden = " hidden" if i > 0 else ""
    opts_html = ""
    if len(qz["opts"]) == 2 and qz["type"] == "True or False":
        for label, correct in qz["opts"]:
            hover = "hover:border-[#CB187D] hover:bg-[#fdf0f7]" if correct else "hover:border-red-400 hover:bg-red-50"
            icon = "fa6-solid:check" if label == "True" else "fa6-solid:xmark"
            opts_html += f'            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 {hover} transition-colors" onclick="checkQuiz(this, {str(correct).lower()})"><span class="iconify mr-1.5" data-icon="{icon}"></span> {label}</button>\n'
        opts_html = f'          <div class="flex gap-3">\n{opts_html}          </div>'
    else:
        opts_html = '          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">\n'
        for label, correct in qz["opts"]:
            opts_html += f'            <button class="quiz-btn w-full text-left px-5 py-3 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, {str(correct).lower()})"><code class="font-mono text-xs">{label}</code></button>\n'
        opts_html += '          </div>'

    # Escape quotes for data attributes
    fb_c = qz["fb_correct"].replace('"', '&quot;')
    fb_w = qz["fb_wrong"].replace('"', '&quot;')
    html += f'''
      <div class="qz-panel qz-panel-anim{hidden}" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{qz["num"]}</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:circle-question"></span></span>
              <div><h3 class="font-bold text-gray-800">{qz["type"]}</h3><p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p></div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q{i}" data-fb-correct="{fb_c}" data-fb-wrong="{fb_w}">
              <p class="text-sm font-semibold text-gray-800 mb-4">{qz["q"]}</p>
{opts_html}
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>
        </div>
      </div>'''

# ── Next Lesson + Bottom Nav ──────────────────────────────────
html += '''
    </div>
  </div>
</section>

<!-- ═══════════════════ NEXT LESSON ═══════════════════ -->
<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">3</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 5 &middot; Lesson 3</p>
          <h3 class="text-base font-bold text-gray-800">Interactive Filters</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="fa6-solid:sliders"></span></span>
            <div><p class="text-sm font-semibold text-gray-700">Dropdown &amp; slider filters</p></div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="fa6-solid:rotate"></span></span>
            <div><p class="text-sm font-semibold text-gray-700">Dynamic data updates</p></div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="fa6-solid:gauge-high"></span></span>
            <div><p class="text-sm font-semibold text-gray-700">Reactive dashboards</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Bottom nav -->
<section>
  <div class="flex flex-col sm:flex-row gap-3">
    <a href="lesson01_why_build_data_apps.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all no-underline">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Why Build Data Apps?</p>
      </div>
    </a>
    <a href="../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full no-underline">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>
    <a href="lesson03_interactive_filters.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right no-underline">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Interactive Filters</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>
  </div>
</section>

      </main>
    </div>
  </div>

  <footer class="border-t border-gray-100 bg-white py-8">
    <div class="max-w-[1280px] mx-auto px-4 text-center">
      <p class="text-xs text-gray-400">
        <span class="iconify inline text-sm mr-1" data-icon="logos:python"></span>
        Python Learning Hub &middot; Track 4 &mdash; Data Applications &middot; Building Data Applications
      </p>
    </div>
  </footer>
</div>

<script>
  function toggleToc() {
    const sidebar = document.querySelector('.lesson-toc-sidebar');
    const icon = document.getElementById('toc-toggle-icon');
    const collapsed = sidebar.classList.toggle('toc-collapsed');
    icon.setAttribute('data-icon', collapsed ? 'fa6-solid:angles-right' : 'fa6-solid:angles-left');
    if (window.Iconify) Iconify.scan();
  }

  const tocLinks = document.querySelectorAll('.toc-link');
  const sections = [...tocLinks].map(link => document.getElementById(link.getAttribute('href').replace('#', ''))).filter(Boolean);
  function updateScrollSpy() {
    let currentId = '';
    sections.forEach(section => { if (window.scrollY >= section.offsetTop - 120) currentId = section.id; });
    tocLinks.forEach(link => { link.classList.toggle('active', link.getAttribute('href') === '#' + currentId); });
  }
  function updateScrollProgress() {
    const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    document.getElementById('scroll-progress').style.width = (height > 0 ? (winScroll / height) * 100 : 0) + '%';
  }
  function updateBackToTop() { document.getElementById('back-to-top').classList.toggle('visible', window.scrollY > 400); }
  window.addEventListener('scroll', () => { updateScrollSpy(); updateScrollProgress(); updateBackToTop(); });

  function copyCode(btn) {
    const container = btn.closest('.rounded-xl') || btn.closest('.relative') || btn.parentElement.closest('div');
    const pre = container ? container.querySelector('pre') : null;
    const text = pre ? pre.innerText : '';
    function showFeedback() {
      const orig = btn.innerHTML;
      btn.innerHTML = '<span class="iconify mr-1" data-icon="fa6-solid:check"></span>Copied!';
      btn.style.background = 'rgba(34,197,94,0.2)'; btn.style.borderColor = 'rgba(34,197,94,0.5)'; btn.style.color = '#4ade80';
      setTimeout(() => { btn.innerHTML = orig; btn.style.background = ''; btn.style.borderColor = ''; btn.style.color = ''; }, 2000);
    }
    function fallbackCopy() {
      const ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); } catch (e) {} document.body.removeChild(ta); showFeedback();
    }
    if (navigator.clipboard && window.isSecureContext) { navigator.clipboard.writeText(text).then(showFeedback).catch(fallbackCopy); } else { fallbackCopy(); }
  }

  function toggleAccordion(btn) {
    const body = btn.nextElementSibling;
    const isOpen = body.classList.contains('open');
    btn.classList.toggle('open', !isOpen);
    body.classList.toggle('open', !isOpen);
    if (!isOpen && window.Prism) Prism.highlightAllUnder(body);
  }

  const kcColors = [
    { num: '#CB187D', numShadow: 'rgba(203,24,125,0.25)', activeBg: '#fdf0f7' },
    { num: '#7c3aed', numShadow: 'rgba(124,58,237,0.25)', activeBg: '#f5f3ff' },
    { num: '#2563eb', numShadow: 'rgba(37,99,235,0.25)',  activeBg: '#eff6ff' },
    { num: '#059669', numShadow: 'rgba(5,150,105,0.25)',  activeBg: '#ecfdf5' },
    { num: '#c74905', numShadow: 'rgba(199,73,5,0.25)',   activeBg: '#ffddb3' }
  ];
  function switchKcTab(idx) {
    const c = kcColors[idx % kcColors.length];
    const tabs = document.querySelectorAll('.kc-tab');
    const panels = document.querySelectorAll('.kc-panel');
    const indicator = document.querySelector('.kc-indicator');
    tabs.forEach((t, i) => {
      const num = t.querySelector('.kc-tab-num');
      const label = t.querySelector('.kc-tab-label');
      if (i === idx) {
        t.classList.add('kc-tab-active'); t.style.background = c.activeBg;
        if (num) { num.style.background = c.num; num.style.color = '#fff'; num.style.boxShadow = '0 2px 8px ' + c.numShadow; }
        if (label) { label.style.color = '#111827'; }
      } else {
        t.classList.remove('kc-tab-active'); t.style.background = '';
        if (num) { num.style.background = '#f3f4f6'; num.style.color = '#9ca3af'; num.style.boxShadow = 'none'; }
        if (label) { label.style.color = '#9ca3af'; }
      }
    });
    if (indicator && tabs[idx]) { indicator.style.top = tabs[idx].offsetTop + 'px'; indicator.style.height = tabs[idx].offsetHeight + 'px'; indicator.style.background = c.num; }
    panels.forEach((p, i) => { if (i === idx) { p.classList.remove('hidden'); p.classList.remove('kc-panel-anim'); void p.offsetWidth; p.classList.add('kc-panel-anim'); } else { p.classList.add('hidden'); } });
    const visible = panels[idx]; if (visible && window.Prism) Prism.highlightAllUnder(visible);
  }

  function _switchDarkPills(prefix, idx) {
    document.querySelectorAll('.' + prefix + '-step').forEach((s, i) => {
      if (i === idx) {
        s.classList.add(prefix + '-step-active');
        s.style.background = 'linear-gradient(to right, #CB187D, #e84aad)'; s.style.color = '#fff';
        s.style.boxShadow = '0 10px 25px -5px rgba(203,24,125,0.3)';
      } else {
        s.classList.remove(prefix + '-step-active');
        s.style.background = '#1f2937'; s.style.color = '#9ca3af'; s.style.boxShadow = 'none';
      }
    });
    document.querySelectorAll('.' + prefix + '-panel').forEach((p, i) => {
      if (i === idx) { p.classList.remove('hidden'); p.classList.remove(prefix + '-panel-anim'); void p.offsetWidth; p.classList.add(prefix + '-panel-anim'); }
      else { p.classList.add('hidden'); }
    });
    const visible = document.querySelectorAll('.' + prefix + '-panel:not(.hidden)')[0];
    if (visible && window.Prism) Prism.highlightAllUnder(visible);
  }
  function switchCeTab(idx) { _switchDarkPills('ce', idx); }
  function switchMkTab(idx) { _switchDarkPills('mk', idx); }
  function switchPeTab(idx) { _switchDarkPills('pe', idx); }
  function switchQzTab(idx) { _switchDarkPills('qz', idx); }

  function checkQuiz(btn, answer) {
    const question = btn.closest('.quiz-question');
    const feedback = question.querySelector('.quiz-feedback');
    const buttons = question.querySelectorAll('.quiz-btn');
    buttons.forEach(b => { b.disabled = true; b.style.opacity = '0.6'; });
    if (answer === true) {
      btn.classList.add('correct'); btn.style.opacity = '1';
      const msg = question.dataset.fbCorrect || 'Correct!';
      feedback.innerHTML = '\\u2713 ' + msg;
      feedback.className = 'quiz-feedback mt-2 text-sm font-medium text-green-600';
    } else {
      btn.classList.add('incorrect'); btn.style.opacity = '1';
      const msg = question.dataset.fbWrong || 'Not quite \\u2014 review the lesson recap above.';
      feedback.innerHTML = '\\u2717 ' + msg;
      feedback.className = 'quiz-feedback mt-2 text-sm font-medium text-red-500';
    }
  }

  document.addEventListener('DOMContentLoaded', () => { if (window.Prism) Prism.highlightAll(); });
</script>

</body>
</html>'''

# Write the file
with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(html)

lines = html.count('\n') + 1
print(f'✅ Wrote {TARGET} ({lines} lines)')

# Quick structural verification
import re
html_part = html.split('<script>')[0]
opens = html_part.count('<div')
closes = html_part.count('</div>')
print(f'   Div balance: {opens - closes} (opens={opens}, closes={closes})')

ce = len(re.findall(r'ce-step-label', html_part))
ce_p = len(re.findall(r'class="ce-panel', html_part))
kc = len(re.findall(r'kc-tab-label', html_part))
kc_p = len(re.findall(r'class="kc-panel', html_part))
pe = len(re.findall(r'pe-step-label', html_part))
pe_p = len(re.findall(r'class="pe-panel', html_part))
mk = len(re.findall(r'mk-step-label', html_part))
mk_p = len(re.findall(r'class="mk-panel', html_part))
qz = len(re.findall(r'qz-step-label', html_part))
qz_p = len(re.findall(r'class="qz-panel', html_part))

print(f'   CE tabs/panels: {ce}/{ce_p}')
print(f'   KC tabs/panels: {kc}/{kc_p}')
print(f'   PE tabs/panels: {pe}/{pe_p}')
print(f'   MK tabs/panels: {mk}/{mk_p}')
print(f'   QZ tabs/panels: {qz}/{qz_p}')

# Check per-section balance
sections_text = re.split(r'<section ', html_part)
for s in sections_text[1:]:  # skip before first section
    sid = re.search(r'id="([^"]*)"', s)
    name = sid.group(1) if sid else '??'
    end = s.find('</section>')
    chunk = s[:end] if end > 0 else s
    o = chunk.count('<div')
    c = chunk.count('</div>')
    b = o - c
    status = '✅' if b == 0 else '❌'
    print(f'   {status} Section #{name}: div balance = {b}')
