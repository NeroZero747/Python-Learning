"""Fix lesson04 KC button classes to match lesson03 design."""

path = r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson04_efficient_storage_parquet.html'
html = open(path, encoding='utf-8').read()

TARGET = (
    'quiz-btn w-full text-left px-4 py-2.5 rounded-xl border border-gray-200 '
    'bg-white text-sm font-medium text-gray-600 '
    'hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors'
)

# Fix 1: broken backslash-escaped class written by previous bad script
BROKEN = (
    'quiz-btn w-full text-left px-4 py-2.5 rounded-xl border border-gray-200 '
    'bg-white text-sm font-medium text-gray-600 '
    r'hover:border-[\#CB187D] hover:bg-[\#fdf0f7] transition-colors'
)

# Fix 2: original correct-hover buttons (px-5, no w-full, text-left at end)
OLD_CORRECT = (
    'quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 '
    'bg-white text-sm font-medium text-gray-600 text-left '
    'hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors'
)

n_broken  = html.count(BROKEN)
n_correct = html.count(OLD_CORRECT)

html = html.replace(BROKEN, TARGET)
html = html.replace(OLD_CORRECT, TARGET)

open(path, 'w', encoding='utf-8').write(html)
print(f'Fixed {n_broken}  broken-escape buttons  -> TARGET')
print(f'Fixed {n_correct} old-correct buttons     -> TARGET')
print('Done')
