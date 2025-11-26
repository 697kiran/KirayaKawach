from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fuzzywuzzy import fuzz
import shutil
import os
import uuid

from ocr_engine import extract_text
from forgery_detect import detect_tampering
from models import VerificationResponse

app = FastAPI(title="MeraNivas AI Backend")

# CORS setup - Allows the React Frontend to talk to this Python Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Open for hackathon demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure uploads directory exists to prevent errors
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "MeraNivas AI System Operational"}

@app.post("/verify", response_model=VerificationResponse)
async def verify_document(file: UploadFile = File(...), expected_name: str = Form(...)):
    """
    Main Verification Pipeline:
    1. Save File -> 2. Check Forgery -> 3. Extract Text -> 4. Match Name -> 5. Return Score
    """

    # Generate unique filename to avoid conflicts if two users upload "doc.jpg"
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    try:
        # 1. Save file locally
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"Processing file: {file.filename} for tenant: {expected_name}")

        # 2. Run Forgery Detection (ELA)
        is_tampered, forgery_confidence = detect_tampering(file_path)

        # 3. Run OCR (Text Extraction)
        extracted_text = extract_text(file_path)

        # 4. Check Name Mismatch (Fuzzy Logic)
        # partial_ratio helps match "Rahul Kumar" with "Rahul K." or "Mr. Rahul Kumar"
        name_match_score = fuzz.partial_ratio(expected_name.lower(), extracted_text.lower())

        # 5. Calculate Risk Score
        risk = "LOW"
        msg = "Document Verified Successfully."

        if is_tampered:
            risk = "HIGH"
            msg = "Digital manipulation detected (ELA Analysis)."
        elif name_match_score < 70:
            risk = "MEDIUM"
            msg = f"Name mismatch. Found similar text with {name_match_score}% confidence."

        # 6. Return Response
        return VerificationResponse(
            filename=file.filename,
            risk_level=risk,
            message=msg,
            details={
                "forgery_score": f"{forgery_confidence}%",
                "name_match_score": f"{name_match_score}%",
                "is_tampered": str(is_tampered)
            },
            extracted_text_snippet=extracted_text[:100] + "..." # Snippet for debugging
        )

    except Exception as e:
        print(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Cleanup: Remove file after processing to save disk space
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)