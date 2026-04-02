# 为 OpenCode 安装 Obsidian Skills

## 前置条件

- 已安装 [OpenCode.ai](https://opencode.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 obsidian-skills 仓库

```bash
git clone https://github.com/kepano/obsidian-skills.git ~/.config/opencode/obsidian-skills
```

### 2. 创建符号链接

创建符号链接，使 OpenCode 的原生技能工具能够发现所有 Obsidian 技能：

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.config/opencode/obsidian-skills/skills ~/.config/opencode/skills/obsidian
```

### 3. 重启 OpenCode

重启 OpenCode，插件将自动注入 Obsidian Skills 上下文。

通过询问以下问题来验证是否安装成功："do you have obsidian-markdown skill?"

## 更新

```bash
cd ~/.config/opencode/obsidian-skills
git pull
```

## 获取帮助

- Obsidian Skills GitHub: https://github.com/kepano/obsidian-skills
- Agent Skills 规范: https://agentskills.io/specification