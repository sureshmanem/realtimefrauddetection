# ml/model.py
from typing import Dict, Any
import random

def score_claim(claim: Dict[str, Any], seed: int = 42) -> Dict[str, Any]:
    """
    Scores the claim for fraud probability using a fixed random seed for deterministic results.
    Replace with actual model inference logic (e.g., load a trained model).
    """
    random.seed(seed)
    fraud_score = random.uniform(0, 1)
    claim['fraud_score'] = fraud_score
    claim['ml_flagged'] = fraud_score > 0.7  # Example threshold
    return claim
