class Planner:
    def __init__(self, llm):
        self.llm = llm

    def plan(self, query):
        res = self.llm.run(f"Break into steps:\n{query}")
        return [s.strip("- ").strip() for s in res.split("\n") if s.strip()]
