# 幻灯片页面类型

## 1. 封面页

用于演示开场。

**结构：**
- 超大主标题（font-weight: 900）
- 副标语（font-weight: 300，半透明白色）
- 系列标识/Logo（可选）

**示例：**
```html
<div class="content">
  <p style="font-size: 20px; color: rgba(255,255,255,0.5); letter-spacing: 4px; margin-bottom: 30px;">LOGO</p>
  <h1 style="font-size: 96px; font-weight: 900; line-height: 1.1; margin-bottom: 40px;">
    主标题 <span class="gradient">关键词</span>
  </h1>
  <p style="font-size: 36px; font-weight: 300; color: rgba(255,255,255,0.5);">副标题说明</p>
</div>
```

---

## 2. 标题冲击页

用于章节开始或重点强调。

**结构：**
- 单行/双行大标题
- 一行辅助文字（可选）

**示例：**
```html
<div class="content">
  <h1 style="font-size: 88px; font-weight: 900; line-height: 1.2; margin-bottom: 50px;">
    冲击性标题
  </h1>
  <p style="font-size: 42px; font-weight: 300; color: rgba(255,255,255,0.5);">
    辅助说明
  </p>
</div>
```

---

## 3. 金句强调页

用于引用、名言、核心观点。

**结构：**
- 大引号装饰
- 金句内容（font-weight: 700）
- 来源/出处（font-weight: 300，灰色）

**示例：**
```html
<div class="content">
  <p style="font-size: 100px; color: rgba(255,255,255,0.3);">"</p>
  <p style="font-size: 72px; font-weight: 700; line-height: 1.3; margin-bottom: 50px;">
    金句内容
  </p>
  <p style="font-size: 32px; font-weight: 300; color: rgba(255,255,255,0.5);">— 来源</p>
</div>
```

---

## 4. 三栏列表页（重要！）

用于多点说明，最多3-5个要点。

**结构：**
- 标题
- 三栏卡片（固定宽度确保等宽）

**正确示例（使用 flexbox + 固定宽度）：**
```html
<h2 style="font-size: 64px; font-weight: 700; margin-bottom: 100px;">标题</h2>
<div style="display: flex; justify-content: center; gap: 50px; width: 100%;">
  <div class="card fade-up" style="width: 380px; min-width: 380px; padding: 50px 40px; text-align: center; border-top: 4px solid #3b82f6;">
    <p style="font-size: 48px; margin-bottom: 30px;">👤</p>
    <p style="font-size: 36px; font-weight: 700; color: #3b82f6; margin-bottom: 30px;">要点一</p>
    <p style="font-size: 24px; font-weight: 300; color: rgba(255,255,255,0.6); line-height: 2;">
      说明文字<br>第二行
    </p>
  </div>
  <div class="card fade-up" style="width: 380px; min-width: 380px; padding: 50px 40px; text-align: center; border-top: 4px solid #8b5cf6;">
    <!-- 要点二 -->
  </div>
  <div class="card fade-up" style="width: 380px; min-width: 380px; padding: 50px 40px; text-align: center; border-top: 4px solid #06b6d4;">
    <!-- 要点三 -->
  </div>
</div>
```

**注意**：不要使用 grid，因为内容长度不同会导致卡片宽度不一致。

---

## 5. 两栏对比页

用于展示差异、前后对比、双选项。

**结构：**
- 两栏固定宽度布局
- 每栏一个卡片

**示例：**
```html
<h2 style="font-size: 64px; font-weight: 700; margin-bottom: 80px;">标题</h2>
<div style="display: flex; justify-content: center; gap: 60px; width: 100%;">
  <div class="card" style="width: 450px; text-align: center;">
    <p style="font-size: 80px; font-weight: 900; color: #3b82f6; margin-bottom: 30px;">A</p>
    <p style="font-size: 36px; font-weight: 700; margin-bottom: 20px;">选项A</p>
    <p style="font-size: 24px; font-weight: 300; color: rgba(255,255,255,0.5);">说明</p>
  </div>
  <div class="card" style="width: 450px; text-align: center;">
    <p style="font-size: 80px; font-weight: 900; color: #10b981; margin-bottom: 30px;">B</p>
    <p style="font-size: 36px; font-weight: 700; margin-bottom: 20px;">选项B</p>
    <p style="font-size: 24px; font-weight: 300; color: rgba(255,255,255,0.5);">说明</p>
  </div>
</div>
```

---

## 6. 数据展示页

用于关键数字、统计、成果。

**结构：**
- 超大数字（font-weight: 900）
- 单位/说明（font-weight: 300）
- 简短解释

**示例：**
```html
<div class="content">
  <p style="font-size: 120px; font-weight: 900; color: #3b82f6;">10x</p>
  <p style="font-size: 36px; font-weight: 300; color: rgba(255,255,255,0.5); margin-top: 30px;">效率提升</p>
</div>
```

---

## 7. 步骤说明页（左右布局）

用于流程、方法、操作指南。

**结构：**
- 左侧：步骤编号（固定宽度）
- 右侧：标题 + 说明（垂直居中，居左对齐）

**示例：**
```html
<div class="content" style="max-width: 1000px;">
  <h2 style="font-size: 56px; font-weight: 700; margin-bottom: 60px;">标题</h2>
  <div style="width: 100%;">
    <div style="display: flex; align-items: center; gap: 30px; padding: 25px 35px; background: rgba(255,255,255,0.03); border-radius: 16px; margin-bottom: 12px;">
      <span style="font-size: 42px; font-weight: 900; min-width: 70px; color: #3b82f6;">01</span>
      <div style="display: flex; flex-direction: column; justify-content: center; text-align: left;">
        <p style="font-size: 30px; font-weight: 700;">步骤名称</p>
        <p style="font-size: 22px; font-weight: 300; color: rgba(255,255,255,0.5);">说明文字</p>
      </div>
    </div>
    <!-- 更多步骤... -->
  </div>
</div>
```

**关键点**：
- 左侧数字：`min-width: 70px` 固定宽度
- 右侧 div：`flex-direction: column; justify-content: center; text-align: left;`

---

## 8. 结尾行动页

用于演示结束，呼吁行动。

**结构：**
- 总结金句
- 行动号召（CTA）
- 联系方式/二维码（可选）

**示例：**
```html
<div class="content">
  <h1 style="font-size: 72px; font-weight: 900; line-height: 1.2; margin-bottom: 50px;">
    总结金句
  </h1>
  <p style="font-size: 38px; font-weight: 300; color: rgba(255,255,255,0.5); margin-bottom: 60px;">
    行动号召
  </p>
</div>
```

---

## 页面选择指南

| 内容类型 | 推荐页面类型 |
|---------|-------------|
| 演示开场 | 封面页 |
| 章节分隔 | 标题冲击页 |
| 核心观点 | 金句强调页 |
| 多点说明（3-5点）| 三栏列表页 |
| 对比/双选项 | 两栏对比页 |
| 关键数据 | 数据展示页 |
| 操作步骤 | 步骤说明页 |
| 演示结束 | 结尾行动页 |