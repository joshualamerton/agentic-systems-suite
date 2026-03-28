# Agentic Systems Suite

A modular agentic commerce system.

This system:
- Understands intent using LLMs (OpenAI / Gemini)
- Plans multi-step actions
- Queries multiple retailers (Shopify + Amazon)
- Ranks results
- Learns user preferences
- Generates affiliate links

---

## Architecture

User Query → LLM → Planner → Async Execution → Retail APIs → Ranking → Memory → Affiliate Links

---

## Retail Support

- Shopify (live API)
- Amazon (placeholder, ready for PAAPI)

---

## Run

pip install -r requirements.txt

python demos/demo.py
