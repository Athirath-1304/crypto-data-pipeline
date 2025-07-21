import pandera as pa
from pandera import Column, DataFrameSchema

crypto_schema = DataFrameSchema({
    "id": Column(pa.String),
    "symbol": Column(pa.String),
    "name": Column(pa.String),
    "current_price": Column(pa.Float),
    "market_cap": Column(pa.Float, nullable=True),
    "market_cap_rank": Column(pa.Int, nullable=True),
    "total_volume": Column(pa.Float, nullable=True),
    "high_24h": Column(pa.Float, nullable=True),
    "low_24h": Column(pa.Float, nullable=True),
    "price_change_24h": Column(pa.Float, nullable=True),
    "price_change_percentage_24h": Column(pa.Float, nullable=True),
    "circulating_supply": Column(pa.Float, nullable=True),
    "total_supply": Column(pa.Float, nullable=True),
    "max_supply": Column(pa.Float, nullable=True),
    "ath": Column(pa.Float, nullable=True),
    "atl": Column(pa.Float, nullable=True),
    "last_updated": Column(pa.String)
})
