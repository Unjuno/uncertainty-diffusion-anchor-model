# 38 Visual Claims Routing Audit

This document completes the first Stage 4 routing task for visual claims.

The goal is to prevent diagrams, rendered figures, README visual paths, and overview visual paths from becoming independent sources of theory claims.

## Routing principle

Visual claims should have three layers:

```text
visual explanation policy -> docs/32_visual_explanation_layer.md
editable visual source -> assets/diagrams/
reader-facing rendered output -> assets/figures/
```

The formal and conceptual source of the underlying claims remains in:

```text
theory/
docs/10_formal_refinement.md
docs/17_literature_support_map.md
docs/21_failure_decision_tree.md
```

Visual files should clarify and route.

They should not introduce new theory.

## Source-of-truth split

| Visual claim type | Primary source | Supporting source | Visual behavior |
|---|---|---|---|
| Visual layer purpose and policy | `docs/32_visual_explanation_layer.md` | `assets/figures/README.md` | define what visual artifacts may and may not claim |
| Editable diagram content | `assets/diagrams/` | `docs/32_visual_explanation_layer.md` | editable source; still not formal theory source |
| Rendered figure output | `assets/figures/` | `assets/diagrams/` | reader-facing artifact; not primary source |
| Formula meaning | `theory/variables.md`, `docs/10_formal_refinement.md` | `docs/32_visual_explanation_layer.md` | diagrams may display formulas but not redefine them |
| Proposition-like claim | `theory/propositions.md` | `docs/05_propositions.md` | diagrams may summarize only |
| Failure boundary | `docs/21_failure_decision_tree.md`, `docs/06_failure_cases.md`, `theory/counterexamples.md` | `docs/32_visual_explanation_layer.md` | diagrams may show decision flow |
| Literature support strength | `docs/17_literature_support_map.md`, `notes/literature_verification.md` | `assets/figures/literature_support_map.svg` | figure may summarize categories only |
| Reader visual path | `README.md`, `docs/00_overview.md` | `docs/32_visual_explanation_layer.md` | route readers to figures |

## Current visual source roles

### `docs/32_visual_explanation_layer.md`

Role:

```text
visual explanation policy and inventory
```

It should answer:

```text
what the visual layer is for
which visual artifacts exist
which common misreadings the visuals must avoid
which diagrams are rendered
where readers should start
```

It is the correct source for visual workflow and visual claim boundaries.

It is not the source for formal equations, propositions, or literature support claims.

### `assets/diagrams/`

Role:

```text
editable Mermaid source layer
```

It should hold diagram source files.

Mermaid files may contain short formulas or warnings, but those statements must already be supported elsewhere.

If a diagram needs a new concept, update the relevant theory or docs source first.

### `assets/figures/`

Role:

```text
reader-facing rendered output layer
```

SVG files are outputs derived from Mermaid sources.

They are useful for reading, embedding, and presentation.

They should not be edited as the primary source.

## Allowed visual claims

Visual artifacts may show:

```text
workflow order
decision checkpoints
short guardrails
formula labels
support categories
reader navigation
```

Examples:

```text
state-informative != favorable
local success does not imply global expansion permission
component support does not prove full synthesis
r_i is selected, not automatically 2
U being unknown does not automatically invalidate R
```

These are allowed because they are guardrails already supported by the main text.

## Disallowed visual claims

Visual artifacts should not introduce:

```text
new variables
new propositions
new proof steps
new support classifications
new application domains
new empirical claims
new therapeutic or clinical claims
new expansion rules
```

Do not allow diagrams to imply:

```text
Any small action works
More information is always better
Double after success
Local success proves global safety
Literature proves the whole model
UDAM is empirically validated
UDAM is therapy
```

## Required routing for new visual claims

When adding or changing a visual claim:

```text
1. Check whether the claim is already supported in docs/ or theory/.
2. If it is formal, update theory/ first.
3. If it is literature-related, update docs/17 and notes/literature_verification.md first.
4. If it is a failure boundary, update docs/21, docs/06, or theory/counterexamples.md first.
5. Update the Mermaid source in assets/diagrams/.
6. Regenerate or manually update the SVG in assets/figures/.
7. Update docs/32_visual_explanation_layer.md if the visual inventory or policy changes.
8. Keep README and overview limited to visual routing links.
```

## Current route decision

The current source-of-truth routing is acceptable.

No immediate content moves are required.

The main procedural rule is:

```text
visual artifacts summarize theory; they do not authorize theory
```

## Stage 4 status update

Visual-claims routing audit: complete as first pass.

Next consolidation target:

```text
decide whether draft files need source-of-truth disclaimers
```
