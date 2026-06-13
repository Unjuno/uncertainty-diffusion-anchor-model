# 04 Action Value

## Purpose

UDAM does not say that all actions are useful.

It says that an action can be useful when it returns information, improves the state, or both, at a cost low enough to justify it.

## Variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `a` | action | dimensionless | a confirmation, measurement, work unit, message, or test | chosen from available actions | decision variable |
| `I(a)` | informational value | utility unit | value from reducing uncertainty | `I(a) >= 0` | scalar |
| `B(a)` | intervention value | utility unit | value from improving the state | real number | scalar |
| `C(a)` | action cost | utility unit | time, fatigue, money, danger, opportunity cost | `C(a) >= 0` | scalar |
| `V(a)` | total action value | utility unit | `V(a) = I(a) + B(a) - C(a)` | real number | scalar |

## Basic equation

```text
V(a) = I(a) + B(a) - C(a)
```

The action is favorable when:

```text
V(a) > 0
```

## Interpretation

- `I(a)` captures what the action teaches the agent.
- `B(a)` captures how the action changes the world or the agent.
- `C(a)` captures what the action consumes or risks.

## Unit check

All terms must be converted into the same utility scale.

```text
[V(a)] = [I(a)] = [B(a)] = [C(a)] = utility unit
```

The equation is valid only after this conversion.

## Important correction

UDAM does not justify arbitrary activity.

It justifies **small informative actions** when their value exceeds their cost.

## Good actions

| Action type | Why it can be valuable |
|---|---|
| one problem | measures current skill and slightly trains it |
| one short message | tests relationship state and may repair it |
| one symptom log | records health state for future comparison |
| ten-minute project inspection | reconstructs project state |
| restarting a timer count | anchors elapsed time from now onward |

## Bad actions

| Action type | Why it can be harmful |
|---|---|
| compulsive checking | high cost, low new information |
| vague browsing | weak signal, high time cost |
| planning with no state contact | may not reduce uncertainty |
| high-risk action under uncertainty | cost may dominate |
| misleading measurement | may reduce apparent uncertainty while increasing error |

## Practical rule

Prefer actions with:

```text
high I(a), nonnegative B(a), low C(a)
```

Avoid actions with:

```text
I(a) ≈ 0 and B(a) ≈ 0 and C(a) > 0
```
