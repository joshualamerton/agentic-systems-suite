class Ranker:
    def run(self, products, prefs):
        scored = []

        for p in products:
            score = 0

            for k in prefs:
                if k in p["title"].lower():
                    score += 1

            score += max(0, 1 - p["price"]/1000)

            scored.append((score, p))

        return [p for _, p in sorted(scored, reverse=True)]
