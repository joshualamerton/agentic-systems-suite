from pinecone import Pinecone
from openai import OpenAI
from src.config import Config

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
index = pc.Index("agentic-memory")

client = OpenAI(api_key=Config.OPENAI_API_KEY)

class VectorStore:
    def embed(self, text):
        res = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return res.data[0].embedding

    def add(self, text):
        vec = self.embed(text)
        index.upsert([(text, vec)])

    def search(self, query):
        vec = self.embed(query)
        res = index.query(vector=vec, top_k=3, include_metadata=True)
        return [m["id"] for m in res["matches"]]
