import re

filepath = r'c:\Users\nightwolf\Projects\Python-Learning\pages\hub_home_page.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the second occurrence of <section id="skills"
marker = '<section id="skills"'
first = content.find(marker)
second = content.find(marker, first + 1)

if second == -1:
    print('Only one #skills section found — nothing to remove.')
else:
    # Find start of the comment block preceding the second skills section
    # Walk backwards from second to find the nearest <!-- 
    comment_start = content.rfind('\n\n  <!--', 0, second)
    
    # Find the closing </section> of the second skills section
    section_end = content.find('  </section>', second)
    section_end += len('  </section>')
    
    print(f'First #skills at char {first}')
    print(f'Second #skills at char {second}')
    print(f'Comment block start at char {comment_start}')
    print(f'Section end at char {section_end}')
    print()
    print('--- Text being removed ---')
    print(repr(content[comment_start:comment_start+120]))
    print('...')
    print(repr(content[section_end-60:section_end+30]))
    print()

    # Remove the block (comment + duplicate section)
    result = content[:comment_start] + content[section_end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)

    removed = content.count('\n') - result.count('\n')
    print(f'Done — removed ~{removed} lines')
