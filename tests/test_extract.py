import os
from crypto_data_pipeline.extract.fetch_crypto_data import fetch_crypto_data

def test_fetch_crypto_data_runs():
    """
    Smoke test to verify fetch_crypto_data() executes without errors
    and returns a valid .parquet file path.
    """
    output_path = fetch_crypto_data()
    assert output_path.endswith(".parquet")
    assert os.path.exists(output_path)

