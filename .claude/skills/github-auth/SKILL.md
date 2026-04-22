---
name: github-auth
description: Re-authenticate the GitHub App so git push and gh CLI work
user_invocable: true
---

# GitHub App Re-Authentication

Re-authenticate using the personal GitHub App (`github-app-personal`) so that `git push`, `gh pr create`, and other GitHub operations work.

## Important

The `eval` approach (`eval "$(reauth.sh)"`) does NOT work in Claude Code because each Bash tool call runs in a subshell — exported env vars do not persist. Instead, read the token directly and set `GH_TOKEN` in every command that needs it.

## Steps

1. Clear any stale cached token and generate a fresh one:

```bash
rm -f ~/.config/github-app-personal/token-cache.json && ~/.config/github-app-personal/get-token.sh > /dev/null
```

2. In every subsequent Bash call that uses `gh` or `git push`, **prefix the command** with the token export:

```bash
export GH_TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.config/github-app-personal/token-cache.json'))['token'])") && gh auth status
```

3. Confirm the token works by listing accessible repos:

```bash
export GH_TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.config/github-app-personal/token-cache.json'))['token'])") && gh api /installation/repositories --jq '.repositories[].full_name'
```

4. Also configure the git credential helper so `git push` uses the same token:

```bash
TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.config/github-app-personal/token-cache.json'))['token'])") && git config --global credential.https://github.com.helper "!f() { echo \"username=x-access-token\"; echo \"password=$TOKEN\"; }; f"
```

5. Report the result to the user — which account is active and which repos are accessible.
