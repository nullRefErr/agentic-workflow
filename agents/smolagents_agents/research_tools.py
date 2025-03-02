import os

from litellm import completion
from smolagents import tool


@tool
def researcher(context: str) -> str:
    """
    knowledgebase. Finds anything and researches it for you.

    Args:
        context: the subject which will be explained.

    Returns:
        str: subject explanation.
    """
    response = completion(
        model="openai/gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        messages=[{
            "content": "You are a researcher agent that provides information about any subject. You can research any subject and provide information about it. You should explain what you have been doing to the user.",
            "role": "system"
        }, {
            "content": context,
            "role": "user"
        }]
    )
    return response.choices[0].message.content
