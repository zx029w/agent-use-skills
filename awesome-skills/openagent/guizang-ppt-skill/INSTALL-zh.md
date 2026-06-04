# 在 OpenAgent 中安装 Guizang PPT Skill

## 准备工作

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.openagent/guizang-ppt-skill
```

### 2. 创建软链接

创建软链接使 OpenAgent 能够发现该技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/guizang-ppt-skill
ln -s ~/.openagent/guizang-ppt-skill ~/.openagent/skills/guizang-ppt-skill
```

### 3. 验证安装

重启 OpenAgent，然后尝试提问：
- "帮我做一份杂志风 PPT"
- "帮我做一份瑞士风 PPT"

如果成功，OpenAgent 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.openagent/guizang-ppt-skill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/guizang-ppt-skill
```

## 获取帮助

- GitHub: https://github.com/op7418/guizang-ppt-skill
- 提交问题: https://github.com/op7418/guizang-ppt-skill/issues
