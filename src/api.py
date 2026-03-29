from fastapi import FastAPI
from src.agent.agent import Agent
from src.tools.registry import Tools
from src.commerce.shopify import Shopify
from src.commerce.amazon_paapi import AmazonPAAPI
from src.tracking.tracker import Tracker

app = FastAPI(title="Agentic Systems API")

# 🔴 TOOL REGISTRATION (UPDATED)
tools = Tools()
tools.add("shopify", Shopify())
tools.add("amazon_paapi", AmazonPAAPI())

# agent + tracker
agent = Agent(tools)
tracker = Tracker()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/query")
async def query(q: str):
    return await agent.run(q)

@app.post("/click")
def click(product: dict):
    return tracker.track_click(product)

@app.post("/convert")
def convert(product: dict):
    return tracker.track_conversion(product)
