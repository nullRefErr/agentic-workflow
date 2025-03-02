from smolagents import tool

from services.message_service import send_message
from services.user_service import get_phone_number_info, get_id_info


@tool
def send_chat_message(id: str, phone: str, message: str) -> str:
    """
    Sends messages to a given user phone number with user_id.

    Args:
        id: id of the sender who wants to send message to a phone number. This should be like uuid.
        phone: Phone number of the receiver.
        message: Message to be sent.

    Returns:
        str: Message sent.
    """
    sender = get_id_info(id)
    if not sender:
        return "Sender not found."
    receiver = get_phone_number_info(phone)
    result = send_message(sender["id"], receiver["id"], message)
    return result["message"]
