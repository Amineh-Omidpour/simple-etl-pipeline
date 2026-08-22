import pandas as pd

from src.main import validate_data


def test_validate_data_rejects_missing_required_value():

    data = {
        "order_id": [1, 2, 3],
        "customer_id": [101, 102, 103],
        "order_date": ["2026-08-01", "2026-08-02", "2026-08-03"],
        "product": ["Laptop", "Mouse", None],
        "quantity": [1, 2, 1],
        "unit_price": [800, 25, 300]
    }

    df = pd.DataFrame(data)

    valid_rows, rejected_rows = validate_data(df)

    assert len(valid_rows) == 2
    assert len(rejected_rows) == 1