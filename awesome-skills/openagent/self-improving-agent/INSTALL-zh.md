# 在 OpenAgent 中安装 Self-Improving Agent

## 前置条件

- 已安装 OpenAgent
- 已安装 Git

## 安装步骤

### 1. 克隆 self-improving-agent 仓库

```bash
git clone https://github.com/peterskoett/self-improving-agent.git ~/.openagent/self-improving-agent
```

### 2. 创建符号链接

创建符号链接，使 OpenAgent 能够发现 self-improving-agent 技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/self-improving-agent
ln -s ~/.openagent/self-improving-agent/skills/self-improving-agent ~/.openagent/skills/self-improving-agent
```

### 3. 验证安装

重启 OpenAgent，尝试询问：
- "帮我记录这次学习的经验"
- "do you have self-improving-agent?"

如果安装成功，OpenAgent 会自动识别并调用 Self-Improving Agent 技能工作流。

## 更新

```bash
cd ~/.openagent/self-improving-agent
git pull
```

## 卸载

删除符号链接即可卸载：

```bash
rm -rf ~/.openagent/skills/self-improving-agent
```

## 获取帮助

- GitHub：https://github.com/peterskoett/self-improving-agent