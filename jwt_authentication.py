import jwt
import datetime


def generate_token(secret_key: str, user_id: int):
    payload = {"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}

    return jwt.encode(payload, secret_key, algorithm="HS256")


def verify_token(secret_key: str, token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload.get("user_id")
    except jwt.ExpiredSignatureError:
        return None


secret_key = "secret_key"
token = generate_token(secret_key, 123)
print(verify_token(secret_key, token))