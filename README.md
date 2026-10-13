A Python CLI tool that converts fuel-station PDF reports into structured ODS spreadsheets, automating data extraction, calculations, and document processing.

![AutoTable Example](docs/images/autotable-example.png)

## Motivation

While working at a gas station, I noticed that processing daily reports took me and my colleagues around 15 minutes per day on average. We had to manually transfer information from PDF reports into an ODS spreadsheet, perform calculations, and combine the required documentation. This repetitive workflow also left room for human error, so I built AutoTable to automate the process by extracting the required data, performing calculations, populating the spreadsheet, and merging the documentation PDFs. What used to take around 15 minutes could now be completed almost instantly. In testing, the application processed 20 reports without a single failure.

## ⚙️ Engineering Highlights

- **PDF Data Extraction:** Extracts structured data from PDF reports using PyMuPDF.
- **Data Processing & Calculations:** Processes 20+ fields across 3 fuel products and 4 payment categories, including inventory, sales, prices, and daily totals.
- **Reporting Modes:** Implements 2 processing modes with support for multiple PDFs per reporting period and configurable fuel prices.
- **ODS Generation:** Populates an existing spreadsheet template with extracted and calculated data.
- **PDF Merging:** Combines existing documentation PDFs into a consolidated document.
## 🚀 Quick Start

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/cirkovicivan/autotable-rework.git
cd autotable-rework
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run AutoTable

```bash
python -m src.main
```

## 📖 Usage

### Input Reports

Place the required PDF reports in the configured input directory (`./reports`). The application extracts the relevant information needed for the reporting period.

### Process and Calculate

AutoTable processes the extracted data, including fuel products, inventory, sales, prices, payment categories, and daily totals. Configure fuel prices and use the appropriate report-processing mode for the input data.

### Generate the Spreadsheet

The application populates the configured ODS template with the extracted data and calculated reporting values, reducing repetitive manual data entry.

### Merge Documentation PDFs

AutoTable combines the required existing documentation PDFs into a consolidated PDF, eliminating the need to merge those files manually.

## 🧪 Demo Data and Disclaimer

This repository is an independent portfolio project created to demonstrate PDF processing, data extraction, spreadsheet automation, and document handling in Python.

- **Sample data:** Any example reports, records, or output files included in this repository are intended for demonstration and should use synthetic data rather than real business records.
- **No employer affiliation:** This project is not an official product of, affiliated with, or endorsed by any employer.
- **No confidential information:** The public repository is not intended to contain employer documents, personal information, proprietary templates, internal business records, or other confidential material.
- **Demonstration purposes:** The repository demonstrates an automation workflow and is not a representation of any company's official reporting system.

The project was inspired by a real-world reporting problem. The public repository should contain only code and sample materials that I have the right to publish. This notice does not override applicable laws, contractual obligations, or third-party rights.

## 🤝 Contributing

Contributions are welcome. If you'd like to improve the project, fork the repository, create a branch for your changes, and open a pull request to the `main` branch.