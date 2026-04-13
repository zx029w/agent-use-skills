# 在 OpenAgent 中安装求是 Skill

## 前置条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 qiushi-skill 仓库

```bash
git clone https://github.com/HughYau/qiushi-skill.git ~/.openagent/qiushi-skill
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 qiushi-skill 技能：

```bash
mkdir -p ~/.openagent/skills
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/qiushi-skill/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. 验证安装

重启 OpenAgent，尝试询问：
- "用实事求是的方法分析这个问题"
- "do you have qiushi-skill?"

如果安装成功，OpenAgent 会自动识别并调用求是 Skill 工作流。

## 更新

```bash
cd ~/.openagent/qiushi-skill
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.openagent/skills/$skill
done
```

## 获取帮助

- GitHub：https://github.com/HughYau/qiushi-skill