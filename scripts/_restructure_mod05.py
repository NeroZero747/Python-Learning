"""
Restructure mod_05_data_application from 11 lessons to 7 lessons.

Mapping:
  OLD lesson01 → NEW lesson01  (keep, update nav only)
  OLD lesson02 + lesson03 → NEW lesson02  (merge: Streamlit intro + dashboard building)
  OLD lesson04 → NEW lesson03  (rename + update nav)
  OLD lesson05 → NEW lesson04  (rename + update nav)
  OLD lesson06 + lesson09 + lesson10 + lesson11 → NEW lesson05  (merge: deployment + devops + CI/CD)
  OLD lesson07 → NEW lesson06  (rename + update nav)
  OLD lesson08 → NEW lesson07  (rename + update nav)

Delete after: old lesson03, lesson09, lesson10, lesson11
"""

import os
import re
import shutil

DIR = os.path.join('pages', 'mod_05_data_application')
BACKUP = os.path.join('pages', 'mod_05_data_application', '_backup')

# ── New lesson definitions ────────────────────────────────────
NEW_LESSONS = [
    {
        'num': 1,
        'file': 'lesson01_why_build_data_apps.html',
        'title': 'Why Build Data Apps?',
    },
    {
        'num': 2,
        'file': 'lesson02_introduction_to_streamlit.html',
        'title': 'Introduction to Streamlit',
    },
    {
        'num': 3,
        'file': 'lesson03_interactive_filters.html',
        'title': 'Interactive Filters',
    },
    {
        'num': 4,
        'file': 'lesson04_exporting_data.html',
        'title': 'Exporting Data',
    },
    {
        'num': 5,
        'file': 'lesson05_deploying_data_applications.html',
        'title': 'Deploying Data Applications',
    },
    {
        'num': 6,
        'file': 'lesson06_shiny_for_python.html',
        'title': 'Shiny for Python',
    },
    {
        'num': 7,
        'file': 'lesson07_streamlit_vs_shiny.html',
        'title': 'Streamlit vs Shiny',
    },
]

# ── Helper: generate sidebar HTML for a given active lesson ──
def make_sidebar_html(active_num):
    """Generate the Module Lessons sidebar block with the correct active link."""
    lines = []
    for lesson in NEW_LESSONS:
        num = lesson['num']
        href = lesson['file']
        title = f"{num}. {lesson['title']}"
        if num == active_num:
            lines.append(
                f'<a href="{href}" class="flex items-center gap-2 px-3 py-2 rounded-lg border '
                f'bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors">\n'
                f'  <span class="w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span>\n'
                f'  <span class="truncate">{title}</span>\n'
                f'</a>'
            )
        else:
            lines.append(
                f'<a href="{href}" class="flex items-center gap-2 px-3 py-2 rounded-lg border '
                f'bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
                f'  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
                f'  <span class="truncate">{title}</span>\n'
                f'</a>'
            )
    return '\n'.join(lines)


def make_next_lesson_section(current_num):
    """Generate the #next-lesson section for the given lesson number."""
    if current_num >= len(NEW_LESSONS):
        return ''  # Last lesson — no next
    
    nxt = NEW_LESSONS[current_num]  # 0-indexed, so current_num is the next
    num = nxt['num']
    title = nxt['title']
    
    # Simple 3-card preview — generic since content will be audited later
    preview_icons = ['fa6-solid:play', 'fa6-solid:puzzle-piece', 'fa6-solid:sitemap']
    preview_items = {
        2: ['Install &amp; run Streamlit', 'Core Streamlit widgets', 'App layout &amp; structure'],
        3: ['Dropdown &amp; slider filters', 'Dynamic data updates', 'Reactive dashboards'],
        4: ['CSV &amp; Excel export', 'Download buttons', 'File generation'],
        5: ['Deployment environments', 'CI/CD concepts', 'Production workflows'],
        6: ['Shiny app structure', 'Reactive inputs', 'Building Shiny dashboards'],
        7: ['Framework comparison', 'When to use Streamlit', 'When to use Shiny'],
    }
    items = preview_items.get(num, ['Topic 1', 'Topic 2', 'Topic 3'])
    
    cards = ''
    for icon, item in zip(preview_icons, items):
        cards += f'''
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="{icon}"></span></span>
            <div><p class="text-sm font-semibold text-gray-700">{item}</p></div>
          </div>'''
    
    return f'''<section id="next-lesson" class="scroll-mt-24">
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
          <span class="text-white font-bold text-lg">{num}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 5 &middot; Lesson {num}</p>
          <h3 class="text-base font-bold text-gray-800">{title}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">{cards}
        </div>
      </div>
    </div>
  </div>
</section>'''


def make_bottom_nav(current_num):
    """Generate the bottom nav bar (Previous / Next)."""
    prev_link = ''
    next_link = ''
    
    if current_num == 1:
        # First lesson in module — previous goes to prior module
        prev_link = '''<a href="../mod_03_api_data_for_applications/lesson10_loading_api_data_into_pandas.html" class="lesson-nav-link group flex-1 flex items-center gap-3 rounded-xl border border-gray-100 bg-white px-5 py-4 no-underline hover:border-[#CB187D] transition-colors">
  <span class="iconify text-gray-300 text-sm shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-left"></span>
  <div class="min-w-0">
    <p class="text-xs text-gray-400">Previous</p>
    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">Loading API Data into Pandas</p>
  </div>
</a>'''
    elif current_num > 1:
        prev = NEW_LESSONS[current_num - 2]
        prev_link = f'''<a href="{prev['file']}" class="lesson-nav-link group flex-1 flex items-center gap-3 rounded-xl border border-gray-100 bg-white px-5 py-4 no-underline hover:border-[#CB187D] transition-colors">
  <span class="iconify text-gray-300 text-sm shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-left"></span>
  <div class="min-w-0">
    <p class="text-xs text-gray-400">Previous</p>
    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">{prev['title']}</p>
  </div>
</a>'''
    
    if current_num < len(NEW_LESSONS):
        nxt = NEW_LESSONS[current_num]  # 0-indexed next
        next_link = f'''<a href="{nxt['file']}" class="lesson-nav-link group flex-1 flex items-center gap-3 rounded-xl border border-gray-100 bg-white px-5 py-4 no-underline hover:border-[#CB187D] transition-colors text-right">
  <div class="min-w-0 ml-auto">
    <p class="text-xs text-gray-400">Next</p>
    <p class="text-sm font-semibold text-gray-800 group-hover:text-[#CB187D] transition-colors truncate">{nxt['title']}</p>
  </div>
  <span class="iconify text-gray-300 text-sm shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:chevron-right"></span>
</a>'''
    
    return f'<div class="flex flex-col sm:flex-row gap-3 mt-6">{prev_link}{next_link}</div>'


def replace_sidebar(text, active_num):
    """Replace the Module Lessons sidebar block in a lesson file."""
    new_sidebar = make_sidebar_html(active_num)
    
    # Pattern: find the <div class="space-y-1"> block inside toc-module-list
    pattern = r'(<div class="space-y-1">).*?(</div>\s*</div>\s*</div>\s*</aside>)'
    replacement = r'\1' + new_sidebar + '\n' + r'\2'
    result, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    return result, count


def replace_next_lesson(text, current_num):
    """Replace the #next-lesson section."""
    new_next = make_next_lesson_section(current_num)
    
    # Find and replace the next-lesson section
    pattern = r'<section id="next-lesson"[^>]*>.*?</section>'
    if new_next:
        result, count = re.subn(pattern, new_next, text, count=1, flags=re.DOTALL)
    else:
        # Remove next-lesson section entirely (last lesson)
        result, count = re.subn(pattern + r'\s*', '', text, count=1, flags=re.DOTALL)
    return result, count


def replace_bottom_nav(text, current_num):
    """Replace the bottom nav Previous/Next links."""
    new_nav = make_bottom_nav(current_num)
    
    # Pattern: the flex div containing lesson-nav-link anchors
    pattern = r'<div class="flex flex-col sm:flex-row gap-3 mt-6">.*?</div>(?=\s*</main>)'
    result, count = re.subn(pattern, new_nav, text, count=1, flags=re.DOTALL)
    return result, count


def update_hero_lesson_num(text, new_num, new_title, total=7):
    """Update the hero section lesson number and title."""
    # Update "Lesson XX" label
    text = re.sub(
        r'(<p class="text-xs font-bold uppercase tracking-\[0\.2em\] text-white/90 mb-2">)Lesson \d+',
        rf'\g<1>Lesson {new_num:02d}',
        text, count=1
    )
    
    # Update h1 title
    text = re.sub(
        r'(<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3[^"]*">)[^<]+(</h1>)',
        rf'\g<1>{new_title}\2',
        text, count=1
    )
    
    # Update progress pill (X/Y)
    text = re.sub(
        r'(<span class="font-extrabold">)\d+(<span class="font-bold opacity-50">)/\d+',
        rf'\g<1>{new_num}\g<2>/{total}',
        text, count=1
    )
    
    # Update <title> tag
    text = re.sub(
        r'<title>Lesson \d+ &mdash; [^<]+</title>',
        f'<title>Lesson {new_num} &mdash; {new_title} | Python Learning Hub</title>',
        text, count=1
    )
    
    # Update meta description lesson reference
    text = re.sub(
        r'(<meta name="description" content="Learn )[^"]+(")',
        rf'\g<1>{new_title} in Python. Part of the Building Data Applications module — Track 4: Data Applications — Python Learning Hub.\2',
        text, count=1
    )
    
    return text


def update_footer_if_needed(text):
    """Ensure footer references Track 4."""
    # Already correct in most files; just standardize
    return text


def merge_l02_l03():
    """
    Merge lesson02 (Streamlit intro) + lesson03 (simple dashboard) into new lesson02.
    Strategy: Use L02 as base. Add L03's unique CE panels and KC tabs.
    """
    l02 = open(os.path.join(DIR, 'lesson02_introduction_to_streamlit.html'), encoding='utf-8').read()
    l03 = open(os.path.join(DIR, 'lesson03_building_a_simple_dashboard.html'), encoding='utf-8').read()
    
    # Use L02 as the base — it already has the right title
    merged = l02
    
    # ── Extract L03's unique CE panels (panels 0-3) ──
    l03_html = l03.split('<script>')[0]
    
    # Extract L03 CE panel content: "Displaying Summary Metrics" and "Combining Components" are unique
    # L03 CE panels: Dashboard Structure, Summary Metrics, Creating Charts, Combining Components
    # L02 CE panels: Simple App, Displaying Data, Charts, User Input  
    # Overlap: Charts — keep L03's "Summary Metrics" and "Combining Components" as new tabs 5 & 6 in L02
    
    # Extract L03's CE panels
    l03_ce_panels = re.findall(r'(<div class="ce-panel[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>\s*</div>)', l03_html, re.DOTALL)
    
    # We want panels 1 (Summary Metrics) and 3 (Combining Components) from L03
    new_ce_panels = []
    if len(l03_ce_panels) >= 4:
        # Panel index 1 = Summary Metrics, index 3 = Combining Components
        for idx in [1, 3]:
            panel = l03_ce_panels[idx]
            # Ensure it's hidden
            panel = panel.replace('ce-panel ce-panel-anim ', 'ce-panel ce-panel-anim hidden')
            if 'ce-panel ce-panel-anim  ' in panel:
                panel = panel.replace('ce-panel ce-panel-anim  ', 'ce-panel ce-panel-anim hidden ')
            new_ce_panels.append(panel)
    
    # Add the new CE tabs to L02's tab bar
    # Find the last ce-step button and add two more after it
    # L02 has 4 tabs (index 0-3), so new ones will be index 4 and 5
    new_tab_buttons = '''
<button onclick="switchCeTab(4)" class="ce-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
  <span class="ce-step-label text-xs font-bold">Metrics</span>
</button>
<button onclick="switchCeTab(5)" class="ce-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
  <span class="ce-step-label text-xs font-bold">Full Dashboard</span>
</button>'''
    
    # Insert new tab buttons before the closing </div> of the tab bar
    merged = re.sub(
        r'(</button>\s*</div>\s*<div class="ce-panel ce-panel-anim ")',
        r'\g<0>',
        merged, count=1
    )
    # Simpler approach: find the tablist closing, add buttons
    tablist_pattern = r'(switchCeTab\(3\).*?</button>)\s*(</div>\s*<div class="ce-panel)'
    tablist_match = re.search(tablist_pattern, merged, re.DOTALL)
    if tablist_match:
        insert_pos = tablist_match.start(2)
        merged = merged[:insert_pos] + new_tab_buttons + '\n' + merged[insert_pos:]
    
    # Now insert the new CE panels at the end of existing panels (before the closing of code-examples section body)
    # Find the last ce-panel and insert after it
    # Pattern: find the last </div> before the closing of the code-examples section
    ce_section_end = merged.find('</section>', merged.find('id="code-examples"'))
    # Go backwards to find the right insertion point — after the last ce-panel
    last_panel_end = merged.rfind('</div>\n</div>', 0, ce_section_end)
    if last_panel_end > 0:
        # Find the actual end of the last panel div structure
        # Insert new panels after the last panel
        panels_text = '\n'.join(new_ce_panels)
        # Find insertion point: after last ce-panel's closing divs but before the section body closing
        ce_body_close = merged.rfind('</div>\n  </div>\n</section>', 0, ce_section_end + 20)
        if ce_body_close > 0:
            merged = merged[:ce_body_close] + '\n' + panels_text + '\n' + merged[ce_body_close:]
    
    # ── Add L03's KC panel for "Summary Metrics" as 4th KC tab ──
    # L02 has 3 KC tabs, L03 has "Summary Metrics" and "Data Visualization"
    # Add "Data Visualization" as 4th KC tab in L02
    l03_kc_panels = re.findall(r'(<div class="kc-panel[^"]*"[^>]*data-color="[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>)', l03_html, re.DOTALL)
    
    if len(l03_kc_panels) >= 3:
        # Index 2 = Data Visualization panel from L03
        new_kc_panel = l03_kc_panels[2]
        if 'hidden' not in new_kc_panel[:60]:
            new_kc_panel = new_kc_panel.replace('kc-panel kc-panel-anim ', 'kc-panel kc-panel-anim hidden')
        
        # Add KC tab button
        new_kc_tab = '''<button onclick="switchKcTab(3)" class="kc-tab  group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:chart-bar"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Data Visualization</span>
</button>'''
        
        # Insert KC tab button after the last kc-tab button
        kc_tab_pattern = r'(switchKcTab\(2\).*?</button>)\s*(</div>\s*<div class="flex-1)'
        kc_match = re.search(kc_tab_pattern, merged, re.DOTALL)
        if kc_match:
            insert_pos = kc_match.start(2)
            merged = merged[:insert_pos] + '\n' + new_kc_tab + '\n' + merged[insert_pos:]
        
        # Insert KC panel at end of KC panels
        kc_section = merged.find('id="key-concepts"')
        kc_section_end = merged.find('</section>', kc_section)
        # Find last kc-panel closing
        last_kc_close = merged.rfind('</div>\n</div>\n</div>', kc_section, kc_section_end)
        if last_kc_close > 0:
            insert_after = last_kc_close + len('</div>\n</div>\n</div>')
            merged = merged[:insert_after] + '\n' + new_kc_panel + '\n' + merged[insert_after:]
    
    return merged


def merge_deployment():
    """
    Merge L06 (deployment basics) + L09 (devops) + L10 (gitlab CI/CD) + L11 (deployment workflow) 
    into new lesson05.
    Strategy: Use L06 as base. Add KC tabs from L09/L10, code examples from L09/L11.
    """
    l06 = open(os.path.join(DIR, 'lesson06_deployment_basics.html'), encoding='utf-8').read()
    l09 = open(os.path.join(DIR, 'lesson09_devops_concepts_for_data_analytics.html'), encoding='utf-8').read()
    l10 = open(os.path.join(DIR, 'lesson10_gitlab_ci_cd_overview.html'), encoding='utf-8').read()
    l11 = open(os.path.join(DIR, 'lesson11_deployment_workflow.html'), encoding='utf-8').read()
    
    merged = l06
    
    # ── Update the title to "Deploying Data Applications" ──
    # This will be done by update_hero_lesson_num later
    
    # ── Update objectives to be broader ──
    # Replace L06's 4 objectives with expanded set covering deployment + CI/CD + workflow
    old_obj_pattern = r'(<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">).*?(</div>\s*<div class="mt-5">)'
    new_objectives = '''\\1<div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
  <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
    <span class="iconify text-brand text-lg" data-icon="fa6-solid:bullseye"></span>
  </span>
  <div>
    <p class="text-sm font-semibold text-gray-800">Understand what deployment means for data applications</p>
  </div>
</div>
<div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
  <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
    <span class="iconify text-brand text-lg" data-icon="fa6-solid:cloud-arrow-up"></span>
  </span>
  <div>
    <p class="text-sm font-semibold text-gray-800">Identify common deployment environments and workflows</p>
  </div>
</div>
<div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
  <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
    <span class="iconify text-brand text-lg" data-icon="fa6-solid:rotate"></span>
  </span>
  <div>
    <p class="text-sm font-semibold text-gray-800">Explain how CI/CD pipelines automate testing and deployment</p>
  </div>
</div>
<div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
  <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
    <span class="iconify text-brand text-lg" data-icon="fa6-solid:gears"></span>
  </span>
  <div>
    <p class="text-sm font-semibold text-gray-800">Describe how Python applications move from development to production</p>
  </div>
</div>
</div>
      <div class="mt-5"><div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">This lesson covers the complete deployment lifecycle, from basic hosting concepts through CI/CD automation and production deployment workflows.</p>
</div>\\2'''
    merged = re.sub(old_obj_pattern, new_objectives, merged, count=1, flags=re.DOTALL)
    
    # ── Add KC tabs from L09 (CI, CD) ──
    l09_html = l09.split('<script>')[0]
    l09_kc_panels = re.findall(r'(<div class="kc-panel[^"]*"[^>]*data-color="[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>)', l09_html, re.DOTALL)
    
    # L09 KC: [0]=DevOps, [1]=CI, [2]=CD — add CI and CD as tabs 3 and 4 in merged file
    new_kc_tabs = ''
    new_kc_panels_text = ''
    
    if len(l09_kc_panels) >= 3:
        for idx, (tab_idx, label, icon) in enumerate([(3, 'CI/CD Pipelines', 'fa6-solid:rotate'), (4, 'DevOps for Data', 'fa6-solid:gears')]):
            new_kc_tabs += f'''
<button onclick="switchKcTab({tab_idx})" class="kc-tab  group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="{icon}"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">{label}</span>
</button>'''
        
        # Use L09's CI panel (index 1) and CD panel (index 2)
        for panel in [l09_kc_panels[1], l09_kc_panels[2]]:
            if 'hidden' not in panel[:80]:
                panel = panel.replace('kc-panel kc-panel-anim ', 'kc-panel kc-panel-anim hidden')
            new_kc_panels_text += '\n' + panel
    
    if new_kc_tabs:
        # Insert KC tabs
        kc_tab_pattern = r'(switchKcTab\(2\).*?</button>)\s*(</div>\s*<div class="flex-1)'
        kc_match = re.search(kc_tab_pattern, merged, re.DOTALL)
        if kc_match:
            insert_pos = kc_match.start(2)
            merged = merged[:insert_pos] + new_kc_tabs + '\n' + merged[insert_pos:]
        
        # Insert KC panels
        kc_section = merged.find('id="key-concepts"')
        kc_section_end = merged.find('</section>', kc_section)
        last_kc_close = merged.rfind('</div>\n</div>\n</div>', kc_section, kc_section_end)
        if last_kc_close > 0:
            insert_after = last_kc_close + len('</div>\n</div>\n</div>')
            merged = merged[:insert_after] + new_kc_panels_text + merged[insert_after:]
    
    # ── Add code examples from L09 and L11 ──
    # L09 has 3 Python code blocks, L11 has 3 — add as additional CE tabs
    l09_ce_html = l09.split('<script>')[0]
    l11_html = l11.split('<script>')[0]
    
    l09_ce_panels = re.findall(r'(<div class="ce-panel[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>\s*</div>)', l09_ce_html, re.DOTALL)
    l11_ce_panels = re.findall(r'(<div class="ce-panel[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>\s*</div>)', l11_html, re.DOTALL)
    
    # Add L09 panel 1 (Automated Script) and L11 panel 0 (Deployment Script) as tabs 4 and 5
    new_ce_tabs = ''
    new_ce_panels_list = []
    tab_labels = ['CI Script', 'Deploy Script']
    source_panels = []
    if len(l09_ce_panels) >= 2:
        source_panels.append(l09_ce_panels[1])  # Automated Script
    if len(l11_ce_panels) >= 1:
        source_panels.append(l11_ce_panels[0])  # Deployment Script
    
    for i, (label, panel) in enumerate(zip(tab_labels[:len(source_panels)], source_panels)):
        tab_num = 4 + i
        new_ce_tabs += f'''
<button onclick="switchCeTab({tab_num})" class="ce-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
  <span class="ce-step-label text-xs font-bold">{label}</span>
</button>'''
        panel_hidden = panel
        if 'hidden' not in panel_hidden[:80]:
            panel_hidden = panel_hidden.replace('ce-panel ce-panel-anim ', 'ce-panel ce-panel-anim hidden')
        if 'ce-panel ce-panel-anim  ' in panel_hidden:
            panel_hidden = panel_hidden.replace('ce-panel ce-panel-anim  ', 'ce-panel ce-panel-anim hidden ')
        new_ce_panels_list.append(panel_hidden)
    
    if new_ce_tabs:
        # Insert CE tab buttons
        ce_tablist_pattern = r'(switchCeTab\(3\).*?</button>)\s*(</div>\s*<div class="ce-panel)'
        ce_match = re.search(ce_tablist_pattern, merged, re.DOTALL)
        if ce_match:
            insert_pos = ce_match.start(2)
            merged = merged[:insert_pos] + new_ce_tabs + '\n' + merged[insert_pos:]
        
        # Insert CE panels before section close
        ce_section = merged.find('id="code-examples"')
        ce_section_end = merged.find('</section>', ce_section)
        ce_body_close = merged.rfind('</div>\n  </div>\n</section>', 0, ce_section_end + 20)
        if ce_body_close > 0:
            panels_text = '\n'.join(new_ce_panels_list)
            merged = merged[:ce_body_close] + '\n' + panels_text + '\n' + merged[ce_body_close:]
    
    return merged


def process_file(text, lesson_num, lesson_title):
    """Apply all navigation updates to a lesson file."""
    # 1. Replace sidebar
    text, n = replace_sidebar(text, lesson_num)
    if n == 0:
        print(f"  ⚠️  Sidebar replacement failed")
    
    # 2. Update hero
    text = update_hero_lesson_num(text, lesson_num, lesson_title)
    
    # 3. Replace next-lesson section
    text, n = replace_next_lesson(text, lesson_num)
    
    # 4. Replace bottom nav
    text, n = replace_bottom_nav(text, lesson_num)
    if n == 0:
        print(f"  ⚠️  Bottom nav replacement failed")
    
    return text


def main():
    # ── Step 1: Backup all original files ──
    os.makedirs(BACKUP, exist_ok=True)
    originals = [f for f in os.listdir(DIR) if f.startswith('lesson') and f.endswith('.html')]
    for f in originals:
        src = os.path.join(DIR, f)
        dst = os.path.join(BACKUP, f)
        shutil.copy2(src, dst)
    print(f"✅ Backed up {len(originals)} files to {BACKUP}/")
    
    # ── Step 2: Create merged files ──
    print("\n── Creating merged lesson02 (Streamlit intro + dashboard) ──")
    merged_l02 = merge_l02_l03()
    
    print("── Creating merged lesson05 (deployment + devops + CI/CD) ──")
    merged_l05 = merge_deployment()
    
    # ── Step 3: Read source files for rename-only lessons ──
    l01 = open(os.path.join(DIR, 'lesson01_why_build_data_apps.html'), encoding='utf-8').read()
    l04 = open(os.path.join(DIR, 'lesson04_interactive_filters.html'), encoding='utf-8').read()
    l05 = open(os.path.join(DIR, 'lesson05_exporting_data.html'), encoding='utf-8').read()
    l07 = open(os.path.join(DIR, 'lesson07_shiny_for_python.html'), encoding='utf-8').read()
    l08 = open(os.path.join(DIR, 'lesson08_streamlit_vs_shiny.html'), encoding='utf-8').read()
    
    # ── Step 4: Process each file ──
    files_to_write = {}
    
    # L01: keep, update nav only
    print("\nProcessing lesson01...")
    files_to_write['lesson01_why_build_data_apps.html'] = process_file(l01, 1, 'Why Build Data Apps?')
    
    # L02: merged file
    print("Processing lesson02 (merged)...")
    files_to_write['lesson02_introduction_to_streamlit.html'] = process_file(merged_l02, 2, 'Introduction to Streamlit')
    
    # L04 → L03
    print("Processing lesson03 (was lesson04)...")
    files_to_write['lesson03_interactive_filters.html'] = process_file(l04, 3, 'Interactive Filters')
    
    # L05 → L04
    print("Processing lesson04 (was lesson05)...")
    files_to_write['lesson04_exporting_data.html'] = process_file(l05, 4, 'Exporting Data')
    
    # L06+L09+L10+L11 → L05: merged deployment file
    print("Processing lesson05 (merged deployment)...")
    files_to_write['lesson05_deploying_data_applications.html'] = process_file(merged_l05, 5, 'Deploying Data Applications')
    
    # L07 → L06
    print("Processing lesson06 (was lesson07)...")
    files_to_write['lesson06_shiny_for_python.html'] = process_file(l07, 6, 'Shiny for Python')
    
    # L08 → L07
    print("Processing lesson07 (was lesson08)...")
    files_to_write['lesson07_streamlit_vs_shiny.html'] = process_file(l08, 7, 'Streamlit vs Shiny')
    
    # ── Step 5: Delete all old lesson files ──
    for f in originals:
        path = os.path.join(DIR, f)
        os.remove(path)
    print(f"\n🗑️  Removed {len(originals)} old files")
    
    # ── Step 6: Write new files ──
    for filename, content in files_to_write.items():
        path = os.path.join(DIR, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        lines = content.count('\n') + 1
        print(f"✅ Wrote {filename} ({lines} lines)")
    
    print(f"\n✅ Restructuring complete: {len(files_to_write)} lesson files")
    print(f"📁 Backups saved in {BACKUP}/")


if __name__ == '__main__':
    main()
