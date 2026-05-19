# 安装 Obsidian CLI 技能（Qoder）

## 前提条件

- Qoder 已安装
- Git 已安装
- Obsidian Desktop v1.12.0+ 已安装且 CLI 已启用（Settings → Command line interface → 开启）

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/pablo-mano/Obsidian-CLI-skill.git ~/.qoder/Obsidian-CLI-skill
```

### 2. 创建符号链接

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/obsidian-cli
ln -s ~/.qoder/Obsidian-CLI-skill/skills/obsidian-cli ~/.qoder/skills/obsidian-cli
```

### 3. 验证安装

重启 Qoder，然后尝试询问：

- "Read my daily note"
- "Search my vault for meeting notes"
- "do you have obsidian-cli?"

如果安装成功，Qoder 将自动识别并调用 Obsidian CLI 技能。

## 更新

```bash
cd ~/.qoder/Obsidian-CLI-skill
git pull
```

## 卸载

```bash
rm -rf ~/.qoder/skills/obsidian-cli
```

## 获取帮助

- GitHub: https://github.com/pablo-mano/Obsidian-CLI-skill
- 报告问题: https://github.com/pablo-mano/Obsidian-CLI-skill/issues
