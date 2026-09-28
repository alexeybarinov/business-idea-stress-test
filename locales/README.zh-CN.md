<div align="center">

<img src="../assets/icon.png" alt="Business Idea Stress Test 图标" width="110">

# Business Idea Stress Test

**先严格验证商业创意，再投入大量时间和资金**

一款开源 Agent Skill，帮助创业者对商业创意进行**一次性、有证据支持的压力测试**

[English](../README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt-BR.md) · [日本語](README.ja.md)

[安装指南](../docs/installation.md) · [快速入门](../docs/quickstart.md) · [最新版本](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest)
</div>

> **语言说明：**本页提供简体中文介绍。核心 `SKILL.md` 用英文编写，但技能会根据使用者的语言作答。完整的平台安装说明目前使用英文

## 解决什么问题？

有些创业想法听起来很有吸引力，但尚未证明客户愿意付费，也没有计算获客成本、交付能力和潜在风险。本技能不是自动赞同想法或生成乐观的商业计划，而是提出尖锐问题、查找反面证据，并明确区分事实、估算和未经验证的假设

目标是找出**是否值得进行下一步真实测试，以及应该先验证什么**，而不是预测企业一定会成功或失败

## 六个分析阶段

1. **创始人访谈：**逐步厘清产品、客户、付款人、目标地区、预算及限制。通常一次只问一个关键问题
2. **初步验证：**找出核心假设、现有替代方案和可能阻碍项目的关键问题
3. **外部研究：**在工具允许时调查市场需求、客户行为、直接和间接竞争者，并记录资料来源和日期
4. **财务与运营分析：**列出关键成本、收入逻辑、单位经济模型、现金需求及基于明确假设的不同情景
5. **反方审查：**从潜在客户、竞争者、财务和运营角度提出有依据的反驳
6. **结论与低成本实验：**整理证据缺口，设计可衡量、预算有限且有停止条件的测试

单个模型模拟多个视角并不等于独立专家团队。没有浏览能力时，技能必须明确说明无法核实的数据，不得编造访谈、价格或市场统计

## 安装方法

**ChatGPT：**从 [Releases](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest) 下载带版本号的专用技能 ZIP。在支持该功能的账户中进入 **Plugins → Skills → Create → Upload from your computer**。不要使用 GitHub 自动生成的源码 ZIP。实际可用性取决于账户和工作区

**Codex：**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a codex
```

**Claude Code：**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a claude-code
```

**Gemini CLI：**

```bash
gemini skills install https://github.com/alexeybarinov/business-idea-stress-test.git
```

Cursor、GitHub Copilot、OpenCode、Claude.ai 等平台及手动安装方式请参阅[英文完整安装指南](../docs/installation.md)。`-g` 表示面向当前用户的全局安装。只有使用 `npx` 安装时才需要 Node.js；技能本身无需运行 Python 或付费 API

## 第一次使用

每个独立的商业创意建议使用新对话。安装后明确要求助手启用此技能：

```text
使用 Business Idea Stress Test。我的商业创意是：[描述]。
先向我逐个提出最重要的问题，再研究市场。
不要为了鼓励我而忽视风险；请注明每项关键结论的证据或未知部分
```

你可以回答“我不知道”。如果有竞争者网站、客户访谈或实际报价，可以提供给助手，并说明国家和资料日期。最终报告应给出关键风险、透明的财务假设，以及成本可控的真实测试方案

**隐私提示：**不要提供密码、客户个人数据或没有权限分享的保密材料。涉及重大法律或投资事项时，请咨询相应专业人士

## 版本与致谢

[更新日志](../CHANGELOG.md) · [版本下载](https://github.com/alexeybarinov/business-idea-stress-test/releases)。通过 `npx` 全局安装的用户可尝试 `npx skills update business-idea-stress-test -g`；手动上传的版本通常需要重新上传 ZIP

感谢 [Matt Pocock](https://github.com/mattpocock/skills)、[BuildGreatProducts](https://github.com/BuildGreatProducts/builder-os)、[xcrrr](https://github.com/xcrrr/claude-skills)、[Corey Haines](https://github.com/coreyhaines31/marketingskills)、[sickn33](https://github.com/sickn33/agentic-awesome-skills) 和 [jukeyman](https://github.com/jukeyman/jukeyman-skills) 分享启发本项目的方法。本项目独立开发，不代表上述作者的认可。完整来源见[英文致谢](../README.md#-standing-on-the-shoulders-of-the-community)

本项目原创文件采用 [MIT 许可证](../LICENSE)
