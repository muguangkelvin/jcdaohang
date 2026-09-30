import os
import json

os.makedirs("content/picks", exist_ok=True)

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

# Sort providers by rank to ensure 1 to 12
top12 = [p for p in providers if p["rank"] <= 12]

# 12-Airport Table Markdown Generator
def get_12_table_md():
    md = "### 2. 2026年 12 款精选机场参数横向对比表\n\n"
    md += "| 排名 | 机场名称 | 线路特色 | 参考价格 | 包含流量 | 专享优惠码 | 官网注册直达通道 |\n"
    md += "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for p in top12:
        coupon = f"`{p['coupon']}`" if p.get('coupon') else "暂无"
        md += f"| **No. {p['rank']}** | [{p['name']}](/providers/{p['slug']}/) | {p['suitableFor'][:22]} | **{p['priceFrom']}** | {p['trafficFrom']} | {coupon} | [👉 前往官网注册]({p['inviteURL']}) |\n"
    md += "\n> **💡 编辑部提醒**：所有第三方跳转链接均配置 `rel=\"sponsored nofollow noopener\"` 安全规范，最终价格与优惠规则请以结算页最新数据为准。\n\n"
    return md

# 12-Airport Detailed Sections Generator
def get_12_details_md():
    md = "## 3. 12 款精选机场详细测评与特点解读\n\n"
    md += "以下是本站编辑部对 12 款精选机场的详细介绍与适用场景拆解，帮您精准匹配最满意的魔法梯子：\n\n"
    for p in top12:
        coupon = f"`{p['coupon']}`" if p.get('coupon') else "暂无优惠码"
        md += f"### {p['rank']}. {p['name']}\n\n"
        md += f"- **服务定位与一句话结论**：{p['summary']}\n"
        md += f"- **起步价格与流量**：**{p['priceFrom']}**（包含流量：{p['trafficFrom']}）\n"
        md += f"- **专享优惠码**：{coupon}\n"
        md += f"- **核心适用场景**：{p['suitableFor']}\n"
        md += f"- **测评与注册通道**：[查看 {p['name']} 独立测评](/providers/{p['slug']}/) \| [👉 点击前往 {p['name']} 官网注册入口]({p['inviteURL']})\n\n"
        md += "---\n\n"
        if p['rank'] == 4:
            md += "<!--more-->\n\n"
    return md

# Picks 12 articles list
picks_articles = [
    ("2026好用的机场推荐：12款高速稳定科学上网梯子精选", "2026-good-airports-recommendation", ["机场推荐", "稳定梯子", "12款机场推荐", "科学上网"]),
    ("性价比机场推荐：平民小白月付与年付梯子对比指南", "value-airports-recommendation", ["性价比机场", "便宜梯子", "月付机场", "小白梯子"]),
    ("稳定机场推荐：晚高峰不卡顿的IEPL专线机场排行榜", "stable-airports-recommendation", ["稳定机场", "IEPL专线", "晚高峰不卡顿", "机场排行榜"]),
    ("便宜机场推荐：低至折合7元/月的极致性价比梯子测评", "cheap-airports-recommendation", ["便宜机场", "低价梯子", "折合7元", "平民机场"]),
    ("备用机场推荐：防止失联断网的第二梯子配置策略", "backup-airports-recommendation", ["备用机场", "防失联梯子", "双订阅策略", "应急梯子"]),
    ("大流量机场推荐：适合4K高清影音与海量下载的套餐选择", "large-traffic-airports", ["大流量机场", "4K影音梯子", "海量下载", "不限速机场"]),
    ("小流量年付机场推荐：轻度上网与学术科研最佳性价比方案", "small-traffic-yearly-airports", ["小流量机场", "年付梯子", "学术科研", "轻度上网"]),
    ("月付机场推荐：随用随充不踩坑的灵活梯子挑选技巧", "monthly-pay-airports", ["月付机场", "随用随充", "灵活套餐", "防跑路梯子"]),
    ("多设备共享机场推荐：支持5-10台电脑手机同时在线方案", "multi-device-sharing-airports", ["多设备机场", "家庭共享梯子", "多端同时在线", "设备不限制"]),
    ("远程办公机场推荐：跨境电商与Zoom外服会议稳定专线", "remote-work-airports", ["远程办公机场", "跨境电商梯子", "Zoom会议", "外贸网络加速"]),
    ("AI机场推荐：ChatGPT与Claude专用原生IP节点套餐选择", "ai-tools-airports", ["AI机场推荐", "ChatGPT梯子", "Claude节点", "原生IP机场"]),
    ("AI工具办公机场推荐：跨境协作、代码工具与多设备需求比较", "ai-office-collaboration-airports", ["AI办公机场", "GitHub Copilot梯子", "多设备协作", "低延迟节点"])
]

for title, slug, kw in picks_articles:
    summary = f"本文为广大小白用户详细评测了《{title}》的12款精选机场。涵盖灵动云、暮光网络、飞猫云、微风网络、隐形人、浪网、梯子云、飞V等12款优质梯子，提供完整参数对比表与官网直达通道。"
    path = f"content/picks/{slug}.md"
    content = f"""---
title: "{title}"
date: 2026-09-29
lastmod: 2026-09-29
draft: false
categories: ["优质机场推荐"]
tags: {json.dumps(kw, ensure_ascii=False)}
keywords: "{','.join(kw)}"
description: "{summary}"
summary: "{summary}"
toc: true
---

# {title}

**【导读摘要】**：{summary}

针对新手小白最关心的 **{kw[0]}** 议题，编辑部整理了 2026 最新物理专线压测数据，严选了以下 **12 款高速稳定机场**。无论是追求极致 0 丢包游戏低延迟，还是寻找平民低至 7 元/月的性价比年付套餐，本指南均为您提供详尽的实战挑选与配置建议。

## 1. 2026年{kw[0]}行业现状与 12 款机场选型标准

挑选一款高品质的梯子机场，首先需要理清以下几个关键维度：

1. **物理线路质量**：是否包含 IPLC/IEPL 内网专线或 BGP 多线中继。例如 [灵动云](/providers/lingdong-cloud/) 和 [暮光网络](/providers/twilight-cloud/) 均搭载全专线传输，保障晚高峰连线流畅。
2. **协议兼容性**：是否同时覆盖 Shadowsocks (SS)、Trojan、V2Ray/VMess 与新一代 Hysteria2 (歇斯底里)。
3. **性价比与计费模式**：是否提供平民年付（如 [飞猫云](/providers/flycat-cloud/) 折合 7 元/月方案）或灵活月付（如 [微风网络](/providers/breezenet/) 12 元/月方案）。

{get_12_table_md()}

{get_12_details_md()}

## 4. 保姆级新手实操设置步骤（1-2-3）

### 步骤 1：挑选并注册合适的机场
点击上述列表中的“前往官网注册”链接，完成账号注册并选择符合您预算的套餐。

### 步骤 2：获取订阅链接并导入客户端
在机场用户后台复制一键订阅地址，打开适配您设备的客户端（Windows/Mac 推荐 [Clash Verge](/clients/clash-verge-guide/)，iOS 推荐 [小火箭 Shadowrocket](/clients/shadowrocket-ios-tutorial/)），完成订阅导入。

### 步骤 3：选择节点并开启系统代理
刷新同步节点列表，勾选低延迟节点并开启系统代理，即可顺畅科学上网。

## 5. 常见误区与使用防坑建议

- 避免购买没有明确运营历史的廉价“终身套餐”。
- 遇到节点超时排查：检查本地电脑时间是否与标准北京时间一致。
- 观看 Netflix / 使用 ChatGPT 时，请选择标注“解锁AI/奈飞”的专用原生节点。

## 6. 延伸阅读与相关推荐
- 📖 [小白入门教程](/tutorials/)：零基础魔法上网设置图文指南
- 🛠️ [客户端下载配置](/clients/)：Clash / v2rayN / 小火箭完整保姆级教程
- ⚡ [专线与游戏加速](/iplc-gaming/)：IEPL低延迟外服加速节点解析
- 🎬 [流媒体与AI工具](/streaming/)：Netflix 4K与ChatGPT高效解锁
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated all 12 full airport recommendations in picks successfully!")
