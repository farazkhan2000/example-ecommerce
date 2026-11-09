class CheckoutService:
    def __init__(self, user_service, order_service):
        self.user_service = user_service
        self.order_service = order_service

    def checkout_registered_user(self, user, total):
        return self.order_service.create_order(
            user_id=user.id,
            email=user.email,
            total=total,
        )