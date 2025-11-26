import React from 'react';
import UploadDoc from './components/UploadDoc';
import './App.css'; // Importing the new beautiful styles

function App() {
    return (
        <div className="App">
            <header className="navbar">
                <div className="brand">
                    <span style={{fontSize: '2rem'}}>🏠</span>
                    <h1>KirayaKawach AI</h1>
                </div>
                <p className="subtitle">Tier 2/3 Housing Fraud Prevention System</p>
            </header>

            <main className="main-container">
                <UploadDoc />
            </main>

            <footer style={{textAlign: 'center', padding: '20px', color: '#94a3b8', fontSize: '0.9rem'}}>
                <p>© 2024 MeraNivas Hackathon Project • Powered by Python & EasyOCR</p>
            </footer>
        </div>
    );
}

export default App;