import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.abspath("."))  # Add current folder to Python path
load_dotenv()

from crypto_data_pipeline.extract.fetch_crypto_data import fetch_crypto_data
from crypto_data_pipeline.load.upload_latest_to_s3 import upload_to_s3, get_latest_parquet_file

def main():
    print("🚀 Fetching crypto data from CoinGecko...")
    fetch_crypto_data()

    print("📂 Getting latest .parquet file...")
    data_dir = os.getenv("DATA_DIR")
    latest_file = get_latest_parquet_file(data_dir)

    print("☁️ Uploading to S3...")
    bucket = os.getenv("BUCKET_NAME")
    prefix = os.getenv("S3_PREFIX")
    s3_key = f"{prefix}/{os.path.basename(latest_file)}"
    upload_to_s3(latest_file, bucket, s3_key)

    print("✅ Pipeline complete.")

if __name__ == "__main__":
    main()
