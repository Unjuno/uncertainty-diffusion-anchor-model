# 日本語版ドキュメント

このディレクトリは、Uncertainty-Diffusion Anchor Model（UDAM / 不確実性拡散アンカーモデル）の日本語説明です。

英語版と別リポジトリに分けず、同じリポジトリ内で管理します。

## Source-of-truth status

現時点では、英語版 Markdown が source of truth です。

日本語版は下流の説明レイヤーであり、英語版より強い主張を追加しません。

特に、次の主張は避けます。

```text
UDAM は証明済み
UDAM は実証済み
UDAM はシミュレーションで確認済み
UDAM は既存の意思決定理論を置き換える
UDAM は治療法である
```

英語版の編集・安定化方針は、主に次を優先します。

```text
AGENTS.md
docs/33_project_note_consolidation.md
docs/43_notation_consistency_audit.md
docs/47_remaining_work_register.md
docs/48_stabilization_pass_summary.md
docs/53_repository_completion_check.md
docs/54_final_repository_audit.md
```

## 目的

日本語版の目的は、英語版の完全な直訳ではありません。

目的は次の3つです。

```text
1. 発想の直感を残す
2. 平易な日本語で説明する
3. 英語版の理論構造と対応させる
```

## いちばん短い説明

```text
途中でわからなくなった部分があることと、
これから確かめることが意味ないことは別。
```

UDAM の中心はこれです。

```text
過去のアンカー喪失は、未来の有効観測を無効化しない。
```

英語版では次のように表現しています。

```text
Anchor loss does not imply future anchor invalidation.
```

## 最小モデル

```text
τ = K + U + R
```

意味：

```text
K = わかっている過去の部分
U = 見失った不明な部分
R = そこから再開して新しくわかった部分
τ = 現在位置
```

重要なのは、`U` が不明でも `R` は無効にならないことです。

## 読む順番

1. [`00_plain_explanation.md`](00_plain_explanation.md)  
   平易な説明。
2. [`01_timer_model.md`](01_timer_model.md)  
   タイマー問題からの出発点。
3. [`02_practical_protocol.md`](02_practical_protocol.md)  
   実際の使い方。
4. [`03_failure_cases.md`](03_failure_cases.md)  
   使えない場合・誤用しやすい場合。
5. [`05_failure_examples.md`](05_failure_examples.md)  
   具体的な失敗例。
6. [`04_positioning.md`](04_positioning.md)  
   UDAM が何で、何ではないか。
7. [`06_repository_status_and_simulations.md`](06_repository_status_and_simulations.md)  
   リポジトリ状態と toy simulation の位置づけ。

## 図

図は英語名のまま `assets/diagrams/` と `assets/figures/` に置いています。

まず見るなら、英語版の Stage 3 SVG 図です。

- [`../../assets/figures/one_page_udam_flow.svg`](../../assets/figures/one_page_udam_flow.svg)  
  全体の流れ。
- [`../../assets/figures/anchor_reanchor_timeline.svg`](../../assets/figures/anchor_reanchor_timeline.svg)  
  アンカー喪失から再アンカーまで。
- [`../../assets/figures/observation_value_decision.svg`](../../assets/figures/observation_value_decision.svg)  
  観測価値と条件付き行動。
- [`../../assets/figures/expansion_boundary_risk.svg`](../../assets/figures/expansion_boundary_risk.svg)  
  拡張と境界リスク。

古い Mermaid 図のレンダリング判断は、英語版の `docs/50_visual_rendering_audit.md` を優先します。

## 英語版との対応

| 日本語版 | 英語版 |
|---|---|
| `00_plain_explanation.md` | `docs/00_overview.md` |
| `01_timer_model.md` | `docs/01_timer_model.md` |
| `02_practical_protocol.md` | `docs/14_practical_reanchor_protocol.md` |
| `03_failure_cases.md` | `docs/06_failure_cases.md` |
| `05_failure_examples.md` | `examples/failure_*.md` |
| `04_positioning.md` | `docs/19_positioning_and_novelty.md` |
| `06_repository_status_and_simulations.md` | `docs/53_repository_completion_check.md`, `docs/54_final_repository_audit.md`, `simulations/README.md` |

## 注意

UDAM は、完全に新しい数学理論ではありません。

より正確には、既存の考え方をタイマー問題から整理した実践的なモデルです。

```text
新しい基礎数学ではなく、タイマー由来の実践的統合モデル。
```

シミュレーションは説明補助の toy demonstration / sanity check であり、実証ではありません。
