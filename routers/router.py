from typing import Annotated

from fastapi import APIRouter, Header

from controller import chatbot
from models.user_input import ChatbotPrompt

router = APIRouter()


@router.post("/chatbot/agent", tags=["chatbot"])
async def chatbot_agent(
        data: ChatbotPrompt,
        x_user_id: Annotated[str | None, Header()] = None):
    return chatbot.chatbot_agent(data, x_user_id)
