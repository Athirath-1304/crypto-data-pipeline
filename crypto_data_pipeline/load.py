"""
load.py – Handles loading or post-processing of data (e.g., reading back Parquet files),
used as part of the crypto data pipeline.
"""

import pandas as pd
import pyarrow.parquet as pq

def load_parquet_file(filepath: str) -> pd.DataFrame:
    """
    Load a Parquet file and return a pandas DataFrame.

    Args:
        filepath (str): Path to the .parquet file.

    Returns:
        pd.DataFrame: Loaded DataFrame from the file.
    """
    return pq.read_table(filepath).to_pandas()
