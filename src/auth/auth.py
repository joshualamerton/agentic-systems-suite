from jose import jwt
from datetime import datetime, timedelta
from src.config import Config

SECRET = Config.JWT_SECRET or "secret"
ALGO = "HS256"

def create_token(user_id):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def verify_token(token):
    return jwt.decode(token, SECRET, algorithms=[ALGO])
