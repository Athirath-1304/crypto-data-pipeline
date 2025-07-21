import pytest
import os
from crypto_data_pipeline import extract  # ✅ This is correct based on your structure

def test_fetch_crypto_data_runs():
    """
    Smoke test to verify fetch_crypto_data() executes without errors
    and returns a valid .parquet file path.
    """
    output_path = extract.fetch_crypto_data()
    assert output_path.endswith(".parquet")
    assert os.path.exists(output_path)
