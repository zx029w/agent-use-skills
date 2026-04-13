# Installing Qiushi Skill for OpenAgent

## Prerequisites

- OpenAgent installed
- Git installed

## Installation Steps

### 1. Clone qiushi-skill

```bash
git clone https://github.com/HughYau/qiushi-skill.git ~/.openagent/qiushi-skill
```

### 2. Symlink Skills

Create symlinks so OpenAgent discovers the skills:

```bash
mkdir -p ~/.openagent/skills
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.openagent/skills/$skill
  ln -s ~/.openagent/qiushi-skill/skills/$skill ~/.openagent/skills/$skill
done
```

### 3. Verify Installation

Restart OpenAgent and try asking:
- "Use seeking truth from facts to analyze this problem"
- "do you have qiushi-skill?"

If successful, OpenAgent will automatically recognize and invoke Qiushi Skill workflow.

## Updating

```bash
cd ~/.openagent/qiushi-skill
git pull
```

## Uninstallation

Remove the symlinks to uninstall:

```bash
for skill in arming-thought contradiction-analysis practice-cognition investigation-first mass-line criticism-self-criticism protracted-strategy concentrate-forces spark-prairie-fire overall-planning; do
  rm -rf ~/.openagent/skills/$skill
done
```

## Getting Help

- GitHub: https://github.com/HughYau/qiushi-skill