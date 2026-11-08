# Ops Console desktop plugins (scrubbed method)

How monerostar runs a **live fleet glance** inside Hermes Desktop without living in three browser tabs.

## What it is

One Desktop plugin pane (**Ops Console**) that polls local board APIs:

| Board | Default port | Role |
|-------|--------------|------|
| Usage | 8787 | Fleet token / cost cycle |
| Miner | 8789 | Hashrate, lottery share, node |
| Think | 8790 | Active session tool/token snapshot |

Cards refresh every few seconds. Full boards stay available via Open when you need charts or long trails.

A second plugin (**Think HUD**) keeps a deeper live tool trail on the gateway event stream. It stays **palette-only** so the sidebar has one home: Ops Console.

## What we looked for first

- Community **Token Pulse** style widgets (X build-in-public): inspiration only, not an install pack we could drop in.
- Upstream requests for **status-bar token usage** (e.g. product feature requests): core Hermes product surface, not multi-board fleet ops.
- TUI ambient widgets: different surface (`hermes --tui`), not Desktop cards.

Nothing public matched **usage + miner + session think** in one Desktop pane for a multi-host home fleet. So this pattern is original operator work, not a fork of someone else's console.

## Pattern (portable ideas)

1. Keep heavy boards as small local HTTP servers with `/data.json` (stdlib Python is enough).
2. Add a thin Desktop plugin that `fetch`es those JSON endpoints and renders cards with `@hermes/plugin-sdk`.
3. Startup launchers (hidden VBS or equivalent) so boards survive reboot.
4. One sidebar entry. Deep tools stay palette/keybind.

## Safety

- Localhost only in the default plugin.
- No wallets, pool user strings, or API keys in plugin source or public docs.
- Private desk holds host paths and Startup wiring; public notes stay method-only.

## Related monerostar surfaces

- Public fleet CLI/HTML: `monerostar/monero-fleet-console`
- Private multi-host desk: `monerostar/hermes-fleet-desk` (`hosts/windows-tech/ops-console`, `think-hud`, usage/miner dashboards)
- Desktop Plugin SDK: Hermes docs developer-guide desktop-plugin-sdk

## Status

Lived and promoted on a Windows tech daily driver, 2026-08. Treat as a **pattern pack**, not a one-click product installer for every OS.
