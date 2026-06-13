# Example: Timer Bomb

## Situation

A fixed event will occur after 60 seconds. The agent counts time but loses track during an interruption, then restarts counting.

This is the seed example of UDAM.

## Lost anchor

The agent loses the time-counting anchor during an unknown interval.

## Variables

```text
T = 60 s
τ = K + U + R
```

- `K`: known counted time before losing track
- `U`: unknown time during interruption
- `R`: counted time after restarting

## Re-anchoring action

Restart counting from the current point.

## Informational value

Restarting does not recover `U`, but it provides `R`.

The current time is no longer completely unknown. It is constrained by:

```text
τ = K + U + R
```

## Additional observation

If the event has not occurred yet, then:

```text
τ < T
```

This also constrains `U`.

Example:

```text
K = 20 s
R = 10 s
T = 60 s
τ = 30 s + U
```

If the event has not occurred:

```text
30 s + U < 60 s
U < 30 s
```

## Lesson

The unknown interval remains uncertain, but restarting the count is not meaningless.

It is a re-anchor.
