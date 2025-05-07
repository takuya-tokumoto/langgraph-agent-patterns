# LangGraph Agent Patterns テストリポジトリ

「LangChain と LangGraph による RAG・AI エージェント［実践］入門」第12章に対応した実装トライアルをまとめたリポジトリです。
各ステップで紹介したデザインパターンを順番に学習・検証できます。

---

## 🚀 Getting Started

### 1. リポジトリをクローン

```bash
git clone https://github.com/takuya-tokumoto/langgraph-agent-patterns.git
cd langgraph-agent-patterns
```

### 2. 開発環境のセットアップ

```bash
# Conda 環境を作成・有効化
conda create -n langgraph-test python=3.10.12
conda activate langgraph-test

# 依存パッケージをインストール
pip install -r requirements.txt
```

---

## 🎯 Usage

各ステップごとにエントリポイントが用意されています。`--task`に記事テーマやゴールを指定して実行してください。

### Step 1: Passive Goal Creator

```bash
python -m passive_goal_creator.main  --task "新入社員に向けて Git の使い方を解説する記事を執筆したい"
```

### Step 2: Prompt Optimizer

```bash
python -m prompt_optimizer.main --task "新入社員向けにGitの基本的な使い方を解説するテックブログ記事を執筆する。具体的には、Gitの基本概念（リポジトリ、コミット、ブランチなど）を分かりやすく説明し、実際の操作手順（リポジトリの作成、クローン、コミット、プッシュ、プル、ブランチの作成とマージなど）をステップバイステップで解説する。また、Gitを使用する際のベストプラクティスやよくあるトラブルシューティングについても触れる。記事は初心者が理解しやすいように、専門用語を避け、図やスクリーンショット を用いて視覚的にサポートする。最終的に、新入社員がGitを使って基本的なバージョン管理を自信を持って行えるようになることを目指す。"
```

### Step 3: Single-Pass Planner

```bash
python -m single_path_plan_generation.main_dev --task "新入社員向けにGitの基本的な使い方を解説するテックブログ記事を執筆する。記事はGitの基本概念（リポジトリ、コミット、ブランチなど）を分かりやすく説明し、実 際の操作手順（リポジトリの作成、クローン、コミット、プッシュ、プル、ブランチの作成とマージなど）をステップバイステップで解説する。また、Gitを使用する際のベストプラクティスやよくあるトラブルシューティングについても触れる。記事は初心者が理解しやすいように、専門用語を避け、図やスクリー ンショットを用いて視覚的にサポートする。最終的に、新入社員がGitを使って基本的なバージョン管理を自信を持って行えるようになることを目指す。( 測定基準: 1. 記事の公開後1ヶ月以内に、記事を読んだ新入社員の80%以上がGitの基本操作に関する社内テストで80点以上を取得する。2. 記事の公開後1ヶ月以 内に、記事を読んだ新入社員の70%以上がGitを使用したプロジェクトでの初回コミットを成功させる。3. 記事の公開後1ヶ月以内に、記事に対するフィードバックアンケートで、80%以上の新入社員が記事の内容が理解しやすかったと回答する。)"
```

### Step 4: 通しで実行してみる

```bash
python -m develop.main  --task "Git の基本概念と操作手順を初心者向けにわかりやすく説明するテックブログ記事を執筆する。"
```

> **Tip:** 各モジュール内に `README.md` や `main.py` があり、詳しい使い方や引数の説明も掲載しています。


---

## 🔗 Reference

- **書籍**  
  LangChain と LangGraph による RAG・AI エージェント［実践］入門 第12章  
  https://www.amazon.co.jp/dp/4297145308

- **リポジトリ**  
  https://github.com/takuya-tokumoto/langgraph-agent-patterns

---
