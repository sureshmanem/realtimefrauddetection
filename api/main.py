from fastapi import FastAPI, HTTPException
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
    # Placeholder: Pass claim to preprocessing/rule engine
    # For now, just echo back the claim
    return {"status": "received", "claim": claim}

# To run: uvicorn main:app --reload
