import os
import re
import json
import xml.etree.ElementTree as ET

def verify():
    public_dir = "public"
    errors = []

    index_path = os.path.join(public_dir, "index.html")
    if not os.path.exists(index_path):
        errors.append("public/index.html missing")
        return errors

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    if len(h1s) != 1:
        errors.append(f"H1 count in index.html is {len(h1s)}, expected 1")

    # TG link check
    if "https://t.me/+KJWZtRAFDBMwOTE1" not in html and "t.me" not in html:
        errors.append("TG channel link missing in index.html")

    # Search bar check
    if "searchInput" not in html:
        errors.append("Search input missing")

    # Top 4 Provider Ranking Order
    p_names = ["灵动云", "暮光网络", "飞猫云", "微风网络"]
    for idx, name in enumerate(p_names, 1):
        if name not in html:
            errors.append(f"Main provider Rank {idx} '{name}' missing from index.html")

    # Check rel="sponsored nofollow noopener" on affiliate links
    tags = re.findall(r'<a\s+[^>]*>', html, re.IGNORECASE)
    checked_affs = 0
    for tag in tags:
        if 'href="http' in tag and 'jcdaohang.cyou' not in tag and 'schema.org' not in tag and 't.me' not in tag:
            if 'rel=' not in tag or 'sponsored' not in tag or 'nofollow' not in tag or 'noopener' not in tag:
                errors.append(f"Link missing rel: {tag}")
            checked_affs += 1

    # Sitemap check
    sitemap_path = os.path.join(public_dir, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        errors.append("sitemap.xml missing")
    else:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        if not urls:
            errors.append("sitemap.xml empty")
        for u in urls:
            if not u.startswith("https://jcdaohang.cyou"):
                errors.append(f"Sitemap URL invalid: {u}")

    # Robots check
    if not os.path.exists(os.path.join(public_dir, "robots.txt")):
        errors.append("robots.txt missing")

    # Provider review pages check
    with open("data/providers.json", "r", encoding="utf-8") as f:
        providers = json.load(f)

    for p in providers:
        p_path = os.path.join(public_dir, "providers", p["slug"], "index.html")
        if not os.path.exists(p_path):
            errors.append(f"Provider review page missing: {p['slug']}")

    # Section pages check
    sections = ["picks", "tutorials", "clients", "iplc-gaming", "streaming", "faq", "all-airports"]
    for sec in sections:
        if not os.path.exists(os.path.join(public_dir, sec, "index.html")):
            errors.append(f"Section page missing: {sec}")

    return errors, checked_affs, len(urls), len(providers)

if __name__ == "__main__":
    errs, aff_count, sitemap_count, provider_count = verify()
    print(f"Checked {aff_count} affiliate links in index.html.")
    print(f"Sitemap URLs: {sitemap_count}")
    print(f"Provider pages verified: {provider_count}")
    if errs:
        print(f"FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"- {e}")
    else:
        print("SUCCESS: ALL TESTS PASSED!")
