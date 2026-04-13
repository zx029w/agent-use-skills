# Obsidian Skills

**Obsidian Skills** 是一套专为 Obsidian 知识管理工具设计的 Agent Skills，遵循 [Agent Skills 规范](https://agentskills.io/specification)，可与 Claude Code、Codex CLI 等兼容 Skills 的 AI 编码助手配合使用。

## 标签

🛠️ 效率工具 | ✅ 已验证

## 核心理念

- **标准化**: 严格遵循 Agent Skills 规范，确保跨平台兼容性
- **模块化**: 每个 Skill 独立可用，按需组合，灵活高效
- **原生体验**: 深度集成 Obsidian 特有功能，提供原生级的使用体验
- **开发者友好**: 支持 Obsidian 插件和主题开发，提供完整的开发工具链

## 关键特性与工作流程

### 1. Obsidian Markdown 编辑
创建和编辑 Obsidian Flavored Markdown，支持：
- **Wikilinks**: 使用 `[[Note Name]]` 进行内部链接
- **Embeds**: 使用 `![[embed]]` 嵌入笔记、图片、PDF
- **Callouts**: 高亮信息展示，支持 `note`、`warning`、`tip` 等类型
- **Properties**: YAML 前置属性管理，支持标签、别名、自定义属性
- **注释与高亮**: `%%隐藏注释%%` 和 `==高亮文本==`

### 2. Obsidian Bases 数据库
创建和编辑 `.base` 文件，实现类似 Notion 的数据库功能：
- **多视图支持**: 表格、卡片、列表、地图视图
- **过滤器**: 按标签、文件夹、属性、日期筛选
- **公式**: 支持算术运算、条件逻辑、日期计算
- **汇总**: 平均值、总和、最小/最大值等统计功能

### 3. JSON Canvas 可视化
创建和编辑 `.canvas` 文件，支持无限画布：
- **节点类型**: 文本、文件、链接、分组
- **边连接**: 带标签的连接器，支持方向箭头
- **布局自由**: 负坐标支持，无限扩展的画布
- **颜色预设**: 6 种品牌色彩 + 自定义 HEX

### 4. Obsidian CLI 集成
通过命令行与 Obsidian Vault 交互：
- **笔记管理**: 创建、读取、搜索、追加内容
- **任务管理**: 待办事项列表操作
- **属性操作**: 设置和修改前置属性
- **开发调试**: 插件重载、错误捕获、截图、DOM 检查

### 5. Defuddle 网页提取
使用 Defuddle CLI 从网页提取干净的 Markdown：
- **去噪处理**: 自动移除导航、广告和杂项
- **节省 Token**: 提取核心内容，减少不必要的数据传输
- **元数据提取**: 支持标题、描述、域名等字段

## Skills 库概览

| Skill | 描述 |
|-------|------|
| **obsidian-markdown** | 创建和编辑 Obsidian Flavored Markdown (.md)，支持 wikilinks、embeds、callouts、properties |
| **obsidian-bases** | 创建和编辑 Obsidian Bases (.base)，支持视图、过滤器、公式、汇总 |
| **json-canvas** | 创建和编辑 JSON Canvas 文件 (.canvas)，支持节点、边、组、连接 |
| **obsidian-cli** | 通过 Obsidian CLI 与 Vault 交互，支持插件和主题开发 |
| **defuddle** | 使用 Defuddle 从网页提取干净的 Markdown，去除杂项节省 Token |

## 安装与支持

Obsidian Skills 支持以下 AI 编辑器和平台：

- [Claude Code](../../claudecode/obsidian/INSTALL-zh.md)
- [Cursor](../../cursor/obsidian/INSTALL-zh.md)
- [Codex CLI](../../codex/obsidian/INSTALL-zh.md)
- [OpenCode](../../opencode/obsidian/INSTALL-zh.md)
- [OpenClaw](../../openclaw/obsidian/INSTALL-zh.md)
- [OpenAgent](../../openagent/obsidian/INSTALL-zh.md)
- [Qoder](../../qoder/obsidian/INSTALL-zh.md)

---

更多信息请访问: [GitHub - kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
