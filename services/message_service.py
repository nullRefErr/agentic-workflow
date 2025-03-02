from repository import db


def send_message(from_id: str, to_id: str, message: str):
    db.save_message(from_id, to_id, message)
    return {"message": "Message sent successfully!"}


def get_messages(from_id: str, to_id: str):
    my_messages = db.get_messages(from_id, to_id)
    their_messages = db.get_messages(to_id, from_id)

    sorted_messages = sorted(my_messages + their_messages, key=lambda x: x["created_at"])
    return {"messages": sorted_messages}
