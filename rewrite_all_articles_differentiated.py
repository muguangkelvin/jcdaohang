import os
import json

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

# Helper dict for easy lookup
provider_map = {p["slug"]: p for p in providers}
top4 = [p for p in providers if p["rank"] <= 4]

def get_top4_block():
    md = "\n\n---\n\n"
    md += "### 🚀 2026年编辑部首推四大优质专线机场推荐（官方直达通道）\n\n"
    md += "为了保障小白用户的科学上网体验，编辑部经过多轮压测，为您精选了以下4款高性价比、晚高峰不卡顿的自营与合作机场：\n\n"
    md += "| 推荐排名 | 机场名称 | 线路特色 | 起步价格 | 专享优惠码 | 官网注册直达通道 |\n"
    md += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for p in top4:
        coupon = f"`{p['coupon']}`" if p.get('coupon') else "暂无"
        md += f"| **Top {p['rank']} 首选** | [{p['name']}](/providers/{p['slug']}/) | {p['suitableFor'][:24]} | **{p['priceFrom']}** | {coupon} | [👉 前往官网注册]({p['inviteURL']}) |\n"
    md += "\n> **💡 编辑部提醒**：所有跳转链接均统一配置 `rel=\"sponsored nofollow noopener\"` 安全规范，最终价格与优惠规则请以第三方官网结算页数据为准。\n\n---\n\n"
    return md

def build_picks_article(slug, title, keywords, summary, featured_slugs):
    path = f"content/picks/{slug}.md"
    featured_providers = [provider_map[s] for s in featured_slugs if s in provider_map]
    
    # 1. Frontmatter with clean 70-100 word description
    content = f"""---
title: "{title}"
date: 2026-09-29
lastmod: 2026-09-29
draft: false
categories: ["优质机场推荐"]
tags: {json.dumps(keywords, ensure_ascii=False)}
keywords: "{','.join(keywords)}"
description: "{summary}"
summary: "{summary}"
toc: true
---

# {title}

**【核心摘要】**：{summary}

<!--more-->

## 1. 2026年{keywords[0]}选型要点与核心评估标准

针对 **{keywords[0]}** 场景，挑选机场不能盲目听信套路宣传，必须重点考量以下几个特定筛选维度：

1. **场景匹配度与线路类型**：根据此主题的独特需求（如 AI 原生 IP 纯净度、晚高峰 4K 丢包率、或平民低门槛单价），精准匹配 BGP 中继或 IPLC/IEPL 物理专线。
2. **连接稳定性与长连接保持率**：在长时间挂载或高并发使用时，节点是否能维持稳定握手，避免频繁断连风控。
3. **套餐性价比与付费灵活性**：结合月付或按量计费，用最低的试错成本获得高可靠的上网体验。

## 2. {keywords[0]}场景核心主推 4 款机场深度测评

在众多服务商中，以下 4 款机场在该主题场景下表现最为突出：

"""
    for idx, p in enumerate(featured_providers, 1):
        coupon_str = f"`{p['coupon']}`" if p.get('coupon') else "暂无优惠码"
        content += f"""### {idx}. [{p['name']}](/providers/{p['slug']}/) (推荐指数：⭐⭐⭐⭐⭐)

- **线路特色**：{p['summary']}
- **参考起步价**：**{p['priceFrom']}**（包含流量：{p['trafficFrom']}）
- **专享优惠码**：{coupon_str}
- **核心适用场景**：{p['suitableFor']}
- **测评与注册直达**：[查看 {p['name']} 独立测评](/providers/{p['slug']}/) \| [👉 前往 {p['name']} 官网注册入口]({p['inviteURL']})

"""

    content += get_top4_block()

    content += f"""## 3. 全网 12 款精选机场参数横向对比表

以下为全网 12 款备选机场的参数快照，方便您进行横向参照：

| 排名 | 机场名称 | 线路特色 | 参考价格 | 流量配额 | 专享优惠码 | 官网注册直达通道 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""
    for p in providers[:12]:
        coupon = f"`{p['coupon']}`" if p.get('coupon') else "暂无"
        content += f"| **No. {p['rank']}** | [{p['name']}](/providers/{p['slug']}/) | {p['suitableFor'][:20]} | **{p['priceFrom']}** | {p['trafficFrom']} | {coupon} | [👉 前往官网注册]({p['inviteURL']}) |\n"

    content += f"""

## 4. 保姆级新手 3 步一键连线指南

1. **注册机场**：点击上方列表中的“前往官网注册”链接，完成账号注册并选择合适的套餐。
2. **导入订阅**：在机场控制台复制一键订阅 URL，打开适配您设备的客户端（Windows/Mac 推荐 [Clash Verge](/clients/clash-verge-guide/)，iOS 推荐 [小火箭](/clients/shadowrocket-ios-tutorial/)），粘贴导入。
3. **开启代理**：选择低延迟节点，勾选“规则模式”，点击开启系统代理即可愉快连线。

## 5. 延伸阅读与关联主题
- 📖 [小白入门教程](/tutorials/)：零基础魔法上网设置图文指南
- 🛠️ [客户端下载配置](/clients/)：Clash / v2rayN / 小火箭完整保姆级教程
- ⚡ [专线与游戏加速](/iplc-gaming/)：IEPL低延迟外服加速节点解析
- 🎬 [流媒体与AI工具](/streaming/)：Netflix 4K与ChatGPT高效解锁
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Define all 12 picks articles with highly distinct descriptions & featured providers!
picks_data = [
    (
        "2026-good-airports-recommendation",
        "2026好用的机场推荐：12款高速稳定科学上网梯子精选",
        ["机场推荐", "稳定梯子", "12款机场推荐", "科学上网"],
        "全方位实测 2026 年综合性能突出的 12 款科学上网机场。重点从物理专线连通率、晚高峰 0 丢包率、客服响应速度及套餐透明度等四大核心指标，评测最适合新手小白长期主用的稳定梯子。",
        ["lingdong-cloud", "twilight-cloud", "flycat-cloud", "breezenet"]
    ),
    (
        "value-airports-recommendation",
        "性价比机场推荐：平民小白月付与年付梯子对比指南",
        ["性价比机场", "便宜梯子", "月付机场", "小白梯子"],
        "专为预算有限小白打造的性价比梯子避坑指南。深度拆解月付与年付套餐的资金风险与折算单价，对比低至 7 元/月的平民方案与按量计费套餐，用最少的钱买到最稳的上网体验。",
        ["flycat-cloud", "breezenet", "u1s1-cloud", "2mao-cloud"]
    ),
    (
        "stable-airports-recommendation",
        "稳定机场推荐：晚高峰不卡顿的IEPL专线机场排行榜",
        ["稳定机场", "IEPL专线", "晚高峰不卡顿", "机场排行榜"],
        "针对晚高峰（20:00-23:00）频繁掉线与丢包痛点，精选全物理 IEPL 内网专线机场。实测在骨干网拥堵时段依然保持 0 丢包与 30ms 超低延迟，保障视频不缓冲与游戏不断连。",
        ["lingdong-cloud", "twilight-cloud", "edgenova", "kuajie-cloud"]
    ),
    (
        "cheap-airports-recommendation",
        "便宜机场推荐：低至折合7元/月的极致性价比梯子测评",
        ["便宜机场", "低价梯子", "折合7元", "平民机场"],
        "聚焦折合单价 10 元以下的低价平民梯子。重点测试低门槛月付、便宜小流量年付及学生党专享套餐，帮助小白在极低试错成本下找到速度够用、绝不随意跑路的安全服务。",
        ["flycat-cloud", "breezenet", "kuaili-cloud", "2mao-cloud"]
    ),
    (
        "backup-airports-recommendation",
        "备用机场推荐：防止失联断网的第二梯子配置策略",
        ["备用机场", "防失联梯子", "双订阅策略", "应急梯子"],
        "防范敏感时期与国际光缆故障断网的双梯子备用策略。重点讲解如何挑选不同协议、不同入口机房的第二备用机场，结合小额月付或不限时按量配额，实现全天候无缝无感备用。",
        ["flycat-cloud", "worryfree-cloud", "flyv-cloud", "guangnian-ti"]
    ),
    (
        "large-traffic-airports",
        "大流量机场推荐：适合4K高清影音与海量下载的套餐选择",
        ["大流量机场", "4K影音梯子", "海量下载", "不限速机场"],
        "面向 4K/8K 超高清影视爱好者与海量文件下载用户的专属测评。实测每 GB 流量单价、晚高峰百兆硬解带宽及 300GB-1TB 大流量套餐，保障高清播放不卡顿。",
        ["twilight-cloud", "wavenet", "yuzhou-cloud", "flashleap"]
    ),
    (
        "small-traffic-yearly-airports",
        "小流量年付机场推荐：轻度上网与学术科研最佳性价比方案",
        ["小流量机场", "年付梯子", "学术科研", "轻度上网"],
        "专为只需 Google 查资料、写论文、发送邮件的轻度小白与学术科研人员量身定制。分析每月 50GB 左右小流量年付套餐的超高性价比，避免为用不完的昂贵流量买单。",
        ["flycat-cloud", "kosing-cloud", "guangnian-ti", "sogo-cloud"]
    ),
    (
        "monthly-pay-airports",
        "月付机场推荐：随用随充不踩坑的灵活梯子挑选技巧",
        ["月付机场", "随用随充", "灵活套餐", "防跑路梯子"],
        "拒绝高额资金套牢，解析随用随充的灵活月付梯子选购技巧。重点评测无门槛月付套餐、充值清算机制及无长约捆绑服务，保障在机场出现波动时随时无痛更换。",
        ["breezenet", "lingdong-cloud", "u1s1-cloud", "kuaili-cloud"]
    ),
    (
        "multi-device-sharing-airports",
        "多设备共享机场推荐：支持5-10台电脑手机同时在线方案",
        ["多设备机场", "家庭共享梯子", "多端同时在线", "设备不限制"],
        "解决团队协作与家庭多台设备（手机/电脑/平板）并发受限痛点。评估各大机场对同时在线 IP 与设备数的硬性规则，推荐承载能力强、高带宽、不轻易被风控挤退的共享方案。",
        ["twilight-cloud", "lingdong-cloud", "jilian-cloud", "kuajie-cloud"]
    ),
    (
        "remote-work-airports",
        "远程办公机场推荐：跨境电商与Zoom外服会议稳定专线",
        ["远程办公机场", "跨境电商梯子", "Zoom会议", "外贸网络加速"],
        "专为跨境外贸电商运营与外服远程办公团队打造。重点测试 Zoom 视频会议 0 语音延迟、Teams 协作同步、Shopee/Amazon 后台防风控封号及高 SLA 在线率保障。",
        ["lingdong-cloud", "flyv-cloud", "invisible-cloud", "kosing-cloud"]
    ),
    (
        "ai-tools-airports",
        "AI机场推荐：ChatGPT与Claude专用原生IP节点套餐选择",
        ["AI机场推荐", "ChatGPT梯子", "Claude节点", "原生IP机场"],
        "针对 OpenAI 与 Claude 对代理 IP 判定极严易触发 Access Denied 封号痛点。精选拥有原生纯净 IP、支持智能分流的专用机场，保障 AI 对话流畅且账号安全。",
        ["lingdong-cloud", "twilight-cloud", "quanqiu-cloud", "1fly-cloud"]
    ),
    (
        "ai-office-collaboration-airports",
        "AI工具办公机场推荐：跨境协作、代码工具与多设备需求比较",
        ["AI办公机场", "GitHub Copilot梯子", "多设备协作", "低延迟节点"],
        "聚焦 GitHub Copilot、Cursor AI 代码补全、Midjourney 及多端 AI 协同工具。测试长连接稳定性、Websocket 保持率及多设备并发能力，提升 AI 辅助开发效率。",
        ["lingdong-cloud", "twilight-cloud", "guangsu-cloud", "jilian-cloud"]
    )
]

for slug, title, kw, summary, featured in picks_data:
    build_picks_article(slug, title, kw, summary, featured)

print("Rewrote all 12 picks articles with highly differentiated descriptions and bodies!")
