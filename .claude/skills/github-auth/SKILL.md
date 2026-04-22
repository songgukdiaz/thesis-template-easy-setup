---
name: github-auth
description: Re-authenticate the GitHub App so git push and gh CLI work
user_invocable: true
---

# GitHub App Re-Authentication

Re-authenticate using the personal GitHub App (`github-app-personal`) so that `git push`, `gh pr create`, and other GitHub operations work.

## Steps

1. Run the reauth script to get a fresh token:

```bash
eval "$(~/.config/github-app-personal/reauth.sh)"
```

2. Verify authentication:

```bash
gh auth status
```

3. Confirm the token works by listing accessible repos:

```bash
gh api /installation/repositories --jq '.repositories[].full_name'
```

4. Report the result to the user — which account is active and which repos are accessible.
