# 12 — Getting another machine into the Bots rail (SSH vs Remote gateway)

**Date:** 2026-10-18 · Hermes Desktop's multi-connection registry, learned the hard way
across two family machines with opposite constraints.

The Desktop app's **Bots** rail is not limited to profiles on this PC. Under
**Settings → Gateways** lives a connection registry (`connections.json` in the app
home, version 2). Every registered gateway contributes its profiles as bots; handles
disambiguate as `@profile-device` when names collide. A *bot* is a **profile**, not a
machine — one machine with four profiles gives you four rows.

There are two practical kinds, and the choice is usually made for you by one question:
**does the other machine allow SSH?**

## Path 1 — SSH connection (when Remote Login is on)

- Add connection → **SSH**, host as `user@ip` (or an `~/.ssh/config` alias); the app
  uses system OpenSSH in `BatchMode`, so your fleet `IdentityFile` applies.
- The clever part: the remote's dashboard does **not** need to be running or exposed.
  The Desktop opens a tunnel and starts the dashboard on demand, then adopts a session
  token through the tunnel. SSH kind = zero remote daemons to babysit.
- Rows stay **On demand** until first opened. A reachable-but-undialed connection is
  normal, not broken.
- Keep **Primary = this device**; adding a connection must not move your Sessions
  workspace.

## Path 2 — Remote gateway (when SSH is off *on purpose*)

A privacy boundary like "this laptop never runs sshd" rules path 1 out. The supported
alternative is a **Remote gateway** connection to a running `hermes serve`:

1. On the remote machine, put dashboard credentials in its `~/.hermes/.env`:
   `HERMES_DASHBOARD_BASIC_AUTH_USERNAME` / `_PASSWORD` / a stable `_SECRET`
   (without the secret every restart logs you out).
2. Run the backend bound to a reachable address:
   `hermes serve --host 0.0.0.0 --port 9119`
   Non-loopback binding **automatically engages the auth gate** — the gate is a
   consequence of the bind, not an extra flag.
3. Keep it alive: a systemd unit on Linux; a **LaunchAgent** plist on macOS
   (`RunAtLoad` + `KeepAlive`, ProgramArguments through a login shell so PATH works).
4. In the app: Add connection → **Remote gateway** → URL `http://<lan-ip>:9119` →
   sign in with those credentials → **Test** (it probes HTTP *and* WebSocket, so a
   pass means chat actually works).

Username/password is the quick path for a **trusted LAN only**. Anything beyond that
should use the Portal OAuth provider (`hermes dashboard register`). Never port-forward
a basic-auth backend.

## What this is *not*

- **A2A** (agent-to-agent, its own ports and tokens) is a different wire. It lets two
  Hermes agents exchange tasks without any Desktop being open, and it will never show a
  row in the Bots rail. A machine can run both: one thin A2A lane for one-line asks,
  one full gateway connection for the rail.
- **Not a backup.** Connecting a machine's gateway shows its sessions and profiles;
  it does not copy anything over.

## The privacy shape, before connecting

This is the part nobody tells you: a gateway connection rosters **every profile on that
gateway**, not one profile you picked. So before the first sign-in, agree what's fair
game with that machine's owner. Rows can be **Hidden per Desktop** after connecting,
which removes them from your rail but is presentation, not a permission wall.

Practical rules we keep:

- Credentials change hands **in person**. Never through a chat app, and never inside an
  A2A message — agent channels scrub credentials anyway.
- A laptop lid closed = the row errors until it wakes. Cosmetic; don't "fix" it.
- DHCP leases drift. A router reservation (or a hostname) keeps the URL honest.
- Rollback is two commands: stop/remove the service, delete the credential lines. The
  machine is untouched otherwise.

## Checklist that survived contact with reality

```text
[ ] decide: SSH allowed?  yes -> path 1 | no -> path 2
[ ] path 2: creds in .env + stable secret, serve bound, keepalive unit
[ ] owner agreed on which profiles are fair game (whole gateway, remember)
[ ] Add connection, Test -> Reachable (HTTP+WS)
[ ] hide rows that shouldn't be in the rail
[ ] primary still = this device; Sessions workspace didn't move
```

Official docs worth reading once: Hermes Desktop → *Connecting to a remote backend*,
and *Multi-connection Desktop*.
