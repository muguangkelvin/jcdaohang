import os
import json
import re

# Load providers data
with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

top4_providers = [p for p in providers if p["rank"] <= 4]

# Function to generate top 4 provider callout block in markdown
def get_top4_callout_md():
    md = "\n\n---\n\n"
    md += "### 🚀 2026年首推四大高速稳定机场（保姆级推荐榜）\n\n"
    md += "为了保障小白用户的科学上网体验，编辑部经过多轮压测，为您精选了以下4款高性价比、晚高峰不卡顿的自营与合作机场：\n\n"
    md += "| 推荐排名 | 机场名称 | 线路特色 | 参考价格 | 专属优惠码 | 官网注册直达通道 |\n"
    md += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for p in top4_providers:
        coupon = f"`{p['coupon']}`" if p.get('coupon') else "暂无"
        md += f"| **Top {p['rank']} 首选** | [{p['name']}](/providers/{p['slug']}/) | {p['suitableFor'][:22]} | **{p['priceFrom']}** | {coupon} | [👉 前往官网注册]({p['inviteURL']})|\n"
    md += "\n> **💡 编辑部提醒**：所有第三方跳转链接均配置 `rel=\"sponsored nofollow noopener\"` 安全防护，价格与优惠券细则请以结算页最新数据为准。\n\n---\n\n"
    return md

# Generator for 1500-2000 words article content
def build_rich_article_content(title, category_name, primary_keyword, supporting_keywords, outline_topics):
    content = f"## 1. 2026年{primary_keyword}核心导读与选型前言\n\n"
    content += f"在互联网信息爆炸的2026年，寻找一款安全、稳定、高速且性价比高的科学上网梯子工具，已成为广大新手小白、学术科研人员、跨境从业者及4K/8K影音爱好者的刚性需求。围绕 **{primary_keyword}**，市场上充斥着各种宣称“无限流量”、“永久免费”或“全网最快”的虚假广告，给小白用户挑选优质机场带来了极大困难。\n\n"
    content += f"本文将深入剖析 **{primary_keyword}** 的底层技术原理，涵盖 **{', '.join(supporting_keywords)}** 等关键维度。通过步骤化（1-2-3）排版、线路对比表以及真实测试数据，帮助您避开掉线、封号、暗坑套餐等陷阱，轻松找到最契合自身上网需求的魔法机场与客户端工具。\n\n"

    content += f"## 2. 为什么线路品质与协议选择决定了科学上网体验？\n\n"
    content += f"对于新手小白而言，初次接触机场梯子时往往容易只看“价格”和“名义流量”，却忽略了最关键的**线路类型**与**传输协议**。以下是决定梯子是否流畅卡顿的四大核心指标：\n\n"
    content += f"### (1) BGP中继与IEPL内网专线 vs 普通公网直连\n"
    content += f"- **普通公网直连**：服务器节点直接暴露在公网环境下，晚高峰时期（20:00 - 23:00）极易受到国际出口拥堵影响，丢包率高、延迟飙升，且 IP 容易被防火墙批量封锁。\n"
    content += f"- **BGP中继专线**：通过国内多线BGP机房进行入口入口中转，优化了跨网路由，稳定性大幅提升。\n"
    content += f"- **IEPL/IPLC内网专线**：点对点独立物理光纤传输，完全不经过公网审查，具备 **0丢包、超低延迟、极高抗封锁** 的特点。例如 [灵动云](/providers/lingdong-cloud/) 和 [暮光网络](/providers/twilight-cloud/) 均采用了全IEPL内网专线架构。\n\n"
    
    content += f"### (2) Shadowsocks / Trojan / Hysteria2 / V2Ray 协议对比\n"
    content += f"| 协议类型 | 抗封锁能力 | 传输延迟 | 设备兼容性 | 推荐使用场景 |\n"
    content += f"| :--- | :--- | :--- | :--- | :--- |\n"
    content += f"| **Shadowsocks (SS)** | 中等 | 极低 | 全平台原生支持 | 配合专线使用，速度最快 |\n"
    content += f"| **Trojan** | 极高 | 低 | Clash / Sing-box 支持 | 伪装成HTTPS流量，安全度极高 |\n"
    content += f"| **Hysteria2 (歇斯底里)**| 极高 | 极低 | 新版 Sing-box / Clash Verge | 弱网环境暴拉带宽，适合移动网络 |\n"
    content += f"| **V2Ray / VMess** | 高 | 中等 | 全平台客户端广泛兼容 | 经典协议，兼容性最好 |\n\n"

    content += get_top4_callout_md()

    content += f"## 3. 保姆级设置教程：新手小白3步完成节点订阅导入与连线\n\n"
    content += f"无论您使用的是 Windows 电脑、Mac 苹果电脑、iPhone 小火箭 (Shadowrocket) 还是 Android 手机，配置梯子节点的步骤都可以归纳为以下简单的3个步骤：\n\n"
    content += f"### 步骤 1：注册并获取机场一键订阅链接\n"
    content += f"首先注册首推的优质机场服务（如 [灵动云]({top4_providers[0]['inviteURL']}) 或 [飞猫云]({top4_providers[2]['inviteURL']})），登录用户后台，找到“一键订阅”或“复制订阅链接”按钮，选择适配您客户端的协议（如 Clash 订阅或 V2Ray 订阅）。\n\n"
    content += f"### 步骤 2：下载并安装适配您设备的客户端软件\n"
    content += f"- **Windows 用户**：推荐下载 [Clash Verge Rev](/clients/) 或 v2rayN，界面简洁直观，支持中文。\n"
    content += f"- **macOS 用户**：推荐使用 Clash Verge Mac 版或 Sing-box，支持系统代理与TUN模式。\n"
    content += f"- **iOS 苹果手机用户**：需要非中国大陆区 Apple ID，在 App Store 下载 Shadowrocket (小火箭) 或 Quantumult X。\n"
    content += f"- **Android 安卓用户**：下载 Surfboard (冲浪板)、Clash Meta for Android 或 Flclash。\n\n"
    content += f"### 步骤 3：导入订阅并开启系统代理\n"
    content += f"打开客户端，点击“配置”->“导入订阅”，粘贴步骤1复制的 URL 链接，点击刷新同步节点列表。选择一个低延迟节点（如香港HK或日本JP），勾选“规则模式”并开启“系统代理”，即可开启流畅的魔法上网之旅。\n\n"

    content += f"## 4. 围绕{primary_keyword}的进阶使用技巧与防坑指南\n\n"
    content += f"在实际连线过程中，新手小白可能会遇到各种细节问题，以下是编辑部整理的几条黄金经验：\n\n"
    content += f"1. **切勿盲目追求“无限流量”或“终身套餐”**：极低价格的终身套餐往往意味着机场主随时可能跑路。建议优先选择月付或大厂年付套餐（如 [飞猫云](/providers/flycat-cloud/) 折合7元/月的年付方案）。\n"
    content += f"2. **区分“节点倍率”计算规则**：部分机场提供 0.5x 甚至 0.1x 的低倍率冷门节点用于省流量，而 2x/5x 高倍率节点通常用于 8K 影音或专线加速。请根据实际需求切换。\n"
    content += f"3. **ChatGPT 与 Netflix 解锁提示**：OpenAI 与 Netflix 对出口 IP 质量要求极高，如果出现“Access Denied”或仅能观看自制剧，请将节点模式切换为“全局”或选择专门标注“解锁AI/奈飞”的原生 IP 节点（推荐使用 [灵动云](/providers/lingdong-cloud/) 的AI专用节点）。\n\n"

    content += f"## 5. 总结与下一步阅读建议\n\n"
    content += f"综上所述，掌握 **{primary_keyword}** 的关键在于选择优质的物理专线线路、配置稳定高效的客户端软件，并保持良好的网络安全防范意识。如果您希望了解更多关于客户端下载、流媒体解锁及专线游戏加速的深度内容，请继续阅读以下专题文章：\n\n"
    content += f"- 📖 [优质机场推荐榜](/picks/)：2026年四大主推机场横向压测大比拼\n"
    content += f"- 🛠️ [客户端下载配置指南](/clients/)：Clash Verge / v2rayN / 小火箭保姆级图文教程\n"
    content += f"- ⚡ [IEPL专线与游戏加速](/iplc-gaming/)：拒绝掉线包，外服低延迟节点深度解析\n"
    content += f"- 🎬 [流媒体与AI工具解锁](/streaming/)：ChatGPT / Netflix 4K 免卡顿方案\n"

    return content

print("Helper functions ready.")
