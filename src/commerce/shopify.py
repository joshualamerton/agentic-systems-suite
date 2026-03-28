import requests
from src.config import Config

class Shopify:
    def execute(self, params):
        query = params["query"]

        if not Config.SHOPIFY_STORE_URL:
            return [{"title": "Fallback Sofa", "price": 500, "url": "#"}]

        endpoint = f"{Config.SHOPIFY_STORE_URL}/api/2023-01/graphql.json"

        headers = {
            "X-Shopify-Storefront-Access-Token": Config.SHOPIFY_STOREFRONT_TOKEN,
            "Content-Type": "application/json"
        }

        q = {
            "query": f"""
            {{
              products(first: 5, query: "{query}") {{
                edges {{
                  node {{
                    title
                    handle
                  }}
                }}
              }}
            }}
            """
        }

        res = requests.post(endpoint, json=q, headers=headers).json()

        out = []
        for e in res["data"]["products"]["edges"]:
            n = e["node"]
            out.append({
                "title": n["title"],
                "price": 100,
                "url": f"{Config.SHOPIFY_STORE_URL}/products/{n['handle']}"
            })

        return out
