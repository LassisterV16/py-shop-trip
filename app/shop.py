from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def buy_product(self, customer: Customer) -> int | float:
        customer.has_bought[self] = []
        products_cost = 0
        for product, value in customer.product_cart.items():
            price = value * self.products[product]
            products_cost += price
            cost_of_product = int(price) if price % 1 == 0 else price
            customer.has_bought[self].append(
                f"{value} {product}s for {cost_of_product} dollars"
            )
        customer.has_bought[self].append(
            f"Total cost is {products_cost} dollars"
        )
        return products_cost
