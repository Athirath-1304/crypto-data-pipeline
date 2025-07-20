import os

def create_folders():
    base_dir = "crypto_data_pipeline"
    subdirs = [
        "extract",
        "transform",        # we'll use this later
        "load",             # for uploading to cloud
        "data",             # raw and processed data files
        "logs",             # logging output
        "dags",             # for Airflow DAGs if needed later
        "config",           # for config/env files
        "notebooks"         # optional: for quick data checks
    ]

    # Create base project folder
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    # Create subdirectories
    for sub in subdirs:
        path = os.path.join(base_dir, sub)
        os.makedirs(path, exist_ok=True)

    print("✅ Project folders created successfully!")

if __name__ == "__main__":
    create_folders()
