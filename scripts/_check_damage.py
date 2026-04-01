import os, re

fp = "pages/track_03_data_engineering/mod_03_api_data_integration/lesson01_what_is_an_api.html"
c = open(fp, "r", encoding="utf-8").read()
sections = re.findall(r'section id="([^"]+)"', c)
print("Sections:", sections)
print("Lines:", c.count("\n"))
print("Has closing script:", "</script>" in c)
print("Last 200 chars:", repr(c[-200:]))
