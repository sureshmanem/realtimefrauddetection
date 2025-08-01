# monitoring/dashboard.py
"""
Fraud Detection Monitoring Dashboard
- Real-time visualization of claim volumes, flagged claims, and fraud rates.
- Trends over time (daily/weekly/monthly).
"""

import json
from datetime import datetime
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import pandas as pd

CLAIMS_FILE = 'storage/claims.jsonl'

def load_claims():
    claims = []
    with open(CLAIMS_FILE, 'r') as f:
        for line in f:
            claims.append(json.loads(line))
    return claims

def dashboard_summary():
    claims = load_claims()
    df = pd.DataFrame(claims)
    total_claims = len(df)
    flagged_claims = df['flagged_for_review'].sum() if 'flagged_for_review' in df else 0
    fraud_rate = flagged_claims / total_claims if total_claims else 0
    print(f"Total claims: {total_claims}")
    print(f"Flagged for review: {flagged_claims}")
    print(f"Fraud rate: {fraud_rate:.2%}")
    return df

def plot_trends(df):
    if 'timestamp' in df:
        df['date'] = pd.to_datetime(df['timestamp']).dt.date
        daily_counts = df.groupby('date').size()
        daily_flagged = df[df['flagged_for_review']].groupby('date').size()
        plt.figure(figsize=(10,5))
        plt.plot(daily_counts.index, daily_counts.values, label='Total Claims')
        plt.plot(daily_flagged.index, daily_flagged.values, label='Flagged Claims')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.title('Claims and Flagged Claims Over Time')
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("No timestamp data available for trend plotting.")

if __name__ == "__main__":
    df = dashboard_summary()
    plot_trends(df)
