import json
from unittest.mock import patch

from src.utils import input_json


def test_input_json():
    with patch("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(
            {
                "id": 185048835,
                "state": "EXECUTED",
                "date": "2019-05-06T00:17:42.736209",
                "operationAmount": {"amount": "74895.83", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 27921306202254867520",
                "to": "Счет 49884962711830774470",
            }
        )
        assert input_json("../data/operations.json") == []
