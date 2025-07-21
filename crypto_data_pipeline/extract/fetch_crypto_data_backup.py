import requests
import pandas as pd
import os
from datetime import datetime
import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }

    logger.info("Requesting data from CoinGecko API...")
    response = requests.get(url, params=params)
    if response.status_code != 200:
        logger.error(f"Failed to fetch data. Status code: {response.status_code}")
        raise Exception("API request failed.")

    data = response.json()
    df = pd.DataFrame(data)

    # Ensure output folder exists
    output_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    # Filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"crypto_data_{timestamp}.parquet")

    df.to_parquet(output_path, index=False)
    logger.info(f"Data saved to {output_path}")
