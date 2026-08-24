from unittest.mock import patch

from src.main import main


@patch("src.main.load_to_database")
@patch("src.main.save_rejected_rows")
@patch("src.main.validate_data")
@patch("src.main.transform_data")
@patch("src.main.extract_data")
def test_main_pipeline(
    mock_extract,
    mock_transform,
    mock_validate,
    mock_save_rejected,
    mock_load
):

    mock_extract.return_value = "raw_data"
    mock_transform.return_value = "transformed_data"
    mock_validate.return_value = (
        ["valid_row"],
        ["rejected_row"]
    )

    main()

    mock_extract.assert_called_once_with("data/orders.csv")
    mock_transform.assert_called_once_with("raw_data")
    mock_validate.assert_called_once_with("transformed_data")
    mock_save_rejected.assert_called_once_with(["rejected_row"])
    mock_load.assert_called_once_with(["valid_row"])