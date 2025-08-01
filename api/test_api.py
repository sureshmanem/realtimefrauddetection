# api/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_claim_pipeline():
    claim_data = {
        "claim_id": " 12345 ",
        "claim_type": "AUTO ",
        "amount": 15000,
        "claimant_name": " John Doe ",
        "claimant_id": " JD001 ",
        "details": "Accident on highway"
    }
    response = client.post("/claims", json=claim_data)
    assert response.status_code == 200
    result = response.json()["claim"]
    assert result["claim_id"] == "12345"
    assert result["claim_type"] == "auto"
    assert result["amount"] == 15000
    assert result["is_suspicious"] is True
    assert result["flagged_for_review"] is True
    assert "rule_engine" in result["flag_reason"]
    assert "ml_model" in result["flag_reason"] or not result["ml_flagged"]
    assert "fraud_score" in result
    print("Test passed. Pipeline output:", result)
