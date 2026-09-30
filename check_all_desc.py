import glob
import json
import os

files = glob.glob('content/**/*.md', recursive=True)
desc_dict = {}

for f in files:
    if '_index.md' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        desc = ''
        for line in lines[:25]:
            if line.startswith('description:'):
                desc = line.split('description:', 1)[1].strip().strip('"\'')
                break
        if desc:
            desc_dict.setdefault(desc, []).append(f)

print(f'Total articles scanned: {sum(len(v) for v in desc_dict.values())}')
print(f'Total unique descriptions: {len(desc_dict)}')

duplicates = {k: v for k, v in desc_dict.items() if len(v) > 1}
if duplicates:
    print(f'\nFound {len(duplicates)} duplicate descriptions:')
    for d, file_list in duplicates.items():
        print(f'Count {len(file_list)}: {d[:60]}...')
        for fl in file_list:
            print(f'   -> {fl}')
else:
    print('\n🎉 All articles have 100% UNIQUE descriptions!')
