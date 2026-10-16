# finance-coach-skill

A shareable Claude skill: a plain-language, verify-first personal finance
coach for friends and family. It contains **no personal data** - it is the
method behind the private `financial-advisor` project, rewritten from scratch.

## Install

1. Download **finance-coach.zip** from the
   [latest release](https://github.com/duwilliam16-code/finance-coach-skill/releases/latest).
   Don't unzip it.
2. Follow **[SETUP.md](SETUP.md)** - about 5 minutes on claude.ai, free plan
   works.

Education, not professional financial advice.

## Layout

| Path | What it is |
|------|------------|
| `finance-coach/SKILL.md` | The skill: household and goals setup, eleven-question interview, goal checklists, rules, priorities, financial-status.md |
| `finance-coach/references/` | Status template, military/federal module, investing primer |
| `SETUP.md` | One-page install guide for non-technical users |
| `dist/finance-coach.zip` | The upload file (built, not committed) |

## Build the zip

claude.ai needs the skill **folder** at the top of the zip, not loose files.
From this folder:

```
python build.py
```

## Before sharing

Search the skill for personal names, institutions and dollar figures from the
private project. Nothing household-specific belongs here.
