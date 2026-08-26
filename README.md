# Simple ETL Pipeline

A practical ETL (Extract, Transform, Load) pipeline built with Python, Pandas, and PostgreSQL.

The project processes order data from a CSV source, performs data transformation and quality validation, separates valid and rejected records, and loads valid records into a PostgreSQL database.

The project also includes automated tests, test coverage, logging, error handling, and a GitHub Actions CI workflow.

## Project Overview

This project demonstrates a basic but structured Data Engineering workflow for processing order data.

The pipeline performs the following operations:

1. Extract order data from a CSV file
2. Transform the input data
3. Validate data quality
4. Separate valid and rejected records
5. Save rejected records to a separate CSV file
6. Load valid records into PostgreSQL
7. Handle duplicate records
8. Handle database connection errors
9. Log important pipeline events
10. Run automated tests
11. Measure test coverage
12. Run tests automatically through GitHub Actions

## ETL Flow

```text
CSV Source
    │
    ▼
Extract
    │
    ▼
Transform
    │
    ▼
Data Validation
    │
    ├──────────────► Rejected Records
    │                    │
    │                    ▼
    │              rejected_orders.csv
    │
    ▼
Valid Records
    │
    ▼
PostgreSQL
```

## Key Features

* CSV data extraction
* Data transformation
* Required-field validation
* Data quality checks
* Rejected record handling
* PostgreSQL loading
* Duplicate record handling
* Database connection error handling
* Environment variable configuration
* Structured logging
* Automated unit tests
* Test coverage measurement
* GitHub Actions CI
* Virtual environment support

## Technologies

* Python 3.14
* Pandas
* PostgreSQL
* psycopg2
* python-dotenv
* pytest
* pytest-cov
* Git
* GitHub
* GitHub Actions

## Project Structure

```text
simple-etl-pipeline/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── data/
│   └── orders.csv
│
├── sql/
│
├── src/
│   ├── __init__.py
│   ├── db_connection.py
│   └── main.py
│
├── tests/
│   ├── test_db_connection.py
│   ├── test_extract.py
│   ├── test_load.py
│   ├── test_main.py
│   ├── test_rejected.py
│   ├── test_transform.py
│   └── test_validation.py
│
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Data Source

The input data is stored in:

```text
data/orders.csv
```

The dataset contains order-related information including:

* Order ID
* Customer ID
* Order Date
* Product
* Quantity
* Unit Price

The pipeline calculates `total_amount` during the transformation stage.

## Data Quality

The pipeline performs validation before loading records into PostgreSQL.

Required fields are checked for missing values, including:

* `order_id`
* `customer_id`
* `order_date`
* `product`
* `quantity`
* `unit_price`

Records containing missing values in required fields are rejected.

Valid and rejected records are separated during the validation stage.

Rejected records are saved to:

```text
data/rejected_orders.csv
```

This prevents invalid records from being loaded into the target database.

## Database

PostgreSQL is used as the target database.

Database connection logic is separated into:

```text
src/db_connection.py
```

The main pipeline uses the `get_connection()` function to establish the database connection.

The pipeline also handles duplicate `order_id` values using PostgreSQL's `ON CONFLICT` mechanism.

## Environment Variables

Database credentials are stored in environment variables.

The application expects:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
```

Create a local `.env` file in the project root and provide your actual database credentials.

The `.env` file is excluded from Git and should never be committed to GitHub.

A template is provided in:

```text
.env.example
```

## Requirements

Project dependencies are listed in:

```text
requirements.txt
```

Install them with:

```powershell
pip install -r requirements.txt
```

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/Amineh-Omidpour/simple-etl-pipeline.git
```

Move into the project directory:

```powershell
cd simple-etl-pipeline
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Configure PostgreSQL

Create a `.env` file in the project root and add your PostgreSQL connection settings:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
```

### 6. Run the pipeline

```powershell
python src\main.py
```

## Testing

The project uses `pytest` for automated testing.

Run all tests with:

```powershell
pytest
```

The test suite covers:

* Database connection
* Data extraction
* Data transformation
* Data validation
* Rejected record handling
* Database loading
* Main pipeline execution

The current test suite contains **13 tests**.

## Test Coverage

Test coverage is measured using `pytest-cov`.

Run tests with coverage using:

```powershell
pytest --cov=src --cov-report=term-missing
```

The current project achieves approximately **99% test coverage** across the `src` package.

## Continuous Integration

The project uses GitHub Actions to automatically run the test suite whenever changes are pushed to the `main` branch or a pull request targets `main`.

The workflow is located at:

```text
.github/workflows/tests.yml
```

The CI workflow:

1. Checks out the repository
2. Sets up Python 3.14
3. Installs project dependencies
4. Runs pytest with coverage

This helps ensure that changes to the project do not break the existing functionality.

## Logging

The project uses Python's built-in `logging` module.

Logs are displayed in the terminal and are also stored locally in:

```text
logs/etl.log
```

The logging system records events such as:

* Number of valid rows
* Number of rejected rows
* Database connection status
* Number of rows read
* Number of rows inserted
* Number of rows skipped
* Database errors

The `logs/` directory is excluded from Git.

## Error Handling

The database connection layer handles PostgreSQL connection errors.

If a connection cannot be established, the error is logged and the exception is raised so that the failure is not silently ignored.

## Git and Repository Security

Git is used for version control and GitHub is used to host the repository.

The `.gitignore` file prevents sensitive and unnecessary files from being committed, including:

```text
.env
.venv/
.pytest_cache/
__pycache__/
*.pyc
.coverage
htmlcov/
logs/
data/rejected_orders.csv
```

Database credentials are therefore kept outside the public repository.

## Future Improvements

Possible future improvements include:

* Adding more comprehensive validation rules
* Adding support for additional data sources
* Improving pipeline configuration for multiple environments
* Adding more advanced monitoring and alerting
* Containerizing the application with Docker
* Adding database schema migration management
* Introducing a more scalable orchestration solution for scheduled ETL jobs

## Project Purpose

This project was developed as a practical Data Engineering project to demonstrate a complete basic ETL workflow using Python, Pandas, and PostgreSQL.

It also demonstrates software engineering practices such as automated testing, test coverage, logging, environment-based configuration, version control, and continuous integration with GitHub Actions.
