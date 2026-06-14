# AGENTS.md

This file gives repository-editing guidance for future agents and automated assistants working on UDAM.

UDAM means **Uncertainty-Diffusion Anchor Model** / **不確実性拡散アンカーモデル**.

The current project phase is GitHub repository completion and stabilization, not theory expansion, external posting, or paperization.

## 1. Project identity

UDAM is a timer-derived practical synthesis about anchor loss, partial uncertainty, re-anchoring, observation value, and boundary-risk-constrained expansion.

The minimal timer seed is:

```text
τ = K + U + R
```

where:

- `K` is the known interval before anchor loss;
- `U` is the unknown interval during anchor loss;
- `R` is the re-anchored interval after restart;
- `τ` is the current position.

Core wording to preserve:

```text
partial uncertainty does not imply total invalidation
lost anchor does not imply future anchor invalidation
```

Japanese rendering:

```text
過去のアンカー喪失は、未来の有効観測を無効化しない。
```

## 2. Current phase rule

Do not add new UDAM theory unless explicitly requested by the maintainer.

The current work is to complete and stabilize the GitHub repository:

```text
English theory
reader-facing explanations
figures and diagrams
literature-support routing
repository structure
safe wording
simulation disclaimers
repository completion status
```

Do not create external-publication drafts, Quora-specific files, or paperization work unless explicitly requested.

Prefer compression, routing, consistency checks, and completion status over expansion.

## 3. Source-of-truth map

Use the following routing unless the maintainer changes it:

| Claim or content type | Source of truth | Supporting layer |
|---|---|---|
| Public landing page | `README.md` | `docs/00_overview.md` |
| Compact conceptual overview | `docs/00_overview.md` | `FAQ.md` |
| Formal claims | `theory/` | `docs/10_formal_refinement.md` |
| Timer seed model | `docs/01_timer_model.md` | `docs/11_timer_three_layer_model.md`, `docs/13_deterministic_event_scope.md` |
| Practical protocol | `docs/14_practical_reanchor_protocol.md` | `docs/15_application_cautions.md`, `docs/16_adaptive_observation_cadence.md`, `docs/18_adaptive_expansion_factor.md` |
| Failure boundaries | `docs/21_failure_decision_tree.md` | `docs/06_failure_cases.md`, `theory/counterexamples.md` |
| Literature support | `docs/17_literature_support_map.md` | `notes/literature_verification.md`, `docs/22` through `docs/31` |
| Visual explanation | `docs/32_visual_explanation_layer.md` | `assets/diagrams/`, `assets/figures/`, `docs/50_visual_rendering_audit.md` |
| Simulation sanity checks | `docs/39_simulation_sanity_checks.md`, `docs/49_extended_simulation_sanity_checks.md` | `simulations/` |
| Changelog policy | `docs/41_changelog_maintenance_policy.md` | `docs/42_changelog_catchup_entry.md`, `docs/51_release_history_routing_decision.md` |
| Notation audit | `docs/43_notation_consistency_audit.md` | `theory/variables.md`, `theory/propositions.md`, `theory/proofs.md` |
| Contraction-rule decision | `docs/44_contraction_rule_decision.md` | `docs/18_adaptive_expansion_factor.md`, `docs/21_failure_decision_tree.md` |
| Publication readiness | `docs/45_publication_readiness_audit.md` | `docs/47_remaining_work_register.md` |
| README / overview compression | `docs/46_readme_overview_compression_decision.md` | `README.md`, `docs/00_overview.md` |
| Remaining work register | `docs/47_remaining_work_register.md` | `ROADMAP.md` |
| Japanese explanation | `docs/ja/README.md` | `docs/ja/*` |
| Presentations and drafts | `drafts/` | `README.md`, `docs/00_overview.md` |

When a claim is duplicated, keep the detailed version in its source-of-truth layer and make the duplicate a short pointer.

## 4. Claim routing rules

General rule:

```text
repeat slogans, not derivations
repeat navigation, not full arguments
repeat warnings, not whole sections
```

Do not let README, overview, drafts, figures, or simulations silently become source-of-truth documents.

Use `theory/` for formal claims. Use `docs/17_literature_support_map.md` and `notes/literature_verification.md` for literature claims.

## 5. Literature claim rules

Literature support must remain graded. Do not collapse component-level support into proof of the whole synthesis.

Allowed labels include:

```text
direct support
partial support
analogy only
not supported
requires wording correction
UDAM-specific synthesis
```

Safe interpretation:

```text
The literature supports components of UDAM.
It does not prove the full UDAM synthesis.
```

## 6. Formal claim rules

Formal claims belong in `theory/` first.

Reader-facing documents may summarize formal claims, but should route back to the formal source.

Maintain these distinctions:

```text
state-informative != favorable
small != useful
local success != global expansion permission
component support does not prove full synthesis
```

Do not replace existing decision theory, Bayesian decision theory, active inference, sequential analysis, bandit theory, online algorithms, or behavioral activation with UDAM language.

## 7. Visual claim rules

Visual artifacts summarize the theory. They do not authorize, prove, validate, or extend the theory.

Editable visual sources live in:

```text
assets/diagrams/
```

Rendered reader-facing figures live in:

```text
assets/figures/
```

Older diagram rendering decisions route through:

```text
docs/50_visual_rendering_audit.md
```

When editing figures, update the Mermaid source first when possible, then render the SVG output.

## 8. Simulation claim rules

Simulations in this repository are toy demonstrations and sanity checks.

Use:

```text
toy demonstration
sanity check
not empirical validation
```

Do not use:

```text
validated
confirmed
proved
empirical support
```

The current simulation layer demonstrates five limited patterns:

```text
Timer re-anchor: R can reduce the relative influence of U.
Observation value: state-informative observations can still be unfavorable when cost is high.
Expansion boundary risk: large r_i can become unfavorable under boundary risk or correction cost.
Repeated checking: MOV_i can become non-positive after repeated observation under toy assumptions.
Boundary-risk sensitivity: harsher risk/correction settings can shrink or eliminate favorable expansion factors.
```

These results do not establish external validity.

## 9. Draft disclaimer rules

`drafts/` contains downstream presentations.

Drafts may explain or package the model, but they do not define it.

Do not continue paperization or external-publication drafting unless explicitly requested.

If a draft conflicts with `theory/`, `docs/17_literature_support_map.md`, `notes/literature_verification.md`, or `docs/32_visual_explanation_layer.md`, treat the source-of-truth file as authoritative.

## 10. README and overview rules

Keep `README.md` short.

README should:

```text
identify the project
state the minimal model
route readers to stable documents
warn against common misreadings
```

README should not:

```text
carry long derivations
expand literature review
host detailed simulations
become a paper draft
```

Keep `docs/00_overview.md` compact. Move detailed derivations, literature checks, simulations, and policy notes to their dedicated files.

For the current compression decision, see:

```text
docs/46_readme_overview_compression_decision.md
```

## 11. Changelog and release-history rules

Keep `CHANGELOG.md`.

Use it only for milestone-level changes.

Do not backfill every missed micro-edit. Use `docs/41_changelog_maintenance_policy.md`, `docs/42_changelog_catchup_entry.md`, and `docs/51_release_history_routing_decision.md` before editing `CHANGELOG.md`.

Direct catch-up insertion into `CHANGELOG.md` is deferred until a patch-safe path exists. It is not a public-release blocker while `docs/42_changelog_catchup_entry.md`, `ROADMAP.md`, `docs/47_remaining_work_register.md`, and Git history preserve milestone history.

Avoid full-file replacement of long changelog content unless necessary.

## 12. Japanese sync rules

English Markdown is the current source of truth.

Japanese documentation should not be substantially expanded until the English structure stabilizes.

When syncing Japanese files, translate stable claims conservatively. Do not introduce stronger claims in Japanese than the English version supports.

## 13. Safe wording and banned wording

Avoid or remove:

```text
UDAM is proven
UDAM is empirically validated
UDAM is confirmed by simulation
UDAM replaces decision theory
UDAM is therapy
UDAM treats depression
Any small action is useful
More information is always better
Double after success
Local success proves global safety
Literature proves UDAM
Visual artifacts prove the theory
Drafts define the model
```

Prefer:

```text
first-pass complete
toy demonstration
sanity check
reader-facing layer
source-of-truth routing
component-level support
UDAM-specific synthesis
not empirical validation
not proof
not source of truth
```

For high-stakes domains, including medical, clinical, financial, security, and safety-critical decisions, use neutral cautionary wording. Do not present UDAM as advice, diagnosis, treatment, risk approval, or operational validation.

## 14. Editing workflow rules

Before changing an existing GitHub file, fetch the current file and SHA.

Before creating a new file, confirm that the target path does not already exist.

Prefer small, scoped edits.

Be especially careful with large files such as:

```text
README.md
CHANGELOG.md
long theory files
long literature verification files
```

Do not perform broad repository rewrites while making a routing or policy edit.

## 15. Preferred next tasks

Good next tasks:

```text
1. Repository completion check across README, ROADMAP, AGENTS, docs/47, docs/48, simulations/README, and docs/ja/README.
2. Full Japanese synchronization only if needed for repository readability.
3. Optional repository-facing simulation plots or further toy sensitivity checks, still labeled toy demonstrations / sanity checks.
```

Tasks no longer immediate blockers after the latest stabilization pass:

```text
agent editing guidance
notation consistency audit
contraction rule decision
README / overview compression decision
publication-readiness audit
remaining-work register
paper draft cleanup first pass
minimal Japanese source-of-truth guardrail
extended toy simulation pass
older diagram rendering audit
release-history routing decision
empirical validation for current repository completion
paperization for current repository completion
external-publication drafting
```

Bad next tasks:

```text
adding unsupported new theory
inflating README
presenting simulations as validation
turning drafts into source-of-truth files
making strong high-stakes application claims
creating Quora-specific or external-publication files unless explicitly requested
```
