from dataclasses import dataclass


@dataclass
class Payments:
    date: str = ""
    cards: float = 0
    cash: float = 0
    vouchers: float = 0


@dataclass
class FuelMetrics:
    total_sales: float = 0
    discount: float = 0
    invoice_discount: float = 0
    quantity_liters: float = 0
    tank_level_cm: float = 0
    stock_liters: float = 0
    temperature_c: float = 0
    stock_at_15c: float = 0


@dataclass
class FuelData:
    diesel: FuelMetrics
    gasoline: FuelMetrics
    premium_diesel: FuelMetrics