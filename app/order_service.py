from app.models import Order


class OrderService:
    def __init__(self):
        self.orders = []

    def create_order(self, user_id, email, total):
        order = Order(
            id=len(self.orders) + 1,
            user_id=user_id,
            email=email,
            total=total,
        )

        self.orders.append(order)

        return order