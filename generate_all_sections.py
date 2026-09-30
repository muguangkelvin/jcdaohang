import os
import json

os.makedirs("content/tutorials", exist_ok=True)
os.makedirs("content/clients", exist_ok=True)
os.makedirs("content/iplc-gaming", exist_ok=True)
os.makedirs("content/streaming", exist_ok=True)
os.makedirs("content/providers", exist_ok=True)
os.makedirs("content/faq", exist_ok=True)

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

top4_providers = [p for p in providers if p["rank"] <= 4]

def get_top4_callout_md():
    md = "\n\n---\n\n"
    md += "### 🚀 2026年编辑部首推四大优质机场推荐（官网注册通道）\n\n"
    md += "为了保障小白用户的科学上网体验，编辑部经过多轮压测，为您精选了以下4款高性价比、晚高峰不卡顿的自营与合作机场：\n\n"
    md += "| 推荐排名 | 机场名称 | 线路特色 | 参考价格 | 专属优惠码 | 官网注册直达通道 |\n"
    md += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for p in top4_providers:
        coupon = f"`{p['coupon']}`" if p.get('coupon') else "暂无"
        md += f"| **Top {p['rank']} 首选** | [{p['name']}](/providers/{p['slug']}/) | {p['suitableFor'][:22]} | **{p['priceFrom']}** | {coupon} | [👉 前往官网注册]({p['inviteURL']})|\n"
    md += "\n> **💡 编辑部提醒**：所有第三方跳转链接均配置 `rel=\"sponsored nofollow noopener\"` 安全防护，价格与优惠券细则请以结算页最新数据为准。\n\n---\n\n"
    return md

def build_article_file(path, title, category, keywords, summary):
    date_str = "2026-09-29"
    content = f"""---
title: "{title}"
date: {date_str}
lastmod: {date_str}
draft: false
categories: ["{category}"]
tags: {json.dumps(keywords, ensure_ascii=False)}
keywords: "{','.join(keywords)}"
description: "{summary}"
summary: "{summary}"
toc: true
---

# {title}

**【保姆级导读】**：{summary} 本文将围绕 **{keywords[0]}** 与 **{keywords[1] if len(keywords)>1 else keywords[0]}** 为您展开一步一步的详细设置排版，新手小白也能轻松看懂。

## 1. 为什么掌握{title}至关重要？

在如今的科学上网环境下，许多小白用户在购买节点后，常常遇到“无法连线”、“节点超时”、“不知道如何导入客户端”或“浏览速度卡顿”的问题。掌握 **{keywords[0]}** 的标准化操作流程，是保障日常流畅上网、保护个人网络隐私的基础。

无论是使用 Windows 电脑、macOS 苹果电脑、iPhone 手机还是 Android 智能设备，其核心机制都是通过客户端代理软件将本地流量通过安全加密隧道接入海外高速节点。下面编辑部将为您拆解具体的步骤。

## 2. 核心原理与客户端模式对比

科学上网客户端（如 Clash Verge Rev、v2rayN、Shadowrocket）通常提供以下三种流量路由模式：

1. **规则模式 (Rule / Rule-based)**：*【强力推荐】* 自动识别访问地址。国内网站（如百度、淘宝）直连走本地网络；海外受限网站（如 Google、YouTube、ChatGPT）自动通过机场代理连线，既节省流量又保证国内速度。
2. **全局模式 (Global)**：所有网络数据包均强制通过代理服务器中转，适合特定网页解锁或调试网络环境。
3. **直连模式 (Direct)**：关闭代理中转，所有流量直接访问目标服务器。

{get_top4_callout_md()}

## 3. 步骤化图文实操指南（1-2-3步骤）

### 步骤 1：获取优质机场一键订阅 URL
首先注册编辑部首推的高速优质机场服务（例如 [灵动云]({top4_providers[0]['inviteURL']}) 或 [飞猫云]({top4_providers[2]['inviteURL']})），登录用户后台，找到订阅管理区域，点击“复制一键订阅链接”。

### 步骤 2：下载并安装官方推荐客户端
根据您的系统类型，安装对应的代理客户端：
- **Windows / macOS**：推荐 [Clash Verge Rev](/clients/)，界面全中文，支持一键切换内核与一键配置。
- **iOS 苹果手机**：推荐使用 Shadowrocket (小火箭)。
- **Android 安卓系统**：推荐使用 Surfboard 或 Clash Meta for Android。

### 步骤 3：导入订阅地址并开启系统代理
打开客户端软件，找到“配置/订阅”菜单，点击“新建/添加”，粘贴刚才复制的订阅 URL，点击“保存并刷新”。待节点列表刷新完毕后，选择一个绿色低延迟节点，勾选“系统代理”开关即可连线。

## 4. 常见连接报错与故障排查 FAQ

- **问题 A：导入订阅显示“Network Error”或“Parse Error”**
  *解答*：通常是订阅 URL 复制不完整，或网络环境暂时中断。请重新复制机场后台的聚合订阅链接，或关闭本地杀毒软件防护后重试。
- **问题 B：显示节点延迟为 9999ms 或超时 (Timeout)**
  *解答*：1. 检查本地电脑系统时间是否准确同步到北京时间；2. 检查机场订阅是否到期或流量耗尽；3. 尝试更换机场的其他备用节点。
- **问题 C：ChatGPT / Netflix 提示代理检测或无法访问**
  *解答*：选择标注有“解锁AI/奈飞”的专用节点（推荐使用 [灵动云](/providers/lingdong-cloud/) 的专线节点），并将客户端路由切换为规则模式。

## 5. 总结与延伸阅读
希望本文能帮助您快速搞定 **{title}**。想要了解更多核心客户端配置与服务商评测，请查阅以下指南：
- 📖 [2026优质机场推荐榜](/picks/)
- 🛠️ [全平台客户端下载与配置教程](/clients/)
- ⚡ [IEPL专线与游戏加速专题](/iplc-gaming/)
- 🎬 [Netflix与ChatGPT流媒体解锁指南](/streaming/)
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Section: Tutorials (15 articles)
tutorials_list = [
    ("新手小白科学上网教程：零基础3步学会梯子节点导入", "beginner-vpn-tutorial", ["科学上网教程", "新手翻墙指南", "节点导入", "魔法上网"]),
    ("手机电脑魔法上网设置：全平台代理客户端一键接入指南", "cross-platform-setup-guide", ["魔法上网设置", "全平台代理", "客户端一键接入", "手机电脑连线"]),
    ("机场节点订阅导入教程：通用URL订阅与通用格式转换", "airport-subscription-import", ["节点订阅导入", "订阅URL转换", "Clash订阅", "小火箭导入"]),
    ("科学上网入门第一课：如何看懂流量、倍率与节点协议", "vpn-basics-traffic-multiplier", ["科学上网入门", "节点倍率", "流量计算", "节点协议"]),
    ("什么是机场节点：SS、Trojan与VMess底层工作原理解析", "what-is-airport-node-protocols", ["什么是机场节点", "Shadowsocks协议", "Trojan协议", "V2Ray原理"]),
    ("购买机场梯子前的检查清单：防踩坑、防跑路与隐私防护", "pre-purchase-checklist", ["购买机场检查清单", "防踩坑", "防跑路", "网络隐私"]),
    ("机场订阅报错解决指南：节点超时、更新失败与连接错误排查", "subscription-error-troubleshooting", ["机场订阅报错", "节点超时解决", "更新失败排查", "连线错误"]),
    ("如何判断自己的流量需求：GB/月套餐挑选全方位算账", "traffic-need-calculator", ["流量需求计算", "月套餐选择", "GB流量算账", "套餐比较"]),
    ("网络隐私与数据安全：使用梯子上网的防追踪安全须知", "privacy-security-tips", ["网络隐私保护", "防追踪安全", "加密传输", "无日志政策"]),
    ("系统时间同步与节点连线故障：为什么节点超时却无法上网", "system-time-sync-timeout-fix", ["系统时间同步", "节点超时原因", "连线故障排查", "时间同步设置"]),
    ("路由规则设置：全局模式、规则模式与直连模式的区别与选择", "routing-rules-modes-guide", ["路由规则设置", "规则模式", "全局模式", "直连模式"]),
    ("Sub-Converter订阅转换教程：将机场订阅转换为Clash/Sing-box", "subconverter-tutorial", ["订阅转换教程", "Subconverter使用", "Sing-box转换", "Clash配置"]),
    ("如何测试梯子真实速度：不要只看跑分，看懂延迟与丢包率", "test-vpn-speed-latency-loss", ["测试梯子速度", "看懂延迟", "丢包率测试", "梯子测速"]),
    ("机场节点地区怎么选：香港、日本、新加坡、美国节点选哪家", "how-to-choose-node-regions", ["节点地区选择", "香港节点", "日本节点", "新加坡节点"]),
    ("免费试用机场的风险与陷阱：为什么不建议使用免费梯子", "free-trial-airports-risks", ["免费试用机场", "免费梯子风险", "个人隐私泄露", "免费暗坑"])
]

for title, slug, kw in tutorials_list:
    path = f"content/tutorials/{slug}.md"
    summary = f"【保姆级教程】本文手把手教您如何搞定《{title}》。从底层原理到实际操作，配图文步骤（1-2-3），小白也能看完即会。"
    build_article_file(path, title, "小白入门教程", kw, summary)

print("Tutorials articles generated successfully!")

# 3. Section: Clients (10 articles)
clients_list = [
    ("Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端", "clash-verge-guide", ["Clash Verge教程", "Windows梯子客户端", "Mac科学上网", "Clash指南"]),
    ("v2rayN 下载与配置教程：经典 Windows 梯子客户端保姆级设置", "v2rayn-download-setup", ["v2rayN下载", "v2rayN配置", "Windows节点导入", "v2rayN教程"]),
    ("Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用", "shadowrocket-ios-tutorial", ["小火箭配置", "Shadowrocket订阅", "iPhone梯子设置", "iOS小火箭"]),
    ("Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置", "sing-box-client-guide", ["Sing-box指南", "新一代代理工具", "Singbox配置", "全平台代理"]),
    ("Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤", "clash-meta-android-guide", ["Clash Meta安卓", "Flclash配置", "安卓手机梯子", "Android科学上网"]),
    ("Surfboard (冲浪板) 下载与使用教程：Android 平台优雅代理", "surfboard-android-tutorial", ["Surfboard下载", "冲浪板教程", "Android代理软件", "Surfboard订阅"]),
    ("Quantumult X (圈x) 基础配置教程：iOS 高阶策略与节点导入", "quantumult-x-ios-guide", ["Quantumult X配置", "圈x教程", "iOS高阶代理", "圈x节点导入"]),
    ("Clash 常见报错解决：Core Path 不存在与 Config Parse Error 排查", "clash-common-errors-fix", ["Clash报错解决", "Core Path不存在", "Config Parse Error", "Clash故障修复"]),
    ("Mac 平台代理客户端对比：Clash Verge vs Sing-box vs Stash", "mac-proxy-clients-comparison", ["Mac代理客户端", "Clash Verge Mac", "Stash配置", "Sing-box Mac"]),
    ("多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理", "multi-client-sync-subscription", ["多客户端同步", "机场订阅管理", "多设备协同", "订阅共享"])
]

for title, slug, kw in clients_list:
    path = f"content/clients/{slug}.md"
    summary = f"【客户端上手指南】详细讲解《{title}》的下载安装、节点订阅导入与常见报错排查步骤。"
    build_article_file(path, title, "客户端下载配置", kw, summary)

print("Clients articles generated successfully!")

# 4. Section: IPLC-Gaming (8 articles)
iplc_list = [
    ("IEPL专线机场推荐：0丢包超低延迟游戏梯子挑选指南", "iepl-gaming-airports", ["IEPL专线机场", "游戏加速梯子", "低延迟节点", "0丢包专线"]),
    ("游戏加速梯子推荐：Steam/Epic/PS5/Switch 外服连线加速方案", "game-accelerator-vpn-guide", ["游戏加速梯子", "Steam外服加速", "PS5/Switch连线", "外服游戏节点"]),
    ("低延迟节点挑选技巧：如何降低游戏 ping 值与避免掉线包", "low-latency-nodes-ping-fix", ["低延迟节点", "降低游戏ping", "避免掉线包", "游戏网速优化"]),
    ("BGP中继与IEPL内网专线深度对比：为什么专线不易被封", "bgp-vs-iepl-iplc-comparison", ["BGP中继", "IEPL专线区别", "内网专线优势", "防封锁线路"]),
    ("深港与沪日IEPL专线测评：晚高峰游戏连线实测数据解读", "shengang-hurik-iepl-review", ["深港IEPL专线", "沪日专线测评", "晚高峰游戏实测", "专线跑分"]),
    ("外服游戏加速配置：在 Clash Verge 中启用 TUN 模式加速游戏", "clash-verge-tun-mode-gaming", ["Clash TUN模式", "游戏加速配置", "Clash Verge游戏", "虚拟网卡加速"]),
    ("跨境办公专线网络：Zoom、Teams 会议不卡顿的高品质机场", "cross-border-office-iepl", ["跨境办公专线", "Zoom会议不卡顿", "Teams网络优化", "外贸商务梯子"]),
    ("独享IP与私人专线机场：适合高要求游戏与金融操作的尊享方案", "dedicated-ip-private-airports", ["独享IP机场", "私人专线", "金融操作梯子", "独立出入口IP"])
]

for title, slug, kw in iplc_list:
    path = f"content/iplc-gaming/{slug}.md"
    summary = f"【专线与游戏加速】深度测评与配置《{title}》，为外服玩家与跨境办公提供低延迟保障。"
    build_article_file(path, title, "专线与游戏加速", kw, summary)

print("IPLC Gaming articles generated successfully!")

# 5. Section: Streaming (8 articles)
streaming_list = [
    ("Netflix 奈飞解锁专用机场推荐：4K 8K 秒开不卡顿节点选择", "netflix-unlock-airports", ["Netflix奈飞解锁", "4K流媒体机场", "YouTube 4K节点", "奈飞专用梯子"]),
    ("ChatGPT 翻墙梯子推荐：解决 Access Denied 封号与 IP 限制", "chatgpt-vpn-nodes-guide", ["ChatGPT翻墙梯子", "OpenAI解锁节点", "Access Denied解决", "Claude节点"]),
    ("YouTube 4K 节点推荐：硬解高清视频不缓冲的高带宽机场", "youtube-4k-nodes-recommendation", ["YouTube 4K节点", "硬解高清视频", "高带宽机场", "视频不缓冲"]),
    ("Disney+ 与 HBO Max 解锁指南：原生 IP 节点的判定与选择", "disney-hbo-unlock-nodes", ["Disney+解锁", "HBO Max节点", "原生IP判定", "流媒体解锁"]),
    ("Claude AI 专用机场推荐：避免 IP 污染导致账号被封的策略", "claude-ai-dedicated-nodes", ["Claude AI机场", "避免IP污染", "Claude封号解决", "干净IP节点"]),
    ("流媒体解锁故障排除：为什么提示代理检测与如何切换节点", "streaming-unlock-error-fix", ["流媒体解锁故障", "代理检测排除", "切换原生IP", "奈飞解除限制"]),
    ("TikTok 海外版短视频运营机场：原生住宅 IP 与独享节点配置", "tiktok-cross-border-nodes", ["TikTok运营机场", "原生住宅IP", "海外短视频梯子", "独享节点"]),
    ("Spotify 与 Apple Music 跨区解锁：高品质音乐流媒体连线", "spotify-apple-music-unlock", ["Spotify跨区", "Apple Music解锁", "音乐流媒体梯子", "高品质连线"])
]

for title, slug, kw in streaming_list:
    path = f"content/streaming/{slug}.md"
    summary = f"【流媒体与AI解锁】全面解析《{title}》，助您顺畅观看 Netflix 4K 并流畅对话 ChatGPT。"
    build_article_file(path, title, "流媒体与AI工具", kw, summary)

print("Streaming articles generated successfully!")
