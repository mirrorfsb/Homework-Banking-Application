import unittest
from unittest.mock import patch, Mock
from src.external_api import convert_currency, process_transaction


class TestFunctions(unittest.TestCase):

    @patch("requests.get")
    def test_convert_currency(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"result": 1000}  # Мокируем возвращаемый JSON ответ
        mock_get.return_value = mock_response
        result = convert_currency(100, "USD")
        self.assertEqual(result, 1000)

    def test_process_transaction(self):
        file_json = {"amount": 100, "currency": "USD"}
        with patch("src.external_api.convert_currency") as mock_convert_currency:
            mock_convert_currency.return_value = 1000  # Мокируем возвращаемое значение convert_currency
            result = process_transaction(file_json)
            self.assertEqual(result, 1000)