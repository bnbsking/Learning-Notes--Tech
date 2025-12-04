from paddleocr import PaddleOCR
from pdf2image import convert_from_path
import os

# Initialize PaddleOCR
ocr = PaddleOCR(lang='en')  # English

# Folder with PDFs
pdf_path = "/app/_data/receipt.pdf"

# Convert PDF to images
pages = convert_from_path(pdf_path, dpi=300)

for i, page in enumerate(pages):
    print(f"--- Page {i+1} ---")
    
    # Save PIL image temporarily as PNG
    img_path = f"/tmp/page_{i+1}.png"
    page.save(img_path)
    
    # Run OCR
    result = ocr.predict(img_path)
    
    # Print detected text
    for res in result:
        # Access recognized text and confidence
        rec_texts = res['rec_texts']
        rec_scores = res['rec_scores']

        for text, score in zip(rec_texts, rec_scores):
            print(f"{text} (confidence: {score:.2f})")

        # Remove temporary image
        os.remove(img_path)

"""
STORE (confidence: 1.00)
NAME (confidence: 1.00)
123 Sample Street, City, Country (confidence: 1.00)
Phone: (000) 123-4567 (confidence: 0.99)
RECEIPT (confidence: 1.00)
Date: 2025-12-04 (confidence: 1.00)
Receipt #: 00012345 (confidence: 1.00)
Item (confidence: 1.00)
Qty (confidence: 1.00)
Unit Price (confidence: 1.00)
Total (confidence: 1.00)
USB Cable (confidence: 1.00)
2 (confidence: 1.00)
$5.00 (confidence: 0.99)
$10.00 (confidence: 1.00)
Keyboard (confidence: 1.00)
1 (confidence: 0.81)
$25.00 (confidence: 1.00)
$25.00 (confidence: 1.00)
Notebook (confidence: 1.00)
3 (confidence: 1.00)
$2.50 (confidence: 1.00)
$7.50 (confidence: 1.00)
Subtotal: $42.50 (confidence: 1.00)
Tax (5%): $2.13 (confidence: 1.00)
Total: $44.63 (confidence: 1.00)
Thank you for your purchase! (confidence: 1.00)
"""