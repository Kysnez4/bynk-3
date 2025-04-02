import pytest
from src.utils import XLSX_file_read, file_df
import os
import pandas as pd


def test_XLSX_file_read_success(tmp_path, sample_transactions):
    file_path = tmp_path / "test_operations.xlsx"
    df = pd.DataFrame(sample_transactions)
    df.to_excel(file_path, index=False)

    original_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "operations.xlsx")
    os.makedirs(os.path.dirname(original_path), exist_ok=True)
    os.rename(file_path, original_path)

    try:
        result = XLSX_file_read()
        assert isinstance(result, list)
        assert len(result) == 3
        assert result[0]["Номер карты"] == "1234"
    finally:
        if os.path.exists(original_path):
            os.remove(original_path)


def test_XLSX_file_read_file_not_found():
    result = XLSX_file_read()
    assert result == "Файл не найден"


def test_file_df_success(tmp_path, sample_transactions):
    file_path = tmp_path / "test_operations.xlsx"
    df = pd.DataFrame(sample_transactions)
    df.to_excel(file_path, index=False)

    original_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "operations.xlsx")
    os.makedirs(os.path.dirname(original_path), exist_ok=True)
    os.rename(file_path, original_path)

    try:
        result = file_df()
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3
    finally:
        if os.path.exists(original_path):
            os.remove(original_path)