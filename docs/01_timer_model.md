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

The lost interval is not recovered, but future uncertainty growth is constrained.

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

## Generalization

The timer model generalizes as follows:

```text
current state = known part + uncertain part + re-anchored observed part
```

This is the seed of the broader uncertainty-diffusion anchor model.
