# Global Bank Market Cap — ETL Pipeline

A Python ETL pipeline that extracts market capitalisation data for the world's
largest banks from Wikipedia, converts values across multiple currencies, and
outputs a clean dataset ready for analysis.

---

## What it does

- **Extracts** bank market cap data from Wikipedia using `pandas.read_html()`
- **Transforms** raw strings into numeric values and converts USD into GBP, EUR, and INR using exchange rates loaded from CSV
- **Loads** the cleaned dataset into a structured CSV for use in Power BI, Excel, or SQL

Execution steps and errors are tracked via a custom logging implementation.

---

## Tech stack

| Tool | Purpose |
|---|---|
| Python | Pipeline logic |
| Pandas | Data extraction and transformation |
| Requests | HTTP requests |
| lxml | HTML parsing |
| CSV | Output format |
| Logging | Custom execution tracking |

---

## Pipeline

Wikipedia (HTML) → Extract (pandas.read_html()) → Transform (clean → numeric → currency conversion) → Load (output CSV)

---

## Output

The final CSV contains market cap values in:
- USD (source)
- GBP
- EUR
- INR

Ready to plug into Power BI, Excel, or load into a SQL database.

---

## Project structure

global-bank-market-cap/
├── etl_pipeline.py
├── exchange_rate.csv
├── output/
│   └── Largest_banks_data.csv
├── logs/
│   └── loggy.txt
└── README.md

---

## How to run

pip install pandas requests lxml
python etl_pipeline.py

---

## Skills demonstrated

- Web scraping with pandas.read_html()
- Data cleaning and type conversion
- Multi-currency transformation
- File I/O with CSV
- Custom logging for pipeline observability

---

## Author

Temi
Data Analyst transitioning into Data Engineering
LinkedIn | GitHub
