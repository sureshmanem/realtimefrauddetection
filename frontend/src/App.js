import React, { useState } from 'react';
import axios from 'axios';
import './style.css';

function App() {
    const [form, setForm] = useState({
        claim_id: '',
        claim_type: 'auto',
        amount: '',
        claimant_name: '',
        claimant_id: '',
        details: ''
    });
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleChange = e => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async e => {
        e.preventDefault();
        setLoading(true);
        setError('');
        setResult(null);
        try {
            const response = await axios.post('http://localhost:8000/claims', form);
            setResult(response.data.claim);
        } catch (err) {
            setError('Failed to submit claim. Is the backend running?');
        }
        setLoading(false);
    };

    return (
        <div className="container">
            <h1>Insurance Fraud Detection Demo</h1>
            <form onSubmit={handleSubmit}>
                <label>Claim ID
                    <input name="claim_id" value={form.claim_id} onChange={handleChange} required />
                </label>
                <label>Claim Type
                    <select name="claim_type" value={form.claim_type} onChange={handleChange}>
                        <option value="auto">Auto</option>
                        <option value="health">Health</option>
                    </select>
                </label>
                <label>Amount
                    <input name="amount" type="number" value={form.amount} onChange={handleChange} required />
                </label>
                <label>Claimant Name
                    <input name="claimant_name" value={form.claimant_name} onChange={handleChange} required />
                </label>
                <label>Claimant ID
                    <input name="claimant_id" value={form.claimant_id} onChange={handleChange} required />
                </label>
                <label>Details
                    <textarea name="details" value={form.details} onChange={handleChange} rows={3} />
                </label>
                <button type="submit" disabled={loading}>{loading ? 'Checking...' : 'Submit Claim'}</button>
            </form>
            {error && <div className="result" style={{ background: '#ffebee', color: '#b71c1c' }}>{error}</div>}
            {result && (
                <div className="result">
                    <strong>Claim ID:</strong> {result.claim_id}<br />
                    <strong>Type:</strong> {result.claim_type}<br />
                    <strong>Amount:</strong> {result.amount}<br />
                    <strong>Suspicious:</strong> {result.is_suspicious ? 'Yes' : 'No'}<br />
                    <strong>Flagged for Review:</strong> {result.flagged_for_review ? 'Yes' : 'No'}<br />
                    <strong>Fraud Score:</strong> {result.fraud_score && result.fraud_score.toFixed(2)}<br />
                </div>
            )}
        </div>
    );
}

export default App;
