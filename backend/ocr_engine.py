import easyocr
import logging

# Initialize reader only once to save RAM.
# 'en' = English, 'hi' = Hindi (Crucial for Tier 2/3 India context)
# gpu=False ensures it runs on any laptop during the hackathon (CPU mode).
print("Loading OCR Model... this may take a moment.")
reader = easyocr.Reader(['en', 'hi'], gpu=False)

def extract_text(image_path: str) -> str:
    """
    Reads text from the image using EasyOCR.
    Returns a single string of all text found.
    """
    try:
        # detail=0 returns just the list of text strings found
        result = reader.readtext(image_path, detail=0)

        # Join them into one block of text for easier searching
        full_text = " ".join(result)
        return full_text
    except Exception as e:
        logging.error(f"OCR Failed: {str(e)}")
        return ""