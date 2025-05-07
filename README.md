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

各ステップごとにエントリポイントが用意されています。`--task`（または `--query`）に記事テーマやゴールを指定して実行してください。

### Step 1: Passive Goal Creator

```bash
python -m passive_goal_creator.main   --query "新入社員に向けて Git の使い方を解説する記事を執筆したい"
```

### Step 2: Prompt Optimizer

```bash
python -m prompt_optimizer.main   --query "新入社員向けに Git の基本操作（リポジトリ作成、コミット、ブランチ運用など）をステップバイステップで解説し、ベストプラクティスやトラブルシュートも含めたテックブログ記事を執筆する。"
```

### Step 3: Single-Pass Planner

```bash
python -m single_path_plan_generation.main   --query "Git の基本概念と操作手順を初心者向けにわかりやすく説明するテックブログ記事を執筆する。"
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
