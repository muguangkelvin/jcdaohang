import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('public/index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total indexed pages in index.json: {len(data)}")

def simulate_search(query):
    q = query.lower()
    matches = 0
    sample_titles = []
    for item in data:
        t = item['title'].lower()
        d = item['description'].lower()
        kw = item['keywords'].lower()
        c = item['content'].lower()
        if q in t or q in d or q in kw or q in c:
            matches += 1
            if len(sample_titles) < 2:
                sample_titles.append(item['title'])
    print(f"Query '{query}' matches {matches} pages. Samples: {sample_titles}")

simulate_search("灵动云")
simulate_search("Clash")
simulate_search("IPLC")
simulate_search("ChatGPT")
simulate_search("折合7元")
simulate_search("节点超时")
simulate_search("Shadowrocket")
