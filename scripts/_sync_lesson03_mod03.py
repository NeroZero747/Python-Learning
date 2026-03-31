import re

ref_file    = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson01_what_is_programming.html"
target_file = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_03_object_oriented_programming/lesson03_attributes_methods.html"

with open(ref_file, encoding="utf-8") as f:
    ref = f.read()
with open(target_file, encoding="utf-8") as f:
    content = f.read()

# Step 1 — Extract style block from lesson01
style_match = re.search(r'(<style>.*?</style>)', ref, re.DOTALL)
assert style_match, "Could not find <style> block in reference"
ref_style = style_match.group(1)
print(f"Step 1 OK — extracted style block ({ref_style.count(chr(10))+1} lines)")

# Step 2 — Strip forbidden HTML shell tags
content = re.sub(r'<!DOCTYPE[^>]*>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'<html[^>]*>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'</html>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'<head>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'</head>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'<body[^>]*>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'</body>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'  <meta[^>]*/?\>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'<meta[^>]*/?\>\s*\n?', '', content, flags=re.IGNORECASE)
content = re.sub(r'<title>.*?</title>\s*\n?', '', content, flags=re.IGNORECASE | re.DOTALL)
# Trim leading blank lines and locate first preconnect link
first_link = content.find('<link rel="preconnect"')
if first_link > 0:
    content = content[first_link:]
content = content.lstrip('\n')
# Remove trailing </body>, </html> and blank lines
content = re.sub(r'\s*(</body>|</html>)\s*$', '', content, flags=re.IGNORECASE)
content = content.rstrip()
print(f"Step 2 OK — starts: {repr(content[:50])}")
print(f"         — ends:   {repr(content[-30:])}")

# Step 3 — Replace style block in target
style_in_target = re.search(r'<style>.*?</style>', content, re.DOTALL)
assert style_in_target, "Could not find <style> block in target"
content = content[:style_in_target.start()] + ref_style + content[style_in_target.end():]
print("Step 3 OK — style block replaced")

# Step 4 — Add id="hub-root"
if 'id="hub-root"' in content:
    print("Step 4 SKIP — id=hub-root already present")
else:
    content, n = re.subn(
        r'<div class="bg-gray-50 min-h-screen">',
        '<div id="hub-root" class="bg-gray-50 min-h-screen">',
        content, count=1
    )
    print(f"Step 4 OK — id=hub-root added ({n} replacement)")

# Step 5 — Hover fix
if 'background-color: #ffffff' in content:
    print("Step 5 SKIP — hover fix already present")
else:
    old = ('    .obj-card-kt:hover { box-shadow: none; }\n'
           '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }\n'
           '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }')
    new = ('    .obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }\n'
           '    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }\n'
           '    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }')
    if old in content:
        content = content.replace(old, new, 1)
        print("Step 5 OK — hover fix applied")
    else:
        print("Step 5 WARN — pattern not found; may already be correct or needs manual check")

# Write
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("\nFile written.")

# Verify
with open(target_file, encoding='utf-8') as f:
    final = f.read()
lines = final.splitlines()
print("\n── Verification ──")
print(f"  Starts with preconnect : {lines[0].strip().startswith('<link rel=\"preconnect\"')}")
print(f"  Ends with </script>    : {final.rstrip().endswith('</script>')}")
print(f"  No <!DOCTYPE           : {'<!DOCTYPE' not in final.upper()}")
print(f"  No <html>              : {'<HTML>' not in final.upper()}")
print(f"  No <head>              : {'<head>' not in final.lower()}")
print(f"  No <body>              : {'<body>' not in final.lower()}")
print(f"  id=hub-root count      : {final.count('id=\"hub-root\"')}")
print(f"  hover fix present      : {'background-color: #ffffff' in final}")
