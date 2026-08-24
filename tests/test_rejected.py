import pandas as pd

from src.main import save_rejected_rows


def test_save_rejected_rows(tmp_path):

    rejected_rows = [
        {
            "order_id": 2,
            "customer_id": 102,
            "order_date": "2026-08-02",
            "product": "Mouse",
            "quantity": None,
            "unit_price": 20,
            "row_number": 3,
            "reason": "Missing required value"
        }
    ]

    output_file = tmp_path / "rejected_orders.csv"

    original_to_csv = pd.DataFrame.to_csv

    def save_to_temp_file(self, path, index=False):
        original_to_csv(self, output_file, index=index)

    pd.DataFrame.to_csv = save_to_temp_file

    try:
        save_rejected_rows(rejected_rows)
    finally:
        pd.DataFrame.to_csv = original_to_csv

    assert output_file.exists()

    result = pd.read_csv(output_file)

    assert len(result) == 1
    assert result["order_id"].iloc[0] == 2
    assert result["reason"].iloc[0] == "Missing required value"

def test_save_rejected_rows_with_empty_list(tmp_path):

    output_file = tmp_path / "rejected_orders.csv"

    original_to_csv = pd.DataFrame.to_csv

    def save_to_temp_file(self, path, index=False):
        original_to_csv(self, output_file, index=index)

    pd.DataFrame.to_csv = save_to_temp_file

    try:
        save_rejected_rows([])
    finally:
        pd.DataFrame.to_csv = original_to_csv

    assert not output_file.exists()
