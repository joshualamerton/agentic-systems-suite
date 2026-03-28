import asyncio

class AsyncExecutor:
    def __init__(self, tools):
        self.tools = tools

    async def run(self, name, params):
        tool = self.tools.get(name)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, tool.execute, params)

    async def run_all(self, tasks):
        return await asyncio.gather(*[
            self.run(t["tool"], t["params"]) for t in tasks
        ])
