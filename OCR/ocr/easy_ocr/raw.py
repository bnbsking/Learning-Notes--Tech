import easyocr
from pdf2image import convert_from_path
import numpy as np

# Path to your PDF receipt
pdf_path = "/app/_data/receipt.pdf"

# Convert PDF to images
pages = convert_from_path(pdf_path, dpi=300)

# Initialize EasyOCR reader
reader = easyocr.Reader(
    ['ch_tra', 'en'],
    model_storage_directory="/app/models/easy_ocr/.EasyOCR",
)

# Run
for i, page in enumerate(pages):
    print(f"--- Page {i+1} ---")
    
    # Convert PIL Image to NumPy array
    img_np = np.array(page)
    
    # Run OCR
    result = reader.readtext(img_np)
    
    for (bbox, text, prob) in result:
        print(f"{text} (confidence: {prob:.2f})")
    

"""
STORE NAME (confidence: 1.00)
123 Sample Street; (confidence: 0.93)
Country (confidence: 1.00)
Phone: (000) 123-4567 (confidence: 0.99)
RECEIPT (confidence: 1.00)
...
"""
