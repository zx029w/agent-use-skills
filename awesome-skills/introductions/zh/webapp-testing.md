# Webapp Testing

**Webapp Testing** 是一个旨在使用 Playwright 交互和测试本地 Web 应用程序的强大工具包。

## 标签

💻 开发与测试 | 🔍 待验证

## 核心理念
- 提供自动化的服务器生命周期管理（支持单服务器和多服务器架构）。
- 使用原生 Python Playwright 脚本进行可靠的本地 Web 测试。
- 提倡侦察-执行（Reconnaissance-then-action）模式处理动态 Web 应用。
- 提供开箱即用的黑盒辅助脚本，避免冗长的上下文污染。

## 主要功能与工作流
1. **静态 HTML 测试**: 直接读取本地 HTML 文件，识别 DOM 选择器并编写 Playwright 脚本进行交互。
2. **动态 Web 应用测试**: 通过提供的 `with_server.py` 辅助脚本，自动启动并管理目标服务器（如 `npm run dev`）。
3. **多服务共管**: 支持同时拉起前端和后端服务器进行端到端全链路测试。
4. **侦察-执行流**: 
   - 导航并等待页面完成网络请求 (`networkidle`)。
   - 通过屏幕截图或 DOM 检查识别目标元素。
   - 使用获取的选择器执行精确操作。

## 技能库概览
- **服务器辅助脚本**: 提供 `with_server.py` 高效托管目标进程。
- **示例预设**: 包含常见自动化模式的示例：探索元素（`element_discovery.py`）、静态网页控制（`static_html_automation.py`）及控制台日志抓取（`console_logging.py`）。

## 安装与支持
Webapp Testing 支持以下平台：
- [Claude Code](../../claudecode/webapp-testing/INSTALL-zh.md)
- [Cursor](../../cursor/webapp-testing/INSTALL-zh.md)
- [Codex](../../codex/webapp-testing/INSTALL-zh.md)
- [OpenCode](../../opencode/webapp-testing/INSTALL-zh.md)
- [OpenClaw](../../openclaw/webapp-testing/INSTALL-zh.md)
- [Qoder](../../qoder/webapp-testing/INSTALL-zh.md)

---
获取更多信息，请访问：[GitHub - anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/webapp-testing)
