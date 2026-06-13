# 09 Open Questions

This file lists unresolved questions for the Uncertainty-Diffusion Anchor Model.

## Q1. How should the diffusion rate be estimated?

The model uses:

```text
P_{t+Δt} = P_t + QΔt
```

But `Q` may depend on domain, task complexity, memory decay, external volatility, and emotional load.

Open problem:

> What determines `Q` in each domain?

## Q2. What is the minimum condition for an anchor?

A candidate anchor must constrain the belief state.

Open problem:

> How much uncertainty reduction is required for an action to count as a re-anchor?

## Q3. How should informational value be measured?

The model uses:

```text
I(a)
```

Open problem:

> Should `I(a)` be defined as variance reduction, entropy reduction, expected value of information, or decision improvement?

## Q4. How can compulsive checking be separated from re-anchoring?

Both may look like repeated action.

Open problem:

> What threshold separates useful repeated measurement from low-information compulsive checking?

## Q5. How does intervention value interact with information value?

Some actions both measure and improve the state.

Example: solving one problem reveals skill and trains skill.

Open problem:

> How should `I(a)` and `B(a)` be separated in practice?

## Q6. What are the strongest counterexamples?

The model should identify domains where small informative action is not advantageous.

Open problem:

> Under what conditions is inaction or waiting optimal?

## Q7. How should state dynamics and belief dynamics be separated?

UDAM currently focuses on belief uncertainty:

```text
P_t = Var(S_t | D_t)
```

But an unanchored interval may involve both state change and belief change.

Open problem:

> When does uncertainty increase because the world changed, and when does it increase because the agent lost epistemic contact with a stable state?

## Q8. How should the model be tested?

Possible tests:

- interrupted timer tasks;
- interrupted work recovery;
- learning restart tasks;
- task-state recall after delay;
- small-action versus no-action comparisons.

Open problem:

> Which experiment best isolates uncertainty diffusion and re-anchoring?
