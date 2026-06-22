# SDD 実装タスク v0.1

このファイルは、実装エージェントが Noisebrush / UDAM Interactive Prototype v0.1 を実装するための作業順序を定義する。

実装は必ずこの順序で進める。

## 共通ルール

- `docs/sdd/spec.md` に書かれていない機能を実装しない。
- 画像品質より、UI と生成ループの体験成立を優先する。
- まず Mock backend で動く状態を作り、その後に実モデル接続を行う。
- 各タスクは `docs/sdd/acceptance.md` の該当条件を満たすまで完了扱いにしない。
- 実装中に仕様の曖昧さを見つけた場合、実装で勝手に解決せず `docs/sdd/grill.md` に従って仕様更新を提案する。

## Task 0: Project scaffold

### 目的

実装の土台を作る。

### 実装内容

- Web アプリ用ディレクトリを作成する。
- 依存関係管理を設定する。
- 開発起動コマンドを用意する。
- Lint / format / type check の最低限の導線を用意する。

### 完了条件

- ローカルでアプリを起動できる。
- 空のページまたは仮ページが表示される。
- README または開発メモに起動手順がある。

## Task 1: Static UI

### 目的

AI 未接続でもプロダクトの骨格が見える UI を作る。

### 実装内容

- Top Bar
  - App name
  - Model selector
  - Prompt input
  - Step / Auto / Pause controls
- Main Area
  - 左: Human Layer canvas placeholder
  - 右: Generated Image canvas placeholder
- Settings panel
  - Steps
  - CFG
  - Noise Strength
  - Seed
  - Update Interval
  - Brush Size
- Bottom Area
  - Snapshot Timeline placeholder

### 完了条件

- 仕様書の画面構成と対応した UI が表示される。
- 入力欄とボタンが操作可能である。
- まだ生成が動かなくてもよい。

## Task 2: App state model

### 目的

生成状態・UI状態・Snapshot状態を一元的に管理する。

### 実装内容

`docs/sdd/spec.md` の `AppState` に対応する状態を実装する。

最低限保持する状態：

- prompt
- selectedModel
- mode
- generationStatus
- steps
- cfg
- noiseStrength
- brushSize
- updateIntervalMs
- seed
- seedLocked
- humanLayer
- generatedImage
- noiseMask
- snapshots
- selectedSnapshotId

### 完了条件

- UI 操作が state に反映される。
- state の初期値が仕様と一致している。
- 主要状態をデバッグ表示または devtool で確認できる。

## Task 3: Human Layer canvas

### 目的

人間が介入信号を描ける独立レイヤーを実装する。

### 実装内容

- 左キャンバスで描画できる。
- 線の描画を即時表示する。
- Clear 操作を実装する。
- Human Layer を Generated Image と分離して保持する。
- Human Layer を data URL または同等形式で export できる。

### 完了条件

- ユーザーが Human Layer に描画できる。
- 生成画像の更新で Human Layer が消えない。
- Clear で Human Layer のみ消える。

## Task 4: Mock generation backend

### 目的

実モデル未接続でも生成ループと UI を検証できるようにする。

### 実装内容

- `GenerationRequest` / `GenerationResponse` 型を定義する。
- Mock backend を実装する。
- Prompt、seed、steps、cfg、noiseStrength を受け取る。
- 出力画像を data URL などで返す。
- latencyMs を返す。

Mock backend は本物の拡散品質を再現しなくてよい。目的は状態遷移と UI 確認である。

### 完了条件

- Prompt から仮画像を生成できる。
- Step ボタンで Generated Image が更新される。
- エラーを疑似的に発生させ、UI に表示できる。

## Task 5: Basic generation flow

### 目的

Prompt から Generated Image を生成し、現在画像として保持する。

### 実装内容

- Generate / Step 操作で generation request を作る。
- backend response の image を Generated Image に表示する。
- generationStatus を idle / generating / error で更新する。
- 生成失敗時に UI が操作不能にならないようにする。

### 完了条件

- Prompt 入力後、Step 実行で Generated Image が表示される。
- 生成中状態が UI に表示される。
- エラー時にエラーメッセージが表示される。

## Task 6: Noise Brush mask

### 目的

Generated Image 上の一部を再生成対象として指定できるようにする。

### 実装内容

- 右キャンバス上でブラシ描画できる。
- ブラシ領域を noiseMask として保持する。
- Brush Size を UI 設定と連動させる。
- Noise Brush は Human Layer に作用しない。
- noiseMask を generation request に渡す。

### 完了条件

- Generated Image 上に Noise Brush を塗れる。
- 塗った領域が noiseMask として保持される。
- Step 実行時に noiseMask が request に含まれる。
- Human Layer は影響を受けない。

## Task 7: Step / Auto / Pause loop

### 目的

生成途中状態が止まらず調整される体験を作る。

### 実装内容

- Step Mode: ボタン 1 回で 1 回生成更新。
- Auto Mode: updateIntervalMs ごとに生成更新。
- Pause Mode: Auto loop を停止。
- Auto 中に stale result が返った場合の保護を実装する。
- 生成中の多重リクエストを制御する。

### 完了条件

- Step で 1 回だけ更新される。
- Auto で継続的に Generated Image が更新される。
- Pause で更新が止まる。
- Auto 中も Human Layer 描画が可能である。
- 古い生成結果が新しい状態を破壊しない。

## Task 8: Snapshot save / restore

### 目的

良い中間状態を保存し、後から復元できるようにする。

### 実装内容

- Save Snapshot ボタンを実装する。
- Snapshot を `Snapshot` 型で保存する。
- Snapshot Timeline にサムネイル表示する。
- Snapshot をクリックして選択できる。
- Restore Snapshot を実装する。

### 完了条件

- 現在状態を Snapshot として保存できる。
- Snapshot に generatedImage、prompt、model、seed、steps、cfg、noiseStrength が保存される。
- Restore で Generated Image と主要設定が復元される。
- Human Layer も保存されている場合は復元される。

## Task 9: Finish from Snapshot

### 目的

選択した中間状態から仕上げ生成に進める。

### 実装内容

- Snapshot を選択する。
- Finish from Snapshot ボタンを実装する。
- Finish 用 steps / noiseStrength / cfg を適用する。
- 選択 Snapshot の generatedImage を base image として generation request を作る。
- Finish 結果を Generated Image に表示する。

### 完了条件

- Snapshot を選択して Finish を実行できる。
- Finish は選択 Snapshot を base とする。
- Finish 実行後も元 Snapshot は残る。
- Finish 結果を新しい Snapshot として保存できる。

## Task 10: TinySD backend hook

### 目的

Mock backend の後に、軽量拡散モデルを接続できる構造を用意する。

### 実装内容

- backend interface を維持したまま TinySD backend を追加する。
- 実行環境に依存する処理は isolated module に閉じ込める。
- TinySD が使えない環境では Mock backend にフォールバックできるようにする。

### 完了条件

- backend selector で mock / TinySD 相当を切り替えられる。
- TinySD が利用不可でもアプリが起動する。
- 生成失敗が UI に表示される。

## Task 11: Documentation and demo path

### 目的

第三者またはエージェントがプロトタイプを起動・確認できるようにする。

### 実装内容

- 起動手順を README または docs に記載する。
- v0.1 デモ手順を記載する。
- 既知制約を記載する。

### 完了条件

- 初見の実装者が起動方法を読める。
- デモシナリオに沿って Prompt → Auto → Noise Brush → Snapshot → Finish を確認できる。

## 実装しないタスク

v0.1 では以下をタスク化しない。

- ControlNet
- Mermaid / UML / SVG 変換
- 認証
- 共同編集
- クラウド永続化
- latent snapshot 完全再開
- 高品質モデル調整
