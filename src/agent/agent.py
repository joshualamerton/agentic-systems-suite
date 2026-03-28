from src.models import Product, AgentResponse
from src.llm.router import LLM
from src.planner.planner import Planner
from src.async_layer.executor import AsyncExecutor
from src.ranking.ranker import Ranker
from src.memory.memory import Memory
from src.commerce.affiliate import Affiliate

class Agent:
    def __init__(self, tools, provider="openai"):
        self.llm = LLM(provider)
        self.planner = Planner(self.llm)
        self.executor = AsyncExecutor(tools)
        self.ranker = Ranker()
        self.memory = Memory()
        self.affiliate = Affiliate()
        self.tools = tools

    async def run(self, query):
        self.memory.update(query)

        plan = self.planner.plan(query)

        tasks = [
            {"tool": "shopify", "params": {"query": query}},
            {"tool": "amazon", "params": {"query": query}}
        ]

        results = await self.executor.run_all(tasks)

        products = []
        for r in results:
            for p in r:
                products.append(Product(**p))

        ranked = self.ranker.run(
            [p.model_dump() for p in products],
            self.memory.get()
        )

        enriched = self.affiliate.run(ranked)

        final_products = [Product(**p) for p in enriched]

        return AgentResponse(
            plan=plan,
            products=final_products
        )
