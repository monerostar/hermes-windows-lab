# hermes-windows-lab

Public learning lab for running [Hermes Agent](https://hermes-agent.nousresearch.com/) on Windows — notes, safe samples, and small scripts.

**Owner:** [monerostar](https://github.com/monerostar)  
**Visibility:** public  
**Not this repo:** full Hermes profile backups, sessions, API keys, wallets, or live configs with secrets.

## What this is

A calm place to:

- learn Git/GitHub with real Hermes-related work
- document Windows multi-profile setup (main vs tech, etc.)
- keep **sanitized** skill samples and helper scripts
- build a portfolio-shaped project without dumping the whole machine

## What this is not

| Avoid here | Why |
|------------|-----|
| `HERMES_HOME` full copy | secrets + personal history |
| `.env`, OAuth tokens, keyrings | credential leak risk |
| xmrig configs with wallets/pools | privacy / security |
| chat session databases | personal + bulky |

Use a **separate private backup** flow for disaster recovery (`monerostar/hermes-backup`). This lab stays readable and teachable.

## Layout

```text
docs/               explainers (learning notes) + stack map HTML
docs/assets/        concept art / diagrams (no secrets)
scripts/            small helper scripts (no secrets)
skills-samples/     optional scrubbed skill excerpts
.gitignore          blocks common secret patterns
```

## Docs index

1. [What is Hermes (for this lab)](docs/01-what-is-hermes.md)
2. [Profiles: main vs tech](docs/02-profiles-main-vs-tech.md)
3. [GitHub CLI setup on this machine](docs/03-github-cli-setup.md)
4. [Safety: no secrets in git](docs/04-safety-no-secrets.md)
5. [Backup vs lab (two different jobs)](docs/05-backup-vs-lab.md)
6. [Hermes stack map](docs/06-hermes-stack-map.md) · [interactive diagram](docs/hermes-stack-map.html)
7. [Optional: free-model play profile](docs/07-optional-free-play-profile.md)
8. [Handoff 2026-08-01: Legion Go setup state](docs/08-handoff-2026-08-01-legion-go.md)
9. [Spotify hygiene with Hermes](docs/09-spotify-hygiene-with-hermes.md) (scrubbed method + API notes; no personal library)

## Quick git reminders

```bash
git status
git add -A
git commit -m "short description of what changed"
git push
```

Commits on this account use:

- `user.name` = monerostar
- `user.email` = GitHub noreply (private)

## Status

- Skeleton created: 2026-07-23
- First real content: setup docs from initial monerostar GitHub wiring
- Stack map (Option C): 2026-07-25 — multi-profile systems portrait HTML + companion md
- 2026-08-01: Legion Go handoff pushed (SSH wiring, gaming account prep, PTY gotcha)
- 2026-08-05: Spotify hygiene lab note (play counts > likes; Feb-2026 API gotchas; no secrets)
