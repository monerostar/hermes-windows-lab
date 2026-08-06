# Spotify hygiene with Hermes (scrubbed lab note)

**Audience:** monerostar / anyone learning Hermes + Spotify without dumping a personal library.  
**Not in this doc:** tokens, Client IDs, playlist IDs, taste profiles, export CSVs, Plex paths.

## What problem this solves

People often treat Spotify **likes** as "my music." Many do not. The stronger signal for "what I actually play" is Spotify's **top tracks / top artists** (`user-top-read`), plus playlists they built on purpose.

A calm hygiene pass:

1. Export (or inspect) the account  
2. Rank by **play counts**, not likes  
3. Clean playlists in **small approved chunks**  
4. Never rewrite a whole library in one shot  

## Hermes pieces

| Piece | Role |
|-------|------|
| Native **Spotify toolset** | Playback, search, playlists, library (enable via `hermes tools`) |
| `hermes auth spotify` | PKCE OAuth; tokens in profile `auth.json` under `providers.spotify` |
| Optional **cleanup skill / scripts** | Export + top-data + propose-only maps (fleet desk or local scripts) |

Hermes does **not** need a second bundled Spotify skill for day-to-day control. Hygiene scripts sit **beside** the agent when you want bulk export/analysis.

### Setup (high level)

```bash
hermes tools enable spotify
hermes auth spotify
```

For listening-profile work, include scope **`user-top-read`** when you auth (re-run auth if it was missing). Default scopes cover playback + playlists + library; top artists/tracks are easy to miss.

Create a Spotify developer app (Web API), redirect URI matching Hermes docs (loopback callback). Never commit Client ID/secret or tokens into this lab.

## Feb-2026 Web API gotchas (operators)

These bit real cleanup scripts. Hermes' native plugin already targets the modern shapes for add/remove/create; scripts you write yourself must match:

| Action | Use | Avoid |
|--------|-----|--------|
| List / add / remove playlist contents | `/playlists/{id}/items` | old `/tracks` on playlists |
| DELETE body | `{"items":[{"uri":"spotify:track:..."}]}` | `{"tracks":[...]}` |
| Create playlist | `POST /me/playlists` | `POST /users/{id}/playlists` (often 403) |
| Play-count tops | `GET /me/top/tracks` and `/me/top/artists` | treating saved tracks as "taste" |
| Token 401 | force refresh even if `expires_at` looks fine | trusting a stale access token forever |

Only **owned** playlists expose items; followed editorial playlists often 403.

## Chunk cleanup pattern (human in the loop)

Good chunks (examples of *shape*, not a real library):

1. Merge near-duplicate workout lists into one named list  
2. Remove A∩B dups from one of two genre lists  
3. Orphan likes → small **Keepers** (play-count hits) + optional **Sleep** (ambient)  
4. Empty a "to organize" bin into existing lists  
5. Delete only lists that are fully redundant  

Rules:

- Show the track list **before** mutate  
- User says yes per chunk  
- Verify with **name + artist** keys (Spotify re-links track ids)  
- Sleep/nature noise is often not "taste" — ask before ranking it  

## What stays private

| Private | Why |
|---------|-----|
| Full export CSVs / JSON | identity + listening graph |
| Taste write-ups | personal |
| OAuth tokens / Client secrets | credentials |
| Home media paths (Plex, drives) | host ops, not portfolio |

Public monerostar surface stops at **method + API notes**. Personal runs stay on the machine or a private desk.

## Related reading

- Official Hermes Spotify feature docs (install tree / docs site): user-guide → features → Spotify  
- This lab: [Safety: no secrets](04-safety-no-secrets.md), [Backup vs lab](05-backup-vs-lab.md)

## Status

- Lab note added: 2026-08-05  
- Based on a real Windows Hermes + Spotify hygiene pass; **no personal library data** included  
