from fastapi import FastAPI
from src.agent.agent import Agent
from src.tools.registry import Tools
from src.commerce.shopify import Shopify
from src.commerce.amazon_paapi import AmazonPAAPI
from src.tracking.tracker import Tracker

app = FastAPI(
    title="Agentic Systems API",
    description="Agentic commerce system with multi-retailer support and tracking",
    version="1.0.0"
)

# -----------------------------
# TOOL REGISTRATION
# -----------------------------
tools = Tools()
tools.add("shopify", Shopify())
tools.add("amazon_paapi", AmazonPAAPI())

# -----------------------------
# CORE SYSTEM
# -----------------------------
agent = Agent(tools)
tracker = Tracker()

# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/")
def root():
    return {"status": "running"}

# -----------------------------
# MAIN QUERY ENDPOINT
# -----------------------------
@app.post("/query")
async def query(q: str):
    """
    Main agent endpoint

    Example:
    q = "modern sofa under 1000"
    """
    return await agent.run(q)

# -----------------------------
# CLICK TRACKING
# -----------------------------
@app.post("/click")
def click(product: dict):
    """
    Track user click on product
    """
    return tracker.track_click(product)

# -----------------------------
# CONVERSION TRACKING
# -----------------------------
@app.post("/convert")
def convert(product: dict):
    """
    Track completed purchase / conversion
    """
    return tracker.track_conversion(product)
