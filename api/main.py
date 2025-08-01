from fastapi import FastAPI, HTTPException
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../preprocessing')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../rules')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ml')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../decision')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../review')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../storage')))
from preprocessing import preprocess_claim
from rule_engine import apply_rules
from model import score_claim
from decision_engine import make_decision
from review_system import notify_investigator
from storage import store_claim
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
    scored_claim = score_claim(ruled_claim, seed=42)
    decision_claim = make_decision(scored_claim)
    notify_investigator(decision_claim)
    store_claim(decision_claim)
    return {"status": "received", "claim": decision_claim}

# To run: uvicorn main:app --reload
