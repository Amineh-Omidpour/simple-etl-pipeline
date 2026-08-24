import pandas as pd

from src.main import extract_data


def test_extract_data(tmp_path):

    input_file = tmp_path / "orders.csv"

    test_data = pd.DataFrame({
        "order_id": [1, 2],
        "customer_id": [101, 102],
        "product": ["Laptop", "Mouse"],
        "quantity": [1, 2],
        "unit_price": [800, 20]
    })

    test_data.to_csv(input_file, index=False)

    result = extract_data(input_file)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert result["order_id"].tolist() == [1, 2]
    assert result["product"].tolist() == ["Laptop", "Mouse"]