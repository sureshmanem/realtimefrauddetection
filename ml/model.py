# ml/model.py
from typing import Dict, Any
import random

def score_claim(claim: Dict[str, Any]) -> Dict[str, Any]:
    """
    Scores the claim for fraud probability using a placeholder ML model.
    Replace with actual model inference logic (e.g., load a trained model).
    """
    # Placeholder: random score for demonstration
    fraud_score = random.uniform(0, 1)
    claim['fraud_score'] = fraud_score
    claim['ml_flagged'] = fraud_score > 0.7  # Example threshold
    return claim
