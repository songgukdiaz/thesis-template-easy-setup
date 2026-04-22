---
name: data-explorer
description: Reads a dataset from data/clean/, describes its structure, suggests summary statistics, and flags data quality issues. Student must provide the file path in the same message.
---

# Data Explorer Skill

Use this skill when the student wants to understand a dataset or identify data quality issues.

## Input required

The student must provide the file path (relative to the project root, within data/clean/) in the same message as /data-explorer.

Example: `/data-explorer data/clean/firm_panel.csv`

If no path is provided, ask for it before proceeding.

## Rules

- Read docs/student-profile.md to understand the research question and methodology.
- Read the file using the Read tool.
- For CSV files: parse the first row as headers and analyse structure from the first ~100 rows visible in the Read output.
- Do not modify the file.
- Suggest summary statistics the student should include in thesis/04_data.md.
- Generate Python code the student can run to produce the suggested outputs.

## Output format

# Data Explorer: [filename]

## Schema

| Column | Inferred Type | Non-null Count | Notes |
|---|---|---|---|
| [column name] | [int/float/str/date] | [count if visible] | [any observation] |

## Data Quality Flags

List any of the following if detected:
- **Duplicates:** [description]
- **Missing values:** [which columns, approximate frequency]
- **Outliers:** [which columns, describe]
- **Implausible values:** [e.g. negative prices, future dates]
- **Date range:** [if date column present]

## Suggested Summary Statistics

Given the research question ([quote from student-profile.md]), the student should report:
- [Variable]: mean, standard deviation, min, max, N
- [Variable]: [same]

## Suggested Python Code

Paste this into code/04_tables_figures.py and adjust as needed:

```python
import pandas as pd
from pathlib import Path

df = pd.read_csv("data/clean/[filename]")

# Summary statistics
summary = df[["var1", "var2"]].describe().T[["count", "mean", "std", "min", "max"]]
print(summary.round(3).to_string())

# Missing values
print(df.isnull().sum()[df.isnull().sum() > 0])

# Duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")
```

## Connection to Thesis

[1–2 sentences on how this dataset connects to the stated research question, and what the student should highlight in thesis/04_data.md.]
