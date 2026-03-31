import os, re

root = r'C:/Users/nightwolf/Projects/Python-Learning/pages/track_02_data_analytics'

mods = [
    ('mod_01_data_analysis_with_pandas', [
        'lesson01_introduction_to_pandas.html',
        'lesson02_dataframes_explained.html',
        'lesson03_reading_data_csv_excel.html',
        'lesson04_selecting_columns.html',
        'lesson05_filtering_rows.html',
        'lesson06_creating_calculated_columns.html',
        'lesson07_aggregations_group_by.html',
        'lesson08_joining_data_merge.html',
        'lesson09_handling_missing_data.html',
        'lesson10_exporting_data.html',
    ]),
    ('mod_02_working_with_data_sources', [
        'lesson01_reading_csv_files.html',
        'lesson02_working_with_json_files.html',
        'lesson03_connecting_to_databases.html',
        'lesson04_running_sql_in_python.html',
        'lesson05_writing_data_back_to_a_database.html',
        'lesson06_managing_credentials_env.html',
    ]),
    ('mod_03_python_for_analysts', [
        'lesson01_why_analysts_use_python.html',
        'lesson02_replacing_excel_workflows_with_python.html',
        'lesson03_using_python_with_sql_queries.html',
        'lesson04_automating_repetitive_data_tasks.html',
        'lesson05_building_a_simple_reporting_script.html',
        'lesson06_automating_reports_end_to_end.html',
    ]),
    ('mod_04_handling_large_data', [
        'lesson02_memory_optimization.html',
        'lesson03_chunk_processing.html',
        'lesson04_processing_millions_of_rows.html',
        'lesson05_columnar_storage.html',
        'lesson06_parquet_files.html',
        'lesson13_performance_profiling.html',
    ]),
]

icon_re = re.compile(r'data-icon="([^"]+)"')
label_re = re.compile(r'<p class="text-sm font-semibold text-gray-800">([^<]+)</p>')

for mod, files in mods:
    for fname in files:
        path = os.path.join(root, mod, fname)
        html = open(path, encoding='utf-8').read()
        
        # Find objective section
        obj_start = html.find('<section id="objective">')
        obj_end = html.find('</section>', obj_start)
        obj_html = html[obj_start:obj_end]
        
        # Extract obj-card divs
        cards = re.findall(r'<div class="obj-card flex items-start.*?</div>\s*</div>', obj_html, re.DOTALL)
        
        print(f"\n=== {mod}/{fname} ===")
        for i, card in enumerate(cards[:4]):
            icons = icon_re.findall(card)
            labels = label_re.findall(card)
            # filter to fa6-solid icons
            fa_icons = [ic for ic in icons if ic.startswith('fa6-solid')]
            label = labels[0] if labels else '???'
            icon = fa_icons[0] if fa_icons else icons[0] if icons else '???'
            print(f"  Card {i+1}: icon={icon}  label={label}")
