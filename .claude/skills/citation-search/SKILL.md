---
name: citation-search
description: Given a claim or topic, returns structured search queries for academic databases. Never invents papers.
---

# Citation Search Skill

Use this skill when the student wants to find papers supporting a specific claim or exploring a specific topic.

## Rules

- Never invent papers, authors, journals, or publication years.
- Produce search queries only — not paper lists.
- Organise queries by database.
- Read docs/student-profile.md to tailor the queries to the student's field and RQ.

## Input

The student should provide in their message:
- The claim or topic they want to find papers for (e.g. "momentum in equity markets" or "the effect of CEO turnover on firm performance")

## Output format

# Citation Search: [claim or topic]

## Search Queries by Database

### Google Scholar
- "[exact phrase query 1]"
- "[exact phrase query 2]"

### SSRN
- [keyword string 1]
- [keyword string 2]

### NBER Working Papers (nber.org/papers)
- [keyword string]

### Semantic Scholar (semanticscholar.org)
- [keyword string]

### Journal-Specific Searches
[Recommend 2–3 journals most likely to publish on this topic, with the journal name and a suggested query]

## Search Tips

[Give 2–3 practical tips for this specific search: e.g. which author names to look up, whether to filter by year, whether to look for survey papers first]
