from datetime import datetime
import sys

from src.models import Payments, FuelData, FuelMetrics
from src.parser import extract_data
from src.pdfdata import merge_pdf, read_pdf
from src.price_config import change_prices, print_prices
from src.table import insert_table


REPORT_MODES = {
    "standard": [
        "reports/standard_report_1.pdf",
        "reports/standard_report_2.pdf",
        "reports/standard_report_3.pdf",
    ],
    "extended": [
        "reports/extended_report_1.pdf",
        "reports/extended_report_2.pdf",
        "reports/extended_report_3.pdf",
    ],
}

OUTPUT_PDFS = {
    "standard": "output/merged_standard.pdf",
    "extended": "output/merged_extended.pdf",
}

REPORT_TEMPLATE = "templates/report_template.ods"
OUTPUT_TABLE = "output/daily_report.ods"


def main():
    print(f"\n{datetime.now()}")

    while True:
        print("\n=== Report Automation ===")
        print("1. Process daily report")
        print("2. Change fuel prices")
        print("3. View current fuel prices")
        print("4. Exit")

        choice = input("Select an option: ")

        match choice:
            case "1":
                process_daily_report()

            case "2":
                update_prices()

            case "3":
                print_prices()

            case "4":
                print("Goodbye!")
                break

            case _:
                print("Invalid option.")

    return 0


def process_daily_report():
    fuel = FuelData(
        diesel=FuelMetrics(),
        gasoline=FuelMetrics(),
        premium_diesel=FuelMetrics(),
    )

    payments = Payments()

    process_report(
        REPORT_MODES["standard"],
        OUTPUT_PDFS["standard"],
        payments,
        fuel,
    )

    use_extended_report = input(
        "Process extended report? (y/n): "
    ).lower() == "y"

    if use_extended_report:
        process_report(
            REPORT_MODES["extended"],
            OUTPUT_PDFS["extended"],
            payments,
            fuel,
        )

    insert_table(
        payments,
        fuel,
        REPORT_TEMPLATE,
        OUTPUT_TABLE,
    )

    print(f"Report saved to: {OUTPUT_TABLE}")


def process_report(input_reports, output_pdf, payments, fuel):
    merge_pdf(
        input_reports,
        output_pdf,
    )

    text = read_pdf(output_pdf)

    if not text:
        print("No text was found in the PDF.")
        return

    extract_data(
        text,
        payments,
        fuel,
    )


def update_prices():
    prices = {
        "DIESEL": input("Diesel: "),
        "GASOLINE": input("Gasoline: "),
        "PREMIUM DIESEL": input("Premium Diesel: "),
    }

    change_prices(prices)


if __name__ == "__main__":
    sys.exit(main())