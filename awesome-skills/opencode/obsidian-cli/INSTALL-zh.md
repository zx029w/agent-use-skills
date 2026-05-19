# 安装 Obsidian CLI 技能（OpenCode）

## 前提条件

- [OpenCode](https://opencode.ai) 已安装
- Git 已安装
- Obsidian Desktop v1.12.0+ 已安装且 CLI 已启用（Settings → Command line interface → 开启）

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.config/opencode/Obsidian-CLI-skill
```

### 2. 创建符号链接

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/obsidian-cli
ln -s ~/.config/opencode/Obsidian-CLI-skill/skills/obsidian-cli ~/.config/opencode/skills/obsidian-cli
```

### 3. 验证安装

重启 OpenCode，然后尝试询问：

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

如果安装成功，OpenCode 将自动识别并调用 Obsidian CLI 技能。

## 更新

```bash
cd ~/.config/opencode/Obsidian-CLI-skill
git pull
```

## 卸载

```bash
rm -rf ~/.config/opencode/skills/obsidian-cli
```

## 获取帮助

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- 报告问题: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
