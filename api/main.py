from fastapi import FastAPI, HTTPException
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../preprocessing')))
try:
    from preprocessing import preprocess_claim
except ImportError:
    def preprocess_claim(claim):
        # Placeholder: actual preprocessing logic will be implemented in preprocessing layer
        return claim
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
    # Placeholder: Pass processed_claim to rule engine next
    return {"status": "received", "claim": processed_claim}

# To run: uvicorn main:app --reload
