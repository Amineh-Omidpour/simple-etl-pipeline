import logging
import psycopg2
import pytest

from unittest.mock import MagicMock, patch
from src.main import load_to_database

def test_load_to_database_connection_error():

    with patch(
        "src.main.get_connection",
        side_effect=psycopg2.OperationalError("Database connection failed")
    ):

        with pytest.raises(psycopg2.OperationalError):

            load_to_database([])


def test_load_to_database_inserts_valid_rows():

    valid_rows = [
        {
            "order_id": 1,
            "customer_id": 101,
            "order_date": "2026-08-01",
            "product": "Laptop",
            "quantity": 1,
            "unit_price": 800,
            "total_amount": 800
        },
        {
            "order_id": 2,
            "customer_id": 102,
            "order_date": "2026-08-02",
            "product": "Mouse",
            "quantity": 2,
            "unit_price": 25,
            "total_amount": 50
        }
    ]

    mock_connection = MagicMock()
    mock_cursor = mock_connection.cursor.return_value

    mock_cursor.rowcount = 1

    with patch("src.main.get_connection", return_value=mock_connection):

        load_to_database(valid_rows)

    assert mock_cursor.execute.call_count == 2
    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()


def test_load_to_database_skips_existing_rows(caplog):

    caplog.set_level(logging.INFO)
    valid_rows = [
        {
            "order_id": 1,
            "customer_id": 101,
            "order_date": "2026-08-01",
            "product": "Laptop",
            "quantity": 1,
            "unit_price": 800,
            "total_amount": 800
        }
    ]

    mock_connection = MagicMock()
    mock_cursor = mock_connection.cursor.return_value

    mock_cursor.rowcount = 0

    with patch("src.main.get_connection", return_value=mock_connection):

        load_to_database(valid_rows)

    assert mock_cursor.execute.call_count == 1
    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()

    assert "Rows read from CSV: 1" in caplog.text
    assert "Rows inserted: 0" in caplog.text
    assert "Rows skipped: 1" in caplog.text   