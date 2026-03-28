from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    title: str
    price: float
    url: str
    affiliate: str | None = None

class AgentResponse(BaseModel):
    plan: List[str]
    products: List[Product]
