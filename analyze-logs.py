import pandas as pd
from sklearn.ensemble import IsolationForest

# Load process logs
df = pd.read_csv("sample-data/process-logs.csv")

# Clean numeric features
features = df[["CPU", "WS"]].fillna(0)

# Train Isolation Forest for anomaly detection
model = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = model.fit_predict(features)

# Save anomalies
anomalies = df[df["anomaly"] == -1]
anomalies.to_csv("sample-data/anomalies.csv", index=False)

print("✅ Analysis complete. Found", len(anomalies), "suspicious processes.")
print("Results saved in sample-data/anomalies.csv")
