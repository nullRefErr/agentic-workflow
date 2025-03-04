from smolagents import CodeAgent

from agents.smolagents_agents.agent_helper import get_agent_model
from agents.smolagents_agents.chat_tools import send_chat_message
from agents.smolagents_agents.user_tools import get_premium_status, get_trust_score_by_id, get_user_info_by_id, \
    get_user_info_by_phone, block_number_by_id, get_trust_score_phone


def get_agent():
    manager_agent = CodeAgent(
        name="manager_agent",
        description="you are a manager agent that manages other agents. generate human-like responses.",
        model=get_agent_model(),
        tools=[
            get_premium_status,
            get_trust_score_by_id,
            get_trust_score_phone,
            get_user_info_by_id,
            get_user_info_by_phone,
            block_number_by_id,
            send_chat_message
        ],
        additional_authorized_imports=[
            'datetime',
            'math',
            'time',
        ]
    )

    return manager_agent
