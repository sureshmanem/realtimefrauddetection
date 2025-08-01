from fastapi import FastAPI, HTTPException
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../preprocessing')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../rules')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ml')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../decision')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../review')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../storage')))
try:
    from preprocessing import preprocess_claim
except ImportError:
    def preprocess_claim(claim):
        # Placeholder: actual preprocessing logic will be implemented in preprocessing layer
        return claim
try:
    from rule_engine import apply_rules
except ImportError:
    def apply_rules(claim):
        # Placeholder: actual rule logic will be implemented in rule engine layer
        return claim
try:
    from model import score_claim
except ImportError:
    def score_claim(claim):
        # Placeholder: actual ML logic will be implemented in ML layer
        return claim
try:
    from decision_engine import make_decision
except ImportError:
    def make_decision(claim):
        # Placeholder: actual decision logic will be implemented in decision engine layer
        return claim
try:
    from review_system import notify_investigator
except ImportError:
    def notify_investigator(claim):
        # Placeholder: actual review logic will be implemented in review system layer
        pass
try:
    from storage import store_claim
except ImportError:
    def store_claim(claim):
        # Placeholder: actual storage logic will be implemented in storage layer
        pass
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Claim(BaseModel):
    claim_id: str
    claim_type: str  # e.g., 'auto', 'health'
    amount: float
    claimant_name: str
    claimant_id: str
    details: Optional[str] = None

@app.post("/claims")
def submit_claim(claim: Claim):
    processed_claim = preprocess_claim(claim)
    ruled_claim = apply_rules(processed_claim)
    scored_claim = score_claim(ruled_claim)
    decision_claim = make_decision(scored_claim)
    notify_investigator(decision_claim)
    store_claim(decision_claim)
    return {"status": "received", "claim": decision_claim}

# To run: uvicorn main:app --reload
