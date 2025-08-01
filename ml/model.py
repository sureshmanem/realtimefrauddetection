# ml/model.py
from typing import Dict, Any
import random

def score_claim(claim: Dict[str, Any], seed: int = None) -> Dict[str, Any]:
    """
    Scores the claim for fraud probability using a variable seed (claim_id) for variability.

    ---
    Production Guidance:
    1. Train a real ML model (e.g., scikit-learn, XGBoost, TensorFlow) using historical claim data and fraud labels.
    2. Save the trained model to disk (e.g., with joblib for scikit-learn):
        import joblib
        joblib.dump(model, 'fraud_model.pkl')
    3. In production, load the model and preprocess incoming claims to match the model's expected input features:
        import joblib
        model = joblib.load('fraud_model.pkl')
        features = [...]  # Extract features from claim
        fraud_score = model.predict_proba([features])[0][1]
    4. Replace the random score logic below with your model's prediction.
    5. Remove or adjust the seed logic for true randomness or reproducibility as needed.
    ---
    """
    if seed is None:
        # Use claim_id as seed if available, else fallback to default
        seed = hash(str(claim.get('claim_id', 42)))
    random.seed(seed)
    fraud_score = random.uniform(0, 1)
    claim['fraud_score'] = fraud_score
    claim['ml_flagged'] = fraud_score > 0.8  # Example threshold
    return claim
