# easy_ocr.py
import easyocr
from PIL import Image
import numpy as np

reader = easyocr.Reader(['en'])

def extract_text_easyocr(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")
    image_np = np.array(image)
    result = reader.readtext(image_np)
    extracted_text = " ".join([text for _, text, _ in result])
    return extracted_text
