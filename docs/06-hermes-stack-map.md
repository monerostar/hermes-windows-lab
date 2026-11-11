# Hermes Stack Map

**Living systems portrait** of the multi-profile Hermes world on this Windows host.
**Visual:** [hermes-stack-map.html](./hermes-stack-map.html). The picture is the July layout and was not redrawn in the 2026-11-09 pass. This markdown is the truth.
**Concept art:** [assets/hermes-stack-map-concept.png](./assets/hermes-stack-map-concept.png)
**Date:** 2026-11-09 content pass. First cut 2026-07-25. October layout 2026-10-18.

## What this is

A calm map of how the pieces relate. Not a full inventory dump and not a backup.

| Artifact | Job |
|----------|-----|
| **This md map** | Current text portrait |
| **This HTML map** | July picture. Lags this note until it is redrawn |
| **Private backup repo** | Disaster recovery. Not named here |
| **Borgmatic** | Real disk disaster recovery |
| **This lab** | Learning docs |

## Layers (north to south on the diagram)

1. **Human.** Operator in the loop. No fake urgency.
2. **Surfaces.** Desktop app (Sessions plus a Bots rail that spans machines), TUI/CLI, per-profile gateways.
3. **Profiles.** Ten Windows profile homes. Bot labels are profile names. This note names the working seats. One private lane is not described here.
4. **Model pins.** Each profile picks its own default. No ensemble ladder on this host right now.
5. **Orchestrator cron.** The fleet schedule lives on the main profile. Shape only, not a clock table.
6. **Shared integrations.** Obsidian, GitHub, GWS, AgentMail, Browser Use, Spotify. The life queue is a local board, not a hosted Trello list.
7. **Monero fleet.** Fleet Console plus rig health, pool, node, and miner. The mining lane is its own profile, not mixed into tech.
8. **Storage.** Per-drive roles, cold librarian, session policy.
9. **Backup.** Borg, a private backup repo, and this lab. Three different jobs.
10. **Sibling machines.** Roles only. A Linux ops box exists and is not documented in this lab yet.

## Profile cheat sheet (2026-11-09)

Skill counts are omitted on purpose. They rot faster than the roles.

| Profile | Role |
|---------|------|
| **main** | Gateway and life routing. Most of the schedule lives here. |
| **tech** | Hands-on computer work, GitHub, Hermes itself. |
| **house** | Home systems. |
| **lifestyle** | Personal rhythm. |
| **x** | Public voice. |
| **books** | Records and receipts. |
| **rig-ops** | Rig hardware. Split out of tech. |
| **gaming** | Games library. |
| **model-test** | Free-model experiments. Not a production seat. |

One more profile home exists and is intentionally not described here.

**Models.** Working seats usually pin a cheap daily model. Review work uses a stronger seat when asked. The experiment seat stays on a free model. The Desktop sidebar shows the exact model id per session. Switch with `/model` or the picker. Chat words alone do not switch the model.

There is no ensemble ladder on this host right now. An old ladder drawn in the HTML is historical.

## Web ladder (2026-11-09)

1. Local files, vault, memory.
2. X search tools for X. A normal page fetch gets blocked there.
3. Keyless web search and extract. Not a logged-in portal.
4. Browser Use for pages that need clicks.
5. A fingerprint-stable browser path for sessions that should not show a terminal.

## Schedule shape

The orchestrator profile holds the schedule. Jobs pause when they are not earning their keep. Do not treat a published clock as current.

The shape, not the clocks:

- morning glances
- a Sunday maintenance block
- a Monday model note
- monthly storage

Several of those are paused on purpose while their value is being decided. A Linux overnight relay is not documented here.

## Fleet beyond this box

One Desktop rail, several machines. The two wiring paths are in [doc 12](./12-bots-rail-another-machine.md).

- A desktop can join the Bots rail over SSH. The app tunnels and starts the dashboard on demand.
- A Mac with Remote Login off joins as a remote gateway (`hermes serve` behind dashboard auth), plus a thin ask lane while the lid is open.
- A Linux ops box is part of the fleet and is not documented in this lab yet.
- Other Windows boxes are monitored, not agent seats.

A2A and the Bots rail are different wires. A machine can have one, the other, or both.

## Monero path

```text
node  +  rig health  +  pool  +  miner
        \__________ Fleet Console __________/
```

- Public CLI and notes: `monerostar/monero-fleet-console`
- Wallet stays masked. Secrets stay in a profile env file, never in this lab.
- The miner is standalone. The mining lane is its own profile.

## Storage and cold

| Mount | Role |
|-------|------|
| C: | OS and Hermes profile homes |
| D: | cold archive and photo library |
| E: | bulk oddment and offsite-backup tray |
| F: | borg repo |
| G: | bulk media |
| H: | hot media intake |
| K: | games, project data, notes vault |

Session policy: orchestrator hot about 30 days. Worker profiles about 90 days. Titled sessions kept.

## Related docs in this lab

1. [What is Hermes](./01-what-is-hermes.md)
2. [Profiles main vs tech](./02-profiles-main-vs-tech.md)
3. [GitHub CLI setup](./03-github-cli-setup.md)
4. [Safety: no secrets](./04-safety-no-secrets.md)
5. [Backup vs lab](./05-backup-vs-lab.md)
6. **This map**
7. [Optional free-model seat](./07-optional-free-play-profile.md)
8. [Handheld PC handoff](./08-handoff-2026-08-01-handheld.md)
9. [Spotify hygiene](./09-spotify-hygiene-with-hermes.md)
10. [Ops Console desktop plugins](./10-ops-console-desktop-plugins.md)
11. [Outbound fact gate](./11-outbound-fact-gate.md)
12. [Bots rail: another machine](./12-bots-rail-another-machine.md)

## Refresh

When the stack drifts (new integrations, a major model change, a new profile or machine):

1. Re-scan profiles' `config.yaml` and `cron/jobs.json`.
2. Edit this markdown first. It is the truth. Redraw the HTML when there is time.
3. Optional: regenerate concept art.

Keep secrets out of both the HTML and this markdown. No IPs, no hostnames that map the house, no private repo names, no tokens. Machine roles are enough for a public doc.
