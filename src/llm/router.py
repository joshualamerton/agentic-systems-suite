from src.config import Config

class LLM:
    def __init__(self, provider="openai"):
        self.provider = provider

        if provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

        elif provider == "gemini":
            import google.generativeai as genai
            genai.configure(api_key=Config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-1.5-flash")

    def run(self, prompt):
        if self.provider == "openai":
            res = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return res.choices[0].message.content

        return self.model.generate_content(prompt).text
