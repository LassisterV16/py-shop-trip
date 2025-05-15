import datetime
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config_file = json.load(config)

    fuel_price = config_file["FUEL_PRICE"]
    customers = [
        Customer(*customer.values()) for customer in config_file["customers"]
    ]
    shops = [Shop(*shop.values()) for shop in config_file["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs_dict = {}

        for i, shop in enumerate(shops):
            trip_cost = customer.cost_trip(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            costs_dict[trip_cost] = i

        cheapest_cost = min(costs_dict.keys())
        cheapest_shop = shops[costs_dict[cheapest_cost]]

        if customer.money < cheapest_cost:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        print(
            f"{customer.name} rides to {cheapest_shop.name}\n",
            f"\nDate: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}",
            f"\nThanks, {customer.name}, for your purchase!",
            "\nYou have bought:",
            sep=""
        )
        for product in customer.has_bought[cheapest_shop]:
            print(product)
        customer.money -= cheapest_cost
        print(
            "See you again!\n",
            f"\n{customer.name} rides home",
            f"\n{customer.name} now has {customer.money} dollars\n",
            sep=""
        )


shop_trip()
