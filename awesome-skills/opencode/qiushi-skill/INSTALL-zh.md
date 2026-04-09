# 为 OpenCode 安装求是 Skill

## 系统要求

- OpenCode 已安装
- Git 已安装

## 安装步骤

OpenCode 建议以"手动加载 skill 文件"的方式使用,避免把平台差异隐藏在文档承诺里。

### 1. 克隆仓库到本地

```bash
git clone https://github.com/HughYau/qiushi-skill
```

### 2. 将入口 Skill 作为会话起始方法论

将 `skills/arming-thought/SKILL.md` 作为新会话的起始方法论入口。

### 3. 按需加载具体 Skill

具体任务开始后,再按需读取对应 `skills/*/SKILL.md`:
- `skills/contradiction-analysis/SKILL.md` — 矛盾分析法
- `skills/practice-cognition/SKILL.md` — 实践认识论
- `skills/investigation-first/SKILL.md` — 调查研究
- `skills/mass-line/SKILL.md` — 群众路线
- `skills/criticism-self-criticism/SKILL.md` — 批评与自我批评
- `skills/protracted-strategy/SKILL.md` — 持久战略
- `skills/concentrate-forces/SKILL.md` — 集中兵力
- `skills/spark-prairie-fire/SKILL.md` — 星火燎原
- `skills/overall-planning/SKILL.md` — 统筹兼顾
- `skills/workflows/SKILL.md` — 工作流组合

### 4. 加载命令文件(可选)

如果 OpenCode 支持命令目录,则一并加载 `commands/`;否则直接读取对应命令文件内容。

### 5. 验证安装

#### macOS / Linux:

```bash
cd qiushi-skill
bash tests/validate.sh
```

#### Windows:

```powershell
cd qiushi-skill
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File tests/validate.ps1
```

验证脚本会检查:
- JSON 配置是否有效
- hook 文件与命令文件是否齐全
- `SKILL.md` / agent / command 的 frontmatter 是否完整
- 本地 Markdown 链接和图片路径是否存在

## 验证安装成功

检查以下几点:
- 入口 skill 只做路由和约束,不会压过宿主系统规则
- 命令文件与 skill 文件一一对应
- 文档中的平台说明与你的实际安装方式一致

## 更新

```bash
cd qiushi-skill
git pull
```

## 获取帮助

- GitHub: https://github.com/HughYau/qiushi-skill
- 问题反馈: https://github.com/HughYau/qiushi-skill/issues
- OpenCode 使用说明: https://github.com/HughYau/qiushi-skill/blob/main/docs/README.opencode.md