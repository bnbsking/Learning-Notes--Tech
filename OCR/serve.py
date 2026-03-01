from fastapi import FastAPI, File, UploadFile

from ocr.easy_ocr.main import EasyOCR


app = FastAPI()


@app.post("/easy_ocr")
def easy_ocr(file: UploadFile = File(...)) -> str:
    ocr = EasyOCR()
    text = ocr.run(pdf_bytes=file.file.read())
    return text
