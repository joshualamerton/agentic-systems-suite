import stripe
from src.config import Config

stripe.api_key = Config.STRIPE_SECRET_KEY

class Checkout:
    def create_session(self, product):
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": product["title"]},
                    "unit_amount": int(product["price"] * 100),
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://localhost:3000/success",
            cancel_url="http://localhost:3000/cancel",
        )
        return session.url
