from src.views import main_sheet, get_top_transactions, get_cards
import json


def test_get_top_transactions(sample_transactions):
    result = get_top_transactions(sample_transactions)
    assert isinstance(result, list)
    assert len(result) == 3
    assert result[0]["amount"] == 300


def test_get_cards(sample_transactions):
    result = get_cards(sample_transactions)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["last_digits"] == "1234"
    assert result[0]["total_spent"] == 300


def test_main_sheet(sample_transactions, tmp_path, monkeypatch, user_settings):
    settings_path = tmp_path / "user_settings.json"
    with open(settings_path, "w") as f:
        json.dump(user_settings, f)

    def mock_XLSX_file_read():
        return sample_transactions

    monkeypatch.setattr("src.views.XLSX_file_read", mock_XLSX_file_read)
    monkeypatch.setattr("src.views.open", lambda x: open(settings_path))

    result = main_sheet("2023-01-03 15:00:00")
    data = json.loads(result)

    assert data["greeting"] == "Добрый день"
    assert len(data["cards"]) == 2
    assert len(data["top_transactions"]) == 3
    assert len(data["currency_rates"]) == 2
    assert len(data["stock_prices"]) == 2