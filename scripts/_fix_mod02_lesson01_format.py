"""
Convert lesson01_what_is_programming.html from browser-only format to
Confluence-ready format:
  - Strip DOCTYPE / <html> / <head> / <body> / </body> / </html>
  - Add CDN links at the very top
  - Replace the minimal <style> block with the full CSS (section-comment
    groups + #hub-root Confluence isolation block)
  - Add id="hub-root" to the outer wrapper div
  - Add the correct CSS section comments to the style block
"""

import re
import sys

FILE = 'pages/track_01/mod_02_programming_foundations/lesson01_what_is_programming.html'

with open(FILE, 'r', encoding='utf-8') as f:
    src = f.read()

# ── 1. CDN block ─────────────────────────────────────────────────────────────
CDN = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap">

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Iconify -->
  <script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>

  <!-- Prism.js -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" crossorigin="anonymous">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js" crossorigin="anonymous"></script>"""

# ── 2. Full <style> block ─────────────────────────────────────────────────────
STYLE = """  <style>
    /* ── CSS Variables — font tokens (:root) ──────────────────────── */
    :root {
      --font-body: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'Fira Code', monospace;
    }

    /* ── Global reset — smooth scroll ──────────────────────────── */
    * { scroll-behavior: smooth; }

    /* ── Prism.js — syntax highlighted code blocks ─────────────── */
    pre[class*="language-"] {
      border-radius: 0.75rem;
      font-family: var(--font-mono);
      font-size: 0.875rem;
      margin: 0;
      padding: 1.25rem 1.5rem;
    }
    code[class*="language-"], pre[class*="language-"] {
      background: #1e1e2e;
    }

    /* ── Heading resets — strip Confluence default margins ─────── */
    h1, h2, h3, h4, h5, h6 {
      margin-top: 0;
      margin-bottom: 0;
      padding: 0;
      line-height: 1.3;
    }
    h1 { font-weight: 800 !important; }
    h2 { font-size: 1.25rem; font-weight: 700 !important; }
    h3 { font-size: 1rem;   font-weight: 600 !important; }

    /* ── Brand utility classes ─────────────────────────────────── */
    .text-brand      { color: #CB187D; }
    .text-brand-dark { color: #CB187D; }
    .bg-brand        { background: #CB187D; }
    .bg-brand-soft   { background: #fdf0f7; }
    .brand-soft-panel { background: #fdf0f7; border-color: #f5c6e0; }
    .bg-amber-tip    { background: #fff7ed; border: 1px solid #fed7aa; }
    .bg-code         { background: #1e1e2e; }
    .border-code-sep { border-color: rgba(255, 255, 255, 0.08); }
    .pre-reset       { margin: 0; border-radius: 0; background: transparent; }

    /* ── Key Concepts sidebar tabs  (.kc-tab / .kc-tab-active) ─── */
    .kc-tab-active { background: #fdf0f7; }
    .kc-indicator { height: 68px; }
    .kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }

    /* ── Code Examples pill tabs   (.ce-step / .ce-step-active) ── */
    .ce-step:not(.ce-step-active):hover,
    /* ── Common Mistakes pill tabs (.mk-step / .mk-step-active) ── */
    .mk-step:not(.mk-step-active):hover,
    /* ── Knowledge Check quiz tabs (.qz-step / .qz-step-active) ── */
    .qz-step:not(.qz-step-active):hover,
    /* ── Practice Exercise tabs    (.pe-step / .pe-step-active) ── */
    .pe-step:not(.pe-step-active):hover { background: #374151; color: #ffffff; }

    /* Keyframe used by all tab panel fade-in animations */
    @keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    .kc-panel-anim,
    .ce-panel-anim,
    .mk-panel-anim,
    .qz-panel-anim,
    .pe-panel-anim { animation: kcFadeIn 0.25s ease-out; }

    .ce-step:not(.ce-step-active),
    .mk-step:not(.mk-step-active),
    .qz-step:not(.qz-step-active),
    .pe-step:not(.pe-step-active) { background: #1f2937; color: #ffffff; box-shadow: none; }

    .ce-step-active,
    .mk-step-active,
    .qz-step-active,
    .pe-step-active {
      background: linear-gradient(to right, #CB187D, #e84aad);
      color: #ffffff;
      box-shadow: 0 10px 25px -5px rgba(203, 24, 125, 0.3);
    }

    /* ─── Step tab consistent sizing ──────────────────────────── */
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

    /* ── Accordion — used in Overview & Key Ideas sections ─────── */
    .accordion-body      { display: none  !important; }
    .accordion-body.open { display: block !important; }
    .accordion-toggle {
      display: flex !important; align-items: center !important; gap: 8px !important;
      width: 100% !important; padding: 10px 16px !important; border-radius: 10px !important;
      font-size: 0.8rem !important; font-weight: 600 !important; cursor: pointer !important;
      border: 2px dashed #f5c6e0 !important; background: #fdf0f7 !important;
      color: #CB187D !important; line-height: 1.2 !important; text-decoration: none !important;
      transition: background 0.15s, border-color 0.15s !important;
    }
    .accordion-toggle:hover { background: #f9d9ee !important; border-color: #CB187D !important; }
    .accordion-toggle.open { background: #fdf0f7 !important; border-color: #CB187D !important; border-style: solid !important; }
    .accordion-chevron { margin-left: auto !important; transition: transform 0.2s !important; }
    .accordion-toggle.open .accordion-chevron { transform: rotate(180deg) !important; }

    /* ── Task description box inside practice/example panels ───── */
    .task-box { background: #fdf0f7; border: 1px solid #f5c6e0; }

    /* ── Hero banner — full-width gradient header ──────────────── */
    .hero-container {
      position: relative;
      border-radius: 1.25rem;
      overflow: hidden;
      min-height: 380px;
      background: linear-gradient(135deg, #CB187D 0%, #CB187D 40%, #a31268 65%, #7F004C 100%);
    }
    .hero-dots {
      position: absolute; inset: 0; opacity: 0.06;
      background-image: radial-gradient(circle, rgba(255,255,255,0.7) 1px, transparent 1px);
      background-size: 24px 24px;
    }
    .hero-glow { position: absolute; border-radius: 50%; pointer-events: none; filter: blur(70px); }
    .hero-glow-1 { width: 350px; height: 350px; top: -80px; right: 0; background: rgba(255,255,255,0.12); }
    .hero-glow-2 { width: 280px; height: 280px; bottom: -50px; left: 5%; background: rgba(127,0,76,0.35); }
    .hero-glow-line {
      position: absolute; bottom: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, transparent 0%, #f5c6e0 30%, #CB187D 50%, #f5c6e0 70%, transparent 100%);
      opacity: 0.7;
    }
    .hero-pill { background: #ffffff; border: none; color: #CB187D; font-weight: 700; pointer-events: none; cursor: default; }
    .hero-abstract-card {
      position: relative; border-radius: 1rem; overflow: hidden; padding: 0.25rem;
      opacity: 0.75; display: flex; align-items: center; justify-content: center;
    }
    .hero-cta {
      display: inline-flex; align-items: center; gap: 10px; padding: 11px 26px;
      border-radius: 999px; font-weight: 700; font-size: 0.875rem; color: #CB187D;
      background: #ffffff; border: none; cursor: pointer;
      transition: transform 0.2s ease, filter 0.2s ease; text-decoration: none;
    }
    .hero-cta:hover { transform: translateY(-2px); filter: brightness(0.96); }
    .stat-card { transition: background 0.2s ease; }
    .stat-card:hover { background: rgba(255,255,255,0.15) !important; }

    /* ── Scroll progress bar — fixed top-of-page indicator ─────── */
    .scroll-progress {
      position: fixed; top: 0; left: 0; width: 0; height: 3px;
      background: linear-gradient(90deg, #CB187D, #6366f1, #CB187D);
      background-size: 200% 100%;
      animation: scrollGradient 3s linear infinite;
      z-index: 9999; transition: width 0.15s;
    }
    @keyframes scrollGradient {
      0% { background-position: 0% 0%; }
      100% { background-position: 200% 0%; }
    }

    /* ── Page layout — two-column: TOC sidebar + main content ──── */
    .lesson-layout { display: block; }
    .lesson-toc-sidebar {
      float: right; width: 240px; margin-left: 1.75rem; margin-bottom: 1rem;
      position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem);
      overflow-y: auto; transition: width 0.25s ease, opacity 0.25s ease;
    }
    .lesson-toc-sidebar.toc-collapsed { width: 44px; overflow: hidden; }
    .lesson-toc-sidebar.toc-collapsed .toc-body { display: none; }
    .lesson-toc-sidebar.toc-collapsed .toc-header-label { display: none; }
    .lesson-toc-sidebar.toc-collapsed .toc-module-list { display: none; }
    .toc-toggle-btn {
      background: none; border: none; cursor: pointer; padding: 2px; color: #CB187D;
      display: flex; align-items: center; justify-content: center;
      position: absolute; right: 8px; top: 50%; transform: translateY(-50%);
      border-radius: 6px; transition: background 0.15s;
    }
    .toc-toggle-btn:hover { background: #fdf0f7; }
    .toc-link { transition: color 0.15s, padding-left 0.15s; }
    .toc-link:hover { color: #CB187D; padding-left: 4px; }
    .toc-link.active {
      color: #CB187D; font-weight: 600;
      border-left: 3px solid #CB187D; padding-left: 8px;
    }

    /* ── Objective cards (.obj-card) ────────────────────────────── */
    .obj-card {
      transition: transform 0.22s cubic-bezier(.4,0,.2,1),
                  box-shadow 0.22s cubic-bezier(.4,0,.2,1),
                  border-color 0.22s ease, background-color 0.22s ease;
    }
    .obj-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 32px -6px rgba(203,24,125,0.18), 0 6px 12px -2px rgba(203,24,125,0.1);
      border-color: #CB187D; background-color: #fdf0f7;
    }
    .obj-card .obj-icon { transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease; }
    .obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
    .obj-card:hover .obj-icon .iconify { color: white !important; }

    /* ── Section header components ─────────────────────────────── */
    .section-header {
      display: flex; align-items: center; gap: 1rem;
      padding: 1.25rem 2rem 1.25rem 1rem;
      background: #ffffff; border-bottom: 1px solid #f3f4f6;
      border-left: 4px solid #CB187D;
    }
    .section-icon {
      display: inline-flex; align-items: center; justify-content: center;
      width: 2.75rem; height: 2.75rem; border-radius: 0.75rem;
      background: #CB187D; flex-shrink: 0;
    }
    .section-body { min-width: 0; }
    .section-title { font-size: 1.25rem; font-weight: 700; color: #111827; line-height: 1.3; margin: 0; }
    .section-subtitle { font-size: 0.875rem; color: #9ca3af; line-height: 1.4; margin-top: 0.125rem; margin-bottom: 0; }

    /* ── Skill dots (difficulty indicator) ─────────────────────── */
    .skill-dot {
      width: 6px; height: 6px; border-radius: 50%; background: #d1d5db; display: inline-block;
    }
    .skill-dot-active { background: #22c55e; }

    /* ── Hero SVG illustration ──────────────────────────────────── */
    .hero-svg { max-height: 320px; }
    .hero-py-icon-wrap { display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; }
    .hero-py-icon { font-size: 70px; filter: drop-shadow(0 0 14px rgba(255,212,59,0.25)); }

    /* ── Generic outline tab buttons (.tab-btn / .tab-panel) ───── */
    .tab-btn {
      display: inline-flex; align-items: center; gap: 6px; padding: 7px 18px;
      font-size: 0.82rem; font-weight: 600; cursor: pointer;
      border: 1.5px solid #e5e7eb; border-radius: 999px; color: #6b7280; background: #fff;
      line-height: 1.2; transition: color 0.15s, background 0.15s, border-color 0.15s;
    }
    .tab-btn:hover { color: #CB187D; border-color: #CB187D; background: #fdf0f7; }
    .tab-btn.active { color: #fff; background: #CB187D; border-color: #CB187D; }
    .tab-panel { display: none; }
    .tab-panel.active { display: block; }

    /* ── Code block copy button (.copy-btn) ────────────────────── */
    .copy-btn {
      position: absolute; top: 10px; right: 12px; display: inline-flex; align-items: center;
      background: rgba(203,24,125,0.15); border: 1px solid rgba(203,24,125,0.3); color: #CB187D;
      border-radius: 6px; padding: 3px 8px; font-size: 0.65rem; font-weight: 600;
      cursor: pointer; transition: background 0.2s; white-space: nowrap;
    }
    .copy-btn:hover { background: rgba(203,24,125,0.3); }
    .copy-btn-light {
      position: static; color: #fff; border-color: rgba(255,255,255,0.25); background: rgba(255,255,255,0.1);
    }
    .copy-btn-light:hover { background: rgba(255,255,255,0.2); }

    /* ── Bottom lesson navigation — Previous / All Lessons / Next  */
    .lesson-nav-link:hover p,
    .lesson-nav-link:hover span,
    .lesson-nav-link:hover svg { color: #CB187D; transition: color 0.15s; }

    /* ── Back-to-top floating button ───────────────────────────── */
    .back-to-top {
      position: fixed; bottom: 2rem; right: 2rem; width: 44px; height: 44px;
      border-radius: 50%; background: #CB187D; color: white;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 4px 12px rgba(203,24,125,0.3); cursor: pointer;
      opacity: 0; transform: translateY(10px);
      transition: opacity 0.3s, transform 0.3s; z-index: 50; border: none;
    }
    .back-to-top.visible { opacity: 1; transform: translateY(0); }
    .back-to-top:hover { background: #7F004C; }

    /* ── Quiz answer feedback buttons (.quiz-btn.correct / .incorrect)  */
    .quiz-btn.correct { background: #f0fdf4; border-color: #22c55e; color: #16a34a; }
    .quiz-btn.incorrect { background: #fef2f2; border-color: #ef4444; color: #dc2626; }

    /* ── Card hover animations — Mistake, Flow, Recap, Overview cards  */
    .mistake-card { transition: transform 0.18s ease, box-shadow 0.18s ease; }
    .mistake-card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px -5px rgba(0,0,0,0.08); }
    .flow-stepper .flow-step { transition: transform 0.15s ease; }
    .flow-stepper .flow-step:hover { transform: translateX(4px); }
    .recap-item { transition: transform 0.15s ease, box-shadow 0.15s ease; }
    .recap-item:hover { transform: translateX(4px); box-shadow: -4px 0 0 0 #10b981; }
    .overview-card { transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease; }
    .overview-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 12px 30px -6px rgba(203,24,125,0.12);
      border-color: rgba(203,24,125,0.3);
    }

    /* ── Responsive — mobile breakpoint (<768px) ───────────────── */
    @media (max-width: 767px) {
      .lesson-toc-sidebar { float: none; display: none; }
      .lesson-layout { display: block; }
      .lesson-layout > main { overflow: hidden; }
      #lesson-nav { display: block; }
      .hero-container { min-height: auto; }
      .hero-split { flex-direction: column !important; }
      .hero-abstract-card { margin-top: 1.5rem; }
      .hero-title-main { font-size: 1.75rem !important; }
    }

    /* ── Print styles — hide interactive chrome when printing ──── */
    @media print {
      .lesson-toc-sidebar, .back-to-top, .scroll-progress, .copy-btn, .hero-container { display: none; }
      .obj-card:hover { transform: none; box-shadow: none; }
    }

    /* ── Iconify icon alignment utility ─────────────────────────── */
    .iconify { vertical-align: middle; flex-shrink: 0; }

  /* ============================================================
     CONFLUENCE ISOLATION — scoped to #hub-root
     All rules use !important to beat Confluence's element styles.
     ============================================================ */

  #hub-root,
  #hub-root * {
    font-family: var(--font-body) !important;
    box-sizing: border-box !important;
  }

  #hub-root {
    font-size: 16px !important;
    line-height: 1.6 !important;
    color: #1f2937 !important;
  }

  #hub-root code,
  #hub-root pre,
  #hub-root [class*="language-"] { font-family: var(--font-mono) !important; }

  #hub-root h1, #hub-root h2, #hub-root h3,
  #hub-root h4, #hub-root h5, #hub-root h6 {
    margin-top: 0 !important; margin-bottom: 0 !important;
    padding: 0 !important; line-height: 1.3 !important;
  }
  #hub-root h1 { font-size: 1.75rem  !important; font-weight: 700 !important; }
  #hub-root h2 { font-size: 1.25rem  !important; font-weight: 700 !important; }
  #hub-root h3 { font-size: 1rem     !important; font-weight: 600 !important; }
  #hub-root h4 { font-size: 0.875rem !important; font-weight: 600 !important; }
  #hub-root h5, #hub-root h6 { font-size: 0.8rem !important; font-weight: 600 !important; }

  #hub-root .font-black     { font-weight: 900 !important; }
  #hub-root .font-extrabold { font-weight: 800 !important; }
  #hub-root .font-bold      { font-weight: 700 !important; }
  #hub-root .font-semibold  { font-weight: 600 !important; }
  #hub-root .font-medium    { font-weight: 500 !important; }

  #hub-root .text-4xl  { font-size: 2.25rem  !important; line-height: 2.5rem  !important; }
  #hub-root .text-3xl  { font-size: 1.875rem !important; line-height: 2.25rem !important; }
  #hub-root .text-2xl  { font-size: 1.5rem   !important; line-height: 2rem    !important; }
  #hub-root .text-xl   { font-size: 1.25rem  !important; line-height: 1.75rem !important; }
  #hub-root .text-lg   { font-size: 1.125rem !important; line-height: 1.75rem !important; }
  #hub-root .text-base { font-size: 1rem     !important; line-height: 1.5rem  !important; }
  #hub-root .text-sm   { font-size: 0.875rem !important; line-height: 1.25rem !important; }
  #hub-root .text-xs   { font-size: 0.75rem  !important; line-height: 1rem    !important; }

  #hub-root .text-white    { color: #ffffff !important; }
  #hub-root .text-gray-900 { color: #111827 !important; }
  #hub-root .text-gray-800 { color: #1f2937 !important; }
  #hub-root .text-gray-700 { color: #374151 !important; }
  #hub-root .text-gray-600 { color: #4b5563 !important; }
  #hub-root .text-gray-500 { color: #6b7280 !important; }
  #hub-root .text-gray-400 { color: #9ca3af !important; }
  #hub-root .text-gray-300 { color: #d1d5db !important; }

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
  #hub-root .ml-auto { margin-left: auto !important; }

  #hub-root a       { text-decoration: none !important; }
  #hub-root a:hover { text-decoration: none !important; }

  #hub-root .iconify { vertical-align: middle !important; flex-shrink: 0 !important; }
  #hub-root :not(.block) > .iconify:not(.block) {
    display: inline-flex !important; align-items: center !important; justify-content: center !important;
  }

  #hub-root .hero-title-main {
    font-size: 2.25rem !important; font-weight: 800 !important;
    line-height: 1.15 !important; margin-bottom: 2rem !important;
  }
  @media (min-width: 768px) {
    #hub-root .hero-title-main { font-size: 2.5rem !important; }
  }

  /* ── Section header components ── */
  #hub-root .section-header {
    display: flex !important; align-items: center !important; gap: 1rem !important;
    padding: 1.25rem 2rem 1.25rem 1rem !important; background: #ffffff !important;
    border-bottom: 1px solid #f3f4f6 !important; border-left: 4px solid #CB187D !important;
  }
  #hub-root .section-icon {
    display: inline-flex !important; align-items: center !important; justify-content: center !important;
    width: 2.75rem !important; height: 2.75rem !important;
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

  /* ── Step tab consistent sizing (Confluence Tailwind fix) ── */
  #hub-root .ce-step, #hub-root .mk-step,
  #hub-root .qz-step, #hub-root .pe-step {
    display: inline-flex !important; align-items: center !important; gap: 0.5rem !important;
    padding: 0.375rem 1rem !important; border-radius: 9999px !important;
    font-size: 0.75rem !important; font-weight: 700 !important;
    line-height: 1.2 !important; white-space: nowrap !important;
    border: none !important; cursor: pointer !important;
  }

  /* ── Skill dots ── */
  #hub-root .skill-dot {
    width: 6px !important; height: 6px !important; border-radius: 50% !important;
    background: #d1d5db !important; display: inline-block !important;
  }
  #hub-root .skill-dot-active { background: #22c55e !important; }

  /* ── Hero SVG / Python icon ── */
  #hub-root .hero-svg { max-height: 320px !important; }
  #hub-root .hero-py-icon-wrap {
    display: flex !important; align-items: center !important; justify-content: center !important;
    width: 100% !important; height: 100% !important;
  }
  #hub-root .hero-py-icon { font-size: 70px !important; filter: drop-shadow(0 0 14px rgba(255,212,59,0.25)) !important; }

  /* ── Tip / info boxes ── */
  #hub-root .bg-amber-tip { background: #fff7ed !important; border: 1px solid #fed7aa !important; }

  /* ── Dark pill tabs — inactive ── */
  #hub-root .ce-step:not(.ce-step-active),
  #hub-root .mk-step:not(.mk-step-active),
  #hub-root .qz-step:not(.qz-step-active),
  #hub-root .pe-step:not(.pe-step-active) {
    background-color: #1f2937 !important; color: #ffffff !important; box-shadow: none !important;
  }
  /* ── Dark pill tabs — active (pink gradient) ── */
  #hub-root .ce-step-active,
  #hub-root .mk-step-active,
  #hub-root .qz-step-active,
  #hub-root .pe-step-active {
    background: linear-gradient(to right, #CB187D, #e84aad) !important;
    color: #ffffff !important;
    box-shadow: 0 10px 25px -5px rgba(203,24,125,0.3) !important;
  }

  /* ── Key Concepts sidebar labels ── */
  #hub-root .kc-tab-active .kc-tab-label { color: #111827 !important; }
  #hub-root .kc-tab:not(.kc-tab-active) .kc-tab-label { color: #9ca3af !important; }

  /* ── Background utilities ── */
  #hub-root .bg-white    { background-color: #ffffff !important; }
  #hub-root .bg-gray-50  { background-color: #f9fafb !important; }
  #hub-root .bg-gray-100 { background-color: #f3f4f6 !important; }
  #hub-root .bg-gray-800 { background-color: #1f2937 !important; }
  #hub-root .bg-gray-900 { background-color: #111827 !important; }

  /* ── Stat pill label visibility ── */
  #hub-root .hero-pill .iconify { opacity: 0.5 !important; }
  #hub-root .hero-pill .opacity-55 { opacity: 1 !important; }
  #hub-root .hero-pill .opacity-50 { opacity: 1 !important; }
  #hub-root a.hero-pill { color: #CB187D !important; }

  /* ── TOC active state ── */
  #hub-root .toc-link:hover { color: #CB187D !important; }
  #hub-root .toc-link.active {
    color: #CB187D !important; font-weight: 600 !important;
    border-left: 3px solid #CB187D !important; padding-left: 8px !important;
    background-color: #fdf0f7 !important;
  }

  /* ── Module lessons list active link ── */
  #hub-root .mod-lesson-active {
    background-color: #fdf0f7 !important; border-color: #CB187D !important; color: #CB187D !important;
  }
  #hub-root .mod-lesson-active .lesson-dot { background-color: #CB187D !important; }

  /* ── Bottom nav hover ── */
  #hub-root .lesson-nav-link:hover p,
  #hub-root .lesson-nav-link:hover span,
  #hub-root .lesson-nav-link:hover svg {
    color: #CB187D !important; transition: color 0.15s !important;
  }
  </style>"""

# ── 3. Transformation ─────────────────────────────────────────────────────────

# Extract the body content (everything from <body> to </body>)
body_match = re.search(r'<body>(.*?)</body>', src, re.DOTALL)
if not body_match:
    print('ERROR: Could not find <body>...</body> in source file.')
    sys.exit(1)
body_content = body_match.group(1).strip()

# Remove trailing </body></html> or </body> if lingering
body_content = re.sub(r'\s*</body>\s*</html>\s*$', '', body_content)
body_content = re.sub(r'\s*</body>\s*$', '', body_content)

# Add id="hub-root" to the outer bg-gray-50 wrapper div
body_content = body_content.replace(
    '<div class="bg-gray-50 min-h-screen">',
    '<div id="hub-root" class="bg-gray-50 min-h-screen">'
)

# Assemble the final Confluence-ready file
result = f"""{CDN}

{STYLE}

<!-- Scroll progress bar -->
<div class="scroll-progress" id="scroll-progress"></div>

<!-- Back to top -->
<button class="back-to-top" id="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
  <span class="iconify text-lg" data-icon="fa6-solid:arrow-up"></span>
</button>

{body_content}"""

# Check the scroll-progress div isn't duplicated (it may already be in body_content)
if result.count('id="scroll-progress"') > 1:
    # Remove the one we added at the top, rely on the body content version
    result = result.replace(
        '\n<!-- Scroll progress bar -->\n<div class="scroll-progress" id="scroll-progress"></div>\n\n<!-- Back to top -->\n<button class="back-to-top" id="back-to-top" onclick="window.scrollTo({top:0,behavior:\'smooth\'})\">\n  <span class="iconify text-lg" data-icon="fa6-solid:arrow-up"></span>\n</button>\n\n',
        '\n'
    )

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(result)

print(f'✅ {FILE} — converted to Confluence-ready format')

# Quick verification
with open(FILE, 'r', encoding='utf-8') as f:
    final = f.read()

checks = [
    ('No DOCTYPE', '<!DOCTYPE' not in final),
    ('No <html>', '<html' not in final),
    ('No <head>', '<head>' not in final),
    ('No <body>', '<body>' not in final),
    ('Has hub-root', 'id="hub-root"' in final),
    ('Has :root CSS vars', '--font-body' in final),
    ('Has #hub-root isolation', '#hub-root .section-header' in final),
    ('Has CSS section comments', '/* ── CSS Variables' in final),
    ('Has scroll-progress', 'id="scroll-progress"' in final),
    ('Has switchCeTab', 'switchCeTab' in final),
]
for name, ok in checks:
    print(f'  {"✅" if ok else "❌"} {name}')
