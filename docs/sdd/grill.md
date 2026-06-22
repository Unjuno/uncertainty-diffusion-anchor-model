# SDD 仕様レビュー手順 v0.1

このファイルは、Noisebrush / UDAM Interactive Prototype v0.1 の仕様を広げすぎないためのレビュー手順である。

## 1. 基本方針

仕様は、実装エージェントが迷わず作業できる契約として扱う。

新しい機能や UI を追加する場合は、先にこのチェックを行う。

## 2. 必須チェック

仕様変更前に、以下を確認する。

1. v0.1 の目的に直結するか。
2. 画像品質改善だけに寄っていないか。
3. 入力、出力、状態変更、UI 表示、失敗時の挙動が明確か。
4. `acceptance.md` に観察可能な完了条件を書けるか。
5. Mock backend でも検証できるか。
6. Human Layer が生成更新で変更されないか。
7. Noise Brush を通常の消去操作として扱っていないか。
8. Snapshot が Restore と Finish の起点になっているか。
9. v0.1 範囲外の機能を混ぜていないか。
10. `spec.md`、`tasks.md`、`acceptance.md`、`decisions.md` の更新が必要か。

## 3. v0.1 の目的

v0.1 の目的は以下である。

```text
Prompt、Human Layer、Noise Brush、Snapshot を使って、拡散モデルの生成途中状態を探索・介入・仕上げできることを示す。
```

この目的に直結しない変更は、後続バージョンへ回す。

## 4. v0.1 で扱わないもの

以下は v0.1 の範囲外である。

- 図構造認識
- Mermaid / UML / SVG 変換
- ControlNet
- 複雑なレイヤー管理
- Semantic editing
- Latent snapshot の完全保存
- 認証
- クラウドデプロイ
- 共同編集
- 本番品質の最適化
- 高品質モデルへの最適化

## 5. 仕様追加テンプレート

新しい仕様を追加する場合は、次の形で記録する。

```md
## Proposal: <機能名>

### 目的

### v0.1 への必要性

### 入力

### 出力

### 状態変更

### UI

### 失敗時の挙動

### 受け入れ条件

### 判断

採用 / 後回し / 不採用
```

## 6. 更新対象

仕様を変えた場合、必要に応じて以下を同時に更新する。

- `docs/sdd/spec.md`
- `docs/sdd/tasks.md`
- `docs/sdd/acceptance.md`
- `docs/sdd/glossary.md`
- `docs/sdd/decisions.md`

`spec.md` だけを更新して終わってはならない。

## 7. 実装開始前の最終確認

実装エージェントへ渡す前に、以下を確認する。

```text
[ ] UI は仕様書の範囲に収まっている
[ ] Mock backend で先に動かせる
[ ] 生成ループは現在画像を継続状態として扱う
[ ] Snapshot は Restore と Finish の起点になる
[ ] 生成失敗時も UI が操作可能である
```
