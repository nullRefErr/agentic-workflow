import os

from litellm import completion


def translator_helper(content: str) -> str:
    response = completion(
        model="openai/gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        messages=[
            {
                "role": "system",
                "content": """
                you are a translator who have a degree in Linguistics and Translation Studies. you started your career working for a translation agency before becoming a full-time freelance translator. With over 10 years of experience, you have developed expertise in legal documents, user manuals, and literature translation. you are proficient in CAT tools like SDL Trados, MemoQ, and DeepL Pro, ensuring efficiency and accuracy. Translate the given text to English.
                """,
            },
            {
                "role": "user",
                "content": content,
            }
        ]
    )
    return response.choices[0].message.content


def stemma_helper(content: str, user_id: str) -> str:
    response = completion(
        model="openai/gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        messages=[
            {"content": f"""
    User Input: {content}
    ---------------------------
    System Function:
    get_user_info_by_phone(phone: str): Get the current user from database by phone number.
    get_user_info_by_id(id: str): Get the current user from database by id.
    get_premium_status(id: str): Get the current user's premium status from database by id.
    get_trust_score_by_id(id: str): Search given user_id for their Trust Scores before doing business with someone! Our artificial intelligence technology is powered by the latest user feedback, spam activities and dozens of different algorithms, and we calculate a trust score for each phone number using this technology. Returns how much you can trust the user and how viable are they.
    block_number_by_id(id: str, phoneNumber: str): Blocks numbers to call or message to the user.
    send_chat_message(id: str, phone: str, message: str): Sends messages to a given user phone number with user_id.
    researcher(context: str): knowledgebase. Finds anything and researches it for you.
    ----------------------------------
    I have this tool set, I want you to find what user would like to do according to this functions
    add mathing possible function list without parameters at the end of the given input
    do not add if there is no mathing possible function list at the end of the given input
    add original input to your answer. if no mathing possible function list found just say #NONE#
    add mathing possible function list without parameters at the end of the given input
    add generata human-like responses command to your responses
    add 'my id:{user_id}' at the end of the response
    IMPORTANT: Do not answer the questions. do not generate response. just find functions that can be used with the given input. 
            """, "role": "system"},
            {
                "content": "add generata human-like responses command to your responses",
                "role": "system"
            }
        ]
    )
    return response.choices[0].message.content


def response_helper(original_prompt: str, stemma_content: str, output) -> str:
    messages = [
        {
            "role": "system",
            "content": f"""
                original prompt: {original_prompt}
                ----------------------------------
                user said: {stemma_content}
                ----------------------------------
                agent said: {output}
                ----------------------------------
                prepare human-like respond to the user's message
                translate response to language of the original prompt
                """,
        },
    ]
    print(messages[0])

    response = completion(
        model="openai/gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        messages=messages,
    )
    return response.choices[0].message.content
