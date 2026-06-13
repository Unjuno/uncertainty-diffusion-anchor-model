# Example: Health Tracking

## Situation

An agent feels physically or mentally off, but does not know whether the state is improving, worsening, or fluctuating.

## Lost anchor

The lost anchor is the body's current state and trajectory.

## Uncertainty diffusion

Without records, uncertainty may grow about:

- symptom duration;
- sleep quality;
- medication or caffeine effects;
- mood trajectory;
- recovery pattern.

```text
P_{health,t+Δt} = P_{health,t} + Q_health Δt
```

## Re-anchoring action

Record one health variable.

Examples:

- sleep duration;
- body temperature;
- mood score;
- symptom severity;
- caffeine amount;
- exercise duration.

## Informational value

A single record may constrain later interpretation.

```text
I(a) > 0
```

## Intervention value

Some tracking actions also encourage stabilizing behavior.

```text
B(a) >= 0
```

## Failure case

Obsessive tracking can increase anxiety and cost.

A useful health re-anchor should be limited, clinically responsible, and not a substitute for professional care when needed.
