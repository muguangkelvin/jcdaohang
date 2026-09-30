# SEO Profile Replacement Contract

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
