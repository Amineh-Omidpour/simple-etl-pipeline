from unittest.mock import patch, MagicMock

from src.db_connection import get_connection


@patch("src.db_connection.psycopg2.connect")
def test_get_connection(mock_connect):

    mock_connection = MagicMock()
    mock_connect.return_value = mock_connection

    result = get_connection()

    assert result is mock_connection
    mock_connect.assert_called_once()

from unittest.mock import patch, MagicMock

import psycopg2
import pytest

from src.db_connection import get_connection


@patch("src.db_connection.psycopg2.connect")
def test_get_connection(mock_connect):

    mock_connection = MagicMock()
    mock_connect.return_value = mock_connection

    result = get_connection()

    assert result is mock_connection
    mock_connect.assert_called_once()


@patch("src.db_connection.psycopg2.connect")
def test_get_connection_handles_database_error(mock_connect):

    mock_connect.side_effect = psycopg2.Error("Connection failed")

    with pytest.raises(psycopg2.Error):
        get_connection()    