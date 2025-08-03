# monitoring/web/app.py
"""
Flask web dashboard for fraud monitoring
"""
from flask import Flask, render_template, jsonify
import json
import pandas as pd
import os

app = Flask(__name__)
CLAIMS_FILE = os.path.join(os.path.dirname(__file__), '../../storage/claims.jsonl')

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/summary')
def summary():
    claims = []
    if os.path.exists(CLAIMS_FILE):
        with open(CLAIMS_FILE, 'r') as f:
            for line in f:
                claims.append(json.loads(line))
    df = pd.DataFrame(claims)
    total_claims = len(df)
    flagged_claims = int(df['flagged_for_review'].sum()) if 'flagged_for_review' in df else 0
    fraud_rate = flagged_claims / total_claims if total_claims else 0
    return jsonify({
        'total_claims': total_claims,
        'flagged_claims': flagged_claims,
        'fraud_rate': round(fraud_rate * 100, 2)
    })

@app.route('/api/trends')
def trends():
    claims = []
    if os.path.exists(CLAIMS_FILE):
        with open(CLAIMS_FILE, 'r') as f:
            for line in f:
                claims.append(json.loads(line))
    df = pd.DataFrame(claims)
    if 'timestamp' in df:
        df['date'] = pd.to_datetime(df['timestamp']).dt.date
        daily_counts = df.groupby('date').size().to_dict()
        daily_flagged = df[df['flagged_for_review']].groupby('date').size().to_dict()
        return jsonify({
            'daily_counts': daily_counts,
            'daily_flagged': daily_flagged
        })
    else:
        return jsonify({'daily_counts': {}, 'daily_flagged': {}})

if __name__ == '__main__':
    app.run(debug=True)
