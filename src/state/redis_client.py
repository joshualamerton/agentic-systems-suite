import redis
from src.config import Config

r = redis.Redis(
    host=Config.REDIS_HOST,
    port=6379,
    decode_responses=True
)

class State:
    def set(self, key, value):
        r.set(key, value)

    def get(self, key):
        return r.get(key)
