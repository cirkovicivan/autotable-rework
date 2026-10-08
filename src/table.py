import ezodf


OUTPUT_SHEET = "Report"


def insert_table(payments, fuel, template_path, output_path):
    doc = ezodf.opendoc(template_path)
    sheet = doc.sheets[OUTPUT_SHEET]

    # Report information
    sheet["B4"].set_value(payments.date)

    # Fuel sales
    sheet["B8"].set_value(fuel.diesel.total_sales)
    sheet["C8"].set_value(fuel.diesel.discount)

    sheet["B9"].set_value(fuel.gasoline.total_sales)
    sheet["C9"].set_value(fuel.gasoline.discount)

    sheet["B10"].set_value(fuel.premium_diesel.total_sales)
    sheet["C10"].set_value(fuel.premium_diesel.discount)

    # Payment breakdown
    sheet["B14"].set_value(payments.cash)
    sheet["B15"].set_value(payments.vouchers)
    sheet["B16"].set_value(payments.cards)

    # Tank measurements
    fuel_columns = {
        "B": fuel.diesel,
        "C": fuel.gasoline,
        "D": fuel.premium_diesel,
    }

    for column, metrics in fuel_columns.items():
        sheet[f"{column}20"].set_value(metrics.dpi)
        sheet[f"{column}21"].set_value(metrics.tank_level_cm)
        sheet[f"{column}22"].set_value(metrics.stock_liters)
        sheet[f"{column}23"].set_value(metrics.temperature_c)
        sheet[f"{column}24"].set_value(metrics.stock_at_15c)

    # Invoice discounts
    sheet["B28"].set_value(
        fuel.diesel.invoice_discount
    )
    sheet["B29"].set_value(
        fuel.gasoline.invoice_discount
    )
    sheet["B30"].set_value(
        fuel.premium_diesel.invoice_discount
    )

    doc.saveas(output_path)