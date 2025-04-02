import pytest
from src.services import investment_bank, description_filter

def test_investment_bank(sample_transactions):
    result = investment_bank("2023-01", sample_transactions, 50)
    assert isinstance(result, float)

def test_description_filter(sample_transactions):
    result = description_filter(sample_transactions, "еда")
    assert isinstance(result, str)
    assert "Еда" in result
    assert "Обед" in result
    assert "Ужин" in result
    assert "Такси" not in result