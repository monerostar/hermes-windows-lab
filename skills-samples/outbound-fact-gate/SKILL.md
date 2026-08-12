---
name: outbound-fact-gate
description: "Gate ready emails: facts, tone, leaks before send."
version: 1.0.0
author: Dustin Baerg (monerostar), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [email, fact-check, review, legal-safe, parenting, outbound, ship-gate]
    category: productivity
    related_skills: []
---

# Outbound Fact Gate

Pre-send review for emails and short messages that will leave the human’s control.
Same spirit as a careful code review before merge: **inventory claims → bind sources → catch tone/leak risk → verdict → human sends.**

**Not legal advice. Not strategy coaching. Never auto-send.**

## When to Use (load this skill)

### Explicit
- “fact gate”, “fact check this”, “review before I send”, “is this solid?”
- “check this email”, “any landmines?”, “ready to send?”

### Natural heat (non-technical users — do not wait for jargon)

Load and run the gate when **more than one** of these is true, or when any single high-stakes signal is strong:

| Signal | Examples |
|--------|----------|
| **Done-feeling draft** | Full polished email, “final version”, “this is what I’m sending”, “send this after you look” |
| **Sensitive audience** | Lawyer/counsel, coparent/ex, school admin, court-adjacent, landlord, HR, insurance, debt, medical admin |
| **Hard claims** | Dates, money, schedules, quotes, “always/never”, accusations, legal labels, medical/school statements |
| **Exhibit risk** | Could be forwarded, filed, or screenshot later |

**Default when heat is present:** run the gate **before** offering a “looks good, send it” vibe.
If the user only wanted a tiny wording tweak on a low-stakes note, skip the full card — but still flag any unsourced hard claim you notice.

### Don’t use for
- Pure brainstorming with no outbound draft
- Journaling / venting that will not be sent
- Code review (use code-review skills)
- Auto-filing legal packages or sending mail

## Hard rules

1. **Human sends.** Draft/review only. Never call send/mail tools unless they explicitly order send **after** a SHIP verdict and a final paste they approved.
2. **No invented facts.** Missing source → HOLD or soften to belief/request. Never fill gaps from memory of prior chats unless the user re-states or attaches the source this turn.
3. **Separate layers:** FACT (sourced) · OPINION/FEELING · ASK/REQUEST · LEGAL LABEL (only if their counsel/docs already use it or they insist after warning).
4. **Confidential stays local.** Do not push case narrative, full emails, kids’ detailed records, or medical detail to git, public repos, shared desks, or multi-host drops. Status may say “fact-gate skill installed” only.
5. **Prefer stronger models on high heat.** If a thrift/free model drafted, re-run the gate on the user’s normal strong model when stakes are high.
6. **Short card beats essay.** Non-technical users need a clear verdict and a few fixes, not a brief.

## Procedure

### 1. Catch the outbound unit
Identify: audience class, purpose in one line, channel (email/text/portal), and the exact text under review.
Done when you can state audience + purpose without guessing.

### 2. Inventory hard claims
List every claim that could be checked or used against them later:
- dates, times, deadlines, durations, percentages
- money, amounts owed/paid
- quotes and “you said / they said”
- always / never / refused / failed / harassed / violated
- medical, school, behavior, attendance statements
- legal characterizations

Done when the list is complete for the draft (exhaustive for the text given).

### 3. Bind sources
For each hard claim, require one:
- pasted email/text/order/agreement language
- calendar or log entry with date
- bank/receipt line
- school/medical note the user provided
- **or** rewrite as opinion/request (“I’m concerned that…”, “Please confirm…”)

No source → **HOLD** or rewrite. Do not silently keep the hard form.
Done when every hard claim is sourced, softened, or listed under Blockers.

### 4. Consistency pass
- Names, spellings, kids’/parties’ identifiers consistent
- Math and date ranges coherent
- Schedule/order language matches the period cited (don’t mix old and new regimes)
- Don’t cite a report outside the dates it covers

Done when contradictions are listed or cleared.

### 5. Tone and exhibit risk
Assume the message can be **forwarded or filed**.
Flag: sarcasm, insults, gotchas, new unsourced accusations, oversharing third-party private data, dumping full clinical detail when one factual line would do, promising legal outcomes.
Audience defaults:

| Audience | Posture |
|----------|---------|
| Counsel / lawyer | Calm, cited, questions OK; strategy as questions not conclusions |
| Coparent / ex | Short, operational, kid-centered; one clear ask |
| School / third party | Minimal necessary facts; no case narrative |
| Work / landlord / admin | Factual, dated, one ask; no venting |

Done when tone risks are in Blockers or Warnings.

### 6. Leak / hygiene
- Secrets, account numbers, full medical dumps, other children’s data
- Reply-all / wrong-recipient traps if visible
- Attachments mentioned but missing
- Nothing from this review belongs in git

Done when hygiene notes are explicit or “none noticed.”

### 7. Verdict and optional rewrite
Emit the review card (below). On request, rewrite **only risky sentences** or a full safer draft — still human sends.
Done when verdict is SHIP, HOLD, or KILL with reasons.

## Review card (always use this shape)

```text
## Outbound Fact Gate

**To / channel:** …
**Purpose (one line):** …
**Verdict:** SHIP | HOLD | KILL

### Blockers (must fix)
- …

### Holds (confirm with you)
- …

### Solid
- …

### Suggested fixes
- (short; full rewrite only if asked)

### Leak / hygiene
- …
```

### Verdict meanings

| Verdict | Meaning |
|---------|---------|
| **SHIP** | Hard claims backed or properly softened; tone acceptable; no leak blockers. Human may send after their own read. |
| **HOLD** | One or more items need their confirmation or a missing source/attachment. |
| **KILL** | Wrong fact, unsafe framing, or should not go out as written. |

After SHIP, still say once: **you send it** from your mail app after a final read.

## Optional local habit (user choice)

If they want a private log later: date, audience class, verdict, one-line purpose — **no body text** unless they keep a local-only folder.
Never write that log to a shared git desk.

## Pitfalls

| Pitfall | Instead |
|---------|---------|
| “Looks great!” on a heated draft with no claim pass | Run the card |
| Inventing a date/amount from an old session | HOLD; ask them to paste source |
| Ghostwriting a trial brief into a coparent email | Short operational ask |
| Softening so hard the ask disappears | Keep one clear request |
| Dumping review + full case file into git/status | Skill install note only |
| Auto-send “to be helpful” | Never |
| Waiting for the user to say “fact gate” when heat is obvious | Natural heat triggers above |
| Using thrift model as final gate on lawyer-bound mail | Prefer their strong model |

## Verification

- [ ] Skill loaded when heat or explicit ask present
- [ ] Every hard claim sourced, softened, or blocked
- [ ] Verdict is exactly SHIP, HOLD, or KILL
- [ ] No send action without explicit post-SHIP human order
- [ ] No confidential body text written to shared git paths
