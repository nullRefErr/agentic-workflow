from fastapi import APIRouter

from controller import chatbot
from models.user_input import ChatbotPrompt

router = APIRouter()


@router.post("/chatbot/agent", tags=["chatbot"])
async def chatbot_agent(data: ChatbotPrompt):
    return chatbot.chatbot_agent(data)
