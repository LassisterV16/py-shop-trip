import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "rb") as config:
        config_info = json.load(config)
        Car.FUEL_PRICE = config_info["FUEL_PRICE"]
        customers = [
            Customer(*customer.values())
            for customer in config_info["customers"]
        ]
        shops = [Shop(*shop.values()) for shop in config_info["shops"]]

        for customer in customers:
            customer.store_selection(shops)
