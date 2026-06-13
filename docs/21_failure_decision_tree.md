# 21 Failure Decision Tree

This document gives a compact decision tree for identifying whether UDAM applies, weakens, or fails in a given situation.

It is meant as a practical diagnostic tool.

## Purpose

UDAM should not be used as a vague rule such as:

```text
when uncertain, just do something
```

The correct diagnostic question is:

```text
Is there a low-cost, state-informative observation or action that can change belief, decision, or state?
```

## Step 1: Is there a relevant hidden state?

Ask:

```text
What state am I uncertain about?
```

If no relevant state can be named, UDAM is too vague to apply.

Failure pattern:

```text
unclear feeling -> no defined state -> vague action
```

Correction:

```text
name the state first
```

Examples:

```text
learning ability on this topic
current project blocker
available budget margin
relationship response state
```

## Step 2: Is the target fixed or at least locally fixed?

UDAM's timer seed model works best under:

```text
fixed target, uncertain position
```

If the uncertainty is mainly about whether the target itself exists or occurs, then the core model weakens.

Failure pattern:

```text
uncertain target occurrence -> treated as fixed target
```

Correction:

```text
separate target-occurrence uncertainty from position uncertainty
```

## Step 3: Can action affect the uncertainty?

Ask whether any available action can do at least one of these:

```text
observe the state
update belief
change the next decision
improve the state
```

If none apply, the uncertainty is outside the actionable core.

Failure pattern:

```text
external uncertainty -> treated as actionable uncertainty
```

Correction:

```text
treat it as external, deferred, or requiring outside information
```

## Step 4: Is the observation state-informative?

A valid re-anchor requires:

```text
P(y | S) != P(y)
```

Equivalent posterior form:

```text
P(S | y) != P(S)
```

If:

```text
P(y | S) = P(y)
```

then the observation is not a valid re-anchor for the relevant state.

Failure pattern:

```text
activity feels like checking -> observation unrelated to state
```

Correction:

```text
choose a state-informative observation
```

## Step 5: Can the observation change the next action?

A useful observation can support a conditional action switch:

```text
a(y) != a_0
```

for at least one possible observation result.

If:

```text
a(y) = a_0
```

for all possible results, the observation has weak decision value.

Failure pattern:

```text
observe -> same action no matter what
```

Correction:

```text
observe only if the result can change the next action
```

## Step 6: Does value exceed cost?

For general actions:

```text
V(a) = I(a) + B(a) - C(a)
```

Action is favorable only if:

```text
V(a) > 0
```

For observation-specific actions:

```text
OV > 0
```

If not, the action or observation may be valid but not favorable.

Failure pattern:

```text
state-informative but too costly
```

Correction:

```text
choose a cheaper observation or act without further observation
```

## Step 7: Is this the first observation or a repeated observation?

The first valid observation after observation rate zero can be valuable.

Repeated observation requires marginal value:

```text
MOV_i > 0
```

If:

```text
MOV_i <= 0
```

then repeated checking is unfavorable.

Failure pattern:

```text
first check was useful -> keep checking the same thing
```

Correction:

```text
stop checking or choose a different state-informative observation
```

## Step 8: If expanding, is the expansion factor justified?

Adaptive expansion uses:

```text
s_{i+1} = r_i s_i
```

Expansion is favorable only if:

```text
B_expand(r_i) + I_expand(r_i) > C_obs(r_i) + P_boundary(i) * C_boundary + C_correct(r_i)
```

If not, expansion is excessive.

Failure pattern:

```text
small success -> large expansion without boundary-risk check
```

Correction:

```text
choose a smaller expansion factor or observe sooner
```

## Step 9: Is boundary risk being underestimated?

Previous safe scope is evidence, not proof of safety in larger scope.

Failure pattern:

```text
no boundary crossing at s_i -> assume no boundary crossing at s_{i+1}
```

Correction:

```text
re-estimate P_boundary(i) and C_boundary before expanding
```

## Step 10: Is a local observation being used as a global conclusion?

Local observations update local beliefs.

They do not automatically justify global conclusions.

Failure pattern:

```text
one local result -> total self/world/project judgment
```

Correction:

```text
keep the conclusion at the same scope as the observation
```

## Compact decision tree

```text
1. Can you name the hidden state?
   no -> define state first
   yes -> continue

2. Is the target fixed or locally fixed?
   no -> separate occurrence uncertainty
   yes -> continue

3. Can action affect observation, belief, decision, or state?
   no -> outside actionable core
   yes -> continue

4. Is the observation state-informative?
   no -> not a valid re-anchor
   yes -> continue

5. Can observation change the next action?
   no -> weak decision value
   yes -> continue

6. Does value exceed cost?
   no -> valid but unfavorable
   yes -> action or observation is favorable

7. Is this repeated observation?
   yes and MOV_i <= 0 -> checking loop
   no or MOV_i > 0 -> continue

8. Are you expanding scope?
   no -> act within current scope
   yes -> check expansion inequality

9. Is boundary-risk-constrained expansion favorable?
   no -> reduce expansion or observe sooner
   yes -> expand

10. Is the conclusion local or global?
   global from local evidence -> overreach
   local from local evidence -> acceptable
```

## Diagnostic output labels

Use these labels when evaluating a case.

| Label | Meaning |
|---|---|
| `valid re-anchor` | state-informative observation exists |
| `favorable observation` | `OV > 0` |
| `favorable action` | `V(a) > 0` |
| `checking loop` | `MOV_i <= 0` |
| `excessive expansion` | expansion inequality fails |
| `external uncertainty` | action cannot affect observation, belief, decision, or state |
| `local overreach` | local observation used as global conclusion |
| `out of core scope` | target occurrence uncertainty dominates |

## Short version

```text
Name the state.
Check whether the observation is state-informative.
Check whether it changes action.
Check whether value exceeds cost.
Repeat only if marginal value remains positive.
Expand only if boundary-risk-constrained value is positive.
Do not turn local evidence into global judgment.
```
