import re

with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

card_links = re.findall(r'article-card-title.*?href=([^\s>]+)', html)
print("Homepage article card links (Minified):")
for l in card_links:
    print("- ", l)

with open("public/picks/index.html", "r", encoding="utf-8") as f:
    picks_html = f.read()

picks_card_links = re.findall(r'article-card-title.*?href=([^\s>]+)', picks_html)
print("\nPicks section article card links (Minified):")
for l in picks_card_links:
    print("- ", l)
