"""
Fix KC panel mismatches and div balance issues in L02 and L05 after merge.
L02: 4 KC tabs but 3 panels → insert L03's Data Visualization panel
L05: 5 KC tabs but 3 panels → insert L09's CI and CD panels
Both: fix div balance (+4 from imprecise CE panel extraction)
"""

import re
import os

DIR = os.path.join('pages', 'mod_05_data_application')
BACKUP = os.path.join(DIR, '_backup')


def extract_kc_panels(filepath):
    """Extract all KC panels from a lesson file."""
    text = open(filepath, encoding='utf-8').read()
    html = text.split('<script>')[0] if '<script>' in text else text
    kc_start = html.find('id="key-concepts"')
    kc_end = html.find('</section>', kc_start)
    kc = html[kc_start:kc_end]
    panels = re.findall(
        r'(<div class="kc-panel[^"]*"[^>]*data-color="[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>)',
        kc, re.DOTALL
    )
    return panels


def fix_lesson02():
    """Insert L03's Data Visualization KC panel as 4th panel in L02."""
    filepath = os.path.join(DIR, 'lesson02_introduction_to_streamlit.html')
    text = open(filepath, encoding='utf-8').read()
    
    # Get L03's panel 2 (Data Visualization)
    l03_panels = extract_kc_panels(os.path.join(BACKUP, 'lesson03_building_a_simple_dashboard.html'))
    if len(l03_panels) < 3:
        print("  ❌ Could not extract L03 KC panels")
        return
    
    dv_panel = l03_panels[2]  # Data Visualization (blue)
    # Make sure it has 'hidden'
    if 'hidden' not in dv_panel[:80]:
        dv_panel = dv_panel.replace('kc-panel kc-panel-anim ', 'kc-panel kc-panel-anim hidden ')
    
    # Find the last KC panel in L02 and insert after it
    html_part = text.split('<script>')[0]
    kc_start = html_part.find('id="key-concepts"')
    kc_end = html_part.find('</section>', kc_start)
    kc_section = html_part[kc_start:kc_end]
    
    # Find the end of the last kc-panel (3rd panel)
    # The panels end with </div>\n</div>\n</div> but the flex-1 wrapper has its own </div>
    # We need to find the right spot: after the last panel's closing </div>s
    
    # Find all panel end positions in the KC section
    panel_ends = [m.end() for m in re.finditer(
        r'<div class="kc-panel[^"]*"[^>]*data-color="[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>',
        kc_section, re.DOTALL
    )]
    
    if len(panel_ends) < 3:
        print(f"  ❌ Only found {len(panel_ends)} KC panels in L02")
        return
    
    # Insert the new panel after the last panel
    insert_pos = kc_start + panel_ends[-1]
    text = text[:insert_pos] + '\n' + dv_panel + text[insert_pos:]
    
    # Now fix div balance — check and correct
    html_part2 = text.split('<script>')[0]
    opens = html_part2.count('<div')
    closes = html_part2.count('</div>')
    balance = opens - closes
    print(f"  L02 div balance after KC fix: {balance}")
    
    # Fix CE panel div balance — the issue is extra unclosed divs from panel extraction
    # Find the CE panels that were inserted and check their structure
    # The extra divs are likely from the CE panel extraction having incomplete div closings
    # Let's find and fix by adding missing </div> tags
    if balance > 0:
        # Add closing divs before </section> of code-examples
        ce_section_start = text.find('id="code-examples"')
        ce_section_end = text.find('</section>', ce_section_start)
        # Insert balance number of </div> tags before the section close
        fix = '\n</div>' * balance
        # Find the spot just before </div>\n  </div>\n</section> for code-examples
        close_pattern = text.rfind('</div>\n  </div>\n</section>', ce_section_start, ce_section_end + 20)
        if close_pattern > 0:
            text = text[:close_pattern] + fix + '\n' + text[close_pattern:]
        else:
            # Fallback: add before the section end
            text = text[:ce_section_end] + fix + '\n' + text[ce_section_end:]
    
    # Recheck balance
    html_part3 = text.split('<script>')[0]
    opens2 = html_part3.count('<div')
    closes2 = html_part3.count('</div>')
    balance2 = opens2 - closes2
    print(f"  L02 div balance after full fix: {balance2}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    
    lines = text.count('\n') + 1
    print(f"  ✅ L02 updated ({lines} lines)")


def fix_lesson05():
    """Insert L09's CI and CD KC panels as tabs 3-4 in L05."""
    filepath = os.path.join(DIR, 'lesson05_deploying_data_applications.html')
    text = open(filepath, encoding='utf-8').read()
    
    # Get L09's panels 1 (CI) and 2 (CD)
    l09_panels = extract_kc_panels(os.path.join(BACKUP, 'lesson09_devops_concepts_for_data_analytics.html'))
    if len(l09_panels) < 3:
        print(f"  ❌ Could not extract L09 KC panels (found {len(l09_panels)})")
        return
    
    ci_panel = l09_panels[1]  # CI (violet)
    cd_panel = l09_panels[2]  # CD (blue)
    
    # Ensure hidden
    for panel_text in [ci_panel, cd_panel]:
        if 'hidden' not in panel_text[:80]:
            panel_text = panel_text.replace('kc-panel kc-panel-anim ', 'kc-panel kc-panel-anim hidden ')
    
    # Need a panel for tab index 3 (CI/CD Pipelines) and tab index 4 (DevOps for Data)
    # Use L09's CI panel for "CI/CD Pipelines" and CD panel for "DevOps for Data"
    
    # Find insertion point in L05's KC section
    html_part = text.split('<script>')[0]
    kc_start = html_part.find('id="key-concepts"')
    kc_end = html_part.find('</section>', kc_start)
    kc_section = html_part[kc_start:kc_end]
    
    panel_ends = [m.end() for m in re.finditer(
        r'<div class="kc-panel[^"]*"[^>]*data-color="[^"]*"[^>]*role="tabpanel">.*?</div>\s*</div>\s*</div>',
        kc_section, re.DOTALL
    )]
    
    if len(panel_ends) < 3:
        print(f"  ❌ Only found {len(panel_ends)} KC panels in L05")
        return
    
    insert_pos = kc_start + panel_ends[-1]
    text = text[:insert_pos] + '\n' + ci_panel + '\n' + cd_panel + text[insert_pos:]
    
    # Fix div balance
    html_part2 = text.split('<script>')[0]
    opens = html_part2.count('<div')
    closes = html_part2.count('</div>')
    balance = opens - closes
    print(f"  L05 div balance after KC fix: {balance}")
    
    if balance > 0:
        ce_section_start = text.find('id="code-examples"')
        ce_section_end = text.find('</section>', ce_section_start)
        fix = '\n</div>' * balance
        close_pattern = text.rfind('</div>\n  </div>\n</section>', ce_section_start, ce_section_end + 20)
        if close_pattern > 0:
            text = text[:close_pattern] + fix + '\n' + text[close_pattern:]
        else:
            text = text[:ce_section_end] + fix + '\n' + text[ce_section_end:]
    
    html_part3 = text.split('<script>')[0]
    opens2 = html_part3.count('<div')
    closes2 = html_part3.count('</div>')
    balance2 = opens2 - closes2
    print(f"  L05 div balance after full fix: {balance2}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    
    lines = text.count('\n') + 1
    print(f"  ✅ L05 updated ({lines} lines)")


def main():
    print("── Fixing L02 KC panels + div balance ──")
    fix_lesson02()
    
    print("\n── Fixing L05 KC panels + div balance ──")
    fix_lesson05()
    
    # Final verification
    print("\n── Final verification ──")
    for f in sorted(os.listdir(DIR)):
        if not f.startswith('lesson') or not f.endswith('.html'):
            continue
        text = open(os.path.join(DIR, f), encoding='utf-8').read()
        html = text.split('<script>')[0]
        
        kc_tabs = len(re.findall(r'kc-tab-label', html))
        kc_panels = len(re.findall(r'class="kc-panel', html))
        ce_tabs = len(re.findall(r'ce-step-label', html))
        ce_panels = len(re.findall(r'class="ce-panel', html))
        
        opens = html.count('<div')
        closes = html.count('</div>')
        balance = opens - closes
        
        status = '✅' if balance == 0 and kc_tabs == kc_panels and ce_tabs == ce_panels else '⚠️'
        print(f"  {status} {f}: KC={kc_tabs}/{kc_panels} CE={ce_tabs}/{ce_panels} div_balance={balance}")


if __name__ == '__main__':
    main()
