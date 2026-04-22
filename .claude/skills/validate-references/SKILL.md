---
name: validate-references
description: Checks all citations in thesis/*.md against docs/references.bib, then attempts web verification via Semantic Scholar. Reports confirmed / unverified / suspicious.
---

# Validate References Skill

Use this skill when the student wants to check their bibliography for missing or potentially incorrect entries.

## Process

### Step 1: Extract citation keys from thesis files

Read all files in thesis/*.md. Find every citation in `[@key]` format. Build a list of all unique keys cited.

### Step 2: Cross-check against references.bib

Read docs/references.bib. Extract all BibTeX entry keys (the identifier after @article{, @book{, etc.).

Compare:
- Keys cited in thesis but absent from .bib -> flag as MISSING
- Keys in .bib but never cited in thesis -> flag as UNUSED (informational only)

### Step 3: Web verification via Semantic Scholar

For each key present in .bib, extract:
- title (from the `title = {...}` field)
- author (first author's last name from the `author = {...}` field)
- year (from the `year = {...}` field)

Use WebFetch or WebSearch to query the Semantic Scholar API:
```
https://api.semanticscholar.org/graph/v1/paper/search?query=[title]+[author]&fields=title,authors,year&limit=3
```

This API requires no key and returns JSON. For each result, check whether title, first author, and year are consistent with the .bib entry.

Classify each reference:
- **Confirmed** - Semantic Scholar returned a match with consistent title, author, and year
- **Unverified** - API returned no match or ambiguous results (may still be real - student should check manually)
- **Suspicious** - year is impossible (e.g. future year), author name not found anywhere, title is generic or implausibly short

### Step 4: Write validation report

Write the report to docs/reference-validation.md.

## Output format for docs/reference-validation.md

```markdown
# Reference Validation Report

Generated: [date]

## Summary
- Total citations in thesis: [N]
- Missing from .bib: [N]
- Confirmed via Semantic Scholar: [N]
- Unverified (check manually): [N]
- Suspicious: [N]
- Unused in .bib: [N]

## Missing from .bib (cited but not in references.bib)
[list each key]

## Confirmed References
[list each key with: title, author, year - confirmed]

## Unverified References (check manually)
[list each key with: title as given in .bib, reason not confirmed]

## Suspicious References
[list each key with: title, specific reason for suspicion]

## Unused .bib Entries
[list each key]
```

## Important notes

- "Unverified" does not mean wrong - many real papers are not indexed by Semantic Scholar (books, reports, working papers from small institutions).
- Only flag a reference as "Suspicious" if there is a specific concrete reason (impossible date, zero search results for a supposedly famous paper, etc.).
- Never change the student's .bib file. Only report.
