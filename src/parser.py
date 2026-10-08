import re

from src.price_config import get_prices


FUEL_TYPES = [
    "DIESEL",
    "GASOLINE",
    "PREMIUM DIESEL",
]


def extract_data(text, payments, fuel):
    prices = get_prices()

    sales_report = _extract_section(
        text,
        "SALES SUMMARY",
        "END SALES SUMMARY",
    )

    _extract_payments(sales_report, payments)
    discounts = _calculate_discounts(sales_report, prices)
    _extract_fuel_data(text, fuel, discounts)


def _extract_section(text, start_marker, end_marker):
    try:
        section = text.split(start_marker, 1)[1]
        return section.split(end_marker, 1)[0]
    except IndexError:
        raise ValueError(
            f"Could not find report section: {start_marker}"
        )


def _extract_payments(sales_report, payments):
    date_match = re.search(
        r"DATE:\s*(\d{2}\.\d{2}\.\d{4})",
        sales_report,
    )

    if not date_match:
        raise ValueError("Could not find report date.")

    payments.date = date_match.group(1)

    payments_section = _extract_section(
        sales_report,
        "PAYMENTS",
        "END PAYMENTS",
    )

    values = re.findall(
        r"[\d,]+\.\d+",
        payments_section,
    )

    if len(values) < 4:
        raise ValueError("Incomplete payment data.")

    payments.cash += _parse_number(values[1])
    payments.vouchers += _parse_number(values[2])
    payments.cards += _parse_number(values[3])


def _calculate_discounts(sales_report, prices):
    product_rows = re.findall(
        r"PRODUCT:\s*(DIESEL|GASOLINE|PREMIUM DIESEL)\s+"
        r"QUANTITY:\s*([\d,]+\.\d+)\s+"
        r"PRICE:\s*([\d,]+\.\d+)\s+"
        r"CASH:\s*([\d,]+\.\d+)\s+"
        r"INVOICE:\s*([\d,]+\.\d+)",
        sales_report,
    )

    discounts = {
        fuel_type: {
            "discount": 0.0,
            "invoice_discount": 0.0,
        }
        for fuel_type in FUEL_TYPES
    }

    for fuel_type, quantity, price, cash, invoice in product_rows:
        quantity = _parse_number(quantity)
        price = _parse_number(price)
        cash = _parse_number(cash)
        invoice = _parse_number(invoice)

        if price < prices[fuel_type]:
            discounts[fuel_type]["discount"] += quantity

        if invoice > 0:
            if cash == 0:
                discounts[fuel_type]["invoice_discount"] += quantity
            else:
                discounts[fuel_type]["invoice_discount"] += (
                    invoice / price
                )

    for fuel_type in FUEL_TYPES:
        discounts[fuel_type]["discount"] = round(
            discounts[fuel_type]["discount"], 2
        )
        discounts[fuel_type]["invoice_discount"] = round(
            discounts[fuel_type]["invoice_discount"], 2
        )

    return discounts


def _extract_fuel_data(text, fuel, discounts):
    tank_sections = re.findall(
        r"(TANK\s+\d+.*?)(?=TANK\s+\d+|END TANKS)",
        text,
        re.DOTALL,
    )

    fuel_metrics = [
        fuel.diesel,
        fuel.gasoline,
        fuel.premium_diesel,
    ]

    for index, tank_text in enumerate(tank_sections[:3]):
        data = _parse_tank(tank_text)

        metrics = fuel_metrics[index]
        fuel_type = FUEL_TYPES[index]

        metrics.total_sales += data["sales"]
        metrics.discount += discounts[fuel_type]["discount"]
        metrics.invoice_discount += discounts[fuel_type][
            "invoice_discount"
        ]

        metrics.dpi = data["density"]
        metrics.tank_level_cm = data["level"]
        metrics.stock_liters = data["stock"]
        metrics.temperature_c = data["temperature"]
        metrics.stock_at_15c = data["stock_at_15c"]


def _parse_tank(tank_text):
    values = {}

    for line in tank_text.splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        values[key.strip()] = value.strip()

    required_fields = {
        "SALES": "sales",
        "DENSITY": "density",
        "LEVEL": "level",
        "STOCK": "stock",
        "TEMPERATURE": "temperature",
        "STOCK 15C": "stock_at_15c",
    }

    for field in required_fields:
        if field not in values:
            raise ValueError(
                f"Missing tank field: {field}"
            )

    return {
        name: _parse_number(values[field])
        for field, name in required_fields.items()
    }


def _parse_number(value):
    return float(value.replace(",", ""))