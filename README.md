# BI Datasets Generator

A Command-Line Interface (CLI) Python tool designed to generate realistic, high-volume dimensional datasets for Business Intelligence portfolios and Data Engineering pipelines. 

Currently, the tool generates a synthetic **Employee Dimension** table, which is ideal for testing and building People Analytics dashboards. It uses the `Faker` library to ensure data realism, high cardinality in unique fields (names, emails), and controlled cardinality in business categories (departments, job titles).

## Features

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
* `--rows` : Number of records to generate (Default: 30)
* `--lang` : Language/Locale of the data (`en` or `es`) (Default: `en`)
* `--format`: Output file format (`csv` or `txt`) (Default: `csv`)
* `--sep`  : Column separator character (Default: `,`)

### Examples:

**1. Generate a quick sample of 100 employees in English:**
```bash
python generator.py --rows 100
```

**2. Generate a large dataset for the Spanish market (Chile) with a semicolon separator:**
```bash
python generator.py --lang es --rows 15000 --sep ;
```

## Project Structure (MVP)
* `generator.py`: Main orchestration and data generation script.
* `requirements.txt`: Project dependencies (Faker).
* `.gitignore`: Excludes virtual environments and cached files from version control.