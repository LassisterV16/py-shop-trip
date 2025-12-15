import datetime

from app.customer import Customer
from app.utils import clean_round


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

    def product_cart_cost(self, product_cart: dict) -> dict:
        milk_cost = clean_round(
            product_cart["milk"] * self.products["milk"]
        )
        bread_cost = clean_round(
            product_cart["bread"] * self.products["bread"]
        )
        butter_cost = clean_round(
            product_cart["butter"] * self.products["butter"]
        )
        return {"milk": milk_cost, "bread": bread_cost, "butter": butter_cost}

    def purchase(self, customer: Customer) -> None:
        product_cost = self.product_cart_cost(customer.product_cart)
        print(
            f"{datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S")}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:\n"
            f"{customer.product_cart["milk"]} milks for "
            f"{product_cost["milk"]} dollars\n"
            f"{customer.product_cart["bread"]} breads for "
            f"{product_cost["bread"]} dollars\n"
            f"{customer.product_cart["butter"]} butters for "
            f"{product_cost["butter"]} dollars\n"
            f"Total cost is {sum(product_cost.values())} dollars\n"
            "See you again!\n"
        )
