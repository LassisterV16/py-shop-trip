from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(*car.values())
        self.has_bought = {}

    def cost_trip(self, shop: Shop, fuel_price: float) -> float:
        distance = (((self.location[0] - shop.location[0]) ** 2)
                    + ((self.location[1] - shop.location[1]) ** 2)) ** 0.5
        fuel_cost = self.car.fuel_cost(distance, fuel_price)
        products_cost = shop.buy_product(self)
        total_cost = fuel_cost + products_cost
        return round(total_cost, 2)
