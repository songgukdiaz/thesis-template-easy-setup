---
name: empirical-design
description: Guides the student through designing an empirical strategy — variables, baseline regression, identification, robustness checks, expected tables and figures.
---

# Empirical Design Skill

Use this skill when the student needs to design or review their empirical strategy.

## Process

Read docs/student-profile.md first to understand the student's RQ, data, and methodology.

1. Define the dependent variable.
2. Define the main independent variable.
3. Identify controls, with justification for each.
4. Propose a baseline regression specification.
5. Discuss identification concerns honestly.
6. Suggest robustness checks.
7. List expected tables and figures.
8. Provide an interpretation guide.

## Output format

# Empirical Design

## Hypothesis
[State the testable hypothesis in one sentence.]

## Variables

| Role | Variable | Definition | Expected Sign | Data Source |
|---|---|---|---|---|
| Dependent | | | | |
| Main Independent | | | | |
| Control | | | | |

## Baseline Specification

[Write the regression in plain text:]
[Dependent variable] = α + β₁[Main IV] + β₂[Control 1] + ... + ε

[Write the regression in LaTeX if useful:]
$$Y_{it} = lpha + eta_1 X_{it} + \gamma Z_{it} + arepsilon_{it}$$

[Explain what i and t subscripts represent, if panel data.]

## Identification Concerns

[List identification concerns honestly. If the student cannot claim causality, say so. Do not use the word "exogenous" unless justified.]

## Robustness Checks

[List 3–5 robustness checks appropriate for this design. Explain what each check tests.]

## Expected Tables

| Table | Content |
|---|---|
| Table 1 | Summary statistics |
| Table 2 | Baseline regression |
| Table 3 | [Robustness or heterogeneity] |

## Expected Figures

| Figure | Content |
|---|---|
| Figure 1 | [e.g. time series of main variable] |

## Interpretation Guide

[Explain how the student should interpret β₁: what a one-unit change means, how to report magnitude, and what language to use. Emphasise caution about causality.]
