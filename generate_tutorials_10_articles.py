import os
import json

os.makedirs("content/tutorials", exist_ok=True)

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

top4 = [p for p in providers if p["rank"] <= 4]

def get_top4_block():
    md = "\n\n---\n\n"
    md += "### 🚀 2026年编辑部首推四大优质机场推荐（新手连线首选）\n\n"
    md += "为了保障小白用户的科学上网体验，编辑部经过多轮压测，为您精选了以下4款高性价比、晚高峰不卡顿的自营与合作机场：\n\n"
    md += "| 推荐排名 | 机场名称 | 线路特色 | 起步价格 | 专享优惠码 | 官网注册直达通道 |\n"
    md += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for p in top4:
        coupon = f"`{p['coupon']}`" if p.get('coupon') else "暂无"
        md += f"| **Top {p['rank']} 首选** | [{p['name']}](/providers/{p['slug']}/) | {p['suitableFor'][:24]} | **{p['priceFrom']}** | {coupon} | [👉 前往官网注册]({p['inviteURL']}) |\n"
    md += "\n> **💡 编辑部提醒**：所有跳转链接均统一配置 `rel=\"sponsored nofollow noopener\"` 安全规范，最终价格与优惠规则请以第三方官网结算页数据为准。\n\n---\n\n"
    return md

def write_article(filename, title, category, tags, keywords, summary, body_md):
    content = f"""---
title: "{title}"
date: 2026-09-29
lastmod: 2026-09-29
draft: false
categories: ["{category}"]
tags: {json.dumps(tags, ensure_ascii=False)}
keywords: "{keywords}"
description: "{summary}"
summary: "{summary}"
toc: true
---

# {title}

**【保姆级导读】**：{summary}

{body_md}
"""
    with open(f"content/tutorials/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

# 1. Subconverter Tutorial
t1_body = f"""## 1. 为什么需要使用 Sub-Converter 订阅转换？

许多小白用户在购买机场订阅后，经常遇到客户端无法导入或节点列表显示为空的问题。例如：机场只提供了 V2Ray 格式订阅，而您想在 Clash Verge 中使用；或者机场提供了 Base64 明文链接，而 Sing-box 客户端需要标准的 JSON 配置文件。

**Sub-Converter (订阅转换器)** 是开源社区最强大的节点订阅转换工具。它能够将任何类型的机场原始节点链接，一键智能解析并转换为适配 Clash、Sing-box、Quantumult X、Surge 或 Shadowrocket 的标准配置文件。

## 2. 保姆级使用教程：3步完成机场订阅转换

### 步骤 1：获取机场原始订阅链接
登录您的机场后台（如 [灵动云](/providers/lingdong-cloud/) 或 [飞猫云](/providers/flycat-cloud/)），复制控制台给出的订阅链接。

### 步骤 2：在 Sub-Converter 转换页面中配置参数
1. 打开公认安全的线上订阅转换前端（或本地自建的 Sub-converter 页面）。
2. 在 **“订阅链接” (Subscribe URL)** 输入框中粘贴您的机场原始链接。
3. 在 **“客户端生成” (Target Client)** 下拉菜单中，选择您目标使用的软件（如 **Clash** 或 **Sing-box**）。
4. 在 **“后端地址”** 中，建议选择官方推荐或自建的加密后端，防止隐私泄漏。

### 步骤 3：生成并复制专属转换 URL
点击 **“生成订阅链接”** 按钮，复制生成的专属转换 URL 链接。在 Clash Verge 或小火箭中粘贴该转换链接进行导入，即可获得完整的规则分组与节点列表。

{get_top4_block()}

## 3. 订阅转换过程中的安全防坑须知

- **防范公共第三方后端泄漏订阅**：不建议使用未知的个人搭设的转换后端转换高额机场订阅，防止被恶意获取流量配额。
- **自建 Sub-Converter 后端**：高级极客可以通过 Docker 镜像（`tindy2013/subconverter`）一键在本地部署属于自己的私有转换服务。
- **自定义规则节点引入**：可在转换选项中勾选引入“ACL4SSR 规则集”，实现更精细化的国内直连与海外分流。

## 4. 延伸阅读与相关教程
- 📖 [新手小白科学上网教程：零基础3步学会梯子节点导入](/tutorials/beginner-vpn-tutorial/)
- 🛠️ [机场节点订阅导入教程：通用URL订阅与通用格式转换](/tutorials/airport-subscription-import/)
- 💻 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 🔄 [多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理](/clients/multi-client-sync-subscription/)
"""
write_article("subconverter-tutorial.md", "Sub-Converter订阅转换教程：将机场订阅转换为Clash/Sing-box", "小白入门教程", ["订阅转换教程", "Subconverter使用", "Sing-box转换", "Clash配置", "机场订阅转换"], "订阅转换教程,Subconverter使用,Sing-box转换,Clash配置,机场订阅转换", "保姆级图文教程：手把手教您使用 Sub-Converter 订阅转换工具，将机场原始链接一键转换为 Clash YAML 或 Sing-box JSON 格式。", t1_body)

# 2. What is Airport Node Protocols
t2_body = f"""## 1. 什么是机场节点？它与传统 VPN 有什么区别？

许多刚接触科学上网的新手小白常问：“机场节点到底是什么？”

简而言之，**机场节点** 是由专业服务商在全球数据中心部署的高带宽中转服务器。与传统通用的 VPN（如 ExpressVPN、NordVPN 容易被批量封锁 IP）不同，机场节点采用了专门针对网络防火墙特征而优化的加密代理协议，具备更强的连通性与更高的传输速度。

## 2. Shadowsocks、Trojan 与 VMess/VLESS 协议深度拆解

目前主流机场节点包含以下四大核心加密协议：

### (1) Shadowsocks (SS 协议)
- **特点**：最经典的轻量级代理协议。采用 AES-256-GCM 或最新的 2022 强加密标准。
- **优势**：加解密计算开销极低，传输速度极快。搭配 IEPL 专线使用时（如 [灵动云](/providers/lingdong-cloud/)），体验体验最佳。

### (2) Trojan 协议 (特洛伊木马)
- **特点**：将代理流量完全伪装成最常见的互联网 HTTPS 网页加密流量。
- **优势**：过墙防封锁能力极强，GFW 防火墙难以将 Trojan 数据包与正常的网银/电商交易流量区分开来。

### (3) V2Ray (VMess / VLESS 协议)
- **特点**：由 V2Ray 社区发明的多路复用代理协议。配合 WebSocket + TLS 技术，可将流量隐藏在真实域名网站后面。
- **优势**：抗封锁能力优异，节点生命周期极长。

### (4) Hysteria2 (歇斯底里2 协议)
- **特点**：基于 QUIC / UDP 协议打造的新一代高速传输协议。
- **优势**：专为弱网与高丢包环境设计，即使在网络抖动时也能暴拉带宽，完美适配 Sing-box 与新版 Clash。

{get_top4_block()}

## 3. 小白如何根据需求挑选协议与节点？

- **追求游戏极速低延迟**：选择搭载全 IEPL 专线的 **Shadowsocks** 或 **Trojan** 节点（首推 [灵动云](/providers/lingdong-cloud/)）。
- **移动网络或弱网看 4K 视频**：选择 **Hysteria2** 节点（首推 [暮光网络](/providers/twilight-cloud/)）。
- **日常网页浏览与学术科研**：选择标准的 **VMess / Trojan** 节点（首推 [微风网络](/providers/breezenet/)）。

## 4. 延伸阅读与相关文章
- 📖 [新手小白科学上网教程：零基础3步学会梯子节点导入](/tutorials/beginner-vpn-tutorial/)
- 🌐 [机场节点地区怎么选：香港、日本、新加坡、美国节点选哪家](/tutorials/how-to-choose-node-regions/)
- ⚡ [BGP中继与IEPL内网专线深度对比：为什么专线不易被封](/iplc-gaming/bgp-vs-iepl-iplc-comparison/)
"""
write_article("what-is-airport-node-protocols.md", "什么是机场节点：SS、Trojan与VMess底层工作原理解析", "小白入门教程", ["什么是机场节点", "Shadowsocks协议", "Trojan协议", "V2Ray原理", "科学上网协议"], "什么是机场节点,Shadowsocks协议,Trojan协议,V2Ray原理,科学上网协议", "科普指南：深度拆解什么是机场节点，对比 Shadowsocks、Trojan、VMess 与 Hysteria2 四大协议的加密与速度差异。", t2_body)

# 3. Free Trial Airports Risks
t3_body = f"""## 1. 为什么“免费梯子”和“永久免费试用”不可信？

互联网上流传着许多宣称“永久免费”、“无限流量”、“无需注册一键连接”的免费梯子或免费 VPN 软件。许多新手小白为了省钱而安装使用，却不知背后隐藏着巨大的安全隐患。

所谓“天下没有免费的午餐”，运营海外服务器带宽与专线拥有高昂的固定月度成本。**任何不收取费用的免费梯子，必然通过其他方式从用户身上获取商业利益。**

## 2. 免费梯子的五大致命安全陷阱与风险

1. **变相卖流量与个人隐私泄露**：绝大多数免费梯子会在后台收集用户的浏览历史、设备信息甚至账号密码，打包出售给广告商或黑色产业链。
2. **中间人攻击 (MITM) 与注入广告**：免费代理软件可在传输的网页中篡改内容、插入恶意弹窗广告或拦截未加密的账户数据。
3. **捆绑木马与恶意病毒**：许多名为“免费梯子”的 `.apk` 或 `.exe` 安装包中捆绑了后门木马，可能盗取您的社交与支付密码。
4. **极度拥堵与高频断网**：免费服务器通常成千上万人挤在一个带宽极小的节点上，丢包率高达 50% 以上，根本无法正常看视频或游戏。
5. **极其容易被封锁**：由于免费节点 IP 被滥用，通常几小时内就会被防火墙批量封锁，导致频繁“失效失联”。

{get_top4_block()}

## 3. 合理的平民低成本解决方案

如果您预算有限，正确的做法不是使用危险的免费梯子，而是选择价格透明、折算单月极便宜的合规平民机场：

- **平民年付首选**：[飞猫云](/providers/flycat-cloud/)（年付仅需 84 元，折合 **7 元/月**），提供真正的专线节点与官方客户端支持，安全放心。
- **灵活月付首选**：[微风网络](/providers/breezenet/)（起步仅 **12 元/月**），随用随充，资金无压力。

## 4. 延伸阅读与相关安全指南
- 📖 [新手小白科学上网教程：零基础3步学会梯子节点导入](/tutorials/beginner-vpn-tutorial/)
- 🔒 [网络隐私与数据安全：使用梯子上网的防追踪安全须知](/tutorials/privacy-security-tips/)
- 💰 [性价比机场推荐：平民小白月付与年付梯子对比指南](/picks/value-airports-recommendation/)
"""
write_article("free-trial-airports-risks.md", "免费试用机场的风险与陷阱：为什么不建议使用免费梯子", "小白入门教程", ["免费试用机场", "免费梯子风险", "个人隐私泄露", "免费暗坑", "廉价梯子安全"], "免费试用机场,免费梯子风险,个人隐私泄露,免费暗坑,廉价梯子安全", "避坑指南：深度揭露免费梯子与永久免费机场的五大安全陷阱，分析隐私泄露风险并推荐高性价比平民替代方案。", t3_body)

# 4. Traffic Need Calculator
t4_body = f"""## 1. 购买机场时该选多少流量？不要多花冤枉钱

新手小白在初次购买机场套餐时，经常纠结：**“每月 50GB、150GB 还是 500GB 够我用？”**

买少了流量不够用中途断网，买多了每个月用不完白白浪费资金。本文为您精确计算不同网络应用下的流量消耗，帮助您精细化选对套餐。

## 2. 常见网络行为流量消耗实测数据表

| 上网行为 / 应用场景 | 分辨率 / 画质 | 流量消耗参考算法 | 1GB 流量可使用时间 |
| :--- | :--- | :--- | :--- |
| **网页浏览 / 查资料** | 纯文字 + 图片 | 约 50MB - 100MB / 小时 | **可看 10 - 20 小时** |
| **ChatGPT / Claude 对话** | 文本交互 | 约 20MB - 50MB / 天 | **可对话 20 - 50 天** |
| **YouTube 视频播放** | 1080P 高清 | 约 1.5GB / 小时 | 可观看约 40 分钟 |
| **YouTube / Netflix 影音** | **4K 超高清 (2160P)** | **约 7.0GB / 小时** | 仅可观看约 8 分钟 |
| **TikTok / Ins 刷短视频** | 720P - 1080P | 约 1.0GB - 2.0GB / 小时 | 可刷约 30 - 60 分钟 |
| **Steam / Epic 游戏连线** | 纯联机数据包 | 约 30MB - 80MB / 小时 | **可连线 12 - 30 小时** |

{get_top4_block()}

## 3. 四种典型用户画像与推荐套餐对照

1. **轻度小白 / 学术查资料用户**
   - *习惯*：主要用于 Google 搜索、查阅论文、ChatGPT 写作、偶尔看 1080P 视频。
   - *建议*：**50GB - 100GB / 月**（推荐选择 [飞猫云](/providers/flycat-cloud/) 年付 50GB/月套餐，折合 7 元/月）。
2. **中度高清影音 / 追剧党**
   - *习惯*：每天晚上看 1-2 小时 YouTube 或 Netflix 1080P/4K 电视剧。
   - *建议*：**150GB - 300GB / 月**（推荐选择 [灵动云](/providers/lingdong-cloud/) 15元/月 150GB 套餐）。
3. **重度 4K 影音 / 海量下载玩家**
   - *习惯*：全天候 4K/8K 视频不间断播放，下载大容量海外资源。
   - *建议*：**500GB - 1TB / 月**（推荐选择 [暮光网络](/providers/twilight-cloud/) 旗舰版或大流量包）。
4. **多设备家庭共享**
   - *习惯*：5-10 台设备同时在线，兼顾游戏、办公与影音。
   - *建议*：选择不限制同时在线设备数的大流量套餐。

## 4. 延伸阅读与相关选购文章
- 📖 [性价比机场推荐：平民小白月付与年付梯子对比指南](/picks/value-airports-recommendation/)
- 🎬 [Netflix 奈飞解锁专用机场推荐：4K 8K 秒开不卡顿节点选择](/streaming/netflix-unlock-airports/)
- 💰 [月付机场推荐：随用随充不踩坑的灵活梯子挑选技巧](/picks/monthly-pay-airports/)
"""
write_article("traffic-need-calculator.md", "如何判断自己的流量需求：GB/月套餐挑选全方位算账", "小白入门教程", ["流量需求计算", "月套餐选择", "GB流量算账", "套餐比较", "机场买多少流量"], "流量需求计算,月套餐选择,GB流量算账,套餐比较,机场买多少流量", "全方位算账指南：手把手教您根据网页浏览、ChatGPT 对话、YouTube 4K 视频等算清流量消耗，挑选最省钱的套餐。", t4_body)

# 5. Test VPN Speed Latency Loss
t5_body = f"""## 1. 为什么“节点跑分大数字”不等于真实上网速度？

许多新手小白看机场评测时，往往只看测速图上“几百兆 (Mbps)”的峰值跑分跑满截图。然而购买后却发现：**网页打开依然缓慢、游戏频繁掉线、甚至连 YouTube 1080P 都在不断缓冲。**

这是因为：软件测速测得的仅是单次多线程下载的短时间极限峰值，而决定日常科学上网流畅度的三个核心指标是：**延时 (Ping)、抖动 (Jitter) 与 丢包率 (Packet Loss)。**

## 2. 三大核心网络性能指标解析

### (1) 延迟 (Ping / Latency)
- **含义**：数据包从您电脑出发到达海外节点并返回所需的毫秒数 (ms)。
- **标准**：香港节点推荐在 **20-40ms** 以内；日本/韩国节点在 **35-60ms** 以内；美国节点在 **130-180ms** 以内。

### (2) 丢包率 (Packet Loss)
- **含义**：在传输过程中丢失的数据包百分比。
- **标准**：对于游戏和视频连线，丢包率必须为 **0.0%**。若丢包率超过 3%，即会出现明显的网页加载超时与视频缓冲。高端专线机场（如 [灵动云](/providers/lingdong-cloud/)）能保持全天 0 丢包。

### (3) 晚高峰抗拥堵性能 (Peak-hour SLA)
- **含义**：在每天晚间 20:00 - 23:00 全网出口最拥堵的时段，机场节点是否能维持稳定速度。

{get_top4_block()}

## 3. 小白如何自己客观测试梯子速度？

1. **网页端真实跑分测试**：打开 [Fast.com](https://fast.com) 或 [Speedtest.net](https://speedtest.net)，切勿开启多线程暴拉模式，观察单线程的平稳下载数值。
2. **YouTube 统计信息测试**：在 YouTube 播放 4K 视频时，右键视频点击 **“详细统计信息” (Stats for nerds)**，查看 `Connection Speed` 运行速度是否保持在 `50,000 Kbps` 以上。
3. **命令行 MTR 追踪**：使用 WinMTR 或 PingPlotter 软件测试节点 IP，直观查看具体在哪一级路由节点产生了丢包。

## 4. 延伸阅读与相关教程
- 📖 [如何测试梯子真实速度：不要只看跑分，看懂延迟与丢包率](/tutorials/test-vpn-speed-latency-loss/)
- 📊 [深港与沪日IEPL专线测评：晚高峰游戏连线实测数据解读](/iplc-gaming/shengang-hurik-iepl-review/)
- ⚡ [IEPL专线机场推荐：0丢包超低延迟游戏梯子挑选指南](/iplc-gaming/iepl-gaming-airports/)
"""
write_article("test-vpn-speed-latency-loss.md", "如何测试梯子真实速度：不要只看跑分，看懂延迟与丢包率", "小白入门教程", ["测试梯子速度", "看懂延迟", "丢包率测试", "梯子测速", "机场真实速度"], "测试梯子速度,看懂延迟,丢包率测试,梯子测速,机场真实速度", "客观测试指南：教您看懂 ping 延迟、抖动与丢包率对梯子速度的影响，学会使用 Fast.com 与 YouTube 统计信息测出真实网速。", t5_body)

# 6. Cross Platform Setup Guide
t6_body = f"""## 1. 2026年全平台魔法上网接入架构概览

无论是使用 Windows 笔记本、Mac 苹果电脑、iPhone 手机还是 Android 安卓设备，科学上网的本质都是：**通过本地代理客户端，将流量加密打包发送至海外机场的代理节点。**

为了帮助新手小白一站式搞定全平台设备连线，编辑部整理了下述全平台客户端最佳匹配推荐。

## 2. 全平台客户端推荐与选择对照表

| 操作系统 / 设备 | 推荐首选客户端 | 备用客户端 | 特色优势 |
| :--- | :--- | :--- | :--- |
| **Windows 10/11** | **[Clash Verge Rev](/clients/clash-verge-guide/)** | v2rayN | 全中文界面、支持 TUN 游戏模式 |
| **macOS (M芯片/Intel)**| **[Clash Verge Mac](/clients/clash-verge-guide/)** | Sing-box / Stash | 内存占用低、原生理疗 M 芯片 |
| **iPhone / iPad** | **[Shadowrocket (小火箭)](/clients/shadowrocket-ios-tutorial/)** | Quantumult X | 规则分流、扫码一键导入 |
| **Android 安卓** | **[Flclash / Clash Meta](/clients/clash-meta-android-guide/)** | Surfboard (冲浪板) | 支持 Hysteria2、分流省电 |

{get_top4_block()}

## 3. 全平台共通的 3 步一键接入流程

无论您在哪个平台上操作，连线流程都可以归纳为统一的 3 个步骤：

1. **注册机场获取通用订阅**：注册高品质专线机场（首推 [灵动云](/providers/lingdong-cloud/) 或 [飞猫云](/providers/flycat-cloud/)），在控制台复制通用订阅地址。
2. **安装对应的客户端应用**：根据上面的表格在相应设备上安装合适软件。
3. **导入订阅并启动系统代理**：粘贴订阅 URL 刷新节点，勾选低延迟节点并开启代理开关。

## 4. 延伸阅读与全平台客户端单篇教程
- 📖 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 📱 [Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤](/clients/clash-meta-android-guide/)
- 🍎 [Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用](/clients/shadowrocket-ios-tutorial/)
- 🚀 [Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置](/clients/sing-box-client-guide/)
"""
write_article("cross-platform-setup-guide.md", "手机电脑魔法上网设置：全平台代理客户端一键接入指南", "小白入门教程", ["魔法上网设置", "全平台代理", "客户端一键接入", "手机电脑连线", "科学上网指南"], "魔法上网设置,全平台代理,客户端一键接入,手机电脑连线,科学上网指南", "一站式全平台魔法上网接入指南：覆盖 Windows、Mac、iPhone 与 Android 设备的客户端选择与保姆级连线步骤。", t6_body)

# 7. Beginner VPN Tutorial
t7_body = f"""## 1. 零基础新手小白科学上网入门第一课

如果您是第一次接触“机场”、“节点”、“订阅”和“Clash”这些概念，请不要被复杂的专业术语吓退。其实科学上网就像使用软件一样简单。

为了让没有任何技术背景的小白用户也能快速学会，本文将晦涩的概念转化为最形象的比喻，并提供 **零基础 3 步保姆级连线教程**。

## 2. 新手必懂的四大通俗概念

1. **什么是“机场”？**：机场就是提供海外部署了网络节点的专业服务商网站。
2. **什么是“节点”？**：节点就是位于海外（如香港、日本、美国）的中转服务器，您的流量通过它访问海外网站。
3. **什么是“订阅链接”？**：订阅链接是一串包含了机场所有节点参数的专属 URL 网址。
4. **什么是“客户端软件”？**：客户端（如 Clash 或小火箭）是安装在您电脑或手机上的软件，负责读取订阅链接并开启代理。

{get_top4_block()}

## 3. 零基础 3 步极速上手教程

### 第一步：注册机场并获取订阅链接
点击注册首推的优质机场 [灵动云]({top4[0]['inviteURL']}) 或平民年付机场 [飞猫云]({top4[2]['inviteURL']})，登录用户后台，找到“一键订阅”按钮并点击复制。

### 第二步：下载安装对应的代理客户端
- **电脑用户**：下载 [Clash Verge Rev](/clients/clash-verge-guide/) 并安装。
- **苹果手机**：下载 [Shadowrocket (小火箭)](/clients/shadowrocket-ios-tutorial/)。
- **安卓手机**：下载 [Flclash](/clients/clash-meta-android-guide/)。

### 第三步：粘贴订阅并开启连线
打开客户端软件，粘贴刚才复制的订阅链接点击“导入”。在节点列表中选择一个延迟最小的香港或日本节点，勾选“规则模式”，点击开启系统代理即可愉快连线！

## 4. 延伸阅读与相关入门指南
- 📖 [科学上网入门第一课：如何看懂流量、倍率与节点协议](/tutorials/vpn-basics-traffic-multiplier/)
- 🛠️ [机场节点订阅导入教程：通用URL订阅与通用格式转换](/tutorials/airport-subscription-import/)
- 🔒 [购买机场梯子前的检查清单：防踩坑、防跑路与隐私防护](/tutorials/pre-purchase-checklist/)
"""
write_article("beginner-vpn-tutorial.md", "新手小白科学上网教程：零基础3步学会梯子节点导入", "小白入门教程", ["科学上网教程", "新手翻墙指南", "节点导入", "魔法上网", "零基础梯子"], "科学上网教程,新手翻墙指南,节点导入,魔法上网,零基础梯子", "面向完全零基础小白的科学上网保姆级入门教程。拆解通用概念，通过 3 个简单步骤带您轻松搞定节点导入与科学上网。", t7_body)

# 8. How to Choose Node Regions
t8_body = f"""## 1. 为什么选择合适的节点地区至关重要？

在机场客户端的节点列表中，通常会排列着数十个来自不同国家和地区的节点（如 HK 香港、JP 日本、SG 新加坡、US 美国、UK 英国等）。

许多新手小白随便点选一个节点连线，可能会发现：**有的节点看视频快但打不开网页，有的节点能看 Netflix 但 ChatGPT 提示被封。**

这是因为：不同的节点地区在**物理延迟、出口 IP 纯净度以及流媒体/AI 解锁权限**上存在巨大差异。

## 2. 热门节点地区特色与适用场景全解析

### (1) 香港节点 (Hong Kong - HK)
- **优势**：物理距离最近（广东地区延迟低至 20ms），网页打开秒开，游戏响应极快。
- **适用场景**：日常网页浏览、外服游戏连线、YouTube 4K 播放。
- **注意**：部分 AI 工具（如 ChatGPT / Claude）因政策原因不对香港 IP 开放。

### (2) 日本节点 (Japan - JP)
- **优势**：延迟极低（30-45ms），网络基础设施优异，原生 IP 丰富。
- **适用场景**：完美解锁 Netflix 日本区、Pixiv、动画番剧、ChatGPT 对话及日本区游戏。

### (3) 新加坡节点 (Singapore - SG)
- **优势**：东南亚核心枢纽，线路稳定，对全球主流 AI 工具友好。
- **适用场景**：ChatGPT、Claude AI、Disney+ 及东南亚服务器游戏。

### (4) 美国节点 (United States - US)
- **优势**：节点带宽充沛，完全解锁美国本土所有 AI 功能、金融网站及特定限制应用。
- **缺点**：物理距离远，延迟较高（约 140ms - 180ms）。

{get_top4_block()}

## 3. 常见场景节点选择快速速查表

| 上网需求 / 场景 | 推荐首选节点地区 | 推荐备用节点地区 | 推荐机场服务商 |
| :--- | :--- | :--- | :--- |
| **极致网页秒开 & 游戏低延迟** | **香港 (HK)** | 台湾 (TW) | [灵动云](/providers/lingdong-cloud/) |
| **ChatGPT & Claude AI 对话** | **日本 (JP) / 新加坡 (SG)** | 美国 (US) | [灵动云](/providers/lingdong-cloud/) |
| **Netflix 奈飞追剧** | **日本 (JP) / 香港 (HK)** | 美区 (US) | [暮光网络](/providers/twilight-cloud/) |
| **日常备用与轻度上网** | **香港 (HK)** | 日本 (JP) | [飞猫云](/providers/flycat-cloud/) |

## 4. 延伸阅读与相关指南
- 📖 [什么是机场节点：SS、Trojan与VMess底层工作原理解析](/tutorials/what-is-airport-node-protocols/)
- 🎬 [Netflix 奈飞解锁专用机场推荐：4K 8K 秒开不卡顿节点选择](/streaming/netflix-unlock-airports/)
- ⚡ [IEPL专线机场推荐：0丢包超低延迟游戏梯子挑选指南](/iplc-gaming/iepl-gaming-airports/)
"""
write_article("how-to-choose-node-regions.md", "机场节点地区怎么选：香港、日本、新加坡、美国节点选哪家", "小白入门教程", ["节点地区选择", "香港节点", "日本节点", "新加坡节点", "美国节点"], "节点地区选择,香港节点,日本节点,新加坡节点,美国节点", "全方位解析机场节点地区挑选技巧。拆解香港、日本、新加坡、美国等节点的延迟、流媒体与 ChatGPT 解锁差异。", t8_body)

# 9. Airport Subscription Import
t9_body = f"""## 1. 什么是机场订阅链接？它的底层机制是什么？

在科学上网过程中，**机场订阅链接**（Subscription URL）是连接服务商与客户端的桥梁。

订阅链接本质上是一个托管在云端服务器上的文本地址。当您在 Clash Verge、小火箭或 v2rayN 中添加该 URL 并点击“更新”时，客户端会自动下载并解析其中包含的数十个甚至上百个节点的加密参数（包括 IP、端口、UUID、密匙与协议类型）。

掌握订阅导入与格式转换技巧，能让您在更换设备时实现秒级重新接入。

## 2. 订阅导入的两大核心方式（扫码 vs 链接粘贴）

### 方式 A：一键链接复制与粘贴导入（推荐电脑端）
1. 登录机场控制台（如 [灵动云](/providers/lingdong-cloud/)），找到“订阅管理”菜单。
2. 点击“复制 Clash 订阅”或“复制通用订阅”。
3. 在 Clash Verge 或 v2rayN 客户端中找到“订阅配置” -> 点击“添加/导入”，粘贴 URL 即可。

### 方式 B：二维码扫码导入（推荐手机端）
1. 在电脑上打开机场后台，展示该订阅的 QR 二维码。
2. 在手机端软件（如 [小火箭 Shadowrocket](/clients/shadowrocket-ios-tutorial/)）中点击右上角扫码图标，扫描电脑屏幕上的二维码即可瞬间完成导入。

{get_top4_block()}

## 3. 订阅导入失败的原因与通用转换技巧

- **问题一：导入后节点列表中全是汉字报错**
  *原因*：订阅链接粘贴有误，或者机场后台返回了 404 网页。请重新复制最新的智能聚合订阅 URL。
- **问题二：客户端提示“Unsupported Subscription Format”**
  *解决办法*：使用 [Sub-Converter 订阅转换工具](/tutorials/subconverter-tutorial/)，将原始链接转换为目标客户端支持的格式。

## 4. 延伸阅读与相关教程
- 📖 [Sub-Converter订阅转换教程：将机场订阅转换为Clash/Sing-box](/tutorials/subconverter-tutorial/)
- 💻 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 📱 [Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用](/clients/shadowrocket-ios-tutorial/)
"""
write_article("airport-subscription-import.md", "机场节点订阅导入教程：通用URL订阅与通用格式转换", "小白入门教程", ["节点订阅导入", "订阅URL转换", "Clash订阅", "小火箭导入", "通用订阅格式"], "节点订阅导入,订阅URL转换,Clash订阅,小火箭导入,通用订阅格式", "新手必看：机场节点订阅导入图文教程。拆解一键 URL 导入、二维码扫码导入与通用订阅格式转换步骤。", t9_body)

# 10. Subscription Error Troubleshooting
t10_body = f"""## 1. 为什么机场订阅会突然报错或更新失败？

在使用科学上网梯子时，最让小白用户头疼的就是原本正常的订阅突然提示“更新失败”、“超时”或所有节点变成红色 9999ms。

出现订阅报错并不一定意味着机场跑路。90% 以上的情况都是由于**本地客户端配置冲突、系统时间不同步、防火墙拦截或订阅 URL 格式损坏**所致。

本文整理了完整的故障排查诊断表，助您一步步恢复网络连接。

## 2. 四大常见订阅报错排查与解决方法

### 报错一：节点全部显示 9999ms 或 Timeout 超时
- **诊断**：能看到节点名称，但点测速全都不通。
- **核心原因**：本地电脑/手机系统时间与北京时间不同步（偏差大于 30 秒）。
- **解决步骤**：进入 Windows / Mac / 手机“系统设置” -> “时间与语言” -> 开启“自动同步网络时间”，重新右键刷新订阅。

### 报错二：更新订阅提示“Network Error”或“404 Not Found”
- **诊断**：点击更新订阅时弹框提示网络错误。
- **核心原因**：1. 机场更换了新的订阅域名；2. 账户套餐到期或流量用尽。
- **解决步骤**：登录机场后台（如 [灵动云](/providers/lingdong-cloud/)），确认套餐状态正常后重新复制最新的订阅 URL。

### 报错三：导入订阅提示“Config Parse Error”
- **诊断**：配置文件解析失败。
- **核心原因**：订阅链接解析出了非 YAML 格式内容。
- **解决步骤**：使用 [Sub-Converter 订阅转换工具](/tutorials/subconverter-tutorial/) 重新转换后再导入。

### 报错四：显示连线上但所有网页均打不开
- **诊断**：客户端打勾了，但网页提示无网络。
- **核心原因**：客户端路由模式误选为了“直连模式”或本地系统代理开关被意外关闭。
- **解决步骤**：将路由模式切换回 **“规则模式” (Rule)**，并确认“系统代理”开关处于高亮开启状态。

{get_top4_block()}

## 3. 防范连线故障的良好日常习惯

1. 保持备用机场订阅（推荐搭配 [飞猫云](/providers/flycat-cloud/) 平民年付作为应急备用）。
2. 定期手动在客户端中更新订阅与规则集。
3. 勿在公共场合未加密的 Wi-Fi 下随意更改软件代理端口。

## 4. 延伸阅读与关联教程
- 📖 [Clash 常见报错解决：Core Path 不存在与 Config Parse Error 排查](/clients/clash-common-errors-fix/)
- 🛠️ [Sub-Converter订阅转换教程：将机场订阅转换为Clash/Sing-box](/tutorials/subconverter-tutorial/)
- 💻 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
"""
write_article("subscription-error-troubleshooting.md", "机场订阅报错解决指南：节点超时、更新失败与连接错误排查", "小白入门教程", ["机场订阅报错", "节点超时解决", "更新失败排查", "连线错误", "梯子故障诊断"], "机场订阅报错,节点超时解决,更新失败排查,连线错误,梯子故障诊断", "故障排查大全：手把手教您解决机场订阅更新失败、节点超时 9999ms、解析报错与无法上网等常见问题。", t10_body)

print("Generated all 10 long-form Beginner Tutorial articles successfully!")
