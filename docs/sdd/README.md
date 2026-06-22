# SDD 実装仕様パッケージ

このディレクトリは、Uncertainty-Diffusion Anchor Model（UDAM）の概念を、実装エージェントへ渡せるプロトタイプ仕様として固定するための SDD（Specification Driven Development）領域である。

ここで扱う対象は、理論文書そのものではなく、以下のインタラクティブ実装である。

```text
Prompt、Human Layer、Noise Brush、Snapshot を使って、拡散モデルの生成途中状態を人間が探索・介入・仕上げできるプロトタイプ。
```

## 目的

この SDD パッケージの目的は、リポジトリをエージェントへ渡したときに、実装者が以下を曖昧なく判断できる状態にすることである。

- 何を作るか
- 何を作らないか
- どの順番で実装するか
- どの条件を満たせば完了か
- 仕様変更時に何を問い直すか

## ファイル構成

| ファイル | 役割 |
|---|---|
| `spec.md` | v0.1 のプロダクト仕様。何を作るかを定義する。 |
| `tasks.md` | 実装タスク分解。エージェントが実装する順序を定義する。 |
| `acceptance.md` | 受け入れ条件。完了判定を定義する。 |
| `glossary.md` | 用語定義。曖昧な語を固定する。 |
| `decisions.md` | 設計判断ログ。なぜその仕様にしたかを残す。 |
| `grill.md` | 仕様更新時の問い詰め手順。仕様を安易に広げないためのチェックリスト。 |

## 実装エージェントへの読み順

実装エージェントは、次の順番で読むこと。

1. `AGENTS.md`
2. `docs/sdd/README.md`
3. `docs/sdd/spec.md`
4. `docs/sdd/tasks.md`
5. `docs/sdd/acceptance.md`
6. `docs/sdd/glossary.md`
7. `docs/sdd/decisions.md`
8. `docs/sdd/grill.md`

## 重要ルール

v0.1 では、仕様書に書かれていない機能を実装してはならない。

新しい機能が必要な場合は、先に `grill.md` の問いに通し、`spec.md`、`tasks.md`、`acceptance.md`、`decisions.md` を更新する。

## v0.1 の実装優先順位

```text
1. UI が触れる
2. 生成ループが回る
3. Noise Brush が効く
4. Snapshot が保存・復元できる
5. Snapshot から Finish できる
6. モデル品質を改善する
```

画像品質より、生成途中状態を人間が操作できる体験を優先する。
