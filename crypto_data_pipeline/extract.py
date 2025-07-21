"""
extract.py – Extracts cryptocurrency market data from the CoinGecko API,
validates schema using Pandera, and stores it as a Parquet file locally
and in AWS S3.

This module is intended to be scheduled and run as part of an Airflow DAG.
"""

import logging
import os
from datetime import datetime

import boto3
import pandas as pd
import pandera as pa
import pyarrow as pa
import pyarrow.parquet as pq
import requests
from schema import crypto_schema

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)


def fetch_crypto_data():
    """
    Fetch top 10 cryptocurrencies by market cap from CoinGecko API,
    validate schema, save to Parquet file locally, and upload to S3.

    Returns:
        str: Local file path of the saved Parquet file.
    Raises:
        requests.exceptions.RequestException: If API request fails.
        ValueError: If schema validation fails.
    """

    # Step 1: Fetch data
    logging.info("📡 Fetching crypto data from CoinGecko API...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data)[
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "total_volume",
            "high_24h",
            "low_24h",
            "price_change_24h",
            "price_change_percentage_24h",
            "last_updated",
        ]
    ]

    # Step 2: Validate schema
    try:
        df = crypto_schema.validate(df)
        logging.info("✅ Schema validation passed.")
    except pa.errors.SchemaError as e:
        logging.error("❌ Schema validation failed!")
        logging.error(e)
        raise

    # Step 3: Save to local Parquet file
    os.makedirs("crypto_data_pipeline/data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"crypto_data_pipeline/data/crypto_data_{timestamp}.parquet"
    table = pa.Table.from_pandas(df, preserve_index=False)
    pq.write_table(table, filename)
    logging.info(f"💾 Data saved to {filename}")

    # Step 4: Upload to S3
    s3 = boto3.client("s3")
    bucket_name = "athirath-crypto-data-lake"
    s3_key = f"crypto-data/{os.path.basename(filename)}"

    logging.info(f"☁️ Uploading to s3://{bucket_name}/{s3_key}...")
    s3.upload_file(Filename=filename, Bucket=bucket_name, Key=s3_key)
    logging.info(f"✅ Upload successful: {s3_key}")

    # Step 5: Upload _SUCCESS marker file (optional)
    success_key = f"crypto-data/_SUCCESS"
    logging.info(f"☑️ Uploading _SUCCESS marker to s3://{bucket_name}/{success_key}...")
    s3.put_object(Bucket=bucket_name, Key=success_key, Body="")
    logging.info("✅ _SUCCESS file uploaded.")

    return filename
