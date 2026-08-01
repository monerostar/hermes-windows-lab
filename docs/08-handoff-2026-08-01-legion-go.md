# Handoff — 2026-08-01: Legion Go setup state

Status snapshot pushed from the Legion Go (Hermes) so the ops computer can pick it up and wire its own SSH side.

## Machine

- Lenovo Legion Go (Windows 11 dev build, git-bash/MSYS shell)
- Hermes Agent running locally (profile: default)

## What changed today

### Local user account
- Created a **standard (non-admin), passwordless local account** for family gaming.
- Minecraft Launcher installed machine-wide (Start Menu shortcut present; per-user
  save data is created under that account's `%APPDATA%\.minecraft` on first login).
- Steam setup installer staged at `C:\Users\Public\Downloads\SteamSetup.exe`
  (shared folder, both accounts can reach it). Install it inside the gaming
  account's session so it lands per-user.

### GitHub wiring (this machine → monerostar)
- **SSH key**: ed25519, title `Legion Go (Hermes)`, uploaded to the account.
- **gh CLI**: v2.97.0 via `winget install GitHub.cli` (this time winget behaved;
  an older session noted it can hang on MSI/UAC — see `03-github-cli-setup.md`).
- Auth: **SSH protocol** (not HTTPS), token in `%APPDATA%\GitHub CLI\hosts.yml`.
- Token scopes: `repo`, `read:org`, `gist`, `workflow`, `admin:public_key`.
- Git identity: `monerostar` / `203146215+monerostar@users.noreply.github.com`.
- Smoke test: `ssh -T git@github.com` → authenticated as monerostar.

## Gotcha worth knowing (ops computer may hit this too)

`gh auth login --web` prints the device code but **hangs at "Press Enter to open…
in your browser"** when run inside the Hermes PTY — the Enter never registers.
Workaround that works: drive the OAuth device flow directly with curl
(`client_id=178c6fc778ccc68e1d6a` is GitHub CLI's public OAuth app), poll the
token endpoint, then write `hosts.yml` manually. Managing SSH keys via API needs
the `admin:public_key` scope or `POST /user/keys` returns 404.

## To do from the ops side

- Add the ops computer's own SSH key to monerostar (or exchange keys for direct
  machine-to-machine pulls).
- Pick up this repo via `git pull` over SSH.

## Safety

No tokens, private keys, wallets, or personal identifiers in this repo. The
gaming account is deliberately not named here.
