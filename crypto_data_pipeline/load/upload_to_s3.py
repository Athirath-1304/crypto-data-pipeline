import boto3
import logging
import os

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def upload_to_s3(file_path, bucket_name, s3_key):
    logger.info(f"Uploading {file_path} to s3://{bucket_name}/{s3_key}...")

    s3 = boto3.client("s3")

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        logger.info(f"✅ Upload successful: {s3_key}")
    except Exception as e:
        logger.error(f"❌ Upload failed: {e}")
        raise
