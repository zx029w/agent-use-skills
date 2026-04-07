# 为 Qoder 安装 Baoyu Skills

## 前提条件

- 已安装 [Qoder](https://qoder.ai)
- 已安装 Git

## 安装步骤

### 1. 克隆 Baoyu Skills 仓库

```bash
git clone https://github.com/JimLiu/baoyu-skills.git ~/.qoder/baoyu-skills
```

### 2. 创建符号链接

创建符号链接，使 Qoder 能够发现 Baoyu 技能：

```bash
mkdir -p ~/.qoder/skills
rm -rf ~/.qoder/skills/baoyu-skills
ln -s ~/.qoder/baoyu-skills/skills ~/.qoder/skills/baoyu-skills
```

### 3. 验证安装

重启 Qoder 后，尝试询问：

- "do you have baoyu-imagine?"

如果安装成功，Qoder 将自动识别并调用相应的 Baoyu 技能。

## 更新

```bash
cd ~/.qoder/baoyu-skills
git pull
```

## 卸载

```bash
rm -rf ~/.qoder/skills/baoyu-skills
```

## 获取帮助

- GitHub: https://github.com/JimLiu/baoyu-skills
- 提交问题: https://github.com/JimLiu/baoyu-skills/issues
