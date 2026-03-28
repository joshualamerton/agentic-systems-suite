# Agentic Systems Suite

Production-grade agentic commerce system.

## Features

- Multi-LLM support (OpenAI + Gemini)
- Multi-retailer (Shopify + Amazon-ready)
- Async execution
- Task planning
- Ranking engine
- User memory
- Affiliate monetization
- Typed models (Pydantic)
- Docker-ready

---

## Architecture

User → LLM → Planner → Async Execution → Retail APIs → Ranking → Memory → Affiliate

---

## Setup

pip install -r requirements.txt

---

## Run

python demos/demo.py

---

## Environment

Create `.env`:

OPENAI_API_KEY=xxx  
GEMINI_API_KEY=xxx  

SHOPIFY_STORE_URL=xxx  
SHOPIFY_STOREFRONT_TOKEN=xxx  

---

## Production Ready

- Locked dependencies  
- Docker support  
- Typed models  
- Modular architecture  

---

## Roadmap

- Amazon PAAPI (real)
- Vector DB memory
- FastAPI service
- Image → product matching
