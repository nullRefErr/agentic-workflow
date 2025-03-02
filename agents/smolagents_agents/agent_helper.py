import os

from smolagents import LiteLLMModel


def get_agent_model():
    model = LiteLLMModel(
        # model_id="ollama/llama3.1:8b",
        # api_base="http://localhost:11434",
        model_id="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    return model
