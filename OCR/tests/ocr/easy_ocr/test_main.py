import sys
sys.path.append("/app")
from ocr.easy_ocr.main import EasyOCR


class TestEasyOCR:
    def test_run_path(self):
        ocr = EasyOCR()
        text = ocr.run(pdf_path="/app/_data/receipt.pdf")
        print(text)

    def test_run_bytes(self):
        ocr = EasyOCR()
        with open("/app/_data/receipt.pdf", "rb") as f:
            pdf_bytes = f.read()
        text = ocr.run(pdf_bytes=pdf_bytes)
        print(text)


if __name__ == "__main__":
    test = TestEasyOCR()
    test.test_run_path()
    test.test_run_bytes()
