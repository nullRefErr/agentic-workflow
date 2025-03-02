from models.user_input import ChatbotPrompt
from services import agent_service


def chatbot_agent(data: ChatbotPrompt):
    return agent_service.run_agent(data)
