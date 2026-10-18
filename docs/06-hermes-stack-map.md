# Hermes Stack Map

**Living systems portrait** of the multi-profile Hermes world on this Windows host.  
**Visual:** [hermes-stack-map.html](./hermes-stack-map.html) (open in browser · **animated** CSS/SVG; Pause motion toggle)  
**Concept art:** [assets/hermes-stack-map-concept.png](./assets/hermes-stack-map-concept.png)  
**Date:** 2026-10-18 refresh · first cut 2026-07-25 (the HTML diagram still shows the July layout; this markdown is the source of truth until it gets regenerated)

## What this is

A calm map of how the pieces relate — not a full inventory dump and not a backup.

| Artifact | Job |
|----------|-----|
| **This md map** | Current text portrait |
| **This HTML map** | See the whole system visually (may lag the md) |
| **hermes-backup** (private) | Scrubbed portable DR bits |
| **Borgmatic** | Real disk disaster recovery |
| **This lab** | Learning docs |

## Layers (north → south on the diagram)

1. **Human** — operator in the loop; no fake urgency  
2. **Surfaces** — Desktop app (Sessions + a **Bots rail** that spans machines), TUI/CLI, per-profile gateways  
3. **Profiles** — main · tech · house · lifestyle · x (Bot labels are exactly these profile names)  
4. **MoA ladder** — a paid strong seat plus free-model rungs; each profile pins its own default  
5. **Main cron** — the fleet schedule lives on the orchestrator profile (grouped table below)  
6. **Shared integrations** — Trello, AgentMail, GWS, Obsidian, GitHub, xurl, Browser Use, Spotify (Hound was retired in the interim)  
7. **Monero fleet** — Fleet Console + Hive + HashVault + monerod + xmrig (+ P2Pool mini trials)  
8. **Storage** — per-drive roles, cold librarian, session policy  
9. **Backup** — Borg vs scrubbed GitHub vs lab  
10. **Sibling machines** — a Linux ops box, a family desktop, a laptop, a handheld (see the fleet section)

## Profile cheat sheet (live 2026-10-18; skill count = leaf SKILL.md files on disk)

| Profile | Role | Skills | Notes |
|---------|------|--------|-------|
| **main** | Gateway + ops bus | 174 | orchestrator home; most cron jobs live here |
| **tech** | Hard work / fleet / GitHub | 257 | fleet console home; ships the desk PRs |
| **house** | Home / projects | 124 | agentmail + trello |
| **lifestyle** | Personal / lifestyle | 156 | GWS; cold export bias |
| **x** | Social monerostar | 128 | xurl; garden skills |

**Models:** defaults move with the season rather than sitting still. Right now the
working profiles (tech/house/x) run a cheap daily default with a `:free` fallback rung,
while the two human-facing lanes keep the strong paid seat. The Desktop sidebar shows
the exact model id per session so there is no guessing. Switch with `/model` or the
picker — chat words alone don't switch.

## MoA ladder (operator)

```text
solo strong seat (paid)  →  nous-cheap  →  nous-balanced  →  nous-deep  →  :free rungs
```

- Which rung is the default is a per-profile pin, not one global switch  
- No Kimi in MoA ensembles  
- Image generation is a separate Nous-managed path  

## Web ladder (2026-10-18)

1. Local files / vault / memory  
2. x_search / xurl for X (OAuth — no separate API key to babysit)  
3. **`web_search` / `web_extract`** — portal-backed search, gateway-backed extract  
4. **Browser Use** — a real interactive browser on the Windows profiles  
5. **Camofox** — fingerprint-stable browsing for sessions that shouldn't show a terminal  

## Main cron (gateway) — grouped

The full list is `hermes cron list` on the orchestrator profile; jobs pause and return
by season, so this is the shape, not a guarantee.

| Cadence | Jobs |
|---------|------|
| daily 05:00 / 08:00 / 19:00 | X mentions glance · soft movement ping · Life Board glance |
| daily 05:15 | Linux sibling's overnight ops brief relay |
| every 5 min (windowed) | family screen-time stop check |
| ~6-hourly ticks | hardware deal watch · concert-window sampler |
| Sunday block | vault hygiene · fleet memory pressure · tech health · session maintenance · lifestyle check-in |
| Monday 09:00 | model + Hermes-fit report |
| monthly | storage + Plex health · skill comb reminder |
| paused right now | nightly upstream easy-jobs run · usage pull · classroom swap |

## Fleet beyond this box

One Desktop rail, several machines — the two wiring paths are written up in
[doc 12](./12-bots-rail-another-machine.md):

- **Family desktop** — joined the Bots rail over SSH (the app tunnels and starts its
  dashboard on demand)  
- **Partner laptop (macOS)** — no Remote Login by design; joins as a **Remote gateway**
  via `hermes serve` on the LAN behind the dashboard auth gate, plus a thin A2A lane for
  one-line asks while the lid is open  
- **Linux ops box** — headless; A2A + nightly GitHub lane; its own two profiles  
- **Handheld + kids' boxes** — play-limit and monitoring ticks, not agent seats  

A2A and the Bots rail are different wires. A machine can have one, the other, or both.

## Monero path

```text
monerod (local)  +  Hive (rig health)  +  HashVault (pool)  +  P2Pool mini
        \______________________ Fleet Console ______________________/
```

- Local checkout: `~/src/monero-fleet-console`  
- Wallet masked in UI; secrets stay in the profile `.env`  
- xmrig is fully standalone now (Awesome Miner / GUPAX are gone); P2Pool mini and
  XvB trials run as side lanes  

## Storage & cold

| Mount | Role |
|-------|------|
| C: | OS + Hermes profile homes |
| D: | cold archive + photo library |
| E: | bulk oddment + offsite-backup tray |
| F: | borg repo (pull backups from sibling Linux boxes) |
| G: | bulk Plex media |
| H: | hot media intake |
| K: | Steam NVMe + XMR data + Obsidian vault + projects |

Session policy (librarian): orchestrator hot ~30d; worker profiles ~90d; titled
sessions kept; one profile exports reports instead of hoarding transcripts.

## Related docs in this lab

1. [What is Hermes](./01-what-is-hermes.md)  
2. [Profiles main vs tech](./02-profiles-main-vs-tech.md)  
3. [GitHub CLI setup](./03-github-cli-setup.md)  
4. [Safety: no secrets](./04-safety-no-secrets.md)  
5. [Backup vs lab](./05-backup-vs-lab.md)  
6. **This map**  
7. [Optional free-play profile](./07-optional-free-play-profile.md)  
8. [Legion Go handoff](./08-handoff-2026-08-01-legion-go.md)  
9. [Spotify hygiene](./09-spotify-hygiene-with-hermes.md)  
10. [Ops Console desktop plugins](./10-ops-console-desktop-plugins.md)  
11. [Outbound fact gate](./11-outbound-fact-gate.md)  
12. [Bots rail: another machine](./12-bots-rail-another-machine.md)  

## Refresh

When the stack drifts (new integrations, major model change, new profile or machine):

1. Re-scan profiles' `config.yaml` + `cron/jobs.json`  
2. Edit this markdown first (it is the truth), then the HTML boxes when there's time  
3. Optional: regenerate concept art  

Keep secrets out of both the HTML and this markdown. No IPs, no hostnames that map the
house, no tokens — machine *roles* are enough for a public doc.
