import asyncio
from src.agent.agent import Agent
from src.tools.registry import Tools
from src.commerce.shopify import Shopify
from src.commerce.amazon import Amazon

tools = Tools()
tools.add("shopify", Shopify())
tools.add("amazon", Amazon())

agent = Agent(tools)

async def main():
    result = await agent.run("modern sofa under 1000")
    print(result)

asyncio.run(main())
