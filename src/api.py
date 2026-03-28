from fastapi import FastAPI
from src.agent.agent import Agent
from src.tools.registry import Tools
from src.commerce.shopify import Shopify
from src.commerce.amazon import Amazon

app = FastAPI(title="Agentic Systems API")

# setup once
tools = Tools()
tools.add("shopify", Shopify())
tools.add("amazon", Amazon())

agent = Agent(tools)

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/query")
async def query(q: str):
    result = await agent.run(q)
    return result
