import os
import logging
import psycopg2

logger = logging.getLogger(__name__)

from dotenv import load_dotenv


load_dotenv()


def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        return conn

    except psycopg2.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise