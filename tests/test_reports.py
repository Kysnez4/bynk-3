import pandas as pd
import pytest
from src.reports import spending_by_category

def test_spending_by_category(sample_df):
    result = spending_by_category(sample_df, "Еда", "2023-01-10")
    assert isinstance(result, pd.DataFrame)
    assert "Еда" in result.columns
    assert result["Еда"].iloc[0] < 0

def test_spending_by_category_default_date(sample_df):
    result = spending_by_category(sample_df, "Еда")
    assert isinstance(result, pd.DataFrame)