# rules/rule_engine.py
from typing import Dict, Any

def apply_rules(claim: Dict[str, Any]) -> Dict[str, Any]:
    """
    Applies rule-based checks to the claim.
    Flags suspicious claims based on simple rules:
    - High claim amount (> $10,000)
    - Missing details
    - Duplicate claim_id (placeholder, needs DB/storage)
    """
    flags = []
    if claim['amount'] > 10000:
        flags.append('high_amount')
    if not claim.get('details'):
        flags.append('missing_details')
    # Placeholder for duplicate check
    # if is_duplicate(claim['claim_id']):
    #     flags.append('duplicate_claim_id')
    claim['rule_flags'] = flags
    claim['is_suspicious'] = bool(flags)
    return claim
