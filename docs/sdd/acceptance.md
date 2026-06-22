# SDD 受け入れ条件 v0.1

このファイルは、Noisebrush / UDAM Interactive Prototype v0.1 の完了判定を定義する。

受け入れ条件は、主観的な「よさ」ではなく、観察可能な挙動で判定する。

## 1. 全体完了条件

v0.1 は、以下をすべて満たしたら完了とする。

1. Prompt を入力できる。
2. Model を選択できる。
3. Step 実行で画像を生成できる。
4. Human Layer に描画できる。
5. Human Layer が Generated Image と分離されている。
6. Generated Image に Noise Brush を塗れる。
7. Noise Brush 領域を次回生成 request に反映できる。
8. Step 実行ができる。
9. Auto 実行ができる。
10. Pause できる。
11. Snapshot を保存できる。
12. Snapshot を復元できる。
13. Snapshot から Finish できる。
14. 生成エラーが UI に表示される。
15. 生成失敗時にも UI が操作不能にならない。
16. Generated Image の更新によって Human Layer が変更されない。

## 2. 画面条件

### AC-UI-001: 基本レイアウト

アプリを開いたとき、以下が表示されること。

- Prompt 入力
- Model 選択
- Step / Auto / Pause 操作
- Human Layer キャンバス
- Generated Image キャンバス
- Snapshot Timeline
- 生成設定
- Noise Brush 設定

### AC-UI-002: 設定変更

以下の値を UI から変更できること。

- Steps
- CFG
- Noise Strength
- Seed
- Update Interval
- Brush Size

## 3. Human Layer 条件

### AC-HL-001: 描画

Human Layer キャンバス上でドラッグしたとき、線が体感即時に表示されること。

### AC-HL-002: 独立保持

Human Layer に描画した状態で Generated Image を更新しても、Human Layer の描画が消えないこと。

### AC-HL-003: Clear

Clear Human Layer を実行したとき、Human Layer のみが消え、Generated Image は残ること。

## 4. 生成条件

### AC-GEN-001: Step 生成

Prompt が入力されている状態で Step を押すと、1 回だけ generation request が送られ、Generated Image が更新されること。

### AC-GEN-002: 生成中表示

generation request が実行中のとき、UI に generationStatus = generating 相当の表示が出ること。

### AC-GEN-003: エラー表示

backend がエラーを返したとき、エラーメッセージが UI に表示され、アプリ全体は操作可能なままであること。

### AC-GEN-004: 現在画像の保持

Generated Image が存在するとき、Step または Auto 更新は現在画像を base image として扱うこと。

毎回ゼロから生成する挙動は v0.1 の目的に反する。

## 5. Noise Brush 条件

### AC-NB-001: ブラシ描画

Generated Image 上で Noise Brush を使うと、ブラシ領域が noiseMask として保持されること。

### AC-NB-002: Brush Size

Brush Size を変更すると、Noise Brush の描画サイズが変わること。

### AC-NB-003: request 反映

noiseMask が存在するとき、Step または Auto 更新の generation request に noiseMask が含まれること。

### AC-NB-004: Human Layer 維持

Noise Brush を使用しても Human Layer は変更されないこと。

## 6. Auto Loop 条件

### AC-LOOP-001: Auto 開始

Auto を押すと、updateIntervalMs ごとに generation request が実行されること。

### AC-LOOP-002: Pause

Auto 実行中に Pause を押すと、新規 generation request が停止すること。

### AC-LOOP-003: UI 継続操作

Auto 実行中も Human Layer 描画、Noise Brush 描画、Pause 操作が可能であること。

### AC-LOOP-004: stale result protection

古い generation response が遅れて返ってきても、新しい状態を古い画像で上書きしないこと。

実装方法は以下のどちらでもよい。

- request id による破棄
- single-flight による多重 request 抑制

## 7. Snapshot 条件

### AC-SNAP-001: 保存

Generated Image が表示されているとき、Save Snapshot を押すと Snapshot Timeline に新しい Snapshot が追加されること。

Snapshot は最低限以下を保存する。

- id
- createdAt
- prompt
- model
- seed
- steps
- cfg
- noiseStrength
- generatedImageDataUrl

### AC-SNAP-002: Human Layer 保存

Human Layer に描画がある状態で Save Snapshot を押すと、humanLayerDataUrl も Snapshot に保存されること。

### AC-SNAP-003: 復元

Restore Snapshot を実行すると、Generated Image と主要生成設定が Snapshot の状態へ戻ること。

### AC-SNAP-004: 元 Snapshot 保持

Snapshot を Restore または Finish しても、元 Snapshot は削除されないこと。

## 8. Finish 条件

### AC-FIN-001: Snapshot 選択

Snapshot Timeline の Snapshot をクリックすると、selectedSnapshotId がその Snapshot になること。

### AC-FIN-002: Finish 実行

selectedSnapshotId が存在するとき、Finish from Snapshot を実行すると、選択 Snapshot の generatedImage を base image として仕上げ生成を実行すること。

### AC-FIN-003: Finish 設定

Finish では Explore よりも仕上げ寄りの設定を使えること。

推奨値：

```text
finish_steps: 12-30
noise_strength: 0.05-0.20
cfg: 3.0-6.0
```

### AC-FIN-004: Finish 結果

Finish が成功したとき、Generated Image に Finish 結果が表示されること。

また、Finish 結果を新しい Snapshot として保存できること。

## 9. Mock backend 条件

### AC-MOCK-001: モデル未接続でも動作

実モデルが利用できない環境でも、Mock backend により Step / Auto / Snapshot / Finish の UI 検証ができること。

### AC-MOCK-002: request 内容確認

Mock backend は、受け取った request の主要値をログまたは UI デバッグ表示で確認できること。

主要値：

- prompt
- model
- seed
- steps
- cfg
- noiseStrength
- image 有無
- noiseMask 有無
- humanLayer 有無

## 10. デモシナリオ

v0.1 の最小デモは以下である。

```text
1. アプリを起動する。
2. Prompt を入力する。
3. Step を押して Generated Image を表示する。
4. Human Layer に線を描く。
5. Auto を押して生成ループを開始する。
6. Generated Image の一部を Noise Brush で塗る。
7. 塗った領域が次回更新に反映されることを確認する。
8. 良い中間状態で Save Snapshot を押す。
9. 別の状態まで生成を進める。
10. Snapshot を Restore する。
11. Restore した Snapshot から Finish from Snapshot を実行する。
12. Finish 結果を確認する。
```

このデモが通れば、v0.1 の体験価値は成立している。

## 11. 不合格条件

以下のいずれかがある場合、v0.1 は未完了である。

- Human Layer が生成更新で消える。
- Auto を停止できない。
- Snapshot を復元できない。
- Noise Brush が Human Layer を変更する。
- 生成エラーで UI 全体が固まる。
- 毎回ゼロから生成され、現在画像の継続状態がない。
- 仕様外の機能追加により MVP が複雑化している。
