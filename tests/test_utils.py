import pytest
import os
import shutil
import pandas as pd
from src.utils import XLSX_file_read, file_df


def test_XLSX_file_read_success(tmp_path, sample_transactions, clean_test_file):
    # Подготовка тестового файла
    test_file = tmp_path / "operations.xlsx"
    pd.DataFrame(sample_transactions).to_excel(test_file, index=False)

    # Копируем в папку data
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    os.makedirs(data_dir, exist_ok=True)
    shutil.copy(test_file, os.path.join(data_dir, "operations.xlsx"))

    # Тестируем
    result = XLSX_file_read()
    assert isinstance(result, list)
    assert len(result) > 0


def test_XLSX_file_read_file_not_found(monkeypatch):
    # Мокаем путь к несуществующему файлу
    monkeypatch.setattr("src.utils.os.path.join", lambda *args: "nonexistent_file.xlsx")
    assert XLSX_file_read() == "Файл не найден"


def test_file_df_success(tmp_path, sample_transactions, clean_test_file):
    # Подготовка тестового файла
    test_file = tmp_path / "operations.xlsx"
    pd.DataFrame(sample_transactions).to_excel(test_file, index=False)

    # Копируем в папку data
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    os.makedirs(data_dir, exist_ok=True)
    shutil.copy(test_file, os.path.join(data_dir, "operations.xlsx"))

    # Тестируем
    result = file_df()
    assert isinstance(result, pd.DataFrame)
    assert not result.empty


@pytest.fixture
def clean_test_file():
    """Фикстура для очистки тестового файла после выполнения тестов"""
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    test_file = os.path.join(data_dir, "operations.xlsx")
    yield
    if os.path.exists(test_file):
        os.remove(test_file)