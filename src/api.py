from fastapi import FastAPI, Header
from src.agent.agent import Agent
from src.tools.registry import Tools
from src.commerce.shopify import Shopify
from src.commerce.amazon_paapi import AmazonPAAPI
from src.tracking.tracker import Tracker
from src.auth.auth import verify_token
from src.commerce.checkout import Checkout

app = FastAPI(title="Agentic Systems API")

tools = Tools()
tools.add("shopify", Shopify())
tools.add("amazon_paapi", AmazonPAAPI())

agent = Agent(tools)
tracker = Tracker()
checkout = Checkout()

# ---------------- AUTH ----------------
def auth_required(token: str):
    return verify_token(token)

# ---------------- ROUTES ----------------
@app.post("/query")
async def query(q: str, authorization: str = Header(None)):
    if authorization:
        auth_required(authorization.replace("Bearer ", ""))
    return await agent.run(q)

@app.post("/checkout")
def create_checkout(product: dict):
    url = checkout.create_session(product)
    return {"checkout_url": url}

@app.post("/click")
def click(product: dict):
    return tracker.track_click(product)

@app.post("/convert")
def convert(product: dict):
    return tracker.track_conversion(product)
