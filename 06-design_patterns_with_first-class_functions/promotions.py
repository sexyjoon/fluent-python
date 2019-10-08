def fidelity_promo(order):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""

    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_promo(order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""

    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""

    return order.total() * .07 if len(order.cart) >= 10 else 0