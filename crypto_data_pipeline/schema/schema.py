import pandera as pa
from pandera import Column, DataFrameSchema
from pandera.dtypes import String, Float, DateTime, Int

coin_schema = DataFrameSchema({
    "id": Column(String),
    "symbol": Column(String),
    "name": Column(String),
    "current_price": Column(Float),
    "market_cap": Column(Int),
    "total_volume": Column(Int),
    "high_24h": Column(Float),
    "low_24h": Column(Float),
    "price_change_24h": Column(Float),
    "price_change_percentage_24h": Column(Float),
    "last_updated": Column(DateTime),
})

