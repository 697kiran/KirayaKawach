import cv2
import numpy as np
import os

def detect_tampering(image_path: str):
    """
    Performs Error Level Analysis (ELA) to find digital modifications.
    """
    try:
        # Read original image
        original = cv2.imread(image_path)
        if original is None:
            print(f"Error: Could not read image at {image_path}")
            return False, 0.0

        # 1. Create a compressed version in memory
        # We save it at 90% quality to generate artifacts
        _, encoded = cv2.imencode('.jpg', original, [cv2.IMWRITE_JPEG_QUALITY, 90])
        compressed = cv2.imdecode(encoded, cv2.IMREAD_COLOR)

        # 2. Calculate absolute difference (The "Error")
        diff = cv2.absdiff(original, compressed)

        # 3. Enhance the difference so we can see it
        diff_enhanced = cv2.convertScaleAbs(diff, alpha=20)

        # 4. Convert to grayscale to check intensity
        gray = cv2.cvtColor(diff_enhanced, cv2.COLOR_BGR2GRAY)

        # 5. Find the maximum pixel intensity difference
        max_diff = np.max(gray)

        # Threshold Logic
        is_forged = max_diff > 140
        confidence = min((max_diff / 255) * 100, 99.9)

        return is_forged, round(confidence, 2)

    except Exception as e:
        print(f"ELA Error: {e}")
        return False, 0.0