from typing import List

import easyocr
import numpy as np
from pdf2image import convert_from_bytes, convert_from_path

from ..base import BaseOCR


class EasyOCR(BaseOCR):
    def __init__(
            self,
            lang_list: List[str] = ['ch_tra', 'en'],
            model_storage_directory: str = "/app/models/easy_ocr/.EasyOCR",
        ):
        self.reader = easyocr.Reader(
            lang_list,
            model_storage_directory=model_storage_directory,
        )

    def run(self, pdf_bytes: bytes = None, pdf_path: str = "") -> str:
        assert (pdf_path and not pdf_bytes) or (pdf_bytes and not pdf_path)
        if pdf_bytes:
            pages = convert_from_bytes(pdf_bytes, dpi=300)
        else:  # pdf_path
            pages = convert_from_path(pdf_path, dpi=300)
        
        out = []
        for i, page in enumerate(pages):
            #print(f"--- Page {i+1} ---")
            img_np = np.array(page)
            result = self.reader.readtext(img_np)
            for (bbox, text, prob) in result:
                #print(f"{text} (confidence: {prob:.2f})")
                out.append(text)

        return "\n".join(out)
