import pandera.pandas as pa  # ✅ Updated import to remove future warning
from pandera.pandas import Column, DataFrameSchema
from pandera.dtypes import Float64, String

crypto_schema = DataFrameSchema({
    "id": Column(String),
    "symbol": Column(String),
    "name": Column(String),
    "current_price": Column(Float64),
    "market_cap": Column(Float64, nullable=True, coerce=True),
    "total_volume": Column(Float64, nullable=True, coerce=True),
    "high_24h": Column(Float64, nullable=True, coerce=True),
    "low_24h": Column(Float64, nullable=True, coerce=True),
    "price_change_24h": Column(Float64, nullable=True, coerce=True),
    "price_change_percentage_24h": Column(Float64, nullable=True, coerce=True),
    "last_updated": Column(String)
})
