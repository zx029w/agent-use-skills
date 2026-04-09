# 为 Codex 安装求是 Skill

## 系统要求

- Codex 已安装
- Git 已安装

## 安装步骤

Codex 不依赖 Claude/Cursor 插件壳。核心做法是:把 `skills/` 当作方法论技能库,把 `commands/` 当作可选的手动命令模板。

### 1. 克隆仓库到本地

```bash
git clone https://github.com/HughYau/qiushi-skill
```

### 2. 在新会话开始时加载入口 Skill

让 Codex 读取 `skills/arming-thought/SKILL.md`,把它作为路由和方法论约束。

### 3. 针对具体任务按需加载 Skill

根据任务类型,按需读取以下文件:
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

### 4. 加载命令模板(可选)

如果 Codex 支持 Markdown commands,可额外加载 `commands/` 目录作为手动入口;不支持时,直接读取同名命令文件内容即可。

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

手动验证两点:
- 会话起始时能够成功读取 `arming-thought`
- 针对一个具体问题时,能够按需切换到对应 skill,而不是机械全调用

## 更新

```bash
cd qiushi-skill
git pull
```

## 获取帮助

- GitHub: https://github.com/HughYau/qiushi-skill
- 问题反馈: https://github.com/HughYau/qiushi-skill/issues
- Codex 使用说明: https://github.com/HughYau/qiushi-skill/blob/main/docs/README.codex.md