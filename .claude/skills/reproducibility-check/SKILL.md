---
name: reproducibility-check
description: Checks whether the thesis project can be reproduced by someone else — folder structure, script order, data documentation, README completeness.
---

# Reproducibility Check Skill

Use this skill when the student wants to verify their project is reproducible before submission.

## Checklist

Check each item by reading the relevant files:

1. **Raw data folder** — does `data/raw/` exist and contain files (or at least a note about where data comes from)?
2. **Clean data folder** — does `data/clean/` contain processed files?
3. **Numbered scripts** — are scripts in `code/` numbered in execution order (01_, 02_, etc.)?
4. **Script completeness** — do the scripts contain real code (not just stubs with `raise NotImplementedError`)?
5. **Output folder** — does `output/` contain generated tables or figures?
6. **README** — does README.md explain how to run the project?
7. **Requirements** — does `requirements.txt` exist and contain real dependencies?
8. **Data dictionary** — does `docs/data_dictionary.md` contain actual variable definitions (not placeholders)?
9. **Raw vs generated** — does `.gitignore` exclude raw data and generated files?
10. **References** — does `docs/references.bib` contain at least some entries?

## Output format

# Reproducibility Report

## Summary

[N]/10 checks passed.

## Checklist Results

| Check | Status | Notes |
|---|---|---|
| Raw data folder | [Pass/Fail/Warning] | |
| Clean data folder | [Pass/Fail/Warning] | |
| Numbered scripts | [Pass/Fail/Warning] | |
| Script completeness | [Pass/Fail/Warning] | |
| Output folder | [Pass/Fail/Warning] | |
| README | [Pass/Fail/Warning] | |
| Requirements | [Pass/Fail/Warning] | |
| Data dictionary | [Pass/Fail/Warning] | |
| Raw vs generated | [Pass/Fail/Warning] | |
| References | [Pass/Fail/Warning] | |

## Missing Elements

[List each failed check with a concrete description of what is missing.]

## Immediate Fixes

[For each failed check, give a specific file or folder change the student should make.]

## Risks

[Describe what would break if someone tried to reproduce the project right now.]
