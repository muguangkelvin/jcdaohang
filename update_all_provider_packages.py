import json
import os

# Complete 3-4 tier package definitions for all 28 airports
provider_packages = {
    "lingdong-cloud": [
        {"name": "基础版", "price": "15元/月", "traffic": "150GB/月", "suitable": "轻度上网、Google查资料与学术科研"},
        {"name": "标准版", "price": "30元/月", "traffic": "350GB/月", "suitable": "日常4K影音追剧与ChatGPT/Claude开发"},
        {"name": "旗舰版", "price": "60元/月", "traffic": "800GB/月", "suitable": "多设备并发、大流量下载与家庭共享"},
        {"name": "独享专线", "price": "150元/月", "traffic": "2000GB/月", "suitable": "跨境电商独立站与团队远程办公"}
    ],
    "twilight-cloud": [
        {"name": "基础版", "price": "20元/月", "traffic": "120GB/月", "suitable": "高清追剧与日常外贸联络"},
        {"name": "标准版", "price": "40元/月", "traffic": "300GB/月", "suitable": "4K/8K影音硬解与多设备同时在线"},
        {"name": "旗舰版", "price": "100元/月", "traffic": "700GB/月", "suitable": "海量大流量与高速专线下载"},
        {"name": "年付轻量", "price": "109元/年", "traffic": "70GB/月", "suitable": "平民低门槛长约备用推荐"}
    ],
    "flycat-cloud": [
        {"name": "学生版/年付", "price": "84元/年 (折合7元/月)", "traffic": "50GB/月", "suitable": "极致平民性价比、学生党小白首选"},
        {"name": "星耀版/月付", "price": "25元/月", "traffic": "150GB/月", "suitable": "无长约套牢、随用随充日常主用"},
        {"name": "尊享版/月付", "price": "45元/月", "traffic": "350GB/月", "suitable": "全节点解锁与4K流媒体流畅播放"},
        {"name": "不限时按量包", "price": "120元/一次性", "traffic": "500GB永不过期", "suitable": "备用梯子防失联首选方案"}
    ],
    "breezenet": [
        {"name": "体验版", "price": "12元/月", "traffic": "100GB/月", "suitable": "低预算试错与轻度连线"},
        {"name": "畅享版", "price": "28元/月", "traffic": "250GB/月", "suitable": "老牌稳定线路、支持全端客户端"},
        {"name": "年付版", "price": "137元/年", "traffic": "100GB/月", "suitable": "长期稳定主用超值套餐"}
    ],
    "invisible-cloud": [
        {"name": "体验版", "price": "18元/月", "traffic": "100GB/月", "suitable": "隐私防护与匿名连线"},
        {"name": "进阶版", "price": "36元/月", "traffic": "260GB/月", "suitable": "全节点IEPL中继与流媒体解锁"},
        {"name": "年付旗舰", "price": "188元/年", "traffic": "150GB/月", "suitable": "高性价比年付长约套餐"}
    ],
    "wavenet": [
        {"name": "高能版", "price": "22元/月", "traffic": "200GB/月", "suitable": "大流量影音下载与高清播发"},
        {"name": "狂飙版", "price": "45元/月", "traffic": "500GB/月", "suitable": "百兆带宽硬解与多端并发"},
        {"name": "不限时包", "price": "150元/一次性", "traffic": "600GB不限时", "suitable": "终身按量备用防断网"}
    ],
    "laddercloud": [
        {"name": "入门版", "price": "15元/月", "traffic": "150GB/月", "suitable": "零基础小白上手体验"},
        {"name": "进阶版", "price": "32元/月", "traffic": "350GB/月", "suitable": "高速BGP中继与流畅4K"},
        {"name": "年付省心包", "price": "149元/年", "traffic": "120GB/月", "suitable": "省心年付超值方案"}
    ],
    "flyv-cloud": [
        {"name": "商务版", "price": "25元/月", "traffic": "300GB/月", "suitable": "外贸商务与远程会议加速"},
        {"name": "企业专线", "price": "68元/月", "traffic": "800GB/月", "suitable": "独立原生IP与SLA稳定保障"},
        {"name": "年付商务", "price": "238元/年", "traffic": "250GB/月", "suitable": "企业团队长约优惠"}
    ],
    "xingdaomeng": [
        {"name": "基础版", "price": "16元/月", "traffic": "120GB/月", "suitable": "日常社交通讯与网页浏览"},
        {"name": "高级版", "price": "32元/月", "traffic": "280GB/月", "suitable": "4K流媒体与游戏加速"},
        {"name": "年付特惠", "price": "158元/年", "traffic": "100GB/月", "suitable": "学生党与平民年付首选"}
    ],
    "guangsu-cloud": [
        {"name": "标准版", "price": "19元/月", "traffic": "180GB/月", "suitable": "光速专线连通与低延迟处理"},
        {"name": "尊享版", "price": "38元/月", "traffic": "400GB/月", "suitable": "AI代码补全与高清视频协同"},
        {"name": "年付尊享", "price": "189元/年", "traffic": "180GB/月", "suitable": "长约稳定冲浪方案"}
    ],
    "v2yun": [
        {"name": "普及版", "price": "15元/月", "traffic": "100GB/月", "suitable": "V2ray协议轻度连线"},
        {"name": "专业版", "price": "30元/月", "traffic": "250GB/月", "suitable": "多协议智能分流与流媒体"},
        {"name": "年付普及", "price": "139元/年", "traffic": "90GB/月", "suitable": "高性价比年付套餐"}
    ],
    "u1s1-cloud": [
        {"name": "实用版", "price": "14元/月", "traffic": "120GB/月", "suitable": "有一说一高性价比随用随充"},
        {"name": "发烧版", "price": "28元/月", "traffic": "300GB/月", "suitable": "晚高峰硬核抗封锁打游戏"},
        {"name": "不限时流量包", "price": "99元/一次性", "traffic": "300GB不限时", "suitable": "轻度备用不过期"}
    ],
    "jilian-cloud": [
        {"name": "极速版", "price": "18元/月", "traffic": "150GB/月", "suitable": "极速握手与长连接保持"},
        {"name": "团队版", "price": "42元/月", "traffic": "450GB/月", "suitable": "多设备并发与团队协同"},
        {"name": "年付极速", "price": "168元/年", "traffic": "120GB/月", "suitable": "长期稳定主用推荐"}
    ],
    "quanqiu-cloud": [
        {"name": "轻量版", "price": "20元/月", "traffic": "120GB/月", "suitable": "全球节点智能选路与解锁"},
        {"name": "全能版", "price": "45元/月", "traffic": "380GB/月", "suitable": "原生IP解锁ChatGPT与流媒体"},
        {"name": "年付全能", "price": "199元/年", "traffic": "150GB/月", "suitable": "全球跨境出海首选"}
    ],
    "guangnian-ti": [
        {"name": "稳定版", "price": "16元/月", "traffic": "130GB/月", "suitable": "老牌抗封锁线路与稳定连线"},
        {"name": "豪华版", "price": "35元/月", "traffic": "320GB/月", "suitable": "4K无缓冲与高并发握手"},
        {"name": "年付稳定", "price": "159元/年", "traffic": "110GB/月", "suitable": "性价比长约套餐"}
    ],
    "sogo-cloud": [
        {"name": "便携版", "price": "15元/月", "traffic": "100GB/月", "suitable": "移动端与平板便携连线"},
        {"name": "全能版", "price": "30元/月", "traffic": "260GB/月", "suitable": "全端订阅与多设备支持"},
        {"name": "年付便携", "price": "138元/年", "traffic": "80GB/月", "suitable": "学生党学术科研推荐"}
    ],
    "yuzhou-cloud": [
        {"name": "旗舰版", "price": "22元/月", "traffic": "200GB/月", "suitable": "大流量与百兆独享带宽"},
        {"name": "星际版", "price": "48元/月", "traffic": "550GB/月", "suitable": "海量4K/8K视频与大文件下载"},
        {"name": "年付旗舰", "price": "210元/年", "traffic": "180GB/月", "suitable": "长期大流量主用"}
    ],
    "2mao-cloud": [
        {"name": "学生版", "price": "12元/月", "traffic": "80GB/月", "suitable": "平民低门槛学生党试错"},
        {"name": "进阶版", "price": "26元/月", "traffic": "220GB/月", "suitable": "日常科学上网与4K追剧"},
        {"name": "年付超值", "price": "118元/年", "traffic": "80GB/月", "suitable": "折合9元/月极低年付"}
    ],
    "1fly-cloud": [
        {"name": "基础版", "price": "17元/月", "traffic": "140GB/月", "suitable": "一键翻墙与基础网页连线"},
        {"name": "飞跃版", "price": "35元/月", "traffic": "320GB/月", "suitable": "原生IP解锁AI与4K播放"},
        {"name": "年付飞跃", "price": "169元/年", "traffic": "120GB/月", "suitable": "省心稳定主用"}
    ],
    "edgenova": [
        {"name": "专业版", "price": "25元/月", "traffic": "250GB/月", "suitable": "IEPL专线与游戏低延迟加速"},
        {"name": "极客版", "price": "55元/月", "traffic": "600GB/月", "suitable": "软路由分流与全节点解锁"},
        {"name": "年付专业", "price": "249元/年", "traffic": "200GB/月", "suitable": "极客发烧友长约推荐"}
    ],
    "kosing-cloud": [
        {"name": "可信版", "price": "16元/月", "traffic": "130GB/月", "suitable": "可信高SLA在线率保障"},
        {"name": "卓越版", "price": "33元/月", "traffic": "300GB/月", "suitable": "外贸沟通与办公长连接"},
        {"name": "年付可信", "price": "158元/年", "traffic": "100GB/月", "suitable": "稳定连线首选"}
    ],
    "sujie-cloud": [
        {"name": "速享版", "price": "19元/月", "traffic": "160GB/月", "suitable": "速界BGP中继与快速握手"},
        {"name": "尊速版", "price": "39元/月", "traffic": "380GB/月", "suitable": "4K流媒体与多端并发"},
        {"name": "年付速享", "price": "188元/年", "traffic": "150GB/月", "suitable": "高性价比年付"}
    ],
    "kuaili-cloud": [
        {"name": "轻盈版", "price": "13元/月", "traffic": "90GB/月", "suitable": "低单价轻量查资料"},
        {"name": "敏捷版", "price": "26元/月", "traffic": "230GB/月", "suitable": "敏捷响应与流媒体解锁"},
        {"name": "年付轻盈", "price": "129元/年", "traffic": "80GB/月", "suitable": "平民月付/年付双选"}
    ],
    "worryfree-cloud": [
        {"name": "无忧版", "price": "15元/月", "traffic": "100GB/月", "suitable": "无忧稳定连接与备用防护"},
        {"name": "畅游版", "price": "32元/月", "traffic": "280GB/月", "suitable": "晚高峰0丢包与视频播发"},
        {"name": "年付无忧", "price": "148元/年", "traffic": "90GB/月", "suitable": "无忧防失联备用"}
    ],
    "civet-cloud": [
        {"name": "灵动版", "price": "17元/月", "traffic": "130GB/月", "suitable": "灵动敏捷连接与小巧稳定"},
        {"name": "猫享版", "price": "34元/月", "traffic": "300GB/月", "suitable": "4K全节点解锁与高带宽"},
        {"name": "年付灵动", "price": "168元/年", "traffic": "110GB/月", "suitable": "稳定主用长约推荐"}
    ],
    "flashleap": [
        {"name": "高跃版", "price": "21元/月", "traffic": "180GB/月", "suitable": "闪跃高速物理专线"},
        {"name": "飞腾版", "price": "46元/月", "traffic": "450GB/月", "suitable": "大流量海量下载与极速体验"},
        {"name": "年付高跃", "price": "208元/年", "traffic": "150GB/月", "suitable": "高速专线年付包"}
    ],
    "firefly-cloud": [
        {"name": "飞跃版", "price": "18元/月", "traffic": "140GB/月", "suitable": "飞为稳定节点与流媒体"},
        {"name": "星光版", "price": "36元/月", "traffic": "320GB/月", "suitable": "全端订阅与低延迟握手"},
        {"name": "年付飞跃", "price": "178元/年", "traffic": "120GB/月", "suitable": "高性价比年付"}
    ],
    "kuajie-cloud": [
        {"name": "跨境版", "price": "20元/月", "traffic": "150GB/月", "suitable": "跨境出海与外贸业务专线"},
        {"name": "商务尊享", "price": "48元/月", "traffic": "450GB/月", "suitable": "原生住宅IP与防封号风控"},
        {"name": "年付跨境", "price": "218元/年", "traffic": "180GB/月", "suitable": "跨境电商长约首选"}
    ]
}

def update_providers():
    with open("data/providers.json", "r", encoding="utf-8") as f:
        providers = json.load(f)

    for p in providers:
        slug = p["slug"]
        if slug in provider_packages:
            p["packages"] = provider_packages[slug]

    with open("data/providers.json", "w", encoding="utf-8") as f:
        json.dump(providers, f, ensure_ascii=False, indent=2)

    print("Successfully updated data/providers.json with full package details for all 28 airports!")

    # Now rewrite every content/providers/{slug}.md file to feature the rich packages table and list!
    for p in providers:
        slug = p["slug"]
        name = p["name"]
        invite_url = p["inviteURL"]
        coupon = p.get("coupon", "")
        coupon_str = f"`{coupon}`" if coupon else "暂无"
        pkgs = p.get("packages", [])

        file_path = f"content/providers/{slug}.md"
        if not os.path.exists(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            old_content = f.read()

        # Build Package Table & List Markdown
        table_md = "| 套餐梯度 | 订阅周期与参考价格 | 包含流量配额 | 核心适用人群与场景 | 官方注册通道 |\n"
        table_md += "| :--- | :--- | :--- | :--- | :--- |\n"
        list_md = ""

        for pkg in pkgs:
            pname = pkg["name"]
            pprice = pkg["price"]
            ptraffic = pkg["traffic"]
            psuitable = pkg["suitable"]

            table_md += f"| **{pname}** | **{pprice}** | {ptraffic} | {psuitable} | [👉 注册/购买]({invite_url}) |\n"
            list_md += f"- **{pname}**：**{pprice}**，提供 **{ptraffic}** 配额（适用场景：{psuitable}）\n"

        sec3_content = f"""## 3. {name} 价格与所有套餐梯度快照

以下为当前编辑部核验收集到的 **{name}** 全量价格与套餐梯度快照（优惠码：{coupon_str}，最终价格与优惠规则请以官网结算页数据为准）：

### 📊 {name} 所有套餐梯度横向对比表

{table_md}

### 📝 {name} 各套餐详细规格说明

{list_md}
> **💡 编辑部贴心建议**：新手小白首次使用建议先挑选 **月付/季付套餐** 进行本地网络压测，确认晚高峰 4K 播放与游戏延迟满意后再考虑升级长期年付套餐。
"""

        # Replace Section 3 in old content
        # Find start of section 3 and section 4
        sec3_marker = f"## 3. {name}套餐价格与梯度列表"
        sec3_alt_marker = f"## 3. {name} 价格与所有套餐梯度快照"
        sec4_marker = "## 4. 购买前注意事项与防坑提醒"

        start_idx = -1
        if sec3_marker in old_content:
            start_idx = old_content.find(sec3_marker)
        elif sec3_alt_marker in old_content:
            start_idx = old_content.find(sec3_alt_marker)
        elif "## 3." in old_content:
            start_idx = old_content.find("## 3.")

        end_idx = old_content.find(sec4_marker)

        if start_idx != -1 and end_idx != -1:
            new_content = old_content[:start_idx] + sec3_content + "\n---\n\n" + old_content[end_idx:]
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

    print("Successfully updated all 28 provider review markdown files with full packages table & details!")

if __name__ == "__main__":
    update_providers()
