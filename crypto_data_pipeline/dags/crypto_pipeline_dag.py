from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "athirath",
    "depends_on_past": False,
    "start_date": datetime(2025, 7, 20),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="crypto_pipeline_dag",
    default_args=default_args,
    description="A DAG to run crypto data pipeline",
    schedule_interval="@daily",  # runs every day at midnight
    catchup=False,
) as dag:

    run_crypto_pipeline = BashOperator(
        task_id="run_crypto_pipeline",
        bash_command="source airflow-venv/bin/activate && PYTHONPATH=$(pwd) python crypto_data_pipeline/main.py",
    )
