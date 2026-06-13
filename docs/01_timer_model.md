# 01 Timer Model

## Purpose

The timer model is the minimal example from which UDAM is generalized.

It is intentionally simple. Its role is to make the structure difficult to evade.

## Situation

A person is counting toward a fixed deadline, for example 60 seconds.

They count accurately for a known interval, then lose track during an interruption, and then restart counting.

The question is whether the restarted count is meaningless.

UDAM answers: no.

## Variables

| Symbol | Meaning | SI unit | Definition | Domain / assumptions | Type |
|---|---|---:|---|---|---|
| `T` | fixed deadline | s | total duration, e.g. 60 s | `T > 0` | scalar |
| `K` | known counted interval | s | interval counted before losing the anchor | `K >= 0` | scalar |
| `U` | unknown interval | s | interval while the anchor was lost | `U >= 0` | random variable |
| `R` | re-anchored counted interval | s | interval counted after restarting | `R >= 0` | scalar or low-noise observation |
| `τ` | current elapsed time | s | `τ = K + U + R` | `τ >= 0` | random variable |
| `D` | observation history | context-dependent | remembered counts and observations | arbitrary | data |

## Minimal equation

```text
τ = K + U + R
```

## Interpretation

- `K` is known.
- `U` is uncertain.
- `R` is newly observed after re-anchoring.

The uncertainty caused by `U` does not invalidate `R`.

## Main claim

If an agent loses track during `U`, restarting measurement at `R` is still informative.

The lost interval is not recovered, but future uncertainty is no longer merged into the same unknown interval.

## Dilution, not necessarily absolute reduction

In the timer model, re-anchoring does not necessarily reduce the absolute uncertainty of the lost interval `U`.

If `K` and `R` are treated as known and `U` remains unchanged, then:

```text
Var(τ | K, R) = Var(U)
```

So the absolute variance can remain the same.

However, as `R` grows, the known part of elapsed time grows while the unknown part remains localized in `U`.

This creates **relative uncertainty dilution**.

A simple relative uncertainty ratio is:

```text
ρ = sqrt(Var(U)) / E[τ]
```

Since:

```text
E[τ] = K + E[U] + R
```

increasing `R` reduces `ρ`, assuming `Var(U)` and `E[U]` are fixed.

Therefore, the timer-specific claim is more precise as:

> Re-anchoring does not erase the unknown interval. It dilutes the relative influence of the unknown interval by adding new known interval.

## All-or-nothing error

A common mistaken inference is:

> I lost track once, so all future counting is meaningless.

The timer model rejects this.

Correct inference:

> I lost information about `U`, but `R` is still valid information.

## Unit check

```text
[τ] = [K] + [U] + [R] = s
```

All terms have unit seconds. The decomposition is dimensionally valid.

For the relative uncertainty ratio:

```text
ρ = sqrt(Var(U)) / E[τ]
```

we have:

```text
[sqrt(Var(U))] = s
[E[τ]] = s
[ρ] = 1
```

So `ρ` is dimensionless.

## Example

Suppose:

```text
K = 20 s
R = 10 s
τ = 30 s + U
```

The only uncertain part is `U`.

If the deadline is `T = 60 s` and the event has not occurred yet, the agent also observes:

```text
τ < 60 s
```

Therefore:

```text
30 s + U < 60 s
U < 30 s
```

The fact that the event has not occurred is itself information.

## Deadline survival effect

If there is a known deadline `T` and the event has not occurred, then the agent also obtains a survival observation:

```text
K + U + R < T
```

which implies:

```text
U < T - K - R
```

As `R` increases, the upper bound on `U` decreases.

In this special deadline case, re-anchoring plus non-occurrence can reduce the possible range of `U`, not merely dilute its relative influence.

## Generalization

The timer model generalizes as follows:

```text
current state = known part + uncertain part + re-anchored observed part
```

This is the seed of the broader uncertainty-diffusion anchor model.
