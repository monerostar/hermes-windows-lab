# GitHub CLI setup (this machine)

Completed initial wiring so Hermes can help with repos under **monerostar**.

## What was installed

- **GitHub CLI (`gh`)** v2.96.0
- Location: `%LOCALAPPDATA%\Programs\gh\bin\gh.exe` (user-local zip install)
- User PATH updated to include that `bin` folder
- Note: `winget install GitHub.cli` can hang on MSI/UAC on this host — user-local zip avoided that

## Auth

- `gh auth login` (device/browser flow)
- Account: **monerostar**
- Protocol: HTTPS
- Token stored in Windows keyring
- Scopes observed: `repo`, `read:org`, `gist`
- `gh auth setup-git` — git credential helper points at `gh`

## Git identity

```text
user.name  = monerostar
user.email = 203146215+monerostar@users.noreply.github.com
```

Noreply email keeps the address private; commits still attach to the GitHub user for contributions when pushed.

## Smoke checks

```bash
gh auth status
gh repo list monerostar
gh api user --jq .login
```

## Guardrails

- No drive-by pushes or contribution farming
- Prefer clear commits with short messages
- Never commit `.env`, tokens, wallet addresses, or live Hermes profile data
