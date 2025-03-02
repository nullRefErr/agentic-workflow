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


def stemma_helper(content: str) -> str:
    response = completion(
        model="openai/gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        messages=[
            {"content": """
    get_user_info_by_phone(phone: str) -> dict[str, str, str, str]:
        Get the current user from database by phone number.
        Args:
            phone: Given phone number to get the user info from database.
        Returns:
            name: Name of the user with the given phone number.
            email: Email of the user with the given phone number.
            phone: Phone number of the user.
            id: id of the user with the given phone number.
            
    get_user_info_by_id(id: str) -> dict[str, str, str]:
        Get the current user from database by id.
        Args:
            id: Given user id to get the user info from database.
        Returns:
            name: Name of the user with the given phone number.
            email: Email of the user with the given phone number.
            phone: Phone number of the user.
            
    get_premium_status(id: str) -> dict[str]:
        Get the current user's premium status from database by id.
        Args:
            id: Given id to get the user info from database.
        Returns:
            status: User's premium status PREMIUM or IDLE or NONE
    
    get_trust_score_by_id(id: str) -> dict[int]:
        Search given user_id for their Trust Scores before doing business with someone! Our artificial intelligence technology is powered by the latest user feedback, spam activities and dozens of different algorithms, and we calculate a trust score for each phone number using this technology. Returns how much you can trust the user and how viable are they.
        Args:
            id: Given id to get the user info from database.
        Returns:
            trust_score: Integer value to describe User's performance
    
    block_number_by_id(id: str, phoneNumber: str) -> str:
        Blocks numbers to call or message to the user.
        Args:
            id: this is the user id who wants to block given phone number.
            phoneNumber: Given phone number to block by id.
        Returns:
            A string message to describe the result of the action.
            
    send_chat_message(id: str, phone: str, message: str) -> str:
        Sends messages to a given user phone number with user_id.
        Args:
            agent: Name of the agent.
            id: id of the sender who wants to send message to a phone number. This should be like uuid.
            phone: Phone number of the receiver.
            message: Message to be sent.
        Returns:
            str: Message sent.
    
    researcher(context: str) -> str:
        knowledgebase. Finds anything and researches it for you.
        Args:
            context: the subject which will be explained.
        Returns:
            str: subject explanation.
            """, "role": "system"},
            {
                "content": "I have this tool set, I want you to find what user would like to do according to this functions",
                "role": "system"
            },
            {
                "content": "add mathing possible function list without parameters at the end of the given input",
                "role": "system"
            },
            {
                "content": "do not add if there is no mathing possible function list at the end of the given input",
                "role": "system"
            },
            {
                "content": "do not answer the question add original input to your answer",
                "role": "system"
            },
            {
                "content": "add my id at the end of the given input",
                "role": "system"
            },
            {
                "content": "my id is ddf73652-052f-469f-94a8-79f83b8627e6",
                "role": "system"
            },
            {
                "content": "if trust score is less than 50 it is not viable",
                "role": "system"
            },
            {
                "content": "add generata human-like responses command to your responses",
                "role": "system"
            },
            {
                "content": content,
                "role": "user"
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
