from agents.smolagents_agents.agent import get_agent
from models.user_input import ChatbotPrompt
from services.ai_helper_service import translator_helper, stemma_helper, response_helper


def run_agent(data: ChatbotPrompt):
    # Get Agents
    agent = get_agent()

    # Translate user prompt and do not change anything else
    translate = translator_helper(data.input)

    # Find possible agent functions to run and create a new plain prompt which can be undestood by the agent
    new_agent_prompt = stemma_helper(translate)

    # Run agents to do the job and get response
    agent_response = agent.run(new_agent_prompt)

    # Prepare human-like response to the user's message and translate it to the language of the original prompt
    res = response_helper(data.input, new_agent_prompt, agent_response)

    return res
