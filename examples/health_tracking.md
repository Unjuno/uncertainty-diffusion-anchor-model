# Example: Health Tracking

## Situation

An agent feels physically or mentally off, but does not know whether the state is improving, worsening, or fluctuating.

## Lost anchor

The lost anchor is the body's current state and trajectory.

## State variable

The latent state is the current health-related condition:

```text
S_t = current health state
```

This may include sleep, symptoms, mood, recovery, medication effects, or fatigue.

## Belief uncertainty

The agent is uncertain about the current state and its trajectory.

```text
P_{health,t} = Var(S_t | D_t)
```

## Possible state dynamics

The health state may change over time:

- symptoms may improve;
- symptoms may worsen;
- fatigue may accumulate;
- recovery may occur;
- external factors may intervene.

## Belief dynamics

Even if the health state is stable, the agent's uncertainty can increase without records.

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
