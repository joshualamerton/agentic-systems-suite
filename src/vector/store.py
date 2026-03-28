import faiss
import numpy as np
from openai import OpenAI
from src.config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

class VectorStore:
    def __init__(self, dim=1536):
        self.index = faiss.IndexFlatL2(dim)
        self.data = []

    def embed(self, text):
        res = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return np.array(res.data[0].embedding).astype("float32")

    def add(self, text):
        vec = self.embed(text)
        self.index.add(np.array([vec]))
        self.data.append(text)

    def search(self, query, k=3):
        if len(self.data) == 0:
            return []

        q = self.embed(query)
        _, idx = self.index.search(np.array([q]), k)

        return [self.data[i] for i in idx[0] if i < len(self.data)]
