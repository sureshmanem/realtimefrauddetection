
## Project Prompt
Build an AI-powered real-time insurance fraud detection engine with the following requirements:

- Accept insurance claim submissions via a REST API (FastAPI).
- Preprocess and normalize claim data before analysis.
- Apply rule-based logic to flag claims (e.g., high amount, missing details).
- Use a machine learning model to assign a fraud score to each claim.
- Flag claims for review if either rules or ML model indicate suspicion.
- Log flagged claims for audit and investigation.
- Store all claims in a JSONL file for easy retrieval and analysis.
- Provide robust, parameterized testing using pytest and CSV data, with HTML reporting.
- Implement monitoring dashboards (CLI and web) to visualize claim volumes, flagged claims, and fraud rates over time.
- Organize the codebase into clear modules: API, preprocessing, rules, ML, decision, review, storage, monitoring, and testing.
- Support easy customization for new rules, model updates, and dashboard features.

Deliverables:
- Complete Python codebase with modular structure.
- Example test data and test suite.
- CLI and web dashboards for monitoring.
- Documentation (README.md) and setup instructions.

# Real-Time Insurance Fraud Detection Engine

## Overview
This project is an AI-powered, modular system for real-time insurance claim fraud detection. It combines rule-based logic and machine learning to flag suspicious claims, supports robust testing, and provides monitoring and review capabilities.

## Features
- **API Layer:** FastAPI-based REST API for claim submission and integration.
- **Preprocessing:** Cleans and normalizes claim data before analysis.
- **Rule Engine:** Flags claims based on business rules (e.g., high amount, missing details).
- **ML Model:** Assigns a fraud score using a variable seed for realistic variability. Easily replaceable with a trained model.
- **Decision Engine:** Flags claims if either rules or ML model indicate suspicion.
- **Review System:** Logs flagged claims for audit and investigation.
- **Storage:** Stores claims in JSONL format for easy retrieval and analysis.
- **Testing:** Parameterized tests using pytest and CSV data, with HTML reporting.
- **Monitoring:** Dashboard for real-time and historical claim/fraud trends (CLI and web options).

## Project Structure
```
realtimefrauddetection/
├── api/                # API layer (FastAPI)
├── preprocessing/      # Data cleaning and normalization
├── rules/              # Rule engine
├── ml/                 # ML model logic
├── decision/           # Decision engine
├── review/             # Review system and logs
├── storage/            # Data storage (claims.jsonl)
├── monitoring/         # Monitoring dashboard (CLI and web)
├── testingapp/         # All testing files (tests, testdata, reports)
├── README.md           # Project documentation
└── ...                 # Other config and support files
```

## Getting Started
### 1. Backend Setup
- Create and activate a Python virtual environment:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- Start the API:
  ```bash
  uvicorn api.main:app --reload
  ```

### 2. Frontend Setup
- Navigate to the `frontend` folder:
  ```bash
  cd frontend
  npm install
  npm start
  ```
- Open [http://localhost:3000](http://localhost:3000) in your browser.

### 3. Monitoring Dashboard (CLI)
- Run the CLI dashboard:
  ```bash
  python monitoring/dashboard.py
  ```

### 4. Monitoring Dashboard (Web)
- Run the Flask web dashboard:
  ```bash
  pip install flask pandas
  python monitoring/web/app.py
  ```
- Open [http://localhost:5000](http://localhost:5000) in your browser.

### 5. Testing
- All tests and test data are in the `testingapp` folder.
- Run tests:
  ```bash
  pytest testingapp/api/test_api.py --html=testingapp/report.html --self-contained-html
  ```

## Model Training & Usage
- Train a fraud detection model using your data (e.g., scikit-learn, XGBoost).
- Save the model as `ml/fraud_model.pkl`.
- Update `ml/model.py` to load and use your trained model for predictions.

## Logs & Review
- Flagged claims are logged in `review/flagged_claims.log` for audit and investigation.

## Customization
- Add new rules in `rules/rule_engine.py`.
- Replace the ML logic in `ml/model.py` with your own model.
- Extend the dashboard for more analytics or alerts.

## License
MIT

---
For questions or enhancements, contact the project owner or open an issue.
