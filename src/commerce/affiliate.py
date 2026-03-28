class Affiliate:
    def run(self, products):
        for p in products:
            p["affiliate"] = p["url"] + "?ref=agent"
        return products
