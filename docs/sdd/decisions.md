# SDD 設計判断ログ v0.1

このファイルは、Noisebrush / UDAM Interactive Prototype v0.1 の主要な設計判断を記録する。

## D-001: SDD 領域を `docs/sdd/` に分離する

### 判断

実装仕様は `docs/sdd/` 以下に置く。

### 理由

既存の UDAM リポジトリには理論文書が多く存在する。実装仕様を既存理論文書と混在させると、理論の source of truth と実装の source of truth が曖昧になる。

### 結果

実装エージェントは `docs/sdd/` を v0.1 実装仕様の source of truth として扱う。

## D-002: v0.1 は完成画像生成ツールではない

### 判断

v0.1 は、一発で完成画像を生成するツールとして設計しない。

### 理由

本プロトタイプの価値は、生成途中状態に人間が介入し、良い中間状態を探索できる点にある。

### 結果

UI は Prompt-to-final-image ではなく、Explore → Snapshot → Finish の流れを中心にする。

## D-003: Human Layer は独立状態として保持する

### 判断

Human Layer は Generated Image と分離して保持する。

### 理由

Human Layer は人間の介入信号であり、生成処理によって消えたり変更されたりすると、ユーザーの制御感が失われる。

### 結果

v0.1 では Human Layer は独立キャンバスとして実装する。

## D-004: Noise Brush は消しゴムではない

### 判断

Noise Brush は画像を消す道具ではなく、選択領域を再生成対象にする道具として定義する。

### 理由

プロダクトの核は「不確定状態に戻して再解釈させる」ことである。消しゴムとして扱うと、通常の画像編集 UI と区別がつかなくなる。

### 結果

Noise Brush は Generated Image 上で noiseMask を作成し、次回 generation request に渡す。

## D-005: v0.1 は画像 Snapshot による擬似再開でよい

### 判断

v0.1 では latent state と timestep の保存を必須にしない。

### 理由

真の拡散途中再開には latent state、timestep、scheduler state などが必要になり、MVP の実装負荷が大きい。

まずは画像 Snapshot を base image とする擬似再開で、体験価値を検証する。

### 結果

Snapshot 型には画像と主要設定を保存する。latent snapshot は後続バージョンの検討事項とする。

## D-006: Mock backend を先に実装する

### 判断

実モデル接続より先に Mock backend を実装する。

### 理由

本プロトタイプでは、画像品質より UI と生成ループの体験検証が重要である。実モデル接続を先に行うと、環境依存の問題で UI 実装が止まりやすい。

### 結果

まず Mock backend で Prompt、Step、Auto、Noise Brush、Snapshot、Finish の状態遷移を確認する。

## D-007: TinySD は体験検証用モデルとして扱う

### 判断

TinySD または同等の軽量拡散モデルは、完成品質評価用ではなく、リアルタイム体験検証用として扱う。

### 理由

TinySD は軽量で試しやすい一方、最終品質の評価には向かない。

### 結果

v0.1 では TinySD 接続は後段タスクとし、利用できない環境では Mock backend にフォールバックできることを優先する。

## D-008: Tree UI は v0.1 では実装しない

### 判断

Snapshot は `parentId` を持つが、Tree UI は v0.1 の必須機能にしない。

### 理由

探索分岐の概念は重要だが、最初から Tree UI を作ると UI 実装が重くなる。

### 結果

v0.1 では横並びの Snapshot Timeline を実装する。分岐構造はデータだけ保持する。

## D-009: Scheduler は UI に出さない

### 判断

Scheduler / Sampler は v0.1 では UI に出さず固定する。

### 理由

生成設定を増やすと、MVP の焦点がぶれる。ユーザーが最初に触るべき値は Steps、CFG、Noise Strength、Seed、Update Interval、Brush Size に限定する。

### 結果

Scheduler は backend 内部設定とする。

## D-010: Auto Mode は必ず停止可能にする

### 判断

Auto Mode には Pause 操作を必須とする。

### 理由

止められない生成ループはデバッグ不能であり、ユーザー体験としても制御不能になる。

### 結果

Step / Auto / Pause の 3 操作を v0.1 の必須 UI にする。

## D-011: stale result protection を必須にする

### 判断

Auto Mode では古い response による上書きを防ぐ。

### 理由

生成リクエストは非同期で返るため、古い結果が新しい状態を上書きすると、ユーザー操作と画面表示が矛盾する。

### 結果

request id または single-flight 方式で stale result protection を実装する。
