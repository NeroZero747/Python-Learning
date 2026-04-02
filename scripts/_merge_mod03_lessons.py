"""
Merge secondary lesson content into mod_03_python_for_data_analysts lessons.

For each merged lesson this script:
  1. Updates the hero H1 title
  2. Appends CE tab buttons + panels from each secondary file
  3. Appends KC tab buttons + panels from each secondary file
"""

import re, os

BASE_SRC  = 'pages/track_03_data_analytics'
BASE_DEST = 'pages/mod_03_python_for_data_analysts'

# ─────────────────────────────────────────────────────────────────────────────
# HTML helper utilities
# ─────────────────────────────────────────────────────────────────────────────

def find_closing_div(text, start_pos):
    """Return the index just *after* the </div> that closes the <div at start_pos."""
    depth = 0
    i = start_pos
    while i < len(text):
        if text[i:i+4] == '<div':
            depth += 1
            i += 4
        elif text[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return i + 6
            i += 6
        else:
            i += 1
    return -1


def extract_ce_buttons(text):
    """Return list of (label, html_block) for every ce-step button."""
    buttons = []
    for m in re.finditer(r'<button onclick="switchCeTab\(\d+\)"', text):
        start = m.start()
        end   = text.find('</button>', start) + 9
        html  = text[start:end]
        label = re.search(r'ce-step-label[^>]*>([^<]+)<', html)
        buttons.append((label.group(1).strip() if label else '?', html))
    return buttons


def extract_ce_panels(text):
    """Return list of (label, html_block) for every ce-panel div."""
    panels = []
    for m in re.finditer(r'<div class="ce-panel', text):
        start = m.start()
        end   = find_closing_div(text, start)
        html  = text[start:end]
        # derive a label from the matching header inside the panel
        lbl   = re.search(r'ce-header-title[^>]*>([^<]+)<', html)
        if not lbl:
            lbl = re.search(r'font-bold text-gray-800 leading-tight">([^<]+)<', html)
        panels.append((lbl.group(1).strip() if lbl else '?', html))
    return panels


def make_ce_button_inactive(html, new_index):
    """Convert a (possibly active) CE button to inactive and set given index."""
    html = re.sub(r'switchCeTab\(\d+\)', f'switchCeTab({new_index})', html)
    # Replace active classes → inactive
    html = html.replace(
        'ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250',
        'ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250'
    )
    return html


def make_ce_panel_hidden(html):
    """Ensure the panel has the hidden class."""
    return html.replace(
        '<div class="ce-panel ce-panel-anim" role="tabpanel">',
        '<div class="ce-panel ce-panel-anim hidden" role="tabpanel">'
    )


def extract_kc_buttons(text):
    """Return list of (label, html_block) for every kc-tab button."""
    buttons = []
    for m in re.finditer(r'<button onclick="switchKcTab\(\d+\)"', text):
        start = m.start()
        end   = text.find('</button>', start) + 9
        html  = text[start:end]
        label = re.search(r'kc-tab-label[^>]*>([^<]+)<', html)
        buttons.append((label.group(1).strip() if label else '?', html))
    return buttons


def extract_kc_panels(text):
    """Return list of (label, html_block) for every kc-panel div."""
    panels = []
    for m in re.finditer(r'<div class="kc-panel', text):
        start = m.start()
        end   = find_closing_div(text, start)
        html  = text[start:end]
        label = re.search(r'kc-panel-title[^>]*>([^<]+)<|font-bold text-gray-800[^>]*>([^<]+)<', html)
        panels.append(html)
    return panels


def make_kc_button_inactive(html, new_index):
    """Convert a (possibly active) KC button to inactive and renumber."""
    html = re.sub(r'switchKcTab\(\d+\)', f'switchKcTab({new_index})', html)
    # Remove active class
    html = html.replace('kc-tab kc-tab-active group ', 'kc-tab group ')
    # Active num indicator → inactive
    html = re.sub(
        r'style="background:#CB187D;color:#fff;box-shadow:[^"]*"',
        'style="background:#f3f4f6;color:#9ca3af"',
        html
    )
    # Active label text color → inactive
    html = html.replace(
        'kc-tab-label text-xs font-bold leading-tight text-gray-900',
        'kc-tab-label text-xs font-bold leading-tight text-gray-400'
    )
    return html


def make_kc_panel_hidden(html):
    """Ensure the kc-panel has the hidden class."""
    html = html.replace(
        '<div class="kc-panel kc-panel-anim" ',
        '<div class="kc-panel kc-panel-anim hidden" '
    )
    return html


# ─────────────────────────────────────────────────────────────────────────────
# Core merge function
# ─────────────────────────────────────────────────────────────────────────────

def merge_lesson(dest_file, secondary_files, new_h1_title):
    """
    Merge CE tabs and KC tabs from all secondary_files into dest_file.
    Also updates the hero H1 title.
    """
    dest_path = os.path.join(BASE_DEST, dest_file)
    dest_text = open(dest_path, encoding='utf-8').read()

    print(f'\n── {dest_file}')
    print(f'   H1 → "{new_h1_title}"')

    # ── 1. Update H1 title ────────────────────────────────────────────────
    dest_text = re.sub(
        r'(<h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-\[1\.15\] tracking-tight">)[^<]+(</h1>)',
        rf'\g<1>{new_h1_title}\g<2>',
        dest_text
    )

    for sec_rel_path in secondary_files:
        sec_path = os.path.join(BASE_SRC, sec_rel_path)
        sec_text = open(sec_path, encoding='utf-8').read()
        sec_name = os.path.basename(sec_path)

        # ── CE buttons ──────────────────────────────────────────────────
        existing_ce = extract_ce_buttons(dest_text)
        new_ce_btns = extract_ce_buttons(sec_text)

        ce_buttons_html = ''
        for i, (label, btn_html) in enumerate(new_ce_btns):
            new_idx    = len(existing_ce) + i
            btn_inactive = make_ce_button_inactive(btn_html, new_idx)
            ce_buttons_html += f'\n{btn_inactive}'
            print(f'   + CE tab [{new_idx}] "{label}"  ← {sec_name}')

        # Insert before closing </div> of the tablist
        tablist_marker = '<div class="flex items-center gap-2 mb-6" role="tablist">'
        tl_pos  = dest_text.find(tablist_marker)
        tl_end  = find_closing_div(dest_text, tl_pos)
        # Insert just before the closing </div>
        insert_pos = tl_end - 6  # before "</div>"
        dest_text = dest_text[:insert_pos] + ce_buttons_html + '\n' + dest_text[insert_pos:]

        # ── CE panels ───────────────────────────────────────────────────
        # Re-read dest_text positions after insertion
        ce_panel_positions = [m.start() for m in re.finditer(r'<div class="ce-panel', dest_text)]
        last_ce_panel_start = ce_panel_positions[-1]
        last_ce_panel_end   = find_closing_div(dest_text, last_ce_panel_start)

        new_ce_panels = extract_ce_panels(sec_text)
        ce_panels_html = ''
        for (_, panel_html) in new_ce_panels:
            ce_panels_html += '\n' + make_ce_panel_hidden(panel_html)

        dest_text = dest_text[:last_ce_panel_end] + ce_panels_html + dest_text[last_ce_panel_end:]

        # ── KC buttons ──────────────────────────────────────────────────
        existing_kc = extract_kc_buttons(dest_text)
        new_kc_btns = extract_kc_buttons(sec_text)

        kc_buttons_html = ''
        for i, (label, btn_html) in enumerate(new_kc_btns):
            new_idx = len(existing_kc) + i
            btn_inactive = make_kc_button_inactive(btn_html, new_idx)
            kc_buttons_html += f'\n{btn_inactive}'
            print(f'   + KC tab [{new_idx}] "{label}"  ← {sec_name}')

        # Insert before </div><!-- /sidebar -->
        sidebar_close = '</div><!-- /sidebar -->'
        sc_pos = dest_text.find(sidebar_close)
        dest_text = dest_text[:sc_pos] + kc_buttons_html + '\n          ' + dest_text[sc_pos:]

        # ── KC panels ───────────────────────────────────────────────────
        kc_panel_positions = [m.start() for m in re.finditer(r'<div class="kc-panel', dest_text)]
        last_kc_panel_start = kc_panel_positions[-1]
        last_kc_panel_end   = find_closing_div(dest_text, last_kc_panel_start)

        new_kc_panels = extract_kc_panels(sec_text)
        kc_panels_html = ''
        for panel_html in new_kc_panels:
            kc_panels_html += '\n' + make_kc_panel_hidden(panel_html)

        dest_text = dest_text[:last_kc_panel_end] + kc_panels_html + dest_text[last_kc_panel_end:]

    # ── Write ──────────────────────────────────────────────────────────────
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(dest_text)
    print(f'   ✅ Written → {dest_path}')


# ─────────────────────────────────────────────────────────────────────────────
# Merge definitions
# ─────────────────────────────────────────────────────────────────────────────

MERGES = [
    (
        'lesson01_pandas_and_dataframes.html',
        ['mod_01_data_analysis_with_pandas/lesson02_dataframes_explained.html'],
        'Pandas &amp; DataFrames',
    ),
    (
        'lesson02_reading_files_csv_excel_json.html',
        [
            'mod_02_working_with_data_sources/lesson02_working_with_json_files.html',
            'mod_02_working_with_data_sources/lesson01_reading_csv_files.html',
        ],
        'Reading Files: CSV, Excel &amp; JSON',
    ),
    (
        'lesson03_selecting_and_filtering_data.html',
        ['mod_01_data_analysis_with_pandas/lesson05_filtering_rows.html'],
        'Selecting &amp; Filtering Data',
    ),
    (
        'lesson09_connecting_to_databases_and_running_sql.html',
        ['mod_02_working_with_data_sources/lesson04_running_sql_in_python.html'],
        'Connecting to Databases &amp; Running SQL',
    ),
    (
        'lesson10_writing_to_databases_and_managing_credentials.html',
        ['mod_02_working_with_data_sources/lesson06_managing_credentials_env.html'],
        'Writing to Databases &amp; Managing Credentials',
    ),
    (
        'lesson13_building_and_automating_reports.html',
        ['mod_03_python_for_analysts/lesson06_automating_reports_end_to_end.html'],
        'Building &amp; Automating Reports',
    ),
    (
        'lesson14_handling_large_data.html',
        [
            'mod_04_handling_large_data/lesson03_chunk_processing.html',
            'mod_04_handling_large_data/lesson04_processing_millions_of_rows.html',
        ],
        'Handling Large Data: Memory, Chunks &amp; Scale',
    ),
    (
        'lesson15_parquet_and_performance_profiling.html',
        [
            'mod_04_handling_large_data/lesson06_parquet_files.html',
            'mod_04_handling_large_data/lesson13_performance_profiling.html',
        ],
        'Parquet Files &amp; Performance Profiling',
    ),
]


if __name__ == '__main__':
    for dest, secondaries, new_title in MERGES:
        merge_lesson(dest, secondaries, new_title)
    print('\n✅ All merges complete.')
