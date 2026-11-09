from app.user_service import UserService
from app.order_service import OrderService
from app.checkout_service import CheckoutService


def test_registered_user_can_checkout():
    user_service = UserService()
    order_service = OrderService()

    checkout_service = CheckoutService(
        user_service,
        order_service,
    )

    user = user_service.create_user(
        "customer@example.com"
    )

    order = checkout_service.checkout_registered_user(
        user,
        100.0,
    )

    assert order.user_id == user.id
    assert order.email == "customer@example.com"
    assert order.total == 100.0