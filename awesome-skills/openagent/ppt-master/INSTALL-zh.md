# 在 OpenAgent 中安装 PPT Master

## 准备工作

- 已安装 OpenAgent
- 已安装 Git
- 已安装 Python 3.10+

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/hugohe3/ppt-master.git ~/.openagent/ppt-master
```

### 2. 安装依赖

```bash
pip install -r ~/.openagent/ppt-master/requirements.txt
```

### 3. 创建软链接

创建软链接使 OpenAgent 能够发现该技能：

```bash
mkdir -p ~/.openagent/skills
rm -rf ~/.openagent/skills/ppt-master
ln -s ~/.openagent/ppt-master/skills/ppt-master ~/.openagent/skills/ppt-master
```

### 4. 验证安装

重启 OpenAgent，然后尝试提问：
- "do you have ppt-master?"
- "请帮我用 ppt-master 生成一份 PPT"

如果成功，OpenAgent 将自动识别并调用该技能。

## 更新指南

```bash
cd ~/.openagent/ppt-master
git pull
```

## 卸载

```bash
rm -rf ~/.openagent/skills/ppt-master
rm -rf ~/.openagent/ppt-master
```

## 获取帮助

- GitHub: https://github.com/hugohe3/ppt-master
- 提交问题: https://github.com/hugohe3/ppt-master/issues
- 常见问题: https://github.com/hugohe3/ppt-master/blob/main/docs/zh/faq.md
