# Crypto Data Pipeline 🚀

This project fetches live cryptocurrency data from the CoinGecko API, stores it as Parquet files, and uploads them to an AWS S3 data lake.

## 📌 Features

- Public API ingestion (CoinGecko)
- Daily snapshot of top 100 coins
- Saved locally as `.parquet`
- Auto-upload to AWS S3 bucket
- Modular pipeline (extract, load)
- Configurable with `.env`
- Fully GitHub-ready

## 🛠️ Technologies

- Python 3.10+
- pandas
- requests
- boto3
- pyarrow
- python-dotenv
- AWS S3

## 📂 Folder Structure


