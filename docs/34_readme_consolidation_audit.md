# 34 README Consolidation Audit

This document completes the first README audit task in Stage 4.

The goal is not to make the README minimal immediately.

The goal is to decide which README sections should remain as entry-point material, which should route to source-of-truth documents, and which may be compressed later.

## Audit principle

README should remain the public routing document.

It may repeat short slogans and warnings.

It should not become the place where detailed derivations, literature grading, proof sketches, or full application logic live.

Recommended rule:

```text
README keeps orientation.
README links to detail.
README does not carry full detail.
```

## Section audit

| README section | Current role | Audit decision | Source-of-truth route |
|---|---|---|---|
| Title and opening description | public identity | keep | `README.md` |
| One-sentence summary | public orientation | keep | `README.md` |
| Current development policy | project status | keep, but short | `docs/33_project_note_consolidation.md`, `ROADMAP.md` |
| Visual entry points | reader routing | keep | `docs/32_visual_explanation_layer.md`, `assets/figures/README.md` |
| Core model | minimal concept | keep short | `docs/01_timer_model.md`, `docs/11_timer_three_layer_model.md` |
| General model | formula overview | keep as compact formula list | `docs/10_formal_refinement.md`, `theory/variables.md`, `theory/propositions.md` |
| If you want to use it now | practical routing | keep | `docs/14_practical_reanchor_protocol.md`, `docs/15_application_cautions.md` |
| Failure diagnostic | practical warning | keep short | `docs/21_failure_decision_tree.md`, `docs/06_failure_cases.md` |
| Five-stage refinement roadmap | project routing | keep short | `docs/20_five_stage_development_roadmap.md`, `ROADMAP.md` |
| Logical synthesis status | trust signal | keep short | `theory/logical_synthesis_review.md` |
| Novelty position | overclaim guardrail | keep | `docs/19_positioning_and_novelty.md` |
| Reading order | navigation | keep, but may split later | `docs/33_project_note_consolidation.md` |
| Repository map | navigation | keep | `docs/33_project_note_consolidation.md` |
| Development notes | maintenance routing | keep | `notes/`, `theory/` |
| Repository status | status snapshot | keep short | `ROADMAP.md` |
| License | required public information | keep | `LICENSE` |

## Findings

The README is longer than a minimal project landing page, but it is not yet dangerously duplicative.

Most sections are routing sections rather than full derivations.

The highest-risk sections for future bloat are:

```text
Core model
General model
Reading order
Repository status
```

These should remain compact.

They should not accumulate detailed proofs, literature explanations, or long examples.

## Keep as-is for now

The following sections are useful as stable entry material and should remain in README:

```text
One-sentence summary
Current development policy
Visual entry points
If you want to use it now
Failure diagnostic
Novelty position
Repository map
License
```

Rationale:

```text
they orient readers quickly
they prevent common misreadings
they route to deeper files
```

## Route, do not expand

The following sections may remain, but should route to deeper documents rather than expand inside README:

```text
Core model -> docs/01, docs/11, docs/13
General model -> docs/10 and theory/
Five-stage roadmap -> docs/20 and ROADMAP
Logical synthesis status -> theory/logical_synthesis_review.md
Development notes -> notes/ and theory/
```

## Possible later compression

The Reading order section may eventually be shortened if a separate navigation index is added.

Possible future replacement:

```text
For reading paths, see docs/33_project_note_consolidation.md.
```

But do not compress it yet.

At the current stage, explicit reading order is useful because the repository is still being consolidated.

## README should avoid adding

Do not add the following to README:

```text
full proof sketches
full literature review details
full application examples
clinical or high-stakes scenario details
new UDAM concepts
extended Japanese explanations
long changelog summaries
```

## README may repeat

README may continue repeating these short guardrails:

```text
lost anchor does not imply future anchor invalidation
partial uncertainty does not imply total invalidation
small action is not always good
state-informative does not mean favorable
local success does not imply global expansion permission
component support does not prove full synthesis
```

These repetitions are acceptable because they prevent predictable misreadings.

## Current decision

No README sections need immediate removal.

No detailed derivations were found that must be moved immediately.

The README should be treated as acceptable for now, with one maintenance rule:

```text
future additions to README should usually be links, not explanations
```

## Stage 4 status update

README duplication audit: complete as first pass.

Next consolidation target:

```text
docs/00_overview.md
```

The next audit should check whether `docs/00_overview.md` duplicates README or whether it properly serves as a slightly fuller conceptual overview.
