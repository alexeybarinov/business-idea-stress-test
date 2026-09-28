<div align="center">

<img src="../assets/icon.png" alt="Business Idea Stress Test のロゴ" width="110">

# Business Idea Stress Test

**多額の時間や資金を投じる前に、事業アイデアを厳しく検証しましょう**

新規事業の構想について**一度だけ、根拠を重視した批判的な評価**を行うオープンソースの Agent Skill です

[English](../README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt-BR.md) · [日本語](README.ja.md)

[インストール](../docs/installation.md) · [クイックスタート](../docs/quickstart.md) · [最新リリース](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest)
</div>

> **言語について：**このページは日本語訳です。メインの `SKILL.md` は英語ですが、スキルは利用者の言語で回答する設計です。プラットフォーム別の詳しいインストール手順は現在英語で提供しています

## どんな用途に向いているか

事業アイデアが魅力的に見えても、顧客の支払い意思、既存の代替手段、獲得コスト、運営上の制約を確認できていない場合があります。このスキルは安易に賛同したり、楽観的な事業計画を自動生成したりしません。重要な質問を重ね、利用可能な検索機能で外部の根拠を調べ、計画に対する強い反論を検討します

目的は、**確認済みのこと、まだ不明なこと、大きな投資前に実施すべき低コストな実証実験**を明確にすることです

## 6 つの分析段階

1. **創業者へのヒアリング：**課題、支払う顧客、対象地域、予算、リソース、制約を順番に確認し、原則として重要な質問を一つずつ行います
2. **初期検証：**中核となる仮説、現在使われている代替手段、事業成立を妨げる可能性がある問題を特定します
3. **外部調査：**利用環境に調査機能がある場合、需要、顧客、直接・間接の競合を調べ、出典と日付を記録します
4. **財務・運営分析：**収益構造、費用、ユニットエコノミクス、運転資金、前提を明示した複数の条件付きシナリオを整理します
5. **反対意見の検証：**顧客、競合、財務、運営それぞれの視点から、根拠のある反論を検討します
6. **条件付き結論：**不足する証拠を示し、予算上限、成功条件、中止条件を含む小規模な実験を設計します

このスキルだけで実際の顧客インタビューを行ったり、複数の独立した AI を実行したりすることはありません。確認できない数値や価格は不明として明示します

## インストール

**ChatGPT：**[最新リリースの専用 ZIP](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest) をダウンロードします。カスタム Skills に対応するアカウントで **Plugins → Skills → Create → Upload from your computer** を開き、リリース添付の ZIP を選択してください。GitHub が自動生成するソースコード ZIP ではありません。機能の利用可否はプランやワークスペースによって異なります

**Codex：**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a codex
```

**Claude Code：**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a claude-code
```

**Gemini CLI：**

```bash
gemini skills install https://github.com/alexeybarinov/business-idea-stress-test.git
```

Cursor、GitHub Copilot、OpenCode、Claude.ai、手動インストールや更新については[英語版の詳しい手順](../docs/installation.md)をご覧ください。`-g` はユーザー単位のグローバルインストールです。Node.js が必要なのは `npx` を使うインストール時だけで、スキル自体の実行には必要ありません

## 最初の使い方

別の事業アイデアを評価する際は、新しいチャットを開始してください。インストールしたスキルを明示的に指定し、次のように入力します：

```text
Business Idea Stress Test を使ってください。事業アイデア：[説明]
まず、重要な質問を一つずつ行うヒアリングから始めてください
自動的に賛成するのではなく、私の前提を疑い、
根拠のない点を明確にしてください
```

「分かりません」と答えても問題ありません。競合の URL、実際の顧客インタビュー記録、見積書などがあれば、後から追加できます。最終的には、主要な判断の出典、計算に使った前提、測定可能な実験案を確認してください

**プライバシー：**パスワード、不要な顧客の個人情報、共有権限のない機密情報は入力しないでください。重要な法務・財務判断には専門家の確認が必要な場合があります

## バージョンと謝辞

[変更履歴](../CHANGELOG.md) · [リリース](https://github.com/alexeybarinov/business-idea-stress-test/releases)。`npx` によるグローバルインストールの更新例：`npx skills update business-idea-stress-test -g`。ZIP を手動で追加した場合は、新しいファイルの再アップロードが必要な場合があります

着想のもととなったプロジェクトを公開した [Matt Pocock](https://github.com/mattpocock/skills)、[BuildGreatProducts](https://github.com/BuildGreatProducts/builder-os)、[xcrrr](https://github.com/xcrrr/claude-skills)、[Corey Haines](https://github.com/coreyhaines31/marketingskills)、[sickn33](https://github.com/sickn33/agentic-awesome-skills)、[jukeyman](https://github.com/jukeyman/jukeyman-skills) に感謝します。本プロジェクトは独立しており、各作者との提携や公式の承認を意味しません。[詳細な謝辞](../README.md#-standing-on-the-shoulders-of-the-community)

このリポジトリの独自ファイルのライセンス：[MIT](../LICENSE)
