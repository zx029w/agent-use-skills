---
name: ppt-generator
description: 将用户讲稿一键生成乔布斯风极简科技感HTML演示稿。支持横屏全屏自适应模式。触发场景：(1) 用户需要生成PPT、演示文稿、Slides、幻灯片；(2) 要求科技风/极简风/乔布斯风格的演示；(3) 需要将文档/讲稿转换为演示用HTML；(4) 美化现有PPT内容。输出为单个可直接运行的HTML文件。
---

# PPT Generator

将讲稿转换为乔布斯风极简科技感HTML演示稿。

## 设计哲学

- **极简主义** - 一页只讲一件事
- **强视觉对比** - 深色背景 + 白色文字
- **高留白** - 禁止密集排版
- **强节奏感** - 让观众想继续看

## 生成流程

### Step 1: 读取讲稿
读取用户原始讲稿或文档内容。

### Step 2: 提炼内容
将内容精简、增强冲击力、适配演示场景。输出 Markdown 格式的提炼版讲稿。

### Step 3: 生成标题
为每个章节生成标题：
- ≤12 字
- 形式：对比式、问题式、断言式、数字式、比喻式

### Step 4: 设计结构
规划页面顺序和类型，参考 [references/slide-types.md](references/slide-types.md)。

### Step 5: 生成HTML
使用 [assets/template.html](assets/template.html) 作为基础，生成完整HTML。

### Step 6: 输出
依次输出：
1. 提炼后的讲稿（Markdown）
2. 幻灯片结构大纲
3. 完整HTML代码

## 视觉规范

| 项目 | 规范 |
|------|------|
| 布局 | 横屏全屏自适应，100vw × 100vh |
| 背景 | #000000 或 #0a0a0a + 模糊光斑动画 |
| 主文字 | #ffffff |
| 辅助文字 | #9ca3af / rgba(255,255,255,0.5) |
| 中文字体 | Noto Sans SC / 思源黑体 |
| 英文字体 | Inter |
| 标题字重 | 700-900 |
| 正文字重 | 300-400 |

详细规范见 [references/design-spec.md](references/design-spec.md)。

## 布局要点

### 三栏卡片（必须等宽）
```html
<div style="display: flex; justify-content: center; gap: 50px; width: 100%;">
  <div class="card" style="width: 380px; min-width: 380px;">...</div>
  <div class="card" style="width: 380px; min-width: 380px;">...</div>
  <div class="card" style="width: 380px; min-width: 380px;">...</div>
</div>
```
- 使用 flexbox + 固定宽度确保三栏严格等宽
- 避免 grid 导致的内容撑开宽度不一致

### 左右布局（数字+内容）
```html
<div style="display: flex; align-items: center; gap: 30px;">
  <span style="min-width: 70px;">01</span>
  <div style="display: flex; flex-direction: column; justify-content: center; text-align: left;">
    <p>标题</p>
    <p>说明</p>
  </div>
</div>
```
- 左侧固定宽度，右侧 flex column 居左
- 右侧需要 `justify-content: center` 垂直居中

## 交互要求

- 键盘 ← → 或空格翻页
- 底部进度导航条
- 触摸滑动支持
- 平滑切换动画

## 技术栈

- TailwindCSS（国内CDN）
- 原生JavaScript
- 单个HTML文件，可直接打开运行

## 严禁行为

- 堆字、密集排版
- 花哨配色
- 复杂图表
- grid 三栏不指定宽度（会导致不等宽）
- 偏离极简科技风

## 默认规则

- 未指定页数：自动生成 8~15 页
- 未指定风格：默认乔布斯风极简科技感
- 字体使用内联样式确保全屏适配