from abc import ABC, abstractmethod
from collections import namedtuple
import inspect


import promotions


Customer = namedtuple('Customer', 'name, fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


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


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0)]

    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    bulk_cart = [LineItem('banana', 30, .5),
            LineItem('apple', 10, 1.5)]

    print(Order(joe, bulk_cart, bulk_promo))

    large_cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

    print(Order(joe, large_cart, large_order_promo))

    promos = [fidelity_promo, bulk_promo, large_order_promo]

    def best_promo(order):
        return max(promo(order) for promo in promos)

    best_cart = [LineItem('banana', 30, 1.0)]
    print(Order(ann, best_cart, best_promo))

    promos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']

    best_cart = [LineItem('banana', 30, 1.0)]
    print(Order(ann, best_cart, best_promo))

    promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]

    best_cart = [LineItem('banana', 30, 1.0)]
    print(Order(ann, best_cart, best_promo))