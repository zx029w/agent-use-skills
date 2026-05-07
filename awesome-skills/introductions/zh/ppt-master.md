# PPT Master

**PPT Master** 是一款 AI 驱动的多格式内容生成系统，可将 PDF、DOCX、URL、Markdown 等源文档转换为原生可编辑的 PPTX 演示文稿——每个形状、文本框、图表都是真实的 PowerPoint 元素，可直接点击修改。

## 标签

🗂️ 文档与办公 | 🔍 待验证

## 核心理念
- **真正的 PowerPoint**：输出的是真实的 DrawingML 形状、文本框和图表，而非图片嵌入。每个元素都可在 PowerPoint 中直接点击编辑。
- **成本透明可控**：工具本身免费开源（MIT 协议），唯一成本是 AI 模型用量，无额外订阅费用。
- **数据不出本地**：除与 AI 模型的通信外，全流程在本地机器上运行，文件无需上传至第三方服务器。
- **不锁定平台**：支持 Claude Code、Cursor、VS Code Copilot 等多种 AI IDE，兼容 Claude、GPT、Gemini、Kimi 等主流模型。

## 主要功能与工作流
1. **多格式输入**：支持 PDF、DOCX、XLSX、PPTX、URL（含微信公众号）、Markdown 等多种源文档格式。
2. **七步串行流水线**：`源文档处理 → 项目初始化 → 模板选择 → 策划阶段（八大确认） → AI 配图 → SVG 执行生成 → 后处理与 PPTX 导出`。
3. **原生可编辑输出**：通过 SVG 中间格式生成真实的 PowerPoint 形状和文本，支持 Office 2016+ 直接打开编辑。
4. **动画与转场支持**：导出的 PPTX 支持页间转场和页内元素入场动画（真实 OOXML 动画，非嵌入视频）。
5. **AI 配图**（可选）：支持 OpenAI、Gemini 等多家图像生成后端，自动为幻灯片生成配图。
6. **多种画布格式**：支持 PPT 16:9、PPT 4:3、小红书、微信朋友圈等 10+ 种画布格式。
7. **自定义模板**：提供独立的模板创建工作流，可构建品牌或行业专属模板。

## 技能库概览
- **源文档转换脚本**：`pdf_to_md.py`、`doc_to_md.py`、`excel_to_md.py`、`ppt_to_md.py`、`web_to_md.py` 等，覆盖主流文档格式。
- **项目与质量管控**：`project_manager.py`（项目初始化/验证）、`svg_quality_checker.py`（SVG 质量检查）、`finalize_svg.py`（SVG 后处理）。
- **图像处理**：`image_gen.py`（多提供商 AI 生图）、`analyze_images.py`（图片分析）。
- **导出与交付**：`svg_to_pptx.py`（导出 PPTX）、`total_md_split.py`（演讲笔记拆分）。
- **独立工作流**：`create-template`（创建自定义模板）、`verify-charts`（图表坐标校准）。

## 安装与支持
PPT Master 支持以下 AI 编辑器和平台：
- [Claude Code](../../claudecode/ppt-master/INSTALL-zh.md)
- [Cursor](../../cursor/ppt-master/INSTALL-zh.md)
- [Codex](../../codex/ppt-master/INSTALL-zh.md)
- [OpenCode](../../opencode/ppt-master/INSTALL-zh.md)
- [OpenClaw](../../openclaw/ppt-master/INSTALL-zh.md)
- [Qoder](../../qoder/ppt-master/INSTALL-zh.md)

---
获取更多信息，请访问：[GitHub - hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
