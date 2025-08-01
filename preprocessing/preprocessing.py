# preprocessing/preprocessing.py
from typing import Any

def preprocess_claim(claim: Any) -> dict:
    """
    Cleans and normalizes claim data.
    - Strips whitespace from string fields
    - Ensures claim_type is lowercase
    - Validates amount is non-negative
    """
    if hasattr(claim, 'model_dump'):
        claim_dict = claim.model_dump()
    elif hasattr(claim, 'dict'):
        claim_dict = claim.dict()
    else:
        claim_dict = dict(claim)
    claim_dict['claim_id'] = claim_dict['claim_id'].strip()
    claim_dict['claim_type'] = claim_dict['claim_type'].strip().lower()
    claim_dict['claimant_name'] = claim_dict['claimant_name'].strip()
    claim_dict['claimant_id'] = claim_dict['claimant_id'].strip()
    claim_dict['details'] = claim_dict.get('details', '').strip() if claim_dict.get('details') else None
    if claim_dict['amount'] < 0:
        claim_dict['amount'] = 0.0
    return claim_dict
