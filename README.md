# Crypto Data Pipeline 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Airflow](https://img.shields.io/badge/Airflow-Orchestrated-green)
![License](https://img.shields.io/badge/License-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/Athirath-1304/crypto-data-pipeline)
![CI](https://github.com/Athirath-1304/crypto-data-pipeline/actions/workflows/python-ci.yml/badge.svg)

---

A production-ready data engineering pipeline that ingests live cryptocurrency data from the [CoinGecko API](https://www.coingecko.com/), validates its schema, saves it as Parquet files, and uploads it to an AWS S3 data lake. The entire workflow is orchestrated using Apache Airflow and modularized for maintainability. A Streamlit dashboard provides a visual view of the crypto data with filters and time-based trends.

---

## 📌 Key Features

- ⛽ **Ingestion:** Live data from CoinGecko API (top 100 coins)  
- ✅ **Schema Validation:** Ensures structured, consistent data  
- 📀 **Storage:** Saves data locally as `.parquet` files  
- ☁️ **Cloud Upload:** Automatically uploads to AWS S3  
- ⚙️ **Orchestration:** Apache Airflow DAG handles full flow  
- 🔀 **Modular Design:** Split into extract, validate, load stages  
- 📊 **Streamlit Dashboard:** Visual insights with filters + trends  
- 🔐 **Configurable:** Use `.env` for keys and bucket names  

---

## 🛠️ Tech Stack

- **Python 3.10+**  
- **Apache Airflow** for orchestration  
- `pandas`, `requests`, `boto3`, `pyarrow`, `python-dotenv`  
- **AWS S3** for cloud storage  
- **Streamlit** for visualization  

---

## 🧱 Architecture

This project follows a modular pattern and uses Airflow for daily orchestration:

![Crypto Data Pipeline Architecture](assets/pipeline_architecture.png)

---

## 🔧 Local Setup & Demo

```bash
# 📦 Install dependencies
pip install -r requirements.txt

# 🔐 Set up environment variables
# Create a .env file in the root directory with the following content:
echo "AWS_ACCESS_KEY_ID=your_access_key" >> .env
echo "AWS_SECRET_ACCESS_KEY=your_secret_key" >> .env
echo "S3_BUCKET_NAME=athirath-crypto-data-lake" >> .env

# 🧪 Quick Local Demo (No AWS Required)

# Step 1: Disable S3 Upload
# In crypto_data_pipeline/dags/crypto_pipeline_dag.py, comment out the upload_to_s3 line:
# upload_to_s3(df, s3_bucket, filename)

# Step 2: Start Airflow
airflow standalone

# Step 3: Trigger the DAG manually
# Open Airflow UI at http://localhost:8080
# Enable and trigger the DAG: crypto_pipeline_dag

# Step 4: Check generated .parquet files
ls crypto_data_pipeline/data/

# 📊 Streamlit Dashboard

# Run the dashboard
streamlit run app.py

# Access dashboard at:
# http://localhost:8501
# Use the sidebar to:
# - View Top Gainers
# - View Top Losers
# - Filter by coin
# - View price trends and market caps
```

---

## 📂 Folder Structure

```bash
crypto-data-pipeline/
├── crypto_data_pipeline/
│   ├── dags/                 # Airflow DAGs
│   ├── data/                 # Local Parquet data files
│   ├── extract/              # API ingestion logic
│   ├── load/                 # AWS S3 upload logic
│   ├── schema/               # Schema validation
│   └── ...
├── app.py                   # Streamlit dashboard
├── requirements.txt
├── .env
├── README.md
└── ...
```

---

## 📌 Status

🟢 **Stable** — tested with local DAGs and dashboard.

---

## ✅ Next Goals

- [ ] Add unit tests  
- [ ] Integrate AWS Athena querying  
- [ ] Add GitHub Actions for CI/CD  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Connect

Built by **Athirath Bommerla**  
⭐ Star this repo if you found it helpful!

---

> Let me know if you want to add:
> - ✅ A **live demo badge**
> - 📹 A **GIF of the Streamlit dashboard**
> - ⚙️ **Auto-deploy instructions**
> 
> and I’ll help you plug that in too!
