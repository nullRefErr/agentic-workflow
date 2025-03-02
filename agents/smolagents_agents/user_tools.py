from smolagents import tool

from services.user_service import get_phone_number_info, get_id_info, get_status, get_trust_score, block_number


@tool
def get_user_info_by_phone(phone: str) -> dict[str, str, str, str]:
    """
    Get the current user from database by phone number.

    Args:
        phone: Given phone number to get the user info from database.

    Returns:
        name: Name of the user with the given phone number.
        email: Email of the user with the given phone number.
        phone: Phone number of the user.
        id: id of the user with the given phone number.
    """
    user = get_phone_number_info(phone)
    return user


@tool
def get_user_info_by_id(id: str) -> dict[str, str, str]:
    """
    Get the current user from database by id.

    Args:
        id: Given user id to get the user info from database.

    Returns:
        name: Name of the user with the given phone number.
        email: Email of the user with the given phone number.
        phone: Phone number of the user.
    """

    user = get_id_info(id)
    return user


@tool
def get_premium_status(id: str) -> dict[str]:
    """
    Get the current user's premium status from database by id.

    Args:
        id: Given id to get the user info from database.

    Returns:
        status: User's premium status PREMIUM or IDLE or NONE
    """
    result = get_status(id)
    return result


@tool
def get_trust_score_by_id(id: str) -> dict[int]:
    """
    Search for their Trust Scores before doing business with someone! Our artificial intelligence technology is powered by the latest user feedback, spam activities and dozens of different algorithms, and we calculate a trust score for each phone number using this technology. Returns how much you can trust the user and how viable are they.

    Args:
        id: Given id to get the user info from database.

    Returns:
        trust_score: Integer value to describe User's performance
    """
    result = get_trust_score(id)
    return result


@tool
def block_number_by_id(id: str, phone_number: str) -> str:
    """
    Blocks numbers to call or message to the user.

    Args:
        id: this is the user id who wants to block given phone number.
        phone_number: Given phone number to block by id.

    Returns:
        A string message to describe the result of the action.
    """
    result = block_number(id, phone_number)
    return result["message"]
