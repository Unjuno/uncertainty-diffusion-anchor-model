# リポジトリ状態とシミュレーション注記

この文書は、日本語版の追加同期メモです。

英語版 Markdown が source of truth です。

この文書は新しい理論を追加しません。

## 現在のリポジトリ状態

現在の位置づけは次です。

```text
GitHub 上の理論整理リポジトリとして、ほぼ完成。
```

ただし、次のものではありません。

```text
外部データによる一般妥当性の確立
既存の意思決定理論の置き換え
完成した論文パッケージ
```

英語版での主要な状態管理は、次を参照します。

```text
AGENTS.md
docs/47_remaining_work_register.md
docs/48_stabilization_pass_summary.md
docs/53_repository_completion_check.md
docs/54_final_repository_audit.md
docs/55_repository_simulation_plots_and_sensitivity.md
```

## シミュレーションの位置づけ

`simulations/` には、UDAM の最小的な toy sanity check があります。

ここでのシミュレーションは、次の意味です。

```text
toy demonstration
sanity check
```

次の意味ではありません。

```text
外部データによる検証
一般的な証明
一般的な妥当性の確立
既存理論より優れていることの根拠
```

## 現在の toy check

現在の simulation layer は、次のパターンを確認するためのものです。

```text
1. Timer re-anchor
2. Observation value
3. Expansion boundary risk
4. Repeated-checking MOV_i
5. Boundary-risk sensitivity
6. Observation-cost threshold sensitivity
```

これらは、選んだ toy parameter の下で、期待される定性的パターンが出るかを見るものです。

## 現在の repository-facing plot

現在の repository-facing plot は次です。

```text
simulations/plots/repeated_checking_mov.svg
simulations/plots/boundary_risk_sensitivity.svg
simulations/plots/observation_cost_threshold.svg
```

これらは説明補助の plot であり、外部データによる検証や一般的な証明ではありません。

## 読み方

詳細は英語版を参照します。

```text
simulations/README.md
simulations/plots/README.md
docs/39_simulation_sanity_checks.md
docs/49_extended_simulation_sanity_checks.md
docs/55_repository_simulation_plots_and_sensitivity.md
```

現在の repository-facing plot や sensitivity check も、同じ制限の下で読みます。

```text
シミュレーションは説明補助であり、実証ではない。
```

## 日本語版で避ける主張

避ける主張：

```text
simulation による一般的な確認
外部データによる一般妥当性の確立
一般的な証明
```

使える表現：

```text
toy simulation では、選んだ仮定の下で期待される挙動を再現した。
```
