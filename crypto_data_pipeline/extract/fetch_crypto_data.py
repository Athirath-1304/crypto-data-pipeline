import requests
import pandas as pd
import os
from datetime import datetime

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"crypto_data_{timestamp}.parquet"
    output_path = os.path.join("crypto_data_pipeline", "data", filename)

    # ✅ Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_parquet(output_path, index=False)

    print(f"✅ Data saved to {output_path}")
    return output_path  # Needed if test expects it

