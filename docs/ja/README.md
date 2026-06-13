# 日本語版ドキュメント

このディレクトリは、Uncertainty-Diffusion Anchor Model（UDAM / 不確実性拡散アンカーモデル）の日本語説明です。

英語版と別リポジトリに分けず、同じリポジトリ内で管理します。

## 目的

日本語版の目的は、英語版の完全な直訳ではありません。

目的は次の3つです。

```text
1. 発想の直感を残す
2. 中学生でも読める説明にする
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

1. [`00_chugaku_explanation.md`](00_chugaku_explanation.md)  
   中学生向けの説明。
2. [`01_timer_model.md`](01_timer_model.md)  
   タイマー問題からの出発点。
3. [`02_practical_protocol.md`](02_practical_protocol.md)  
   実際の使い方。
4. [`03_failure_cases.md`](03_failure_cases.md)  
   使えない場合・誤用しやすい場合。
5. [`04_positioning.md`](04_positioning.md)  
   UDAM が何で、何ではないか。

## 英語版との対応

| 日本語版 | 英語版 |
|---|---|
| `00_chugaku_explanation.md` | `docs/00_overview.md` |
| `01_timer_model.md` | `docs/01_timer_model.md` |
| `02_practical_protocol.md` | `docs/14_practical_reanchor_protocol.md` |
| `03_failure_cases.md` | `docs/06_failure_cases.md` |
| `04_positioning.md` | `docs/19_positioning_and_novelty.md` |

## 注意

UDAM は、完全に新しい数学理論ではありません。

より正確には、既存の考え方をタイマー問題から整理した実践的なモデルです。

```text
新しい基礎数学ではなく、タイマー由来の実践的統合モデル。
```
