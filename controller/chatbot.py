from models.user_input import ChatbotPrompt
from services import agent_service


def chatbot_agent(data: ChatbotPrompt, user_id: str):
    return agent_service.agent(data, user_id)
