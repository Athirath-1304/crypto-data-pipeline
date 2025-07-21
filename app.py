import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("📊 Crypto Data Viewer")

# Load .parquet files
data_dir = "crypto_data_pipeline/data/"
parquet_files = sorted([f for f in os.listdir(data_dir) if f.endswith(".parquet")])

if not parquet_files:
    st.error("❌ No data found. Please run the pipeline first.")
    st.stop()

dfs = []
for file in parquet_files:
    df = pd.read_parquet(os.path.join(data_dir, file))
    # Inject timestamp from filename if not in dataframe
    if "timestamp" not in df.columns:
        timestamp_str = file.replace("crypto_data_", "").replace(".parquet", "")
        df["timestamp"] = pd.to_datetime(timestamp_str, format="%Y%m%d_%H%M%S", errors="coerce")
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)

# Sidebar filters
st.sidebar.header("🔍 Filters")
view_option = st.sidebar.selectbox("View", ["All Coins", "Top Gainers (24h)", "Top Losers (24h)"])

if view_option == "Top Gainers (24h)":
    filtered_df = df_all[df_all['price_change_percentage_24h'] > 0].sort_values("price_change_percentage_24h", ascending=False).head(10)
elif view_option == "Top Losers (24h)":
    filtered_df = df_all[df_all['price_change_percentage_24h'] < 0].sort_values("price_change_percentage_24h").head(10)
else:
    filtered_df = df_all

st.dataframe(filtered_df, use_container_width=True)

# Bar chart for latest prices
if "timestamp" in df_all.columns:
    latest_df = df_all[df_all["timestamp"] == df_all["timestamp"].max()]
    st.subheader("💵 Current Prices (Latest Snapshot)")
    top_10 = latest_df.nlargest(10, 'market_cap')
    st.bar_chart(top_10.set_index("symbol")["current_price"])
else:
    st.warning("📛 No timestamp available to determine latest snapshot.")

# Time trend
if "timestamp" in df_all.columns:
    st.subheader("📅 Price Trend Over Time")
    coin_options = df_all["symbol"].unique().tolist()
    selected_coins = st.multiselect("Choose coins to show trend", coin_options, default=["btc", "eth"])

    trend_df = df_all[df_all["symbol"].isin(selected_coins)].sort_values("timestamp")
    trend_pivot = trend_df.pivot(index="timestamp", columns="symbol", values="current_price")
    st.line_chart(trend_pivot)
else:
    st.warning("⏳ Timestamp not found — cannot plot trend chart.")
