# preprocessing/preprocessing.py
from typing import Any

def preprocess_claim(claim: Any) -> dict:
    """
    Cleans and normalizes claim data.
    - Strips whitespace from string fields
    - Ensures claim_type is lowercase
    - Validates amount is non-negative
    """
    claim_dict = claim.dict() if hasattr(claim, 'dict') else dict(claim)
    claim_dict['claim_id'] = claim_dict['claim_id'].strip()
    claim_dict['claim_type'] = claim_dict['claim_type'].strip().lower()
    claim_dict['claimant_name'] = claim_dict['claimant_name'].strip()
    claim_dict['claimant_id'] = claim_dict['claimant_id'].strip()
    claim_dict['details'] = claim_dict.get('details', '').strip() if claim_dict.get('details') else None
    if claim_dict['amount'] < 0:
        claim_dict['amount'] = 0.0
    return claim_dict
