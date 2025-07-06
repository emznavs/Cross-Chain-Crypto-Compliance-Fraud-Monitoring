import pandas as pd
import numpy as np

# Load raw data with timestamps parsed
ev = pd.read_csv("data/raw/user_events.csv", parse_dates=["timestamp"])
tx = pd.read_csv("data/raw/onchain_txns.csv", parse_dates=["block_time"])

# Merge user events and onchain transactions approximately by user and timestamp (nearest within 30s)
merged = pd.merge_asof(
    ev.sort_values("timestamp"),
    tx.sort_values("block_time"),
    left_on="timestamp",
    right_on="block_time",
    by="user_id",
    tolerance=pd.Timedelta("30s"),
    direction="nearest"
)

# Feature engineering
merged["hour"] = merged["timestamp"].dt.hour
merged["weekday"] = merged["timestamp"].dt.dayofweek
merged["time_diff"] = (merged["block_time"] - merged["timestamp"]).dt.total_seconds()
merged["device_reuse_ratio"] = merged.groupby("device_id")["user_id"].transform("nunique") / merged["device_id"].count()
merged["kyc_score"] = np.random.uniform(0, 1, size=len(merged))  # Placeholder for KYC scoring
merged["rolling_std"] = merged.groupby("user_id")["amount"].transform(lambda x: x.rolling(3, min_periods=1).std())

# Fill NaNs in rolling_std (first few rows per user)
merged["rolling_std"] = merged["rolling_std"].fillna(0)


merged.to_csv("data/processed/merged_features.csv", index=False)
print("Features engineering complete - merged_features.csv saved.")
