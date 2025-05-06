from typing import List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Goal(BaseModel):
    description: str = Field(..., description="目標の説明")

    @property
    def text(self) -> str:
        return f"{self.description}"

class PassiveGoalCreator:
    def __init__(
        self,
        llm: ChatOpenAI,
    ):
        self.llm = llm
        prompt = ChatPromptTemplate.from_template(
            "ユーザーから指示された要望をもとにテックブログ記事を執筆する。テックブログ記事として達成すべきゴール目標をしてください\n"
            "要件:\n"
            "1. 目標は具体的かつ明確であり、実行可能なレベルで詳細化されている必要があります。\n"
            "2. あなたが実行可能な行動は以下の行動だけです。\n"
            "   - インターネットを利用して、目標を達成するための調査を行う。\n"
            "   - ユーザーのためにテックブログ記事を生成する。\n"
            "3. 決して2.以外の行動を取ってはいけません。\n"
            "ユーザーの入力: {query}"
        )
        self.chain = prompt | self.llm.with_structured_output(Goal)

    def run(self, query: str) -> Goal:

        return self.chain.invoke({"query": query})


def main():
    import argparse

    from settings import Settings

    settings = Settings()

    parser = argparse.ArgumentParser(
        description="PassiveGoalCreatorを利用して目標を生成します"
    )
    parser.add_argument("--task", type=str, required=True, help="実行するタスク")
    args = parser.parse_args()

    llm = ChatOpenAI(
        model=settings.openai_smart_model, temperature=settings.temperature
    )
    goal_creator = PassiveGoalCreator(llm=llm)
    result: Goal = goal_creator.run(query=args.task)

    print(f"{result.text}")


if __name__ == "__main__":
    main()
