# 📰 Awesome Gaussians - 项目更新日志

本文件记录 Awesome Gaussians 的重要功能更新、Bug 修复和内容改进。

---

## 🔧 2026-08-08 - arXiv 定时更新可靠性修复

### 🐛 问题

arXiv API 在限流、服务器错误或网络超时时，会导致定时 GitHub Actions 失败，并存在空数据覆盖有效历史数据的风险。

### 💡 解决方案

- 统一使用 `https://export.arxiv.org/api/query`
- 设置明确的 User-Agent，并对 `429`、`5xx` 和连接超时进行有限重试
- 优先遵循 `Retry-After`，否则使用 10/30/60 秒退避
- 为搜索命令增加稳定退出码：`0` 成功、`3` 无结果、`75` 临时故障、`1` 真实错误
- 只有非空且结构有效的 JSON 才会通过临时文件原子替换写入
- README 生成时忽略空文件和损坏文件，回退到最近的有效非空数据
- GitHub Actions 使用 `jq` 验证数据结构；临时故障时保留旧数据、跳过 README 和提交，并在 Job Summary 输出 warning

### ✅ 验证结果

- arXiv 临时不可用时不再污染数据，也不会错误改写 README
- 配置、解析和程序错误仍会正常使工作流失败
- 14 项自动化测试通过，包括限流、超时、服务器错误、空结果及 README 数据回退

---

## 📚 2026-08-08 - 收录社区推荐论文

根据 [Issue #3](https://github.com/longxiang-ai/awesome-gaussians/issues/3) 的建议，手动收录 STAG 2024 论文：

- [A Study on the Use of High Dynamic Range Imaging for Gaussian Splatting Methods: Are 8 Bits Enough?](https://doi.org/10.2312/stag.20241341)
- 作者：Valentina Piras, Amedeo F. Bonatti, Carmelo De Maria, Paolo Cignoni, Francesco Banterle
- 主题：HDR、色调映射、3D Gaussian Splatting

该条目保存在 README 模板中，后续自动生成 README 时不会被覆盖。

---

## 🚀 2026-02 - v2.0 主要功能更新

- 新增统一 CLI 入口 `main.py`，支持 `init`、`search`、`suggest`、`export-bib` 和 `readme`
- 新增交互式配置向导
- 支持相对和绝对时间范围过滤
- 新增论文链接自动提取与分类
- 新增 BibTeX 导出、LLM 关键词建议及 arXiv 分类过滤

---

## 🛠️ 2025-06-26 - 历史更新

### HTTP 301 重定向处理

当时通过直接请求 API、手动解析 XML 和降级策略缓解了 arXiv 重定向问题。该 HTTP 绕行方案已于 2026-08-08 被统一 HTTPS 端点与新的有限重试机制取代。

### 可配置搜索关键词

- 支持通过 `data/search_config.json` 自定义关键词
- 支持摘要、标题或两者联合搜索
- 提供配置验证工具 `scripts/validate_search_config.py`

---

## 📋 后续计划

### 优先级高

- [ ] GitHub 链接检测优化
- [ ] 引用数获取功能增强
- [ ] 论文质量评分系统

### 优先级中

- [ ] 多语言摘要支持
- [ ] 自定义输出格式
- [ ] 数据可视化界面

### 优先级低

- [ ] 机器学习论文推荐
- [ ] 社交媒体集成
- [ ] API 接口开发

---

## 📝 维护说明

本文件在每次重要功能更新时维护，包括：

- 🎉 重大功能发布
- 🐛 重要 Bug 修复
- 🔧 性能与稳定性改进
- 📚 文档和内容更新

---

*最后更新：2026-08-08*  
*项目地址：[awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians)*
