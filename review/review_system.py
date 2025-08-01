# review/review_system.py
from typing import Dict, Any
import logging

logging.basicConfig(filename='review/flagged_claims.log', level=logging.INFO)

def notify_investigator(claim: Dict[str, Any]) -> None:
    """
    Notifies human investigators about flagged claims.
    For now, logs flagged claims to a file. Replace with email, dashboard, or queue integration as needed.
    """
    if claim.get('flagged_for_review'):
        logging.info(f"Flagged claim for review: {claim}")
