import os
import json

os.makedirs("content/clients", exist_ok=True)

with open("data/providers.json", "r", encoding="utf-8") as f:
    providers = json.load(f)

top4 = [p for p in providers if p["rank"] <= 4]

def get_top4_block():
    md = "\n\n---\n\n"
    md += "### 🚀 2026年编辑部首推四大优质专线机场推荐（客户端通用订阅通道）\n\n"
    md += "客户端软件需要搭配高速稳定的机场节点才能发挥极致速度。编辑部压测并推荐以下 4 款自营与合作优质机场：\n\n"
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

**【导读摘要】**：{summary}

{body_md}
"""
    with open(f"content/clients/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

# 1. Clash Meta (Flclash) Android Guide
c1_body = f"""## 1. 2026年 Android 安卓平台最佳代理软件 Clash Meta (Flclash) 简介

在 Android 安卓手机与平板平台上，**Clash Meta**（包含其分支应用 **Flclash**）是目前公认功能最强、协议支持最全的科学上网客户端。它基于最新的 Clash.Meta (Mihomo) 内核构建，全面支持传统 Shadowsocks (SS)、Trojan、VMess、VLESS 以及新一代的 **Hysteria2 (歇斯底里)** 与 TUIC 协议。

相比传统老旧客户端，Flclash 拥有现代化 Material You 界面设计，操作极其流畅，且支持自动后台省电策略，是安卓新手小白连线的首选。

## 2. 步骤化图文配置指南（1-2-3 步骤）

### 步骤 1：下载安装正版 APK 安装包
1. 访问官方开源 GitHub Releases 页面或本站推荐链接下载 Flclash/Clash Meta 的 `.apk` 安装包。
2. 在安卓手机中打开安装包，允许“安装未知来源应用”权限并完成安装。

### 步骤 2：获取并导入机场一键订阅 URL
1. 登录您购买的专线机场后台（推荐选择 [灵动云](/providers/lingdong-cloud/) 或 [飞猫云](/providers/flycat-cloud/)）。
2. 在“一键订阅”菜单中点击“复制 Clash 订阅链接”或“一键导入到 Clash”。
3. 打开 Flclash 软件，点击“配置” (Profiles) -> “添加” (Add)，粘贴订阅 URL，点击右上角保存并刷新节点。

### 步骤 3：启动代理并设置路由规则
1. 返回软件主界面，点击底部的“开启” (Start) 按钮，在系统弹出的“网络连接请求 (VPN 权限)”中点击“允许”。
2. 将路由模式切换为 **“规则模式” (Rule)**，挑选一个低延迟绿色节点，手机即可顺畅访问海外网页与应用。

{get_top4_block()}

## 3. 安卓手机使用中的防坑与优化设置

1. **设置系统后台白名单（防止进程被杀）**：进入手机“设置” -> “电池/省电策略”，将 Clash Meta / Flclash 设置为“无限制”或“允许后台高耗电运行”，防止息屏后断网。
2. **开启“应用分流”功能**：如果您希望某些国内 App（如微信、支付宝、网易云音乐）完全不经过代理，可在客户端设置中开启“应用分流” (Bypass Apps)，勾选对应的应用即可。
3. **节点超时排查**：若显示节点延迟为 9999ms，请进入系统设置确认“自动同步网络时间”已开启。

## 4. 延伸阅读与相关客户端指南
- 💻 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 🍎 [Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用](/clients/shadowrocket-ios-tutorial/)
- 📱 [Surfboard (冲浪板) 下载与使用教程：Android 平台优雅代理](/clients/surfboard-android-tutorial/)
- 🚀 [Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置](/clients/sing-box-client-guide/)
"""
write_article("clash-meta-android-guide.md", "Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤", "客户端下载配置", ["Clash Meta安卓", "Flclash配置", "安卓手机梯子", "Android科学上网", "手机代理软件"], "Clash Meta安卓,Flclash配置,安卓手机梯子,Android科学上网,手机代理软件", "2026 最新 Android 安卓平台 Clash Meta (Flclash) 极速连线教程。手把手教您下载 APK、导入机场订阅、设置系统后台白名单与应用分流。", c1_body)

# 2. Clash Verge Guide
c2_body = f"""## 1. 为什么 Clash Verge Rev 是 2026年 Windows/Mac 首选客户端？

在过去的代理软件演进中，原版的 Clash for Windows (CFW) 已停止维护。**Clash Verge Rev** 作为其最佳替代者，基于 Tauri + Rust 架构开发，内存占用小、启动速度极快，并完美继承了开源社区最新的 Mihomo (Clash.Meta) 核心。

它同时原生适配了 Windows 10/11 操作系统与 Apple Silicon (M1/M2/M3/M4) 系列芯片的 Mac 电脑，提供全中文界面与简便的订阅管理。

## 2. Windows / macOS 平台 3 步保姆级安装与使用教程

### 步骤 1：下载安装合适版本的 Clash Verge
访问开源 Releases 页面下载安装包：
- **Windows 用户**：下载 `Clash.Verge_x64-setup.exe` 并安装。
- **Mac 苹果电脑用户**：根据芯片选择 `x64.dmg`（Intel 芯片）或 `aarch64.dmg`（Apple 芯片），将软件拖入 Applications 文件夹。

### 步骤 2：导入机场订阅链接
1. 注册并登录您的专线机场后台（推荐选择 [灵动云](/providers/lingdong-cloud/) 或 [暮光网络](/providers/twilight-cloud/)）。
2. 复制控制台中的“一键 Clash 订阅 URL”。
3. 打开 Clash Verge，点击左侧 **“订阅” (Profiles)** 菜单，在顶部输入框粘贴 URL 链接，点击“导入” (Import)。

### 步骤 3：开启系统代理与游戏/视频连线
1. 导入成功后，点击该订阅配置使其变为激活状态（高亮显示）。
2. 进入左侧 **“代理” (Proxies)** 页面，选择“规则模式” (Rule)，并挑选一个低延迟节点。
3. 点击左下角开启 **“系统代理” (System Proxy)** 开关，即可顺利访问 Google、YouTube 及 ChatGPT。

{get_top4_block()}

## 3. 高阶功能配置：TUN 模式与服务模式

对于需要玩外服游戏（如 CS2、Valorant）或使用全局软件的用户，强烈建议配置 TUN 模式：

1. 进入 Clash Verge **“设置” (Settings)** 页面。
2. 在 **“服务模式” (Service Mode)** 右侧点击“安装” (Install)，并在系统弹窗中点击“授权”。
3. 安装成功后，开启 **“TUN 模式”** 开关，即可接管系统底层的 UDP 游戏数据包，实现全盘连线加速。详情可参阅 [外服游戏 TUN 模式加速指南](/iplc-gaming/clash-verge-tun-mode-gaming/)。

## 4. 延伸阅读与相关教程
- 🔧 [Clash 常见报错解决：Core Path 不存在与 Config Parse Error 排查](/clients/clash-common-errors-fix/)
- 💻 [Mac 平台代理客户端对比：Clash Verge vs Sing-box vs Stash](/clients/mac-proxy-clients-comparison/)
- 🪟 [v2rayN 下载与配置教程：经典 Windows 梯子客户端保姆级设置](/clients/v2rayn-download-setup/)
- 🔄 [多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理](/clients/multi-client-sync-subscription/)
"""
write_article("clash-verge-guide.md", "Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端", "客户端下载配置", ["Clash Verge教程", "Windows梯子客户端", "Mac科学上网", "Clash指南", "Clash Verge Rev"], "Clash Verge教程,Windows梯子客户端,Mac科学上网,Clash指南,Clash Verge Rev", "2026年最新 Windows/Mac 最佳科学上网客户端 Clash Verge Rev 完整保姆级教程。手把手教您订阅导入、界面配置与 TUN 模式设置。", c2_body)

# 3. Clash Common Errors Fix
c3_body = f"""## 1. 为什么 Clash 客户端会出现各种报错？

新手小白在使用 Clash Verge、Clash for Windows 或 Clash Meta 过程中，偶发性的报错常常让人不知所措。产生报错的核心原因通常包括：**订阅 YAML 语法格式损坏、内核核心文件缺失、端口被其他软件占用、本地系统时间不同步** 等。

本文整理了全网最常见的 Clash 报错信息，并给出了精准一步到位的解决方案。

## 2. 5 大核心报错排查与解决方法

### 报错一：“Core Path 不存在” 或 “Clash Core missing”
- **原因**：软件安装过程中杀毒软件（如 Windows Defender 或 360）误删了 Mihomo/Clash 可执行内核文件。
- **解决办法**：关闭杀毒软件或将 Clash Verge 文件夹加入白名单，重新覆盖安装最新版 Clash Verge 软件即可自动补全内核。

### 报错二：“Config Parse Error” 或 “YAML syntax error”
- **原因**：机场返回的订阅链接中含有非法字符、网址跳转失败返回了 HTML 错误页面而非有效的 YAML 配置文件。
- **解决办法**：
  1. 重新登录机场后台（如 [灵动云](/providers/lingdong-cloud/)），确认账户套餐未过期且流量未耗尽。
  2. 使用 Sub-converter（订阅转换工具）重新将原始订阅转换为标准的 Clash 节点格式后再导入。

### 报错三：“Initial Proxy Group Failed” 或 “Empty Proxy List”
- **原因**：配置文件中指定的节点组为空或路由规则找不到对应节点。
- **解决办法**：在软件界面中右键该订阅选择“重新下载/强制刷新”，确保节点列表已成功加载。

### 报错四：“Port 7890 (or 9090) already in use”
- **原因**：本地 7890 代理端口被其他软件（如迅雷、百度网盘或旧版代理工具）占用。
- **解决办法**：进入 Clash Verge 设置页面，将 HTTP 代理端口从 `7890` 修改为 `7895` 或 `10809` 并保存。

### 报错五：所有节点显示延迟为 9999ms 或 Timeout 超时
- **原因**：90% 的情况是因为本地电脑/手机系统时间与标准北京时间存在偏差（相差超过 30 秒加密握手即失败）。
- **解决办法**：进入 Windows / Mac 系统设置，勾选“自动同步网络时间”，重新右键刷新订阅。

{get_top4_block()}

## 3. 防范报错的日常使用良好习惯

1. 保持客户端版本定期更新，使用社区维护的开源分支。
2. 配置备份机场（如 [飞猫云](/providers/flycat-cloud/)），避免单一订阅失效导致断网。
3. 勿随意修改生成的配置文件内容，除非了解标准的 YAML 缩进规则。

## 4. 延伸阅读与相关教程
- 📖 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 📱 [Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤](/clients/clash-meta-android-guide/)
- 🔄 [多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理](/clients/multi-client-sync-subscription/)
- 🛠️ [Sub-Converter订阅转换教程：将机场订阅转换为Clash/Sing-box](/tutorials/subconverter-tutorial/)
"""
write_article("clash-common-errors-fix.md", "Clash 常见报错解决：Core Path 不存在与 Config Parse Error 排查", "客户端下载配置", ["Clash报错解决", "Core Path不存在", "Config Parse Error", "Clash故障修复", "订阅转换报错"], "Clash报错解决,Core Path不存在,Config Parse Error,Clash故障修复,订阅转换报错", "深度排查 Clash 常见报错：手把手解决 Core Path 不存在、Config Parse Error、7890 端口占用以及 9999ms 超时问题。", c3_body)

# 4. Mac Proxy Clients Comparison
c4_body = f"""## 1. macOS 苹果电脑平台主流代理软件盘点

对于使用 Mac 苹果电脑（包含 Intel 芯片与 Apple M1/M2/M3/M4 系列芯片）的用户，选择一款性能优异、优雅易用的代理客户端至关重要。

目前 macOS 平台上最主流的三款代理工具分别是：
1. **Clash Verge Rev**（基于 Tauri + Mihomo 核心，免费开源）
2. **Sing-box GUI**（基于新一代 Universal 代理引擎，免费开源）
3. **Stash for Mac**（基于 Clash 规则生态的付费精致客户端）

编辑部从资源占用、M 芯片原生适配、TUN 性能以及易用性四大维度进行了深度实测。

## 2. 三大 Mac 代理客户端多维度对比表

| 对比维度 | Clash Verge Rev (Mac) | Sing-box GUI (Mac) | Stash for Mac |
| :--- | :--- | :--- | :--- |
| **软件性质** | 免费开源 | 免费开源 | 商业付费 ($9.99) |
| **界面语言** | 原生全中文 | 中文 / 英文 | 原生全中文 |
| **M系列芯片优化** | 原生 Apple Silicon 支持 | 原生 Apple Silicon 支持 | 原生 Apple Silicon 支持 |
| **内存占用 (RAM)** | 约 80MB - 150MB | **极低 (约 40MB)** | 约 100MB |
| **特色功能** | 强大的 Script & 规则集 | 支持 Hysteria2 / VLESS | 极致美观、可视化分析 |
| **小白推荐指数** | ⭐⭐⭐⭐⭐ (首选) | ⭐⭐⭐⭐ (适合极客) | ⭐⭐⭐⭐⭐ (体验极佳) |

{get_top4_block()}

## 3. 新手 Mac 用户该如何选择？

- **如果您追求简单免费、上手快**：首选 **Clash Verge Rev**。支持一键导入订阅，完美兼容国内各大专线机场（如 [灵动云](/providers/lingdong-cloud/) 和 [暮光网络](/providers/twilight-cloud/)）。
- **如果您希望协议最新、极致省电**：选择 **Sing-box**。在 M 芯片 Mac 上耗电极低，且对 Hysteria2 协议支持最好。
- **如果您预算充足、喜欢极简精致 UI**：购买 **Stash for Mac**，体验顶级可视化网络流量图表与策略组切换。

## 4. 延伸阅读与相关文章
- 📖 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 🚀 [Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置](/clients/sing-box-client-guide/)
- 🍎 [Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用](/clients/shadowrocket-ios-tutorial/)
- ⚡ [IEPL专线机场推荐：0丢包超低延迟游戏梯子挑选指南](/iplc-gaming/iepl-gaming-airports/)
"""
write_article("mac-proxy-clients-comparison.md", "Mac 平台代理客户端对比：Clash Verge vs Sing-box vs Stash", "客户端下载配置", ["Mac代理客户端", "Clash Verge Mac", "Stash配置", "Sing-box Mac", "macOS科学上网"], "Mac代理客户端,Clash Verge Mac,Stash配置,Sing-box Mac,macOS科学上网", "macOS 苹果电脑 3 大主流代理客户端横向对比：测评 Clash Verge Rev、Sing-box 与 Stash 在 M 芯片 Mac 上的内存占用、TUN 性能与易用性。", c4_body)

# 5. Quantumult X (圈x) iOS Guide
c5_body = f"""## 1. 什么是 Quantumult X (圈x)？它与小火箭有何区别？

在 iOS 苹果生态（iPhone/iPad）中，**Quantumult X**（俗称“圈x”）被誉为功能最强大的高阶网络代理软件。

相比面向小白用户的 Shadowrocket (小火箭)，Quantumult X 具备更强大的分流策略引擎、自定义 JavaScript 脚本重写 (Rewrite)、mitm 抓包及资源解析器能力。非常适合追求高自定义连线体验的进阶用户。

## 2. 保姆级图文设置步骤：3步完成节点导入与策略配置

### 步骤 1：从非中国区 App Store 购买下载
1. 准备一个非中国大陆区（如美区、港区）的 Apple ID 并在 App Store 登录。
2. 搜索并购买下载 Quantumult X（价格约为 $7.99 美金）。

### 步骤 2：使用资源解析器导入机场订阅
1. 登录您的专线机场后台（如 [灵动云](/providers/lingdong-cloud/) 或 [暮光网络](/providers/twilight-cloud/)），复制控制台的原始订阅链接。
2. 打开 Quantumult X，点击右下角的 **“风车”图标** 进入设置。
3. 在“节点”区域点击 **“引用 (订阅)”**，粘贴订阅 URL，并在最下方开启“资源解析器”开关，点击右上角保存。

### 步骤 3：开启系统代理与策略组选择
1. 返回软件主界面，长按右下角风车图标，开启代理开关。
2. 在节点策略组中，挑选一个低延迟香港或日本节点，即可畅享高品质科学上网。

{get_top4_block()}

## 3. Quantumult X 常用高阶使用技巧

1. **配置远程重写与脚本**：可导入第三方规则集，实现去广告、解锁特定网页以及自动化签到。
2. **多机场节点聚合**：圈x 支持同时添加多个机场的订阅（如主用 [灵动云](/providers/lingdong-cloud/) + 备用 [飞猫云](/providers/flycat-cloud/)），并在一个界面中进行节点检测。
3. **按需连接 (On Demand)**：开启按需连接后，当连接特定 Wi-Fi 或蜂窝网络时，圈x 将自动开启或关闭代理。

## 4. 延伸阅读与相关 iOS 教程
- 🚀 [Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用](/clients/shadowrocket-ios-tutorial/)
- 💻 [Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置](/clients/sing-box-client-guide/)
- 🔄 [多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理](/clients/multi-client-sync-subscription/)
- ⚡ [IEPL专线机场推荐：0丢包超低延迟游戏梯子挑选指南](/iplc-gaming/iepl-gaming-airports/)
"""
write_article("quantumult-x-ios-guide.md", "Quantumult X (圈x) 基础配置教程：iOS 高阶策略与节点导入", "客户端下载配置", ["Quantumult X配置", "圈x教程", "iOS高阶代理", "圈x节点导入", "iOS科学上网"], "Quantumult X配置,圈x教程,iOS高阶代理,圈x节点导入,iOS科学上网", "2026 最新 iOS 平台 Quantumult X (圈x) 基础配置教程。手把手教您资源解析器使用、机场订阅导入、策略组选择与脚本重写。", c5_body)

# 6. Shadowrocket (小火箭) iOS Tutorial
c6_body = f"""## 1. 为什么 Shadowrocket (小火箭) 是 iPhone/iPad 用户必装应用？

在所有 iOS 科学上网软件中，**Shadowrocket**（因图标为一只小火箭而被称为“小火箭”）是知名度最高、上手最简单的应用。

它售价便宜（美区 App Store 仅需 $2.99），且功能极其全面：全面支持二维码一键扫码导入、订阅 URL 自动同步、规则分流、延迟测试以及全局路由设置，是苹果手机小白用户的必备工具。

## 2. 3 步保姆级安装与订阅导入教程

### 步骤 1：切换美区 Apple ID 并下载小火箭
由于政策原因，中国区 App Store 无法搜索到小火箭。
1. 在 iPhone 的 App Store 中退出当前大陆账号，登录一个非中国区（如美区、港区）的 Apple ID。
2. 搜索 “Shadowrocket”，确认开发者为 *Shadowrocket Limited*，完成购买与下载。

### 步骤 2：一键导入机场订阅链接
1. 注册并登录专线机场后台（首推 [灵动云](/providers/lingdong-cloud/) 或 [飞猫云](/providers/flycat-cloud/)）。
2. 在用户控制台点击“一键导入 Shadowrocket”或“复制订阅链接”。
3. 打开小火箭软件，点击右上角 **“+” 号**：
   - 类型选择 **Sub / Subscribe**；
   - 在 URL 栏粘贴步骤2复制的链接，备注填入机场名称，点击右上角“保存”。

### 步骤 3：测速、选择节点与开启代理
1. 保存后，小火箭会自动拉取节点列表。点击“连通性测试”，测试所有节点的延迟。
2. 勾选一个绿色低延迟节点，将全局路由保持为 **“配置” (Config / 规则模式)**。
3. 开启最上方的 **“未连接”** 开关，在系统弹出的 VPN 权限提示中点击“允许”并验证 Face ID / 指纹，即可完成连线！

{get_top4_block()}

## 3. 小火箭日常使用故障排查 FAQ

- **问题 A：扫码或导入后节点列表为空**
  *解决排查*：检查订阅链接是否完整，或在小火箭设置中将“订阅更新”开启为“打开时更新”。
- **问题 B：小火箭连线上后无法打开微信或国内网页**
  *解决排查*：确认全局路由设置为了“配置”而非“代理（全局）”。
- **问题 C：小火箭后台经常断连**
  *解决排查*：在小火箭设置中找到“按需连接” (On Demand)，开启后系统将自动维持 VPN 常驻。

## 4. 延伸阅读与相关文章
- 📱 [Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤](/clients/clash-meta-android-guide/)
- 💻 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 🍏 [Quantumult X (圈x) 基础配置教程：iOS 高阶策略与节点导入](/clients/quantumult-x-ios-guide/)
- 🔄 [多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理](/clients/multi-client-sync-subscription/)
"""
write_article("shadowrocket-ios-tutorial.md", "Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用", "客户端下载配置", ["小火箭配置", "Shadowrocket订阅", "iPhone梯子设置", "iOS小火箭", "苹果手机科学上网"], "小火箭配置,Shadowrocket订阅,iPhone梯子设置,iOS小火箭,苹果手机科学上网", "2026 最新 iPhone/iPad 小火箭 (Shadowrocket) 节点订阅导入教程。从美区 Apple ID 获取到一键扫码导入、测速与按需连接全排查。", c6_body)

# 7. Sing-box Client Guide
c7_body = f"""## 1. 什么是 Sing-box？为什么它是新一代跨平台代理神器？

**Sing-box** 是开源社区近年来异军突起的通用网络代理引擎。与传统的 Clash 核心相比，Sing-box 采用了极致优化的 Go 语言架构，具有**内存占用极低、性能极强、启动毫秒级**的优势。

最重要的是，Sing-box 是首批原生支持 **Hysteria2 (歇斯底里2)** 与 **VLESS Reality** 等新一代抗封锁协议的通用客户端，全面覆盖 Windows、macOS、Linux、Android 及 iOS 全平台。

## 2. 全平台 Sing-box 客户端使用指南

### (1) Windows / Mac 平台配置
1. 下载 Sing-box GUI 官方客户端。
2. 导入专线机场（如 [灵动云](/providers/lingdong-cloud/) 或 [暮光网络](/providers/twilight-cloud/)）提供的 Sing-box 专属 JSON 订阅链接。
3. 开启 TUN 模式或系统代理即可使用。

### (2) Android / iOS 手机端配置
1. Android 用户在 Google Play 或 GitHub 下载 Sing-box Android APK；iOS 用户在 App Store 下载 Sing-box 应用。
2. 打开软件，进入 Profiles 页面添加订阅 URL，刷新拉取节点。
3. 开启代理开关并授权系统 VPN 权限。

{get_top4_block()}

## 3. Sing-box 核心优势对比

| 对比维度 | Sing-box | 传统 Clash 核心 |
| :--- | :--- | :--- |
| **Hysteria2 原生支持** | **原生极速支持** | 部分分支支持 |
| **内存占用 (RAM)** | **仅约 30MB - 50MB** | 约 100MB - 200MB |
| **跨平台统一性** | Win/Mac/iOS/Android/Linux 全覆盖 | 需借助不同 UI 前端 |
| **极客自定义空间** | 极高 (JSON 灵活配置) | 高 (YAML 格式) |

## 4. 延伸阅读与相关教程
- 📖 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 💻 [Mac 平台代理客户端对比：Clash Verge vs Sing-box vs Stash](/clients/mac-proxy-clients-comparison/)
- 📱 [Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤](/clients/clash-meta-android-guide/)
- 🔄 [多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理](/clients/multi-client-sync-subscription/)
"""
write_article("sing-box-client-guide.md", "Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置", "客户端下载配置", ["Sing-box指南", "新一代代理工具", "Singbox配置", "全平台代理", "Hysteria2客户端"], "Sing-box指南,新一代代理工具,Singbox配置,全平台代理,Hysteria2客户端", "新一代跨平台代理神器 Sing-box 完整上手指南。解析 Hysteria2 协议支持、低内存占用优势与 Windows/Mac/iOS/Android 全平台配置。", c7_body)

# 8. Surfboard Android Tutorial
c8_body = f"""## 1. 什么是 Surfboard (冲浪板)？

**Surfboard**（中文俗称“冲浪板”）是 Android 安卓平台上口碑极佳的精致代理软件。它的设计理念高度借鉴了 iOS 上的顶级代理应用 Surge，支持兼容 Surge 3/4 的配置文件格式。

Surfboard 拥有美观优雅的 Material You UI 界面，提供极具特色的**应用分流 (App Gateway)**、可视化实时流量图表以及 Android 12+ 快捷控制面板瓷贴 (Tile Widget)。

## 2. 3 步保姆级安装与使用教程

### 步骤 1：下载安装 Surfboard APK
从 Google Play 商店或官方 GitHub Releases 页面下载最新的 Surfboard `.apk` 安装包并完成安装。

### 步骤 2：导入机场 Surge/Surfboard 订阅
1. 登录您的专线机场后台（如 [灵动云](/providers/lingdong-cloud/) 或 [飞猫云](/providers/flycat-cloud/)）。
2. 点击“一键订阅”，选择“复制 Surfboard 订阅”或“Surge 订阅”。
3. 打开 Surfboard，点击底部 **“配置” (Profile)** -> 点击右下角 **“+” 号** -> 选择 “从 URL 导入”，粘贴链接并保存。

### 步骤 3：选点与开启连接
1. 进入 **“节点” (Point)** 页面，测试节点延迟，选择一个低延迟节点。
2. 进入 **“开关” (Switch)** 页面，将代理模式保持为“规则” (Rule)。
3. 点击右下角连接按钮开启代理即可！

{get_top4_block()}

## 3. Surfboard 独家亮点功能：按应用精准分流

在 Surfboard **“设置” -> “应用分流”** 中，您可以自由选择哪些安卓 App 走代理、哪些 App 直连：
- 勾选 Telegram、Twitter、YouTube 走代理通道；
- 勾选微信、淘宝、美团走本地直连通道，彻底杜绝国内应用误走代理消耗机场流量。

## 4. 延伸阅读与相关 Android 指南
- 📱 [Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤](/clients/clash-meta-android-guide/)
- 🚀 [Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置](/clients/sing-box-client-guide/)
- 📖 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
"""
write_article("surfboard-android-tutorial.md", "Surfboard (冲浪板) 下载与使用教程：Android 平台优雅代理", "客户端下载配置", ["Surfboard下载", "冲浪板教程", "Android代理软件", "Surfboard订阅", "安卓优雅梯子"], "Surfboard下载,冲浪板教程,Android代理软件,Surfboard订阅,安卓优雅梯子", "Android 平台优雅代理应用 Surfboard (冲浪板) 下载与配置教程。图文拆解 Surge 格式订阅导入、应用分流与瓷贴设置。", c8_body)

# 9. v2rayN Download & Setup
c9_body = f"""## 1. 为什么 v2rayN 是 Windows 经典老牌客户端？

在 Clash 流行之前，**v2rayN** 始终是 Windows 平台上普及率最高、资历最老的代理软件。即使在 2026 年，更新到了 v6/v7 大版本的 v2rayN 依然凭借其纯粹的节点管理能力与极高的兼容性，被无数技术老手与小白用户使用。

它不仅支持 VMess、VLESS、Shadowsocks、Trojan，还集成了 Xray 核心与 Sing-box 核心，是测试单节点连通性的必备神器。

## 2. 保姆级图文设置步骤（1-2-3 步骤）

### 步骤 1：下载软件与运行库依赖
1. 访问 v2rayN 官方 GitHub 仓库下载 `v2rayN-With-Core.zip` 压缩包并解压。
2. **重要依赖**：Windows 电脑需安装微软 `.NET Desktop Runtime 6.0` 或更高版本运行库，否则软件双击无法启动。

### 步骤 2：添加机场订阅地址
1. 打开 `v2rayN.exe`，点击顶部菜单栏的 **“订阅分组” -> “订阅分组设置”**。
2. 点击“添加”，在“别名”处填入机场名称（如 [灵动云](/providers/lingdong-cloud/)），在“地址 (url)”处粘贴机场后台复制的 V2Ray 订阅链接，点击确定。
3. 返回主界面，点击 **“订阅分组” -> “更新订阅 (不通过代理)”**，等待下方的节点列表加载完成。

### 步骤 3：选择节点并开启系统代理
1. 在节点列表中选择一个节点，右键点击“设为活动节点”（或按 Enter 键）。
2. 在屏幕右下角任务栏托盘中，找到 v2rayN 的红色图标，右键点击：
   - **自动配置系统代理**：勾选（图标变为黄色/蓝色）；
   - **路由**：选择“绕过大陆 (Bypass mainland)”或“自定义路由规则”。

{get_top4_block()}

## 3. v2rayN 常见故障快速修复

- **图标双击没反应**：未安装微软 `.NET` 桌面运行库，下载安装后即可启动。
- **更新订阅提示 404/Timeout**：确认机场套餐有效，或点击“订阅分组”取消勾选旧配置后再试。
- **浏览器无法上网**：确认右下角图标是否已被设为“自动配置系统代理”。

## 4. 延伸阅读与相关 Windows 教程
- 📖 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 🔧 [Clash 常见报错解决：Core Path 不存在与 Config Parse Error 排查](/clients/clash-common-errors-fix/)
- 🔄 [多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理](/clients/multi-client-sync-subscription/)
"""
write_article("v2rayn-download-setup.md", "v2rayN 下载与配置教程：经典 Windows 梯子客户端保姆级设置", "客户端下载配置", ["v2rayN下载", "v2rayN配置", "Windows节点导入", "v2rayN教程", "经典V2Ray软件"], "v2rayN下载,v2rayN配置,Windows节点导入,v2rayN教程,经典V2Ray软件", "Windows 经典代理软件 v2rayN 下载、安装与配置保姆级教程。手把手解决 .NET 运行库依赖、订阅更新与路由设置。", c9_body)

# 10. Multi Client Sync Subscription
c10_body = f"""## 1. 为什么需要在多设备间高效管理一套机场订阅？

当代用户通常拥有多台上网设备（如 Windows 办公电脑、Mac 笔记本、iPhone 手机、Android 备用机或 iPad 平板）。

如果您在每台设备上单独手动输入节点，不仅操作繁琐，而且当机场更新服务器 IP 或节点域名时，多台设备容易产生节点失效不同步的问题。

掌握**多客户端同步订阅技巧**，可以用一套机场订阅在全平台设备间高效同步更新，省时省力。

## 2. 多设备高效协同的三大黄金法则

### 法则一：统一使用机场提供的“通用订阅 URL”
高品质机场（如 [灵动云](/providers/lingdong-cloud/)、[暮光网络](/providers/twilight-cloud/) 和 [飞猫云](/providers/flycat-cloud/)）后台通常提供智能聚合订阅 URL。无论您在 Windows 端使用 Clash Verge，还是在 iPhone 端使用小火箭，只需粘贴同一个订阅 URL，机场后台会自动根据请求头 (User-Agent) 返回适配该软件的格式。

### 法长二：合理利用 Sub-Converter 订阅转换
如果您使用的软件（如老版客户端）不支持机场的原生订阅格式，可以使用开源码的 **Sub-Converter (订阅转换器)**。将原始链接一键转换为 Clash、Sing-box、Quantumult X 或 Surge 格式。

### 法则三：开启软件“启动时自动更新订阅”
在 Windows Clash Verge、Android Flclash 及 iOS 小火箭中，均开启“启动时更新” (Update on Startup) 选项。每次打开软件时自动拉取最新节点，彻底告别节点失效。

{get_top4_block()}

## 3. 多设备使用机场的流量与设备数防坑提醒

1. **核对套餐允许的最高同时在线设备数**：普通套餐通常限制 3-5 台设备同时在线。若多台设备同时连线超出限制，可能会导致部分设备暂时被断连。
2. **区分设备流量消耗**：电脑端观看 4K 视频流量消耗远高于手机端，建议在主设备上选择高流量或低倍率节点。
3. **安全提示**：切勿将您的私人机场订阅链接公开发布在社交网络，防止流量被他人盗刷。

## 4. 延伸阅读与全平台客户端教程
- 📖 [Clash Verge 小白上手指南：2026 Windows/Mac 最佳科学上网客户端](/clients/clash-verge-guide/)
- 🚀 [Shadowrocket (小火箭) 节点订阅导入教程：iPhone/iPad 必备应用](/clients/shadowrocket-ios-tutorial/)
- 📱 [Clash Meta (Flclash) 安卓版配置教程：手机极速连线图文步骤](/clients/clash-meta-android-guide/)
- 🛠️ [Sing-box 客户端保姆级指南：通用跨平台新一代代理工具配置](/clients/sing-box-client-guide/)
"""
write_article("multi-client-sync-subscription.md", "多客户端同步订阅技巧：一套机场订阅在多台设备上的高效管理", "客户端下载配置", ["多客户端同步", "机场订阅管理", "多设备协同", "订阅共享", "Sub-converter转换"], "多客户端同步,机场订阅管理,多设备协同,订阅共享,Sub-converter转换", "高效多设备管理技巧：教您如何用一套机场订阅在 PC、Mac、iPhone、Android 多端实现节点自动同步与更新。", c10_body)

print("Generated all 10 long-form Client Download & Configuration articles successfully!")
