import pytest
import pandas as pd
import os
from datetime import datetime, timedelta


@pytest.fixture
def sample_transactions():
    return [
        {"Номер карты": "1234", "Сумма операции": 100, "Категория": "Еда", "Описание": "Обед",
         "Дата операции": "01.01.2023 12:00:00", "Дата платежа": "01.01.2023", "Сумма операции с округлением": 100,
         "Кэшбэк": 1},
        {"Номер карты": "1234", "Сумма операции": 200, "Категория": "Транспорт", "Описание": "Такси",
         "Дата операции": "02.01.2023 12:00:00", "Дата платежа": "02.01.2023", "Сумма операции с округлением": 200,
         "Кэшбэк": 2},
        {"Номер карты": "5678", "Сумма операции": 300, "Категория": "Еда", "Описание": "Ужин",
         "Дата операции": "03.01.2023 12:00:00", "Дата платежа": "03.01.2023", "Сумма операции с округлением": 300,
         "Кэшбэк": 3},
    ]


@pytest.fixture
def sample_df(sample_transactions):
    return pd.DataFrame(sample_transactions)


@pytest.fixture
def user_settings():
    return {
        "user_currencies": ["USD", "EUR"],
        "user_stocks": ["AAPL", "GOOGL"]
    }


@pytest.fixture
def mock_requests(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if "exchangerates_data" in args[0]:
            return MockResponse({"result": 75.5}, 200)
        elif "api-ninjas" in args[0]:
            return MockResponse({"price": 150.75}, 200)
        return MockResponse(None, 404)

    monkeypatch.setattr("requests.get", mock_get)