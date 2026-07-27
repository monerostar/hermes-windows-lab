# Hermes Stack Map

**Living systems portrait** of the multi-profile Hermes world on this Windows host.  
**Visual:** [hermes-stack-map.html](./hermes-stack-map.html) (open in browser · **animated** CSS/SVG; Pause motion toggle)  
**Concept art:** [assets/hermes-stack-map-concept.png](./assets/hermes-stack-map-concept.png)  
**Date:** 2026-07-25 · Option C from brainstorming session

## What this is

A calm map of how the pieces relate — not a full inventory dump and not a backup.

| Artifact | Job |
|----------|-----|
| **This HTML map** | See the whole system |
| **hermes-backup** (private) | Scrubbed portable DR bits |
| **Borgmatic** | Real disk disaster recovery |
| **This lab** | Learning docs |

## Layers (north → south on the diagram)

1. **Human** — operator in the loop; no fake urgency  
2. **Surfaces** — Desktop (tech), TUI/CLI, Gateway (main)  
3. **Profiles** — main · tech · house · lifestyle · x  
4. **MoA ladder** — nous-cheap → **balanced** (default) → deep → free; solo Grok default  
5. **Main cron** — fleet watchdog, monerod window, glances, weekly hygiene  
6. **Shared integrations** — Trello, AgentMail, Hound (tech), GWS, Obsidian, GitHub, xurl  
7. **Monero fleet** — Fleet Console + Hive + HashVault + monerod + xmrig  
8. **Storage** — C/D/E–H/K, HermesCold, session policy  
9. **Backup** — Borg vs scrubbed GitHub vs lab  

## Profile cheat sheet (live 2026-07-25)

| Profile | Role | Skills ~ | Notes |
|---------|------|----------|--------|
| **main** | Gateway + crons | 110 | 8 scheduled jobs; orchestrator home |
| **tech** | Hard work / desktop | 128 | Hound + Trello MCP; fleet console home |
| **house** | Home / projects | 100 | agentmail + trello |
| **lifestyle** | Personal / lifestyle | 102 | GWS; cold export bias |
| **x** | Social monerostar | 105 | xurl; garden skills |

**All:** default model `grok-4.5` / `xai-oauth`, MoA default `nous-balanced`, web via Nous gateway Firecrawl.

## MoA ladder (operator)

```text
Grok alone  →  Ollama solo (simple)  →  nous-cheap  →  nous-balanced★  →  nous-deep (rare)
```

- Switch only with `/model nous-*` (or picker) — bare chat words do not switch  
- No Kimi in MoA ensembles  
- Image generation is a separate Nous-managed path  

## Web ladder (post Hound smoke)

1. Local files / vault / memory  
2. x_search / xurl for X  
3. **Nous `web_search` / `web_extract`** — daily default  
4. **Hound** — focus extract, PDF, crawl, stealth (tech)  
5. Personal Firecrawl key — emergency only  

## Main cron (gateway)

| When | Job | Mode |
|------|-----|------|
| 05:00 | X mentions glance | agent |
| 06:00 / 22:00 | monerod stop / start | no_agent |
| 15 */6 | Hive fleet fail-only watchdog | no_agent |
| 19:00 | Trello Life Board glance | no_agent |
| Sun 10 | Weekly vault hygiene | agent |
| Sun 11 | Weekly tech health | no_agent |
| Sun 12 | Weekly session maintenance | no_agent |

## Monero path

```text
monerod (local)  +  Hive (rig health)  +  HashVault (pool)
        \______________ Fleet Console ______________/
```

- Local path: `C:\Users\Admin\src\monero-fleet-console`  
- Wallet masked in UI; secrets stay in tech `.env`  
- xmrig standalone migration ongoing (away from Awesome Miner / GUPAX)

## Storage & cold

| Mount | Role |
|-------|------|
| C: | OS + Hermes profile homes |
| D: | HermesCold librarian, Immich archive, cold text |
| E–H | TerraMaster bulk |
| K: | Steam NVMe + Obsidian vault |
| F:\borg-repo | Borgmatic target (via WSL) |

Session policy (librarian): main hot ~30d; tech/house/x ~90d; titled sessions kept; lifestyle report/export bias.

## Related docs in this lab

1. [What is Hermes](./01-what-is-hermes.md)  
2. [Profiles main vs tech](./02-profiles-main-vs-tech.md)  
3. [GitHub CLI setup](./03-github-cli-setup.md)  
4. [Safety: no secrets](./04-safety-no-secrets.md)  
5. [Backup vs lab](./05-backup-vs-lab.md)  
6. **This map**  

## Refresh

When the stack drifts (new MCP, major MoA change, new profile):

1. Re-scan profiles’ `config.yaml` + `cron/jobs.json`  
2. Edit the HTML boxes + this cheat sheet  
3. Optional: regenerate concept art  

Keep secrets out of both the HTML and this markdown.
