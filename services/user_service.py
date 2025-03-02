from repository import db


def get_phone_number_info(phone_number):
    user = db.get_user_by_phone(phone_number)
    if user is not None:
        return {"name": user["name"] + user["surname"], "email": user["email"], "phone": phone_number,
                "id": user["_id"]}
    return {"message": "User not found!"}


def get_id_info(user_id):
    user = db.get_user_by_id(user_id)
    if user is not None:
        return {"name": user["name"] + user["surname"], "email": user["email"], "phone": user["phone"],
                "id": user["_id"]}
    return {"message": "User not found!"}


def get_status(user_id):
    return {"status": db.get_status(user_id)}


def get_trust_score(user_id):
    return {"trust_score": db.get_trust_score(user_id)}


def block_number(user_id, phone_number):
    user = db.get_user_by_id(user_id)

    if phone_number in user["blocked_numbers"]:
        return {"message": "Number already blocked!"}

    db.block_number(user_id, phone_number)
    return {"message": "Number blocked!"}
