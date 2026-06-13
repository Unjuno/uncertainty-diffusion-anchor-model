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

Japanese: 不確実性拡散

## Informative action

An action that returns information about the current state.

Japanese: 情報行動

## Intervention value

The value produced when an action improves the state itself.

Japanese: 介入価値

## Empty activity

Activity that consumes cost without informational or intervention value.

Japanese: 空回り行動 / 空虚な多動

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
