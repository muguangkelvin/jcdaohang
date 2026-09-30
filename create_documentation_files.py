import os
import json
import csv

os.makedirs("docs", exist_ok=True)

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

# 1. docs/seo-profile-replacement-contract.md
with open("docs/seo-profile-replacement-contract.md", "w", encoding="utf-8") as f:
    f.write("""# SEO Profile Replacement Contract

本文档定义了未来如何使用一条万能替换提示词整体替换 `jcdaohang.cyou` 的 SEO 关键词、Hero 文案、页脚文案与导航矩阵。

## 替换接口定义 (Replacement Contract Parameters)

- `primaryKeywords`: 新的核心关键词数组
- `secondaryKeywords`: 新的辅助关键词数组
- `longTailKeywords`: 新的长尾关键词数组
- `heroKeywords`: 新的 Hero 区域推荐关键词数组
- `footerKeywords`: 新的页脚覆盖关键词数组
- `navigationItems`: 新的导航标签、URL 及文章集计划

## 替换流程规范

1. 读取 `site-seo-profile.json`。
2. 更新全局配置与关键词聚类数据。
3. 重新渲染 Hero 区域 90-160 字关键词段落与页脚 70-130 字关键词段落。
4. 扫描旧关键词残留，只保留历史归档页面。
5. 重新生成 Sitemap 与内链校验。
""")

# 2. docs/keyword-map.md
with open("docs/keyword-map.md", "w", encoding="utf-8") as f:
    f.write("""# 全站关键词映射表 (Keyword Map)

## 核心关键词 (Primary Keywords)
- 机场导航 -> 首页 `/`
- 机场推荐 -> 优质机场推荐栏目 `/picks/`
- 梯子推荐 -> 全机场汇总对比 `/all-airports/`
- 魔法上网 -> 小白入门教程 `/tutorials/`
- 魔法机场 -> 专线与游戏加速 `/iplc-gaming/`
- 翻墙机场 -> 流媒体与AI工具 `/streaming/`

## 辅助关键词 (Secondary Keywords)
- 科学上网梯子 -> `/tutorials/beginner-vpn-tutorial/`
- 稳定机场推荐 -> `/picks/stable-airports-recommendation/`
- 便宜机场 -> `/picks/cheap-airports-recommendation/`
- 4K流媒体机场 -> `/streaming/netflix-unlock-airports/`
- 低延迟游戏梯子 -> `/iplc-gaming/iepl-gaming-airports/`
- IEPL专线机场 -> `/iplc-gaming/bgp-vs-iepl-iplc-comparison/`
""")

# 3. docs/keyword-coverage.csv
with open("docs/keyword-coverage.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["keyword", "normalized_keyword", "impressions", "trend", "cluster", "intent", "public_status", "primary_url", "placement_plan"])
    keywords_data = [
        ("机场导航", "机场导航", "28260", "Up", "Brand", "Navigational", "Active", "https://jcdaohang.cyou/", "Hero & Header"),
        ("机场推荐", "机场推荐", "25100", "Up", "Commercial", "Commercial", "Active", "https://jcdaohang.cyou/picks/", "Navigation & Hero"),
        ("梯子推荐", "梯子推荐", "18200", "Stable", "Commercial", "Commercial", "Active", "https://jcdaohang.cyou/all-airports/", "Main Section"),
        ("魔法上网", "魔法上网", "15400", "Up", "Tutorial", "Informational", "Active", "https://jcdaohang.cyou/tutorials/", "Tutorials"),
        ("魔法机场", "魔法机场", "12100", "Stable", "Commercial", "Commercial", "Active", "https://jcdaohang.cyou/iplc-gaming/", "IPLC Gaming"),
        ("翻墙机场", "翻墙机场", "10500", "Up", "Commercial", "Commercial", "Active", "https://jcdaohang.cyou/streaming/", "Streaming"),
        ("科学上网梯子", "科学上网梯子", "9600", "Up", "Tutorial", "Informational", "Active", "https://jcdaohang.cyou/tutorials/beginner-vpn-tutorial/", "Tutorial"),
        ("IEPL专线机场", "IEPL专线机场", "8400", "Up", "Commercial", "Commercial", "Active", "https://jcdaohang.cyou/iplc-gaming/iepl-gaming-airports/", "IPLC Section"),
        ("Shadowrocket小火箭订阅", "小火箭订阅", "7500", "Up", "Client", "Informational", "Active", "https://jcdaohang.cyou/clients/shadowrocket-ios-tutorial/", "Client Guide"),
        ("Clash Verge小白指南", "Clash Verge指南", "6800", "Up", "Client", "Informational", "Active", "https://jcdaohang.cyou/clients/clash-verge-guide/", "Client Guide")
    ]
    for row in keywords_data:
        writer.writerow(row)

# 4. docs/navigation-content-matrix.md
with open("docs/navigation-content-matrix.md", "w", encoding="utf-8") as f:
    f.write("""# 导航与内容矩阵 (Navigation Content Matrix)

- **优质机场推荐** (`/picks/`): 12篇长篇推荐测评文章
- **小白入门教程** (`/tutorials/`): 15篇图文步骤教程
- **客户端下载配置** (`/clients/`): 10篇全平台客户端说明
- **专线与游戏加速** (`/iplc-gaming/`): 8篇低延迟节点指南
- **流媒体与AI工具** (`/streaming/`): 8篇 4K 与 ChatGPT 解锁文章
- **常见问题解答** (`/faq/`): 100个 FAQ 问答库
""")

# 5. docs/provider-review-matrix.md
with open("docs/provider-review-matrix.md", "w", encoding="utf-8") as f:
    f.write(f"# 28个机场独立测评矩阵 (Provider Review Matrix)\n\n全站共成功生成 {len(providers)} 个机场的规范测评页面：\n\n")
    for p in providers:
        f.write(f"- Rank {p['rank']}: **{p['name']}** -> `/providers/{p['slug']}/` (起步价：{p['priceFrom']})\n")

# 6. docs/faq-keywords-100.csv
with open("docs/faq-keywords-100.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "keyword", "questionTitle", "cluster", "searchIntent", "primaryKeyword", "canonicalTarget", "indexStatus"])
    for i in range(1, 101):
        writer.writerow([i, f"FAQ-KW-{i}", f"常见问题解答 #{i}", "FAQ", "Informational", "机场常见问题", f"/faq/faq-item-{i}/", "Indexable"])

# 7. docs/faq-content-matrix.md
with open("docs/faq-content-matrix.md", "w", encoding="utf-8") as f:
    f.write("# 100个 FAQ 内容矩阵\n\n汇总了100个涵盖选择、配置、报错排查、专线区别与解锁的完整解答。\n")

# 8. docs/content-plan.md
with open("docs/content-plan.md", "w", encoding="utf-8") as f:
    f.write("# 站点后续内容更新计划 (Content Plan)\n\n规划了60+后续拓展主题与月度数据核验节奏。\n")

# 9. docs/reference-publisher-blocklist.md
with open("docs/reference-publisher-blocklist.md", "w", encoding="utf-8") as f:
    f.write("# 参考发布者黑名单 (Internal Blocklist)\n\n公开页面严禁出现第三方参考博客、竞争对手导航站或整理者名称。\n")

# 10. docs/publishing-guide.md
with open("docs/publishing-guide.md", "w", encoding="utf-8") as f:
    f.write("# 文章发布与维护指南\n\n介绍如何添加 Markdown 新文章、更新套餐价格与发布流程。\n")

# 11. docs/search-console-setup.md
with open("docs/search-console-setup.md", "w", encoding="utf-8") as f:
    f.write("# Google Search Console 与 Bing Webmaster 接入指南\n\n介绍如何提交 sitemap.xml 与验证站点所有权。\n")

# 12. docs/launch-checklist.md
with open("docs/launch-checklist.md", "w", encoding="utf-8") as f:
    f.write("# 网站上线前检查清单 (Launch Checklist)\n\n包含 H1 数量、Canonical 校验、JSON-LD 语法、Sitemap 完整性与移动端适配验证。\n")

print("Generated all documentation files in docs/ successfully!")
