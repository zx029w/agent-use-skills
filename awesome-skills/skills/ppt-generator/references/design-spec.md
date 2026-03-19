# 设计规范详细文档

## 布局规范

### 全屏自适应
- 容器：`width: 100%; height: 100vh;`
- 无固定宽度限制，无 aspect-ratio
- 内容宽度：`max-width: 1400px ~ 1600px`

### 页面容器
```css
.slide {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 80px;
  overflow: hidden;
  background: linear-gradient(135deg, #0a0a0a 0%, #000000 100%);
}
```

## 关键布局模式

### 三栏等宽卡片（重要！）
**问题**：grid 三栏不指定宽度会导致卡片宽度不一致

**解决方案**：使用 flexbox + 固定宽度
```html
<div style="display: flex; justify-content: center; gap: 50px; width: 100%;">
  <div class="card" style="width: 380px; min-width: 380px;">
    <!-- 内容 -->
  </div>
  <div class="card" style="width: 380px; min-width: 380px;">
    <!-- 内容 -->
  </div>
  <div class="card" style="width: 380px; min-width: 380px;">
    <!-- 内容 -->
  </div>
</div>
```

### 左右布局（数字 + 标题说明）
**要求**：数字在左，标题说明在右，右侧内容居左且垂直居中

```html
<div style="display: flex; align-items: center; gap: 30px; padding: 25px 35px; background: rgba(255,255,255,0.03); border-radius: 16px;">
  <span style="font-size: 42px; font-weight: 900; min-width: 70px; color: #3b82f6;">01</span>
  <div style="display: flex; flex-direction: column; justify-content: center; text-align: left;">
    <p style="font-size: 30px; font-weight: 700;">标题</p>
    <p style="font-size: 22px; font-weight: 300; color: rgba(255,255,255,0.5);">说明文字</p>
  </div>
</div>
```

**关键点**：
- 数字：`min-width` 固定宽度
- 右侧 div：`flex-direction: column; justify-content: center; text-align: left;`

## 背景效果

### 主背景
- 主色：#000000 或 #0a0a0a
- 深色渐变底色

### 动态光斑（必须包含）
每页必须包含 1~3 个模糊光斑：

```css
.light-spot {
  position: absolute;
  border-radius: 50%;
  filter: blur(150px);
  opacity: 0.25;
  pointer-events: none;
}

.spot-1 {
  width: 600px;
  height: 600px;
  background: #3b82f6;
  top: -150px;
  right: -100px;
}

.spot-2 {
  width: 500px;
  height: 500px;
  background: #8b5cf6;
  bottom: -100px;
  left: -100px;
}

.spot-3 {
  width: 400px;
  height: 400px;
  background: #06b6d4;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

## 字体加载（国内CDN）

```html
<!-- 思源黑体 -->
<link href="https://fonts.loli.net/css2?family=Noto+Sans+SC:wght@300;400;700;900&display=swap" rel="stylesheet">

<!-- Inter 英文字体 -->
<link href="https://fonts.loli.net/css2?family=Inter:wght@300;400;700;900&display=swap" rel="stylesheet">
```

## 排版层级

使用内联样式确保全屏适配：

```css
/* 超大标题 */
font-size: 72px ~ 96px;
font-weight: 900;
line-height: 1.1 ~ 1.2;
color: #ffffff;

/* 副标题 */
font-size: 36px ~ 48px;
font-weight: 300;
color: rgba(255,255,255,0.5);

/* 正文说明 */
font-size: 22px ~ 28px;
font-weight: 300;
color: rgba(255,255,255,0.5);

/* 卡片标题 */
font-size: 32px ~ 40px;
font-weight: 700;

/* 卡片正文 */
font-size: 22px ~ 24px;
font-weight: 300;
color: rgba(255,255,255,0.5);
```

## 卡片样式

```css
.card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  padding: 40px;
  transition: all 0.3s;
}

.card:hover {
  background: rgba(255,255,255,0.05);
  border-color: rgba(255,255,255,0.15);
  transform: translateY(-5px);
}
```

## 颜色规范

| 用途 | 颜色 |
|------|------|
| 主背景 | #000000 / #0a0a0a |
| 主文字 | #ffffff |
| 辅助文字 | rgba(255,255,255,0.5) |
| 强调色-蓝 | #3b82f6 |
| 强调色-紫 | #8b5cf6 |
| 强调色-青 | #06b6d4 |
| 强调色-绿 | #10b981 |

## 渐变文字

```css
.gradient {
  background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #06b6d4 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

## 切换动画

```css
.slide {
  opacity: 0;
  transform: translateX(100%);
  transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide.active {
  opacity: 1;
  transform: translateX(0);
}

.slide.prev {
  opacity: 0;
  transform: translateX(-100%);
}
```

## 进度条

```css
.progress-bar {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 14px;
  z-index: 100;
}

.dot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: rgba(255,255,255,0.3);
  cursor: pointer;
}

.dot.active {
  background: #fff;
  transform: scale(1.4);
}
```

## 常见问题

### 三栏宽度不一致
- 原因：grid 不指定宽度时，内容会撑开宽度
- 解决：改用 flexbox + `width: 380px; min-width: 380px;`

### 左右布局不对齐
- 原因：右侧 div 没有垂直居中
- 解决：添加 `display: flex; flex-direction: column; justify-content: center;`

### 文字居中但需要居左
- 原因：父容器设置了 `text-align: center`
- 解决：在需要居左的容器添加 `text-align: left;`