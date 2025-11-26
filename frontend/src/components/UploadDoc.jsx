import React, { useState } from 'react';
import axios from 'axios';

const UploadDoc = () => {
    const [file, setFile] = useState(null);
    const [name, setName] = useState("");
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [previewUrl, setPreviewUrl] = useState(null);

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
        if (selectedFile) {
            setFile(selectedFile);
            setPreviewUrl(URL.createObjectURL(selectedFile));
        }
    };

    const handleUpload = async () => {
        if (!file || !name) {
            alert("Please enter a name and select a file!");
            return;
        }

        setLoading(true);
        setResult(null);

        const formData = new FormData();
        formData.append("file", file);
        formData.append("expected_name", name);

        try {
            const response = await axios.post("http://localhost:8000/verify", formData);
            setResult(response.data);
        } catch (error) {
            console.error("Upload error:", error);
            alert("Failed to connect to backend. Is Python running?");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="glass-card">
            <h2 className="section-title">📄 Verify Tenant Document</h2>

            {/* Input Section */}
            <div className="input-group">
                <label className="input-label">Expected Tenant Name</label>
                <input
                    type="text"
                    className="modern-input"
                    placeholder="e.g. Rahul Sharma"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>

            <div className="input-group">
                <label className="input-label">Upload ID / Rent Agreement</label>
                <div className="drop-zone" onClick={() => document.getElementById('fileInput').click()}>
                    <input
                        id="fileInput"
                        type="file"
                        onChange={handleFileChange}
                        accept="image/*"
                        style={{display: 'none'}}
                    />
                    <div className="upload-icon">☁️</div>
                    <p style={{margin: 0}}>Click to upload document image</p>
                    {file && <div className="file-info">Selected: {file.name}</div>}
                </div>
            </div>

            {previewUrl && (
                <div style={{textAlign: 'center', marginBottom: '1.5rem'}}>
                    <img
                        src={previewUrl}
                        alt="Preview"
                        style={{maxWidth: '100%', maxHeight: '200px', borderRadius: '8px', border: '1px solid #e2e8f0'}}
                    />
                </div>
            )}

            <button className="primary-btn" onClick={handleUpload} disabled={loading}>
                {loading ? <><span className="spinner"></span> Analyzing...</> : "Verify Document Now"}
            </button>

            {/* Results Section */}
            {result && (
                <div className={`result-box risk-${result.risk_level.toLowerCase()}`}>
                    <div className="result-header">
                        <div>
                            <span style={{opacity: 0.8, fontSize: '0.9rem', textTransform: 'uppercase'}}>Risk Level</span>
                            <h2 style={{margin: 0}}>{result.risk_level} RISK</h2>
                        </div>
                        <div style={{fontSize: '2rem'}}>
                            {result.risk_level === 'LOW' ? '✅' : result.risk_level === 'MEDIUM' ? '⚠️' : '🚨'}
                        </div>
                    </div>

                    <div className="result-body">
                        <p style={{fontSize: '1.1rem', fontWeight: 500, margin: '0 0 1rem 0'}}>
                            Verdict: {result.message}
                        </p>

                        <div className="score-grid">
                            <div className="score-card">
                <span className="score-value" style={{color: result.details.is_tampered === 'True' ? '#ef4444' : '#10b981'}}>
                  {result.details.forgery_score}
                </span>
                                <span className="score-label">Forgery Probability</span>
                            </div>
                            <div className="score-card">
                                <span className="score-value">{result.details.name_match_score}</span>
                                <span className="score-label">Name Match</span>
                            </div>
                        </div>

                        <details style={{marginTop: '1rem', color: '#64748b', fontSize: '0.9rem', cursor: 'pointer'}}>
                            <summary>View Extracted Text</summary>
                            <p style={{padding: '10px', background: '#f1f5f9', borderRadius: '6px', marginTop: '5px'}}>
                                {result.extracted_text_snippet}
                            </p>
                        </details>
                    </div>
                </div>
            )}
        </div>
    );
};

export default UploadDoc;