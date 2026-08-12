# Outbound Fact Gate (skill sample)

**Skill:** `skills-samples/outbound-fact-gate/`  
**Job:** Before a human sends a sensitive email, Hermes runs a short review card — facts backed, tone safe if forwarded, no leaky overshare.

## Why

People send “done” drafts that still have wrong dates, unsourced hard claims, or heat that ages badly as an exhibit. This skill is the email twin of careful PR review: **gate, then human ships.**

## Install

Copy the whole folder into a profile skills tree under `productivity/outbound-fact-gate/`, then start a new chat (or reload skills).

## Natural heat (non-technical)

The user should not need to say “fact gate.” If the draft feels finished and the audience is sensitive (lawyer, coparent, school, HR, landlord) or the text has hard claims, Hermes should run the gate on its own.

## Verdicts

| Verdict | Meaning |
|---------|---------|
| SHIP | Solid enough; human sends after one final read |
| HOLD | Confirm a fact/source/attachment first |
| KILL | Do not send as written |

## Hard rules

- Not legal advice  
- Never auto-send  
- No case bodies in git  
- Prefer a strong model on high-stakes gates  

## Related

Desk install path for Michelle-class hosts: private `hermes-fleet-desk` → `shared/skills/outbound-fact-gate/` + host outgoing note.
