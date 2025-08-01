# api/test_api.py
import csv
import os
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def load_claims_from_csv():
    csv_path = os.path.join(os.path.dirname(__file__), '../testdata/claims.csv')
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        claims = []
        for row in reader:
            claim = {
                "claim_id": row["claim_id"],
                "claim_type": row["claim_type"],
                "amount": float(row["amount"]),
                "claimant_name": row["claimant_name"],
                "claimant_id": row["claimant_id"],
                "details": row["details"]
            }
            expected = {
                "expected_claim_id": row["expected_claim_id"],
                "expected_claim_type": row["expected_claim_type"],
                "expected_amount": float(row["expected_amount"]),
                "expected_is_suspicious": row["expected_is_suspicious"] == "True",
                "expected_flagged_for_review": row["expected_flagged_for_review"] == "True"
            }
            claims.append((claim, expected))
        return claims

@pytest.mark.parametrize("claim,expected", load_claims_from_csv())
def test_claim_pipeline_csv(claim, expected):
    response = client.post("/claims", json=claim)
    assert response.status_code == 200
    result = response.json()["claim"]
    assert result["claim_id"] == expected["expected_claim_id"]
    assert result["claim_type"] == expected["expected_claim_type"]
    assert result["amount"] == expected["expected_amount"]
    assert result["is_suspicious"] == expected["expected_is_suspicious"]
    assert result["flagged_for_review"] == expected["expected_flagged_for_review"]
