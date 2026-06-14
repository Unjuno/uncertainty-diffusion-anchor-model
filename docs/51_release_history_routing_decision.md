# 51 Release History Routing Decision

This document records the release-history routing decision after the changelog catch-up entries were prepared.

The purpose is not to remove `CHANGELOG.md`.

The purpose is to avoid risky broad replacement of a long changelog while still preserving milestone-level release history.

## Current decision

Status:

```text
release-history routing decision: first-pass complete
CHANGELOG.md catch-up insertion: deferred until patch-safe path exists
```

Decision:

```text
Do not treat direct CHANGELOG.md catch-up insertion as a public-release blocker.
Use docs/42_changelog_catchup_entry.md as the catch-up ledger until CHANGELOG.md can be patched safely.
```

Reason:

```text
CHANGELOG.md is long.
The current GitHub file update path replaces whole files.
Broad full-file replacement would create avoidable history and merge-risk.
```

## Current release-history layers

Use the following layers:

| Layer | Role |
|---|---|
| `CHANGELOG.md` | existing milestone-level changelog; keep it |
| `docs/42_changelog_catchup_entry.md` | prepared compact catch-up entries for missed milestone summaries |
| `ROADMAP.md` | current milestone status and next work |
| `docs/47_remaining_work_register.md` | active remaining-work register |
| Git history | fine-grained implementation history |

## Prepared catch-up entries

`docs/42_changelog_catchup_entry.md` currently stores compact proposed entries for:

```text
0.8.0 - Stage 3, Stage 4, and simulation sanity-check catch-up
0.9.0 - Agent guidance and stabilization-pass catch-up
0.10.0 - Draft, Japanese guardrail, and extended simulation catch-up
0.11.0 - Visual rendering audit catch-up
```

These are sufficient as a catch-up ledger for the current public repository state.

## When to edit CHANGELOG.md

Edit `CHANGELOG.md` only if at least one of these is true:

```text
1. A patch-safe update path is available.
2. The repository owner explicitly accepts full-file replacement risk.
3. A release tag requires CHANGELOG.md itself to contain the compact entries.
```

If none is true, leave `CHANGELOG.md` intact and rely on:

```text
docs/42_changelog_catchup_entry.md
ROADMAP.md
docs/47_remaining_work_register.md
```

## What not to do

Do not:

```text
rewrite the whole changelog casually
backfill every micro-edit
copy ROADMAP into CHANGELOG.md
copy docs/42 verbatim without checking placement and formatting
turn CHANGELOG.md into a development diary
```

## Public-release implication

Current implication:

```text
Missing direct catch-up insertion into CHANGELOG.md is not a blocker for repository-level publication.
```

Reason:

```text
Milestone history is still discoverable through docs/42, ROADMAP.md, docs/47, and Git history.
```

## Safe wording

Use:

```text
CHANGELOG catch-up entries are prepared in docs/42 and can be inserted later when a patch-safe path exists.
```

Avoid:

```text
CHANGELOG is complete.
CHANGELOG has been fully synchronized.
All release history is already in CHANGELOG.md.
```

## Result

Result:

```text
release-history routing: stable enough for public repository readiness
CHANGELOG.md direct insertion: deferred, not abandoned
```
