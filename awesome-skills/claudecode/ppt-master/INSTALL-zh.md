# 在 Claude Code 中安装 PPT Master

## 准备工作

- 已安装 [Claude Code](https://claude.ai/code)
- 已安装 Git
- 已安装 Python 3.10+

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.claude/ppt-master
```

### 2. 安装依赖

```bash
pip install -r ~/.claude/ppt-master/requirements.txt
```

### 3. 创建软链接

创建软链接使 Claude Code 能够发现该技能：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/ppt-master
ln -s ~/.claude/ppt-master/skills/ppt-master ~/.claude/skills/ppt-master
```

### 4. 验证安装

重启 Claude Code，然后尝试提问：
- "do you have ppt-master?"
- "请帮我用 ppt-master 生成一份 PPT"

如果成功，Claude Code 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.claude/ppt-master
git pull
```

也可使用内置更新脚本：
```bash
python3 ~/.claude/ppt-master/skills/ppt-master/scripts/update_repo.py
```

## 卸载

```bash
rm -rf ~/.claude/skills/ppt-master
rm -rf ~/.claude/ppt-master
```

## 获取帮助

- GitHub: https://github.com/hugohe3/ppt-master
- 提交问题: https://github.com/hugohe3/ppt-master/issues
- 常见问题: https://github.com/hugohe3/ppt-master/blob/main/docs/zh/faq.md
