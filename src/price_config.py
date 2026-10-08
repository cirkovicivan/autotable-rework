import json

FUEL_TYPES = [
    "DIESEL",
    "GASOLINE",
    "PREMIUM DIESEL",
]

PRICE_FILE = "fuel_prices.json"

def get_prices():
    with open(PRICE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def change_prices(prices):
    validated_prices = {}

    for fuel_type in FUEL_TYPES:
        if fuel_type not in prices:
            raise ValueError(
                f"Missing price for fuel type: {fuel_type}"
            )

        validated_prices[fuel_type] = float(prices[fuel_type])

    with open(PRICE_FILE, "w", encoding="utf-8") as file:
        json.dump(
            validated_prices,
            file,
            indent=4,
        )


def print_prices():
    prices = get_prices()

    for fuel_type, price in prices.items():
        print(f"{fuel_type}: {price:.2f}")