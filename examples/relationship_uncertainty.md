# Example: Relationship Uncertainty

## Situation

A relationship becomes uncertain after silence, conflict, or delayed response.

The agent does not know whether the other person is angry, indifferent, busy, or waiting.

## Lost anchor

The lost anchor is the social state.

## State variable

The latent state is the actual relationship or social condition:

```text
S_t = current social state
```

This may include the other person's attitude, availability, expectations, and willingness to respond.

## Belief uncertainty

The agent is uncertain about the social state.

```text
P_{relation,t} = Var(S_t | D_t)
```

## Possible state dynamics

The social state may change over time:

- the other person may cool down;
- misunderstanding may increase;
- external context may change;
- the relationship may stabilize without action.

UDAM does not assume that the relationship necessarily worsens during silence.

## Belief dynamics

Even if the social state is stable, the agent's uncertainty may increase without contact.

```text
P_{relation,t+Δt} = P_{relation,t} + Q_relation Δt
```

## Re-anchoring action

Send one short, clear, low-pressure message.

## Informational value

The response, or lack of response, updates the belief state.

```text
I(a) > 0
```

## Intervention value

The message may also repair or stabilize the relationship.

```text
B(a) >= 0
```

## Failure case

Repeated anxious messages may increase cost and damage the state.

A useful re-anchor should be small, clear, and non-compulsive.
