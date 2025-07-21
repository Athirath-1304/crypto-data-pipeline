import os
import sys

# Set the root directory for consistent paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Append module paths for local imports
sys.path.append(BASE_DIR)

from extract.fetch_crypto_data import fetch_crypto_data
from load.upload_to_s3 import upload_to_s3

if __name__ == "__main__":
    print("📥 Fetching crypto data from CoinGecko...")
    fetch_crypto_data()

    print("📂 Getting latest .parquet file...")
    latest_file = max(
        [
            os.path.join(DATA_DIR, f)
            for f in os.listdir(DATA_DIR)
            if f.endswith(".parquet")
        ],
        key=os.path.getctime,
    )

    print("☁️ Uploading to S3...")
    upload_to_s3(
        file_path=latest_file,
        bucket_name="athirath-crypto-data-lake",
        s3_key=f"crypto-data/{os.path.basename(latest_file)}",
    )

    print("✅ Pipeline complete.")
