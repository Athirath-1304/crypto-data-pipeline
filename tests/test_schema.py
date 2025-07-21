from crypto_data_pipeline.schema.schema import coin_schema

def test_coin_schema_fields():
    """
    Ensure required columns exist in the schema definition.
    """
    expected_columns = {
        "id", "symbol", "name", "current_price", "market_cap",
        "total_volume", "high_24h", "low_24h", "price_change_24h",
        "price_change_percentage_24h", "last_updated"
    }

    actual_columns = set(coin_schema.columns.keys())
    assert expected_columns.issubset(actual_columns)

