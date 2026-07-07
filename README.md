# BI Datasets Generator

A Command-Line Interface (CLI) Python tool designed to generate realistic, high-volume dimensional datasets for Business Intelligence portfolios and Data Engineering pipelines. 

Currently, the tool supports modular data domains, allowing users to generate synthetic data for different corporate departments:
* **Employee Dimension (`employees`):** Ideal for testing and building People Analytics dashboards.
* **Sales Facts (`sales`):** Designed for transactional analysis, revenue tracking, and financial dashboards.

It uses the `Faker` library to ensure data realism, high cardinality in unique fields (names, emails, transaction IDs), and controlled cardinality in business categories (departments, product categories).

## Features

* **Modular Architecture:** Clean separation between the CLI orchestrator and domain-specific data models.
* **Dynamic Volume:** Generate anywhere from a handful of records to tens of thousands of rows instantly.
* **Localization:** Supports regional data generation (currently `en_US` and `es_CL` for the Chilean market).
* **Flexible Output:** Export datasets as `.csv` or `.txt` files.
* **Custom Delimiters:** Control the column separator (e.g., `,` or `;`) to match your ETL ingestion requirements.

## Prerequisites

* Python 3.8+
* Git

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/datasets-generator.git](https://github.com/your-username/datasets-generator.git)
   cd datasets-generator
   ```

2. Create and activate a virtual environment:
   * **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **Mac/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `generator.py` script from your terminal using the available arguments.

### Arguments:
* `--domain` : Data domain to generate (`employees` or `sales`) (Default: `employees`)
* `--rows`   : Number of records to generate (Default: 30)
* `--lang`   : Language/Locale of the data (`en` or `es`) (Default: `en`)
* `--format` : Output file format (`csv` or `txt`) (Default: `csv`)
* `--sep`    : Column separator character (Default: `,`)

### Examples:

**1. Generate a quick sample of 100 employees in English:**
```bash
python generator.py --domain employees --rows 100
```

**2. Generate a large dataset for the Spanish market (Chile) with a semicolon separator:**
```bash
python generator.py --domain employees --lang es --rows 15000 --sep ;
```

**3. Generate 500 sales transactions in Spanish (CLP currency):**
```bash
python generator.py --domain sales --lang es --rows 500
```

## Project Structure
```text
datasets-generator/
│
├── models/                  # Domain-specific data generation models
│   ├── __init__.py          # Python package initializer
│   ├── employees.py         # Employee dimension logic (People Analytics)
│   └── sales.py             # Sales transactional fact logic (Commercial BI)
│
├── generator.py             # Main CLI Orchestrator and exporter
├── README.md                # Project documentation
└── requirements.txt         # Project dependencies (Faker)
```