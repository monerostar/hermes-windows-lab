# Optional: free-model play profile

This note describes an OPTIONAL, low-risk pattern for learning with Hermes using
only free Nous models. It is not required to run the lab. It is not for production
work or fleet tasks.

## Why it exists

A separate "play" profile keeps experiments away from the profile that drives
hands-on computer work. That separation means a wrong model, a bad setting, or a
broken skill can never affect the profile used for real tasks.

## How it looks

- A dedicated profile in Hermes (for example, a name you choose for casual work).
- A dedicated play folder on the machine. All work, checkouts, and notes live there.
- No link to fleet tasks, mine configs, or private keys. Nothing in git that should
  not be public.

## Rules that make it safe

1. Free models only. Use model IDs that end with the `:free` suffix. No paid tiers.
2. Stay in the play folder. Keep experiments and checkouts inside it. Do not reach
   into other profiles' skills, memory, or configs without clear intent.
3. No secrets in git. No API keys, no tokens, no wallets, no mine configs. If a
   script needs a secret, read it from an environment variable, never hard-code.
4. Manual sessions first. Do not set up unattended scheduled jobs until the pattern
   is steady and the owner signs off. Optional: a session fire loop can run each free
   model once plus one free MoA when you start play. One clear experiment per slot.
5. Leave a findings trail. Write short notes to `review/FINDINGS.md`. Flag anything
   important to the main reviewer in `review/inbox/`.

## When to use it

- Learning Git and GitHub with real but harmless changes.
- Testing small skills, helper scripts, or docs.
- Reading public repos and taking safe notes.
- Trying new Hermes features without risk to main work.

## When NOT to use it

- Anything that handles live fleet tools, wallet data, or private credentials.
- Work that must stay with the main or tech profile by design.

## Test plan

1. Create a new Hermes profile for play, separate from main and tech.
2. Set models that end with `:free`.
3. Do a small edit, commit, and push to a draft branch.
4. Confirm no secrets are present before pushing.

This pattern exists to make learning safe and reversible.
