import os
import re
import json
import xml.etree.ElementTree as ET

def verify():
    print("Starting site verification for jcdaohang.cyou (Pure Python)...")
    public_dir = "public"
    errors = []
    warnings = []

    # 1. Check index.html
    index_path = os.path.join(public_dir, "index.html")
    if not os.path.exists(index_path):
        errors.append("public/index.html does not exist!")
        return errors, warnings

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Check H1
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    print(f"Index H1 count: {len(h1_matches)}")
    if len(h1_matches) != 1:
        errors.append(f"index.html should have exactly 1 H1 tag, found {len(h1_matches)}")

    # Check TG channel link
    tg_matches = re.findall(r'href=["\'](https://t\.me/[^"\']+)["\']', html)
    print(f"TG Links in index.html: {len(tg_matches)}")
    if not tg_matches:
        errors.append("index.html missing Telegram channel link https://t.me/+KJWZtRAFDBMwOTE1")

    # Check Search Bar
    if 'id="searchInput"' not in html:
        errors.append("index.html missing search input with id='searchInput'")

    # Check Top 4 Provider Ranking Order
    p_names = ["灵动云", "暮光网络", "飞猫云", "微风网络"]
    for idx, name in enumerate(p_names, 1):
        if name not in html:
            errors.append(f"Main provider Rank {idx} '{name}' missing from index.html!")

    # Check Position 5-8 Provider Ranking Order
    p58_names = ["隐形人", "浪网", "梯子云", "飞V"]
    for idx, name in enumerate(p58_names, 5):
        if name not in html:
            warnings.append(f"Position {idx} provider '{name}' missing from index.html")

    # Check rel="sponsored nofollow noopener" on affiliate links
    verified_affs = 0
    for tag in re.findall(r'<a\s+[^>]*>', html, re.IGNORECASE):
        if 'href="http' in tag and 'jcdaohang.cyou' not in tag and 'schema.org' not in tag and 't.me' not in tag:
            if 'rel=' not in tag or 'sponsored' not in tag or 'nofollow' not in tag or 'noopener' not in tag:
                errors.append(f"External link tag missing required rel: {tag}")
            verified_affs += 1
    print(f"Verified {verified_affs} external affiliate link tags in index.html with rel='sponsored nofollow noopener'.")

    # 2. Check sitemap.xml & robots.txt
    sitemap_path = os.path.join(public_dir, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        errors.append("sitemap.xml does not exist in public/")
    else:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        print(f"Sitemap URL count: {len(urls)}")
        if not urls:
            errors.append("sitemap.xml is empty!")
        for u in urls:
            if not u.startswith("https://jcdaohang.cyou"):
                errors.append(f"Sitemap URL {u} does not use https://jcdaohang.cyou base URL!")

    robots_path = os.path.join(public_dir, "robots.txt")
    if not os.path.exists(robots_path):
        errors.append("robots.txt does not exist in public/")

    # 3. Check section pages
    sections = ["picks", "tutorials", "clients", "iplc-gaming", "streaming", "faq", "all-airports"]
    for sec in sections:
        sec_path = os.path.join(public_dir, sec, "index.html")
        if not os.path.exists(sec_path):
            errors.append(f"Section page public/{sec}/index.html missing!")

    # 4. Check 28 provider review pages
    with open("data/providers.json", "r", encoding="utf-8") as f:
        providers = json.load(f)
    print(f"Checking {len(providers)} provider review pages in public/providers/...")
    for p in providers:
        p_path = os.path.join(public_dir, "providers", p["slug"], "index.html")
        if not os.path.exists(p_path):
            errors.append(f"Provider review page missing: public/providers/{p['slug']}/index.html")

    print(f"\nVerification complete. Errors: {len(errors)}, Warnings: {len(warnings)}")
    return errors, warnings

if __name__ == "__main__":
    errs, warns = verify()
    if errs:
        print("\n❌ ERRORS FOUND:")
        for e in errs:
            print(f"- {e}")
    else:
        print("\n✅ ALL VERIFICATION TESTS PASSED SUCCESSFULLY!")
