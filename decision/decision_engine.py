# decision/decision_engine.py
from typing import Dict, Any

def make_decision(claim: Dict[str, Any]) -> Dict[str, Any]:
    """
    Combines rule-based and ML model results to flag claims for review.
    Flags claim if either rule engine or ML model marks it as suspicious.
    """
    flagged_by_rule = claim.get('is_suspicious', False)
    flagged_by_ml = claim.get('ml_flagged', False)
    claim['flagged_for_review'] = flagged_by_rule or flagged_by_ml
    claim['flag_reason'] = []
    if flagged_by_rule:
        claim['flag_reason'].append('rule_engine')
    if flagged_by_ml:
        claim['flag_reason'].append('ml_model')
    return claim
