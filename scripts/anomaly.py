import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/processed/merged_features.csv")

# Select features for anomaly detection (fill NaNs just in case)
X = df[["amount", "time_diff", "rolling_std", "kyc_score"]].fillna(0)

clf = IsolationForest(contamination=0.1, random_state=42)
df["anomaly_flag"] = clf.fit_predict(X) == -1

df.to_csv("data/processed/anomalies.csv", index=False)
print("Anomaly detection complete - anomalies.csv saved.")
