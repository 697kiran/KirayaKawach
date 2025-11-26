from pydantic import BaseModel
from typing import Optional, Dict

class VerificationResponse(BaseModel):
    filename: str
    risk_level: str  # LOW, MEDIUM, HIGH
    message: str
    details: Dict[str, str]  # Stores scores like "95%"
    extracted_text_snippet: str

class ErrorResponse(BaseModel):
    error: str
    details: Optional[str] = None