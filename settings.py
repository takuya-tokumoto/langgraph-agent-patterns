import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    TAVILY_API_KEY: str
    LANGCHAIN_TRACING_V2: str = "true"
    LANGCHAIN_ENDPOINT: str = "https://api.smith.langchain.com"
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str = "agent-book"

    # for Azure OpenAI
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str = "https://test-toku-instance.openai.azure.com/"
    AZURE_OPENAI_DEPLOYMENT_NAME: str = "gpt-4"
    AZURE_OPENAI_VERSION: str = "2024-02-15-preview"


    # for Application
    openai_smart_model: str = "gpt-4o"
    openai_embedding_model: str = "text-embedding-3-small"
    anthropic_smart_model: str = "claude-3-5-sonnet-20240620"
    temperature: float = 0.0
    default_reflection_db_path: str = "tmp/reflection_db.json"

    def __init__(self, **values):
        super().__init__(**values)
        self._set_env_variables()

    def _set_env_variables(self):
        for key in self.__annotations__.keys():
            if key.isupper():
                os.environ[key] = getattr(self, key)
