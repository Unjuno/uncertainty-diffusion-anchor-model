# 46 README and Overview Compression Decision

This document records a first-pass decision about whether `README.md` and `docs/00_overview.md` need immediate compression.

The purpose is not to rewrite either file.

The purpose is to prevent unnecessary churn while preserving the rule that README and overview should not become bloated source-of-truth documents.

## Decision status

Status:

```text
first-pass decision recorded
```

Decision:

```text
Do not perform immediate broad compression.
Use targeted compression only when a section duplicates detailed derivations, literature verification, simulation results, or policy notes already housed elsewhere.
```

Reason:

```text
README.md is long but still mostly functions as a landing page and routing map.
docs/00_overview.md should remain compact, but no urgent broad rewrite is required without a targeted duplication finding.
```

## README role

README should answer:

```text
What is UDAM?
What is the minimal model?
Where should readers go next?
What should readers not overclaim?
```

README should not answer in full:

```text
all formal derivations
all literature verification details
all simulation results
all visual policy details
all maintenance policy details
```

## Current README decision

Current decision:

```text
Leave README structurally intact for now.
```

Permitted small additions:

```text
links to new routing or maintenance documents
one-line status updates
short warnings that prevent major misreadings
```

Avoid:

```text
adding long explanations of AGENTS.md
copying notation audit tables into README
copying simulation findings into README
turning README into a paper abstract plus literature review
```

## Overview role

`docs/00_overview.md` should answer:

```text
What is the conceptual model?
How do the major pieces relate?
Where does the reader go for formal details?
```

It should not become:

```text
a full proof document
a literature review ledger
a simulation report
a policy manual
```

## Compression triggers

Compress README or overview only when one of these is true:

```text
1. A section repeats a detailed derivation already in theory/ or docs/10.
2. A section repeats literature verification already in docs/17 or notes/literature_verification.md.
3. A section repeats simulation details already in docs/39 or simulations/.
4. A section repeats visual policy already in docs/32 or assets/figures/README.md.
5. A section repeats maintenance policy already in AGENTS.md or docs/33 through docs/46.
```

## Safe compression pattern

Use this pattern:

```text
replace long explanation -> one-sentence summary + link to source-of-truth file
```

Do not use this pattern:

```text
remove section entirely without preserving navigation
```

## Current result

Result:

```text
No immediate broad README or overview compression is required.
Targeted compression remains a future cleanup task, not a blocker.
```

Recommended next action:

```text
If README is edited again, add only short routing links and avoid expanding explanatory prose.
```
