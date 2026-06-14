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
実証済みモデル
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
実証
証明
一般的な妥当性の確認
既存理論より優れていることの確認
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

これらは、選んだ toy parameter の下で、期待される定性的挙動が出るかを見るものです。

## 読み方

詳細は英語版を参照します。

```text
simulations/README.md
docs/39_simulation_sanity_checks.md
docs/49_extended_simulation_sanity_checks.md
```

追加の plot や sensitivity check がある場合も、同じ制限を守ります。

```text
シミュレーションは説明補助であり、実証ではない。
```

## 日本語版で避ける表現

避ける表現：

```text
UDAM はシミュレーションで確認済み
UDAM は実証済み
UDAM は証明済み
```

使える表現：

```text
toy simulation では、選んだ仮定の下で期待される挙動を再現した。
```
