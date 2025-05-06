
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class DecomposedTasks(BaseModel):
    values: list[str] = Field(
        default_factory=list,
        min_items=3,
        max_items=5,
        description="3~5個に分解されたタスク",
    )

    @property
    def text(self) -> str:
        return "\n".join(self.values)

class QueryDecomposer:
    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.current_date = datetime.now().strftime("%Y-%m-%d")

    def run(self, query: str) -> DecomposedTasks:
        prompt = ChatPromptTemplate.from_template(
            f"CURRENT_DATE: {self.current_date}\n"
            "-----\n"
            "タスク: 与えられた目標を具体的で実行可能なタスクに分解してください。\n"
            "要件:\n"
            "1. 以下の行動だけで目標を達成すること。決して指定された以外の行動をとらないこと。\n"
            "   - インターネットを利用して、目標を達成するための調査を行う。\n"
            "   - 最終成果物はmarkdown形式で記載された記事原稿を出力してほしい。\n"
            "2. 各タスクは具体的かつ詳細に記載されており、単独で実行ならびに検証可能な情報を含めること。一切抽象的な表現を含まないこと。\n"
            "3. タスクは実行可能な順序でリスト化すること。\n"
            "4. タスクは日本語で出力すること。\n"
            "目標: {query}"
        )
        chain = prompt | self.llm.with_structured_output(DecomposedTasks)
        return chain.invoke({"query": query})


def main():
    import argparse

    from settings import Settings

    settings = Settings()

    parser = argparse.ArgumentParser(
        description="SinglePathPlanGenerationを使用して一連のタスクを計画します"
    )
    parser.add_argument("--task", type=str, required=True, help="実行するタスク")
    args = parser.parse_args()

    llm = ChatOpenAI(
        model=settings.openai_smart_model, temperature=settings.temperature
    )
    query_decomposer = QueryDecomposer(llm=llm)
    result = query_decomposer.run(query=args.task)

    print(f"{result.text}")


if __name__ == "__main__":
    main()
