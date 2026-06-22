# SDD 用語集 v0.1

この用語集は、Noisebrush / UDAM Interactive Prototype v0.1 の実装上の曖昧さを減らすために用語を固定する。

## UDAM

Uncertainty-Diffusion Anchor Model / 不確実性拡散アンカーモデル。

本 SDD では、UDAM 理論そのものではなく、UDAM の「不確実性」「拡散」「アンカー」という発想を利用したインタラクティブ生成プロトタイプを扱う。

## Noisebrush

本 SDD 内でのプロトタイプ名。

Prompt、Human Layer、Noise Brush、Snapshot を使って、拡散モデルの生成途中状態を人間が探索・介入・仕上げできるプロトタイプを指す。

## Prompt

生成方向を指定するテキスト条件。

Prompt は単なる説明文ではなく、モデルが何として画像を解釈・生成するかを決める条件として扱う。

## Human Layer

人間が描画する独立レイヤー。

完成画像ではなく、生成過程に対する介入信号として扱う。

v0.1 では Generated Image とは別状態として保持し、生成更新によって変更されないことを必須とする。

## Generated Image

現在の生成状態を表示する画像。

Auto Mode では、Generated Image が現在状態として保持され、少しずつ更新される。

## Noise Brush

Generated Image の一部を再び不確定状態に戻すためのブラシ。

消しゴムではない。

選択領域を次回生成で再解釈させるための noiseMask を作る道具である。

## noiseMask

Noise Brush によって作られるマスク。

生成画像のどの領域を再生成対象にするかを示す。

v0.1 では data URL、canvas bitmap、または同等の形式で保持してよい。

## Snapshot

生成途中状態の保存単位。

Snapshot は単なる画像履歴ではなく、探索・復元・仕上げの起点である。

v0.1 では画像 Snapshot による擬似再開でよい。

## Restore

保存済み Snapshot の状態を現在状態へ戻す操作。

Restore は元 Snapshot を削除してはならない。

## Branch

ある Snapshot を起点に別方向の探索を始めること。

v0.1 では `parentId` を保持するが、Tree UI は必須ではない。

## Finish

選択した Snapshot を base image として、より仕上げ寄りの設定で生成を進める操作。

Finish は Explore とは異なり、良い骨格を大きく崩さず細部を整えることを目的とする。

## Explore Mode

良い中間状態・良い骨格を探すためのモード。

少ない steps、控えめな CFG、適度な noiseStrength を使う。

## Finish Mode

Snapshot から仕上げるためのモード。

Explore より steps を増やし、noiseStrength を下げる。

## Step Mode

ユーザー操作 1 回につき 1 回だけ生成更新を実行するモード。

デバッグと挙動確認に使う。

## Auto Mode

一定間隔で生成更新を繰り返すモード。

リアルタイムに生成途中状態が変化する体験を作るために使う。

## Pause Mode

Auto Mode を停止する状態。

Pause 中も Human Layer 描画や Snapshot 操作は可能とする。

## Seed

生成に使う乱数の初期値。

v0.1 では比較・デバッグしやすくするため、初期状態では seed lock を有効にする。

## CFG / Guidance Scale

Prompt をどれだけ強く反映させるかの設定。

v0.1 では初期値 3.0 を基準とする。

## Steps

denoise を何回実行するかの設定。

Explore では少なく、Finish では多くする。

## Noise Strength

現在画像をどの程度不確定状態へ戻すかの設定。

Noise Brush と組み合わせて、どの程度再解釈させるかを制御する。

## Update Interval

Auto Mode で generation request を実行する間隔。

v0.1 の初期値は 300ms とする。

## Mock backend

実モデル未接続でも UI と状態遷移を確認するための仮バックエンド。

v0.1 では Mock backend を先に実装する。

## TinySD backend

軽量拡散モデルを使う実生成バックエンド。

v0.1 では後段タスクとし、利用できない環境では Mock backend へフォールバックできることを優先する。

## 擬似再開

画像 Snapshot を base image として再生成を行うこと。

latent state と timestep を保存しないため、厳密な拡散途中再開ではない。

v0.1 ではこれでよい。

## 真の途中再開

latent state、timestep、scheduler state などを保存し、拡散過程の途中から正確に再開すること。

v0.1 の範囲外である。

## stale result

古い generation request の response が、新しい状態より遅れて返ってくること。

Auto Mode では stale result による上書きを防ぐ必要がある。
