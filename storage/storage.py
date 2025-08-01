# storage/storage.py
from typing import Dict, Any
import json
import os
from datetime import datetime

STORAGE_PATH = 'storage/claims.jsonl'

def store_claim(claim: Dict[str, Any]) -> None:
    """
    Stores claim data in a JSON Lines file for auditing and retraining.
    Each claim is appended as a new line.
    """
    os.makedirs(os.path.dirname(STORAGE_PATH), exist_ok=True)
    claim_record = claim.copy()
    claim_record['timestamp'] = datetime.utcnow().isoformat()
    with open(STORAGE_PATH, 'a') as f:
        f.write(json.dumps(claim_record) + '\n')
