from repository import db


def add_spam(userId, phone):
    db.add_spam(userId, phone)
    return {"message": "Spam reported!"}


def is_phone_spam(phone):
    spam_count = db.check_for_spam(phone)
    if spam_count > 2:
        return {"message": "Phone number is spam!"}
    else:
        return {"message": "Phone number is not spam!"}
