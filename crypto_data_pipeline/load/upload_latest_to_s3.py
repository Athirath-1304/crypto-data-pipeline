import os
from glob import glob

import boto3


def get_latest_parquet_file(folder):
    files = glob(os.path.join(folder, "*.parquet"))
    if not files:
        raise FileNotFoundError("No parquet files found.")
    return max(files, key=os.path.getctime)


def upload_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"✅ Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")


if __name__ == "__main__":
    bucket = "athirath-crypto-data-lake"
    data_dir = "crypto_data_pipeline/data"

    latest_file = get_latest_parquet_file(data_dir)
    s3_key = f"crypto-data/{os.path.basename(latest_file)}"

    upload_to_s3(latest_file, bucket, s3_key)
