# SDD Agent Handoff v0.1

この文書は、実装エージェントへ渡すための作業指示である。

## 1. 役割

あなたは `Unjuno/uncertainty-diffusion-anchor-model` の `docs/sdd/` 仕様に従って、Noisebrush / UDAM Interactive Prototype v0.1 を実装する。

既存の UDAM 理論文書を拡張することは目的ではない。

## 2. 読む順番

1. `AGENTS.md`
2. `AGENTS.sdd.md`
3. `IMPLEMENTATION_SDD.md`
4. `docs/sdd/README.md`
5. `docs/sdd/AGENTS.md`
6. `docs/sdd/spec.md`
7. `docs/sdd/architecture.md`
8. `docs/sdd/tasks.md`
9. `docs/sdd/acceptance.md`
10. `docs/sdd/glossary.md`
11. `docs/sdd/decisions.md`
12. `docs/sdd/grill.md`

## 3. v0.1 の対象

作る体験は以下である。

```text
Prompt 入力
→ Human Layer 描画
→ Generated Image 更新
→ Noise Brush 指定
→ Auto loop
→ Snapshot 保存
→ Snapshot 復元
→ Snapshot から Finish
```

## 4. 実装順序

`docs/sdd/tasks.md` の順番に従う。

```text
Static UI
→ AppState
→ Human Layer canvas
→ Mock backend
→ Basic generation
→ Noise Brush
→ Auto loop
→ Snapshot
→ Finish
→ TinySD backend hook
```

Mock backend より前に TinySD 連携を始めない。

## 5. v0.1 の対象外

以下は実装しない。

- 図構造認識
- Mermaid / UML / SVG 変換
- ControlNet
- 認証
- 共同編集
- クラウドデプロイ
- latent snapshot の完全再開
- 高品質モデル調整

## 6. 最小デモ

v0.1 は、以下の流れが通れば成立する。

```text
1. アプリを起動する。
2. Prompt を入力する。
3. Step で Generated Image を表示する。
4. Human Layer に描く。
5. Auto を開始する。
6. Generated Image に Noise Brush を塗る。
7. Save Snapshot を押す。
8. 別状態まで進める。
9. Snapshot を Restore する。
10. Finish from Snapshot を実行する。
```

## 7. 完了判定

完了判定は `docs/sdd/acceptance.md` に従う。

主観ではなく、観察可能な挙動で判定する。

## 8. 迷った場合

仕様が曖昧な場合、コード側で勝手に決めない。

`docs/sdd/grill.md` に従って仕様更新案を出す。

## 9. 最重要制約

- Human Layer は Generated Image と分ける。
- Generated Image 更新で Human Layer を変えない。
- Noise Brush は Generated Image にだけ適用する。
- Auto Mode は必ず停止できる。
- Snapshot は Restore と Finish の起点である。
- 実モデルがなくても Mock backend で確認できる。
