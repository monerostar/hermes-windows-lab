# Safety: no secrets in git

If a secret hits GitHub — even in a private repo — treat it as burned and rotate it.

## Never commit

- API keys, OAuth client secrets, refresh tokens
- `.env` files with real values
- `google_token.json` / `google_client_secret.json`
- SSH private keys, `~/.xurl`, keyring exports
- Monero/Wownero wallet files, seed phrases, pool passwords
- Full Hermes `sessions/`, `state.db`, raw memory dumps with personal data

## Do commit

- `.env.example` with empty or fake placeholders
- Docs that say *where* a secret lives, not the secret
- Scrubbed configs (redact keys, wallets, hostnames if sensitive)
- Scripts that read secrets from the environment

## Before every push

```bash
git status
git diff
# eye-scan for tokens, emails you care about, wallet strings
```

When unsure: leave it out. Backup paths are for recovery; this lab is for learning.
