import logging
import os
from datetime import datetime, timezone

import boto3
import pandas as pd
import pandera.pandas as pda  # ✅ avoid naming conflict
import pyarrow as pa
import pyarrow.parquet as pq
import requests

from crypto_data_pipeline.schema.crypto_schema import crypto_schema

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)


def fetch_crypto_data():
    logging.info("📥 Fetching crypto data from CoinGecko...")
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

    # ✅ Schema validation using Pandera
    try:
        df = crypto_schema.validate(df, lazy=True)
        logging.info("✅ Schema validation passed.")
    except pda.errors.SchemaError as e:
        logging.error("❌ Schema validation failed!")
        logging.error(e)
        raise

    # 💾 Save to local Parquet
    os.makedirs("crypto_data_pipeline/data", exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"crypto_data_pipeline/data/crypto_data_{timestamp}.parquet"
    table = pa.Table.from_pandas(df, preserve_index=False)
    pq.write_table(table, filename)
    logging.info(f"✅ Data saved to {filename}")

    # ☁️ Upload to S3
    s3 = boto3.client("s3")
    bucket_name = "athirath-crypto-data-lake"
    s3_key = f"crypto-data/{os.path.basename(filename)}"
    logging.info(f"Uploading {filename} to s3://{bucket_name}/{s3_key}...")
    s3.upload_file(Filename=filename, Bucket=bucket_name, Key=s3_key)
    logging.info(f"✅ Upload successful: {s3_key}")

    # ✅ Upload _SUCCESS file
    success_key = f"crypto-data/_SUCCESS"
    logging.info(
        f"Uploading empty _SUCCESS file to s3://{bucket_name}/{success_key}..."
    )
    s3.put_object(Bucket=bucket_name, Key=success_key, Body="")
    logging.info("✅ _SUCCESS file uploaded.")

    return filename
