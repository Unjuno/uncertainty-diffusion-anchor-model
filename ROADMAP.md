# Roadmap

## v0.1: Theory skeleton

Goal: Fix the minimal theory structure.

- [x] README
- [x] license notice
- [x] timer model
- [x] variables
- [x] assumptions
- [x] axioms
- [x] propositions
- [x] proofs
- [x] counterexamples

Status: complete as initial skeleton.

## v0.2: Applications

Goal: Add structured application examples.

- [x] learning recovery
- [x] work interruption recovery
- [x] health tracking
- [x] relationship uncertainty
- [x] life strategy after failure
- [x] missed re-anchor miscalculation examples
- [x] happy miscalculation examples
- [x] false comfort miscalculation examples

Status: initial examples added. Further examples can be added later.

## v0.3: Related work

Goal: Map the model to existing fields without overclaiming novelty.

- [x] Bayesian filtering
- [x] Kalman filtering
- [x] POMDP / belief state
- [x] active inference
- [x] value of information
- [x] behavioral activation
- [x] cognitive anchoring

Status: initial related-work map added. Needs expansion and citations if developed into a paper.

## v0.4: Diagrams

Goal: Add conceptual diagrams.

- [x] uncertainty diffusion without anchors
- [x] lost interval and re-anchored interval
- [x] timer relative dilution
- [x] action value flow
- [x] failure case taxonomy
- [x] observability value flow

Status: Mermaid source diagrams added under `assets/diagrams/`. Rendered figures can be added later under `assets/figures/`.

## v0.5: Formal refinement

Goal: sharpen the mathematical status of the model.

- [x] separate cognitive uncertainty from physical state change
- [x] distinguish absolute uncertainty from relative uncertainty dilution in the timer model
- [x] formalize the possibility that absolute uncertainty increases while relative influence decreases
- [x] add fixed-target scope for the timer seed model
- [x] add controllability boundary for actionable versus uncontrollable uncertainty
- [x] add notation for observation update after re-anchoring
- [x] formalize diminishing information value for repeated checking
- [x] define conditions under which `Q > 0`
- [x] decide whether `P_t` is variance, covariance, entropy, or a general uncertainty functional

Status: complete as formal refinement layer. Core uses variance/covariance-like `P_t`; general uncertainty functional `𝓤_t` is reserved for future extension.

## v0.6: Public-facing safety and clarity

Goal: keep examples useful while preventing misreadings.

- [x] add high-stakes example policy
- [x] require neutral wording for high-stakes examples
- [x] distinguish theory failure cases from missed-application miscalculations
- [x] add a concise public-facing FAQ
- [ ] render diagrams for easier reading

Status: public-facing clarification is mostly complete. Remaining work is rendered figures.

## v0.7: Observability value model

Goal: formalize the value of observation as conditional-action value.

- [x] add observability value model
- [x] add observability variables to `theory/variables.md`
- [x] add observability propositions
- [x] add observability proof sketches
- [x] add upside uncertainty / happy miscalculation
- [x] add downside uncertainty / false comfort miscalculation
- [x] add fixed-target disbelief inequality
- [x] sync observability model into README
- [x] sync observability model into `docs/10_formal_refinement.md`
- [x] sync observability model into `drafts/paper_outline.md`
- [x] add observability consistency checks
- [x] add an observability diagram

Status: complete as a formal integrated layer. Remaining future work is rendering diagrams and possibly expanding examples.

## v1.0: Stable theory note

Goal: Publish a coherent theory note with definitions, propositions, proofs, examples, and limitations.

Remaining work:

- refine definitions;
- strengthen proofs;
- add rendered figures;
- add a formal novelty statement;
- expand related work;
- add Japanese and English paper-style drafts;
- audit notation consistency across timer, action-value, and observability layers.
