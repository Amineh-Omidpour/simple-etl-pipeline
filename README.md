# Simple ETL Pipeline

A simple ETL pipeline built with Python, Pandas, and PostgreSQL.

## Project Overview

This project implements a simple ETL (Extract, Transform, Load) pipeline for processing order data.

The pipeline reads order data from a CSV file, performs data validation and transformation, separates valid and rejected records, and loads valid records into a PostgreSQL database.

The project also includes error handling and logging to make the pipeline more reliable and easier to monitor.

## ETL Process

The pipeline follows these main steps:

1. Extract data from a CSV file
2. Validate and transform the input data
3. Check data quality
4. Separate valid and rejected records
5. Save rejected records to a separate CSV file
6. Load valid records into PostgreSQL
7. Handle database connection errors
8. Log pipeline execution and important events

## Technologies

- Python
- Pandas
- PostgreSQL
- psycopg2
- python-dotenv
- Git
- GitHub

## Project Structure

```text
simple-etl-pipeline/
│
├── data/
│   └── orders.csv
│
├── src/
│   ├── main.py
│   └── db_connection.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Data Source

The input data is stored in:

```text
data/orders.csv
```

The dataset contains order-related information such as:

- Order ID
- Customer ID
- Order Date
- Product
- Quantity
- Unit Price

The pipeline processes this data before loading it into the database.

## Data Quality

The pipeline performs data quality checks before loading data into PostgreSQL.

Required fields are checked for missing values.

If a record contains a missing value in a required field, the record is considered invalid and is rejected.

Valid and rejected records are separated during the validation process.

Rejected records are saved to:

```text
data/rejected_orders.csv
```

This prevents invalid data from being loaded into the target database.

## Database

PostgreSQL is used as the target database for storing valid order records.

The database connection is handled through:

```text
src/db_connection.py
```

Database connection settings are stored in environment variables using a `.env` file.

The `.env` file contains sensitive information such as database credentials and is excluded from Git using `.gitignore`.

## Environment Variables

The application expects the following environment variables:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
```

The actual database credentials should be stored in a local `.env` file and should never be committed to GitHub.

## Requirements

The required Python packages are listed in:

```text
requirements.txt
```

Install them using:

```powershell
pip install -r requirements.txt
```

## How to Run

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

### 5. Configure the database

Create a `.env` file in the project root directory and add your PostgreSQL connection settings:

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

## Error Handling

The pipeline includes error handling for database connection failures.

If the application cannot connect to PostgreSQL, the error is captured and logged.

For example, an authentication failure caused by an incorrect database password is detected and reported instead of failing silently.

## Logging

The project uses Python's built-in `logging` module to record important events during pipeline execution.

Logs are displayed in the terminal and are also stored locally in:

```text
logs/etl.log
```

The log system records events such as:

- Number of valid rows
- Number of rejected rows
- Database connection status
- Number of rows read
- Number of rows inserted
- Number of rows skipped
- Database errors

The `logs/` directory is excluded from Git and is not committed to the repository.

## Git and GitHub

Git is used for version control and GitHub is used to host the project repository.

The project uses a `.gitignore` file to prevent sensitive and unnecessary files from being committed, including:

```text
.env
.venv/
logs/
__pycache__/
*.pyc
data/rejected_orders.csv
```

## Key Features

- CSV data extraction
- Data validation
- Data quality checks
- Rejected record handling
- PostgreSQL database loading
- Duplicate record handling
- Database error handling
- Environment variable configuration
- Logging
- Virtual environment support
- Git version control

## Future Improvements

Possible future improvements include:

- Adding automated tests
- Adding more comprehensive data validation rules
- Adding configuration files for different environments
- Improving logging and monitoring
- Adding support for additional data sources
- Containerizing the application with Docker
- Adding an automated workflow using GitHub Actions



This project was created as a practical Data Engineering project to demonstrate a basic ETL workflow using Python, Pandas, and PostgreSQL.