import pandas as pd

from src.main import transform_data


def test_transform_data_calculates_total_amount():

    df = pd.DataFrame({
        "quantity": [2],
        "unit_price": [25]
    })

    result = transform_data(df)

    assert result["total_amount"].iloc[0] == 50