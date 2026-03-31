base = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/'
files = ['lesson01_what_is_programming.html','lesson02_variables_data_types.html','lesson03_additional_python_data_types.html','lesson04_lists_dictionaries.html','lesson05_operators.html','lesson06_if_statements.html']
shell_tags = ['DOCTYPE','<html ','<head>','<body>','</body>','</html>']

for f in files:
    txt = open(base + f).read()
    hub_id = 'id="hub-root"' in txt
    forbidden = [t for t in shell_tags if t in txt]
    ends = txt.rstrip()[-10:]
    print(f"{f}: hub-id={hub_id}  forbidden={forbidden or 'none'}  ends={repr(ends)}")
