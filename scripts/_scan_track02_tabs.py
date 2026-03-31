import glob, re, os

pattern = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics\**\*.html'
files = sorted(glob.glob(pattern, recursive=True))

for fp in files:
    content = open(fp, encoding='utf-8').read()
    ce = content.count('class="ce-step ')
    pe = content.count('class="pe-step ')
    print(f'{os.path.basename(fp):<60s} ce={ce} pe={pe}')
