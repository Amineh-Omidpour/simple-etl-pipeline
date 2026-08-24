import os
import logging
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from db_connection import get_connection

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# Load environment variables
load_dotenv()


# Extract
def extract_data(file_path):
    df = pd.read_csv(file_path)

    print("Original data:")
    print(df)

    return df



# Transform
def transform_data(df):
    df["total_amount"] = df["quantity"] * df["unit_price"]

    return df



# Data quality checks
def validate_data(df):
    required_columns = [
        "order_id",
        "customer_id",
        "order_date",
        "product",
        "quantity",
        "unit_price"
    ]

    valid_rows = []
    rejected_rows = []

    for index, row in df.iterrows():

        if row[required_columns].isnull().any():
            rejected_row = row.to_dict()
            rejected_row["row_number"] = index + 2
            rejected_row["reason"] = "Missing required value"

            rejected_rows.append(rejected_row)
        else:
            valid_rows.append(row)

    logger.info(f"Valid rows: {len(valid_rows)}")
    logger.info(f"Rejected rows: {len(rejected_rows)}")

    return valid_rows, rejected_rows


def save_rejected_rows(rejected_rows):
    if rejected_rows:
        rejected_df = pd.DataFrame(rejected_rows)

        rejected_df.to_csv(
            "data/rejected_orders.csv",
            index=False
        )

        logger.info("Rejected rows saved to data/rejected_orders.csv")

def load_to_database(valid_rows):
    conn = get_connection()
    cursor = conn.cursor()

    logger.info("Database connection successful!")

    inserted_count = 0
    skipped_count = 0

    insert_query = """
        INSERT INTO orders (
            order_id,
            customer_id,
            order_date,
            product,
            quantity,
            unit_price,
            total_amount
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING;
    """

    for row in valid_rows:
        cursor.execute(
            insert_query,
            (
                row["order_id"],
                row["customer_id"],
                row["order_date"],
                row["product"],
                row["quantity"],
                row["unit_price"],
                row["total_amount"]
            )
        )

        if cursor.rowcount == 1:
            inserted_count += 1
        else:
            skipped_count += 1

    conn.commit()

    cursor.close()
    conn.close()

    logger.info(f"Rows read from CSV: {len(valid_rows)}")
    logger.info(f"Rows inserted: {inserted_count}")
    logger.info(f"Rows skipped: {skipped_count}")



def main():
    df = extract_data("data/orders.csv")

    df = transform_data(df)

    valid_rows, rejected_rows = validate_data(df)

    save_rejected_rows(rejected_rows)

    load_to_database(valid_rows)


if __name__ == "__main__":
    main()


