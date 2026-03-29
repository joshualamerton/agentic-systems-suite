from src.models import Product, AgentResponse
from src.llm.router import LLM
from src.planner.planner import Planner
from src.async_layer.executor import AsyncExecutor
from src.ranking.ranker import Ranker
from src.memory.memory import Memory
from src.commerce.affiliate import Affiliate
from src.vector.store import VectorStore

class Agent:
    def __init__(self, tools, provider="openai"):
        self.llm = LLM(provider)
        self.planner = Planner(self.llm)
        self.executor = AsyncExecutor(tools)
        self.ranker = Ranker()
        self.memory = Memory()
        self.vector = VectorStore()
        self.affiliate = Affiliate()
        self.tools = tools

    async def run(self, query: str):
        # update user memory
        self.memory.update(query)

        # semantic recall (optional)
        past_memory = self.vector.search(query)

        # planning
        plan = self.planner.plan(query)

        # 🔴 UPDATED TOOL EXECUTION (SHOPIFY + AMAZON PAAPI)
        tasks = [
            {"tool": "shopify", "params": {"query": query}},
            {"tool": "amazon_paapi", "params": {"query": query}}
        ]

        results = await self.executor.run_all(tasks)

        # flatten product results
        products = []
        for r in results:
            if isinstance(r, list):
                for p in r:
                    products.append(Product(**p))

        # ranking
        ranked = self.ranker.run(
            [p.model_dump() for p in products],
            self.memory.get()
        )

        # affiliate links
        enriched = self.affiliate.run(ranked)
        final_products = [Product(**p) for p in enriched]

        # store query in vector memory
        self.vector.add(query)

        return {
            "plan": plan,
            "products": final_products,
            "memory": past_memory
        }
