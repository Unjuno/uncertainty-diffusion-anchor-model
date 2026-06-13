# Terminology

## Anchor

An observation, record, count, action, or feedback signal that constrains the agent's belief about the current state.

Japanese: アンカー

## Anchor loss

A condition where the agent loses a reference point for the current state.

Japanese: アンカー喪失

## Re-anchoring

An action that restores or creates a reference point by returning information about the current state.

Japanese: 再アンカー

## Uncertainty diffusion

The increase of uncertainty over time when no anchoring observations are available.

In UDAM, this usually means belief uncertainty, not necessarily physical deterioration of the external state.

Japanese: 不確実性拡散

## Belief uncertainty

Uncertainty in the agent's belief about the state.

Minimal variance form:

```text
P_t = Var(S_t | D_t)
```

Japanese: 信念不確実性 / 認識上の不確実性

## State dynamics

Change in the state itself.

```text
S_t changes
```

Japanese: 状態変化

## Belief dynamics

Change in the agent's uncertainty about the state.

```text
P_t changes
```

Japanese: 信念変化 / 認識状態の変化

## Fixed target

A target condition treated as fixed inside the local timer seed model.

```text
fixed target, uncertain position
```

Japanese: 固定ターゲット / 固定対象条件

## Uncertain target

A target condition whose occurrence is itself uncertain.

This is outside the core timer seed model unless a separate occurrence layer is added.

```text
uncertain target, uncertain position
```

Japanese: 不確実ターゲット / 発生不確実な対象条件

## Agent position

The agent's current position relative to a fixed target condition.

In the timer model this is elapsed position:

```text
τ = K + U + R
```

Japanese: 現在位置 / 対象に対する位置

## Controllability boundary

The boundary between uncertainty that action can affect and external uncertainty that action cannot control.

UDAM core includes uncertainty that action can affect through observation, belief update, decision improvement, or state intervention.

Japanese: 制御可能性境界

## Actionable uncertainty

Uncertainty that can be affected by action through observation, belief update, decision improvement, or state intervention.

Japanese: 行動可能な不確実性 / 行動で扱える不確実性

## External uncertainty

Uncertainty outside the agent's control.

In UDAM, uncontrollable event-occurrence uncertainty is treated as external, exceptional, or deferred to an extension.

Japanese: 外生的不確実性 / 非制御可能な不確実性

## Upside uncertainty

Uncertainty that may contain favorable latent states.

It does not mean uncertainty is good by itself.

It means:

```text
uncertainty may hide upside
observation can reveal it
```

Japanese: 上振れ不確実性 / 良い方向を含む不確実性

## Happy miscalculation

A case where the agent expects or fears a poor state, but observation reveals that the true state is better than expected.

This is an observability effect, not blind optimism.

Japanese: 嬉しい誤算

## Observability value

The value produced when an action makes the current state more observable and enables better conditional action.

Representative form:

```text
E[max_a V(a | y)] >= max_a E[V(a)]
```

assuming no observation cost and ideal use of information.

Japanese: 観測可能性価値

## Informative action

An action that returns information about the current state.

Japanese: 情報行動

## Intervention value

The value produced when an action improves the state itself.

Japanese: 介入価値

## Empty activity

Activity that consumes cost without informational or intervention value.

Japanese: 空回り行動 / 空虚な多動

## Missed re-anchor miscalculation

A miscalculation where UDAM applies but the agent fails to use it.

Common pattern:

```text
partial uncertainty → total invalidation
```

UDAM correction:

```text
partial uncertainty → re-anchor if the next action has positive value
```

Japanese: 再アンカー見落とし / 部分的不確実性の全体無効化

## High-stakes fixed-target example

A neutral, non-operational example type used to show the timer structure clearly.

It preserves:

```text
fixed target
uncertain position
lost anchor
re-anchoring action
```

without preserving harmful scenario details.

Japanese: 高緊張固定ターゲット例

## Positive hyperactivity

A potentially misleading phrase. In UDAM, the intended meaning is not impulsive activity, but high-frequency low-cost informative action.

Preferred term:

```text
high-frequency low-cost re-anchoring
```

Japanese:

```text
高頻度・低コスト再アンカー行動
```
