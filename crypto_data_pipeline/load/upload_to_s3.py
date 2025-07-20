import boto3
import os

def upload_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"✅ Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    bucket = "athirath-crypto-data-lake"  # Replace with your real bucket name
    local_file = "crypto_data_pipeline/data/crypto_data_20250720_180951.parquet"  # Replace with the exact file you saved
    s3_file = f"crypto-data/{os.path.basename(local_file)}"

    upload_to_s3(local_file, bucket, s3_file)

